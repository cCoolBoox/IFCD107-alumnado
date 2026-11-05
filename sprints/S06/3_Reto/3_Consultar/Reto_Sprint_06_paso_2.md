# Paso 2 · Inventario de defectos (día 1, 30 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md) · [Paso 3 →](Reto_Sprint_06_paso_3.md)
<!--/nav-->

1. Abrir un cuaderno nuevo en Colab (`reto_S06`), cargar `reservas_sucio.csv` y pasar `resumen_calidad`.
2. Buscar defectos con tablas y gráficos, categoría por categoría.
3. Rellenar **una fila de la tabla del informe por cada defecto** (mínimo 6).
4. Apuntar las preguntas que haríais al cliente.

**En sencillo.** Es como revisar un coche usado antes de comprarlo: no se arregla nada todavía, solo se mira con una lista y se anota cada fallo (qué es, dónde está, cuántos hay y cómo lo habéis visto). El «coche» es `reservas_sucio.csv`, un fichero de reservas que el cliente exportó a mano desde varios sistemas. Vais a escribir unas pocas celdas de código que **cuentan y muestran** cosas, y con lo que salga rellenaréis una tabla. Nada de lo que escribáis cambia el fichero: solo lo leéis. No hace falta saber programar: copiáis las celdas tal cual y cambiáis, como mucho, el nombre de una columna. Lo difícil no es el código, es **fijarse** en lo que sale.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Defecto de calidad** | Algo del fichero que no cuadra con la realidad: un hueco, una repetición, un formato mezclado, un valor imposible. |
| **`crudo`** | El nombre de la tabla tal y como llega del cliente. No se modifica nunca: sirve para comparar al final. |
| **Función (`def`)** | Un trozo de código con nombre que se escribe una vez y se usa muchas. Aquí, `dato` y `resumen_calidad`. |
| **Nulo (`NaN`)** | Una casilla vacía, sin dato. |
| **Tipo de dato** | Cómo guarda pandas una columna: `int64` (entero), `float64` (decimal), `object` o `str` (texto; según la versión de pandas sale una u otra). Un precio en texto es sospechoso. |
| **Duplicado** | Una fila idéntica a otra en todas sus columnas. |
| **Categoría inconsistente** | Lo mismo escrito de varias formas: `directo`, `Directo` y `DIRECTO` son para el ordenador tres cosas distintas. |
| **Valor imposible** | Un dato que no puede ser verdad (un precio negativo). Un *outlier* es un valor extremo pero **posible**: ante la duda, es una pregunta para el cliente. |
| **`errors="coerce"`** | «Si no sabes convertir esto, ponlo como nulo en vez de dar error». Sirve para probar un formato de fecha sin que el cuaderno se pare. |

**Cómo se hace**

1. **Abrir el cuaderno.** En Colab, *Archivo → Nuevo cuaderno* y renombradlo `reto_S06`. Con *Compartir* (arriba a la derecha) dad acceso de editor al resto del equipo. Una persona escribe y el resto mira y propone; cambiad de turno cada pocos minutos. Cada bloque de código de abajo va en **una celda nueva** (*+ Código*), y se ejecuta con el botón ▶ o con Mayús + Intro. Ejecutad **de arriba abajo**: cada celda usa nombres que crean las anteriores.

2. **Preparar y cargar el CSV.** Primera celda:

    ```python
    import os, urllib.request
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

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

    SEMILLA = 42
    sns.set_theme(style="whitegrid")
    pd.set_option("display.max_columns", 30)

    crudo = pd.read_csv(dato("reservas_sucio.csv"))
    print(crudo.shape)
    ```

    Qué hace cada línea:

    - `import … as pd`: trae las herramientas (pandas para tablas, matplotlib y seaborn para gráficos). Los nombres cortos `pd`, `plt`, `sns` y `np` son los de siempre: no los cambiéis.
    - `def dato(nombre):`: define la función `dato`. Busca el fichero en tres carpetas y, si no está, lo descarga de GitHub a la carpeta `datos`. Es la misma que usan los cuadernos `S06_01` y `S06_02`.
    - `SEMILLA = 42`: el número que fija el azar para que todo salga igual en cada ejecución.
    - `pd.set_option(…)`: pide que las tablas anchas muestren hasta 30 columnas.
    - `crudo = pd.read_csv(dato("reservas_sucio.csv"))`: lee el fichero y lo guarda en `crudo`. **Esta tabla no se modifica nunca.**
    - `print(crudo.shape)`: imprime (filas, columnas).

3. **Mirar el estado de cada columna.** Celda nueva:

    ```python
    def resumen_calidad(tabla):
        return pd.DataFrame({
            "tipo": tabla.dtypes.astype(str),
            "nulos": tabla.isna().sum(),
            "pct_nulos": (tabla.isna().mean() * 100).round(2),
            "distintos": tabla.nunique(),
        })

    resumen_calidad(crudo)
    ```

    Qué hace cada línea:

    - `def resumen_calidad(tabla):`: una función que recibe una tabla y devuelve otra con una fila por columna.
    - `"tipo"`, `"nulos"`, `"pct_nulos"`, `"distintos"`: el tipo de dato, cuántas casillas vacías, el porcentaje de vacías y cuántos valores diferentes hay.
    - `resumen_calidad(crudo)`: al ser la **última línea** de la celda, Colab muestra su resultado.

    Después, en otra celda, `crudo.describe().round(1)` da mínimo, máximo y media de las columnas numéricas.

4. **Duplicados, tipos y fechas.** Celda nueva:

    ```python
    print("Filas duplicadas exactas:", crudo.duplicated().sum())
    print("Precios escritos con coma:", crudo["precio_noche"].astype(str).str.contains(",").sum())
    iso = pd.to_datetime(crudo["fecha_reserva"], format="%Y-%m-%d", errors="coerce")
    espanol = pd.to_datetime(crudo["fecha_reserva"], format="%d/%m/%Y", errors="coerce")
    print("Fechas ISO:", iso.notna().sum(), "· dd/mm/aaaa:", espanol.notna().sum(), "· sin leer:", (iso.isna() & espanol.isna()).sum())
    crudo[["fecha_reserva", "precio_noche"]].head(8)
    ```

    Qué hace cada línea:

    - `crudo.duplicated().sum()`: marca con «verdadero» cada fila repetida y suma cuántas hay.
    - `.astype(str).str.contains(",")`: convierte la columna a texto y marca los precios que llevan una coma (por ejemplo `83,36`).
    - `iso = …` y `espanol = …`: intentan leer la fecha en dos formatos. `%Y-%m-%d` es `2025-11-09` y `%d/%m/%Y` es `19/11/2024`. Donde no encaja, `errors="coerce"` deja un nulo.
    - `iso.notna().sum()`: cuenta las fechas que se han leído con ese formato; `(iso.isna() & espanol.isna()).sum()` cuenta las que no se leen con ninguno.
    - `.head(8)`: enseña las 8 primeras filas de esas dos columnas para verlas con vuestros ojos.

5. **Categorías inconsistentes.** Celda nueva. Cambiad el nombre de la columna para revisar las demás de texto (`tipo_habitacion`, `regimen`, `tarifa`, `deposito`):

    ```python
    print(crudo["canal"].value_counts().to_string())
    print()
    print(crudo["pais_origen"].value_counts().to_string())
    ```

    Qué hace cada línea:

    - `crudo["canal"]`: elige la columna `canal` (el nombre va entre comillas y debe ser exacto).
    - `.value_counts()`: cuenta cuántas veces aparece cada valor distinto.
    - `.to_string()`: lo escribe completo, sin recortar filas.
    - `print()` solo deja una línea en blanco entre las dos listas.

6. **Valores imposibles y *outliers*.** Celda nueva:

    ```python
    precio = pd.to_numeric(crudo["precio_noche"].astype(str).str.replace(",", "."), errors="coerce")
    print(precio.describe().round(1))
    print("Precios <= 0:", (precio <= 0).sum(), "· precios > 1000:", (precio > 1000).sum())
    print("Noches <= 0:", (crudo["noches"] <= 0).sum())
    print("Antelaciones negativas:", (crudo["antelacion_dias"] < 0).sum())
    ```

    Qué hace cada línea:

    - `precio = …`: copia la columna de precios cambiando la coma por un punto y la convierte en número. Es una copia aparte: `crudo` no cambia.
    - `precio.describe()`: mínimo, máximo, media… del precio.
    - `(precio <= 0).sum()`: cuenta los precios que cumplen la condición. Cambiad el `0` o el `1000` si queréis probar otros límites.
    - `noches` y `antelacion_dias`: el mismo truco con otras dos columnas que no pueden ser negativas.

    Para ver los *outliers*, un diagrama de caja con los precios razonables (la caja es donde está la mayoría; los puntos sueltos son los extremos):

    ```python
    precio_ok = precio[precio.between(1, 1000)]
    fig, ejes = plt.subplots(1, 2, figsize=(11, 3.5))
    sns.boxplot(x=precio_ok, ax=ejes[0], color="#8ecae6")
    ejes[0].set(title="Precio de todas las reservas", xlabel="Precio por noche (€)")
    sns.boxplot(x=precio_ok, y=crudo.loc[precio_ok.index, "tipo_habitacion"], ax=ejes[1], color="#8ecae6")
    ejes[1].set(title="Precio por tipo de habitación", xlabel="Precio por noche (€)", ylabel="Tipo de habitación")
    plt.tight_layout()
    plt.show()
    ```

    - `precio.between(1, 1000)`: se queda con los precios entre 1 y 1000 para que los 9999 no aplasten el dibujo.
    - `plt.subplots(1, 2, …)`: prepara dos gráficos lado a lado; `sns.boxplot(…, ax=ejes[0])` dibuja uno en cada hueco.
    - `.set(title=…, xlabel=…)`: pone título y nombres a los ejes. `plt.show()` dibuja el resultado.

7. **Nulos e incoherencias entre columnas.** Celda nueva:

    ```python
    nulos = crudo.isna().sum()
    print(nulos[nulos > 0])
    fecha_reserva = iso.fillna(espanol)
    fecha_llegada = pd.to_datetime(crudo["fecha_llegada"], format="%Y-%m-%d")
    antelacion_calculada = (fecha_llegada - fecha_reserva).dt.days
    print("Antelaciones que no cuadran con las fechas:", (antelacion_calculada != crudo["antelacion_dias"]).sum())
    ```

    Qué hace cada línea:

    - `nulos[nulos > 0]`: de todas las columnas, deja solo las que tienen algún hueco. **Mirad todas**, también las de texto como `regimen`.
    - `iso.fillna(espanol)`: rellena las fechas que `iso` no pudo leer con las que sí leyó `espanol`; así hay una fecha de reserva para cada fila.
    - `(fecha_llegada - fecha_reserva).dt.days`: los días entre reservar y llegar, calculados por vosotros.
    - `!= crudo["antelacion_dias"]`: compara con lo que dice el fichero y cuenta las filas donde no coincide.

8. **Rellenar la tabla de defectos.** Una persona crea en el repositorio del equipo, dentro de `sprint-06/`, el archivo `informe_calidad.md`: abre [`informe_calidad_plantilla.md`](../1_Trabajar/plantillas/informe_calidad_plantilla.md), pulsa *Raw*, copia todo el texto, y en GitHub usa *Add file → Create new file*. Por **cada defecto**, una fila de la tabla del apartado 2, con ocho columnas. Un ejemplo con los números reales de este fichero:

    | Columna de la plantilla | Qué se escribe |
    |---|---|
    | Nº | 1 |
    | Defecto | Precios escritos con coma decimal (`83,36`) |
    | Columna(s) | `precio_noche` |
    | Filas afectadas | 153 de 1545 |
    | Cómo lo detectamos | `resumen_calidad` dice `object` o `str` (texto) en una columna de precios; `.str.contains(",")` los cuenta |
    | Causa probable | Exportación desde un Excel en español |
    | Tratamiento aplicado | Cambiar la coma por un punto y convertir a número |
    | Por qué (y riesgo) | No se pierde información; un texto raro pasaría a nulo sin avisar, por eso se cuentan |

    Hacen falta **6 filas o más**. Revisad las ocho familias de la plantilla (duplicados, tipos incorrectos, formatos de fecha, categorías inconsistentes, valores imposibles, *outliers*, nulos e incoherencias entre columnas) y marcad los tres defectos más graves. Si no llegáis a seis, mirad la «Ayuda 3» de la [ficha del reto](Reto_Sprint_06.md).

9. **Preguntas al cliente.** Lo que no podéis decidir solos va al apartado 5 del informe, con lo que haréis mientras tanto. Ejemplos de la plantilla: «¿por qué hay precios con coma?», «¿el 0 en precio significa "gratis" o "sin dato"?», «¿qué hace el sistema con el país cuando reserva una agencia?». Apuntad al menos una. Para repasar las técnicas, los cuadernos [`S06_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/para_casa/S06_01_pandas_eda.ipynb) y [`S06_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/para_casa/S06_02_limpieza.ipynb) hacen lo mismo con más explicación.

**Qué deberíais ver.** Con este CSV, estas salidas (los recuentos son los del fichero del curso):

- `(1545, 18)`: 1545 filas y 18 columnas.
- `resumen_calidad`: nulos en **cuatro columnas** (`adultos` 46, `regimen` 61, `pais_origen` 115 y `precio_noche` 84), y texto (`object` o `str`) en `fecha_reserva`, `fecha_llegada` y `precio_noche`. `id_reserva` tiene 1500 valores distintos en 1545 filas.
- `Filas duplicadas exactas: 45` y `Precios escritos con coma: 153`.
- `Fechas ISO: 1391 · dd/mm/aaaa: 154 · sin leer: 0`: dos formatos de fecha, y entre los dos se leen todas.
- `canal` con 9 valores (`web_intermediaria` 718, pero también `WEB_INTERMEDIARIA` 34, `Web Intermediaria` 33, `web intermediaria` 28, `Directo` 24, `directo` 16…) y `pais_origen` con 12 (`ES` 351 y también `España` 26 y `es` 23; `UK` 316 y también `Reino Unido` 22 y `uk` 23).
- Precios: mínimo `-50.0` y máximo `9999.0`, con `Precios <= 0: 4` y `precios > 1000: 4`; `Noches <= 0: 6`; `Antelaciones negativas: 5`.
- `Antelaciones que no cuadran con las fechas: 5`: cinco filas con `antelacion_dias` igual a `-3`.
- Un diagrama de caja con muchos puntos sueltos a la derecha. Un precio alto no es por sí solo un error: decidid si es imposible o solo raro.

Y en el informe, una tabla con **6 filas o más**. La plantilla da una columna para cada cosa: número, defecto, columna(s), filas afectadas, cómo lo detectasteis, causa probable, tratamiento aplicado y por qué (y riesgo).

**Hecho cuando:** la tabla tiene 6 o más defectos con sus datos completos y hay al menos una pregunta para el cliente.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'crudo' is not defined` | La celda de carga no se ha ejecutado (o Colab se reinició). | Ejecutad desde arriba: la celda del paso 2 primero. |
| `NameError: name 'iso' is not defined` | La celda de fechas (paso 4) no se ejecutó antes de la de incoherencias (paso 7). | Ejecutad la del paso 4 y luego la del 7. |
| `KeyError: 'precio_noches'` | El nombre de la columna no es exacto. | Escribid `crudo.columns` y copiad el nombre tal cual, con sus guiones bajos. |
| `HTTPError: HTTP Error 404: Not Found` al cargar | La dirección de `BASE_URL` o el nombre del CSV tienen una errata. | Copiad de nuevo la celda 2 y comprobad `reservas_sucio.csv`, todo en minúsculas. |
| `ValueError: time data "19/11/2024" doesn't match format "%Y-%m-%d"` | Se ha quitado `errors="coerce"` o se ha usado un solo formato para toda la columna. | Dejad las dos líneas `iso` y `espanol` con `errors="coerce"`: así cada una lee solo lo suyo. |
| Una celda se ejecuta pero no muestra nada | Colab enseña solo la **última** expresión; un resultado en medio de la celda no se ve. | Envolvedlo en `print(…)` o ponedlo como última línea. |
| La tabla del informe se ve rota en la vista previa de GitHub | Falta una `\|` en una fila o hay un salto de línea dentro de una celda. | Cada fila, en una sola línea y con el mismo número de `\|` que la cabecera. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_06_paso_1.md) · [Ficha del reto](Reto_Sprint_06.md) · [Paso 3 →](Reto_Sprint_06_paso_3.md)
<!--/nav-->
