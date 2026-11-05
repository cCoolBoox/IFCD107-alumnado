# Paso 2 · Primeros modelos en el leaderboard (día 2, 30 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 3 →](Reto_Sprint_08_paso_3.md)
<!--/nav-->

1. Abrir `S08_06_leaderboard_plantilla` en Colab, guardar una copia y llamarla `reto_S08.ipynb`.
2. Ejecutar las celdas de preparación y de herramientas **sin cambiarlas**.
3. Registrar el modelo de referencia (*baseline*), la regresión logística, un árbol podado y un bosque.
4. Comprobar que la tabla tiene una fila por modelo.

**En sencillo.** Un *leaderboard* es como la clasificación de una liga: todos juegan con las mismas reglas y los resultados se apuntan en una tabla. Aquí los jugadores son **modelos** y las reglas (los mismos datos, las mismas particiones de validación cruzada y la misma nota, el AUC) vienen ya hechas en una celda que **no se toca**. Vosotros metéis a los cuatro primeros: un modelo que no sabe nada (la referencia o *baseline*, para saber si los demás merecen la pena), una regresión logística, un árbol y un bosque. Cada uno se apunta con una sola orden, `registrar(evaluar_modelo(...))`: solo escribís cuál es, cómo se llama y qué nota de explicabilidad le dais. No hace falta saber cómo funciona cada modelo por dentro: los ajustes vienen dados.

**Qué puede pasar.** Este paso se hace dentro de la práctica `S08_02` (30 minutos), que ya trae sus propios ejercicios, así que es probable que no os dé tiempo a todo. Registrad primero los cuatro modelos en `S08_06` y dejad para casa los ejercicios de `S08_02` que os falten. Si al empezar el paso 4 aún falta algo de esta tabla, completadlo antes de seguir (pedid ayuda al docente): sin la tabla no se pueden calcular las puntuaciones.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Celda** | Cada caja del cuaderno. Las de código se ejecutan con el botón ▶ (o con `Mayús + Intro`). |
| **Función** | Una receta con nombre que se usa con paréntesis, como `evaluar_modelo(...)`. Lo de dentro de los paréntesis son los «ingredientes» que le pasáis. |
| **Modelo de referencia** (*baseline*) | Un modelo tonto, `DummyClassifier`, que siempre predice lo más habitual sin mirar ninguna columna. Su AUC es 0,5: es el suelo que hay que superar. |
| **Regresión logística** | Un modelo sencillo que da un peso a cada variable y los suma para calcular la probabilidad de cancelar. |
| **Árbol podado** | Una cadena de preguntas de sí o no sobre la reserva a la que se limita el tamaño (`min_samples_leaf=80`: cada hoja final reúne al menos 80 reservas) para que no memorice. |
| **Bosque aleatorio** | Muchos árboles (aquí 200) que votan. Suele acertar más, pero cuesta más explicarlo. |
| **Familia** | El tipo de modelo: `referencia`, `lineal`, `arbol`, `ensemble_bagging`… Es una etiqueta que escribís al registrar. |
| **Semilla** (`SEMILLA`) | Un número (42) que fija el azar: así todos los equipos obtienen lo mismo. |
| **`assert`** | Una línea de comprobación del cuaderno: si algo no cuadra, se para y escribe un mensaje. |

**Cómo se hace**

1. **Abrir vuestra copia del cuaderno.** Entrad en el [cuaderno `S08_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_06_leaderboard_plantilla.ipynb) (se abre en Colab). Arriba, *Archivo → Guardar una copia en Drive* y después *Archivo → Cambiar nombre*: llamadla `reto_S08.ipynb`. Trabajad siempre en **vuestra copia**. Pulsad *Compartir* y añadid al equipo con permiso de **Editor**. Una persona escribe y las demás miran y opinan.
2. **Ejecutar las celdas de preparación y de herramientas, por orden y sin cambiarlas.** Son cuatro, de arriba abajo: «Preparación» (la primera), la de las importaciones (`import os`, `import pickle`…), la del apartado «1 · Datos y partición» y la del apartado «2 · Herramientas del leaderboard (no modificar)». Pulsad ▶ en cada una. Las dos últimas escriben un mensaje:

    ```text
    Train: 4800 · Test (intacto hasta el final): 1200
    Herramientas listas. Leaderboard en: leaderboard_S08.csv
    ```

    Quiere decir que 4800 reservas se usan para entrenar y comparar, y 1200 quedan **apartadas** para el examen final del paso 4. Es un test **nuevo**: no es el de las prácticas `S08_01` a `S08_05` (otra partición), así que nadie lo ha visto. Ojo: la celda de herramientas **borra `leaderboard_S08.csv` cada vez que se ejecuta** (por `REINICIAR = True`), así que la tabla empieza de cero.

3. **Ejercicio 1: el modelo de referencia y la logística.** Buscad la celda del apartado «3 · Registrar el baseline y el modelo lineal». Veréis una línea `# TODO`, tres puntos `...` y varias líneas con `assert`. **Borrad solo los tres puntos** y escribid ahí:

    ```python
    lb = registrar(evaluar_modelo("baseline", "referencia",
                                  hacer_pipe(DummyClassifier(strategy="prior")), 5, "Siempre predice lo más habitual"))
    lb = registrar(evaluar_modelo("logistica", "lineal",
                                  hacer_pipe(LogisticRegression(max_iter=1000), escalar=True), 4, "La más sencilla de explicar"))
    ```

    Qué hace cada línea:

    - `lb = registrar(evaluar_modelo(...))`: `evaluar_modelo` mide el modelo y devuelve una fila de resultados; `registrar` la apunta en `leaderboard_S08.csv` y devuelve **la tabla entera**, que se guarda en `lb`. Todas las líneas de este paso empiezan por `lb = `: así `lb` siempre tiene la tabla más reciente, y el `assert` de debajo la usa.
    - Los cinco datos que lleva `evaluar_modelo`, **en este orden**: el nombre (`"baseline"`), la familia (`"referencia"`), el modelo, la nota de explicabilidad (`5`) y unas notas en texto libre.
    - `hacer_pipe(...)`: prepara los datos (rellena huecos y convierte los textos en 0 y 1) y se los pasa al modelo. **El modelo nunca va suelto**: siempre dentro de `hacer_pipe(...)`.
    - `DummyClassifier(strategy="prior")`: el modelo que siempre predice lo más habitual.
    - `LogisticRegression(max_iter=1000)`: la logística; `max_iter=1000` le deja hasta 1000 intentos para ajustarse. `escalar=True` pone las variables en la misma escala antes de usarla: la logística y la SVM lo necesitan.
    - Los nombres entre comillas (`"baseline"`, `"logistica"`) tienen que ser **exactamente esos**: el `assert` los comprueba.

    Pulsad ▶. Si todo va bien, no aparece ningún mensaje de error y debajo sale la tabla `lb` con dos filas.

4. **Ejercicio 2, primera mitad: el árbol y el bosque.** Buscad la celda del apartado «4 · Registrar los contendientes del duelo». Borrad los `...` y escribid:

    ```python
    lb = registrar(evaluar_modelo("arbol_podado", "arbol",
                                  hacer_pipe(DecisionTreeClassifier(min_samples_leaf=80, random_state=SEMILLA)),
                                  5, "Reglas fáciles de leer"))
    lb = registrar(evaluar_modelo("random_forest", "ensemble_bagging",
                                  hacer_pipe(RandomForestClassifier(n_estimators=200, min_samples_leaf=5,
                                                                    random_state=SEMILLA, n_jobs=2)),
                                  2, "200 árboles que votan"))
    ```

    Qué hace cada línea:

    - Es el mismo patrón que antes. Cambian el nombre, la familia, el modelo y la explicabilidad: **5** para el árbol (se lee como una lista de reglas) y **2** para el bosque (200 árboles: no se puede leer).
    - `DecisionTreeClassifier(min_samples_leaf=80, random_state=SEMILLA)`: el árbol; `min_samples_leaf=80` es la poda y `random_state=SEMILLA` fija el azar.
    - `RandomForestClassifier(n_estimators=200, …)`: el bosque; `n_estimators=200` son los 200 árboles y `n_jobs=2` usa dos procesadores a la vez.
    - Los nombres `"arbol_podado"` y `"random_forest"` van tal cual, y `SEMILLA` se escribe en mayúsculas: es el nombre de la variable que creó la celda de importaciones.

    Pulsad ▶. Esta celda **acabará con un error rojo, y es normal**: el `assert` pide 6 modelos y todavía hay 4 (faltan *boosting* y SVM, que son el paso 3). Los cuatro modelos **sí se han apuntado** igualmente. Para verlos, abrid una celda nueva (botón **+ Código**), escribid `lb` y pulsad ▶.

5. **Leer la tabla.** Cada fila es un modelo y cada columna, una nota. Que cada persona del equipo sepa explicar qué mide cada una:

    | Columna | Qué mide |
    |---|---|
    | `auc_cv_media` y `auc_cv_desv` | El AUC medio de las 5 pruebas de la validación cruzada y cuánto varía de una a otra (la «±»). |
    | `ap_cv_media` | Otra nota de acierto, parecida al AUC. La tabla la guarda; no se usa para decidir. |
    | `seg_ajuste` | Segundos que tarda en entrenarse, por prueba. |
    | `ms_pred_1000` | Milisegundos que tarda en predecir 1000 reservas. |
    | `tamano_kb` | Lo que ocupa el modelo guardado, en kilobytes. |
    | `explicabilidad_1a5` | La nota que habéis puesto vosotros. |
    | `auc_test` | Vacía hasta el paso 4: el test se estrena una sola vez. |

    Si queréis entender mejor un modelo, el cuaderno de [`S08_01` (árboles)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/para_casa/S08_01_arboles_decision.ipynb) y el de [`S08_02` (bosques)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/para_casa/S08_02_random_forest.ipynb) lo explican, pero no hace falta para este paso.

**Qué deberíais ver.**
- **Tras las celdas de preparación:** `Train: 4800 · Test (intacto hasta el final): 1200` y `Herramientas listas. Leaderboard en: leaderboard_S08.csv`.
- **Tras el ejercicio 1:** una tabla de dos filas. `logistica` con AUC ≈ 0,755 (± 0,014) y `baseline` con AUC 0,5 y desviación 0.
- **Tras el ejercicio 2:** el error `AssertionError: Deben estar el baseline, la logística y al menos cuatro modelos más`, y al escribir `lb`, una tabla ordenada por `auc_cv_media` con cuatro filas: `logistica` (≈ 0,755), `random_forest` (≈ 0,737), `arbol_podado` (≈ 0,719) y `baseline` (0,500). El bosque es el que más pesa: `tamano_kb` de unos 11 800 KB, frente a menos de 11 KB en los demás.
- **En el panel de archivos de Colab** (el icono de la carpeta 📁 de la izquierda; si no aparece, pulsad el icono de refrescar), el fichero `leaderboard_S08.csv`.

Los AUC son los mismos en cada ejecución (con `SEMILLA = 42`) y los tiempos y tamaños pueden variar un poco de un ordenador a otro.

**Hecho cuando:** el leaderboard tiene `baseline`, `logistica`, `arbol_podado` y `random_forest`, y cada persona sabe explicar qué mide cada columna.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'dato' is not defined` (o `'pd'`, `'SEMILLA'`, `'hacer_pipe'`, `'DummyClassifier'`) | No se ha ejecutado una de las celdas de preparación, o Colab se reinició y olvidó todo. | Ejecutad por orden las cuatro celdas de preparación y herramientas y después la vuestra. |
| `AssertionError: Deben estar el baseline, la logística y al menos cuatro modelos más` | En este paso es normal: pide 6 modelos y aún hay 4. | Seguid al paso 3 sin tocar el `assert`. Los cuatro modelos están apuntados. |
| `AssertionError: El leaderboard debe tener baseline y logistica` | Habéis vuelto a ejecutar la celda del ejercicio 1 cuando la tabla ya tenía más modelos. | La tabla no se ha estropeado. No repitáis esa celda; para empezar de cero, ejecutad otra vez la celda de herramientas y después el ejercicio 1. |
| `AssertionError: El baseline debe dar AUC ≈ 0,5` | El modelo `baseline` no es el modelo de referencia. | Comprobad que es `DummyClassifier(strategy="prior")` y que va dentro de `hacer_pipe(...)`. |
| `ValueError: All the 5 fits failed.` y, al final del mensaje, `could not convert string to float: 'estandar'` | Habéis pasado el modelo suelto, sin `hacer_pipe(...)`: el modelo no sabe leer los textos de las columnas. | Envolved el modelo: `hacer_pipe(DecisionTreeClassifier(...))`. |
| `SyntaxError: '(' was never closed` | Falta algún paréntesis de cierre (o sobra uno). | Contad: cada `(` necesita su `)`. Al final de cada orden se cierran dos seguidos (`))`): el de `evaluar_modelo` y el de `registrar`. |
| La tabla sale vacía o con menos filas de las que esperáis | Se ejecutó otra vez la celda de herramientas, que borra el CSV y empieza de cero. | Volved a ejecutar los ejercicios 1 y 2 en orden. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_08_paso_1.md) · [Ficha del reto](Reto_Sprint_08.md) · [Paso 3 →](Reto_Sprint_08_paso_3.md)
<!--/nav-->
