# README Sprint S06 · Datos listos para modelar

**Pregunta guía:** ¿están los datos en condiciones de entrenar algo fiable?
**Fechas:** 4–5 de noviembre · **Horas:** 12 h (4 h teoría · 4 h práctica guiada · 4 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_06.pdf) · [ecofriendly, para imprimir](README_Sprint_06_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. Explorar una tabla con pandas y elegir el gráfico adecuado para cada tipo de dato.
2. Encontrar defectos en un dataset (nulos, duplicados, *outliers*, tipos y fechas mal formados, categorías inconsistentes) y **razonar de dónde vienen**.
3. Construir un **pipeline** reproducible (`ColumnTransformer` + `Pipeline`) que impute, escale y codifique sin fuga de datos.
4. Medir un modelo con honestidad: *baseline*, métricas, validación cruzada, partición temporal.
5. Reconocer y evitar la **fuga de datos** (*data leakage*).

## Requisitos previos
- Sprint 4 y 5: Python básico, NumPy y algo de estadística con pandas.
- Cuenta de Google (para Colab) o el entorno local del curso (Python 3.11).
- Datos: `datos/reservas_turisdata.csv` (limpio) y `datos/reservas_sucio.csv` (el del reto). Los notebooks los descargan solos si no los encuentran.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_06.pdf) · [ecofriendly](guia/Guia_Sprint_06_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_06.md) · [PDF](guia/Reto_Sprint_06.pdf) · [ecofriendly](guia/Reto_Sprint_06_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S06_00_resumen_del_sprint.png) | Lámina con la pregunta del cliente, los pasos, lo que se entrega y lo que se aprende | — | Antes del planning |
| [Infografías del reto](infografias/) | 3 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf`](presentaciones/S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf) | Datos, pandas y visualización exploratoria | 15 min | Teoría · miércoles 4/11 |
| [`S06.2_Limpieza_y_preprocesado.pdf`](presentaciones/S06.2_Limpieza_y_preprocesado.pdf) | Limpieza y preprocesado | 20 min | Teoría · miércoles 4/11 |
| [`S06.3_scikit_learn_metricas_y_validacion.pdf`](presentaciones/S06.3_scikit_learn_metricas_y_validacion.pdf) | scikit-learn: métricas y validación | 15 min | Teoría · jueves 5/11 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S06_01_pandas_eda` | pandas, EDA y visualización exploratoria; primer chequeo de calidad | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_01_pandas_eda.ipynb) |
| `S06_02_limpieza` | Limpieza: duplicados, tipos, fechas, categorías, imposibles, nulos | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_02_limpieza.ipynb) |
| `S06_03_preprocesado_pipeline` | Escalado, codificación, `ColumnTransformer` y `Pipeline` | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_03_preprocesado_pipeline.ipynb) |
| `S06_04_metricas_validacion` | Baseline, métricas, sobreajuste, validación cruzada, fuga y partición temporal | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_04_metricas_validacion.ipynb) |

Cada notebook tiene ejercicios con `assert`: si la celda de comprobación no da error, vas bien. Los datos se descargan solos.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Miércoles 4/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Datos sucios, cliente impaciente» y reparto de roles | 10 min |
| 2 | 📖 Teoría | [Datos, pandas y visualización exploratoria](presentaciones/S06.1_Datos_pandas_y_visualizacion_exploratoria.pdf) | 15 min |
| 3 | 💻 Práctica | [pandas, EDA y primer chequeo de calidad](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_01_pandas_eda.ipynb) | 45 min |
| 4 | 🎯 Reto | [Arrancar el inventario de defectos del fichero sucio (pasos 1–2)](guia/Reto_Sprint_06.md) | 30 min |
| 5 | 📖 Teoría | [Limpieza y preprocesado](presentaciones/S06.2_Limpieza_y_preprocesado.pdf) | 20 min |
| 6 | 💻 Práctica | [Limpieza: duplicados, tipos, fechas, categorías, imposibles y nulos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_02_limpieza.ipynb) | 55 min |
| 7 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 25 min |

**Jueves 5/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 8 | 💻 Práctica | [Escalado, codificación, `ColumnTransformer` y `Pipeline`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_03_preprocesado_pipeline.ipynb) | 40 min |
| 9 | 🎯 Reto | [Función de limpieza, partición train/test, *pipeline* y *baseline* (pasos 3–4)](guia/Reto_Sprint_06.md) | 35 min |
| 10 | 📖 Teoría | [scikit-learn: métricas y validación](presentaciones/S06.3_scikit_learn_metricas_y_validacion.pdf) | 15 min |
| 11 | 💻 Práctica | [*Baseline*, métricas, validación cruzada y fuga de datos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_04_metricas_validacion.ipynb) | 45 min |
| 12 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 10 min |
| 13 | 🎯 Reto | [Informe, README y ensayo (paso 5)](guia/Reto_Sprint_06.md) | 20 min |
| 14 | 🔔 Ceremonia | Entrega en `sprint-06/`, autoevaluación y coevaluación, review y retrospectiva | 35 min |

<!--orden:fin-->

## Reto · «Datos sucios, cliente impaciente»

📄 [Reto en PDF](guia/Reto_Sprint_06.pdf) · [ecofriendly](guia/Reto_Sprint_06_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

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
