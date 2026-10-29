# %% [markdown]
# # S3.5 · Laboratorio de AutoML sin nube de pago (AutoGluon)
# **Sprint 3 · Reto "Primer modelo en producción" · IFCD107**
#
# Se ejecuta en Google Colab o en tu PC y **no tiene coste**.
# Objetivo: predecir si una reserva de *TurisData Canarias* se cancelará.
#
# Uso en Colab: copia cada bloque `# %%` en una celda. La primera celda instala AutoGluon.
# Uso en local:  python S3.5_lab_autogluon.py   (variables de entorno opcionales: TIME_LIMIT, DATOS)

# %% Instalación (solo Colab; en local ya lo tendrás instalado)
# !pip install -q "autogluon.tabular[lightgbm,xgboost,catboost]"

# %% 0. Configuración
import os
import time

import numpy as np
import pandas as pd

RUTA_DATOS = os.environ.get("DATOS", "reservas_turisdata.csv")
LIMITE_TIEMPO = int(os.environ.get("TIME_LIMIT", "120"))  # segundos de entrenamiento
CARPETA_MODELO = "modelo_cancelaciones"
OBJETIVO = "cancelada"
SEMILLA = 42
np.random.seed(SEMILLA)

# %% 1. Cargar los datos
# Si no tienes el CSV, genéralo con:  python generar_reservas_turisdata.py
datos = pd.read_csv(RUTA_DATOS, parse_dates=["fecha_reserva", "fecha_llegada"])
print(datos.shape)
print(datos.head())

# %% 2. Exploración y calidad del dato (en una plataforma de nube: "explorar el dataset")
print("\nTipos de dato:\n", datos.dtypes)
print("\nNulos por columna:\n", datos.isna().sum()[datos.isna().sum() > 0])
print("\nProporción de cancelaciones:", round(datos[OBJETIVO].mean(), 3))
print("\nResumen numérico:\n", datos.describe().T[["mean", "std", "min", "max"]])
# Preguntas para el informe:
#  - ¿Está desbalanceada la clase objetivo? ¿Qué métrica conviene?
#  - ¿Qué columnas podrían provocar fuga de datos (información posterior al desenlace)?

# %% 3. Partición TEMPORAL (evita fuga de datos: se entrena con el pasado y se prueba con el futuro)
datos = datos.sort_values("fecha_reserva").reset_index(drop=True)
corte = int(len(datos) * 0.8)
entrenamiento = datos.iloc[:corte].drop(columns=["id_reserva"])
prueba = datos.iloc[corte:].drop(columns=["id_reserva"])
print(f"\nEntrenamiento: {len(entrenamiento)} filas ({entrenamiento.fecha_reserva.min().date()} a "
      f"{entrenamiento.fecha_reserva.max().date()})")
print(f"Prueba:        {len(prueba)} filas ({prueba.fecha_reserva.min().date()} a "
      f"{prueba.fecha_reserva.max().date()})")

# %% 4. Entrenar con AutoML (equivale al experimento de Autopilot/Canvas)
from autogluon.tabular import TabularPredictor

inicio = time.time()
predictor = TabularPredictor(
    label=OBJETIVO,
    problem_type="binary",
    eval_metric="roc_auc",
    path=CARPETA_MODELO,
).fit(
    train_data=entrenamiento,
    time_limit=LIMITE_TIEMPO,
    presets="medium_quality",
)
tiempo_entrenamiento = time.time() - inicio
print(f"\nTiempo de entrenamiento: {tiempo_entrenamiento:.0f} s")

# %% 5. Revisar los modelos candidatos (leaderboard)
clasificacion = predictor.leaderboard(prueba, silent=True)
print(clasificacion[["model", "score_test", "score_val", "fit_time"]].head(10))
# Preguntas: ¿el mejor modelo es un ensamblado? ¿Cuánto tarda cada uno? ¿Merece la pena el coste de cómputo?

# %% 6. Evaluar en el periodo de prueba
from sklearn.metrics import (classification_report, confusion_matrix, f1_score,
                             precision_score, recall_score, roc_auc_score)

y_real = prueba[OBJETIVO]
prob = predictor.predict_proba(prueba.drop(columns=[OBJETIVO]))[1]  # probabilidad de cancelar
for umbral in (0.5, 0.3):
    pred = (prob >= umbral).astype(int)
    print(f"\nUmbral {umbral}: precisión={precision_score(y_real, pred):.3f} "
          f"recall={recall_score(y_real, pred):.3f} F1={f1_score(y_real, pred):.3f}")
print("\nROC-AUC:", round(roc_auc_score(y_real, prob), 3))
print("\nMatriz de confusión (umbral 0.5):\n", confusion_matrix(y_real, (prob >= 0.5).astype(int)))
print("\n", classification_report(y_real, (prob >= 0.5).astype(int), digits=3))
# Pregunta de negocio: ¿qué cuesta más, una cancelación no prevista o una alerta falsa? ¿Qué umbral elegirías?

# %% 6b. Elegir el umbral con costes (EJEMPLO: cambia los dos importes por los vuestros)
COSTE_NO_PREVISTA = 100    # euros que cuesta una cancelación que no avisamos (noche vacía)
COSTE_ALERTA_FALSA = 40    # euros que cuesta una alerta que no hacía falta (p. ej. un descuento regalado)
y_array = y_real.to_numpy()
filas = []
for u in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7):
    pred = (prob >= u).astype(int)
    no_previstas = int(((pred == 0) & (y_array == 1)).sum())
    falsas = int(((pred == 1) & (y_array == 0)).sum())
    filas.append({"umbral": u, "alertas": int(pred.sum()), "no_previstas": no_previstas,
                  "alertas_falsas": falsas, "coste_euros": COSTE_NO_PREVISTA * no_previstas + COSTE_ALERTA_FALSA * falsas})
tabla_costes = pd.DataFrame(filas)
print("\n", tabla_costes.to_string(index=False))
print("\nUmbral con menos coste (de los probados):", tabla_costes.loc[tabla_costes["coste_euros"].idxmin(), "umbral"])
print("Umbral teórico = alerta falsa / (alerta falsa + no prevista) =",
      round(COSTE_ALERTA_FALSA / (COSTE_ALERTA_FALSA + COSTE_NO_PREVISTA), 2))
print("Comparación: no avisar nunca =", COSTE_NO_PREVISTA * int(y_array.sum()), "euros · avisar a todos =",
      COSTE_ALERTA_FALSA * int((y_array == 0).sum()), "euros")
# Pregunta: ¿gana el modelo a «avisar a todos»? ¿Y si la alerta falsa costara 5 euros en vez de 40?

# %% 7. Explicabilidad: importancia de variables
importancia = predictor.feature_importance(prueba, num_shuffle_sets=3, subsample_size=1000, silent=True)
print(importancia[["importance", "stddev"]].head(10))
# Pregunta: ¿tienen sentido las variables más importantes para el negocio? ¿Alguna sospechosa de fuga?

# %% 8. Guardar y recargar el modelo (equivale a "desplegar"; el modelo queda en una carpeta)
predictor.save()
predictor_recargado = TabularPredictor.load(CARPETA_MODELO)
comprobacion = predictor_recargado.predict_proba(prueba.drop(columns=[OBJETIVO]).head(5))[1]
print("\nModelo recargado. Probabilidades de ejemplo:", comprobacion.round(3).tolist())


# %% 9. Función de predicción (la usará la API del paso 10)
def predecir_cancelacion(reserva: dict) -> dict:
    """Recibe una reserva (dict con las columnas de entrada) y devuelve la probabilidad de cancelación."""
    fila = pd.DataFrame([reserva])
    fila["fecha_reserva"] = pd.to_datetime(fila["fecha_reserva"])
    fila["fecha_llegada"] = pd.to_datetime(fila["fecha_llegada"])
    p = float(predictor_recargado.predict_proba(fila)[1].iloc[0])
    return {"probabilidad_cancelacion": round(p, 4), "alerta": p >= 0.5}


ejemplo = prueba.drop(columns=[OBJETIVO]).iloc[0].to_dict()
print("\nEjemplo de predicción:", predecir_cancelacion(ejemplo))

# %% 10. Servir el modelo por API (equivale al endpoint) -> ver api_cancelaciones.py
# En local:   uvicorn api_cancelaciones:app --reload
#             abre http://127.0.0.1:8000/docs y prueba POST /predecir
# En Colab la API no es accesible desde fuera; demuéstrala con las llamadas de arriba
# o con TestClient (ver guía).

# %% 11. Informe de recursos (equivale al "informe de costes"; aquí el coste económico es 0 EUR)
tamano_mb = sum(
    os.path.getsize(os.path.join(raiz, f))
    for raiz, _, ficheros in os.walk(CARPETA_MODELO) for f in ficheros
) / 1e6
print("\n--- Informe de recursos ---")
print(f"Tiempo de entrenamiento: {tiempo_entrenamiento:.0f} s (límite fijado: {LIMITE_TIEMPO} s)")
print(f"Tamaño del modelo en disco: {tamano_mb:.1f} MB")
print("Coste económico: 0 EUR (Colab gratuito o equipo local)")
print("Recursos que hay que cerrar: la sesión de Colab (Entorno de ejecución > Desconectar).")
