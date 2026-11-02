# Paso 3 · Función de limpieza y partición train/test (día 2, 15 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md) · [Paso 4 →](Reto_Sprint_06_paso_4.md)
<!--/nav-->

1. Escribir `limpiar_reservas(df)`: una función con docstring que aplica **todos** vuestros tratamientos.
2. Comprobar el antes y el después.
3. Separar *train* y *test*.

**En sencillo.** Una función de limpieza es como un programa de lavado: metéis la ropa sucia, lo ponéis en marcha y sale limpia, **siempre igual**, y la prenda original no se estropea porque se lava una copia. Eso es `limpiar_reservas`: recibe la tabla sucia y devuelve la limpia más un pequeño resumen de lo que ha cambiado. Después se separa una parte de las reservas, el *test*, y se guarda sin mirar, como el examen que el profesor no enseña antes de tiempo. No hace falta entender cada símbolo: copiad la función, ejecutadla y comprobad con los números que sale lo que esperáis. Lo que sí tenéis que decidir es qué columnas sirven para predecir y cuáles no.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Función (`def`) y `return`** | `def` crea un trozo de código con nombre; `return` es lo que devuelve al terminar. |
| **Docstring** | El texto entre triples comillas justo debajo de `def`: explica qué hace la función. |
| **Copia (`.copy()`)** | Una tabla igual pero independiente: lo que le hagáis no afecta a `crudo`. |
| **Diccionario (`{…}`)** | Una lista de parejas «nombre: valor». Aquí sirve de tabla de equivalencias (`"españa": "ES"`) y de resumen de cambios. |
| **Regla fija** | Una regla de limpieza que no depende de los datos: «el precio va entre 20 y 1000». |
| **`X` e `y`** | `X` son las columnas con las que se predice; `y` es lo que se quiere predecir (`cancelada`). |
| ***Train* y *test*** | *Train* (entrenamiento): reservas con las que el modelo aprende. *Test*: reservas apartadas que no se miran hasta el final. |
| **`stratify=y`** | Pide que *train* y *test* tengan la misma proporción de reservas canceladas. |
| **Fuga** | Usar para predecir algo que no se sabe a la hora de predecir. |

**Cómo se hace**

1. **Escribir la función.** Celda nueva. Es la función del mini-reto de [`S06_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_02_limpieza.ipynb), ya montada y con una línea más (`mes_llegada`). Si vuestra tabla del paso 2 tiene un defecto que aquí no aparece, añadid una línea antes del `return`.

    ```python
    EQUIV_PAIS = {"es": "ES", "españa": "ES", "uk": "UK", "reino unido": "UK", "de": "DE",
                  "nl": "NL", "it": "IT", "fr": "FR", "nordicos": "Nordicos", "otros": "otros"}

    def limpiar_reservas(tabla):
        """Limpia reservas_sucio.csv con reglas fijas y devuelve (tabla_limpia, resumen).

        No modifica la tabla que recibe: trabaja sobre una copia.
        Solo aplica reglas que no dependen de los datos (no calcula medias ni medianas).
        El resumen cuenta lo que ha cambiado: filas quitadas, valores imposibles pasados a nulo, etc.
        """
        t = tabla.copy()
        resumen = {"filas_antes": len(t)}

        t = t.drop_duplicates().reset_index(drop=True)
        resumen["duplicados_quitados"] = resumen["filas_antes"] - len(t)

        t["precio_noche"] = pd.to_numeric(t["precio_noche"].astype(str).str.replace(",", "."), errors="coerce")
        iso = pd.to_datetime(t["fecha_reserva"], format="%Y-%m-%d", errors="coerce")
        espanol = pd.to_datetime(t["fecha_reserva"], format="%d/%m/%Y", errors="coerce")
        t["fecha_reserva"] = iso.fillna(espanol)
        t["fecha_llegada"] = pd.to_datetime(t["fecha_llegada"], format="%Y-%m-%d")

        t["canal"] = t["canal"].str.strip().str.lower().str.replace(" ", "_")
        t["pais_origen"] = t["pais_origen"].str.strip().str.lower().map(EQUIV_PAIS)

        nulos_antes = t[["precio_noche", "noches"]].isna().sum().sum()
        t["precio_noche"] = t["precio_noche"].where(t["precio_noche"].between(20, 1000))
        t["noches"] = t["noches"].where(t["noches"].between(1, 60))
        resumen["imposibles_a_nulo"] = int(t[["precio_noche", "noches"]].isna().sum().sum() - nulos_antes)

        antelacion_vieja = t["antelacion_dias"]
        t["antelacion_dias"] = (t["fecha_llegada"] - t["fecha_reserva"]).dt.days
        resumen["antelaciones_recalculadas"] = int((t["antelacion_dias"] != antelacion_vieja).sum())

        t["mes_llegada"] = t["fecha_llegada"].dt.month
        resumen["filas_despues"] = len(t)
        return t, resumen
    ```

    Qué hace cada línea:

    - `EQUIV_PAIS = {…}`: tabla de equivalencias «cómo viene escrito (en minúsculas) → cómo debe quedar». Un país que no esté aquí acabaría como nulo.
    - `def limpiar_reservas(tabla):` y las líneas entre triples comillas: el nombre de la función y su docstring. `tabla` es el nombre que tiene la tabla **dentro** de la función; `crudo` no se llama así allí.
    - `t = tabla.copy()`: trabaja sobre una copia. `resumen = {…}` abre el diccionario donde se apunta cada cambio.
    - `drop_duplicates().reset_index(drop=True)`: quita las filas repetidas y renumera. La resta siguiente cuenta cuántas se quitaron.
    - `precio_noche …`: cambia la coma por un punto y convierte a número. Las cuatro líneas de `iso`, `espanol` y fechas leen las dos formas de escribir la fecha (como en el paso 2).
    - `.str.strip().str.lower().str.replace(" ", "_")`: quita espacios sobrantes, pasa a minúsculas y cambia el espacio por un guion bajo: `Web Intermediaria` pasa a `web_intermediaria`.
    - `.map(EQUIV_PAIS)`: sustituye cada país por su equivalencia.
    - `.where(…between(20, 1000))`: conserva el valor si está en el rango y, si no, pone un nulo. **No se borra la fila.** Los límites (precio 20–1000 €, noches 1–60) son los de `S06_02`.
    - `antelacion_dias`: se recalcula como días entre reserva y llegada. `mes_llegada` es un número de 1 a 12 sacado de la fecha de llegada.
    - `return t, resumen`: devuelve **dos** cosas, por eso se recogen con dos nombres.

2. **Ejecutarla y leer el resumen.** Celda nueva:

    ```python
    limpia, resumen = limpiar_reservas(crudo)
    print(resumen)
    print(crudo.shape, limpia.shape)
    ```

    Qué hace cada línea:

    - `limpia, resumen = …`: guarda la tabla limpia en `limpia` y el diccionario en `resumen`. `crudo` sigue igual.
    - `print(resumen)`: filas antes y después, duplicados, valores imposibles y antelaciones corregidas.
    - `crudo.shape, limpia.shape`: la forma de cada tabla, para comprobar que `crudo` no cambió.

3. **Antes y después.** Dos celdas más. Es el apartado 3 del informe: si una corrección no se nota en estos números, no sirve.

    ```python
    antes_despues = pd.DataFrame({
        "antes": [len(crudo), crudo.duplicated().sum(), crudo["canal"].nunique(), crudo["pais_origen"].nunique()],
        "después": [len(limpia), limpia.duplicated().sum(), limpia["canal"].nunique(), limpia["pais_origen"].nunique()],
    }, index=["filas", "duplicados", "valores distintos de canal", "valores distintos de país"])
    antes_despues
    ```

    ```python
    nulos = pd.DataFrame({"antes": crudo.isna().sum(), "después": limpia[crudo.columns].isna().sum()})
    nulos[nulos.sum(axis=1) > 0]
    ```

    - `pd.DataFrame({…}, index=[…])`: crea una tabla con dos columnas (`antes`, `después`) y una fila por cosa que se cuenta.
    - `.nunique()`: cuántos valores distintos tiene una columna.
    - `limpia[crudo.columns]`: deja en `limpia` solo las 18 columnas originales (la nueva `mes_llegada` no estaba antes).
    - `nulos[nulos.sum(axis=1) > 0]`: enseña solo las columnas que tienen algún nulo antes o después.

    Y una comprobación de las fechas, por si el día y el mes se hubieran cambiado:

    ```python
    print(limpia["fecha_reserva"].min().date(), limpia["fecha_reserva"].max().date())
    ```

    - `.min()` y `.max()`: la fecha más antigua y la más reciente; `.date()` quita las horas.

4. **Elegir las columnas y separar *train* y *test*.** Para cada columna, una pregunta: «¿se conoce **al reservar**?». Quedan fuera `cancelada` (es `y`), `id_reserva` (un número de identificación no predice) y las dos fechas, que ya están resumidas en `antelacion_dias` y `mes_llegada`. Pista de cuaderno: [`S06_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_03_preprocesado_pipeline.ipynb) (partición). Celda nueva:

    ```python
    columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                    "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "mes_llegada"]
    columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
    X = limpia[columnas_num + columnas_cat]
    y = limpia["cancelada"]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
    print(X_train.shape, X_test.shape)
    print(round(y_train.mean(), 3), round(y_test.mean(), 3))
    ```

    Qué hace cada línea:

    - `columnas_num` y `columnas_cat`: las columnas de números y las de texto. Se separan porque el paso 4 las trata distinto.
    - `X = limpia[…]` e `y = limpia["cancelada"]`: elige las columnas con las que se predice y la que se quiere predecir.
    - `train_test_split(…)`: separa el 20 % para *test* (`test_size=0.2`). `random_state=SEMILLA` fija el sorteo y `stratify=y` mantiene la proporción de canceladas.
    - `y_train.mean()`: como `cancelada` es 0 o 1, la media es la proporción de canceladas.

**Qué deberíais ver.** Aproximadamente estas cifras con el CSV del curso:

- `print(resumen)`: `{'filas_antes': 1545, 'duplicados_quitados': 45, 'imposibles_a_nulo': 14, 'antelaciones_recalculadas': 5, 'filas_despues': 1500}`.
- `(1545, 18) (1500, 19)`: 1545 filas antes y 1500 después; una columna más, `mes_llegada`.
- La tabla de antes y después: filas 1545 → 1500, duplicados 45 → 0, valores distintos de `canal` 9 → 4 y de país 12 → 8.
- Los nulos pasan, por ejemplo, de 0 a 6 en `noches` (los valores imposibles) y de 115 a 112 en `pais_origen`. Los huecos no se rellenan aquí: lo hace el *pipeline* del paso 4.
- `2024-01-01 2025-12-30`: las fechas de reserva abarcan dos años. Un año fuera de ese rango sería señal de día y mes cambiados.
- `(1200, 15) (300, 15)` y `0.471 0.47`: 1200 reservas para entrenar, 300 para *test*, y casi el mismo porcentaje de canceladas en las dos.

**Hecho cuando:** `limpiar_reservas(crudo)` devuelve la tabla limpia y el resumen sin cambiar `crudo`, y *train* y *test* están separados antes de calcular nada que se aprenda de los datos.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'EQUIV_PAIS' is not defined` | La función se ejecutó sin la tabla de equivalencias. | Ejecutad las dos primeras líneas junto con la función, en la misma celda. |
| `AttributeError: 'tuple' object has no attribute 'shape'` | `limpia = limpiar_reservas(crudo)` guarda las dos cosas juntas. | Escribid `limpia, resumen = …`, con dos nombres. |
| `ValueError: not enough values to unpack (expected 3, got 2)` | Se recogen más nombres de los que devuelve la función. | La función devuelve dos cosas: dos nombres. |
| `KeyError: 'precio_noches'` | El nombre de la columna no es exacto. | Copiad el nombre de `crudo.columns`. |
| `ValueError: time data "19/11/2024" doesn't match format "%Y-%m-%d"` | Falta `errors="coerce"` en `iso` o en `espanol`. | Dejad las dos líneas como en la función. |
| Los países salen como nulos que antes tenían valor | Un país escrito de otra forma no está en `EQUIV_PAIS`. | Mirad `crudo["pais_origen"].value_counts()` y añadid la variante, en minúsculas. |
| `KeyError: "['mes_llegada'] not in index"` | `X` se ha sacado de `crudo`, que no tiene esa columna. | `X` sale de `limpia`: `X = limpia[columnas_num + columnas_cat]`. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_06_paso_2.md) · [Ficha del reto](Reto_Sprint_06.md) · [Paso 4 →](Reto_Sprint_06_paso_4.md)
<!--/nav-->
