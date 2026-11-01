# Paso 3 · *Boosting*, SVM y búsqueda de hiperparámetros (día 2, 25 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 4 →](Reto_Sprint_08_paso_4.md)
<!--/nav-->

1. Registrar un modelo de *boosting* y una SVM.
2. Buscar hiperparámetros en **dos familias** (rejilla o aleatoria), solo con train y validación cruzada, sin pasar de 5 minutos cada búsqueda.
3. Registrar en el leaderboard los mejores modelos de cada búsqueda.
4. Comprobar que hay entre 6 y 8 modelos, de al menos 4 familias.

**En sencillo.** Cada modelo tiene «botones de ajuste», como la temperatura y el tiempo de un horno. Girarlos a mano es lento y, sin querer, se hace trampa. Un **buscador** prueba combinaciones de botones y se queda con la mejor, pero **examinándose siempre con trozos del entrenamiento**: usar el test para elegir sería ver el examen antes de hacerlo. La **rejilla** prueba todas las combinaciones; la **aleatoria** prueba solo unas cuantas elegidas al azar. Antes, completáis la tabla con los dos modelos que faltan, *boosting* y SVM. No hace falta entender qué hace cada botón: los valores que se prueban vienen escritos más abajo (y explicados en el cuaderno [`S08_05`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_05_busqueda_hiperparametros.ipynb), que es la guía de este paso).

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Hiperparámetro** | Un botón de ajuste que fijáis **antes** de entrenar (cuántos árboles, qué profundidad…). El modelo no lo aprende solo. |
| ***Boosting*** | Muchos árboles pequeños puestos en fila: cada uno corrige los errores del anterior. LightGBM y XGBoost son dos versiones. |
| **SVM** | Un modelo que busca la «frontera» que mejor separa las reservas que se cancelan de las que no. Es una caja negra y la más lenta de la tabla. |
| **Rejilla** (`GridSearchCV`) | Búsqueda que prueba **todas** las combinaciones de una lista de valores. |
| **Búsqueda aleatoria** (`RandomizedSearchCV`) | Búsqueda que prueba solo `n_iter` combinaciones al azar, tomadas de rangos. Explora más valores con el mismo tiempo. |
| **Diccionario** | Una lista de parejas `nombre: valor` entre llaves, como `{"clf__max_depth": [4, 8]}`. Aquí, cada ajuste con los valores que se van a probar. |
| **`clf__`** | El prefijo que llevan los nombres de los ajustes: `hacer_pipe` llama `clf` a la parte del modelo, y se pegan con **dos** guiones bajos. |
| **`best_params_`, `best_score_`, `best_estimator_`** | Lo que guarda la búsqueda al acabar: los ajustes ganadores, su AUC y el modelo ya reentrenado con ellos. |

**Cómo se hace**

1. **Terminar el ejercicio 2: *boosting* y SVM.** Volved a la celda del apartado «4 · Registrar los contendientes del duelo». Debajo de las dos líneas del paso 2 (**no las borréis**) añadid las dos siguientes (si queréis saber más, los cuadernos [`S08_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_03_boosting_xgboost_lightgbm.ipynb) y [`S08_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_04_svm.ipynb) explican el *boosting* y la SVM):

    ```python
    lb = registrar(evaluar_modelo("lightgbm", "ensemble_boosting",
                                  hacer_pipe(lgb.LGBMClassifier(n_estimators=100, learning_rate=0.05, num_leaves=8,
                                                                random_state=SEMILLA, n_jobs=2, verbose=-1)),
                                  2, "Árboles pequeños en cadena"))
    lb = registrar(evaluar_modelo("svm_rbf", "svm",
                                  hacer_pipe(SVC(kernel="rbf", C=1, probability=True, random_state=SEMILLA), escalar=True),
                                  1, "Caja negra, la más lenta"))
    ```

    Qué hace cada línea:

    - Mismo patrón que en el paso 2. Cambian el modelo y su explicabilidad: **2** para *boosting* (muchos árboles) y **1** para la SVM (caja negra).
    - `lgb.LGBMClassifier(n_estimators=100, learning_rate=0.05, num_leaves=8, …)`: el modelo LightGBM. Los números son los ajustes de partida que da el cuaderno; `verbose=-1` le dice que no escriba mensajes.
    - `SVC(kernel="rbf", C=1, probability=True, …)`: la SVM. `probability=True` hace que pueda dar probabilidades, y por eso es más lenta. **Lleva `escalar=True`**, como la logística.
    - La familia del *boosting* tiene que ser `"ensemble_boosting"`: el `assert` busca la palabra *boosting*.

    Pulsad ▶. Ahora el `assert` pasa y debajo sale la tabla con **seis modelos**. La SVM tarda unos segundos más que los demás: es normal.

2. **Preparar las búsquedas.** Debajo de la celda del ejercicio 2 y **antes** del apartado «5», pulsad **+ Código** para crear una celda nueva por búsqueda (así podéis repartirlas). Los ejemplos de abajo buscan en el bosque (familia `ensemble_bagging`) y en LightGBM (`ensemble_boosting`), igual que en `S08_05`. Si preferís otras dos familias, el patrón es el mismo, pero los nombres de los ajustes cambian: preguntad antes al docente.
3. **Búsqueda 1: el bosque, con rejilla.** En una celda nueva:

    ```python
    from scipy.stats import randint, loguniform, uniform
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

    pipe_rf = hacer_pipe(RandomForestClassifier(random_state=SEMILLA, n_jobs=2))
    rejilla_rf = {"clf__n_estimators": [100, 200],
                  "clf__max_depth": [4, 8],
                  "clf__min_samples_leaf": [10, 40]}
    busqueda_rf = GridSearchCV(pipe_rf, rejilla_rf, cv=cv, scoring="roc_auc").fit(X_train, y_train)
    print("Bosque · mejor AUC:", round(busqueda_rf.best_score_, 4))
    print(pd.Series(busqueda_rf.best_params_))
    ```

    Qué hace cada línea:

    - Las dos líneas `from … import …` traen las herramientas de búsqueda (`GridSearchCV`, `RandomizedSearchCV`) y los tres «generadores de números» que se usan en la búsqueda 2. Hay que ejecutarlas una vez; se quedan en la memoria del cuaderno.
    - `pipe_rf = hacer_pipe(RandomForestClassifier(…))`: el bosque envuelto en `hacer_pipe`, **sin** los ajustes que vamos a buscar.
    - `rejilla_rf = {…}`: lo que se prueba: 2 valores de `n_estimators` (cuántos árboles), 2 de `max_depth` (cuántas preguntas seguidas, como máximo) y 2 de `min_samples_leaf` (reservas mínimas por hoja). 2 × 2 × 2 = **8 combinaciones**. Fijaos en el prefijo `clf__` de cada nombre.
    - `GridSearchCV(pipe_rf, rejilla_rf, cv=cv, scoring="roc_auc")`: prepara la búsqueda con la **misma validación cruzada** del cuaderno (`cv=cv`) y puntuando con el AUC.
    - `.fit(X_train, y_train)`: la lanza. `X_train` e `y_train` son las 4800 reservas de entrenamiento y su columna `cancelada`. **Nunca `X_test`**: sería mirar el examen.
    - `busqueda_rf.best_score_` y `.best_params_`: el mejor AUC y los ajustes que lo consiguieron; `pd.Series(…)` los pone en una lista legible.

4. **Búsqueda 2: LightGBM, aleatoria.** En otra celda nueva:

    ```python
    pipe_lgb = hacer_pipe(lgb.LGBMClassifier(n_estimators=200, subsample_freq=1,
                                             random_state=SEMILLA, n_jobs=2, verbose=-1))
    distr_lgb = {"clf__learning_rate": loguniform(0.01, 0.3),
                 "clf__num_leaves": randint(3, 40),
                 "clf__min_child_samples": randint(10, 200),
                 "clf__subsample": uniform(0.6, 0.4)}
    busqueda_lgb = RandomizedSearchCV(pipe_lgb, distr_lgb, n_iter=20, cv=cv, scoring="roc_auc",
                                      random_state=SEMILLA).fit(X_train, y_train)
    print("LightGBM · mejor AUC:", round(busqueda_lgb.best_score_, 4))
    print(pd.Series(busqueda_lgb.best_params_).round(3))
    ```

    Qué hace cada línea:

    - `distr_lgb = {…}`: aquí no hay listas sino **rangos**. `randint(3, 40)` da números enteros al azar entre 3 y 39; `loguniform(0.01, 0.3)` da decimales entre 0,01 y 0,3; `uniform(0.6, 0.4)` da decimales entre 0,6 y 1,0.
    - Los cuatro ajustes: `learning_rate` (cuánto corrige cada árbol al anterior), `num_leaves` (tamaño de cada árbol), `min_child_samples` (reservas mínimas por hoja) y `subsample` (qué fracción de reservas ve cada árbol).
    - `subsample_freq=1` en el modelo es necesario para que `subsample` tenga efecto.
    - `n_iter=20`: se prueban 20 combinaciones al azar. `random_state=SEMILLA` hace que sean **las mismas 20** en cada ejecución.
    - El resto es igual que en la búsqueda 1: `cv=cv`, `scoring="roc_auc"` y `.fit(X_train, y_train)`.

5. **Guardar los mejores modelos en el leaderboard.** En otra celda nueva:

    ```python
    lb = registrar(evaluar_modelo("random_forest_ajustado", "ensemble_bagging", busqueda_rf.best_estimator_,
                                  2, "Rejilla de 8 combinaciones"))
    lb = registrar(evaluar_modelo("lightgbm_ajustado", "ensemble_boosting", busqueda_lgb.best_estimator_,
                                  2, "Búsqueda aleatoria de 20 combinaciones"))
    print(len(lb), "modelos de", lb["familia"].nunique(), "familias")
    lb
    ```

    - `busqueda_rf.best_estimator_` es el bosque ya preparado con los mejores ajustes: se pasa **tal cual**, sin `hacer_pipe`, porque ya lo lleva dentro.
    - Los nombres nuevos (`..._ajustado`) **añaden** filas. Si usarais un nombre que ya existe (`"random_forest"`), la fila se **sustituiría**. Con nombres nuevos tenéis 8 modelos, que es el máximo: **no añadáis `xgboost`**.
    - `len(lb)` cuenta las filas y `lb["familia"].nunique()` cuenta las familias distintas.

6. **Leer el resultado con honestidad.** Comparad cada modelo ajustado con el de partida y mirad la desviación (la «±»): una mejora de milésimas, menor que la desviación, es **ruido**, no una mejora. Si no mejora, es un resultado válido y se cuenta en la *model card*. Si varias combinaciones quedan casi empatadas, elegid la más sencilla (la regla del «error estándar» del apartado 4 de `S08_05`). En el paso 4 añadiréis estos dos modelos al `catalogo`.

**Qué deberíais ver.**
- **Tras terminar el ejercicio 2:** seis filas, ordenadas por AUC: `logistica` (≈ 0,758), `lightgbm` (≈ 0,750), `random_forest` (≈ 0,741), `svm_rbf` (≈ 0,740), `arbol_podado` (≈ 0,716) y `baseline` (0,500). La SVM es la que más tarda por prueba (segundos; las demás, menos de uno).
- **Búsqueda 1:** `Bosque · mejor AUC: 0.7456` y, debajo, los ajustes ganadores: `clf__max_depth` 8, `clf__min_samples_leaf` 10 y `clf__n_estimators` 200. Las 8 combinaciones quedan entre 0,744 y 0,746: casi empatadas.
- **Búsqueda 2:** `LightGBM · mejor AUC: 0.7526` y cuatro ajustes con decimales (aproximadamente `learning_rate` 0,092, `min_child_samples` 62, `num_leaves` 4 y `subsample` 0,889). Como son sorteos, pueden salir valores algo distintos si la versión de las librerías no es la misma.
- **Al registrar los dos modelos ajustados:** `8 modelos de 6 familias` y una tabla de 8 filas, con `lightgbm_ajustado` (≈ 0,753) justo por encima de `lightgbm` (≈ 0,750) y `random_forest_ajustado` (≈ 0,746) sobre `random_forest` (≈ 0,741). Mejoras de milésimas: ruido, porque la desviación es de ± 0,013. Cada búsqueda tardó entre 15 y 40 segundos en un ordenador de prueba; en Colab puede tardar más.

**Hecho cuando:** hay entre 6 y 8 modelos de al menos 4 familias, y la búsqueda está hecha en dos familias con validación cruzada sobre train.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'GridSearchCV' is not defined` (o `'randint'`, `'loguniform'`, `'uniform'`) | Falta ejecutar las dos líneas `from … import …` del principio de la búsqueda 1. | Ejecutad esa celda (o añadidlas al principio de la que falla) y volved a probar. |
| `ValueError: Invalid parameter 'max_depth' for estimator Pipeline(…)` | A un nombre de la rejilla le falta el prefijo `clf__`. | Escribidlo como `"clf__max_depth"`, con dos guiones bajos. |
| `ValueError: Invalid parameter 'rf' for estimator Pipeline(…)` (o `'lgb'`) | Habéis copiado el prefijo de `S08_05`: allí el paso se llama `rf` o `lgb`; aquí se llama `clf`. | Cambiad el prefijo por `clf__`. |
| `AssertionError: Falta un modelo de boosting` | La familia del modelo no contiene la palabra *boosting*. | Usad `"ensemble_boosting"`. |
| `AssertionError: Faltan modelos de las familias árbol, bosque o SVM` | Falta alguno de `arbol_podado`, `random_forest` o `svm_rbf`, o tienen otro nombre. | Revisad los nombres, que van tal cual, y que ejecutasteis la celda entera. |
| La búsqueda pasa de 5 minutos | Hay demasiadas combinaciones para el ordenador de Colab. | Parad la celda (el botón de parar, junto a la celda) y reducid: menos valores en la rejilla, o `n_iter=10` en la aleatoria. |
| La tabla tiene 9 filas o más | Hay más de 8 modelos (por ejemplo, `xgboost` más los dos ajustados). | Ejecutad de nuevo la celda de herramientas (empieza de cero) y registrad otra vez los modelos sin `xgboost`. |
| El modelo ajustado sale igual o peor que el de partida | La búsqueda solo elige lo mejor **de lo que probó**, y las diferencias son de milésimas. | Es un resultado válido. Contadlo así en la *model card*. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_08_paso_2.md) · [Ficha del reto](Reto_Sprint_08.md) · [Paso 4 →](Reto_Sprint_08_paso_4.md)
<!--/nav-->
