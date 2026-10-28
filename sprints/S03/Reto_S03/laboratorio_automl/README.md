# Laboratorio de AutoML con AutoGluon (Colab o en local)

**Sprint 3 · Reto «Primer modelo en producción».** Guía del laboratorio: [`Guia_AutoML_AutoGluon.pdf`](../../guia/Guia_AutoML_AutoGluon.pdf). Ficha del reto: [`Reto_Sprint_03.md`](../Reto_Sprint_03.md).

Laboratorio de AutoML con AutoGluon. Flujo: dato → experimento AutoML → evaluación → explicabilidad → servicio por API → informe de recursos.

## Archivos
| Archivo | Para qué |
|---|---|
| `generar_reservas_turisdata.py` | Crea `reservas_turisdata.csv` (6.000 reservas sintéticas de *TurisData Canarias*) |
| `S3.5_lab_autogluon.py` | Laboratorio por celdas (`# %%`); copiar a Colab o ejecutar en local |
| `api_cancelaciones.py` | API local con FastAPI |
| `requirements.txt` | Dependencias (solo hace falta si lo ejecutáis en local) |
| `reservas_turisdata.csv` | El CSV ya generado (6.000 reservas): **subidlo a Colab** y no hace falta ejecutar el generador |

## Requisitos
- Colab (gratis) o Python 3.10–3.13 en local con 8 GB de RAM.
- En Colab: primera celda `!pip install -q "autogluon.tabular[lightgbm,xgboost,catboost]"`.
- Sube `reservas_turisdata.csv` a Colab (panel de archivos de la izquierda, icono de la carpeta) o genéralo con el script.

## Pasos del alumnado
1. **Cargar y explorar** (celdas 1–2): tipos, nulos, proporción de cancelaciones (~46 %). *Pregunta:* ¿qué métrica conviene?
2. **Partición temporal 80/20** (celda 3): se entrena con el pasado y se prueba con el futuro. *Pregunta:* ¿por qué no aleatoria?
3. **Entrenar** (celda 4): `TabularPredictor(...).fit(time_limit=120, presets="medium_quality")`. Con `TIME_LIMIT` menor el ensayo dura ~15 s.
4. **Leaderboard** (celda 5): comparar candidatos y tiempos; identificar el ensamblado.
5. **Evaluar** (celda 6): precisión, recall y F1 con umbral 0,5 y 0,3; matriz de confusión. *Decisión de negocio:* ¿qué cuesta más, una cancelación no prevista o una alerta falsa?
6. **Explicabilidad** (celda 7): importancia de variables. Esperable: `antelacion_dias`, `deposito`, `canal`, `tarifa`.
7. **Guardar y recargar** (celda 8) y función `predecir_cancelacion` (celda 9).
8. **API local** (celda 10): `uvicorn api_cancelaciones:app --reload`, abrir `http://127.0.0.1:8000/docs`, probar `POST /predecir`. En Colab, usar `TestClient`.
9. **Informe de recursos** (celda 11): tiempo, tamaño del modelo (~225 MB) y coste 0 EUR.

**Entregable del reto:** informe del mejor modelo (métricas, umbral elegido y justificación) + captura de la llamada a la API + informe de recursos.

## Equivalencias con SageMaker
| SageMaker | Este laboratorio |
|---|---|
| Subir dataset a S3 | Cargar el CSV con pandas |
| Explorar datos en Canvas | Celdas 1–2 |
| Experimento AutoML (Canvas/Autopilot) | `TabularPredictor.fit` |
| Lista de modelos candidatos | `leaderboard` |
| Métricas y explicabilidad | Celdas 6–7 |
| Desplegar un endpoint | API local con FastAPI |
| IAM, claves y seguridad | Concepto; en local no hay cuenta que proteger (explicar cómo sería) |
| Informe de costes y borrar recursos | Informe de recursos; desconectar la sesión de Colab |
