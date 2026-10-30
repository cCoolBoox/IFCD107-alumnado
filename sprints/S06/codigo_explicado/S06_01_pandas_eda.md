# Código explicado · S06.01 · Conocer los datos: pandas y exploración (EDA)

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_01_pandas_eda.ipynb) · [descargar](../notebooks/S06_01_pandas_eda.ipynb) · ⏱ en clase: 45 min · 🏫 11 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`, `set_theme`, `set_option`. |
| 2 | 2. Cargar e inspeccionar | Practica `dato`, `read_csv`, `head`, `shape` (sección «2. Cargar e inspeccionar»). |
| 4 | 2. Cargar e inspeccionar | Resumen estadístico de las columnas numéricas. |
| 6 | 3. Filtrar y agrupar | Ejemplo: tasa de cancelación por tipo de tarifa. |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `ruta` | `dato("reservas_turisdata.csv")` | 2 |
| `reservas` | `pd.read_csv(ruta, parse_dates=["fecha_reserva", "fecha_ll…` | 2 |
| `temporadas` | `pd.DataFrame({ "mes_llegada": range(1, 13), "temporada":…` | 9 |
| `por_mes` | `df.set_index("fecha_llegada").resample("MS")["id_reserva"…` | 12 |
| `numericas` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 14 |
| `corr` | `df[numericas].corr()` | 14 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `resumen_calidad` | Devuelve una tabla con el estado de calidad de cada columna. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `agg` | Calcula varias estadísticas a la vez (media, suma…) por grupo. | 7 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 16 |
| `boxplot` | Dibuja un diagrama de cajas (mediana, cuartiles y valores extremos). | 11 |
| `corr` | Calcula la correlación entre columnas. | 14 |
| `count` | Cuenta cuántos valores hay (sin contar huecos). | 12 |
| `countplot` | Dibuja cuántas veces aparece cada categoría. | 11 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 9, 16 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `describe` | Resumen estadístico de las columnas (media, mínimo, máximo…). | 4 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 9 |
| `dtypes` | Tipo de datos de cada columna. | 16 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 12, 14 |
| `groupby` | Agrupa las filas por una columna para calcular algo en cada grupo. | 6, 7 |
| `head` | Muestra las primeras filas. | 2, 9 |
| `heatmap` | Dibuja una matriz como un mapa de colores. | 14 |
| `histplot` | Dibuja un histograma con seaborn. | 11 |
| `info` | Resumen de columnas, tipos y huecos de la tabla. | 3 |
| `isna` | Marca qué valores son huecos (nulos). | 16 |
| `mean` | Calcula la media. | 6, 16 |
| `nunique` | Cuenta cuántos valores distintos hay. | 16 |
| `plot` | Dibuja una línea (o puntos unidos). | 12 |
| `print` | Muestra un valor por pantalla. | 2 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 9 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `resample` | Agrupa una serie temporal por periodos (día, semana, mes). | 12 |
| `round` | Redondea un número a los decimales indicados. | 4, 6, 7, 16 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 11 |
| `set_index` | Convierte una columna en el índice (la etiqueta de cada fila). | 12 |
| `set_option` | Cambia una opción de cómo pandas muestra las tablas. | 1 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2 |
| `show` | Muestra el gráfico. | 11, 12, 14 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 11 |
| `sum` | Suma todos los valores. | 16 |
| `tick_params` | Ajusta el aspecto de las marcas de los ejes. | 11 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 11 |
| `title` | Pone el título del gráfico. | 12, 14 |
| `xlabel` | Pone el nombre del eje horizontal. | 12 |
| `ylabel` | Pone el nombre del eje vertical. | 12 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `seed`, `set_theme`, `set_option`.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SEMILLA = 42
np.random.seed(SEMILLA)
sns.set_theme(style="whitegrid")
pd.set_option("display.max_columns", 30)
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `np.random.seed(SEMILLA)` → `seed`: fija la semilla del azar para que salga siempre lo mismo.
- `sns.set_theme(style="whitegrid")` → `set_theme`: elige un estilo visual para todos los gráficos.
- `pd.set_option("display.max_columns", 30)` → `set_option`: cambia una opción de cómo pandas muestra las tablas.

### Celda 2 · 2. Cargar e inspeccionar · 🏫

**Qué hace:** Practica `dato`, `read_csv`, `head`, `shape` (sección «2. Cargar e inspeccionar»).

```python
ruta = dato("reservas_turisdata.csv")
reservas = pd.read_csv(ruta, parse_dates=["fecha_reserva", "fecha_llegada"])
print(reservas.shape)
reservas.head()
```

**Qué hace cada línea:**

- `ruta = dato("reservas_turisdata.csv")` → Guarda en `ruta` el resultado. `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `reservas = pd.read_csv(ruta, parse_dates=["fecha_reserva", "fecha_llegada"])` → Guarda en `reservas` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla.
- `print(reservas.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- `reservas.head()` → `head`: muestra las primeras filas.

### Celda 3 · 2. Cargar e inspeccionar · 🏫

**Qué hace:** Practica `info` (sección «2. Cargar e inspeccionar»).

```python
reservas.info()
```

**Qué hace cada línea:**

- `reservas.info()` → `info`: resumen de columnas, tipos y huecos de la tabla.

### Celda 4 · 2. Cargar e inspeccionar · 🏫

**Qué hace:** Resumen estadístico de las columnas numéricas.

```python
# Resumen estadístico de las columnas numéricas
reservas.describe().T.round(2)
```

**Qué hace cada línea:**

- `reservas.describe().T.round(2)` → `round`: redondea un número a los decimales indicados; `describe`: resumen estadístico de las columnas (media, mínimo, máximo…).

### Celda 5 · 2. Cargar e inspeccionar · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Filtrar y agrupar · 🏫

**Qué hace:** Ejemplo: tasa de cancelación por tipo de tarifa.

```python
# Ejemplo: tasa de cancelación por tipo de tarifa
df.groupby("tarifa")["cancelada"].mean().round(3)
```

**Qué hace cada línea:**

- `df.groupby("tarifa")["cancelada"].mean().round(3)` → `round`: redondea un número a los decimales indicados; `mean`: calcula la media; `groupby`: agrupa las filas por una columna para calcular algo en cada grupo.

### Celda 7 · 3. Filtrar y agrupar · 🏫

**Qué hace:** Ejemplo: varias métricas a la vez.

```python
# Ejemplo: varias métricas a la vez
df.groupby("canal").agg(reservas=("id_reserva", "count"),
                        precio_medio=("precio_noche", "mean"),
                        tasa_cancelacion=("cancelada", "mean")).round(2)
```

**Qué hace cada línea:**

- `df.groupby("canal").agg(reservas=("id_reserva", "count"),` → `round`: redondea un número a los decimales indicados; `agg`: calcula varias estadísticas a la vez (media, suma…) por grupo; `groupby`: agrupa las filas por una columna para calcular algo en cada grupo.

### Celda 8 · 3. Filtrar y agrupar · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4. Unir tablas (`merge`) · 🏫

**Qué hace:** Practica `DataFrame`, `head`, `dt` (sección «4. Unir tablas (`merge`)»).

```python
df["mes_llegada"] = df["fecha_llegada"].dt.month
temporadas = pd.DataFrame({
    "mes_llegada": range(1, 13),
    "temporada": ["alta", "alta", "alta", "baja", "baja", "baja",
                  "alta", "alta", "baja", "baja", "baja", "alta"],
})
temporadas.head(4)
```

**Qué hace cada línea:**

- `df["mes_llegada"] = df["fecha_llegada"].dt.month` → Guarda en `df["mes_llegada"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `temporadas = pd.DataFrame({` → Guarda en `temporadas` el resultado. `DataFrame`: crea una tabla de pandas (filas y columnas); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `temporadas.head(4)` → `head`: muestra las primeras filas.

### Celda 10 · 4. Unir tablas (`merge`) · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 5. Visualización exploratoria: el gráfico según… · 🏫

**Qué hace:** Practica `subplots`, `histplot`, `set`, `countplot` y más (sección «5. Visualización exploratoria: el gráfi…»).

```python
fig, ejes = plt.subplots(1, 3, figsize=(15, 4))
sns.histplot(df["precio_noche"], bins=30, ax=ejes[0], color="#2a6f97")
ejes[0].set(title="Distribución del precio por noche", xlabel="Precio por noche (€)", ylabel="Reservas")
sns.countplot(data=df, x="canal", ax=ejes[1], color="#2a6f97")
ejes[1].set(title="Reservas por canal", xlabel="Canal", ylabel="Reservas")
ejes[1].tick_params(axis="x", rotation=25)
sns.boxplot(data=df, x="tipo_habitacion", y="precio_noche", ax=ejes[2], color="#8ecae6")
ejes[2].set(title="Precio por tipo de habitación", xlabel="Tipo de habitación", ylabel="Precio por noche (€)")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `fig, ejes = plt.subplots(1, 3, figsize=(15, 4))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `sns.histplot(df["precio_noche"], bins=30, ax=ejes[0], color="#2a6f97")` → `histplot`: dibuja un histograma con seaborn.
- `ejes[0].set(title="Distribución del precio por noche", xlabel="Precio por n…` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `sns.countplot(data=df, x="canal", ax=ejes[1], color="#2a6f97")` → `countplot`: dibuja cuántas veces aparece cada categoría.
- `ejes[1].set(title="Reservas por canal", xlabel="Canal", ylabel="Reservas")` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `ejes[1].tick_params(axis="x", rotation=25)` → `tick_params`: ajusta el aspecto de las marcas de los ejes.
- `sns.boxplot(data=df, x="tipo_habitacion", y="precio_noche", ax=ejes[2], col…` → `boxplot`: dibuja un diagrama de cajas (mediana, cuartiles y valores extremos).
- `ejes[2].set(title="Precio por tipo de habitación", xlabel="Tipo de habitaci…` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- … y 1 más con las mismas ideas.

### Celda 12 · 5. Visualización exploratoria: el gráfico según… · 🏫

**Qué hace:** Serie temporal: reservas por mes de llegada.

```python
# Serie temporal: reservas por mes de llegada
por_mes = df.set_index("fecha_llegada").resample("MS")["id_reserva"].count()
plt.figure(figsize=(9, 3.5))
por_mes.plot(marker="o", color="#2a6f97")
plt.title("Reservas por mes de llegada")
plt.xlabel("Mes")
plt.ylabel("Reservas")
plt.show()
```

**Qué hace cada línea:**

- `por_mes = df.set_index("fecha_llegada").resample("MS")["id_reserva"].count()` → Guarda en `por_mes` el resultado. `count`: cuenta cuántos valores hay (sin contar huecos); `resample`: agrupa una serie temporal por periodos (día, semana, mes); `set_index`: convierte una columna en el índice (la etiqueta de cada fila).
- `plt.figure(figsize=(9, 3.5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `por_mes.plot(marker="o", color="#2a6f97")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.title("Reservas por mes de llegada")` → `title`: pone el título del gráfico.
- `plt.xlabel("Mes")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("Reservas")` → `ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 13 · 5. Visualización exploratoria: el gráfico según… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 14 · 6. Relaciones entre variables numéricas · 🏫

**Qué hace:** Practica `corr`, `figure`, `heatmap`, `title` (sección «6. Relaciones entre variables numéricas»).

```python
numericas = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
             "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "cancelada"]
corr = df[numericas].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0, cbar_kws={"label": "Correlación"})
plt.title("Correlaciones entre variables numéricas")
plt.show()
```

**Qué hace cada línea:**

- `numericas = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche…` → Guarda el valor en `numericas`.
- `corr = df[numericas].corr()` → Guarda en `corr` el resultado. `corr`: calcula la correlación entre columnas.
- `plt.figure(figsize=(8, 6))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0, cbar_kws=…` → `heatmap`: dibuja una matriz como un mapa de colores.
- `plt.title("Correlaciones entre variables numéricas")` → `title`: pone el título del gráfico.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 15 · 6. Relaciones entre variables numéricas · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 16 · 7. Calidad del dato: primer chequeo · 🏫

**Qué hace:** Practica `DataFrame`, `astype`, `sum`, `round` y más (sección «7. Calidad del dato: primer chequeo»).

```python
def resumen_calidad(tabla):
    """Devuelve una tabla con el estado de calidad de cada columna."""
    return pd.DataFrame({
        "tipo": tabla.dtypes.astype(str),
        "nulos": tabla.isna().sum(),
        "pct_nulos": (tabla.isna().mean() * 100).round(2),
        "distintos": tabla.nunique(),
    })

resumen_calidad(df)
```

**Qué hace cada línea:**

- `def resumen_calidad(tabla):` → Define la función `resumen_calidad`: Devuelve una tabla con el estado de calidad de cada columna.
- `resumen_calidad(df)` → `resumen_calidad`: devuelve una tabla con el estado de calidad de cada columna.

### Celda 17 · 7. Calidad del dato: primer chequeo · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 18 · 8. Mini-reto: tres hallazgos para el cliente · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S06_01_pandas_eda.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
