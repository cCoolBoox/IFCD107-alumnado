# Paso 1 · Preparar el cuaderno y los datos (día 1, 10 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 2 →](Reto_Sprint_09_paso_2.md)
<!--/nav-->

1. Crear en Colab el cuaderno `reto_S09_conocer_al_huesped.ipynb`.
2. Cargar `huespedes.csv` y mirar sus columnas.
3. Escalar las variables numéricas.
4. Repartir el trabajo de los pasos 2 y 3.

**En sencillo.** Lucía, la directora comercial, manda la misma newsletter a sus 1200 huéspedes y quiere saber qué tipos de cliente tiene. Antes de buscar grupos hay que **preparar la mesa de trabajo**: abrir un cuaderno nuevo, traer los datos y dejarlos en condiciones. El paso más importante es **escalar**. Imaginad que comparáis a dos personas por su edad (en años) y por lo que gastan (en euros): como los euros son números mucho más grandes, el gasto mandaría y la edad apenas contaría. Escalar es pasar todo a una misma regla para que cada columna pese igual. No hace falta saber Python: cada línea que escribáis viene explicada y, si copiáis el código tal cual, funciona.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Cuaderno y celda** | Un cuaderno de Colab es un documento hecho de **celdas**. Las de código se ejecutan con ▶ (o `Shift + Enter`) y debajo muestran el resultado. |
| **Variable** | Un nombre que guarda algo para usarlo después. En `X = 5`, `X` guarda el 5. |
| **DataFrame** | Una tabla de datos dentro de Python, con filas y columnas. Aquí, `huespedes`: un huésped por fila. |
| **Función** | Una mini-receta con nombre. `dato("huespedes.csv")` le pide la receta `dato` el fichero de ese nombre. |
| **Escalar** (estandarizar) | Restar a cada columna su media y dividir por su desviación, para que todas tengan media 0 y la misma escala. |
| **Matriz `X`** | Una tabla solo de números, sin nombres de columna. Es lo que usan los algoritmos de agrupar. |
| **Semilla** (`SEMILLA`) | Un número fijo (aquí, 42) que hace que lo «aleatorio» salga igual cada vez. Sin ella, dos personas obtendrían resultados un poco distintos. |
| **`.shape`** | Las dimensiones de una tabla: `(1200, 7)` es 1200 filas y 7 columnas. |

**Cómo se hace**

1. **Crear el cuaderno.** Entrad en colab.research.google.com, *Archivo → Cuaderno nuevo*. Arriba a la izquierda pulsad sobre el nombre y cambiadlo por `reto_S09_conocer_al_huesped.ipynb`. Trabajad en una sola pantalla compartida o pulsad **Compartir** (arriba a la derecha) y dad permiso de **Editor** al resto. **Nunca dos personas en la misma celda a la vez.**
2. **Primera celda: la preparación.** Pulsad en la celda de código que Colab ya trae, pegad esto y pulsad ▶:

    ```python
    import os, urllib.request

    BASE_URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/"

    def dato(nombre):
        """Devuelve la ruta local de un archivo de datos del curso (lo descarga si no está)."""
        for carpeta in ("datos", "../datos", "../../datos"):
            ruta = os.path.join(carpeta, nombre)
            if os.path.exists(ruta):
                return ruta
        os.makedirs("datos", exist_ok=True)
        ruta = os.path.join("datos", nombre)
        urllib.request.urlretrieve(BASE_URL + nombre, ruta)
        return ruta
    ```

    Qué hace cada línea:

    - `import os, urllib.request`: carga dos herramientas de Python, una para trabajar con carpetas y otra para descargar de internet.
    - `BASE_URL = "…"`: guarda la dirección web donde están los datos del curso.
    - `def dato(nombre):`: crea la función `dato`. El resto de líneas (con sangría, es decir, empujadas a la derecha) son lo que hace: busca el fichero en el ordenador y, si no está, lo descarga. **Copiadla entera y sin cambiar nada.**

    No muestra nada: si no sale un error en rojo, está bien. **Esta celda se ejecuta siempre la primera**, también cuando abráis el cuaderno otro día.

3. **Segunda celda: herramientas, semilla y datos.** Pulsad **+ Código**, pegad y pulsad ▶:

    ```python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    from sklearn.decomposition import PCA

    SEMILLA = 42
    np.random.seed(SEMILLA)
    sns.set_theme(style="whitegrid")

    huespedes = pd.read_csv(dato("huespedes.csv"))
    print(huespedes.shape)
    huespedes.head()
    ```

    Qué hace cada línea:

    - Las líneas con `import` traen las herramientas que usaréis en todo el reto: `numpy` y `pandas` (números y tablas), `matplotlib` y `seaborn` (gráficos), y `scikit-learn` (los algoritmos: escalar, agrupar, silueta y PCA).
    - `SEMILLA = 42` y `np.random.seed(SEMILLA)`: fijan la semilla. **Usad siempre `SEMILLA`** cuando una función pida `random_state`.
    - `huespedes = pd.read_csv(dato("huespedes.csv"))`: lee el fichero y guarda la tabla en la variable `huespedes`.
    - `print(huespedes.shape)`: escribe las dimensiones. La última línea, `huespedes.head()`, enseña las cinco primeras filas.

4. **Mirar las columnas.** En otra celda escribid `huespedes.describe().round(1).T` y pulsad ▶. Es un resumen de cada columna (`mean` es la media, `min` y `max` los extremos). Fijaos en dos cosas: `id_huesped` es solo un número de identificación, y las otras **siete** son números de comportamiento (`viaja_con_ninos` solo vale 0 o 1). Y fijaos en las **escalas**: la edad va de 18 a 75 y el gasto diario, de 35 a 340.
5. **Escalar.** Nueva celda:

    ```python
    variables = [c for c in huespedes.columns if c != "id_huesped"]
    X = StandardScaler().fit_transform(huespedes[variables])
    print(X.shape, round(X.mean(), 3), round(X[:, 0].std(), 3))
    ```

    Qué hace cada línea:

    - `variables = [c for c in huespedes.columns if c != "id_huesped"]`: hace una lista con los nombres de todas las columnas **menos** `id_huesped` (el identificador no describe a nadie y no debe entrar). `!=` significa «distinto de».
    - `X = StandardScaler().fit_transform(huespedes[variables])`: coge esas siete columnas, las escala y guarda el resultado en `X`. **Guardad siempre en `X`**: los pasos 2 y 3 lo usan.
    - `print(…)`: escribe las dimensiones de `X`, su media global y la desviación de su primera columna, para comprobar que se escaló bien.

6. **Repartir el trabajo de los pasos 2 y 3.** Antes de seguir, apuntad en el tablero quién hace qué. Un reparto posible:

    | Persona | Tarea | Paso |
    |---|---|---|
    | A | Probar k-means con `k` de 2 a 8, silueta y elegir `k` | 2 |
    | B | Mapa PCA y perfil de cada segmento | 3 |
    | C | Nombres y acciones comerciales (con A y B) | 3 |

    Si sois más de tres, la persona que quede libre empieza a leer el paso 4. Un cuaderno compartido solo funciona si cada persona escribe en **sus** celdas.

**Qué deberíais ver.** Tras la segunda celda, `(1200, 8)` y una tabla de cinco filas que empieza por `id_huesped` 1 (con 26 años), 2 (41), 3 (60)… Tras `describe()`, una tabla con una fila por columna (la media de la edad es 41,2 y la del gasto diario, 124,2). Y tras el escalado, `(1200, 7) 0.0 1.0`: una matriz `X` de 1200 filas y 7 columnas con la media cerca de 0.

**Hecho cuando:** `X` existe y está escalada, y cada persona sabe qué parte del paso 2 o del 3 le toca.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'dato' is not defined` (o `'pd'`, `'X'`) | No se ha ejecutado la celda donde se define, o Colab se reinició y olvidó todo. | *Entorno de ejecución → Ejecutar todo*, o pulsad ▶ en las celdas de arriba, **en orden**. |
| `HTTPError: HTTP Error 404: Not Found` | El nombre del fichero está mal escrito. | Es exactamente `"huespedes.csv"`: en minúsculas y con la `p` y la `u`. |
| `SyntaxError: invalid character '“' (U+201C)` | Hay comillas «rizadas», típicas al copiar de un documento. | Usad comillas rectas `"` y volved a escribirlas. |
| `SyntaxError: '(' was never closed` | Falta un paréntesis `)` al final de la línea. | Contad los paréntesis: cada `(` tiene su `)`. |
| `KeyError: "None of [Index(['edades'], dtype='object')] are in the [columns]"` | El nombre de una columna está mal escrito. | Copiadlo tal cual de `huespedes.columns` (por ejemplo, `edad` sin la `es`). |
| `X.shape` sale `(1200, 8)` | `id_huesped` se ha colado en `X`. | Escalad `huespedes[variables]`, que ya no lo lleva. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_09.md) · [Paso 2 →](Reto_Sprint_09_paso_2.md)
<!--/nav-->
