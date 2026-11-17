"""Lógica del demostrador BiciPrevisión: cargar el modelo, validar la entrada y prever las 24 horas de un día. Sin interfaz."""
import json
import os

import joblib
import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar

CARPETA = os.path.dirname(os.path.abspath(__file__))
CLIMA = ["weathersit", "temp", "atemp", "hum", "windspeed"]
HORAS_PUNTA = (7, 8, 9, 17, 18, 19)
TIEMPOS = {1: "despejado", 2: "nublado o niebla", 3: "lluvia o nieve ligera", 4: "tormenta o nevada fuerte"}
_FESTIVOS = USFederalHolidayCalendar().holidays(start="2010-12-01", end="2013-12-31")


def cargar_modelo(carpeta=None):
    """Devuelve (modelo, metadatos, histórico). Lanza FileNotFoundError con un mensaje claro si falta algo."""
    carpeta = carpeta or os.path.join(CARPETA, "modelo")
    rutas = [os.path.join(carpeta, n) for n in ("modelo_bicis.joblib", "metadatos.json", "historico_demo.csv")]
    if not all(os.path.exists(r) for r in rutas):
        raise FileNotFoundError("Falta la carpeta 'modelo/'. Ejecuta antes notebooks/04_evaluacion.ipynb: la crea con el modelo, "
                                "los metadatos y el histórico de la demo.")
    with open(rutas[1], encoding="utf8") as f:
        meta = json.load(f)
    historico = pd.read_csv(rutas[2], parse_dates=["ts"], index_col="ts")
    return joblib.load(rutas[0]), meta, historico


def construir_variables(s):
    """Las mismas variables que usó el entrenamiento: todo lo conocido a las 23:00 del día anterior (retrasos de 24 h o más)."""
    x = pd.DataFrame(index=s.index)
    x["hr"], x["weekday"], x["mnth"] = s.index.hour, s.index.dayofweek, s.index.month
    x["holiday"], x["workingday"] = s["holiday"], s["workingday"]
    x["lag_24"] = s["cnt"].shift(24)
    x["lag_168"] = s["cnt"].shift(168)
    x["media4sem"] = sum(s["cnt"].shift(168 * k) for k in (1, 2, 3, 4)) / 4
    x["nivel_7d"] = s["cnt"].shift(24).rolling(168).mean()
    for c in CLIMA:
        x[c] = s[c]
    return x


def cerca_de_festivo(fecha):
    """True si el día es festivo federal, su víspera o el día siguiente (el calendario se conoce de antemano)."""
    d = pd.Timestamp(fecha).normalize()
    return bool(d in _FESTIVOS or d + pd.DateOffset(days=1) in _FESTIVOS or d - pd.DateOffset(days=1) in _FESTIVOS)


def validar_entrada(fecha, tiempo, ajuste_temp, meta):
    """Devuelve una lista de errores en español (lista vacía = entrada válida)."""
    errores = []
    if fecha in (None, ""):
        errores.append("Falta la fecha del día que quieres prever.")
    else:
        try:
            d = pd.Timestamp(fecha).normalize()
        except (ValueError, TypeError):
            errores.append(f"No entiendo la fecha '{fecha}'. Escríbela como 2012-11-14.")
        else:
            ini, fin = (pd.Timestamp(v) for v in meta["rango_fechas"])
            if not ini <= d <= fin:
                errores.append(f"La demo solo conoce los días entre {ini.date()} y {fin.date()} (has escrito {d.date()}).")
    if tiempo is not None and tiempo not in TIEMPOS:
        errores.append(f"El tipo de tiempo debe ser 1, 2, 3 o 4 (has escrito {tiempo}).")
    if ajuste_temp is not None:
        try:
            if not -10 <= float(ajuste_temp) <= 10:
                errores.append(f"El ajuste de temperatura debe estar entre -10 y +10 °C (has escrito {ajuste_temp}).")
        except (TypeError, ValueError):
            errores.append(f"El ajuste de temperatura debe ser un número (has escrito '{ajuste_temp}').")
    return errores


def predecir_dia(fecha, modelo, meta, historico, tiempo=None, ajuste_temp=0.0):
    """Valida y prevé las 24 horas del día. Si hay errores, devuelve solo {'errores': [...]}.

    tiempo: None = usar el clima real de ese día como previsión; 1–4 = tipo de tiempo previsto.
    ajuste_temp: grados que se suman a la temperatura prevista.
    """
    errores = validar_entrada(fecha, tiempo, ajuste_temp, meta)
    if errores:
        return {"errores": errores}
    dia = pd.Timestamp(fecha).normalize()
    horas = pd.date_range(dia, periods=24, freq="h")
    s = historico.loc[:horas[-1]].copy()
    if tiempo is not None:
        s.loc[horas, "weathersit"] = tiempo
    if ajuste_temp:
        s.loc[horas, "temp"] = (s.loc[horas, "temp"] + float(ajuste_temp) / 41).clip(0, 1)
        s.loc[horas, "atemp"] = (s.loc[horas, "atemp"] + float(ajuste_temp) / 50).clip(0, 1)
    x = construir_variables(s).loc[horas, meta["variables"]]
    if x.isna().any().any():
        return {"errores": ["El histórico no llega para calcular las variables de ese día."]}
    pred = np.clip(modelo.predict(x), 0, None)
    cerca = cerca_de_festivo(dia)
    laborable = (x["workingday"] == 1).to_numpy()
    punta = laborable & x["hr"].isin(HORAS_PUNTA).to_numpy()
    franja = ["punta" if p else ("laborable" if lab else "finde") for p, lab in zip(punta, laborable)]
    q = np.array([meta["incertidumbre"]["anchos"][f"{f}_cerca{int(cerca)}"] for f in franja])
    avisos = []
    if cerca:
        avisos.append(f"Día cercano a un festivo: el modelo vio pocos casos y su error medio sube de {meta['metricas']['mae_test']} "
                      f"a {meta['metricas']['mae_cerca_festivo']} bicis por hora. Revisa la previsión con una persona.")
    clima_dia = s.loc[horas, "weathersit"].max()
    if clima_dia >= 3:
        avisos.append("Lluvia, nieve o tormenta: hay pocas horas así en los datos y la previsión es menos fiable.")
    real = historico["cnt"].reindex(horas)
    return {
        "errores": [], "fecha": str(dia.date()), "horas": [int(h.hour) for h in horas],
        "prevision": [round(float(v), 1) for v in pred],
        "minimo": [round(float(v), 1) for v in np.clip(pred - q, 0, None)], "maximo": [round(float(v), 1) for v in pred + q],
        "real": None if real.isna().any() else [int(v) for v in real],
        "total_previsto": round(float(pred.sum())), "hora_pico": int(horas[int(np.argmax(pred))].hour), "pico": round(float(pred.max())),
        "advertencias": avisos,
        "aviso": (f"Estimación orientativa. Con datos de otro periodo (nov–dic 2012) el modelo se equivocó de media en "
                  f"{meta['metricas']['mae_test']} bicis por hora ({meta['metricas']['mae_punta']} en hora punta). "
                  f"El rango mostrado cubre en torno al {int(meta['incertidumbre']['nivel'] * 100)} % de las horas. "
                  "Una persona debe revisar la previsión antes de decidir cuántas bicis recolocar. " + meta["limitaciones"]),
    }
