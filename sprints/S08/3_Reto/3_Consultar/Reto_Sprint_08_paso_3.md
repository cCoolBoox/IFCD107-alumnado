# Paso 3 · *Boosting*, SVM y búsqueda de hiperparámetros (día 2, 25 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 4 →](Reto_Sprint_08_paso_4.md)
<!--/nav-->

1. Registrar un modelo de *boosting* y una SVM.
2. Buscar hiperparámetros en **dos familias** (rejilla o aleatoria), solo con train y validación cruzada, sin pasar de 5 minutos cada búsqueda.
3. Registrar los mejores modelos y actualizar el `catalogo` del cuaderno.
4. Comprobar que hay entre 6 y 8 modelos, de al menos 4 familias.

**Cómo se hace**
- **Los dos modelos que faltan.** Mismo patrón que en el paso 2 (pistas en [`S08_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_03_boosting_xgboost_lightgbm.ipynb) y [`S08_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_04_svm.ipynb)):

| Modelo (nombre) | Familia | Qué le pasáis a `hacer_pipe` | Explicabilidad |
|---|---|---|---|
| `lightgbm` | `ensemble_boosting` | `lgb.LGBMClassifier(n_estimators=100, learning_rate=0.05, num_leaves=8, random_state=SEMILLA, n_jobs=2, verbose=-1)` | 2 |
| `svm_rbf` | `svm` | `SVC(kernel="rbf", C=1, probability=True, random_state=SEMILLA)` con `escalar=True` | 1 |

  Podéis añadir también `xgboost` (familia `ensemble_boosting`). La SVM suele ser la más lenta: eso cuenta en el criterio de coste.
- **Elegir las dos familias.** Mirad el leaderboard y buscad en las **dos más prometedoras** (por ejemplo, el bosque y *boosting*, como en [`S08_05`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_05_busqueda_hiperparametros.ipynb)). Una persona por búsqueda.
- **Buscar sin hacer trampas.** Usad `GridSearchCV` (prueba todas las combinaciones) o `RandomizedSearchCV` (prueba combinaciones al azar), con `cv=cv`, `scoring="roc_auc"` y `.fit(X_train, y_train)`. **Nunca `X_test`.** Como `hacer_pipe` llama `clf` al paso del modelo, los nombres de la rejilla llevan ese prefijo: `clf__max_depth`, `clf__n_estimators`…
- **Cuidar el tiempo.** Si una búsqueda pasa de 5 minutos, reducid las combinaciones (`n_iter` en la aleatoria, menos valores en la rejilla). Si varias combinaciones quedan casi empatadas, elegid la más sencilla (regla de «1 error estándar» de `S08_05`).
- **Guardar el mejor.** Registrad el modelo con los mejores hiperparámetros con `registrar(evaluar_modelo(...))`. Si usáis el **mismo nombre**, la fila se actualiza; si usáis uno nuevo (`random_forest_ajustado`), se añade (recordad el máximo de 8). Añadid también esos modelos al diccionario `catalogo` (más adelante): lo necesitará el paso 4.

**Qué deberíais ver.** Entre 6 y 8 filas, de al menos 4 familias (`referencia`, `lineal`, `arbol`, `ensemble_bagging`, `ensemble_boosting`, `svm`). El modelo ajustado suele quedar igual o algo mejor que el de partida, pero no siempre; si no mejora, es un resultado válido y se cuenta.

**Hecho cuando:** hay entre 6 y 8 modelos de al menos 4 familias, la búsqueda está hecha en dos familias con validación cruzada sobre train y el `catalogo` incluye los modelos ajustados.

<!--nav-->
---

[← Paso 2](Reto_Sprint_08_paso_2.md) · [Ficha del reto](Reto_Sprint_08.md) · [Paso 4 →](Reto_Sprint_08_paso_4.md)
<!--/nav-->
