# Paso 2 · Entrenar con *transfer learning* y una referencia (día 2, 25 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 3 →](Reto_Sprint_11_paso_3.md)
<!--/nav-->

1. Preparar la base preentrenada y hacer el ejercicio 2 (`modelo_transfer`).
2. Entrenar el modelo con la base congelada y después hacer el ajuste fino del último bloque.
3. Entrenar una referencia «desde cero» con la misma arquitectura.
4. Anotar la exactitud de validación de las tres versiones.

**En sencillo.** Pensad en una persona que ya sabe distinguir rayas, cuadrículas, círculos y triángulos: si ahora le enseñáis a reconocer hoteles y campings, aprenderá más rápido que alguien que no ha visto nunca un dibujo. Eso es el ***transfer learning***: se parte de una red que ya aprendió a ver formas y texturas (la **base**), se le **congela** lo aprendido para no estropearlo y solo se entrena una parte nueva al final (la **cabeza**), que es la que da la respuesta «hotel, camping…». Después, el **ajuste fino** descongela el último bloque de la base y lo retoca muy despacio. Y para saber si todo ese esfuerzo sirve, se entrena también una **referencia «desde cero»**: la misma red sin ningún aprendizaje previo. Al final tenéis tres notas de validación que comparar. No hace falta saber cómo funciona una red por dentro: copiáis, ejecutáis y leéis las cifras.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| ***Transfer learning*** | Reutilizar una red que ya aprendió una tarea (aquí, reconocer formas y texturas) para una tarea nueva (reconocer alojamientos). |
| **Base preentrenada** | La parte de la red que mira la imagen y detecta formas. Ya viene entrenada con una tarea auxiliar. |
| **Cabeza** | Las capas nuevas del final de la red, con una neurona por clase. Es lo único que se entrena al principio. |
| **Congelar** (`trainable = False`) | Impedir que unas capas cambien al entrenar. Lo aprendido se queda como está. |
| **Ajuste fino** (*fine-tuning*) | Descongelar el último bloque de la base y entrenarlo un poco más, con retoques muy pequeños. |
| **Tasa de aprendizaje** | El tamaño de cada retoque al entrenar. En el ajuste fino es diez veces menor: `1e-4` se lee 0,0001. |
| **Referencia «desde cero»** | La misma red sin preentrenar, entrenada con las mismas fotos, para ver cuánto aporta el *transfer learning*. |
| **Época** | Una pasada de la red por todas las fotos de entrenamiento. `epochs=30` son 30 pasadas. |
| **Exactitud de validación** | La fracción de las 60 fotos de validación que acierta el modelo (0,883 = 88,3 %). Sirve para ensayar y comparar; la prueba no se toca. |

**Cómo se hace**

1. **Preparar la base preentrenada.** Bajad a la sección 2 («El modelo: *transfer learning*») y ejecutad su celda, que ya está escrita y **no hay que modificarla**. El propio cuaderno avisa de que tarda unos 15 segundos. Su código es este:

    ```python
    def construir_base(nombre="base"):
        entrada = keras.layers.Input(shape=(TAM, TAM, 3))
        x = keras.layers.Rescaling(1 / 255)(entrada)
        for i, f in enumerate((16, 32, 64), start=1):
            x = keras.layers.Conv2D(f, 3, padding="same", activation="relu", name=f"bloque{i}_conv")(x)
            x = keras.layers.MaxPooling2D(name=f"bloque{i}_pool")(x)
        x = keras.layers.Flatten(name="aplanar")(x)
        return keras.Model(entrada, x, name=nombre)

    def con_cabeza(base, n_clases, dropout=0.3, tasa=1e-3):
        entrada = keras.layers.Input(shape=(TAM, TAM, 3))
        x = keras.layers.Dropout(dropout)(base(entrada))
        salida = keras.layers.Dense(n_clases, activation="softmax", name="cabeza")(x)
        m = keras.Model(entrada, salida)
        m.compile(keras.optimizers.Adam(tasa), "sparse_categorical_crossentropy", metrics=["accuracy"])
        return m

    # Tarea auxiliar: formas y texturas (ejecuta unos 15 s)
    X_aux, y_aux = generar_lote(dibujar_forma, CLASES_FORMAS, 400, semilla=3, tam=TAM)
    keras.utils.set_random_seed(SEMILLA)
    base_pre = construir_base("base_preentrenada")
    con_cabeza(base_pre, len(CLASES_FORMAS), dropout=0.0).fit(X_aux, y_aux, epochs=12, batch_size=64, verbose=0)
    print("Base preentrenada lista:", base_pre.count_params(), "parámetros")
    ```

    Qué hace cada parte:

    - `def construir_base(nombre="base"):`: una función que monta la base. Recibe un nombre para reconocerla.
    - `keras.layers.Input(shape=(TAM, TAM, 3))` y `Rescaling(1 / 255)`: la entrada son imágenes de `TAM` × `TAM` píxeles (48 × 48) con 3 colores, y el valor de cada píxel se pasa de 0–255 a 0–1.
    - `for i, f in enumerate((16, 32, 64), start=1):`: repite tres veces, con `i` = 1, 2, 3 y `f` = 16, 32, 64. Cada vuelta añade un **bloque**.
    - `Conv2D(f, 3, …, name=f"bloque{i}_conv")`: una capa que desliza `f` mirillas pequeñas de 3 × 3 sobre la imagen para detectar formas (bordes, esquinas, rayas). Su **nombre** (`bloque1_conv`, `bloque2_conv`, `bloque3_conv`) importa: el ajuste fino buscará el bloque 3 por el nombre.
    - `MaxPooling2D(name=f"bloque{i}_pool")`: reduce la imagen a la mitad quedándose con lo más llamativo de cada zona.
    - `Flatten(…)` y `return keras.Model(entrada, x, name=nombre)`: alisa el resultado en una lista de números y empaqueta todo como un modelo: la base.
    - `def con_cabeza(base, n_clases, dropout=0.3, tasa=1e-3):`: pone la cabeza sobre una base.
    - `Dropout(dropout)(base(entrada))`: pasa la imagen por la base y apaga al azar un 30 % de las conexiones al entrenar, para que la red no memorice.
    - `Dense(n_clases, activation="softmax", name="cabeza")`: la cabeza: una neurona por clase, y `softmax` convierte sus salidas en probabilidades que suman 1.
    - `m.compile(keras.optimizers.Adam(tasa), …)`: deja el modelo listo para entrenar: `Adam` es el método que va corrigiendo los pesos con retoques de tamaño `tasa`; la pérdida (`sparse_categorical_crossentropy`) mide cuánto se equivoca; y `metrics=["accuracy"]` pide también el porcentaje de aciertos.
    - `X_aux, y_aux = generar_lote(dibujar_forma, CLASES_FORMAS, 400, …)`: crea dibujos de la **tarea auxiliar**: formas y texturas como rayas, cuadrículas, puntos, círculos y triángulos. No son alojamientos: es la «experiencia previa».
    - `keras.utils.set_random_seed(SEMILLA)`: fija el azar para que la red empiece siempre igual.
    - `base_pre = construir_base("base_preentrenada")`: crea la base.
    - `con_cabeza(base_pre, len(CLASES_FORMAS), dropout=0.0).fit(…, epochs=12, …)`: le pone una cabeza **provisional** (una neurona por forma) y la entrena 12 épocas con esos dibujos; así la base aprende a ver formas. La cabeza se tira después. `verbose=0` hace que no escriba nada mientras entrena.
    - `print("Base preentrenada lista:", base_pre.count_params(), "parámetros")`: escribe cuántos números ajustables tiene la base.

2. **Ejercicio 2: `modelo_transfer`.** Bajad al enunciado «Ejercicio 2». En su celda hay un `# TODO`, tres puntos `...` y tres líneas con `assert`. Borrad **solo los tres puntos** y escribid:

    ```python
    def modelo_transfer(base_preentrenada, n_clases):
        copia = keras.models.clone_model(base_preentrenada)
        copia.set_weights(base_preentrenada.get_weights())
        copia.trainable = False
        return con_cabeza(copia, n_clases), copia
    ```

    Qué hace cada línea:

    - `def modelo_transfer(base_preentrenada, n_clases):`: define la función. Recibe la base y el número de clases (5). No olvidéis los dos puntos.
    - `copia = keras.models.clone_model(base_preentrenada)`: hace una **copia** de la base con la misma estructura, pero con pesos nuevos al azar.
    - `copia.set_weights(base_preentrenada.get_weights())`: le pasa a la copia lo que sabe la original (`get_weights()` saca los pesos aprendidos; `set_weights(…)` los pone). Sin esta línea la copia no sabría nada.
    - `copia.trainable = False`: **congela** la copia. Se congela la copia y no la original: el `assert` lo comprueba.
    - `return con_cabeza(copia, n_clases), copia`: devuelve **dos cosas** separadas por una coma (una *tupla*): el modelo completo (copia congelada más cabeza nueva) y la propia copia, que se usará luego en el ajuste fino. La celda siguiente espera exactamente eso, aunque el enunciado no lo diga.

    Pulsad ▶. Si no sale nada, los tres `assert` han pasado: la copia está congelada, la original no, y la salida tiene una neurona por clase.

3. **Entrenar: base congelada, ajuste fino y referencia.** Ejecutad la celda siguiente, que ya está escrita:

    ```python
    keras.utils.set_random_seed(SEMILLA)
    modelo, base_congelada = modelo_transfer(base_pre, N_CLASES)
    modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=30, batch_size=16, verbose=0)
    print("Exactitud de validación con base congelada:", round(modelo.evaluate(X_val, y_val, verbose=0)[1], 3))

    # Fine-tuning del último bloque con tasa pequeña (y recompilando)
    base_congelada.trainable = True      # primero se descongela la base entera...
    for capa in base_congelada.layers:
        capa.trainable = capa.name.startswith("bloque3")   # ...y solo el último bloque queda entrenable
    modelo.compile(keras.optimizers.Adam(1e-4), "sparse_categorical_crossentropy", metrics=["accuracy"])
    h = modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=25, batch_size=16, verbose=0)
    print("Exactitud de validación tras fine-tuning:", round(modelo.evaluate(X_val, y_val, verbose=0)[1], 3))

    # Referencia: la misma arquitectura entrenada desde cero
    keras.utils.set_random_seed(SEMILLA)
    desde_cero = con_cabeza(construir_base("desde_cero"), N_CLASES)
    desde_cero.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=40, batch_size=16, verbose=0)
    print("Exactitud de validación desde cero:", round(desde_cero.evaluate(X_val, y_val, verbose=0)[1], 3))
    ```

    Qué hace cada parte:

    - `modelo, base_congelada = modelo_transfer(base_pre, N_CLASES)`: usa vuestra función y recoge las dos cosas que devuelve.
    - `modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=30, batch_size=16, …)`: entrena 30 épocas con las fotos de entrenamiento, en lotes de 16, y mira cómo va con las de validación. Solo se ajusta la cabeza.
    - `print("Exactitud de validación con base congelada:", round(modelo.evaluate(X_val, y_val, verbose=0)[1], 3))`: `evaluate` devuelve dos cifras (la pérdida y la exactitud); el `[1]` se queda con la exactitud y `round(…, 3)` la deja con tres decimales.
    - `base_congelada.trainable = True`: **descongela** la copia entera, para poder decidir capa a capa. Enseguida se vuelve a congelar casi todo.
    - `for capa in base_congelada.layers:` y `capa.trainable = capa.name.startswith("bloque3")`: recorre las capas de la copia y deja sueltas solo las que se llaman `bloque3…` (`bloque3_conv` y `bloque3_pool`); las demás se quedan congeladas.
    - `modelo.compile(keras.optimizers.Adam(1e-4), …)`: **vuelve a compilar** para que el cambio de congelado surta efecto, con una tasa de aprendizaje diez veces menor (retoques pequeños).
    - `h = modelo.fit(…, epochs=25, …)` y el segundo `print`: 25 épocas más con el último bloque suelto, y la nueva exactitud de validación.
    - `desde_cero = con_cabeza(construir_base("desde_cero"), N_CLASES)`: la **referencia**: la misma arquitectura, con una base nueva que no ha aprendido nada. Se entrena 40 épocas con todo suelto, y el último `print` escribe su exactitud de validación.

    La celda no escribe nada mientras entrena y puede tardar un rato (hasta algún minuto): esperad a que aparezcan las tres líneas.

4. **Anotar las tres cifras.** La celda escribe las tres exactitudes de validación (base congelada, tras el ajuste fino y desde cero). Apuntad en el documento del equipo las tres cifras:

    | Versión | Exactitud de validación |
    |---|---|
    | *Transfer learning* con la base congelada | (vuestra cifra) |
    | *Transfer learning* tras el ajuste fino | (vuestra cifra) |
    | Desde cero | (vuestra cifra) |

    **Solo se mide en validación.** La prueba no se toca todavía.

5. **Extra (opcional, necesita internet).** Con fotos reales en Colab podéis probar la rama de MobileNetV2 de la sección 7 del cuaderno (`USAR_INTERNET = True`, un `TAM` de 96 a 160 y `construir_mobilenet(N_CLASES, pesos="imagenet")`). El propio cuaderno avisa de que la descarga de pesos no está verificada en el taller. Si hay dudas, preguntad al docente. Pista de apoyo: el cuaderno de práctica [`S11_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_02_transfer_learning.ipynb) explica el *transfer learning* paso a paso.

**Qué deberíais ver.**
- **De la celda de la base:** `Base preentrenada lista: 23584 parámetros`. Ese número depende solo de la arquitectura, así que debe salir igual.
- **Del ejercicio 2:** nada, si los `assert` pasan.
- **Del entrenamiento:** dos líneas, `Exactitud de validación con base congelada: 0.…` y `Exactitud de validación tras fine-tuning: 0.…`, y después, de la celda que añadisteis, `Exactitud de validación desde cero: 0.…`. Las cifras van de 0 a 1 y, como la validación tiene 60 fotos, cada foto de más o de menos mueve la cifra unos 0,017.
- **Lo esperable:** que el ajuste fino quede igual o mejor que la base congelada, y que el *transfer learning* quede igual o mejor que la referencia. Si no es así, no es un error: anotadlo y pensad por qué (las fotos con ruido, las etiquetas dudosas o que la tarea auxiliar se parezca poco).

**Hecho cuando:** `modelo_transfer` pasa sus comprobaciones y tenéis anotadas las tres cifras de validación.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'modelo_transfer' is not defined` | La celda del ejercicio 2 todavía tiene los `...` o no se ha ejecutado. | Escribid la función y pulsad ▶ antes de la celda de entrenar. |
| `NameError: name 'base_pre' is not defined` (o `'X_ent'`, `'N_CLASES'`) | No se ejecutó la celda de la base o las del paso 1, o Colab se desconectó. | Ejecutad desde arriba, por orden, hasta la celda que falla. |
| `AssertionError: La copia de la base debe estar congelada` | Falta la línea que congela la copia. | Añadid `copia.trainable = False` antes del `return`. |
| `AssertionError: No congeles la base original: trabaja sobre una copia` | Se ha congelado `base_preentrenada` en vez de `copia`. | Cambiad el nombre: la línea es `copia.trainable = False`. |
| `AssertionError: La salida debe tener una neurona por clase` | La cabeza no se ha creado con `n_clases`. | Devolved `con_cabeza(copia, n_clases)`, con `n_clases` y no un número escrito a mano. |
| `TypeError: cannot unpack non-iterable Functional object` (o `NoneType object`) | La función devuelve solo el modelo (o nada) y se esperan dos cosas. | La última línea debe ser `return con_cabeza(copia, n_clases), copia`, con la coma. |
| `NameError: name 'desde_cero' is not defined` | Se ejecutó la celda de la referencia antes que la de entrenar, o no se ejecutó. | Ejecutad la celda de entrenar entera y esperad a que termine. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_11_paso_1.md) · [Ficha del reto](Reto_Sprint_11.md) · [Paso 3 →](Reto_Sprint_11_paso_3.md)
<!--/nav-->
