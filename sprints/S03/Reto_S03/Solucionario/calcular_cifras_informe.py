#!/usr/bin/env python3
"""Cifras del informe resuelto del reto S03 («Primer modelo en producción»).

Reproduce TODOS los números del informe a partir de:
  - reservas_turisdata.csv (datos sintéticos de TurisData)
  - la carpeta modelo_cancelaciones/ que crea el laboratorio S3.5 (S3.5_lab_autogluon.py)

Uso (desde la carpeta donde ejecutaste el laboratorio):
    python calcular_cifras_informe.py            # imprime todo, con los importes del solucionario (225 € y 60 €)
    COSTE_NO_PREVISTA=150 COSTE_ALERTA_FALSA=30 UMBRAL=0.2 python calcular_cifras_informe.py   # con vuestros importes

Los importes del solucionario NO son los del cuaderno (100 € y 40 €): se razonan con el ingreso medio por reserva (consulta SQL
«Ingreso medio por reserva», 568 €): 40 % de ese ingreso se pierde si la cancelación no se prevé (≈ 225 €) y la alerta falsa
cuesta un 10 % de descuento (≈ 57 €) más 5 € de tiempo del equipo (≈ 60 €). Cada equipo debe razonar los suyos.
"""
import os
import sqlite3

import pandas as pd
from autogluon.tabular import TabularPredictor
from sklearn.metrics import confusion_matrix, precision_score, recall_score, roc_auc_score

CSV = os.environ.get("DATOS", "reservas_turisdata.csv")
MODELO = os.environ.get("MODELO", "modelo_cancelaciones")
C_NO_PREV = float(os.environ.get("COSTE_NO_PREVISTA", "225"))
C_FALSA = float(os.environ.get("COSTE_ALERTA_FALSA", "60"))
UMBRAL = float(os.environ.get("UMBRAL", "0.2"))


def titulo(t):
    print(f"\n{'=' * 8} {t} {'=' * 8}")


datos = pd.read_csv(CSV, parse_dates=["fecha_reserva", "fecha_llegada"])

# ---------------------------------------------------------------- A. SQL sobre el dato
titulo("A. SQL: revisar el dato (sqlite en memoria)")
con = sqlite3.connect(":memory:")
datos.assign(fecha_reserva=datos.fecha_reserva.dt.strftime("%Y-%m-%d"),
             fecha_llegada=datos.fecha_llegada.dt.strftime("%Y-%m-%d")).to_sql("reservas", con, index=False)
consultas = {
    "Total, cancelaciones y % global": "SELECT COUNT(*) AS reservas, SUM(cancelada) AS canceladas, ROUND(100.0*AVG(cancelada),1) AS pct FROM reservas",
    "% de cancelación por canal": "SELECT canal, COUNT(*) AS reservas, ROUND(100.0*AVG(cancelada),1) AS pct FROM reservas GROUP BY canal ORDER BY pct DESC",
    "% de cancelación por depósito": "SELECT deposito, COUNT(*) AS reservas, ROUND(100.0*AVG(cancelada),1) AS pct FROM reservas GROUP BY deposito ORDER BY pct DESC",
    "% de cancelación por tarifa": "SELECT tarifa, COUNT(*) AS reservas, ROUND(100.0*AVG(cancelada),1) AS pct FROM reservas GROUP BY tarifa ORDER BY pct DESC",
    "% de cancelación por antelación": "SELECT CASE WHEN antelacion_dias<30 THEN '1) menos de 30 días' WHEN antelacion_dias<90 THEN '2) 30 a 89 días' WHEN antelacion_dias<180 THEN '3) 90 a 179 días' ELSE '4) 180 días o más' END AS antelacion, COUNT(*) AS reservas, ROUND(100.0*AVG(cancelada),1) AS pct FROM reservas GROUP BY 1 ORDER BY 1",
    "Ingreso medio por reserva (noches x precio_noche), base de los importes de coste": "SELECT ROUND(AVG(noches*precio_noche),1) AS ingreso_medio_reserva, ROUND(AVG(precio_noche),2) AS precio_noche_medio, ROUND(AVG(noches),2) AS noches_medias FROM reservas",
    "Nulos en pais_origen": "SELECT COUNT(*) AS sin_pais, ROUND(100.0*COUNT(*)/(SELECT COUNT(*) FROM reservas),1) AS pct FROM reservas WHERE pais_origen IS NULL",
}
for nombre, sql in consultas.items():
    print(f"\n-- {nombre}\n{sql}")
    print(pd.read_sql_query(sql, con).to_string(index=False))

# ---------------------------------------------------------------- B. Partición temporal
titulo("B. Partición temporal 80/20 por fecha_reserva")
datos = datos.sort_values("fecha_reserva").reset_index(drop=True)
corte = int(len(datos) * 0.8)
ent, prueba = datos.iloc[:corte].drop(columns=["id_reserva"]), datos.iloc[corte:].drop(columns=["id_reserva"])
print(f"Entrenamiento: {len(ent)} filas, {ent.fecha_reserva.min().date()} a {ent.fecha_reserva.max().date()}, % cancelación {100*ent.cancelada.mean():.1f}")
print(f"Prueba:        {len(prueba)} filas, {prueba.fecha_reserva.min().date()} a {prueba.fecha_reserva.max().date()}, % cancelación {100*prueba.cancelada.mean():.1f}")
y = prueba["cancelada"].to_numpy()
print(f"Referencia «nadie cancela»: acierta el {100*(1-y.mean()):.1f} % en la prueba")

pred = TabularPredictor.load(MODELO)
prob = pred.predict_proba(prueba.drop(columns=["cancelada"]))[1].to_numpy()
prueba = prueba.assign(prob=prob)

# ---------------------------------------------------------------- C. Métricas
titulo("C. Métricas en datos NO vistos (periodo de prueba)")
print(f"ROC-AUC: {roc_auc_score(y, prob):.3f}")
for u in sorted({0.5, UMBRAL}):
    p = (prob >= u).astype(int)
    tn, fp, fn, tp = confusion_matrix(y, p).ravel()
    print(f"Umbral {u}: alertas={p.sum()}  aciertos de cancelación (TP)={tp}  no previstas (FN)={fn}  alertas falsas (FP)={fp}  "
          f"precisión={precision_score(y, p):.3f}  recall={recall_score(y, p):.3f}")

# ---------------------------------------------------------------- D. Costes
titulo(f"D. Coste por umbral (no prevista={C_NO_PREV:.0f} €, alerta falsa={C_FALSA:.0f} €)")


def tabla_costes(c_np, c_f):
    filas = []
    for u in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7):
        p = (prob >= u).astype(int)
        fn = int(((p == 0) & (y == 1)).sum())
        fp = int(((p == 1) & (y == 0)).sum())
        filas.append(dict(umbral=u, alertas=int(p.sum()), no_previstas=fn, alertas_falsas=fp, coste=c_np * fn + c_f * fp))
    t = pd.DataFrame(filas)
    nunca, todos = c_np * int(y.sum()), c_f * int((y == 0).sum())
    return t, nunca, todos


t, nunca, todos = tabla_costes(C_NO_PREV, C_FALSA)
print(t.to_string(index=False))
print(f"Umbral teórico = {C_FALSA:.0f}/({C_FALSA:.0f}+{C_NO_PREV:.0f}) = {C_FALSA/(C_FALSA+C_NO_PREV):.2f}")
print(f"No avisar nunca: {nunca:.0f} €  ·  Avisar a todos: {todos:.0f} €  ·  Modelo con umbral {UMBRAL}: {t.loc[t.umbral == UMBRAL, 'coste'].iloc[0]:.0f} €")
ahorro = todos - t.loc[t.umbral == UMBRAL, "coste"].iloc[0]
print(f"Ahorro frente a «avisar a todos»: {ahorro:.0f} € ({100*ahorro/todos:.1f} %) en {len(prueba)} reservas")

titulo("D2. Sensibilidad: ¿cambia la conclusión si cambian los importes?")
escenarios = [("Importes del solucionario", C_NO_PREV, C_FALSA),
              ("Importes de ejemplo del cuaderno", 100, 40),
              ("Alerta casi gratis (un correo)", C_NO_PREV, 5)]
for nombre, c_np, c_f in escenarios:
    tt, nunca_, todos_ = tabla_costes(c_np, c_f)
    mejor = tt.loc[tt.coste.idxmin()]
    print(f"\n-- {nombre}: no prevista={c_np:.0f} €, alerta falsa={c_f:.0f} € · umbral teórico {c_f/(c_np+c_f):.2f}")
    print(f"   nunca={nunca_:.0f} € · todos={todos_:.0f} € · mejor umbral probado={mejor.umbral} ({mejor.coste:.0f} €) · "
          f"ahorro frente a «todos»={todos_-mejor.coste:.0f} € ({100*(todos_-mejor.coste)/todos_:.1f} %)")

# ---------------------------------------------------------------- E. Importancia
titulo("E. Importancia de variables (permutación, 3 repeticiones)")
imp = pred.feature_importance(prueba.drop(columns=["prob"]), num_shuffle_sets=3, subsample_size=1000, silent=True)
print(imp[["importance", "stddev"]].head(8).round(4).to_string())

# ---------------------------------------------------------------- F. Sesgos
titulo(f"F. Revisión de sesgos con umbral {UMBRAL}: ¿se equivoca igual con todos?")
prueba["alerta"] = (prueba.prob >= UMBRAL).astype(int)
for col in ("canal", "pais_origen"):
    g = prueba.assign(**{col: prueba[col].fillna("sin_dato")}).groupby(col)
    res = g.apply(lambda d: pd.Series({
        "reservas": len(d),
        "%_alertas": round(100 * d.alerta.mean(), 1),
        "%_cancel_real": round(100 * d.cancelada.mean(), 1),
        "falsas_alarmas_%_de_no_canceladas": round(100 * ((d.alerta == 1) & (d.cancelada == 0)).sum() / max((d.cancelada == 0).sum(), 1), 1),
        "no_previstas_%_de_canceladas": round(100 * ((d.alerta == 0) & (d.cancelada == 1)).sum() / max((d.cancelada == 1).sum(), 1), 1),
    }), include_groups=False)
    print(f"\n-- por {col}\n{res.to_string()}")

# ---------------------------------------------------------------- G. Capacidad limitada
titulo("G. Si el equipo solo puede contactar a una parte de las reservas: ¿a cuáles?")
orden = prueba.sort_values("prob", ascending=False)
base = prueba.cancelada.mean()
for frac in (0.10, 0.20, 0.30, 0.50):
    k = int(len(orden) * frac)
    top = orden.head(k)
    print(f"Top {int(frac*100):>2} % con más riesgo ({k} reservas): cancelan {100*top.cancelada.mean():.1f} % (media general {100*base:.1f} %) · "
          f"capturamos {int(top.cancelada.sum())} de {int(prueba.cancelada.sum())} cancelaciones ({100*top.cancelada.sum()/prueba.cancelada.sum():.0f} %)")
