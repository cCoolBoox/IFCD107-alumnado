"""Lógica del demostrador: cargar el modelo, validar la entrada y predecir. Sin interfaz."""
import json
import os

import joblib
import pandas as pd

CARPETA = os.path.dirname(os.path.abspath(__file__))


def cargar_modelo(carpeta=None):
    """Devuelve (modelo, metadatos). Lanza FileNotFoundError con un mensaje claro si faltan los archivos."""
    carpeta = carpeta or os.path.join(CARPETA, "modelo")
    ruta_modelo = os.path.join(carpeta, "modelo_cancelaciones.joblib")
    ruta_meta = os.path.join(carpeta, "metadatos.json")
    if not (os.path.exists(ruta_modelo) and os.path.exists(ruta_meta)):
        raise FileNotFoundError("Falta el modelo. Ejecuta primero el notebook S16_01 (o tu script de entrenamiento) para crear la carpeta 'modelo/'.")
    with open(ruta_meta, encoding="utf8") as f:
        return joblib.load(ruta_modelo), json.load(f)


def validar_reserva(reserva, meta):
    """Devuelve una lista de errores en español (lista vacía = entrada válida)."""
    errores = []
    for campo, regla in meta["campos"].items():
        if campo not in reserva or reserva[campo] in (None, ""):
            errores.append(f"Falta el campo '{campo}'.")
            continue
        valor = reserva[campo]
        if regla["tipo"] == "categoria":
            if valor not in regla["valores"]:
                errores.append(f"'{valor}' no es un valor válido para '{campo}'. Opciones: {', '.join(regla['valores'])}.")
        else:
            try:
                numero = float(valor)
            except (TypeError, ValueError):
                errores.append(f"'{campo}' debe ser un número (has escrito '{valor}').")
                continue
            if not regla["min"] <= numero <= regla["max"]:
                errores.append(f"'{campo}' debe estar entre {regla['min']} y {regla['max']} (has escrito {valor}).")
    return errores


def nivel_riesgo(probabilidad):
    """Traduce la probabilidad a una etiqueta que entiende quien no sabe de modelos."""
    if probabilidad < 0.30:
        return "bajo"
    if probabilidad < 0.50:
        return "medio"
    return "alto"


def predecir_reserva(reserva, modelo, meta):
    """Valida y predice. Devuelve un diccionario; si hay errores, solo {'errores': [...]}."""
    errores = validar_reserva(reserva, meta)
    if errores:
        return {"errores": errores}
    fila = pd.DataFrame([reserva])[list(meta["campos"])]
    probabilidad = float(modelo.predict_proba(fila)[0, 1])
    return {
        "errores": [],
        "probabilidad": round(probabilidad, 3),
        "nivel": nivel_riesgo(probabilidad),
        "tasa_base": meta["tasa_cancelacion_base"],
        "aviso": (f"Estimación orientativa. El modelo tiene un AUC de {meta['auc_test']} en datos de prueba: "
                  "se equivoca con frecuencia. "
                  + meta["limitaciones"]),
    }
