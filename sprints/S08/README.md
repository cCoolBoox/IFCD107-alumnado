# Sprint 8 · Árboles, ensembles y SVM

**Pregunta guía:** ¿cuál es el mejor modelo y cuánto nos cuesta mantenerlo?
**Fechas:** 10–11 de noviembre · **Horas:** 12 h (3 h teoría · 4 h práctica guiada · 5 h PBL)

> 🎯 **Reto de este sprint: «Duelo de modelos».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_08.md) · [Reto en PDF](guia/Reto_Sprint_08.pdf) ([ecofriendly](guia/Reto_Sprint_08_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_08.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_08.pdf) · [ecofriendly, para imprimir](README_Sprint_08_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_08.pdf`](guia/Guia_Sprint_08.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_08_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_08.md`](guia/Reto_Sprint_08.md)
- 🖥️ **S08.1 · Arboles de decision:** [`S08.1_Arboles_de_decision.pdf`](presentaciones/S08.1_Arboles_de_decision.pdf)
- 🖥️ **S08.2 · Ensembles Random Forest y Boosting:** [`S08.2_Ensembles_Random_Forest_y_Boosting.pdf`](presentaciones/S08.2_Ensembles_Random_Forest_y_Boosting.pdf)
- 🖥️ **S08.3 · Maquinas de vectores de soporte:** [`S08.3_Maquinas_de_vectores_de_soporte.pdf`](presentaciones/S08.3_Maquinas_de_vectores_de_soporte.pdf)

**Contenidos:** M3 UD 3.6 (árboles de decisión), UD 3.7 (Random Forest, Gradient Boosting, XGBoost y LightGBM) y UD 3.8 (SVM), más ajuste de hiperparámetros (`GridSearchCV`, `RandomizedSearchCV`).
**Evaluación:** test de M3 (parte 2, el 11/11) y reto PBL «Duelo de modelos».

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto · [`tests/`](tests/) test de conocimientos

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Martes 10/11**

1. 🔔 **Ceremonia**: Planning del reto «Duelo de modelos» y pesos de los criterios (la «voz del cliente») · _15 min_
2. 📖 **Teoría**: [Árboles de decisión](presentaciones/S08.1_Arboles_de_decision.pdf) · _30 min_
3. 💻 **Práctica**: [Árbol de decisión: reglas, poda e importancia](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_01_arboles_decision.ipynb) · _35 min_
4. 📖 **Teoría**: [Ensembles: Random Forest y *boosting*](presentaciones/S08.2_Ensembles_Random_Forest_y_Boosting.pdf) · _50 min_
5. 💻 **Práctica**: [Random Forest: bagging, OOB e importancia por permutación](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_02_random_forest.ipynb) · _35 min_
6. 💻 **Práctica**: [Gradient Boosting, XGBoost y LightGBM](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_03_boosting_xgboost_lightgbm.ipynb) · _45 min_
7. 🎯 **Reto**: [Primeros modelos en el *leaderboard* (*baseline*, logística, árbol y bosque; pasos 1–2)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_06_leaderboard_plantilla.ipynb) · _40 min_

**Miércoles 11/11**

8. 📖 **Teoría**: [Máquinas de vectores de soporte (SVM)](presentaciones/S08.3_Maquinas_de_vectores_de_soporte.pdf) · _25 min_
9. 💻 **Práctica**: [SVM: margen, kernels, `C` y `gamma`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_04_svm.ipynb) · _30 min_
10. 💻 **Práctica**: [`GridSearchCV` y `RandomizedSearchCV`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_05_busqueda_hiperparametros.ipynb) · _35 min_
11. 🎯 **Reto**: [Búsqueda de hiperparámetros para una familia, la que elijáis (paso 3)](guia/Reto_Sprint_08.md) · _30 min_
12. 🎯 **Reto**: [Sensibilidad de los pesos, elegir el campeón, test **una sola vez**, ficha del modelo y README (pasos 4–5)](guia/Reto_Sprint_08.md) · _1 h 5 min_
13. 📝 **Test**: [**Test de M3 (parte 2)**, solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/tests/test_M3_parte2.html) · _25 min_
14. 🔔 **Ceremonia**: Entrega en `sprint-08/`, autoevaluación y coevaluación, review y retrospectiva · _40 min_

<!--orden:fin-->

## Qué aprenderás
- Entrenar y podar un **árbol de decisión**; entender bosques aleatorios y *boosting* (XGBoost, LightGBM).
- Ajustar una **SVM** y buscar hiperparámetros con `GridSearchCV` y `RandomizedSearchCV`.
- **Elegir un modelo campeón** justificando rendimiento, explicabilidad y coste.
- Hace falta lo de los Sprints 6 y 7; en local: `pip install xgboost lightgbm`.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S08_01_arboles_decision` | Árbol de decisión: reglas, sobreajuste, poda, importancia | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_01_arboles_decision.ipynb) |
| `S08_02_random_forest` | Random Forest: bagging, OOB, importancia por permutación | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_02_random_forest.ipynb) |
| `S08_03_boosting_xgboost_lightgbm` | Gradient Boosting, XGBoost, LightGBM y parada temprana | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_03_boosting_xgboost_lightgbm.ipynb) |
| `S08_04_svm` | SVM: margen, kernels, `C`, `gamma`, escalado y coste | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_04_svm.ipynb) |
| `S08_05_busqueda_hiperparametros` | `GridSearchCV`, `RandomizedSearchCV`, `cv_results_`, test final | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_05_busqueda_hiperparametros.ipynb) |
| `S08_06_leaderboard_plantilla` | **Herramienta del reto**: leaderboard para rellenar | dentro del reto | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_06_leaderboard_plantilla.ipynb) |

Las cinco primeras son prácticas guiadas; la sexta es la plantilla del reto. Los ejercicios se autocorrigen con `assert`.

## Reto · «Duelo de modelos»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_08.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** TurisData ya sabe predecir cancelaciones y ahora quiere saber qué modelo poner en producción: ¿el más preciso, el más comprensible o el más barato de mantener? Enfrentáis árboles, bosques, *boosting* y SVM y elegís un campeón con argumentos.

**Entregáis** (carpeta `sprint-08/` del repositorio del equipo):
- `leaderboard_S08.csv` con ≥ 6 modelos (*baseline* y logística incluidos). Plantilla: [`leaderboard_plantilla.csv`](plantillas/leaderboard_plantilla.csv).
- `model_card.md` del campeón (1–2 páginas). Plantilla: [`model_card_plantilla.md`](plantillas/model_card_plantilla.md).
- `reto_S08.ipynb` con la comparación y la búsqueda de hiperparámetros de al menos dos familias.
- `README.md` (versiones, semilla, orden de ejecución).

**Reglas:**
- Unas 4 h en equipo; máx. 8 modelos; cada búsqueda, 5 min como máximo en Colab; `SEMILLA = 42`.
- Búsqueda solo sobre train; el test se usa una vez, solo con el campeón.
- Nunca claves ni datos personales. Review: 5 min por equipo.

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (usos no previstos, deriva, país de origen), más campeón justificado con rendimiento, explicabilidad y coste.

## 📝 Test de conocimientos · mié 11/11
**Test de M3 · parte 2** · 10 preguntas · unos 20 min · individual, en el navegador, sin penalización por fallo. Cubre M3, UD 3.5 a 3.8 (k-NN y Naive Bayes, árboles, ensembles y SVM).

👉 **[Abrir el test](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/tests/test_M3_parte2.html)** (`https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/tests/test_M3_parte2.html`)

**Solo se abre el día mié 11/11** (hora de Canarias). Al terminar, copia tu resultado y envíaselo al docente. Cuenta para el 30 % de «tests de conocimientos».

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mié 11/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Leaderboard con ≥ 6 modelos de al menos 4 familias
- [ ] Hiperparámetros buscados con validación cruzada en train para dos familias
- [ ] AUC de test calculado una sola vez y `model_card.md` completa
- [ ] Entregable subido a la carpeta `sprint-08/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
