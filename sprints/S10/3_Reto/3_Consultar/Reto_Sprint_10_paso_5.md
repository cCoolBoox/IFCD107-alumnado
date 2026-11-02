# Paso 5 · Comparación justa (día 2, 25 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 5 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 6 →](Reto_Sprint_10_paso_6.md)
<!--/nav-->

1. Repetir el entrenamiento con varias semillas y calcular media ± desviación.
2. Medir el veredicto en la prueba **una sola vez**, con el MLP elegido y con la referencia.
3. Hacer el ejercicio 4 (¿la diferencia es real o es ruido?).
4. Añadir el coste: tiempo, complejidad y explicabilidad.

**En sencillo.** Es el momento del veredicto, el examen final. Se juega **una sola vez**: la prueba lleva guardada desde el paso 1 y, si la mirarais para retocar la red, dejaría de ser un examen justo. Se enfrentan el boosting y el MLP (la media de las tres redes) y se comparan con las mismas notas. Pero un 0,74 frente a un 0,73 puede ser pura suerte, así que el cuaderno hace un truco llamado *bootstrap*: repite 300 veces el examen con reservas sorteadas (con repetición) y mira cuánto baila la diferencia entre los dos modelos. Si el vaivén incluye el cero, **no podéis decir que uno gane**: es un empate, y es una respuesta válida. Por último se pone el precio: cuánto tardan, qué tan complicados son y si se pueden explicar. No hace falta entender cómo se calcula el bootstrap: basta con ejecutarlo y leer el intervalo.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Prueba** (*test*) | El 20 % de las reservas que ningún modelo ha visto ni se ha usado para decidir. Se mira una vez, al final. |
| **Veredicto** | La nota final de cada modelo en la prueba. |
| **Media ± desviación** | La media de varias medidas y, tras el `±`, cuánto se separan de ella. Mide el ruido entre semillas. |
| ***Bootstrap*** | Repetir el cálculo muchas veces con reservas sorteadas con repetición para ver cuánto cambia el resultado por azar. |
| **Intervalo del 95 %** | El tramo de valores `[inf, sup]` en el que cae el 95 % de los resultados del bootstrap. Si incluye el 0, la diferencia no está clara. |
| **Diferencia de AUC** | El AUC del MLP menos el AUC del boosting. Positiva: gana la red; negativa: gana el boosting; cerca de 0: parecidos. |
| **Empate** | Cuando el intervalo incluye el 0: los datos no bastan para decir cuál es mejor. |
| **Booleano** | Un valor que solo puede ser `True` o `False`. |
| **Explicabilidad** | Lo fácil que es contar **por qué** un modelo dice «cancelará» a una reserva concreta. |

**Cómo se hace**

1. **Calcular media ± desviación.** Comprobad primero que el cuaderno usa el MLP elegido en el paso 3 (que se han ejecutado la sección 4 y el ejercicio 2 con él). En una celda nueva:

    ```python
    print(f"AUC de validación del MLP: {np.mean(aucs_mlp_val):.3f} ± {np.std(aucs_mlp_val):.3f}")
    ```

    `np.mean(aucs_mlp_val)` es la media de los tres AUC de validación del ejercicio 2; `np.std(…)` es la desviación (cuánto se separan los tres de esa media) y `:.3f` los deja con tres decimales. El boosting entrena siempre igual (tiene `random_state` fijo), así que no tiene desviación entre semillas: su incertidumbre la da el bootstrap.

2. **El veredicto en la prueba.** Ejecutad la celda «6 · El veredicto en el conjunto de prueba». Ya está escrita y usa la función `evaluar` del ejercicio 1. **Es la única vez que se usa la prueba para decidir: no cambiéis el MLP después de verla.**

    ```python
    prob_mlp_pru = np.mean([m.predict(A_pru, verbose=0).ravel() for m in modelos_mlp], axis=0)
    tabla = pd.DataFrame({"Boosting de árboles": evaluar(y_pru, prob_boost_pru),
                          "MLP (media de 3 semillas)": evaluar(y_pru, prob_mlp_pru)}).T
    tabla["entrenamiento (s)"] = [t_boost, np.mean(tiempos)]
    tabla["parámetros / árboles"] = ["200 iteraciones × árboles de profundidad ≤ 4", f"{modelos_mlp[0].count_params():,} pesos"]
    tabla.round(3)
    ```

    Qué hace cada línea:

    - `prob_mlp_pru = np.mean([… for m in modelos_mlp], axis=0)`: cada una de las tres redes da su probabilidad para cada reserva de **prueba** y se hace la media de las tres: un pequeño «comité».
    - `tabla = pd.DataFrame({…}).T`: monta una tabla con dos columnas, una por modelo, y cada una con las cuatro notas de `evaluar`; `.T` la gira para que cada modelo sea una fila.
    - `tabla["entrenamiento (s)"] = […]`: añade lo que tardó el boosting (`t_boost`) y lo que tardó el MLP de media (`np.mean(tiempos)`).
    - `tabla["parámetros / árboles"] = […]`: añade el tamaño: las iteraciones del boosting y el número de pesos de la red (`count_params()`).
    - `tabla.round(3)`: muestra la tabla con tres decimales.

3. **¿Real o ruido? El bootstrap.** Ejecutad la celda siguiente, también escrita:

    ```python
    rng = np.random.default_rng(SEMILLA)
    difs = []
    for _ in range(300):
        idx = rng.integers(0, len(y_pru), len(y_pru))
        if len(np.unique(y_pru[idx])) < 2:
            continue
        difs.append(roc_auc_score(y_pru[idx], prob_mlp_pru[idx]) - roc_auc_score(y_pru[idx], prob_boost_pru[idx]))
    inf, sup = np.percentile(difs, [2.5, 97.5])
    print(f"Diferencia de AUC (MLP − boosting): {np.mean(difs):+.3f} · intervalo 95 %: [{inf:+.3f}, {sup:+.3f}]")
    plt.hist(difs, bins=25, color="steelblue"); plt.axvline(0, color="red", ls="--", label="sin diferencia")
    ```

    Qué hace cada parte (el final de la celda solo pone títulos a los ejes y muestra el dibujo):

    - `for _ in range(300):`: repite 300 veces lo de debajo.
    - `idx = rng.integers(0, len(y_pru), len(y_pru))`: sortea 1200 posiciones entre las 1200 reservas de prueba, **con repetición**: una prueba «remuestreada».
    - `if len(np.unique(y_pru[idx])) < 2: continue`: si en el sorteo solo hubiera un tipo de reserva no se puede calcular el AUC, y se pasa a la vuelta siguiente.
    - `difs.append(…)`: calcula el AUC del MLP menos el del boosting **en esa prueba sorteada** y lo apunta en `difs`.
    - `inf, sup = np.percentile(difs, [2.5, 97.5])`: se queda con el 95 % central de las 300 diferencias: `inf` es el extremo de abajo y `sup`, el de arriba. Ese es el **intervalo del 95 %**.
    - `print(f"…")`: escribe la diferencia media y el intervalo (`:+.3f` pone el signo).
    - `plt.hist(…)` y `plt.axvline(0, …)`: dibujan el histograma de las 300 diferencias y una línea roja discontinua en el 0.

4. **Ejercicio 4: ¿hay diferencia?** Bajad a «Ejercicio 4», borrad los `...` de su celda y escribid:

    ```python
    hay_diferencia = bool(inf > 0 or sup < 0)
    mejor_modelo = ("MLP" if np.mean(difs) > 0 else "Boosting") if hay_diferencia else "Empate"
    ```

    Qué hace cada línea:

    - `hay_diferencia = bool(inf > 0 or sup < 0)`: el intervalo **no contiene el 0** cuando está entero por encima (`inf > 0`) o entero por debajo (`sup < 0`). `bool(…)` lo convierte en un `True`/`False` de Python: **sin `bool(…)` el `assert` falla**, porque NumPy devuelve su propio tipo de verdadero/falso.
    - `mejor_modelo = (…) if hay_diferencia else "Empate"`: se lee «si hay diferencia, … ; si no, `"Empate"`». Con diferencia, gana `"MLP"` si la diferencia media es positiva y `"Boosting"` si no. Las tres palabras se escriben tal cual, con mayúscula inicial.

    Pulsad ▶: la celda imprime `Veredicto estadístico: …`.

5. **Apuntar el coste.** Con la tabla delante, rellenad una mini tabla para el informe con tres filas: **tiempo** (la columna `entrenamiento (s)`), **complejidad** (árboles o número de pesos) y **explicabilidad**. Para esta última, escribid con vuestras palabras si os parece más fácil o más difícil explicar a un directivo por qué se cancela una reserva con cada modelo (en general, un boosting es más fácil de explicar que una red). Un ejemplo de frase: *«La red tarda [N] veces más y mejora el AUC en [X]; no compensa si el intervalo incluye el 0»*.

**Qué deberíais ver.**
- **Media ± desviación:** una línea como `AUC de validación del MLP: 0.7… ± 0.0…`.
- **La tabla de la sección 6:** dos filas, `Boosting de árboles` y `MLP (media de 3 semillas)`, con las columnas AUC, AP, F1, precisión, entrenamiento (s) y parámetros / árboles. Para el boosting, con esta partición, salen aproximadamente AUC 0.738, AP 0.722, F1 0.639 y precisión 0.672 (un modelo que dijera siempre «no cancela» acertaría un 54 %). El MLP debería quedar muy cerca, con un tiempo de entrenamiento bastante mayor y, con las capas por defecto, `4.417 pesos` (35·64 + 64 + 64·32 + 32 + 32 + 1).
- **El bootstrap:** una línea `Diferencia de AUC (MLP − boosting): +0.0… · intervalo 95 %: [-0.0…, +0.0…]` y un histograma con una línea roja discontinua en el 0.
- **El ejercicio 4:** `Veredicto estadístico: Empate` (o `MLP`, o `Boosting`). Con estos datos lo esperable es que los dos queden muy cerca, y un «Empate» es un resultado perfectamente válido.

**Hecho cuando:** el ejercicio 4 pasa su comprobación, tenéis media ± desviación (o el intervalo) de ambos enfoques y los números del coste apuntados.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `AssertionError: hay_diferencia debe ser True/False` | El valor es de tipo NumPy, no un `True`/`False` de Python. | Envolvedlo: `hay_diferencia = bool(inf > 0 or sup < 0)`. |
| `AssertionError: mejor_modelo debe ser 'MLP', 'Boosting' o 'Empate'` | Hay una errata o una minúscula (`"mlp"`, `"empate"`). | Escribid exactamente `"MLP"`, `"Boosting"` o `"Empate"`. |
| `AssertionError: Si no hay diferencia clara debe ser 'Empate' (y viceversa)` | `mejor_modelo` y `hay_diferencia` no dicen lo mismo. | Con `hay_diferencia` en `False`, `mejor_modelo` ha de ser `"Empate"`; y con `True`, `"MLP"` o `"Boosting"`. |
| `NameError: name 'inf' is not defined` (o `'sup'`, `'difs'`) | No se ejecutó la celda del bootstrap. | Ejecutadla y después repetid el ejercicio 4. |
| `NameError: name 'prob_mlp_pru' is not defined` (o `'prob_boost_pru'`) | No se ejecutó la celda de la tabla (o la del boosting del paso 1). | Ejecutad en orden: boosting, tabla de la sección 6, bootstrap, ejercicio 4. |
| Las cifras cambian un poco al volver a ejecutar todo | El entrenamiento de una red no es idéntico al 100 % entre ejecuciones y ordenadores. | Si la diferencia es pequeña, es normal: usad las cifras de la ejecución final (la de *Reiniciar y ejecutar todo*) en el informe. |
| Queréis cambiar el MLP después de ver la tabla | Eso usaría la prueba para decidir. | No lo hagáis. Anotad lo que salió; lo que probaríais es un «siguiente paso» para el informe. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_10_paso_4.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 6 →](Reto_Sprint_10_paso_6.md)
<!--/nav-->
