# Paso 3 · Variantes (día 2, 25 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 3 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 4 →](Reto_Sprint_10_paso_4.md)
<!--/nav-->

1. Probar **2 o 3 variantes** del MLP cambiando un solo ajuste cada vez.
2. Compararlas mirando **solo la validación**: el test no se toca.
3. Anotar en una tabla pequeña qué ha mejorado y qué no.

**En sencillo.** Imaginad que estáis ajustando una receta de cocina: más sal, menos tiempo de horno, otra temperatura. Si cambiáis tres cosas a la vez y el plato sale mejor, no sabéis cuál ayudó. Con la red pasa igual: tiene unos «botones» (cuántas neuronas, cuánto *dropout*, cuánta regularización L2, qué tan grandes son los retoques) y vais a probar **un botón cada vez**, siempre con las mismas tres semillas, y a comparar las notas **de validación**. La prueba (el examen final) sigue guardada en el cajón. Puede que ninguna variante mejore, y es un resultado válido: lo importante es apuntarlo con su número. No hace falta saber programar: copiáis una celda y cambiáis **un valor** cada vez.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Variante** | Una versión del MLP con un ajuste distinto del de la base. |
| **Ajuste** (hiperparámetro) | Un «botón» que se fija antes de entrenar: no lo aprende la red, lo elegís vosotros. |
| **Argumento con nombre** | Un valor que se pasa a una función escribiendo su nombre: `construir_mlp(35, dropout=0.5)`. Si el nombre está mal escrito, Python da error. |
| **`capas`** | Lista con el número de neuronas de cada capa oculta: `(64, 32)` son dos capas. Con una sola capa se escribe `(32,)`: **la coma del final es obligatoria**. |
| **`dropout`** | La fracción de neuronas que se apagan al azar en cada paso del entrenamiento (0.3 = el 30 %). |
| **`l2`** | La fuerza del castigo a los pesos grandes. Más L2 = red más contenida. |
| **`tasa`** | La tasa de aprendizaje: el tamaño de cada retoque. Muy grande, la red se pasa de largo; muy pequeña, tarda mucho. |
| **Ruido entre semillas** | Lo que cambia el resultado solo por la suerte de la semilla. Una mejora más pequeña que ese vaivén no cuenta. |

**Cómo se hace**

1. **Crear una celda para las variantes.** Justo después del ejercicio 2 (que ya debe pasar su comprobación), pulsad **+ Código** y pegad esta celda. Entrena la red con las tres semillas de siempre, pero guarda los resultados en listas **nuevas** (acabadas en `_v`) para no pisar `modelos_mlp` ni `historiales`:

    ```python
    etiqueta = "base"
    perd_ent_v, perd_val_v, aucs_v = [], [], []
    for semilla in (1, 2, 3):
        keras.utils.set_random_seed(semilla)
        m = construir_mlp(A_ent.shape[1], capas=(64, 32), l2=0.003, dropout=0.3, tasa=1e-3)
        h = m.fit(A_ent, y_ent, validation_data=(A_val, y_val), epochs=40, batch_size=64, verbose=0,
                  callbacks=[keras.callbacks.EarlyStopping(monitor="val_loss", patience=6, restore_best_weights=True)])
        mejor = int(np.argmin(h.history["val_loss"]))
        perd_ent_v.append(h.history["loss"][mejor])
        perd_val_v.append(h.history["val_loss"][mejor])
        aucs_v.append(roc_auc_score(y_val, m.predict(A_val, verbose=0).ravel()))
        print(f"semilla {semilla}: mejor época {mejor + 1} de {len(h.history['loss'])}")
    print(f"{etiqueta}: pérdida entrenamiento {np.mean(perd_ent_v):.3f} · pérdida validación {np.mean(perd_val_v):.3f} · AUC validación {np.mean(aucs_v):.3f} ± {np.std(aucs_v):.3f}")
    ```

    Qué hace cada línea:

    - `etiqueta = "base"`: un nombre para reconocer la prueba en lo que se escribe al final. Lo cambiaréis en cada variante.
    - `perd_ent_v, perd_val_v, aucs_v = [], [], []`: tres listas vacías donde se apuntará, por semilla, la pérdida de entrenamiento, la de validación y el AUC de validación.
    - `for semilla in (1, 2, 3):` y `keras.utils.set_random_seed(semilla)`: igual que en el paso 2: tres vueltas, cada una con su semilla.
    - `m = construir_mlp(A_ent.shape[1], capas=(64, 32), l2=0.003, dropout=0.3, tasa=1e-3)`: construye la red **escribiendo los cuatro ajustes**. Estos valores son los de la base. **Aquí es donde cambiáis un valor por variante** (y solo uno).
    - `h = m.fit(…)`: entrena exactamente igual que en el paso 2 (mismos datos, 40 épocas como máximo, parada temprana).
    - `mejor = int(np.argmin(h.history["val_loss"]))`: busca en qué época la pérdida de validación fue la más baja (`np.argmin` da la posición del valor más pequeño, contando desde 0). Esa es la época de la red que se queda, porque `restore_best_weights=True`.
    - `perd_ent_v.append(h.history["loss"][mejor])` y `perd_val_v.append(h.history["val_loss"][mejor])`: apuntan la pérdida de entrenamiento y la de validación **en esa mejor época**.
    - `aucs_v.append(roc_auc_score(y_val, m.predict(A_val, verbose=0).ravel()))`: el AUC de validación de esa red, como en el ejercicio 2.
    - `print(f"semilla …")`: escribe en qué época estaba lo mejor (`mejor + 1`, contando desde 1) y cuántas épocas hizo en total.
    - El `print` final: la media de las tres semillas de cada cifra y, tras el `±`, la desviación del AUC entre semillas (`np.std`), que es el ruido entre semillas.

2. **Ejecutar primero la base.** Con `etiqueta = "base"` y los valores tal cual, pulsad ▶. Tarda unos minutos como mucho. Apuntad la línea final: es la primera fila de la tabla y es **vuestra regla de medir** para las variantes (se mide igual que ellas).
3. **Probar 2 o 3 variantes, cambiando un solo valor.** Copiad la celda, cambiad `etiqueta` y **un único** valor de la línea de `construir_mlp`, y ejecutad. Ideas:

    - Menos neuronas: `capas=(32,)` (con la coma).
    - Más neuronas: `capas=(128, 64)`.
    - Más *dropout*: `dropout=0.5`.
    - Más L2: `l2=0.01`.
    - Retoques más pequeños: `tasa=3e-4` (se lee 0,0003).

    Si usáis otra paciencia en la parada temprana, cambiad `patience=6` por otro valor. Ejemplo de una variante: `etiqueta = "dropout 0.5"` y `m = construir_mlp(A_ent.shape[1], capas=(64, 32), l2=0.003, dropout=0.5, tasa=1e-3)`.

4. **Rellenar la tabla.** Una fila por prueba, con las cifras de la última línea de cada ejecución:

    | Variante | Qué cambia | Error en entrenamiento | Error en validación | AUC en validación |
    |---|---|---|---|---|
    | Base | `capas=(64, 32)`, `dropout=0.3`, `l2=0.003` | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |
    | Variante 1 | (lo que cambiáis) | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |
    | Variante 2 | (lo que cambiáis) | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |

    Añadid, por variante, una frase con el número: «mejoró» (cuánto), «empeoró» o «igual». Cuidado con L2: la pérdida incluye el castigo, así que con más L2 la pérdida **sube** aunque la red no sea peor. Entre variantes, comparad sobre todo el **AUC**.

5. **Elegir.** Quedaos con la variante de **mayor AUC en validación**. Si dos quedan casi iguales (la diferencia es menor que el `±` de cualquiera de ellas), es ruido: escoged la más sencilla (menos neuronas, menos capas). **Si miráis la prueba para decidir, ya no es una prueba.** Escribid en el documento del equipo cuál elegís y por qué.
6. **Dejar la elegida en el cuaderno.** Si la elegida no es la base, cambiad en la celda de la **sección 4** (la del paso 2) la línea `m = construir_mlp(A_ent.shape[1])` añadiendo el ajuste, por ejemplo `m = construir_mlp(A_ent.shape[1], dropout=0.5)`. Después ejecutad otra vez, **en orden y una a una**, la celda de la sección 4, la del ejercicio 2 y la de las curvas (sección 5). **No ejecutéis todavía la sección 6**: usa la prueba. Así los pasos 4 y 5 trabajan con la variante elegida.

**Qué deberíais ver.** Por cada ejecución, tres líneas `semilla N: mejor época X de Y` y una línea final con las cuatro cifras (por ejemplo, `base: pérdida entrenamiento 0.… · pérdida validación 0.… · AUC validación 0.7… ± 0.0…`). Al final, una tabla con la base y las 2–3 variantes y una frase por variante. Es muy posible que las diferencias de AUC sean pequeñas. Que una variante no mejore es un resultado válido: lo importante es apuntarlo.

**Hecho cuando:** tenéis la tabla rellena, habéis elegido una variante mirando solo la validación, sabéis explicar por qué y el cuaderno (sección 4) usa la elegida.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'construir_mlp' is not defined` (o `'A_ent'`, `'keras'`) | No se han ejecutado las celdas de las secciones 1 o 4. | Ejecutad desde arriba hasta la sección 4 y después la celda de variantes. |
| `TypeError: construir_mlp() got an unexpected keyword argument 'dropuot'` | Un nombre de ajuste está mal escrito. | Los nombres son `capas`, `l2`, `dropout` y `tasa`. |
| `TypeError: 'int' object is not iterable` | Habéis escrito `capas=32` en lugar de `capas=(32,)`. | Poned paréntesis y la coma del final. |
| La variante da exactamente los mismos números que la base | No ha cambiado ningún valor (o solo cambió `etiqueta`). | Cambiad el valor dentro de `construir_mlp(…)`, no solo el nombre. |
| Con `l2=0.01` la pérdida es más alta que en la base | La pérdida incluye el castigo L2. No quiere decir que la red sea peor. | Comparad por el AUC de validación. |
| El AUC sube 0.002 y no sabéis si cuenta | Es menos que el ruido entre semillas (el `±`). | Contadlo como «igual» y quedaos con la variante más sencilla. |
| La celda tarda mucho | Entrena tres redes cada vez. | Probad menos variantes (basta con 2) y esperad a las tres líneas `semilla …`. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_10_paso_2.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 4 →](Reto_Sprint_10_paso_4.md)
<!--/nav-->
