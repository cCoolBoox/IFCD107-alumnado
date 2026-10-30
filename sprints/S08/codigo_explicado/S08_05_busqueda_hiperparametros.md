# Código explicado · S08.05 · Buscar buenos hiperparámetros: GridSearchCV y RandomizedSearchCV

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_05_busqueda_hiperparametros.ipynb) · [descargar](../notebooks/S08_05_busqueda_hiperparametros.ipynb) · ⏱ en clase: 40 min · 🏫 0 celdas de código en clase · 🏠 3 en casa
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
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 1 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 1 |
| `cv` | `StratifiedKFold(3, shuffle=True, random_state=SEMILLA)` | 1 |
| `prep` | `ColumnTransformer([ ("num", SimpleImputer(strategy="media…` | 1 |
| `rng` | `np.random.default_rng(SEMILLA)` | 2 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1, 6 |
| `colorbar` | Añade la barra de colores que explica la escala. | 6 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 2 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 6 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `meshgrid` | Crea una cuadrícula de coordenadas para dibujar o evaluar funciones en 2D. | 2 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 1 |
| `random` | Número aleatorio entre 0 y 1. | 2 |
| `ravel` | Aplana un array a una sola dimensión. | 2 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `scatter` | Dibuja un gráfico de puntos. | 2, 6 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 2 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `show` | Muestra el gráfico. | 2, 6 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 1 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 1 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 2 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 2 |
| `title` | Pone el título del gráfico. | 6 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |
| `xlabel` | Pone el nombre del eje horizontal. | 6 |
| `xscale` | Cambia la escala del eje horizontal (por ejemplo, logarítmica). | 6 |
| `ylabel` | Pone el nombre del eje vertical. | 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏠

**Qué hace:** Practica `filterwarnings`, `set_theme`, `read_csv`, `astype` y más.

```python
import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import randint, loguniform, uniform
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
import lightgbm as lgb

warnings.filterwarnings("ignore")
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)
columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["cancelada"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
cv = StratifiedKFold(3, shuffle=True, random_state=SEMILLA)

prep = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), columnas_cat),
])
```

**Qué hace cada línea:**

- `import time` → Trae `time` para poder usarlo.
- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from scipy.stats import randint, loguniform, uniform` → Trae `randint`, `loguniform`, `uniform` de `scipy.stats` para poder usarlo.
- `from sklearn.model_selection import train_test_split, StratifiedKFold, Grid…` → Trae `train_test_split`, `StratifiedKFold`, `GridSearchCV`, `RandomizedSearchCV` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.ensemble import RandomForestClassifier` → Trae `RandomForestClassifier` de `sklearn.ensemble` para poder usarlo.
- … y 17 más con las mismas ideas.

### Celda 2 · 1. Parámetros frente a hiperparámetros · 🏠

**Qué hace:** Por qué el aleatorio explora mejor: 9 pruebas en rejilla vs 9 al azar (dos hiperparámetros).

```python
# Por qué el aleatorio explora mejor: 9 pruebas en rejilla vs 9 al azar (dos hiperparámetros)
rng = np.random.default_rng(SEMILLA)
gx, gy = np.meshgrid([0.2, 0.5, 0.8], [0.2, 0.5, 0.8])
fig, ejes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
ejes[0].scatter(gx.ravel(), gy.ravel(), color="#2a6f97")
ejes[0].set(title="Rejilla: 9 pruebas, solo 3 valores de cada uno", xlabel="Hiperparámetro importante", ylabel="Hiperparámetro poco importante")
ejes[1].scatter(rng.random(9), rng.random(9), color="#e63946")
ejes[1].set(title="Aleatorio: 9 pruebas, 9 valores de cada uno", xlabel="Hiperparámetro importante")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `gx, gy = np.meshgrid([0.2, 0.5, 0.8], [0.2, 0.5, 0.8])` → Guarda en `gx, gy` el resultado. `meshgrid`: crea una cuadrícula de coordenadas para dibujar o evaluar funciones en 2D.
- `fig, ejes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ejes[0].scatter(gx.ravel(), gy.ravel(), color="#2a6f97")` → `scatter`: dibuja un gráfico de puntos; `ravel`: aplana un array a una sola dimensión.
- `ejes[0].set(title="Rejilla: 9 pruebas, solo 3 valores de cada uno", xlabel=…` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `ejes[1].scatter(rng.random(9), rng.random(9), color="#e63946")` → `scatter`: dibuja un gráfico de puntos; `random`: número aleatorio entre 0 y 1.
- `ejes[1].set(title="Aleatorio: 9 pruebas, 9 valores de cada uno", xlabel="Hi…` → `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 3 · 2. `GridSearchCV` con un bosque aleatorio · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3. `RandomizedSearchCV` con LightGBM · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 4. Leer `cv_results_`: ¿hay un ganador claro? · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 4. Leer `cv_results_`: ¿hay un ganador claro? · 🏠

**Qué hace:** Practica `figure`, `scatter`, `colorbar`, `xscale` y más (sección «4. Leer `cv_results_`: ¿hay un ganador…»).

```python
plt.figure(figsize=(7, 4))
plt.scatter(resultados["param_lgb__learning_rate"].astype(float), resultados["mean_test_score"], c=resultados["param_lgb__num_leaves"].astype(int),
            cmap="viridis", s=50)
plt.colorbar(label="num_leaves")
plt.xscale("log")
plt.title("LightGBM: AUC (validación cruzada) según learning_rate")
plt.xlabel("learning_rate (escala logarítmica)")
plt.ylabel("AUC medio en validación cruzada")
plt.show()
```

**Qué hace cada línea:**

- `plt.figure(figsize=(7, 4))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.scatter(resultados["param_lgb__learning_rate"].astype(float), resultado…` → `scatter`: dibuja un gráfico de puntos; `astype`: cambia el tipo de los datos (por ejemplo, de texto a número).
- `plt.colorbar(label="num_leaves")` → `colorbar`: añade la barra de colores que explica la escala.
- `plt.xscale("log")` → `xscale`: cambia la escala del eje horizontal (por ejemplo, logarítmica).
- `plt.title("LightGBM: AUC (validación cruzada) según learning_rate")` → `title`: pone el título del gráfico.
- `plt.xlabel("learning_rate (escala logarítmica)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("AUC medio en validación cruzada")` → `ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 7 · 5. La nota de la búsqueda es optimista · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 6. Mini-reto: informe de la búsqueda · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S08_05_busqueda_hiperparametros.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
