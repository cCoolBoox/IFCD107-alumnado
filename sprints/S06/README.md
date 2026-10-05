# Sprint 6 · Datos listos para modelar

**Pregunta guía:** ¿están los datos en condiciones de entrenar algo fiable?
**Fechas:** 3–5 de noviembre · **Horas:** 11 h (4 h teoría · 4 h práctica guiada · 3 h PBL)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_06.pdf`](Guia_Sprint_06.pdf)
- 🖥️ **S06.1 · Datos pandas y visualizacion exploratoria:** [`S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf`](presentaciones/S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf)
- 🖥️ **S06.2 · Limpieza y preprocesado:** [`S06.2_Limpieza_y_preprocesado.pdf`](presentaciones/S06.2_Limpieza_y_preprocesado.pdf)
- 🖥️ **S06.3 · scikit learn metricas y validacion:** [`S06.3_scikit_learn_metricas_y_validacion.pdf`](presentaciones/S06.3_scikit_learn_metricas_y_validacion.pdf)

**Contenidos:** M2 (rol del Data Scientist, pandas, visualización, limpieza y preprocesado) y M3 UD 3.1–3.2 (flujo con scikit-learn, pipelines, métricas y validación).

## Qué aprenderás
- Explorar una tabla con pandas y encontrar sus defectos (nulos, duplicados, *outliers*, fechas y categorías mal formadas).
- Construir un **pipeline** reproducible (`ColumnTransformer` + `Pipeline`) sin fuga de datos.
- Medir un modelo con honestidad: *baseline*, métricas y validación cruzada.
- Hace falta haber visto los Sprints 4 y 5 (Python, NumPy y pandas básicos).

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S06_01_pandas_eda` | pandas, EDA y visualización exploratoria; primer chequeo de calidad | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/S06_01_pandas_eda.ipynb) |
| `S06_02_limpieza` | Limpieza: duplicados, tipos, fechas, categorías, imposibles, nulos | 70 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/S06_02_limpieza.ipynb) |
| `S06_03_preprocesado_pipeline` | Escalado, codificación, `ColumnTransformer` y `Pipeline` | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/S06_03_preprocesado_pipeline.ipynb) |
| `S06_04_metricas_validacion` | Baseline, métricas, sobreajuste, validación cruzada, fuga y partición temporal | 65 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/S06_04_metricas_validacion.ipynb) |

Cada notebook tiene ejercicios con `assert`: si la celda de comprobación no da error, vas bien. Los datos se descargan solos.

## Reto · «Datos sucios, cliente impaciente»
**Contexto:** TurisData Canarias nos envía `reservas_sucio.csv`, exportado a mano desde varios sistemas. Quieren un primer modelo de cancelaciones, pero el gerente no se fía de los datos. Pide un informe corto de qué está mal y por qué, y un proceso que deje los datos listos cada vez.

**Entregáis** (carpeta `sprint-06/` del repositorio del equipo):
- `informe_calidad.md` (1–2 páginas): defectos, causa probable, tratamiento y preguntas al cliente. Plantilla: [`informe_calidad_plantilla.md`](informe_calidad_plantilla.md).
- `reto_S06.ipynb`: EDA, función de limpieza, *pipeline* y *baseline* con validación cruzada.
- `README.md` con las instrucciones y versiones para reproducirlo.

**Reglas:**
- 3 h en equipo; solo librerías del curso. Nada de editar el CSV a mano: toda corrección va en código.
- Lo aprendido de los datos (medianas, categorías…) se ajusta **solo con train**. No se descarta ninguna fila sin justificarla.
- Nunca claves ni datos personales. Review: 5 min por equipo (3 defectos graves y *pipeline* en marcha).

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (¿y si el país de origen se imputa mal?).

## ✅ Antes de cerrar el sprint
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] El informe recoge cada defecto con causa probable y tratamiento
- [ ] El notebook se ejecuta de principio a fin (`Restart & Run all`)
- [ ] Hay *baseline* (`DummyClassifier`) y un modelo, comparados con validación cruzada
- [ ] Entregable subido a la carpeta `sprint-06/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
