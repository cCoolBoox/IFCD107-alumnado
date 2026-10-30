# Código explicado · S07.02 · Regularización: Ridge y Lasso

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_02_ridge_lasso.ipynb) · [descargar](../notebooks/S07_02_ridge_lasso.ipynb) · ⏱ en clase: 35 min · 🏫 4 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Simulamos el alojamiento nuevo: solo 120 reservas para entrenar, el resto para evaluar. |
| 2 | 1. El problema: muchas variables, pocos… | Practica `fit`, `make_pipeline`, `clone`, `PolynomialFeatures` y más (sección «1. El prob… |
| 4 | 2. Ridge (L2): encoger los coeficientes | Practica `fit_transform`, `get_feature_names_out`, `logspace`, `array` y más (sección «2.… |
| 7 | 4. Lasso (L1): seleccionar variables | ¿Qué variables ha conservado Lasso? (las de mayor peso). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "petici…` | 1 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 1 |
| `prep` | `ColumnTransformer([("num", StandardScaler(), columnas_num…` | 1 |
| `ols` | `modelo_con(LinearRegression()).fit(X_train, y_train)` | 2 |
| `Xp_train` | `prep.fit_transform(X_train)` | 4 |
| `nombres` | `prep.get_feature_names_out()` | 4 |
| `alphas` | `np.logspace(-2, 3, 30)` | 4 |
| `trayectoria_ridge` | `np.array([Ridge(alpha=a).fit(Xp_train, y_train).coef_ for…` | 4 |
| `trayectoria_lasso` | `np.array([Lasso(alpha=a, max_iter=50000).fit(Xp_train, y_…` | 4 |
| `nombres_poly` | `lasso[:-1].get_feature_names_out()` | 7 |
| `coef_lasso` | `pd.Series(lasso[-1].coef_, index=nombres_poly)` | 7 |
| `principales` | `coef_lasso[coef_lasso != 0].sort_values(key=np.abs, ascen…` | 7 |
| `comparativa` | `pd.DataFrame({ "R² train": [ols.score(X_train, y_train),…` | 8 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `modelo_con` | Preprocesado + variables de grado 2 + escalado + regresor. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 4 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1 |
| `axhline` | Dibuja una línea horizontal de referencia. | 4 |
| `clone` | Crea una copia del modelo con los mismos ajustes pero sin entrenar. | 2 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 8 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `fillna` | Rellena los huecos con un valor. | 1 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 2, 4 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 4 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 4, 7 |
| `head` | Muestra las primeras filas. | 7 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `Lasso` | Regresión lineal con penalización L1 (puede dejar coeficientes en 0). | 4 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 1 |
| `LinearRegression` | Modelo de regresión lineal: ajusta una recta (o un plano) a los datos. | 2 |
| `logspace` | Crea una secuencia de números espaciados en escala logarítmica. | 4 |
| `make_pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 2 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `plot` | Dibuja una línea (o puntos unidos). | 4 |
| `PolynomialFeatures` | Crea columnas nuevas con potencias y productos de las originales. | 2 |
| `print` | Muestra un valor por pantalla. | 1, 2 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `Ridge` | Regresión lineal con penalización L2 (encoge los coeficientes). | 4 |
| `round` | Redondea un número a los decimales indicados. | 7, 8 |
| `score` | Calcula la nota del modelo con la métrica por defecto. | 2, 8 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 7 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 4 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_xscale` | Cambia la escala del eje horizontal (por ejemplo, logarítmica). | 4 |
| `set_ylabel` | Pone el nombre del eje vertical. | 4 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2 |
| `show` | Muestra el gráfico. | 4 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 7 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 1, 2 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 4 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 4 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Simulamos el alojamiento nuevo: solo 120 reservas para entrenar, el resto para evaluar.

```python
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, RidgeCV, LassoCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.base import clone

warnings.filterwarnings("ignore", category=UserWarning)
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)
df["pais_origen"] = df["pais_origen"].fillna("desconocido")

columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especiales",
                "cliente_repetidor", "cancelaciones_previas", "mes_llegada", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["precio_noche"]

# Simulamos el alojamiento nuevo: solo 120 reservas para entrenar, el resto para evaluar
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=120, random_state=SEMILLA)
print("Reservas para entrenar:", len(X_train), "· para evaluar:", len(X_test))

prep = ColumnTransformer([("num", StandardScaler(), columnas_num),
                          ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), columnas_cat)])
```

**Qué hace cada línea:**

- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.linear_model import LinearRegression, Ridge, Lasso, RidgeCV, L…` → Trae `LinearRegression`, `Ridge`, `Lasso`, `RidgeCV`, `LassoCV` de `sklearn.linear_model` para poder usarlo.
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder, Polynomial…` → Trae `StandardScaler`, `OneHotEncoder`, `PolynomialFeatures` de `sklearn.preprocessing` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- … y 15 más con las mismas ideas.

### Celda 2 · 1. El problema: muchas variables, pocos datos · 🏫

**Qué hace:** Practica `fit`, `make_pipeline`, `clone`, `PolynomialFeatures` y más (sección «1. El problema: muchas variables, pocos…»).

```python
def modelo_con(regresor):
    """Preprocesado + variables de grado 2 + escalado + regresor."""
    return make_pipeline(clone(prep), PolynomialFeatures(2, include_bias=False), StandardScaler(), regresor)

ols = modelo_con(LinearRegression()).fit(X_train, y_train)
print("Número de columnas del modelo:", ols[-1].coef_.shape[0])
print(f"R² en entrenamiento: {ols.score(X_train, y_train):.3f} · R² en prueba: {ols.score(X_test, y_test):.3f}")
```

**Qué hace cada línea:**

- `def modelo_con(regresor):` → Define la función `modelo_con`: Preprocesado + variables de grado 2 + escalado + regresor.
- `ols = modelo_con(LinearRegression()).fit(X_train, y_train)` → Guarda en `ols` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `modelo_con`: preprocesado + variables de grado 2 + escalado + regresor; `LinearRegression`: modelo de regresión lineal: ajusta una recta (o un plano) a los datos.
- `print("Número de columnas del modelo:", ols[-1].coef_.shape[0])` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- `print(f"R² en entrenamiento: {ols.score(X_train, y_train):.3f} · R² en prue…` → `print`: muestra un valor por pantalla; `score`: calcula la nota del modelo con la métrica por defecto.

### Celda 3 · 1. El problema: muchas variables, pocos datos · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Ridge (L2): encoger los coeficientes · 🏫

**Qué hace:** Practica `fit_transform`, `get_feature_names_out`, `logspace`, `array` y más (sección «2. Ridge (L2): encoger los coeficientes»).

```python
Xp_train = prep.fit_transform(X_train)
nombres = prep.get_feature_names_out()
alphas = np.logspace(-2, 3, 30)
trayectoria_ridge = np.array([Ridge(alpha=a).fit(Xp_train, y_train).coef_ for a in alphas])
trayectoria_lasso = np.array([Lasso(alpha=a, max_iter=50000).fit(Xp_train, y_train).coef_ for a in alphas])

fig, ejes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)
for ax, tray, titulo in [(ejes[0], trayectoria_ridge, "Ridge (L2): los coeficientes se encogen"),
                         (ejes[1], trayectoria_lasso, "Lasso (L1): los coeficientes llegan a cero")]:
    ax.plot(alphas, tray, lw=1)
    ax.set_xscale("log")
    ax.set(title=titulo, xlabel="alpha (escala logarítmica)")
    ax.axhline(0, color="black", lw=0.8)
ejes[0].set_ylabel("Valor del coeficiente (€)")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `Xp_train = prep.fit_transform(X_train)` → Guarda en `Xp_train` el resultado. `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `nombres = prep.get_feature_names_out()` → Guarda en `nombres` el resultado. `get_feature_names_out`: devuelve los nombres de las columnas después del preprocesado.
- `alphas = np.logspace(-2, 3, 30)` → Guarda en `alphas` el resultado. `logspace`: crea una secuencia de números espaciados en escala logarítmica.
- `trayectoria_ridge = np.array([Ridge(alpha=a).fit(Xp_train, y_train).coef_ f…` → Guarda en `trayectoria_ridge` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez); `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `Ridge`: regresión lineal con penalización L2 (encoge los coeficientes).
- `trayectoria_lasso = np.array([Lasso(alpha=a, max_iter=50000).fit(Xp_train,…` → Guarda en `trayectoria_lasso` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez); `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `Lasso`: regresión lineal con penalización L1 (puede dejar coeficientes en 0).
- `fig, ejes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for ax, tray, titulo in [(ejes[0], trayectoria_ridge, "Ridge (L2): los coef…` → Repite el bloque de debajo para cada valor de `ax, tray, titulo` en `[(ejes[0], trayectoria_ridge, "Ridge (L…`. Dentro del bloque: `plot`: dibuja una línea (o puntos unidos); `set_xscale`: cambia la escala del eje horizontal (por ejemplo, logarítmica); `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `ejes[0].set_ylabel("Valor del coeficiente (€)")` → `set_ylabel`: pone el nombre del eje vertical.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- … y 1 más con las mismas ideas.

### Celda 5 · 3. Elegir `alpha` con validación cruzada · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 4. Lasso (L1): seleccionar variables · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4. Lasso (L1): seleccionar variables · 🏫

**Qué hace:** ¿Qué variables ha conservado Lasso? (las de mayor peso).

```python
# ¿Qué variables ha conservado Lasso? (las de mayor peso)
nombres_poly = lasso[:-1].get_feature_names_out()
coef_lasso = pd.Series(lasso[-1].coef_, index=nombres_poly)
principales = coef_lasso[coef_lasso != 0].sort_values(key=np.abs, ascending=False).head(8)
principales.round(2)
```

**Qué hace cada línea:**

- `nombres_poly = lasso[:-1].get_feature_names_out()` → Guarda en `nombres_poly` el resultado. `get_feature_names_out`: devuelve los nombres de las columnas después del preprocesado.
- `coef_lasso = pd.Series(lasso[-1].coef_, index=nombres_poly)` → Guarda en `coef_lasso` el resultado. `Series`: crea una columna de pandas (una sola serie de valores).
- `principales = coef_lasso[coef_lasso != 0].sort_values(key=np.abs, ascending…` → Guarda en `principales` el resultado. `head`: muestra las primeras filas; `sort_values`: ordena la tabla por una o varias columnas.
- `principales.round(2)` → `round`: redondea un número a los decimales indicados.

### Celda 8 · 5. Comparativa final · 🏠

**Qué hace:** Practica `round`, `DataFrame`, `score` (sección «5. Comparativa final»).

```python
comparativa = pd.DataFrame({
    "R² train": [ols.score(X_train, y_train), ridge.score(X_train, y_train), lasso.score(X_train, y_train)],
    "R² test": [r2_test_ols, r2_test_ridge, r2_test_lasso],
}, index=["Sin regularizar", "Ridge", "Lasso"]).round(3)
comparativa
```

**Qué hace cada línea:**

- `comparativa = pd.DataFrame({` → Guarda en `comparativa` el resultado. `round`: redondea un número a los decimales indicados; `DataFrame`: crea una tabla de pandas (filas y columnas); `score`: calcula la nota del modelo con la métrica por defecto.

### Celda 9 · 6. Mini-reto: ¿cuántos datos hacen falta? · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S07_02_ridge_lasso.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
