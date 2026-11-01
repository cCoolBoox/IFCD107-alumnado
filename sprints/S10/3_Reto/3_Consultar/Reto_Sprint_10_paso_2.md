# Paso 2 · Primera red (día 2, 25 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 2 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 3 →](Reto_Sprint_10_paso_3.md)
<!--/nav-->

1. Comprobar que los datos están escalados **ajustando el escalador solo con el entrenamiento**.
2. Entrenar un MLP pequeño en CPU, con un máximo de 40 épocas.
3. Dibujar la curva de aprendizaje: error en entrenamiento y en validación.
4. Hacer el ejercicio 2 (el AUC de cada semilla).

**En sencillo.** Una red neuronal es como un equipo de «calculadoras» pequeñas colocadas en filas: cada una hace una cuenta sencilla con los datos de la reserva y pasa su resultado a las de la fila siguiente. La última da un número entre 0 y 1: la probabilidad de que la reserva se cancele. Al principio las cuentas son casi al azar; **entrenar** es repasar las reservas una y otra vez, comprobar cuánto se equivoca y retocar un poquito las cuentas para que se equivoque menos. Cada repaso completo se llama **época**. Y como en un examen, hay dos notas: la de los ejercicios que ya ha visto (entrenamiento) y la de un simulacro con preguntas nuevas (validación). Aquí solo ejecutáis código que ya está escrito y lo leéis; escribís una única línea propia (ejercicio 2). **No hace falta** entender las matemáticas de dentro: basta con saber qué significa cada gráfica.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **MLP** | «Perceptrón multicapa»: la red más sencilla, formada por capas de neuronas, cada una conectada con todas las de la siguiente. |
| **Capa y neurona** | Una neurona es una cuenta pequeña (multiplicar, sumar y aplicar una regla). Una capa es un grupo de neuronas en paralelo. Aquí hay dos capas «ocultas» (de 64 y de 32 neuronas) y una de salida. |
| **Época** | Un repaso completo a todas las reservas de entrenamiento. |
| **Pérdida** (*loss*) | La nota del error: cuanto más baja, menos se equivoca la red. |
| **Curva de aprendizaje** | El dibujo de la pérdida época a época, una línea para entrenamiento y otra para validación. |
| **Escalar** | Poner todas las columnas numéricas en una escala parecida (media 0 y desviación 1) para que ninguna «grite» más que las otras. Las redes lo necesitan. |
| **Fuga de datos** | Que el modelo (o el escalador) se entere de algo del examen final antes de tiempo, y la nota salga mejor de lo que merece. |
| **Parada temprana** (*EarlyStopping*) | Parar el entrenamiento cuando la validación deja de mejorar y quedarse con la mejor versión. |
| **Regularización** (L2 y *dropout*) | Trucos para que la red no memorice: L2 castiga los pesos muy grandes; *dropout* apaga neuronas al azar mientras entrena. |

**Cómo se hace**

1. **Entender cómo se escalaron los datos.** En el paso 1 ejecutasteis la celda de la sección 1, que ya escala los datos. Estas son las líneas que lo hacen (no las escribís):

    ```python
    pre = ColumnTransformer([("n", StandardScaler(), num), ("c", OneHotEncoder(handle_unknown="ignore"), cat)])
    A_ent = pre.fit_transform(X_ent).astype("float32")
    A_val = pre.transform(X_val).astype("float32")
    A_pru = pre.transform(X_pru).astype("float32")
    ```

    Qué hace cada línea:

    - `pre = ColumnTransformer([…])`: define el preparador: las columnas numéricas (`num`) se escalan con `StandardScaler()` y las de texto (`cat`) se convierten en columnas de 0 y 1 con `OneHotEncoder` (una columna por cada valor posible).
    - `pre.fit_transform(X_ent)`: **`fit`** = «aprende» las medias y desviaciones, y **`transform`** = «aplica». Con `fit_transform` se hacen las dos cosas **solo con las reservas de entrenamiento**.
    - `pre.transform(X_val)` y `pre.transform(X_pru)`: aplican **las mismas medias y desviaciones aprendidas** a validación y prueba, sin volver a aprender nada. Si el escalador aprendiera también con la prueba, la red «se enteraría» del examen: eso es una **fuga**.
    - `.astype("float32")`: guarda los números con menos decimales, que es lo que espera la red.

    Para comprobarlo, añadid una celda nueva (botón **+ Código**) y ejecutad:

    ```python
    print(A_ent[:, :9].mean(axis=0).round(2))
    print(A_val[:, :9].mean(axis=0).round(2))
    ```

    `A_ent[:, :9]` coge todas las filas y las 9 primeras columnas (las numéricas, que el preparador coloca delante); `.mean(axis=0)` calcula la media de cada columna y `.round(2)` deja dos decimales.

2. **Entrenar el MLP.** Ejecutad la celda de la sección 4, «El MLP, con las buenas prácticas del Sprint 10». Ya está escrita: **no cambiéis ningún número todavía** (en el paso 3 probaréis variantes). Tarda como mucho unos minutos y no escribe nada hasta terminar cada semilla. Este es el código:

    ```python
    def construir_mlp(n_entradas, capas=(64, 32), l2=0.003, dropout=0.3, tasa=1e-3):
        m = keras.Sequential([keras.layers.Input(shape=(n_entradas,))])
        for u in capas:
            m.add(keras.layers.Dense(u, activation="relu", kernel_regularizer=keras.regularizers.l2(l2)))
            m.add(keras.layers.Dropout(dropout))
        m.add(keras.layers.Dense(1, activation="sigmoid"))
        m.compile(optimizer=keras.optimizers.Adam(tasa), loss="binary_crossentropy", metrics=[keras.metrics.AUC(name="auc")])
        return m

    modelos_mlp, historiales, tiempos = [], [], []
    for semilla in (1, 2, 3):
        keras.utils.set_random_seed(semilla)
        t0 = time.time()
        m = construir_mlp(A_ent.shape[1])
        h = m.fit(A_ent, y_ent, validation_data=(A_val, y_val), epochs=40, batch_size=64, verbose=0,
                  callbacks=[keras.callbacks.EarlyStopping(monitor="val_loss", patience=6, restore_best_weights=True)])
        tiempos.append(time.time() - t0)
        modelos_mlp.append(m); historiales.append(h)
        print(f"semilla {semilla}: {len(h.history['loss'])} épocas, AUC validación = {max(h.history['val_auc']):.3f} (máx.)")
    ```

    Qué hace cada parte:

    - `def construir_mlp(…)`: la receta que construye la red. Lo que va tras cada `=` es el ajuste por defecto: `capas=(64, 32)` (dos capas ocultas, de 64 y 32 neuronas), `l2=0.003`, `dropout=0.3` (apaga el 30 % de las neuronas) y `tasa=1e-3` (0,001: el tamaño de cada retoque, la **tasa de aprendizaje**).
    - `keras.Sequential([keras.layers.Input(…)])`: una red vacía que recibe `n_entradas` números por reserva (aquí, 35).
    - `for u in capas:` y `m.add(…Dense(u, activation="relu", …))`: por cada tamaño de la lista añade una capa de `u` neuronas. `relu` es su regla (si el resultado es negativo lo pone a 0) y `kernel_regularizer=…l2(l2)` activa el castigo L2.
    - `m.add(…Dropout(dropout))`: después de cada capa, el *dropout*.
    - `m.add(…Dense(1, activation="sigmoid"))`: la capa final: una neurona que da un número entre 0 y 1, la probabilidad de cancelar.
    - `m.compile(…)`: dice cómo se entrena: `Adam` es el método para retocar las cuentas, `binary_crossentropy` es la fórmula de la pérdida para un sí/no, y `AUC` es la nota que se vigila además.
    - `modelos_mlp, historiales, tiempos = [], [], []`: tres listas vacías donde se guardarán las redes, su historial y lo que tardan.
    - `for semilla in (1, 2, 3):`: repite lo de debajo tres veces, con semillas 1, 2 y 3. Así se ve cuánto depende el resultado de la suerte.
    - `m = construir_mlp(A_ent.shape[1])`: construye la red; `A_ent.shape[1]` es el número de columnas (35).
    - `m.fit(A_ent, y_ent, validation_data=(A_val, y_val), epochs=40, batch_size=64, …)`: **entrena**. Aprende con entrenamiento, se examina con validación al final de cada época, hace como máximo 40 épocas y retoca las cuentas cada 64 reservas. `h` guarda el historial.
    - `EarlyStopping(monitor="val_loss", patience=6, restore_best_weights=True)`: la parada temprana: si la pérdida de validación no mejora en 6 épocas seguidas, para y deja la red de la **mejor** época.
    - `tiempos.append(…)`, `modelos_mlp.append(m)`…: apuntan en las listas lo que ha salido.
    - `print(f"semilla …")`: escribe la semilla, cuántas épocas hizo en total (`len(h.history['loss'])`, incluye las 6 últimas de «paciencia») y el mejor AUC de validación que vio.

3. **Mirar las curvas.** Ejecutad la celda de la sección 5. Dibuja tres gráficas (una por semilla) con dos líneas cada una: la pérdida de entrenamiento y la de validación, época a época. En el paso 4 aprenderéis a leerlas; de momento, comprobad que están y que cada una tiene sus dos líneas y su leyenda.
4. **Ejercicio 2: el AUC de cada semilla.** Bajad al enunciado «Ejercicio 2», borrad los `...` de su celda y escribid:

    ```python
    aucs_mlp_val = [roc_auc_score(y_val, m.predict(A_val, verbose=0).ravel()) for m in modelos_mlp]
    auc_mlp_medio = float(np.mean(aucs_mlp_val))
    ```

    Qué hace cada línea:

    - `aucs_mlp_val = […for m in modelos_mlp]`: se lee «para cada red `m` de la lista `modelos_mlp`, calcula esto, y guarda todos los resultados en una lista». Salen tres números.
    - `m.predict(A_val, verbose=0)`: pide a la red la probabilidad de cancelar de cada reserva de **validación**. `.ravel()` deja el resultado como una lista plana de números.
    - `roc_auc_score(y_val, …)`: pone nota (AUC) comparando esas probabilidades con lo que pasó de verdad (`y_val`). **Es validación: no uséis `A_pru` ni `y_pru`.**
    - `auc_mlp_medio = float(np.mean(aucs_mlp_val))`: la media de los tres AUC. **Los dos nombres** (`aucs_mlp_val` y `auc_mlp_medio`) **tienen que ser exactamente esos**: el punto de control los usa.

    Pulsad ▶ en la celda.

**Qué deberíais ver.**
- **El escalado:** la primera línea del `print` es de ceros (pueden salir como `-0.`, que es lo mismo): en entrenamiento la media es 0 porque el escalador aprendió de esas filas. La segunda son números pequeños pero no nulos, aproximadamente `[ 0.02  0.03  0.    0.02  0.01 -0.07 -0.07 -0.01 -0.03]`: validación no es 0 porque el escalador **no la ha visto**.
- **El entrenamiento:** tres líneas como `semilla 1: N épocas, AUC validación = 0.7… (máx.)`, con N como mucho 40 y AUC en torno a 0,7.
- **Las curvas:** tres gráficas con dos líneas cada una. Lo habitual es que la de entrenamiento siga bajando y la de validación baje al principio y luego se aplane o suba un poco.
- **El ejercicio 2:** `AUC de validación por semilla: [0.7… 0.7… 0.7…] · media 0.7…`. El punto de control espera una media entre 0,6 y 0,85. Estos AUC pueden no coincidir del todo con los «(máx.)» de arriba: aquellos eran el mejor de cualquier época; estos son los de la red que se queda.

**Hecho cuando:** hay un MLP entrenado con su curva de aprendizaje, el ejercicio 2 pasa su comprobación y sabéis decir en una frase qué hace una época.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'A_ent' is not defined` | No se ha ejecutado la celda de la sección 1 (o Colab se reinició). | Ejecutad desde la primera celda hacia abajo hasta la sección 1 y volved aquí. |
| `NameError: name 'modelos_mlp' is not defined` | No se ha ejecutado la celda de la sección 4. | Ejecutadla (tarda unos minutos) y después repetid el ejercicio 2. |
| `NameError: name 'keras' is not defined` | No se ejecutó la celda de importaciones. | Ejecutad la segunda celda de código y después la de la sección 4. |
| `AssertionError: Debe haber un AUC por cada uno de los 3 modelos` | La lista no tiene tres números (por ejemplo, solo se ha calculado el de una red). | Usad la forma `[… for m in modelos_mlp]`, que recorre las tres. |
| `AssertionError: El AUC medio debería rondar 0.7–0.75` | El AUC se ha calculado con datos equivocados (entrenamiento o prueba) o la red no ha aprendido. | Usad `A_val` y `y_val`, y comprobad que no habéis cambiado nada de la celda de la sección 4. |
| La celda de la sección 4 tarda mucho y no escribe nada | Es normal: entrena tres redes y no muestra progreso (`verbose=0`). | Esperad a que aparezcan las tres líneas `semilla …`. Si tarda mucho más de unos minutos, *Entorno de ejecución → Interrumpir ejecución* y volved a ejecutarla. |
| Los AUC del ejercicio 2 no coinciden con los «(máx.)» de la sección 4 | Son medidas distintas: el «máx.» es el mejor de todas las épocas; el ejercicio mide la red que se queda. | Nada: es normal que difieran en la tercera cifra decimal. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_10_paso_1.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 3 →](Reto_Sprint_10_paso_3.md)
<!--/nav-->
