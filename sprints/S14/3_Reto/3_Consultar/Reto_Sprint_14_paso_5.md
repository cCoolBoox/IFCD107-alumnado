# Paso 5 · Go / no-go, EDA, calidad del dato y baseline (día 2, 200 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 5 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 6 →](Reto_Sprint_14_paso_6.md)
<!--/nav-->

1. Leer el *go / no-go* del docente y corregir la ficha si hace falta.
2. Hacer el EDA y el informe de calidad del dato en `01_eda.ipynb`.
3. Fijar la partición de los datos y la métrica técnica **antes** de mirar resultados.
4. Construir el baseline en `02_baseline.ipynb` y calcular su métrica.

**En sencillo.** Hoy se mira de verdad por primera vez a los datos. Es como revisar la despensa antes de cocinar: ¿qué hay?, ¿qué falta?, ¿qué está estropeado? Eso es el **EDA** (análisis exploratorio) y su resultado es un **informe de calidad** con lo que habéis encontrado y qué hacéis con ello. Después decidís **cómo vais a repartir los datos y con qué número vais a medir**, antes de ver ningún resultado, para no engañaros. Por último, construís el **baseline**: el modelo más tonto posible, que sirve de suelo para medir las mejoras. No hace falta saber Python: copiáis el código, cambiáis las líneas que se indican y ejecutáis. Lo importante es **escribir con vuestras palabras qué significan los números**.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **EDA** | Análisis exploratorio: mirar los datos (cuántos hay, qué falta, qué es raro) antes de modelar. |
| **DataFrame (`df`)** | Una tabla de datos dentro de Python. Cada fila es un caso; cada columna, una variable. |
| **Nulo** | Una casilla vacía (el dato no se registró). |
| **Valor raro** (*outlier*) | Un valor muy lejos del resto. Puede ser un error o algo real pero inusual. |
| **Sesgo de muestreo** | Que los datos no representen a todos: por ejemplo, que solo haya hoteles grandes. |
| **Fuga de datos** | Usar como pista una variable que no se conocería en el momento de decidir. |
| **Partición** | Repartir los datos en tres montones: entrenamiento (el modelo aprende), validación (se prueba y se ajusta) y test (se guarda hasta el final). |
| **Estratificar** | Repartir manteniendo en cada montón la misma proporción de cada clase. |
| **Semilla** | Un número fijo (aquí 42) que hace que el azar dé lo mismo cada vez. |
| **Baseline** | El modelo más simple posible, que habrá que superar. |

**Cómo se hace**

1. **Leer el *go / no-go* (20 minutos).** El docente responde con una de tres cosas: **GO** (adelante), **GO con cambios** o **NO-GO** (hay que cambiar el enfoque). Un *no-go* o un cambio es **normal**. Si pide cambios: abrid `ficha_proyecto.md` en GitHub, pulsad el icono del lápiz, corregid, cambiad `Versión: 1` por `Versión: 2` y pulsad **Commit changes** con otro mensaje («Ficha v2: ajusto el alcance»). Si el docente cambia el alcance, apuntadlo en la ficha.

2. **Crear `01_eda.ipynb` y cargar los datos (15 minutos).** En Colab: *Archivo → Cuaderno nuevo*, y pulsad el nombre de arriba para llamarlo `01_eda.ipynb`. Subid vuestro archivo de datos con el panel 📁 de la izquierda (o usad la URL de descarga del plan de datos). En la primera celda:

    ```python
    import pandas as pd

    RUTA = "mis_datos.csv"
    SEMILLA = 42

    df = pd.read_csv(RUTA)
    print(df.shape)
    df.info()
    ```

    Qué hace cada línea:

    - `RUTA` es el nombre del archivo: **cambiadlo** por el vuestro (o por la URL entre comillas). `SEMILLA = 42` se usará para repartir los datos.
    - `pd.read_csv(RUTA)` lee la tabla y la guarda en `df`. `df.shape` da (filas, columnas) y `df.info()` lista las columnas, cuántas casillas tienen datos y su tipo.

    Con el conjunto de práctica `reservas_turisdata.csv` (sintético) sale `(6000, 18)`, y `pais_origen` tiene 5862 datos de 6000. Con los vuestros saldrán otras cifras: apuntad **filas, columnas, periodo y tipos** (resumen de tres líneas).

3. **Nulos y duplicados (20 minutos).** En una celda nueva:

    ```python
    def resumen_calidad(tabla):
        return pd.DataFrame({
            "tipo": tabla.dtypes.astype(str),
            "nulos": tabla.isna().sum(),
            "pct_nulos": (tabla.isna().mean() * 100).round(2),
            "distintos": tabla.nunique(),
        })

    resumen_calidad(df)
    ```

    La función (la misma del cuaderno `S06_01`) crea una tabla con una fila por columna: su tipo, cuántos nulos tiene, qué porcentaje es y cuántos valores distintos hay. **No cambiéis los nombres.** En otra celda:

    ```python
    print("Filas duplicadas:", df.duplicated().sum())
    df.describe().round(2)
    ```

    `df.duplicated().sum()` cuenta las filas repetidas exactas y `df.describe()` da, de cada columna numérica, la media, el mínimo y el máximo. Con `reservas_turisdata.csv` sale `pais_origen` con 138 nulos (2,3 %), `Filas duplicadas: 0`, `antelacion_dias` con media 89,89 y máximo 400, y `precio_noche` con media 102,87. Apuntad **cuántos hay y qué haréis** (dejarlos, quitarlos, rellenarlos), con el motivo.

4. **Valores raros (10 minutos).** Con la regla del rango intercuartílico (IQR, explicada en `S06_02`), sospechoso es lo que queda fuera de `[Q1 − 1,5·IQR, Q3 + 1,5·IQR]`:

    ```python
    COLUMNA = "precio_noche"
    q1, q3 = df[COLUMNA].quantile([0.25, 0.75])
    iqr = q3 - q1
    limite_bajo = q1 - 1.5 * iqr
    limite_alto = q3 + 1.5 * iqr
    raros = df[(df[COLUMNA] < limite_bajo) | (df[COLUMNA] > limite_alto)]
    print(len(raros), "valores raros en", COLUMNA, "· límites", round(limite_bajo, 1), round(limite_alto, 1))
    ```

    - **Cambiad `COLUMNA`** por una columna numérica vuestra (con el nombre exacto, entre comillas).
    - `quantile([0.25, 0.75])` da el valor por debajo del cual está el 25 % y el 75 % de los casos; `iqr` es la distancia entre ambos.
    - `raros` guarda las filas fuera de los límites y `|` significa «o».

    Con `precio_noche` sale `271 valores raros en precio_noche · límites 16.1 180.4`. Un valor raro no se borra sin motivo: escribid **qué son** (error o caso real) y **si los quitáis o los dejáis, y por qué**.

5. **Sesgo de muestreo y desequilibrio (10 minutos).** ¿Quién o qué falta? ¿Hay clases poco frecuentes?

    ```python
    print(df["pais_origen"].value_counts(normalize=True).round(3))
    print(df["cancelada"].value_counts(normalize=True).round(3))
    ```

    `value_counts(normalize=True)` da la proporción de cada valor. **Cambiad** `"pais_origen"` y `"cancelada"` por vuestra columna de grupos y por la que queréis predecir. Con `reservas_turisdata.csv`: ES 0,274, UK 0,255, DE 0,148…; y `cancelada` 0 con 0,541 y 1 con 0,459. Escribid **una frase** de sesgo («solo hay hoteles grandes») y otra del desequilibrio. En el brief 2, contad las imágenes por clase (si vuestras imágenes están en una carpeta por clase):

    ```python
    import os

    CARPETA = "imagenes"
    cuentas = {clase: len(os.listdir(os.path.join(CARPETA, clase))) for clase in os.listdir(CARPETA)}
    print(cuentas)
    ```

    En el brief 3, contad los documentos y su longitud con `len(texto.split())` (cuenta las palabras de un texto).

6. **Tres gráficos que respondan a vuestra pregunta (20 minutos).** Cada gráfico lleva título con la conclusión, ejes con nombre y una frase de lectura debajo:

    ```python
    import matplotlib.pyplot as plt

    df["precio_noche"].hist(bins=30)
    plt.title("Precio por noche de las reservas")
    plt.xlabel("Precio por noche (€)")
    plt.ylabel("Número de reservas")
    plt.show()

    df.groupby("deposito")["cancelada"].mean().plot(kind="bar")
    plt.title("Las reservas sin depósito se cancelan más")
    plt.xlabel("Tipo de depósito")
    plt.ylabel("Proporción de reservas canceladas")
    plt.show()
    ```

    `hist(bins=30)` dibuja el histograma en 30 barras; `groupby("deposito")["cancelada"].mean()` calcula la media de `cancelada` para cada tipo de depósito; `plt.show()` muestra el dibujo. Con los datos de práctica salen las medias `parcial` 0,409, `sin_deposito` 0,540 y `total` 0,264. Para una serie temporal, el primer gráfico es la propia serie:

    ```python
    ocup = pd.read_csv(RUTA, parse_dates=["fecha"]).set_index("fecha").sort_index()
    ocup["ocupacion_pct"].plot(figsize=(10, 3), title="Ocupación diaria")
    plt.show()
    ```

7. **Fugas posibles (5 minutos, sin código).** Recorred la lista de columnas y preguntad de cada una: «¿la conoceríamos **en el momento de decidir**?». Una columna como `reembolso_emitido` solo existe **después** de cancelar: es fuga y se descarta. Escribid cuáles hay y si las descartáis.

8. **El informe de calidad (10 minutos).** Abrid `plan_datos_licencias.md` (con el icono del lápiz para editar). En el apartado 3, una fila por aspecto (nulos, duplicados, valores imposibles o raros, formatos y tipos, **sesgo de muestreo**, desequilibrio, **fuga potencial**), con el hallazgo y la acción tomada. Ejemplo (con los datos de práctica; las vuestras serán otras cifras): «Nulos: `pais_origen` 138 (2,3 %) → se dejan como una categoría más». En el apartado 4 (**linaje**) copiad la cadena «fuente → descarga → limpieza → partición → modelo» con los datos reales de cada paso. Elegid **un hallazgo que cambie el enfoque** para contarlo en la *review*.

9. **Fijar la partición y la métrica (20 minutos), antes de ejecutar nada.** Escribidlas en el apartado 5 de `plan_datos_licencias.md` y en el apartado 5 de la ficha: (a) **cómo partís**: si hay series, **por fechas** (entrenar con el pasado, evaluar con el futuro); si no, aleatoria y estratificada; y por qué eso evita fugas; (b) **tamaño** de entrenamiento, validación y test (**el test no se toca hasta que tengáis un candidato**); (c) la **métrica técnica** (MAE, MAPE, F1 o aciertos sobre 40 preguntas) y el umbral de éxito. Los tamaños los da el código siguiente: apuntadlos después.

10. **Crear `02_baseline.ipynb` y repartir los datos (25 minutos).** Cuaderno nuevo, con la misma primera celda de carga que el EDA. Para datos de tabla, con una columna a predecir:

    ```python
    from sklearn.model_selection import train_test_split

    OBJETIVO = "cancelada"
    X = df.drop(columns=[OBJETIVO])
    y = df[OBJETIVO]

    X_resto, X_test, y_resto, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEMILLA)
    X_ent, X_val, y_ent, y_val = train_test_split(X_resto, y_resto, test_size=0.2, stratify=y_resto, random_state=SEMILLA)
    print(len(X_ent), len(X_val), len(X_test))
    ```

    - **Cambiad `OBJETIVO`** por la columna que queréis predecir. `X` son las pistas y `y` la respuesta.
    - La primera partición aparta el 20 % para el **test**; la segunda parte el resto en entrenamiento (`_ent`) y validación (`_val`). `stratify=y` mantiene las proporciones; `random_state=SEMILLA` hace que sea siempre el mismo reparto.

    Con los datos de práctica salen `3840 960 1200`. Si vuestros datos son una **serie temporal**, no se reparte al azar sino por fechas (los últimos 91 días son 13 semanas; elegid vosotros cuántos):

    ```python
    ocup = pd.read_csv(RUTA, parse_dates=["fecha"]).set_index("fecha").sort_index()
    serie = ocup["ocupacion_pct"]

    DIAS = 91
    entrenamiento = serie.iloc[:-2 * DIAS]
    validacion = serie.iloc[-2 * DIAS:-DIAS]
    test = serie.iloc[-DIAS:]
    print(len(entrenamiento), len(validacion), len(test))
    ```

    Con `ocupacion_diaria.csv` salen `914 91 91`. `iloc` corta por posición: `[:-2 * DIAS]` es todo menos los últimos 182 días, `[-2 * DIAS:-DIAS]` los 91 anteriores a los últimos y `[-DIAS:]` los últimos 91.

11. **Construir el baseline y su métrica (35 minutos).** El modelo más simple posible. Para la tabla, «decir siempre la clase más frecuente»:

    ```python
    from sklearn.dummy import DummyClassifier
    from sklearn.metrics import f1_score

    baseline = DummyClassifier(strategy="most_frequent").fit(X_ent, y_ent)
    pred = baseline.predict(X_val)
    print("exactitud", round(baseline.score(X_val, y_val), 3), "F1", round(f1_score(y_val, pred), 3))
    ```

    `.fit(...)` hace que el modelo «aprenda» (aquí solo cuenta cuál es la clase más frecuente) y `.predict(...)` lo aplica a la validación. Con los datos de práctica sale `exactitud 0.541 F1 0.0`: acierta algo más de la mitad solo por ser la clase mayoritaria, y el F1 de 0 recuerda que **nunca predice la cancelación**. Para la serie, «igual que la semana pasada»:

    ```python
    from sklearn.metrics import mean_absolute_error

    prediccion = serie.shift(7)
    mae = mean_absolute_error(validacion, prediccion.loc[validacion.index])
    print("MAE del baseline en validación:", round(mae, 2))
    ```

    `serie.shift(7)` desplaza la serie 7 días, de modo que cada día queda con el valor del mismo día de la semana anterior; el MAE es el error medio en puntos. Sale `MAE del baseline en validación: 5.02`. Brief 2: acierto de predecir siempre la clase más numerosa (`max(cuentas.values()) / sum(cuentas.values())`, con `cuentas` del punto 5). Brief 3: búsqueda por palabras clave sobre vuestras preguntas de referencia (`pregunta`, `respuesta_esperada`, como en `preguntas_referencia.csv`), como en el cuaderno [S12_06](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/S12_06_mini_rag.ipynb). Escribid la frase: **«Nuestro baseline tiene [métrica] de [valor]»**. Es el suelo que superaréis en los sprints siguientes: **no lo compliquéis**.

12. **Reiniciar, descargar y subir (10 minutos).** En cada cuaderno: *Entorno de ejecución → Reiniciar y ejecutar todo*, después *Archivo → Descargar → Descargar .ipynb* y subid el fichero a `sprint-14/` ([guía](../../../../material/5.%20Como_entregar_en_GitHub.md)): cada cuaderno, una persona distinta.

**Qué deberíais ver.** La ficha con el *go* (o corregida); un `01_eda.ipynb` que termina con la tabla de calidad, y la partición y la métrica escritas en el plan de datos antes de ejecutar el baseline. Un `02_baseline.ipynb` que termina con un número y la frase «Nuestro baseline tiene…». Con los datos de práctica: `3840 960 1200` y `exactitud 0.541 F1 0.0` (tabla) o `914 91 91` y `MAE 5.02` (serie).

**Hecho cuando:** los dos cuadernos se ejecutan de arriba abajo sin errores, la métrica y la partición están escritas antes del baseline y los cuadernos están en `sprint-14/`.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'df' is not defined` | La celda de carga no se ha ejecutado, o Colab se reinició. | Ejecutad desde la primera celda hacia abajo (*Entorno de ejecución → Ejecutar todo*). |
| `FileNotFoundError: [Errno 2] No such file or directory: 'mis_datos.csv'` | El archivo no está subido en esta sesión de Colab, o el nombre no coincide. | Subidlo otra vez con el panel 📁 y copiad el nombre exacto en `RUTA`. Cada vez que Colab se reinicia, los archivos subidos se pierden. |
| `KeyError: 'cancelado'` (con vuestro nombre) | El nombre de la columna no es exacto. | Escribid `df.columns` para ver los nombres y copiadlo tal cual. |
| `ValueError: The least populated classes in y have only 1 member, which is too few` | Una clase tiene una sola fila y `stratify` no puede repartirla. | Quitad `stratify=y` o agrupad esa clase con otra. Apuntadlo en el informe de calidad. |
| El baseline da un `F1` de `0.0` | Es normal si el modelo predice siempre la clase mayoritaria. | No es un error: es justo lo que mide el baseline. Si Colab muestra un aviso naranja (*warning*) sobre «ill-defined», tampoco es un error. Citad también la exactitud y explicad que el F1 de 0 viene de que nunca predice la clase pequeña. |
| `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1…` | El archivo tiene otra codificación. | `pd.read_csv(RUTA, encoding="latin-1")`; si sale una sola columna con `;`, añadid `sep=";"`. |
| Al *Reiniciar y ejecutar todo* una celda falla | Algo depende de una celda que está debajo, o de un archivo que no se ha vuelto a subir. | Leed el primer error en rojo, corregid esa celda y repetid hasta que todo corra. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_14_paso_4.md) · [Ficha del reto](Reto_Sprint_14.md) · [Paso 6 →](Reto_Sprint_14_paso_6.md)
<!--/nav-->
