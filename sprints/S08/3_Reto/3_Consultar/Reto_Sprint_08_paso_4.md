# Paso 4 · Elegir el campeón (día 2, 45 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 5 →](Reto_Sprint_08_paso_5.md)
<!--/nav-->

1. Calcular la puntuación global de cada modelo con vuestros pesos y ver quién gana.
2. Probar otros pesos (análisis de sensibilidad) y anotar si el campeón cambia.
3. Evaluar al campeón en el test, **una sola vez**, y guardar el resultado.
4. Escribir tres o cuatro líneas: por qué ganó, por qué no ganó otro y qué cambiaría la elección.

**En sencillo.** Es como adjudicar una beca con tres notas que no valen lo mismo. La nota final de cada modelo es la media de sus tres notas (rendimiento, explicabilidad y coste) **ponderada con vuestros pesos**; el primero de la lista es el **campeón**. Si cambiáis los pesos puede ganar otro modelo, y eso también es una respuesta para el cliente: «depende de lo que valoréis». Cuando el campeón está elegido llega el **examen final**: se entrena con todo el entrenamiento y se prueba **una sola vez** con las 1200 reservas que se apartaron. Si probarais varios modelos en ese examen y os quedarais con el mejor, os habríais visto las preguntas y la nota saldría demasiado optimista. En el cuaderno ya está casi todo hecho: vosotros escribís unas pocas líneas (si os perdéis, tenéis cada celda explicada en el [código explicado del cuaderno](../../2_Practica/codigo_explicado/S08_06_leaderboard_plantilla.md)).

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Puntuación global** | La nota final de un modelo, de 0 a 1: la suma de sus tres notas multiplicadas por los pesos. |
| **Campeón** | El modelo con la puntuación global más alta con vuestros pesos. |
| **Análisis de sensibilidad** | Repetir la elección con otros pesos para ver si el campeón cambia. Cada reparto de pesos es un **escenario**. |
| **`iloc[0]`** | «La primera fila» de una tabla. Como la tabla viene ordenada, es la mejor. |
| **`catalogo`** | Un diccionario del cuaderno que sabe **reconstruir** cada modelo por su nombre, para poder entrenarlo de nuevo en el examen final. |
| **`lambda:`** | Una mini-receta sin nombre. `lambda: algo` significa «cuando me pidan, devuelvo `algo`». |
| **`predict_proba`** | Pide al modelo la probabilidad de cada clase. `[:, 1]` se queda con la de «se cancela». |
| **Sobreajuste** | Cuando un modelo se aprende de memoria los datos de entrenamiento y falla con los nuevos. Se nota si el AUC del test es mucho más bajo que el de validación. |

**Cómo se hace**

1. **Mirar el gráfico del apartado «5 · Rendimiento frente a explicabilidad y coste».** Ya está escrito: solo pulsad ▶. Cada punto es un modelo; el tamaño del punto es lo que pesa el modelo y su posición dice cuánto tarda en entrenarse (hacia la derecha, más) y cuánto acierta (hacia arriba, más). Os ayuda a ver los compromisos.
2. **Ejercicio 3: pesos, puntuación y campeón.** En la celda del apartado «6 · Puntuación global con tus pesos», borrad los `...` y escribid (con **vuestros** pesos del paso 1):

    ```python
    pesos = {"rendimiento": 0.5, "explicabilidad": 0.3, "coste": 0.2}
    lb_pond = puntuacion_global(lb, pesos)
    campeon = lb_pond.iloc[0]["modelo"]
    ```

    Qué hace cada línea:

    - `pesos = {…}`: vuestros tres pesos **en decimales** (50 % se escribe `0.5`, con punto) y con las tres claves **exactas**: `"rendimiento"`, `"explicabilidad"` y `"coste"`. Tienen que sumar 1.
    - `lb_pond = puntuacion_global(lb, pesos)`: una función del cuaderno calcula la nota de 0 a 1 de cada modelo en cada criterio y las suma con vuestros pesos. Devuelve la tabla ordenada, del mejor al peor.
    - `campeon = lb_pond.iloc[0]["modelo"]`: coge la primera fila y de ella el nombre del modelo.

    Pulsad ▶. Sale `Campeón con estos pesos: …` y una tabla. Las columnas `punt_rendimiento`, `punt_explicabilidad` y `punt_coste` son las tres notas de 0 a 1, y `puntuacion_global` es la suma ponderada. Con los pesos 0,5 / 0,3 / 0,2, la logística sale así: 0,5 × 1,000 + 0,3 × 0,75 + 0,2 × 0,97 ≈ 0,92.

3. **Leer la tabla con cuidado.** Mirad el AUC **y su desviación**: un 0,81 no es mejor que un 0,80 si las desviaciones son parecidas, porque la diferencia puede ser ruido. Si dos modelos empatan, es un resultado válido: elegid el más simple y explicadlo.
4. **Probar otros pesos (sensibilidad).** Debajo hay una celda ya escrita con tres escenarios (`escenarios`): «solo rendimiento» (0.8 / 0.1 / 0.1), «equilibrado» (0.4 / 0.4 / 0.2) y «explicabilidad primero» (0.2 / 0.6 / 0.2). Pulsad ▶ y apuntad en una celda de texto (botón **+ Texto**) una tabla con el campeón de cada escenario, con este molde:

    ```text
    | Pesos (rendimiento / explicabilidad / coste) | Campeón |
    |---|---|
    | 0.5 / 0.3 / 0.2 (los nuestros) | … |
    | 0.8 / 0.1 / 0.1 (solo rendimiento) | … |
    | 0.4 / 0.4 / 0.2 (equilibrado) | … |
    | 0.2 / 0.6 / 0.2 (explicabilidad primero) | … |
    ```

    Debajo, una frase: ¿cambia el campeón? Si cambia, vuestra recomendación depende de lo que valore el cliente, y así hay que contarlo.

5. **Preparar el catálogo.** Bajad a la celda del apartado «7 · El examen final». Veréis la función `actualizar_test` y el diccionario `catalogo`, que ya trae los modelos de partida. **Justo después de la llave `}` que lo cierra** y antes de la línea `# TODO`, añadid una línea por cada modelo ajustado del paso 3:

    ```python
    catalogo["random_forest_ajustado"] = lambda: busqueda_rf.best_estimator_
    catalogo["lightgbm_ajustado"] = lambda: busqueda_lgb.best_estimator_
    ```

    - `catalogo["lightgbm_ajustado"] = …`: añade una entrada nueva. El nombre entre comillas tiene que ser **exactamente el mismo que en el leaderboard**.
    - `lambda: busqueda_lgb.best_estimator_`: la receta que devuelve el modelo ganador de la búsqueda.
    - Si vuestro campeón es uno de los de partida (`logistica`, `arbol_podado`, `random_forest`, `lightgbm` o `svm_rbf`), ya está en el catálogo, pero añadid las líneas igualmente por si cambiáis de campeón.

6. **El examen final: solo el campeón, una vez.** **Antes de ejecutar, comprobad en equipo que `campeon` es el definitivo**: después de ver el número del test no se cambia. En la misma celda, en el hueco de los `...`, escribid:

    ```python
    final = catalogo[campeon]().fit(X_train, y_train)
    auc_test_campeon = roc_auc_score(y_test, final.predict_proba(X_test)[:, 1])
    lb_final = actualizar_test(campeon, auc_test_campeon)
    ```

    Qué hace cada línea:

    - `catalogo[campeon]()`: busca la receta del campeón por su nombre y la usa para crear el modelo. `.fit(X_train, y_train)` lo entrena con **todo** el entrenamiento.
    - `final.predict_proba(X_test)[:, 1]`: la probabilidad de cancelación que da el modelo para cada una de las 1200 reservas del test, que **nunca había visto**. `roc_auc_score(y_test, …)` la compara con lo que pasó de verdad y da el AUC.
    - `actualizar_test(campeon, auc_test_campeon)`: apunta ese número en la fila del campeón de `leaderboard_S08.csv` (columna `auc_test`) y devuelve la tabla. **No evaluéis ningún otro modelo en el test.**

    Pulsad ▶. Los `assert` de debajo comprueban que el AUC está entre 0,65 y 0,85 y que **solo una fila** tiene `auc_test`.

7. **Escribir las líneas de la decisión.** En una celda de texto, con este molde y **vuestros** números:

    ```text
    Campeón: … (AUC en validación cruzada … ± …; en test …).
    No ganó … porque ….
    Si el cliente valorara solo …, elegiríamos ….
    ```

    Por ejemplo, con los números de esta ejecución (los vuestros serán distintos): *«Campeón: logistica (AUC en validación cruzada 0,755 ± 0,014; en test 0,762). No ganó lightgbm_ajustado porque su AUC (0,747) es prácticamente el mismo, pero se explica peor (2 frente a 4) y el modelo pesa unas 30 veces más (123 KB frente a 4 KB). Si el cliente valorara la explicabilidad por encima del rendimiento (pesos 0,2 / 0,6 / 0,2), elegiríamos el árbol podado.»* Esas líneas van a la *model card* (apartado 3) en el paso 5.

**Qué deberíais ver.**
- **Ejercicio 3** (pesos 0,5 / 0,3 / 0,2): `Campeón con estos pesos: logistica`, con `logistica` en cabeza (≈ 0,92) y `arbol_podado` muy cerca (≈ 0,91). Detrás, a mucha distancia (≈ 0,69 y menos), los demás; la SVM, con la puntuación más baja por ser caja negra, lenta y pesada.
- **Sensibilidad:** una tabla con `logistica` para «solo rendimiento» y `arbol_podado` para «equilibrado» y «explicabilidad primero»: **el campeón cambia con los pesos**. En «equilibrado» la ventaja del árbol es corta (≈ 0,93 frente a ≈ 0,90 de la logística): con los tiempos de vuestro ordenador puede ganar cualquiera.
- **Examen final:** `Campeón: logistica · AUC en validación cruzada 0.755 · AUC en test 0.762` y una tabla `lb_final` donde `auc_test` solo tiene valor en la fila del campeón (≈ 0,7623); en el resto, `NaN`.
- El AUC de test se parece al de validación (aquí sale unas 0,007 más alto, dentro de la desviación; en otro reparto podría salir algo más bajo) y está entre 0,65 y 0,85. Si fuera **mucho** más bajo, sería sobreajuste. En `leaderboard_S08.csv`, `auc_test` tiene valor en **una sola fila**.
- Con otros pesos o con otros modelos ajustados, vuestro campeón puede ser otro. Los tiempos cambian de un ordenador a otro y de una ejecución a otra, así que la nota de coste y la puntuación global pueden variar unas centésimas.

**Hecho cuando:** hay un campeón elegido con vuestros pesos, la sensibilidad está probada y apuntada, y `auc_test` aparece en una única fila.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `AssertionError: Los pesos deben sumar 1` | Los pesos no suman 1 (por ejemplo, habéis escrito `50` en vez de `0.5`). | Escribid decimales con punto y comprobad: `0.5 + 0.3 + 0.2 = 1`. |
| `KeyError: 'coste'` (o `'rendimiento'`, `'explicabilidad'`), o `AssertionError: Claves: rendimiento, explicabilidad y coste` | Las claves de `pesos` no son exactamente esas tres. | Copiadlas tal cual, en minúsculas y sin tildes en `coste` ni `rendimiento`. |
| `AssertionError: El campeón debe ser uno de los modelos y no el baseline` | Con vuestros pesos gana el modelo de referencia: casi no pesa el rendimiento. | Subid el peso del rendimiento (con 0,2 o más ya no pasa) y volved a justificarlo. |
| `NameError: name 'lb' is not defined` (o `'busqueda_rf'`, `'campeon'`) | No se ejecutó una celda anterior, o Colab se reinició. | Ejecutad desde arriba, por orden, y no os saltéis las celdas de las búsquedas. |
| `KeyError: 'lightgbm_ajustado'` (u otro nombre) | El campeón no está en `catalogo`: falta la línea del paso 5 o el nombre no coincide con el del leaderboard. | Añadid la línea con **el mismo nombre** y volved a ejecutar la celda. |
| `ValueError: y should be a 1d array, got an array of shape (1200, 2) instead.` | Falta `[:, 1]` detrás de `predict_proba(X_test)`. | Escribid `final.predict_proba(X_test)[:, 1]`. |
| `AssertionError: El AUC de test del campeón debería estar entre 0,65 y 0,85` | Un AUC cercano a 1 suele ser que habéis medido con `X_train`, que el modelo ya vio. | Usad `X_test` y `y_test` en `roc_auc_score` y entrenad solo con `X_train`, `y_train`. |
| `AssertionError: Solo el campeón debe tener AUC de test` | Se calculó el test para más de un modelo (por ejemplo, tras cambiar de campeón). | Ejecutad de nuevo desde la celda de herramientas, que borra el CSV, y repetid el paso. No cambiéis de campeón por haber visto ese número: es la regla de oro. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_08_paso_3.md) · [Ficha del reto](Reto_Sprint_08.md) · [Paso 5 →](Reto_Sprint_08_paso_5.md)
<!--/nav-->
