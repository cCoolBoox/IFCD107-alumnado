# Paso 4 · Demostrador y umbral de confianza (día 2, 15 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 5 →](Reto_Sprint_11_paso_5.md)
<!--/nav-->

1. Probar `clasificar_foto` con 2 o 3 fotos de la prueba.
2. Hacer el ejercicio 5: medir cobertura y acierto para varios umbrales.
3. Elegir el umbral y escribir la recomendación en una frase.

**En sencillo.** Imaginad que contratáis a alguien para clasificar fotos y le decís: «Si estás seguro, decide tú; si dudas, pásame la foto y la miro yo». Eso es lo que hace un modelo responsable. La **confianza** es lo seguro que está (de 0 a 1) y el **umbral** es la línea que ponéis: por encima de ella, el modelo decide solo; por debajo, la foto va a «revisar a mano». Si ponéis el umbral muy alto, el modelo decide pocas fotos pero casi siempre acierta; si lo ponéis muy bajo, decide casi todas pero se equivoca más. En este paso probáis la función que hace esto con fotos de verdad, medís las dos cosas con una función nueva y elegís dónde poner la línea. Lo importante no es sacar un número «bonito», sino **poder explicarle al cliente cuántas fotos revisa una persona y por qué**.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Demostrador** | Una función que recibe **una foto** y responde con la clase y lo segura que está. Es lo que enseñaréis al cliente. |
| **Confianza** | La probabilidad más alta que da el modelo a una foto, de 0 (nada seguro) a 1 (seguro del todo). |
| **Umbral** | La confianza mínima para que el modelo decida solo. Por debajo de ella, responde «revisar a mano». |
| **Cobertura** | De todas las fotos, la fracción que el modelo decide solo (las que superan el umbral). |
| **Precisión de las aceptadas** | De las fotos que el modelo decide solo, la fracción que acierta. |
| **Abstenerse** | No decidir y pasar la foto a una persona. Es lo que hace el modelo con las fotos que no supera el umbral. |
| **Tupla** | Un par o grupo de valores entre paréntesis, como `(0.5, 1.0)`. Una función puede devolver varios valores a la vez en una tupla. |
| **Máscara** | Una lista de `True` y `False`, una por foto, que dice cuáles cumplen una condición. Aquí: cuáles superan el umbral. |
| **Argumento con nombre** | Pasar un valor escribiendo su nombre: `umbral=0.9`. Es obligatorio en `clasificar_foto`, como se explica abajo. |

**Cómo se hace**

1. **Probar el demostrador.** Bajad a la sección 6 («Demostrador») y ejecutad su celda. Ya está escrita y **no hay que modificarla**. El cuaderno la coloca bajo la línea «A partir de aquí, en casa», pero en el reto sí se hace. Su código es este:

    ```python
    def clasificar_foto(ruta_imagen, modelo_=None, umbral=0.7):
        """Devuelve (clase, confianza, probabilidades por clase) o 'revisar a mano' si la confianza es baja."""
        modelo_ = modelo_ or modelo
        img = keras.utils.load_img(ruta_imagen, target_size=(TAM, TAM))
        p = modelo_.predict(np.expand_dims(keras.utils.img_to_array(img), 0), verbose=0)[0]
        clase = NOMBRES[int(p.argmax())] if p.max() >= umbral else "revisar a mano"
        return clase, float(p.max()), dict(zip(NOMBRES, p.round(3)))

    demo_ruta = rutas_pru[0]
    print("Foto:", demo_ruta, "· real:", NOMBRES[y_pru[0]])
    print(clasificar_foto(demo_ruta))
    ```

    Qué hace cada línea:

    - `def clasificar_foto(ruta_imagen, modelo_=None, umbral=0.7):`: recibe la ruta de una foto, opcionalmente un modelo (si no se dice, usa el vuestro) y el umbral (0,7 si no se dice).
    - `modelo_ = modelo_ or modelo`: «si no me han dado modelo, uso `modelo`», el que entrenasteis en el paso 2.
    - `img = keras.utils.load_img(ruta_imagen, target_size=(TAM, TAM))`: abre la foto del disco y la deja del tamaño que espera la red (48 × 48).
    - `p = modelo_.predict(np.expand_dims(keras.utils.img_to_array(img), 0), verbose=0)[0]`: pasa la foto a números, le añade una dimensión (la red espera un lote de fotos, aunque sea de una) y obtiene las 5 probabilidades. El `[0]` se queda con la única fila.
    - `clase = NOMBRES[int(p.argmax())] if p.max() >= umbral else "revisar a mano"`: si la probabilidad más alta llega al umbral, la clase es la de esa probabilidad; si no, la respuesta es `"revisar a mano"`.
    - `return clase, float(p.max()), dict(zip(NOMBRES, p.round(3)))`: devuelve tres cosas: la clase (o «revisar a mano»), la confianza y un diccionario con la probabilidad de cada clase, con tres decimales.
    - `demo_ruta = rutas_pru[0]` y los dos `print`: eligen la primera foto de la prueba, escriben su ruta y la clase real y muestran lo que responde la función.

    La misma celda termina guardando el modelo en una carpeta temporal, recargándolo y comprobando que responde igual (`modelo.save(…)`, `keras.models.load_model(…)`). No hay que hacer nada; sirve para asegurar que el modelo se puede guardar y reutilizar. Después borra la carpeta temporal.

2. **Probar con 2 o 3 fotos.** En una celda nueva (**+ Código**) ejecutad:

    ```python
    for i in (0, 1, 2):
        print("real:", NOMBRES[y_pru[i]], "→", clasificar_foto(rutas_pru[i], umbral=0.9)[:2])
    ```

    Qué hace cada línea:

    - `for i in (0, 1, 2):`: repite lo de debajo tres veces, con `i` valiendo 0, 1 y 2 (las tres primeras fotos de la prueba). Cambiad los números para ver otras.
    - `print("real:", NOMBRES[y_pru[i]], "→", …)`: escribe la clase real de la foto `i` y, a continuación, la respuesta del demostrador.
    - `clasificar_foto(rutas_pru[i], umbral=0.9)[:2]`: llama a la función con un umbral de 0,9; el `[:2]` se queda solo con los dos primeros valores de lo que devuelve (la clase y la confianza) para que sea más corto.

    **Importante:** el umbral se escribe siempre con su nombre (`umbral=0.9`). La función tiene como segundo argumento el modelo (`modelo_`): si escribís `clasificar_foto(ruta, 0.9)`, Python cree que 0,9 es el modelo y da error. Probad también `umbral=0.5` y `umbral=0.99` con la misma foto y fijaos en cómo cambia la respuesta.

3. **Ejercicio 5: cobertura y precisión de las aceptadas.** Bajad al enunciado de la sección 5 («IA responsable»), borrad los tres puntos `...` de su celda y escribid:

    ```python
    def cobertura_y_precision(prob, y_real, umbral):
        aceptadas = prob.max(axis=1) >= umbral
        if aceptadas.sum() == 0:
            return 0.0, 0.0
        aciertos = prob.argmax(axis=1)[aceptadas] == y_real[aceptadas]
        return float(aceptadas.mean()), float(aciertos.mean())
    ```

    Qué hace cada línea:

    - `def cobertura_y_precision(prob, y_real, umbral):`: define la función. Recibe la tabla de probabilidades, las clases reales y el umbral. Los dos puntos del final son obligatorios.
    - `aceptadas = prob.max(axis=1) >= umbral`: `prob.max(axis=1)` es la confianza de cada foto. Comparada con el umbral da una **máscara**: `True` para las fotos que el modelo decide solo.
    - `if aceptadas.sum() == 0:`: `sum()` cuenta los `True`. Si no se acepta ninguna foto no se puede calcular nada...
    - `return 0.0, 0.0`: ...así que se devuelve `(0.0, 0.0)`, que es lo que pide el enunciado. Esta línea va con **8 espacios** (está dentro del `if`).
    - `aciertos = prob.argmax(axis=1)[aceptadas] == y_real[aceptadas]`: se queda solo con las fotos aceptadas (`[aceptadas]`) y comprueba, para cada una, si la clase elegida coincide con la real. El resultado es otra lista de `True` y `False`.
    - `return float(aceptadas.mean()), float(aciertos.mean())`: la media de una lista de `True`/`False` es la fracción de `True`. La primera es la **cobertura** (fracción de fotos aceptadas); la segunda, la **precisión de las aceptadas**. Se devuelven juntas, en una tupla, y siempre en este orden.

    Pulsad ▶. Los `assert` de debajo usan una tabla de juguete de 4 fotos.

4. **Medir varios umbrales.** Ejecutad la celda siguiente, que ya está escrita: calcula la función para los umbrales `0.0`, `0.5`, `0.7`, `0.9` y `0.95` con las probabilidades de la prueba y muestra una tabla con la cobertura y la «precisión en las aceptadas» de cada uno. Fijaos en tres cosas: con umbral `0.0` se acepta todo (cobertura 1) y la precisión es la global del paso 3; **la cobertura solo puede bajar** al subir el umbral; y la precisión de las aceptadas suele subir (no siempre). Con solo 60 fotos, una foto más o menos mueve las cifras unos 1,7 puntos: no saquéis conclusiones de diferencias pequeñas.

5. **Elegir el umbral.**

    - **Estándar:** os basta con el umbral que trae el cuaderno (`0.7`) y explicar con vuestras palabras qué hace y qué cifras da en la tabla.
    - **Extra (el nivel «extra» de la rúbrica):** elegirlo con datos. Como la tabla del cuaderno usa la **prueba**, para decidir sin hacer trampa hay que calcularla sobre la **validación**. Añadid una celda con:

    ```python
    prob_val = modelo.predict(X_val, verbose=0)
    tabla_val = pd.DataFrame([cobertura_y_precision(prob_val, y_val, u) for u in umbrales], index=umbrales,
                             columns=["cobertura", "precisión en las aceptadas"]).round(3)
    tabla_val.index.name = "umbral de confianza"
    tabla_val
    ```

    Es la misma cuenta de la celda anterior, pero con `X_val` e `y_val` en lugar de las de la prueba: `modelo.predict(X_val, …)` da las probabilidades de validación y la lista `[… for u in umbrales]` calcula una fila por cada umbral. Elegid el umbral que equilibre fotos revisadas a mano y errores evitados, y después comprobad una sola vez qué da en la prueba.

    Pensad también qué error es peor para TurisData: confundir «apartamentos» con «hotel» o clasificar un camping como piscina. Cuanto más cuesta equivocarse, más alto debería ser el umbral.

6. **La frase para el cliente.** Escribidla ya, con números de la tabla: *«Con un umbral de […], el modelo decide solo el […] % de las fotos y acierta el […] % de ellas; el resto ([…] %) lo revisa una persona»*. Si la cobertura es 0,8 (el 80 %), el resto, un 20 %, lo revisa una persona: son las fotos para revisar.

**Qué deberíais ver.**
- **Del demostrador:** una tupla de tres valores: la clase (o `revisar a mano`), la confianza con muchos decimales (por ejemplo `0.8999…`) y un diccionario con las 5 probabilidades. Con NumPy reciente, las probabilidades pueden salir como `np.float32(0.9)` en vez de `0.9`: es el mismo número.
- **Del bucle de 3 fotos:** tres líneas `real: … → ('…', 0.…)`, a veces con `'revisar a mano'`.
- **De la tabla de umbrales:** cinco filas con las columnas `cobertura` y `precisión en las aceptadas`, con la cobertura bajando de arriba abajo.
- **Para el extra:** una segunda tabla, igual pero calculada en validación.

**Hecho cuando:** `clasificar_foto` funciona con 2 o 3 fotos delante del equipo, `cobertura_y_precision` pasa sus comprobaciones y tenéis anotado el umbral elegido con su frase.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `AttributeError: 'float' object has no attribute 'predict'` | Habéis escrito el umbral sin su nombre, así que Python lo toma como el modelo. | Escribid `clasificar_foto(ruta, umbral=0.9)`. |
| `NameError: name 'rutas_pru' is not defined` (o `'modelo'`, `'y_pru'`) | Colab se desconectó o no se ejecutaron las celdas de los pasos 1 a 3. | Ejecutad desde arriba, por orden, hasta la sección 3 y después el demostrador. |
| `FileNotFoundError: [Errno 2] No such file or directory: …` | La ruta de la foto no existe: está mal escrita o la carpeta `datos_sinteticos` se ha borrado. | Usad `rutas_pru[0]`, `rutas_pru[1]`… en vez de escribir la ruta a mano. Si se ha borrado, volved a ejecutar la celda de la sección 1. |
| `NameError: name 'cobertura_y_precision' is not defined` | La celda del ejercicio 5 todavía tiene los `...`. | Escribid la función y volved a pulsar ▶. |
| `AssertionError: Con umbral 0.65 se aceptan 2 de 4 (filas 0 y 2) y ambas aciertan` | La cuenta o el orden están mal: se calculan los aciertos sobre todas las fotos y no solo sobre las aceptadas, o se devuelve primero la precisión y después la cobertura. | Revisad que `aciertos` usa `[aceptadas]` y que se devuelve `(cobertura, precisión)`, en ese orden. |
| `AssertionError: Si no se acepta ninguna: (0.0, 0.0)` | Falta el caso especial, o devuelve otra cosa. | Añadid el `if aceptadas.sum() == 0:` con `return 0.0, 0.0` dentro. |
| `IndentationError: expected an indented block after 'if' statement on line …` | El `return` de dentro del `if` no tiene sangría. | Ponedle 8 espacios (4 del `def` y 4 más del `if`). |

<!--nav-->
---

[← Paso 3](Reto_Sprint_11_paso_3.md) · [Ficha del reto](Reto_Sprint_11.md) · [Paso 5 →](Reto_Sprint_11_paso_5.md)
<!--/nav-->
