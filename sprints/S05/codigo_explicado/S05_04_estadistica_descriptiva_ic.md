# Código explicado · S05.04 · Estadística con Python (1): descriptiva, distribuciones, Monte Carlo e intervalos de confianza

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_04_estadistica_descriptiva_ic.ipynb) · [descargar](../notebooks/S05_04_estadistica_descriptiva_ic.ipynb) · ⏱ en clase: 30 min · 🏫 5 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | Contexto TurisData | Practica `read_csv`, `head`, `dato`, `dt` y más (sección «Contexto TurisData»). |
| 2 | 1 · Estadística descriptiva | Practica `round`, `skew`, `describe` (sección «1 · Estadística descriptiva»). |
| 5 | 2 · Distribuciones con SciPy | Practica `mean`, `std`, `round`, `sf` (sección «2 · Distribuciones con SciPy»). |
| 7 | 3 · Simulación de Monte Carlo | Una simulación = 170 reservas, cada una se presenta (1) o no (0). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `ocupacion_df` | `pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["f…` | 1 |
| `reservas` | `pd.read_csv(dato("reservas_turisdata.csv"))` | 1 |
| `rng` | `np.random.default_rng(SEMILLA)` | 7 |
| `p_presentarse` | `1 - 0.459` | 7 |
| `una_simulacion` | `rng.random(170) < p_presentarse` | 7 |
| `n` | `len(serie)` | 9 |
| `error` | `stats.sem(serie)` | 9 |
| `ic_total` | `stats.t.interval(0.95, n - 1, loc=serie.mean(), scale=err…` | 9 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `ic_mes` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 7 |
| `describe` | Resumen estadístico de las columnas (media, mínimo, máximo…). | 2 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `head` | Muestra las primeras filas. | 1 |
| `interval` | Calcula un intervalo de confianza de una distribución. | 9 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 9 |
| `mean` | Calcula la media. | 5, 9 |
| `ppf` | Valor de la normal para una probabilidad dada. | 5 |
| `print` | Muestra un valor por pantalla. | 1, 2, 5, 7, 9 |
| `random` | Número aleatorio entre 0 y 1. | 7 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `round` | Redondea un número a los decimales indicados. | 2, 5 |
| `sem` | Error estándar de la media. | 9 |
| `sf` | Probabilidad de superar un valor (cola de la distribución). | 5 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 1 |
| `skew` | Mide la asimetría de la distribución. | 2 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 5 |
| `sum` | Suma todos los valores. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏫

**Qué hace:** Practica `read_csv`, `head`, `dato`, `dt` y más (sección «Contexto TurisData»).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

SEMILLA = 42
ocupacion_df = pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["fecha"])
ocupacion_df["mes"] = ocupacion_df["fecha"].dt.month
reservas = pd.read_csv(dato("reservas_turisdata.csv"))
print(ocupacion_df.shape, reservas.shape)
ocupacion_df.head()
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from scipy import stats` → Trae `stats` de `scipy` para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `ocupacion_df = pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["fech…` → Guarda en `ocupacion_df` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `ocupacion_df["mes"] = ocupacion_df["fecha"].dt.month` → Guarda en `ocupacion_df["mes"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `reservas = pd.read_csv(dato("reservas_turisdata.csv"))` → Guarda en `reservas` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `print(ocupacion_df.shape, reservas.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- … y 1 más con las mismas ideas.

### Celda 2 · 1 · Estadística descriptiva · 🏫

**Qué hace:** Practica `round`, `skew`, `describe` (sección «1 · Estadística descriptiva»).

```python
print(ocupacion_df["ocupacion_pct"].describe().round(2))
print("Asimetría:", round(ocupacion_df["ocupacion_pct"].skew(), 2))
```

**Qué hace cada línea:**

- `print(ocupacion_df["ocupacion_pct"].describe().round(2))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `describe`: resumen estadístico de las columnas (media, mínimo, máximo…).
- `print("Asimetría:", round(ocupacion_df["ocupacion_pct"].skew(), 2))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `skew`: mide la asimetría de la distribución.

### Celda 3 · 1 · Estadística descriptiva · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1 · Estadística descriptiva · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2 · Distribuciones con SciPy · 🏫

**Qué hace:** Practica `mean`, `std`, `round`, `sf` (sección «2 · Distribuciones con SciPy»).

```python
mu, sigma = serie.mean(), serie.std()
print("P(ocupación > 85 %) según la normal:", round(stats.norm.sf(85, mu, sigma), 4))
print("Proporción real de días > 85 %:     ", round((serie > 85).mean(), 4))
print("Ocupación que se supera solo el 10 % de los días:", round(stats.norm.ppf(0.90, mu, sigma), 1))
```

**Qué hace cada línea:**

- `mu, sigma = serie.mean(), serie.std()` → Guarda en `mu, sigma` el resultado. `mean`: calcula la media; `std`: calcula la desviación típica (cuánto se separan los datos de la media).
- `print("P(ocupación > 85 %) según la normal:", round(stats.norm.sf(85, mu, s…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `sf`: probabilidad de superar un valor (cola de la distribución).
- `print("Proporción real de días > 85 %: ", round((serie > 85).mean(), 4))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.
- `print("Ocupación que se supera solo el 10 % de los días:", round(stats.norm…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `ppf`: valor de la normal para una probabilidad dada.

### Celda 6 · 2 · Distribuciones con SciPy · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 3 · Simulación de Monte Carlo · 🏫

**Qué hace:** Una simulación = 170 reservas, cada una se presenta (1) o no (0).

```python
rng = np.random.default_rng(SEMILLA)
p_presentarse = 1 - 0.459
# Una simulación = 170 reservas, cada una se presenta (1) o no (0)
una_simulacion = rng.random(170) < p_presentarse
print("Se presentan en esta simulación:", una_simulacion.sum())
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `p_presentarse = 1 - 0.459` → Guarda el valor en `p_presentarse`.
- `una_simulacion = rng.random(170) < p_presentarse` → Guarda en `una_simulacion` el resultado. `random`: número aleatorio entre 0 y 1.
- `print("Se presentan en esta simulación:", una_simulacion.sum())` → `print`: muestra un valor por pantalla; `sum`: suma todos los valores.

### Celda 8 · 3 · Simulación de Monte Carlo · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4 · Intervalos de confianza · 🏫

**Qué hace:** Practica `sem`, `interval`, `mean` (sección «4 · Intervalos de confianza»).

```python
n = len(serie)
error = stats.sem(serie)            # error estándar de la media
ic_total = stats.t.interval(0.95, n - 1, loc=serie.mean(), scale=error)
print(f"Media {serie.mean():.2f} · IC 95 %: ({ic_total[0]:.2f}, {ic_total[1]:.2f})")
```

**Qué hace cada línea:**

- `n = len(serie)` → Guarda en `n` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `error = stats.sem(serie) # error estándar de la media` → Guarda en `error` el resultado. `sem`: error estándar de la media.
- `ic_total = stats.t.interval(0.95, n - 1, loc=serie.mean(), scale=error)` → Guarda en `ic_total` el resultado. `interval`: calcula un intervalo de confianza de una distribución; `mean`: calcula la media.
- `print(f"Media {serie.mean():.2f} · IC 95 %: ({ic_total[0]:.2f}, {ic_total[1…` → `print`: muestra un valor por pantalla; `mean`: calcula la media.

### Celda 10 · 4 · Intervalos de confianza · 🏫 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 5 · Mini-reto integrador: ¿enero y septiembre s… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S05_04_estadistica_descriptiva_ic.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
