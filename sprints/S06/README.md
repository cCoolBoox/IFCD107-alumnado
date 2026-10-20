# Sprint 6 · Datos listos para modelar

**Pregunta guía:** ¿están los datos en condiciones de entrenar algo fiable?
**Fechas:** 4–5 de noviembre · **Horas:** 12 h (4 h teoría · 4 h práctica guiada · 4 h PBL)

> 🎯 **Reto de este sprint: «Datos sucios, cliente impaciente».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_06.md) · [Reto en PDF](guia/Reto_Sprint_06.pdf) ([ecofriendly](guia/Reto_Sprint_06_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_06.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_06.pdf) · [ecofriendly, para imprimir](README_Sprint_06_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_06.pdf`](guia/Guia_Sprint_06.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_06_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_06.md`](guia/Reto_Sprint_06.md)
- 🖥️ **S06.1 · Datos pandas y visualizacion exploratoria:** [`S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf`](presentaciones/S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf)
- 🖥️ **S06.2 · Limpieza y preprocesado:** [`S06.2_Limpieza_y_preprocesado.pdf`](presentaciones/S06.2_Limpieza_y_preprocesado.pdf)
- 🖥️ **S06.3 · scikit learn metricas y validacion:** [`S06.3_scikit_learn_metricas_y_validacion.pdf`](presentaciones/S06.3_scikit_learn_metricas_y_validacion.pdf)

**Contenidos:** M2 (rol del Data Scientist, pandas, visualización, limpieza y preprocesado) y M3 UD 3.1–3.2 (flujo con scikit-learn, pipelines, métricas y validación).

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Miércoles 4/11**

1. 🔔 **Ceremonia**: Planning del reto «Datos sucios, cliente impaciente» y reparto de roles · _15 min_
2. 📖 **Teoría**: [Datos, pandas y visualización exploratoria](presentaciones/S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf) · _40 min_
3. 💻 **Práctica**: [pandas, EDA y primer chequeo de calidad](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_01_pandas_eda.ipynb) · _45 min_
4. 🎯 **Reto**: [Arrancar el inventario de defectos del fichero sucio (pasos 1–2)](guia/Reto_Sprint_06.md) · _50 min_
5. 📖 **Teoría**: [Limpieza y preprocesado](presentaciones/S06.2_Limpieza_y_preprocesado.pdf) · _45 min_
6. 💻 **Práctica**: [Limpieza: duplicados, tipos, fechas, categorías, imposibles y nulos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_02_limpieza.ipynb) · _55 min_

**Jueves 5/11**

7. 💻 **Práctica**: [Escalado, codificación, `ColumnTransformer` y `Pipeline`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_03_preprocesado_pipeline.ipynb) · _40 min_
8. 🎯 **Reto**: [Función de limpieza, partición train/test, *pipeline* y *baseline* (pasos 3–4)](guia/Reto_Sprint_06.md) · _1 h_
9. 📖 **Teoría**: [scikit-learn: métricas y validación](presentaciones/S06.3_scikit_learn_metricas_y_validacion.pdf) · _45 min_
10. 💻 **Práctica**: [*Baseline*, métricas, validación cruzada y fuga de datos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_04_metricas_validacion.ipynb) · _45 min_
11. 🎯 **Reto**: [Informe, README y ensayo (paso 5)](guia/Reto_Sprint_06.md) · _25 min_
12. 🔔 **Ceremonia**: Entrega en `sprint-06/`, autoevaluación y coevaluación, review y retrospectiva · _35 min_

<!--orden:fin-->

## Qué aprenderás
- Explorar una tabla con pandas y encontrar sus defectos (nulos, duplicados, *outliers*, fechas y categorías mal formadas).
- Construir un **pipeline** reproducible (`ColumnTransformer` + `Pipeline`) sin fuga de datos.
- Medir un modelo con honestidad: *baseline*, métricas y validación cruzada.
- Hace falta haber visto los Sprints 4 y 5 (Python, NumPy y pandas básicos).

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S06_01_pandas_eda` | pandas, EDA y visualización exploratoria; primer chequeo de calidad | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_01_pandas_eda.ipynb) |
| `S06_02_limpieza` | Limpieza: duplicados, tipos, fechas, categorías, imposibles, nulos | 65 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_02_limpieza.ipynb) |
| `S06_03_preprocesado_pipeline` | Escalado, codificación, `ColumnTransformer` y `Pipeline` | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_03_preprocesado_pipeline.ipynb) |
| `S06_04_metricas_validacion` | Baseline, métricas, sobreajuste, validación cruzada, fuga y partición temporal | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_04_metricas_validacion.ipynb) |

Cada notebook tiene ejercicios con `assert`: si la celda de comprobación no da error, vas bien. Los datos se descargan solos.

## Reto · «Datos sucios, cliente impaciente»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_06.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** TurisData Canarias nos envía `reservas_sucio.csv`, exportado a mano desde varios sistemas. Quieren un primer modelo de cancelaciones, pero el gerente no se fía de los datos. Pide un informe corto de qué está mal y por qué, y un proceso que deje los datos listos cada vez.

**Entregáis** (carpeta `sprint-06/` del repositorio del equipo):
- `informe_calidad.md` (1–2 páginas): defectos, causa probable, tratamiento y preguntas al cliente. Plantilla: [`informe_calidad_plantilla.md`](plantillas/informe_calidad_plantilla.md).
- `reto_S06.ipynb`: EDA, función de limpieza, *pipeline* y *baseline* con validación cruzada.
- `README.md` con las instrucciones y versiones para reproducirlo.

**Reglas:**
- Unas 3 h 45 min en equipo; solo librerías del curso. Nada de editar el CSV a mano: toda corrección va en código.
- Lo aprendido de los datos (medianas, categorías…) se ajusta **solo con train**. No se descarta ninguna fila sin justificarla.
- Nunca claves ni datos personales. Review: 5 min por equipo (3 defectos graves y *pipeline* en marcha).

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (¿y si el país de origen se imputa mal?).

## ✅ Antes de cerrar el sprint
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] El informe recoge cada defecto con causa probable y tratamiento
- [ ] Hay *baseline* (`DummyClassifier`) y un modelo, comparados con validación cruzada
- [ ] Entregable subido a la carpeta `sprint-06/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
