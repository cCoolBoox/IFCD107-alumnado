# Código explicado · S07.01 · Regresión lineal y polinómica: predecir el precio por noche

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_01_regresion_lineal_polinomica.ipynb) · [descargar](../S07_01_regresion_lineal_polinomica.ipynb) · ⏱ en clase: 40 min · 🏫 5 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_theme`, `read_csv`, `astype`, `dato` y más. |
| 2 | 1. La idea: una recta (o un plano) que… | Practica `astype`, `head`, `get_dummies` (sección «1. La idea: una recta (o un plano) que… |
| 4 | 1. La idea: una recta (o un plano) que… | Practica `fit`, `DummyRegressor`, `mean_absolute_error`, `r2_score` y más (sección «¿Mejo… |
| 6 | 3. Residuos: ¿el modelo se equivoca de… | Practica `subplots`, `scatter`, `axhline`, `set` y más (sección «3. Residuos: ¿el modelo… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `X` | `pd.get_dummies(df[["tipo_habitacion"]], drop_first=True).…` | 2 |
| `y` | `df["precio_noche"]` | 2 |
| `base` | `DummyRegressor(strategy="mean").fit(X_train, y_train)` | 4 |
| `residuos` | `y_test - pred` | 6 |
| `lineal` | `LinearRegression()` | 7 |
| `con_interacciones` | `make_pipeline(PolynomialFeatures(degree=2, interaction_on…` | 7 |
| `r2_lineal_cv` | `cross_val_score(lineal, X, y, cv=5, scoring="r2").mean()` | 7 |
| `r2_inter_cv` | `cross_val_score(con_interacciones, X, y, cv=5, scoring="r…` | 7 |
| `est` | `df[df["tipo_habitacion"] == "estandar"]` | 9 |
| `grados` | `list(range(1, 13))` | 9 |
| `r2_por_grado` | `[]` | 9 |
| `mes_ord` | `pd.DataFrame({"mes_llegada": range(1, 13)})` | 9 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `precio_recomendado` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `append` | Añade un elemento al final de una lista. | 9 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1, 2 |
| `axhline` | Dibuja una línea horizontal de referencia. | 6 |
| `cross_val_score` | Evalúa el modelo con validación cruzada (varias particiones). | 7, 9 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 9 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `DummyRegressor` | Modelo «tonto» de referencia que siempre predice la media. | 4 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 9 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 4, 9 |
| `get_dummies` | Convierte una columna de categorías en columnas de 0/1. | 2 |
| `head` | Muestra las primeras filas. | 2 |
| `histplot` | Dibuja un histograma con seaborn. | 6 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `legend` | Muestra la leyenda del gráfico. | 9 |
| `LinearRegression` | Modelo de regresión lineal: ajusta una recta (o un plano) a los datos. | 7, 9 |
| `list` | Crea una lista (o convierte algo en lista). | 9 |
| `make_pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 7, 9 |
| `mean` | Calcula la media. | 7, 9 |
| `mean_absolute_error` | Error medio absoluto (MAE): cuánto se equivoca de media, en las mismas unidades. | 4 |
| `plot` | Dibuja una línea (o puntos unidos). | 9 |
| `PolynomialFeatures` | Crea columnas nuevas con potencias y productos de las originales. | 7, 9 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 4, 9 |
| `print` | Muestra un valor por pantalla. | 1, 4, 7 |
| `r2_score` | Calcula R²: qué parte de la variación explica el modelo. | 4 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 9 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `scatter` | Dibuja un gráfico de puntos. | 6, 9 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 6 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 1 |
| `show` | Muestra el gráfico. | 6, 9 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 9 |
| `subplot` | Elige en qué recuadro de la figura se dibuja. | 9 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 6 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 6, 9 |
| `title` | Pone el título del gráfico. | 9 |
| `xlabel` | Pone el nombre del eje horizontal. | 9 |
| `ylabel` | Pone el nombre del eje vertical. | 9 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_theme`, `read_csv`, `astype`, `dato` y más.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)
print(df.shape)
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split, cross_val_score` → Trae `train_test_split`, `cross_val_score` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.linear_model import LinearRegression` → Trae `LinearRegression` de `sklearn.linear_model` para poder usarlo.
- `from sklearn.dummy import DummyRegressor` → Trae `DummyRegressor` de `sklearn.dummy` para poder usarlo.
- `from sklearn.preprocessing import PolynomialFeatures, StandardScaler` → Trae `PolynomialFeatures`, `StandardScaler` de `sklearn.preprocessing` para poder usarlo.
- `from sklearn.pipeline import make_pipeline` → Trae `make_pipeline` de `sklearn.pipeline` para poder usarlo.
- … y 7 más con las mismas ideas.

### Celda 2 · 1. La idea: una recta (o un plano) que se ajust… · 🏫

**Qué hace:** Practica `astype`, `head`, `get_dummies` (sección «1. La idea: una recta (o un plano) que…»).

```python
X = pd.get_dummies(df[["tipo_habitacion"]], drop_first=True).astype(int)
X["temporada_alta"] = df["temporada_alta"]
y = df["precio_noche"]
X.head()
```

**Qué hace cada línea:**

- `X = pd.get_dummies(df[["tipo_habitacion"]], drop_first=True).astype(int)` → Guarda en `X` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `get_dummies`: convierte una columna de categorías en columnas de 0/1.
- `X["temporada_alta"] = df["temporada_alta"]` → Guarda el valor en `X["temporada_alta"]`.
- `y = df["precio_noche"]` → Guarda el valor en `y`.
- `X.head()` → `head`: muestra las primeras filas.

### Celda 3 · 1. La idea: una recta (o un plano) que se ajust… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1. La idea: una recta (o un plano) que se ajust… · 🏫

**Qué hace:** Practica `fit`, `DummyRegressor`, `mean_absolute_error`, `r2_score` y más (sección «¿Mejor que "no hacer nada"?»).

```python
base = DummyRegressor(strategy="mean").fit(X_train, y_train)
print(f"Baseline: MAE = {mean_absolute_error(y_test, base.predict(X_test)):.2f} € · R² = {r2_score(y_test, base.predict(X_test)):.3f}")
```

**Qué hace cada línea:**

- `base = DummyRegressor(strategy="mean").fit(X_train, y_train)` → Guarda en `base` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `DummyRegressor`: modelo «tonto» de referencia que siempre predice la media.
- `print(f"Baseline: MAE = {mean_absolute_error(y_test, base.predict(X_test)):…` → `print`: muestra un valor por pantalla; `mean_absolute_error`: error medio absoluto (MAE): cuánto se equivoca de media, en las mismas unidades; `r2_score`: calcula R²: qué parte de la variación explica el modelo.

### Celda 5 · 2. Interpretar los coeficientes · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Residuos: ¿el modelo se equivoca de forma "s… · 🏫

**Qué hace:** Practica `subplots`, `scatter`, `axhline`, `set` y más (sección «3. Residuos: ¿el modelo se equivoca de…»).

```python
residuos = y_test - pred
fig, ejes = plt.subplots(1, 2, figsize=(11, 4))
ejes[0].scatter(pred, residuos, s=10, alpha=0.4, color="#2a6f97")
ejes[0].axhline(0, color="black", lw=1)
ejes[0].set(title="Residuos frente a predicción", xlabel="Precio predicho (€)", ylabel="Residuo (€)")
sns.histplot(residuos, bins=30, ax=ejes[1], color="#2a6f97")
ejes[1].set(title="Distribución de los residuos", xlabel="Residuo (€)", ylabel="Reservas")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `residuos = y_test - pred` → Guarda el valor en `residuos`.
- `fig, ejes = plt.subplots(1, 2, figsize=(11, 4))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ejes[0].scatter(pred, residuos, s=10, alpha=0.4, color="#2a6f97")` → `scatter`: dibuja un gráfico de puntos.
- `ejes[0].axhline(0, color="black", lw=1)` → `axhline`: dibuja una línea horizontal de referencia.
- `ejes[0].set(title="Residuos frente a predicción", xlabel="Precio predicho (…` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `sns.histplot(residuos, bins=30, ax=ejes[1], color="#2a6f97")` → `histplot`: dibuja un histograma con seaborn.
- `ejes[1].set(title="Distribución de los residuos", xlabel="Residuo (€)", yla…` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 7 · 4. Términos polinómicos y de interacción · 🏫

**Qué hace:** Practica `LinearRegression`, `make_pipeline`, `mean`, `PolynomialFeatures` y más (sección «4. Términos polinómicos y de interacción»).

```python
lineal = LinearRegression()
con_interacciones = make_pipeline(PolynomialFeatures(degree=2, interaction_only=True, include_bias=False),
                                  LinearRegression())
r2_lineal_cv = cross_val_score(lineal, X, y, cv=5, scoring="r2").mean()
r2_inter_cv = cross_val_score(con_interacciones, X, y, cv=5, scoring="r2").mean()
print(f"R² CV lineal: {r2_lineal_cv:.3f} · con interacciones: {r2_inter_cv:.3f}")
```

**Qué hace cada línea:**

- `lineal = LinearRegression()` → Guarda en `lineal` el resultado. `LinearRegression`: modelo de regresión lineal: ajusta una recta (o un plano) a los datos.
- `con_interacciones = make_pipeline(PolynomialFeatures(degree=2, interaction_…` → Guarda en `con_interacciones` el resultado. `make_pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `PolynomialFeatures`: crea columnas nuevas con potencias y productos de las originales; `LinearRegression`: modelo de regresión lineal: ajusta una recta (o un plano) a los datos.
- `r2_lineal_cv = cross_val_score(lineal, X, y, cv=5, scoring="r2").mean()` → Guarda en `r2_lineal_cv` el resultado. `mean`: calcula la media; `cross_val_score`: evalúa el modelo con validación cruzada (varias particiones).
- `r2_inter_cv = cross_val_score(con_interacciones, X, y, cv=5, scoring="r2").…` → Guarda en `r2_inter_cv` el resultado. `mean`: calcula la media; `cross_val_score`: evalúa el modelo con validación cruzada (varias particiones).
- `print(f"R² CV lineal: {r2_lineal_cv:.3f} · con interacciones: {r2_inter_cv:…` → `print`: muestra un valor por pantalla.

### Celda 8 · 4. Términos polinómicos y de interacción · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5. Polinomios para captar curvas... y su peligro · 🏠

**Qué hace:** Practica `list`, `DataFrame`, `figure`, `subplot` y más (sección «5. Polinomios para captar curvas... y s…»).

```python
est = df[df["tipo_habitacion"] == "estandar"]
X_mes, y_est = est[["mes_llegada"]], est["precio_noche"]
grados = list(range(1, 13))
r2_por_grado = []
for g in grados:
    m = make_pipeline(PolynomialFeatures(g), StandardScaler(), LinearRegression())
    r2_por_grado.append(cross_val_score(m, X_mes, y_est, cv=5, scoring="r2").mean())

mes_ord = pd.DataFrame({"mes_llegada": range(1, 13)})
plt.figure(figsize=(11, 4))
plt.subplot(1, 2, 1)
plt.scatter(est["mes_llegada"], est["precio_noche"], s=8, alpha=0.3, color="gray", label="Reservas estándar")
for g, c in [(2, "#e63946"), (8, "#2a6f97")]:
    m = make_pipeline(PolynomialFeatures(g), StandardScaler(), LinearRegression()).fit(X_mes, y_est)
    plt.plot(mes_ord, m.predict(mes_ord), color=c, lw=2, label=f"Grado {g}")
plt.title("Precio de la estándar según el mes")
plt.xlabel("Mes de llegada")
plt.ylabel("Precio por noche (€)")
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(grados, r2_por_grado, marker="o", color="#2a6f97")
plt.title("R² (validación cruzada) según el grado")
plt.xlabel("Grado del polinomio")
plt.ylabel("R²")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `est = df[df["tipo_habitacion"] == "estandar"]` → Guarda el valor en `est`.
- `X_mes, y_est = est[["mes_llegada"]], est["precio_noche"]` → Guarda el valor en `X_mes, y_est`.
- `grados = list(range(1, 13))` → Guarda en `grados` el resultado. `list`: crea una lista (o convierte algo en lista); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `r2_por_grado = []` → Guarda el valor en `r2_por_grado`.
- `for g in grados:` → Repite el bloque de debajo para cada valor de `g` en `grados`. Dentro del bloque: `make_pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `PolynomialFeatures`: crea columnas nuevas con potencias y productos de las originales; `StandardScaler`: escala los números para que tengan media 0 y desviación 1.
- `mes_ord = pd.DataFrame({"mes_llegada": range(1, 13)})` → Guarda en `mes_ord` el resultado. `DataFrame`: crea una tabla de pandas (filas y columnas); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `plt.figure(figsize=(11, 4))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.subplot(1, 2, 1)` → `subplot`: elige en qué recuadro de la figura se dibuja.
- `plt.scatter(est["mes_llegada"], est["precio_noche"], s=8, alpha=0.3, color=…` → `scatter`: dibuja un gráfico de puntos.
- … y 12 más con las mismas ideas.

### Celda 10 · 5. Polinomios para captar curvas... y su peligro · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 6. Mini-reto: tarifa de referencia explicada al… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S07_01_regresion_lineal_polinomica.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
