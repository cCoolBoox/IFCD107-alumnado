# BiciPrevisión · Las Palmeras IA

**Brief:** Libre (inspirado en el 4: serie horaria) · **Curso:** IFCD107 · Especialista en IA · **Defensa:** día 2 del Sprint 17 · **Versión:** v1.0 (10/12/2026)

## 1. El problema en 3 líneas
- **Pregunta de negocio:** ¿podemos prever cuántas bicis se alquilarán en cada hora de mañana para que el operador decida cuántas recolocar en cada turno?
- **Decisión que apoya y para quién:** cuántas bicis y personas de redistribución poner en cada franja; responsable de operaciones de un sistema de bicis compartidas. **La decisión sigue siendo humana.**
- **Métrica de éxito:** negocio: evitar al menos 17 bicis de error por hora · técnica: MAE (bicis/hora) · baseline: misma hora de la semana pasada · umbral: bajar un 25 %.

## 2. Resultados en una tabla
| Modelo | MAE en validación (sep–oct) | MAE en test (nov–dic) | Tiempo | Notas |
|---|---|---|---|---|
| Baseline (semana pasada) | 69,5 | 75,4 | — | WAPE 39,9 %; hora punta 140,6 |
| Media de 4 semanas | 57,6 | — | — | segundo baseline |
| Red neuronal (MLP, 3 semillas) | 57,3–74,3 | — | ≈ 39 s | peor que el baseline y muy sensible a la semilla |
| **Candidato final: boosting (`HGB_prof6`)** | **42,2** | **44,0** | 3,1 s | 42 % menos error que el baseline (intervalo 31 %–50 %); hora punta 85,5; cerca de festivo 69,2 |

El test se evaluó **una sola vez**. Detalle en `docs/memoria_tecnica.pdf` y en `docs/model_card.md`.

## 3. Estructura del repositorio
```
.
├── README.md
├── requirements.txt
├── sprint-14/        # ficha, plan de datos, 01_eda, 02_baseline, backlog, riesgos, descargar_datos.py
├── sprint-15/        # 03_modelos.ipynb, registro.csv, justificacion_candidato.md, modelo y metadatos
└── sprint-16/
    ├── README.md                      # este fichero (la raíz lleva una copia al día)
    ├── notebooks/04_evaluacion.ipynb  # test, subgrupos, errores, mitigación, riesgos de datos
    ├── demostrador/
    │   ├── app.py  logica.py          # interfaz Streamlit y lógica sin interfaz
    │   ├── requirements.txt           # versiones fijas
    │   ├── tests/test_logica.py       # pytest -q
    │   └── modelo/                    # modelo, metadatos e histórico de la demo (los crea el cuaderno)
    ├── docs/
    │   ├── riesgos_eticos.md  model_card.md  memoria_tecnica.pdf
    │   └── figuras/                   # fig1–fig4 y capturas del demostrador
    └── autoevaluacion_<nombre>.md     # una por persona
```

## 4. Cómo reproducirlo (pasos exactos)
**Requisitos:** Python 3.13.18 · Linux (probado) · sin GPU · conexión para instalar y bajar los datos.

```bash
git clone [url-del-repositorio]
cd [carpeta]
python -m venv .venv
source .venv/bin/activate                         # Windows: .venv\Scripts\activate
pip install -r sprint-16/demostrador/requirements.txt
python sprint-14/descargar_datos.py               # baja los datos de la UCI en data/ y comprueba filas y huella
# ejecutar en orden: sprint-14/01_eda.ipynb, 02_baseline.ipynb, sprint-15/03_modelos.ipynb y sprint-16/notebooks/04_evaluacion.ipynb
```
**Tiempo total aproximado:** unos 6 minutos (cuadernos 01 y 02: 2 min; 03: 3 min; 04: menos de 1 min; la instalación, 16 s). **Semilla fija:** `SEMILLA = 42`. Si solo quieres ver la demo, el repositorio ya lleva la carpeta `sprint-16/demostrador/modelo/`: salta el paso de los cuadernos.

Debe salir **MAE 44,0** en el test (el cuaderno 04 lo comprueba con el del Sprint 15 y se detiene si no coincide).

## 5. Cómo lanzar el demostrador
Desde la raíz del repositorio, **un solo comando**:
```bash
streamlit run sprint-16/demostrador/app.py
```
Se abre en `http://localhost:8501`. Elige un día entre el 01/11 y el 31/12 de 2012, el tiempo previsto (o el real) y pulsa **«Prever el día»**. Muestra las 24 horas con un rango probable, avisos si el día es cercano a un festivo o hay lluvia, y el aviso de incertidumbre.

- **Pruebas:** `cd sprint-16/demostrador && python -m pytest -q` → 10 pruebas pasan en 4,9 s.
- **No guarda datos de la persona usuaria** y no lleva claves.
- **Plan B:** la grabación de 90 s (`docs/demo.mp4`) es una captura de pantalla del equipo y no se incluye en esta copia de referencia; las capturas de `docs/figuras/demostrador_*.png` muestran el mismo recorrido.

## 6. Datos y licencias
| Conjunto | Fuente | Licencia | ¿Incluido en el repo? |
|---|---|---|---|
| Bike Sharing Dataset (`hour.csv`) | https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset | CC BY 4.0 | no (se descarga con el script; el demostrador lleva un histórico recortado de nov–dic 2012, 1.464 horas más las 168 anteriores, para calcular los retrasos) |

**No hay datos personales** en el repositorio: alquileres agregados por hora.

## 7. IA responsable (resumen)
- Clasificación de riesgo (AI Act): **mínimo**, justificada en `docs/riesgos_eticos.md`. Datos personales: **no**.
- Principales riesgos y medidas: clima real usado como previsión (con un 10 % de error en el clima, MAE 46,4 frente a 44,0); fuga de `casual`/`registered` (excluidas); uso sin supervisión humana (aviso y alerta); festivos y hora punta (**abiertos**: rango más ancho, pero el error de la previsión central no mejoró).
- **Una mitigación que no funcionó:** reponderar la hora punta bajó su error y empeoró el global; se descartó con la regla escrita antes.
- **Limitaciones y usos no permitidos:** una ciudad, un operador, 2011–2012; no usar para decidir sobre personas ni para recortar servicio sin revisión humana (`docs/model_card.md`).
- **Uso de IA:** se pidió código de gráficos, de la validación cruzada y del esqueleto del demostrador; **se comprobó a mano** que la partición es temporal, que el MAE del cuaderno coincide con el del Sprint 15 y que el demostrador rechaza entradas erróneas; **se cambió** la agrupación de los intervalos (la primera propuesta agrupaba solo «hora punta / resto» y el fin de semana quedaba infracubierto; al separar punta, laborable y fin de semana la cobertura se acerca al 80 % en los tres) y un título de gráfico que decía «el modelo mejora en todas las horas» cuando a las 4 h no mejora.

## 8. Equipo y contribuciones
| Persona | Roles (S14 / S15 / S16) | Contribución principal |
|---|---|---|
| Marta | Scrum Master / Responsable técnica / Responsable de datos | `04_evaluacion.ipynb` (test y gráficos), figuras 1–2 |
| Persona B | Responsable técnico / Responsable de datos / Responsable de IA responsable | cierre de `riesgos_eticos.md`, README |
| Persona C | Responsable de datos / Responsable de IA responsable / Scrum Master | demostrador, `pytest`, prueba en limpio |
| Persona D | Responsable de IA responsable / Scrum Master / Responsable técnico | mitigación, *model card* y memoria técnica |

Convención de commits: `tipo: descripción` (`feat:`, `fix:`, `docs:`, `data:`, `exp:`). Todas las personas tienen commits propios.

## 9. Evidencias de metodología
- Tablero con las 13 historias y retrospectivas de S14, S15 y S16 en `sprint-14/backlog_y_sprints.md` (se actualiza al final de cada sprint); resumen en la memoria, §8.

## 10. Créditos y licencia del código
Datos: Fanaee-T y Gama (2013), UCI, CC BY 4.0. Librerías: numpy 2.5.3, pandas 2.3.3, scikit-learn 1.9.1, matplotlib 3.11.2, streamlit 1.64.0, pytest 9.1.1. Licencia del código: MIT.

## Revisión con la rúbrica

**Revisado por:** Persona C (no escribió el README) · **Fecha:** 10/12/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 4 | Ejecuté el cuaderno 04 de arriba abajo sin errores: el MAE de test (44,0) coincide con el del Sprint 15, hay intervalos por remuestreo, 8 subgrupos, análisis de los 10 peores días, tres mitigaciones elegidas con validación cruzada y medidas antes y después, y el demostrador rechaza una fecha imposible y una vacía; `pytest -q` pasa (10 pruebas en verde) |
| Reproducibilidad | 4 | Seguí solo este README en una carpeta limpia con un entorno nuevo: instalación en 16 s, `pytest -q` en verde y el demostrador abrió con `streamlit run`; hay versiones fijas, versión de Python, estructura de carpetas, tiempo total y un comando único para la demo. La etiqueta `v1.0-entrega` se crea justo después de esta revisión |
| Análisis y comunicación al cliente | 4 | La memoria empieza con un resumen ejecutivo que se entiende sin leer el resto, las cifras son las mismas en memoria, README, *model card* y cuaderno, y las recomendaciones están priorizadas con lo que hay que hacer antes de un despliegue real y lo que **no** debe hacerse |
| IA responsable | 4 | Registro de 9 riesgos cerrado con estado y evidencia, clasificación justificada, supervisión humana y transparencia explicadas, y se cuenta una mitigación que empeoró (reponderar la hora punta: baja la franja y sube el global) y qué se decidió; el uso de IA dice qué se pidió, qué se revisó y qué se cambió |

**Lo primero que mejoraríamos:** avisar mejor en hora punta y en festivos (el rango cubre solo el 78 % y el 64 %), grabar el vídeo plan B antes de la congelación y pedir una previsión meteorológica real para sustituir el clima del histórico. **Lo que falló en la prueba en limpio:** al ejecutar `pytest` salían 21 avisos de deprecación de pandas en `logica.py` (`pd.Timedelta(days=1)` con numpy 2.5). Se cambió por `pd.DateOffset(days=1)`, se repitió la prueba y ahora pasa sin avisos.
