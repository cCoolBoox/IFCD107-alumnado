# Código explicado · S05.05 · Estadística con Python (2): contrastes de hipótesis, correlación y causalidad

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_05_contrastes_causalidad.ipynb) · [descargar](../notebooks/S05_05_contrastes_causalidad.ipynb) · ⏱ en clase: 40 min · 🏫 0 celdas de código en clase · 🏠 6 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| — | — | Este cuaderno no tiene celdas de explicación previas: se trabaja directamente en el cuaderno. |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `diaria` | `pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["f…` | 1 |
| `reservas` | `pd.read_csv(dato("reservas_turisdata.csv"))` | 1 |
| `festivos` | `diaria.loc[diaria["festivo"] == 1, "ocupacion_pct"]` | 2 |
| `normales` | `diaria.loc[diaria["festivo"] == 0, "ocupacion_pct"]` | 2 |
| `tabla_canal` | `pd.crosstab(reservas["canal"], reservas["cancelada"])` | 5 |
| `modelo_simple` | `smf.ols("ocupacion_pct ~ temperatura_c", data=diaria).fit…` | 9 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `muestras_posterior` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `beta` | Distribución beta: genera probabilidades entre 0 y 1. | 11 |
| `corr` | Calcula la correlación entre columnas. | 7 |
| `crosstab` | Cuenta cuántos casos hay en cada combinación de dos columnas. | 5 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 11 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 9 |
| `groupby` | Agrupa las filas por una columna para calcular algo en cada grupo. | 5 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2, 11 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 2, 11 |
| `mean` | Calcula la media. | 2, 5 |
| `ols` | Ajusta una regresión lineal estadística (con p-valores) escrita como fórmula. | 9 |
| `percentile` | Calcula un percentil (el valor bajo el que queda ese % de los datos). | 11 |
| `print` | Muestra un valor por pantalla. | 1, 2, 5, 7, 9, 11 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `round` | Redondea un número a los decimales indicados. | 5, 7, 9, 11 |
| `scatter` | Dibuja un gráfico de puntos. | 7 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 1 |
| `show` | Muestra el gráfico. | 7 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 5 |
| `spearmanr` | Calcula la correlación de Spearman (por rangos) y su p-valor. | 7 |
| `sum` | Suma todos los valores. | 11 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 7 |
| `title` | Pone el título del gráfico. | 7 |
| `to_dict` | Convierte la tabla o la fila en un diccionario. | 9 |
| `xlabel` | Pone el nombre del eje horizontal. | 7 |
| `ylabel` | Pone el nombre del eje vertical. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏠

**Qué hace:** Practica `read_csv`, `dato`, `dt`, `shape` (sección «Contexto TurisData»).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats

SEMILLA = 42
diaria = pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["fecha"])
diaria["mes"] = diaria["fecha"].dt.month
reservas = pd.read_csv(dato("reservas_turisdata.csv"))
print(diaria.shape, reservas.shape)
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import statsmodels.formula.api as smf` → Trae `statsmodels.formula.api` (lo llamamos `smf`) para poder usarlo.
- `from scipy import stats` → Trae `stats` de `scipy` para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `diaria = pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["fecha"])` → Guarda en `diaria` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `diaria["mes"] = diaria["fecha"].dt.month` → Guarda en `diaria["mes"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `reservas = pd.read_csv(dato("reservas_turisdata.csv"))` → Guarda en `reservas` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- … y 1 más con las mismas ideas.

### Celda 2 · 1 · Contraste de hipótesis: la lógica · 🏠

**Qué hace:** Practica `loc`, `mean` (sección «1 · Contraste de hipótesis: la lógica»).

```python
festivos = diaria.loc[diaria["festivo"] == 1, "ocupacion_pct"]
normales = diaria.loc[diaria["festivo"] == 0, "ocupacion_pct"]
print(f"Festivos: n={len(festivos)}, media={festivos.mean():.1f} · Normales: n={len(normales)}, media={normales.mean():.1f}")
```

**Qué hace cada línea:**

- `festivos = diaria.loc[diaria["festivo"] == 1, "ocupacion_pct"]` → Guarda en `festivos` el resultado. `loc`: selecciona filas/columnas por su etiqueta o por una condición.
- `normales = diaria.loc[diaria["festivo"] == 0, "ocupacion_pct"]` → Guarda en `normales` el resultado. `loc`: selecciona filas/columnas por su etiqueta o por una condición.
- `print(f"Festivos: n={len(festivos)}, media={festivos.mean():.1f} · Normales…` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `mean`: calcula la media.

### Celda 3 · 1 · Contraste de hipótesis: la lógica · 🏠 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1 · Contraste de hipótesis: la lógica · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2 · Chi-cuadrado: dos variables categóricas · 🏠

**Qué hace:** Practica `crosstab`, `sort_values`, `round`, `mean` y más (sección «2 · Chi-cuadrado: dos variables categór…»).

```python
tabla_canal = pd.crosstab(reservas["canal"], reservas["cancelada"])
print(tabla_canal)
print((100 * reservas.groupby("canal")["cancelada"].mean()).round(1).sort_values())
```

**Qué hace cada línea:**

- `tabla_canal = pd.crosstab(reservas["canal"], reservas["cancelada"])` → Guarda en `tabla_canal` el resultado. `crosstab`: cuenta cuántos casos hay en cada combinación de dos columnas.
- `print(tabla_canal)` → `print`: muestra un valor por pantalla.
- `print((100 * reservas.groupby("canal")["cancelada"].mean()).round(1).sort_v…` → `print`: muestra un valor por pantalla; `sort_values`: ordena la tabla por una o varias columnas; `round`: redondea un número a los decimales indicados.

### Celda 6 · 2 · Chi-cuadrado: dos variables categóricas · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 3 · Correlación · 🏠

**Qué hace:** Practica `scatter`, `xlabel`, `ylabel`, `title` y más (sección «3 · Correlación»).

```python
print("Pearson:", round(diaria["ocupacion_pct"].corr(diaria["temperatura_c"]), 3))
print("Spearman:", round(stats.spearmanr(diaria["ocupacion_pct"], diaria["temperatura_c"]).statistic, 3))

diaria.plot.scatter(x="temperatura_c", y="ocupacion_pct", c="mes", colormap="twilight", s=8, figsize=(8, 4))
plt.xlabel("Temperatura (°C)")
plt.ylabel("Ocupación (%)")
plt.title("Ocupación frente a temperatura (el color es el mes)")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `print("Pearson:", round(diaria["ocupacion_pct"].corr(diaria["temperatura_c"…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `corr`: calcula la correlación entre columnas.
- `print("Spearman:", round(stats.spearmanr(diaria["ocupacion_pct"], diaria["t…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `spearmanr`: calcula la correlación de Spearman (por rangos) y su p-valor.
- `diaria.plot.scatter(x="temperatura_c", y="ocupacion_pct", c="mes", colormap…` → `scatter`: dibuja un gráfico de puntos.
- `plt.xlabel("Temperatura (°C)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("Ocupación (%)")` → `ylabel`: pone el nombre del eje vertical.
- `plt.title("Ocupación frente a temperatura (el color es el mes)")` → `title`: pone el título del gráfico.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 8 · 3 · Correlación · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4 · Correlación no es causalidad · 🏠

**Qué hace:** Practica `fit`, `to_dict`, `ols`, `round` (sección «4 · Correlación no es causalidad»).

```python
modelo_simple = smf.ols("ocupacion_pct ~ temperatura_c", data=diaria).fit()
print(modelo_simple.params.round(3).to_dict(), "p =", modelo_simple.pvalues["temperatura_c"])
```

**Qué hace cada línea:**

- `modelo_simple = smf.ols("ocupacion_pct ~ temperatura_c", data=diaria).fit()` → Guarda en `modelo_simple` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `ols`: ajusta una regresión lineal estadística (con p-valores) escrita como fórmula.
- `print(modelo_simple.params.round(3).to_dict(), "p =", modelo_simple.pvalues…` → `print`: muestra un valor por pantalla; `to_dict`: convierte la tabla o la fila en un diccionario; `round`: redondea un número a los decimales indicados.

### Celda 10 · 4 · Correlación no es causalidad · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 5 · Un vistazo a la idea bayesiana · 🏠

**Qué hace:** Practica `default_rng`, `beta`, `round`, `loc` y más (sección «5 · Un vistazo a la idea bayesiana»).

```python
def muestras_posterior(canal, n_muestras=100_000):
    rng = np.random.default_rng(SEMILLA)
    x = reservas.loc[reservas["canal"] == canal, "cancelada"]
    return rng.beta(1 + x.sum(), 1 + len(x) - x.sum(), n_muestras)

post_directo, post_web = muestras_posterior("directo"), muestras_posterior("web_intermediaria")
print("Tasa creíble directo (95 %):", np.percentile(post_directo, [2.5, 97.5]).round(3))
print("Tasa creíble web_intermediaria (95 %):", np.percentile(post_web, [2.5, 97.5]).round(3))
```

**Qué hace cada línea:**

- `def muestras_posterior(canal, n_muestras=100_000):` → Define la función `muestras_posterior`: Función definida en el cuaderno.
- `post_directo, post_web = muestras_posterior("directo"), muestras_posterior(…` → Guarda en `post_directo, post_web` el resultado. `muestras_posterior`: función definida en el cuaderno.
- `print("Tasa creíble directo (95 %):", np.percentile(post_directo, [2.5, 97.…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `percentile`: calcula un percentil (el valor bajo el que queda ese % de los datos).
- `print("Tasa creíble web_intermediaria (95 %):", np.percentile(post_web, [2.…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `percentile`: calcula un percentil (el valor bajo el que queda ese % de los datos).

### Celda 12 · 5 · Un vistazo a la idea bayesiana · 🏠 · ejercicio 6

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 6 · Mini-reto integrador: ¿ocupación de inviern… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S05_05_contrastes_causalidad.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
