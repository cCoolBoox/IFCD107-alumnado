# Laboratorio de AutoML con AutoGluon (Colab o en local)

**Sprint 3 · Reto «Primer modelo en producción».** Ficha del reto: [`Reto_Sprint_03.md`](../Reto_Sprint_03.md).

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/Reto_S03/laboratorio_automl/S3.5_lab_autogluon.ipynb)

**Cómo trabajarlo:** abrid el cuaderno en Colab y seguid la [guía en parejas](../../actividades/automl/guia_automl_en_parejas.md) (roles, plan de 100 min, informe del reto). Más material: [listado de pasos](../../actividades/automl/listado_pasos_automl.md) · [solucionario paso a paso](../../actividades/automl/soluciones_automl_paso_a_paso.md) · [código explicado línea a línea](../../actividades/automl/codigo_explicado_automl.md) · [guía corta en PDF](../../guia/Guia_AutoML_AutoGluon.pdf).

Laboratorio de AutoML con AutoGluon. Flujo: dato → experimento AutoML → evaluación → explicabilidad → servicio por API → informe de recursos.

## Archivos
| Archivo | Para qué |
|---|---|
| `generar_reservas_turisdata.py` | Crea `reservas_turisdata.csv` (6.000 reservas sintéticas de *TurisData Canarias*) |
| `S3.5_lab_autogluon.ipynb` | **Cuaderno para Colab** (el mismo laboratorio): descarga solo el CSV y la API, no hay que subir nada |
| `S3.5_lab_autogluon.py` | El mismo laboratorio por celdas (`# %%`), para ejecutar en local |
| `api_cancelaciones.py` | API local con FastAPI |
| `requirements.txt` | Dependencias (solo hace falta si lo ejecutáis en local) |
| `reservas_turisdata.csv` | El CSV ya generado (6.000 reservas). **El cuaderno lo descarga solo** (necesita internet): no hay que subirlo ni ejecutar el generador. Solo con el `.py` hace falta tenerlo en la misma carpeta |

## Requisitos
- Colab (gratis) o Python 3.10–3.13 en local con 8 GB de RAM.
- En Colab: el cuaderno ya trae la celda de instalación (2–3 min) y descarga `reservas_turisdata.csv` solo. Si usáis el `.py` en Colab, la primera celda es `!pip install -q "autogluon.tabular[lightgbm,xgboost,catboost]"` y hay que subir el CSV (panel de archivos de la izquierda) o generarlo con el script.

## Pasos del alumnado
1. **Cargar y explorar** (celdas 1–2): tipos, nulos, proporción de cancelaciones (~46 %). *Pregunta:* ¿qué métrica conviene?
2. **Partición temporal 80/20** (celda 3): se entrena con el pasado y se prueba con el futuro. *Pregunta:* ¿por qué no aleatoria?
3. **Entrenar** (celda 4): `TabularPredictor(...).fit(time_limit=120, presets="medium_quality")`. Con `TIME_LIMIT` menor el ensayo dura ~15 s.
4. **Leaderboard** (celda 5): comparar candidatos y tiempos; identificar el ensamblado.
5. **Evaluar** (celda 6): precisión, recall y F1 con umbral 0,5 y 0,3; matriz de confusión. *Decisión de negocio:* ¿qué cuesta más, una cancelación no prevista o una alerta falsa?
6. **Umbral con costes** (celda 6b): poner precio a cada error y calcular el coste total por umbral. *Cambiad los importes de ejemplo por vuestras hipótesis.*
7. **Explicabilidad** (celda 7): importancia de variables. Esperable: `antelacion_dias`, `deposito`, `canal`, `tarifa`.
8. **Guardar y recargar** (celda 8) y función `predecir_cancelacion` (celda 9).
9. **API local** (celda 10): `uvicorn api_cancelaciones:app --reload`, abrir `http://127.0.0.1:8000/docs`, probar `POST /predecir`. En Colab, usar `TestClient`.
10. **Informe de recursos** (celda 11): tiempo, tamaño del modelo (~225 MB) y coste 0 EUR.

**Entregable del reto:** informe del mejor modelo (métricas, umbral elegido y justificación) + captura de la llamada a la API + informe de recursos.

## Otras plataformas de AutoML (por ejemplo, Amazon SageMaker Canvas)

El flujo de este laboratorio es el mismo que en las plataformas de nube (SageMaker Canvas o Autopilot, Vertex AI, Azure AutoML, H2O). Lo que cambia es **dónde se ejecuta y cuánto cuesta**: en la nube hay cuentas, permisos y facturación por uso, y todo lo que se deja encendido cuesta dinero. En clase **no se crean cuentas de nube**; esta tabla es para que sepáis traducir lo que hacéis aquí.

| Plataforma de nube (ej. SageMaker) | Este laboratorio |
|---|---|
| Subir dataset a S3 | Cargar el CSV con pandas |
| Explorar datos en Canvas | Celdas 1–2 |
| Experimento AutoML (Canvas/Autopilot) | `TabularPredictor.fit` |
| Lista de modelos candidatos | `leaderboard` |
| Métricas y explicabilidad | Celdas 6–7 |
| Elegir el umbral según el coste de cada error | Celda 6b (es la misma decisión en cualquier plataforma) |
| Desplegar un endpoint | API local con FastAPI |
| IAM, claves y seguridad | Concepto; en local no hay cuenta que proteger (explicar cómo sería) |
| Informe de costes y borrar recursos (endpoints, sesión de Canvas abierta) | Informe de recursos; desconectar la sesión de Colab |
