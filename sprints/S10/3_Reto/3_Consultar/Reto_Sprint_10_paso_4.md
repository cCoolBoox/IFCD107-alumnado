# Paso 4 · Diagnosticar el sobreajuste (día 2, 20 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 4 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 5 →](Reto_Sprint_10_paso_5.md)
<!--/nav-->

1. Mirar las curvas de vuestra mejor red.
2. Hacer el ejercicio 3 (`diagnostico`).
3. Escribir una frase de diagnóstico.

**En sencillo.** Un alumno que memoriza las respuestas del libro de ejercicios saca un 10 en el libro y un 5 en el examen: se ha aprendido el libro, no la materia. Una red hace lo mismo cuando **memoriza** las reservas de entrenamiento y falla con las nuevas: se llama **sobreajuste**. Las curvas de aprendizaje son esas dos notas, la del libro (entrenamiento) y la del examen de prueba (validación), época a época, y dejan ver si la red memoriza, si no ha aprendido lo bastante o si va bien. En este paso aprendéis a leer esas curvas, escribís una pequeña función que lo decide y contáis el resultado con una frase. **No hace falta** saber matemáticas: solo comparar dos líneas.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Sobreajuste** | La red memoriza el entrenamiento y falla con datos nuevos: la pérdida de entrenamiento baja, pero la de validación se estanca o sube. |
| **Subajuste** | La red es demasiado simple (o ha entrenado poco) y falla en todo: las dos pérdidas se quedan altas. |
| **Buen ajuste** | Las dos pérdidas bajan y se estabilizan juntas, una cerca de la otra. |
| **Historial** (`History`) | El objeto que devuelve `fit`. `h.history` es un diccionario con las pérdidas de cada época: la clave `"loss"` es la de entrenamiento y `"val_loss"` la de validación. |
| **Brecha** | La distancia entre la pérdida de validación y la de entrenamiento. Una brecha grande avisa de memorización. |
| **Margen** | Cuánto se tolera que la validación final se pase de su mejor valor antes de llamarlo sobreajuste (aquí 0,03). |
| **Condición** (`if`) | Una línea que ejecuta lo que tiene debajo **solo si** se cumple lo que dice. `or` significa «o»: basta con que se cumpla una de las dos cosas. |
| **`[-1]`** | El último elemento de una lista. `pv[-1]` es la pérdida de la última época. |

**Cómo se hace**

1. **Mirar las curvas.** Si no las tenéis a la vista, ejecutad otra vez la celda de la sección 5 (con la red elegida en el paso 3). Hay una gráfica por semilla, con la pérdida de entrenamiento y la de validación. Cuidado: el eje horizontal empieza en 0, así que la primera época es el 0 del dibujo. Buscad cuál de estas tres formas se parece más:

    - **El entrenamiento baja y la validación sube** (o se aleja hacia arriba): la red memoriza (sobreajuste). Se arregla con más regularización, menos neuronas o parando antes.
    - **Las dos están altas y juntas:** la red es demasiado simple (subajuste).
    - **Las dos bajan y se estabilizan juntas:** buen ajuste.

    Para saber en qué época la validación fue mejor, ejecutad en una celda nueva (**+ Código**):

    ```python
    for s, h in zip((1, 2, 3), historiales):
        print(f"semilla {s}: la pérdida de validación es mínima en la época {int(np.argmin(h.history['val_loss'])) + 1} de {len(h.history['val_loss'])}")
    ```

    `zip((1, 2, 3), historiales)` empareja cada semilla con su historial; `np.argmin(…)` da la posición de la pérdida de validación más baja (contando desde 0) y el `+ 1` la pasa a «contando desde 1». `len(…)` es el número de épocas que se hicieron.

2. **Ejercicio 3: la función `diagnostico`.** Bajad al enunciado «Ejercicio 3» (sección 5). En su celda hay un `# TODO`, tres puntos `...` y varias líneas con `assert`. Borrad **solo los tres puntos** y escribid:

    ```python
    def diagnostico(historial, margen=0.03):
        pv, pe = historial.history["val_loss"], historial.history["loss"]
        if pv[-1] > min(pv) + margen or (pv[-1] - pe[-1]) > 0.15:
            return "sobreajuste"
        return "sin sobreajuste claro"
    ```

    Qué hace cada línea:

    - `def diagnostico(historial, margen=0.03):`: define la función. Recibe un historial de Keras y un `margen` (si no se dice, 0,03). No olvidéis los dos puntos del final.
    - `pv, pe = historial.history["val_loss"], historial.history["loss"]`: guarda en `pv` la lista de pérdidas de validación y en `pe` la de entrenamiento, una cifra por época. Los nombres `"val_loss"` y `"loss"` van entre comillas y **no se pueden cambiar**.
    - `if pv[-1] > min(pv) + margen or (pv[-1] - pe[-1]) > 0.15:`: la condición. Primera parte: ¿la pérdida de validación **final** (`pv[-1]`) supera a su **mínimo** (`min(pv)`) en más de `margen`? Segunda parte: ¿la validación final supera a la de entrenamiento en más de 0,15 (la brecha)? Con que se cumpla una de las dos, hay sobreajuste.
    - `return "sobreajuste"`: va **con 8 espacios** (está dentro del `if`) y devuelve esa palabra, escrita tal cual.
    - `return "sin sobreajuste claro"`: va con 4 espacios y es lo que se devuelve si la condición no se cumple.

    Pulsad ▶. Los `assert` prueban la función con dos historiales de juguete, y la celda aplica `diagnostico` a las tres semillas por sí sola.

3. **Escribir la frase de diagnóstico.** En una celda de texto (**+ Texto**) junto a la gráfica, y resumida luego en el informe del paso 6, una frase para vuestra mejor red con una cifra o una época. Molde: *«Con la variante [X], la validación deja de mejorar en la época [N] y el entrenamiento sigue bajando: [hay un poco de sobreajuste, que la parada temprana corta a tiempo / no hay sobreajuste claro: las dos curvas bajan juntas]».* Tiene que decir qué **veis** en vuestras curvas, no lo que «suele» pasar.

**Qué deberíais ver.** Tres líneas `semilla N: la pérdida de validación es mínima en la época X de Y`; tres líneas `MLP semilla 1: …` (y 2 y 3), cada una con `sobreajuste` o `sin sobreajuste claro`; y vuestra frase escrita junto a la gráfica. No hay una respuesta «correcta»: depende de vuestras curvas. Ojo: `diagnostico` mira la **última** época, que suele ser seis épocas posterior a la mejor (la parada temprana espera ese tiempo). Por eso puede salir `sobreajuste` aunque el cuaderno se quede con la mejor versión: en ese caso, contadlo así.

**Hecho cuando:** el ejercicio 3 pasa su comprobación y la frase de diagnóstico está escrita (en el cuaderno y, resumida, en el informe).

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'diagnostico' is not defined` | La celda del ejercicio 3 aún tiene los `...` o no se ha ejecutado. | Escribid la función y volved a pulsar ▶. |
| `IndentationError: expected an indented block…` | Las líneas de dentro de la función (o del `if`) no tienen sangría. | 4 espacios dentro de `def` y 8 en el `return` que cuelga del `if`. |
| `AssertionError: Validación creciente y brecha grande = sobreajuste` | La función no devuelve `"sobreajuste"` cuando la validación sube mucho. | Revisad la condición: `pv[-1] > min(pv) + margen`, el `or` y `> 0.15`. |
| `AssertionError: Curvas paralelas y juntas: sin sobreajuste` | La función dice `"sobreajuste"` con curvas buenas. | Comprobad que la brecha es `pv[-1] - pe[-1]` (validación menos entrenamiento) y que el 0.15 no se ha cambiado. |
| `AttributeError: 'list' object has no attribute 'history'` | Se ha pasado la lista `historiales` entera en vez de un historial. | Llamad a `diagnostico(h)` con uno de los tres (o dentro del `for` de la celda). |
| `AttributeError: 'dict' object has no attribute 'history'` | Se ha pasado `h.history` (el diccionario) en lugar de `h`. | Pasad `h`, sin el `.history`: la función ya lo añade. |
| Las tres semillas dicen `sobreajuste` | `diagnostico` mira la última época, que viene tras la «paciencia» de 6 épocas. | No es un fallo: miradlo en la gráfica y contadlo como «empezó a memorizar tras la época N; la parada temprana nos devuelve el mejor punto». |

<!--nav-->
---

[← Paso 3](Reto_Sprint_10_paso_3.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 5 →](Reto_Sprint_10_paso_5.md)
<!--/nav-->
