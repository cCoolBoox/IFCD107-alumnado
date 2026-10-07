# Sprint 8 · Árboles, ensembles y SVM

**Pregunta guía:** ¿cuál es el mejor modelo y cuánto nos cuesta mantenerlo?
**Fechas:** 9–11 de noviembre · **Horas:** 11 h (3 h teoría · 5 h práctica guiada · 3 h PBL)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_08.pdf`](Guia_Sprint_08.pdf)
- 🖥️ **S08.1 · Arboles de decision:** [`S08.1_Arboles_de_decision.pdf`](presentaciones/S08.1_Arboles_de_decision.pdf)
- 🖥️ **S08.2 · Ensembles Random Forest y Boosting:** [`S08.2_Ensembles_Random_Forest_y_Boosting.pdf`](presentaciones/S08.2_Ensembles_Random_Forest_y_Boosting.pdf)
- 🖥️ **S08.3 · Maquinas de vectores de soporte:** [`S08.3_Maquinas_de_vectores_de_soporte.pdf`](presentaciones/S08.3_Maquinas_de_vectores_de_soporte.pdf)

**Contenidos:** M3 UD 3.6 (árboles de decisión), UD 3.7 (Random Forest, Gradient Boosting, XGBoost y LightGBM) y UD 3.8 (SVM), más ajuste de hiperparámetros (`GridSearchCV`, `RandomizedSearchCV`).
**Evaluación:** test de M3 (parte 2, el 11/11) y reto PBL «Duelo de modelos».

## Qué aprenderás
- Entrenar y podar un **árbol de decisión**; entender bosques aleatorios y *boosting* (XGBoost, LightGBM).
- Ajustar una **SVM** y buscar hiperparámetros con `GridSearchCV` y `RandomizedSearchCV`.
- **Elegir un modelo campeón** justificando rendimiento, explicabilidad y coste.
- Hace falta lo de los Sprints 6 y 7; en local: `pip install xgboost lightgbm`.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S08_01_arboles_decision` | Árbol de decisión: reglas, sobreajuste, poda, importancia | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/S08_01_arboles_decision.ipynb) |
| `S08_02_random_forest` | Random Forest: bagging, OOB, importancia por permutación | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/S08_02_random_forest.ipynb) |
| `S08_03_boosting_xgboost_lightgbm` | Gradient Boosting, XGBoost, LightGBM y parada temprana | 65 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/S08_03_boosting_xgboost_lightgbm.ipynb) |
| `S08_04_svm` | SVM: margen, kernels, `C`, `gamma`, escalado y coste | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/S08_04_svm.ipynb) |
| `S08_05_busqueda_hiperparametros` | `GridSearchCV`, `RandomizedSearchCV`, `cv_results_`, test final | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/S08_05_busqueda_hiperparametros.ipynb) |
| `S08_06_leaderboard_plantilla` | **Herramienta del reto**: leaderboard para rellenar | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/S08_06_leaderboard_plantilla.ipynb) |

Las cinco primeras son prácticas guiadas; la sexta es la plantilla del reto. Los ejercicios se autocorrigen con `assert`.

## Reto · «Duelo de modelos»
**Contexto:** TurisData ya sabe predecir cancelaciones y ahora quiere saber qué modelo poner en producción: ¿el más preciso, el más comprensible o el más barato de mantener? Enfrentáis árboles, bosques, *boosting* y SVM y elegís un campeón con argumentos.

**Entregáis** (carpeta `sprint-08/` del repositorio del equipo):
- `leaderboard_S08.csv` con ≥ 6 modelos (*baseline* y logística incluidos). Plantilla: [`leaderboard_plantilla.csv`](leaderboard_plantilla.csv).
- `model_card.md` del campeón (1–2 páginas). Plantilla: [`model_card_plantilla.md`](model_card_plantilla.md).
- `reto_S08.ipynb` con la comparación y la búsqueda de hiperparámetros de al menos dos familias.
- `README.md` (versiones, semilla, orden de ejecución).

**Reglas:**
- 3 h en equipo; máx. 8 modelos; cada búsqueda, 5 min como máximo en Colab; `SEMILLA = 42`.
- Búsqueda solo sobre train; el test se usa una vez, solo con el campeón.
- Nunca claves ni datos personales. Review: 5 min por equipo.

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (usos no previstos, deriva, país de origen), más campeón justificado con rendimiento, explicabilidad y coste.

## 📝 Test de conocimientos · mié 11/11
**Test de M3 · parte 2** · 10 preguntas · unos 20 min · individual, en el navegador, sin penalización por fallo. Cubre M3, UD 3.5 a 3.8 (k-NN y Naive Bayes, árboles, ensembles y SVM).

👉 **[Abrir el test](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/test_M3_parte2.html)** (`https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/test_M3_parte2.html`)

**Solo se abre el día mié 11/11** (hora de Canarias). Al terminar, copia tu resultado y envíaselo al docente. Cuenta para el 30 % de «tests de conocimientos».

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mié 11/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Leaderboard con ≥ 6 modelos de al menos 4 familias
- [ ] Hiperparámetros buscados con validación cruzada en train para dos familias
- [ ] AUC de test calculado una sola vez y `model_card.md` completa
- [ ] Entregable subido a la carpeta `sprint-08/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
