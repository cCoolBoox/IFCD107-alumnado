# README Sprint S08 · Árboles, ensembles y SVM

**Pregunta guía:** ¿cuál es el mejor modelo y cuánto nos cuesta mantenerlo?
**Fechas:** 11–12 de noviembre · **Horas:** 9 h (2 h teoría · 3 h práctica · 4 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_08.pdf) · [ecofriendly, para imprimir](README_Sprint_08_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. Entrenar un **árbol de decisión**, detectar su sobreajuste, podarlo y leer sus reglas y su importancia de variables.
2. Explicar la diferencia entre **bosque aleatorio** (promediar árboles) y **boosting** (corregir errores en cadena), y usar XGBoost y LightGBM con parada temprana.
3. Ajustar una **SVM** (`C`, `gamma`, kernel) y saber cuándo su coste la descarta.
4. Buscar hiperparámetros con **`GridSearchCV`** y **`RandomizedSearchCV`** sin engañarte con la nota de validación.
5. **Elegir un modelo campeón** justificando rendimiento, explicabilidad y coste, y documentarlo en una *model card*.

## Requisitos previos
- Sprint 6 y 7: pipelines, validación cruzada, métricas de clasificación (AUC, precisión, recall), umbral y regresión logística como referencia.
- Datos: `datos/reservas_turisdata.csv` (objetivo `cancelada`). Los notebooks lo descargan solos si no lo encuentran.
- Librerías: scikit-learn, xgboost y lightgbm (vienen instaladas en Colab; en local: `pip install xgboost lightgbm`).

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_08.pdf) · [ecofriendly](guia/Guia_Sprint_08_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [**Carpeta del reto: `Reto_S08/`**](Reto_S08/) | Todo el material del reto junto: ficha (.md y PDF), plantillas y material de apoyo, hoja de autoevaluación y coevaluación y láminas del reto | — | Antes del planning y durante el reto |
| [Reto completo, paso a paso (.md)](Reto_S08/Reto_Sprint_08.md) · [PDF](Reto_S08/Reto_Sprint_08.pdf) · [ecofriendly](Reto_S08/Reto_Sprint_08_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S08_00_resumen_del_sprint.png) | Lámina con la pregunta guía, qué aprenderás, cómo se reparte el sprint (teoría, práctica y reto) y dónde estás en el curso | — | Antes del planning |
| [El reto paso a paso](Reto_S08/S08_03_reto_paso_a_paso.png) · [PDF con enlaces](Reto_S08/S08_03_reto_paso_a_paso.pdf) | Los pasos del reto con su día y minutos, el material de cada paso, los errores frecuentes y el uso de la IA | — | Durante el reto |
| [Esquema del contenido y su relación con el reto](infografias/S08_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del sprint](infografias/) | 3 láminas ilustradas | — | Antes del planning y durante el reto |
| [Atlas de algoritmos](infografias/S08_03_atlas_arboles_ensembles_y_svm.png) | Atlas de algoritmos del sprint: árbol, Random Forest, boosting, SVM y ajuste de hiperparámetros | — | Teoría y práctica; consulta cuando elijas modelo |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S08.1_Arboles_de_decision.pdf`](presentaciones/S08.1_Arboles_de_decision.pdf) | Árboles de decisión | 15 min | Teoría · día 1 del S08 |
| [`S08.2_Ensembles_Random_Forest_y_Boosting.pdf`](presentaciones/S08.2_Ensembles_Random_Forest_y_Boosting.pdf) | Ensembles: Random Forest y *boosting* | 20 min | Teoría · día 1 del S08 |
| [`S08.3_Maquinas_de_vectores_de_soporte.pdf`](presentaciones/S08.3_Maquinas_de_vectores_de_soporte.pdf) | Máquinas de vectores de soporte (SVM) | 15 min | Teoría · día 2 del S08 |
| [Test de conocimientos](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/tests/test_M3_parte2.html) | Test de M3 · parte 2 · 10 preguntas · individual, en el navegador, sin penalización por fallo.5 a 3.8 (k-NN y Naive Bayes, árboles, ensembles y SVM). | 20 min | Solo se abre el mié 11/11 (hora de Canarias) |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| [`apuntes_arboles_ensembles_y_svm.md`](actividades/apuntes_arboles_ensembles_y_svm.md) · [PDF](actividades/apuntes_arboles_ensembles_y_svm.pdf) · [ecofriendly](actividades/apuntes_arboles_ensembles_y_svm_ecofriendly.pdf) | **Apuntes que complementan las diapositivas**: árboles de decisión, Random Forest, boosting, SVM, hiperparámetros y cómo elegir un campeón (rendimiento, explicabilidad y coste) explicados con ejemplos que puedes calcular a mano | — | Antes del sprint y cuando tengas dudas |
| `S08_01_arboles_decision` | Árbol de decisión: reglas, sobreajuste, poda, importancia | 35 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_01_arboles_decision.ipynb) |
| `S08_02_random_forest` | Random Forest: bagging, OOB, importancia por permutación | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_02_random_forest.ipynb) |
| `S08_03_boosting_xgboost_lightgbm` | Gradient Boosting, XGBoost, LightGBM y parada temprana | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_03_boosting_xgboost_lightgbm.ipynb) |
| `S08_04_svm` | SVM: margen, kernels, `C`, `gamma`, escalado y coste | 30 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_04_svm.ipynb) |
| `S08_05_busqueda_hiperparametros` | `GridSearchCV`, `RandomizedSearchCV`, `cv_results_`, test final | 30 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_05_busqueda_hiperparametros.ipynb) |
| `S08_06_leaderboard_plantilla` | **Herramienta del reto**: leaderboard para rellenar | dentro del reto | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_06_leaderboard_plantilla.ipynb) |

Las cinco primeras son prácticas guiadas; la sexta es la plantilla del reto. Los ejercicios se autocorrigen con `assert`.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Día 1 del S08**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Duelo de modelos» y pesos de los criterios (la «voz del cliente») | 10 min |
| 2 | 📖 Teoría | [Árboles de decisión](presentaciones/S08.1_Arboles_de_decision.pdf) | 25 min |
| 3 | 💻 Práctica | [Árbol de decisión: reglas, poda e importancia (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_01_arboles_decision.ipynb) | 35 min |
| 4 | 📖 Teoría | [Ensembles: Random Forest y *boosting*](presentaciones/S08.2_Ensembles_Random_Forest_y_Boosting.pdf) | 25 min |

**Día 2 del S08**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 5 | 📖 Teoría | [Máquinas de vectores de soporte (SVM), versión corta](presentaciones/S08.3_Maquinas_de_vectores_de_soporte.pdf) | 10 min |
| 6 | 💻 Práctica | [Random Forest: bagging, OOB e importancia por permutación (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_02_random_forest.ipynb) | 30 min |
| 7 | 💻 Práctica | [Gradient Boosting, XGBoost y LightGBM (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_03_boosting_xgboost_lightgbm.ipynb) | 25 min |
| 8 | 🎯 Reto | [*Leaderboard* (*baseline*, logística, árbol y bosque), búsqueda de hiperparámetros para una familia, sensibilidad de los pesos, campeón, test **una sola vez**, ficha del modelo y README (pasos 1–5)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_06_leaderboard_plantilla.ipynb) | 1 h 15 min |
| 9 | 📝 Test | [**Test de M3 (parte 2)**, solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/tests/test_M3_parte2.html) | 25 min |
| 10 | 🔔 Ceremonia | Entrega en `sprint-08/`, autoevaluación y coevaluación, y review y retrospectiva de los Sprints 7 y 8 | 35 min |

<!--orden:fin-->

## Reto · «Duelo de modelos»

📄 [Reto en PDF](Reto_S08/Reto_Sprint_08.pdf) · [ecofriendly](Reto_S08/Reto_Sprint_08_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](Reto_S08/Reto_Sprint_08.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** TurisData ya sabe predecir cancelaciones y ahora quiere saber qué modelo poner en producción: ¿el más preciso, el más comprensible o el más barato de mantener? Enfrentáis árboles, bosques, *boosting* y SVM y elegís un campeón con argumentos.


**Entregáis** (carpeta `sprint-08/` del repositorio del equipo):
- `leaderboard_S08.csv` con ≥ 6 modelos (*baseline* y logística incluidos). Plantilla: [`leaderboard_plantilla.csv`](Reto_S08/leaderboard_plantilla.csv).
- `model_card.md` del campeón (1–2 páginas). Plantilla: [`model_card_plantilla.md`](Reto_S08/model_card_plantilla.md).
- `reto_S08.ipynb` con la comparación y la búsqueda de hiperparámetros de al menos dos familias.
- `README.md` (versiones, semilla, orden de ejecución).


**Reglas:**
- Unas 2 h 15 min en equipo (planning, reto y entrega); máx. 8 modelos; cada búsqueda, 5 min como máximo en Colab; `SEMILLA = 42`.
- Búsqueda solo sobre train; el test se usa una vez, solo con el campeón.
- Nunca claves ni datos personales. Review: 5 min por equipo.


**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (usos no previstos, deriva, país de origen), más campeón justificado con rendimiento, explicabilidad y coste.

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el jue 12/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Leaderboard con ≥ 6 modelos de al menos 4 familias
- [ ] Hiperparámetros buscados con validación cruzada en train para dos familias
- [ ] AUC de test calculado una sola vez y `model_card.md` completa
- [ ] Entregable subido a la carpeta `sprint-08/` del repositorio del equipo
- [ ] [Autoevaluación y coevaluación](Reto_S08/autoevaluacion_y_coevaluacion.md) rellenadas
