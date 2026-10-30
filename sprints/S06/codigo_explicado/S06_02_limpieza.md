# Código explicado · S06.02 · Limpieza de datos: encontrar defectos y sus causas

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_02_limpieza.ipynb) · [descargar](../notebooks/S06_02_limpieza.ipynb) · ⏱ en clase: 55 min · 🏫 10 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_theme`. |
| 2 | 1. Diagnóstico inicial | Practica `read_csv`, `info`, `dato`, `shape` (sección «1. Diagnóstico inicial»). |
| 3 | 1. Diagnóstico inicial | Practica `DataFrame`, `astype`, `sum`, `round` y más (sección «1. Diagnóstico inicial»). |
| 4 | 2. Duplicados | Practica `head`, `sum`, `sort_values`, `duplicated` (sección «2. Duplicados»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `crudo` | `pd.read_csv(dato("reservas_sucio.csv"))` | 2 |
| `con_coma` | `d1["precio_noche"].astype(str).str.contains(",").sum()` | 6 |
| `iso` | `pd.to_datetime(d2["fecha_reserva"], format="%Y-%m-%d", er…` | 8 |
| `espanol` | `pd.to_datetime(d2["fecha_reserva"], format="%d/%m/%Y", er…` | 8 |
| `antelacion_calculada` | `(d5["fecha_llegada"] - d5["fecha_reserva"]).dt.days` | 14 |
| `incoherentes` | `antelacion_calculada != d5["antelacion_dias"]` | 14 |
| `comparacion` | `pd.DataFrame({ "antes": [len(crudo), crudo.duplicated().s…` | 17 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `resumen_calidad` | Función definida en el cuaderno. |
| `limpiar_reservas` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 3, 6 |
| `between` | Marca los valores que están entre dos límites. | 12 |
| `boxplot` | Dibuja un diagrama de cajas (mediana, cuartiles y valores extremos). | 12 |
| `contains` | Marca los textos que contienen un trozo de texto o un patrón. | 6 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 3, 17 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `describe` | Resumen estadístico de las columnas (media, mínimo, máximo…). | 12 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 14 |
| `dtypes` | Tipo de datos de cada columna. | 3 |
| `duplicated` | Marca qué filas están repetidas. | 4, 17 |
| `head` | Muestra las primeras filas. | 4 |
| `info` | Resumen de columnas, tipos y huecos de la tabla. | 2 |
| `isna` | Marca qué valores son huecos (nulos). | 3, 8 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 17 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 12 |
| `mean` | Calcula la media. | 3 |
| `min` | Devuelve el valor más pequeño. | 14 |
| `notna` | Marca qué valores NO son huecos. | 8 |
| `nunique` | Cuenta cuántos valores distintos hay. | 3, 17 |
| `print` | Muestra un valor por pantalla. | 2, 4, 6, 8, 10, 12… |
| `query` | Filtra filas con una condición escrita como texto. | 15 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `round` | Redondea un número a los decimales indicados. | 3, 12 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 12 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2 |
| `show` | Muestra el gráfico. | 12 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 4 |
| `str` | Da acceso a las operaciones de texto sobre una columna. | 6 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 12 |
| `sum` | Suma todos los valores. | 3, 4, 6, 8, 14, 17 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 12 |
| `to_datetime` | Convierte un texto en fecha. | 8 |
| `to_string` | Convierte la tabla en texto para mostrarla entera. | 10 |
| `value_counts` | Cuenta cuántas veces aparece cada valor. | 10 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_theme`.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SEMILLA = 42
sns.set_theme(style="whitegrid")
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `sns.set_theme(style="whitegrid")` → `set_theme`: elige un estilo visual para todos los gráficos.

### Celda 2 · 1. Diagnóstico inicial · 🏫

**Qué hace:** Practica `read_csv`, `info`, `dato`, `shape` (sección «1. Diagnóstico inicial»).

```python
crudo = pd.read_csv(dato("reservas_sucio.csv"))
print(crudo.shape)
crudo.info()
```

**Qué hace cada línea:**

- `crudo = pd.read_csv(dato("reservas_sucio.csv"))` → Guarda en `crudo` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `print(crudo.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- `crudo.info()` → `info`: resumen de columnas, tipos y huecos de la tabla.

### Celda 3 · 1. Diagnóstico inicial · 🏫

**Qué hace:** Practica `DataFrame`, `astype`, `sum`, `round` y más (sección «1. Diagnóstico inicial»).

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

**Qué hace cada línea:**

- `def resumen_calidad(tabla):` → Define la función `resumen_calidad`: Función definida en el cuaderno.
- `resumen_calidad(crudo)` → `resumen_calidad`: función definida en el cuaderno.

### Celda 4 · 2. Duplicados · 🏫

**Qué hace:** Practica `head`, `sum`, `sort_values`, `duplicated` (sección «2. Duplicados»).

```python
print("Filas duplicadas exactas:", crudo.duplicated().sum())
crudo[crudo.duplicated(keep=False)].sort_values("id_reserva").head(6)
```

**Qué hace cada línea:**

- `print("Filas duplicadas exactas:", crudo.duplicated().sum())` → `print`: muestra un valor por pantalla; `sum`: suma todos los valores; `duplicated`: marca qué filas están repetidas.
- `crudo[crudo.duplicated(keep=False)].sort_values("id_reserva").head(6)` → `head`: muestra las primeras filas; `sort_values`: ordena la tabla por una o varias columnas; `duplicated`: marca qué filas están repetidas.

### Celda 5 · 2. Duplicados · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Tipos incorrectos: números escritos como tex… · 🏫

**Qué hace:** Practica `sum`, `contains`, `astype` (sección «3. Tipos incorrectos: números escritos…»).

```python
con_coma = d1["precio_noche"].astype(str).str.contains(",").sum()
print("Precios con coma decimal:", con_coma)
```

**Qué hace cada línea:**

- `con_coma = d1["precio_noche"].astype(str).str.contains(",").sum()` → Guarda en `con_coma` el resultado. `sum`: suma todos los valores; `contains`: marca los textos que contienen un trozo de texto o un patrón; `str`: da acceso a las operaciones de texto sobre una columna.
- `print("Precios con coma decimal:", con_coma)` → `print`: muestra un valor por pantalla.

### Celda 7 · 3. Tipos incorrectos: números escritos como tex… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4. Fechas en formatos mezclados · 🏫

**Qué hace:** Practica `to_datetime`, `sum`, `notna`, `isna` (sección «4. Fechas en formatos mezclados»).

```python
iso = pd.to_datetime(d2["fecha_reserva"], format="%Y-%m-%d", errors="coerce")
espanol = pd.to_datetime(d2["fecha_reserva"], format="%d/%m/%Y", errors="coerce")
print("ISO:", iso.notna().sum(), "· dd/mm/aaaa:", espanol.notna().sum(), "· sin leer:", (iso.isna() & espanol.isna()).sum())
```

**Qué hace cada línea:**

- `iso = pd.to_datetime(d2["fecha_reserva"], format="%Y-%m-%d", errors="coerce…` → Guarda en `iso` el resultado. `to_datetime`: convierte un texto en fecha.
- `espanol = pd.to_datetime(d2["fecha_reserva"], format="%d/%m/%Y", errors="co…` → Guarda en `espanol` el resultado. `to_datetime`: convierte un texto en fecha.
- `print("ISO:", iso.notna().sum(), "· dd/mm/aaaa:", espanol.notna().sum(), "·…` → `print`: muestra un valor por pantalla; `sum`: suma todos los valores; `notna`: marca qué valores NO son huecos.

### Celda 9 · 4. Fechas en formatos mezclados · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5. Categorías inconsistentes · 🏫

**Qué hace:** Practica `to_string`, `value_counts` (sección «5. Categorías inconsistentes»).

```python
print(d3["canal"].value_counts().to_string())
print()
print(d3["pais_origen"].value_counts().to_string())
```

**Qué hace cada línea:**

- `print(d3["canal"].value_counts().to_string())` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `value_counts`: cuenta cuántas veces aparece cada valor.
- `print()` → `print`: muestra un valor por pantalla.
- `print(d3["pais_origen"].value_counts().to_string())` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `value_counts`: cuenta cuántas veces aparece cada valor.

### Celda 11 · 5. Categorías inconsistentes · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 12 · 6. Valores imposibles y *outliers* · 🏫

**Qué hace:** Practica `subplots`, `boxplot`, `set`, `tight_layout` y más (sección «6. Valores imposibles y *outliers*»).

```python
print(d4[["precio_noche", "noches", "antelacion_dias"]].describe().round(1))
fig, ejes = plt.subplots(1, 2, figsize=(11, 3.5))
sns.boxplot(x=d4["precio_noche"], ax=ejes[0], color="#8ecae6")
ejes[0].set(title="Precio con outliers", xlabel="Precio por noche (€)")
sns.boxplot(x=d4.loc[d4["precio_noche"].between(1, 1000), "precio_noche"], ax=ejes[1], color="#8ecae6")
ejes[1].set(title="Precio sin los valores imposibles", xlabel="Precio por noche (€)")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `print(d4[["precio_noche", "noches", "antelacion_dias"]].describe().round(1))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `describe`: resumen estadístico de las columnas (media, mínimo, máximo…).
- `fig, ejes = plt.subplots(1, 2, figsize=(11, 3.5))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `sns.boxplot(x=d4["precio_noche"], ax=ejes[0], color="#8ecae6")` → `boxplot`: dibuja un diagrama de cajas (mediana, cuartiles y valores extremos).
- `ejes[0].set(title="Precio con outliers", xlabel="Precio por noche (€)")` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `sns.boxplot(x=d4.loc[d4["precio_noche"].between(1, 1000), "precio_noche"],…` → `boxplot`: dibuja un diagrama de cajas (mediana, cuartiles y valores extremos); `loc`: selecciona filas/columnas por su etiqueta o por una condición; `between`: marca los valores que están entre dos límites.
- `ejes[1].set(title="Precio sin los valores imposibles", xlabel="Precio por n…` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 13 · 6. Valores imposibles y *outliers* · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 14 · 7. Consistencia entre columnas · 🏫

**Qué hace:** Las fechas mandan: recalculamos toda la columna desde ellas.

```python
antelacion_calculada = (d5["fecha_llegada"] - d5["fecha_reserva"]).dt.days
incoherentes = antelacion_calculada != d5["antelacion_dias"]
print("Antelaciones negativas:", (d5["antelacion_dias"] < 0).sum())
print("Antelaciones que no cuadran con las fechas:", incoherentes.sum())
# Las fechas mandan: recalculamos toda la columna desde ellas
d5["antelacion_dias"] = antelacion_calculada
print("Mínimo tras recalcular:", d5["antelacion_dias"].min())
```

**Qué hace cada línea:**

- `antelacion_calculada = (d5["fecha_llegada"] - d5["fecha_reserva"]).dt.days` → Guarda en `antelacion_calculada` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `incoherentes = antelacion_calculada != d5["antelacion_dias"]` → Guarda el valor en `incoherentes`.
- `print("Antelaciones negativas:", (d5["antelacion_dias"] < 0).sum())` → `print`: muestra un valor por pantalla; `sum`: suma todos los valores.
- `print("Antelaciones que no cuadran con las fechas:", incoherentes.sum())` → `print`: muestra un valor por pantalla; `sum`: suma todos los valores.
- `d5["antelacion_dias"] = antelacion_calculada` → Guarda el valor en `d5["antelacion_dias"]`.
- `print("Mínimo tras recalcular:", d5["antelacion_dias"].min())` → `print`: muestra un valor por pantalla; `min`: devuelve el valor más pequeño.

### Celda 15 · 8. Nulos: ¿qué hacemos con ellos? · 🏫

**Qué hace:** Practica `query` (sección «8. Nulos: ¿qué hacemos con ellos?»).

```python
resumen_calidad(d5).query("nulos > 0")
```

**Qué hace cada línea:**

- `resumen_calidad(d5).query("nulos > 0")` → `query`: filtra filas con una condición escrita como texto; `resumen_calidad`: función definida en el cuaderno.

### Celda 16 · 9. Mini-reto: tu función `limpiar_reservas` · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 17 · 9. Mini-reto: tu función `limpiar_reservas` · 🏠

**Qué hace:** Comparación antes/después.

```python
# Comparación antes/después
comparacion = pd.DataFrame({
    "antes": [len(crudo), crudo.duplicated().sum(), crudo["canal"].nunique(), crudo["pais_origen"].nunique()],
    "después": [len(limpio), limpio.duplicated().sum(), limpio["canal"].nunique(), limpio["pais_origen"].nunique()],
}, index=["filas", "duplicados", "valores distintos de canal", "valores distintos de país"])
comparacion
```

**Qué hace cada línea:**

- `comparacion = pd.DataFrame({` → Guarda en `comparacion` el resultado. `DataFrame`: crea una tabla de pandas (filas y columnas); `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `sum`: suma todos los valores.

---
*Generado a partir de `laboratorios/fuentes/S06_02_limpieza.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
