# Paso 2 · Probar los modelos clásicos y el neuronal (día 2, 140 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 3 →](Reto_Sprint_15_paso_3.md)
<!--/nav-->

1. Entrenar al menos 3 modelos clásicos con la misma partición y anotar cada prueba.
2. Entrenar al menos un modelo neuronal (o el asistente LLM/RAG en el brief 3).
3. Ajustar 1–2 hiperparámetros clave de cada familia, solo con validación.
4. Comprobar que cada persona ha anotado al menos una fila.

**En sencillo.** Hoy se prueba, se apunta y se compara. Cada persona entrena un modelo o ajusta uno, y **cada prueba se anota nada más terminarla** con la función `experimento` que dejasteis hecha en el paso 1: hace todo el trabajo (entrenar, medir y escribir la fila del registro). Es como una carrera con cronometraje: todos corren en la misma pista (la misma partición) y se apunta cada tiempo, también los malos. No hace falta saber cómo funciona cada modelo por dentro: cambiáis el nombre del modelo, el responsable y, si toca, un ajuste.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Modelo clásico** | Un modelo de aprendizaje automático sin redes neuronales: regresión, bosque aleatorio, *gradient boosting*. |
| **Bosque aleatorio** | Muchos árboles de decisión que votan. Ajuste típico: `max_depth` (profundidad de cada árbol). |
| **Gradient boosting** | Árboles que se entrenan uno tras otro, cada uno corrigiendo los errores del anterior. |
| **Red neuronal** | Un modelo hecho de capas de «neuronas» que aprende combinaciones de las pistas. |
| **Sobreajuste** | Que el modelo se aprenda de memoria el entrenamiento y falle con datos nuevos. |
| **Subconjunto** | Una parte de los datos para que una prueba pesada tarde menos. |

**Cómo se hace**

1. **Repartir (5 minutos).** Un reparto posible si sois 3 o 4:

    | Persona | Qué prueba | Minutos |
    |---|---|---|
    | A | Segundo y tercer modelo clásico (por ejemplo, bosque y boosting) | 50 |
    | B | Modelo neuronal (o RAG/LLM en el brief 3) | 60 |
    | C | Ajuste de 1–2 hiperparámetros de las familias de A (profundidad, número de árboles…) | 40 |
    | D (si hay 4) | Repetir una prueba de otra persona con su código para comprobar que sale igual | 40 |

    Cada persona escribe en **su sección** del cuaderno, con una celda de texto con su nombre como título, y **cambia `responsable="..."` por su nombre** en cada llamada.

2. **Persona A: bosque y boosting.** En una celda nueva:

    ```python
    media, desv = experimento("RandomForest", RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2),
                              {"n_estimators": 200, "min_samples_leaf": 5}, responsable="Luis")
    print(f"Bosque aleatorio: {media:.3f} ± {desv:.3f}")

    media, desv = experimento("HistGradientBoosting", HistGradientBoostingClassifier(random_state=SEMILLA),
                              {"defecto": True}, responsable="Luis")
    print(f"Gradient boosting: {media:.3f} ± {desv:.3f}")
    ```

    - El primer argumento es el **nombre** que verá el registro: el mismo modelo debe llamarse **siempre igual**.
    - El segundo es el modelo con sus ajustes; el tercero, un diccionario `{}` con esos mismos ajustes, para que quede escrito (`{"defecto": True}` significa «sin tocar nada»).
    - Cada llamada entrena 5 veces (validación cruzada), escribe una fila en el registro y devuelve la media y la desviación. Con los datos de práctica salen `Bosque aleatorio: 0.739 ± 0.013` y `Gradient boosting: 0.727 ± 0.011`; el boosting puede tardar de unos segundos a casi medio minuto.

3. **Persona C: ajustar sin trampa.** Probad 2 o 3 valores de un ajuste y **anotad cada valor como una fila**:

    ```python
    for d in (3, 6, 10):
        media, desv = experimento(f"RandomForest_prof{d}",
                                  RandomForestClassifier(n_estimators=200, min_samples_leaf=5, max_depth=d, random_state=SEMILLA, n_jobs=2),
                                  {"n_estimators": 200, "min_samples_leaf": 5, "max_depth": d}, responsable="Marta", notas="ajuste de profundidad")
        print(f"profundidad {d}: {media:.3f} ± {desv:.3f}")
    ```

    `for d in (3, 6, 10)` repite el bloque con `d` igual a 3, luego 6 y luego 10; `f"...{d}"` pone el valor en el nombre. Salen aproximadamente `profundidad 3: 0.742 ± 0.013`, `profundidad 6: 0.745 ± 0.013` y `profundidad 10: 0.742 ± 0.013`: **casi iguales**, y es normal. Anotad también lo que no mejora («empeoró al aumentar la profundidad: sobreajuste»): también es información. **Solo con validación; el test ni se toca.**

4. **Persona B: el modelo neuronal.** La opción más sencilla es la red de scikit-learn, que cabe en la misma función y la misma validación cruzada:

    ```python
    from sklearn.neural_network import MLPClassifier

    media, desv = experimento("RedNeuronal_MLP", MLPClassifier(hidden_layer_sizes=(32, 16), early_stopping=True, max_iter=300, random_state=SEMILLA),
                              {"hidden_layer_sizes": [32, 16], "early_stopping": True, "max_iter": 300}, responsable="Pablo", notas="red neuronal de scikit-learn")
    print(f"Red neuronal: {media:.3f} ± {desv:.3f}")
    ```

    `hidden_layer_sizes=(32, 16)` son dos capas de 32 y 16 neuronas y `early_stopping=True` para de entrenar cuando deja de mejorar. Con los datos de práctica sale aproximadamente `Red neuronal: 0.738 ± 0.019`. Si preferís la red de Keras del sprint 10, copiad `construir_mlp` y el entrenamiento de [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_04_reto_vale_la_pena.ipynb) y anotad la fila a mano con `registrar(...)`, poniendo la métrica de **una sola partición de validación** en `valor_cv`, un `0` en `desv_cv` y en `notas` «una sola partición de validación». En el brief 2 (imágenes) y el brief 3 (asistente), mirad `S11_02` y `S12_06` y anotad también con `registrar`. Si tarda mucho o usa una API de pago, **trabajad con un subconjunto de datos y anotad el coste en `notas`**.

5. **Persona D (si hay cuatro): repetir una prueba.** Copiad en vuestra sección la celda de otra persona (sin cambiar nada salvo `responsable` y `notas="repetición de la prueba de Luis"`) y comprobad que da **las mismas cifras**. Si no, hay azar sin semilla.

6. **Si una prueba la ha generado una IA,** escribidlo en `notas`, por ejemplo `notas="código generado con IA, revisado a mano"`. **Que cada persona toque algo:** si alguien se queda sin fila, que pruebe un ajuste de otra persona y lo anote con su nombre.

7. **Comprobar el registro (10 minutos).** El registro de cada persona vive en su propia sesión de Colab. Para ver todas las filas juntas, la persona con el rol técnico elige *Entorno de ejecución → Reiniciar y ejecutar todo*: se ejecutan todas las secciones, una tras otra, y el registro se rehace completo. Después ejecuta:

    ```python
    registro = pd.read_csv(RUTA_REGISTRO)
    print(len(registro), "filas")
    print(registro["responsable"].value_counts())
    ```

    `value_counts()` cuenta cuántas filas tiene cada nombre. Con las pruebas de ejemplo de arriba (ocho en total) salen `8 filas` y `Marta 3`, `Ana 2`, `Luis 2`, `Pablo 1`. Cada persona del equipo debe aparecer **al menos una vez**.

**Qué deberíais ver.** Un `registro.csv` con unas 8–12 filas de personas distintas, con `valor_cv` y `desv_cv` rellenos. Si dos modelos tienen medias casi iguales y desviaciones parecidas, es normal.

**Hecho cuando:** hay *baseline* y 3 modelos clásicos y 1 neuronal en el registro con la misma partición, y cada persona tiene al menos una fila.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'RandomForestClassifier' is not defined` (o `MLPClassifier`) | Falta importar el modelo, o la celda de importaciones no se ejecutó. | Ejecutad la primera celda del cuaderno; para la red, la línea `from sklearn.neural_network import MLPClassifier` va antes de usarla. |
| `NameError: name 'experimento' is not defined` | Vuestra sesión de Colab no ha ejecutado las celdas comunes. | *Entorno de ejecución → Ejecutar todo* hasta la celda de `experimento` y volved a vuestra sección. |
| Solo veis vuestras filas en el registro | Cada persona tiene su propia sesión de Colab y su propio `registro.csv`. | Que la persona técnica haga *Reiniciar y ejecutar todo* en el cuaderno común y comparta el resultado. |
| Todas las pruebas dan casi lo mismo | Hay poca diferencia real entre los modelos. | Es normal: dejadlo escrito y decidid en el paso 4 por simplicidad y coste. |
| Una celda tarda mucho o Colab se queda sin memoria | El modelo o los datos son pesados. | Probad con un subconjunto (por ejemplo, la mitad de las filas), reducid `n_estimators` y anotad el coste en `notas`. |
| Una persona sin ninguna fila | No ha ejecutado `experimento` con su nombre. | Que pruebe un ajuste distinto de otra persona y lo anote con su `responsable`. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_15_paso_1.md) · [Ficha del reto](Reto_Sprint_15.md) · [Paso 3 →](Reto_Sprint_15_paso_3.md)
<!--/nav-->
