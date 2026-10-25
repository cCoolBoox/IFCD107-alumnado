# Plantilla de demostrador (Sprint 16)

Esta carpeta es un **ejemplo completo y funcional** con el modelo de cancelaciones de TurisData. Vuestro equipo la adapta a **su** proyecto.

## Qué contiene
| Archivo | Para qué sirve |
|---|---|
| `logica.py` | Cargar el modelo, **validar** entradas y **predecir** con aviso de incertidumbre. Sin interfaz. |
| `app.py` | Interfaz **Streamlit** (formulario → resultado). |
| `api.py` | API **FastAPI** *(opcional)*: `/salud` y `/predecir`. |
| `tests/test_logica.py` | Pruebas de sentido común (`pytest -q`). |
| `requirements.txt` | Versiones del entorno donde se comprobó (recortad a lo que uséis). |
| `modelo/` | **No incluida**: la crea el notebook `S16_01_demostrador` (o vuestro script de entrenamiento) con `modelo_cancelaciones.joblib` y `metadatos.json`. |

## Cómo usarla
1. Ejecutad `S16_01_demostrador` (crea `demostrador/modelo/`), o vuestro propio entrenamiento que guarde `modelo/…joblib` + `metadatos.json`.
2. Instalad: `pip install -r requirements.txt` (necesitáis al menos `numpy pandas scikit-learn joblib streamlit`).
3. Lanzad la app: `streamlit run app.py` (http://localhost:8501).
4. *(Opcional)* API: `pip install fastapi uvicorn` y `uvicorn api:app --reload` (http://127.0.0.1:8000/docs).
5. Pruebas: `pip install pytest` y `pytest -q`.

## Qué adaptar en vuestro proyecto
- **`metadatos.json`:** campos que pide vuestro modelo, rangos válidos, categorías, métricas y **limitaciones** propias.
- **`logica.py`:** reglas de validación de vuestro problema y texto del aviso de incertidumbre.
- **`app.py`:** el tipo de entrada. *Series:* seleccionar fechas y mostrar previsión con intervalo. *Imágenes:* `st.file_uploader` y mostrar clase, confianza y aviso «fuera de distribución». *Asistente RAG:* `st.chat_input` y mostrar **citas** de las fuentes e indicar que es una IA.
- **Alternativa Gradio:** `gr.Interface(fn=..., inputs=..., outputs=...)` que llame a `predecir_reserva`.
- **Plan B:** vídeo de 90 s y el notebook con widgets de `S16_01`.

## Buenas prácticas
No guardéis datos personales de quien usa el demostrador. No incluyáis claves en el código (usad variables de entorno). El aviso de incertidumbre debe viajar **con cada respuesta**.
