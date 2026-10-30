# Código explicado · S08.06 · Plantilla del *leaderboard* interno («Duelo de modelos»)

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_06_leaderboard_plantilla.ipynb) · [descargar](../notebooks/S08_06_leaderboard_plantilla.ipynb) · 🏫 5 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `filterwarnings`, `set_theme`. |
| 2 | 1. Datos y partición | Practica `read_csv`, `astype`, `train_test_split`, `StratifiedKFold` y más (sección «1. D… |
| 3 | 2. Herramientas del leaderboard (no mod… | Practica `ColumnTransformer`, `Pipeline`, `cross_validate`, `fit` y más (sección «2. Herr… |
| 6 | 5. Rendimiento frente a explicabilidad… | Practica `figure`, `scatter`, `iterrows`, `xscale` y más (sección «5. Rendimiento frente… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `RUTA_CSV` | `"leaderboard_S08.csv"` | 1 |
| `REINICIAR` | `True` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 2 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 2 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 2 |
| `cv` | `StratifiedKFold(5, shuffle=True, random_state=SEMILLA)` | 2 |
| `escenarios` | `{"solo rendimiento": {"rendimiento": 0.8, "explicabilidad…` | 8 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `hacer_pipe` | Preprocesado estándar (imputar + one-hot; escalar si el modelo lo necesita) + clasificador. |
| `evaluar_modelo` | Mide un modelo con validación cruzada sobre train y devuelve una fila del leaderboard. |
| `registrar` | Añade o actualiza una fila (por nombre de modelo) en el CSV y devuelve la tabla ordenada por AUC. |
| `puntuacion_global` | Puntuación 0-1 = rendimiento (AUC), explicabilidad y coste (tiempo + tamaño), normalizados y ponderados. |
| `actualizar_test` | Guarda el AUC de test del campeón en el leaderboard (solo debe llamarse UNA vez). *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `annotate` | Escribe una nota con flecha en el gráfico. | 6 |
| `assign` | Añade columnas nuevas sin modificar la tabla original. | 3 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 2 |
| `clip` | Limita los valores a un mínimo y un máximo. | 6 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 3 |
| `concat` | Pega tablas una debajo de otra (o una al lado de otra). | 3 |
| `cross_validate` | Validación cruzada que devuelve varias métricas y tiempos. | 3 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 3, 8 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 2 |
| `dumps` | Convierte datos de Python en texto JSON. | 3 |
| `exists` | Comprueba si un fichero o carpeta existe. | 3 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 6 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 3 |
| `head` | Muestra las primeras filas. | 3 |
| `iloc` | Selecciona filas/columnas por su posición. | 3, 8 |
| `isin` | Marca los valores que están en una lista. | 2 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 8 |
| `iterrows` | Recorre la tabla fila a fila. | 6 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2, 3 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 3 |
| `log1p` | Logaritmo de (1 + x); sirve para valores que pueden ser 0. | 3 |
| `max` | Devuelve el valor más grande. | 3 |
| `mean` | Calcula la media. | 3 |
| `min` | Devuelve el valor más pequeño. | 3 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 3 |
| `perf_counter` | Reloj de precisión para medir cuánto tarda un trozo de código. | 3 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 3 |
| `predict_proba` | Pide la probabilidad de cada clase (no solo la clase). | 3 |
| `print` | Muestra un valor por pantalla. | 2, 3 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2, 3 |
| `remove` | Quita un elemento concreto. | 3 |
| `reset_index` | Devuelve el índice de la tabla a 0, 1, 2… | 3 |
| `round` | Redondea un número a los decimales indicados. | 3 |
| `scatter` | Dibuja un gráfico de puntos. | 6 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 3 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `show` | Muestra el gráfico. | 6 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 3 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 3 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 3 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 3 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 2 |
| `title` | Pone el título del gráfico. | 6 |
| `to_csv` | Guarda la tabla en un fichero CSV. | 3 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 2 |
| `xlabel` | Pone el nombre del eje horizontal. | 6 |
| `xscale` | Cambia la escala del eje horizontal (por ejemplo, logarítmica). | 6 |
| `ylabel` | Pone el nombre del eje vertical. | 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `filterwarnings`, `set_theme`.

```python
import os
import pickle
import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, average_precision_score
import xgboost as xgb
import lightgbm as lgb

warnings.filterwarnings("ignore")
SEMILLA = 42
sns.set_theme(style="whitegrid")

RUTA_CSV = "leaderboard_S08.csv"     # el leaderboard se guarda aquí (en la carpeta del notebook)
REINICIAR = True                      # True = empieza de cero al ejecutar todo; False = conserva lo registrado
```

**Qué hace cada línea:**

- `import os` → Trae `os` para poder usarlo.
- `import pickle` → Trae `pickle` para poder usarlo.
- `import time` → Trae `time` para poder usarlo.
- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split, StratifiedKFold, cros…` → Trae `train_test_split`, `StratifiedKFold`, `cross_validate` de `sklearn.model_selection` para poder usarlo.
- … y 17 más con las mismas ideas.

### Celda 2 · 1. Datos y partición · 🏫

**Qué hace:** Practica `read_csv`, `astype`, `train_test_split`, `StratifiedKFold` y más (sección «1. Datos y partición»).

```python
df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)
columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["cancelada"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)
print(f"Train: {len(X_train)} · Test (intacto hasta el final): {len(X_test)}")
```

**Qué hace cada línea:**

- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserv…` → Guarda en `df` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12…` → Guarda en `df["temporada_alta"]` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `isin`: marca los valores que están en una lista; `dt`: da acceso a las operaciones de fecha sobre una columna.
- `columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_no…` → Guarda el valor en `columnas_num`.
- `columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tari…` → Guarda el valor en `columnas_cat`.
- `X, y = df[columnas_num + columnas_cat], df["cancelada"]` → Guarda el valor en `X, y`.
- `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, ra…` → Guarda en `X_train, X_test, y_trai…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)` → Guarda en `cv` el resultado. `StratifiedKFold`: crea particiones de validación cruzada que mantienen la proporción de clases.
- `print(f"Train: {len(X_train)} · Test (intacto hasta el final): {len(X_test)…` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.

### Celda 3 · 2. Herramientas del leaderboard (no modificar) · 🏫

**Qué hace:** Practica `ColumnTransformer`, `Pipeline`, `cross_validate`, `fit` y más (sección «2. Herramientas del leaderboard (no mod…»).

```python
def hacer_pipe(clasificador, escalar=False):
    """Preprocesado estándar (imputar + one-hot; escalar si el modelo lo necesita) + clasificador."""
    num = [("imp", SimpleImputer(strategy="median"))] + ([("esc", StandardScaler())] if escalar else [])
    prep = ColumnTransformer([
        ("num", Pipeline(num), columnas_num),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), columnas_cat),
    ])
    return Pipeline([("prep", prep), ("clf", clasificador)])


def evaluar_modelo(nombre, familia, pipe, explicabilidad, notas=""):
    """Mide un modelo con validación cruzada sobre train y devuelve una fila del leaderboard."""
    res = cross_validate(pipe, X_train, y_train, cv=cv, scoring=["roc_auc", "average_precision"], n_jobs=1)
    pipe.fit(X_train, y_train)
    muestra = X_train.head(1000)
    t0 = time.perf_counter()
    pipe.predict_proba(muestra)
    ms_pred = (time.perf_counter() - t0) * 1000 * (1000 / len(muestra))
    return {
        "modelo": nombre, "familia": familia,
        "auc_cv_media": round(res["test_roc_auc"].mean(), 4), "auc_cv_desv": round(res["test_roc_auc"].std(), 4),
        "ap_cv_media": round(res["test_average_precision"].mean(), 4),
        "seg_ajuste": round(res["fit_time"].mean(), 3), "ms_pred_1000": round(ms_pred, 1),
        "tamano_kb": round(len(pickle.dumps(pipe)) / 1024, 1),
        "explicabilidad_1a5": explicabilidad, "notas": notas, "auc_test": np.nan,
    }


def registrar(fila):
    """Añade o actualiza una fila (por nombre de modelo) en el CSV y devuelve la tabla ordenada por AUC."""
    tabla = pd.read_csv(RUTA_CSV) if os.path.exists(RUTA_CSV) else pd.DataFrame()
    if len(tabla) and fila["modelo"] in set(tabla["modelo"]):
        conservar = tabla.loc[tabla["modelo"] == fila["modelo"], "auc_test"].iloc[0]
        fila = {**fila, "auc_test": conservar}
        tabla = tabla[tabla["modelo"] != fila["modelo"]]
    tabla = pd.concat([tabla, pd.DataFrame([fila])], ignore_index=True)
    tabla = tabla.sort_values("auc_cv_media", ascending=False).reset_index(drop=True)
    tabla.to_csv(RUTA_CSV, index=False)
    return tabla


def puntuacion_global(lb, pesos):
    """Puntuación 0-1 = rendimiento (AUC), explicabilidad y coste (tiempo + tamaño), normalizados y ponderados."""
    rend = (lb["auc_cv_media"] - lb["auc_cv_media"].min()) / (lb["auc_cv_media"].max() - lb["auc_cv_media"].min() + 1e-9)
    expl = (lb["explicabilidad_1a5"] - 1) / 4
    coste_bruto = np.log1p(lb["seg_ajuste"]) + np.log1p(lb["ms_pred_1000"]) + np.log1p(lb["tamano_kb"])
    coste = 1 - (coste_bruto - coste_bruto.min()) / (coste_bruto.max() - coste_bruto.min() + 1e-9)   # 1 = barato
    total = pesos["rendimiento"] * rend + pesos["explicabilidad"] * expl + pesos["coste"] * coste
    return lb.assign(punt_rendimiento=rend.round(3), punt_explicabilidad=expl.round(3),
                     punt_coste=coste.round(3), puntuacion_global=total.round(3)).sort_values("puntuacion_global", ascending=False)


if REINICIAR and os.path.exists(RUTA_CSV):
    os.remove(RUTA_CSV)
print("Herramientas listas. Leaderboard en:", RUTA_CSV)
```

**Qué hace cada línea:**

- `def hacer_pipe(clasificador, escalar=False):` → Define la función `hacer_pipe`: Preprocesado estándar (imputar + one-hot; escalar si el modelo lo necesita) + clasificador.
- `def evaluar_modelo(nombre, familia, pipe, explicabilidad, notas=""):` → Define la función `evaluar_modelo`: Mide un modelo con validación cruzada sobre train y devuelve una fila del leaderboard.
- `def registrar(fila):` → Define la función `registrar`: Añade o actualiza una fila (por nombre de modelo) en el CSV y devuelve la tabla ordenada por AUC.
- `def puntuacion_global(lb, pesos):` → Define la función `puntuacion_global`: Puntuación 0-1 = rendimiento (AUC), explicabilidad y coste (tiempo + tamaño), normalizados y ponderados.
- `if REINICIAR and os.path.exists(RUTA_CSV):` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `remove`: quita un elemento concreto.
- `print("Herramientas listas. Leaderboard en:", RUTA_CSV)` → `print`: muestra un valor por pantalla.

### Celda 4 · 3. Registrar el baseline y el modelo lineal · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 4. Registrar los contendientes del duelo · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 5. Rendimiento frente a explicabilidad y coste · 🏫

**Qué hace:** Practica `figure`, `scatter`, `iterrows`, `xscale` y más (sección «5. Rendimiento frente a explicabilidad…»).

```python
plt.figure(figsize=(8, 4.5))
plt.scatter(lb["seg_ajuste"], lb["auc_cv_media"], s=lb["tamano_kb"].clip(lower=5) * 1.2, alpha=0.6, color="#2a6f97")
for _, f in lb.iterrows():
    plt.annotate(f["modelo"], (f["seg_ajuste"], f["auc_cv_media"]), textcoords="offset points", xytext=(6, 4), fontsize=9)
plt.xscale("log")
plt.title("Leaderboard: rendimiento frente a tiempo de ajuste (tamaño del punto = tamaño del modelo)")
plt.xlabel("Segundos de ajuste por fold (escala logarítmica)")
plt.ylabel("AUC (validación cruzada)")
plt.show()
```

**Qué hace cada línea:**

- `plt.figure(figsize=(8, 4.5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.scatter(lb["seg_ajuste"], lb["auc_cv_media"], s=lb["tamano_kb"].clip(lo…` → `scatter`: dibuja un gráfico de puntos; `clip`: limita los valores a un mínimo y un máximo.
- `for _, f in lb.iterrows():` → Repite el bloque de debajo para cada valor de `_, f` en `lb.iterrows()`. Dentro del bloque: `annotate`: escribe una nota con flecha en el gráfico.
- `plt.xscale("log")` → `xscale`: cambia la escala del eje horizontal (por ejemplo, logarítmica).
- `plt.title("Leaderboard: rendimiento frente a tiempo de ajuste (tamaño del p…` → `title`: pone el título del gráfico.
- `plt.xlabel("Segundos de ajuste por fold (escala logarítmica)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("AUC (validación cruzada)")` → `ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 7 · 6. Puntuación global con **tus** pesos · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 6. Puntuación global con **tus** pesos · 🏫

**Qué hace:** Practica `DataFrame`, `items`, `iloc` (sección «6. Puntuación global con **tus** pesos»).

```python
escenarios = {"solo rendimiento": {"rendimiento": 0.8, "explicabilidad": 0.1, "coste": 0.1},
              "equilibrado": {"rendimiento": 0.4, "explicabilidad": 0.4, "coste": 0.2},
              "explicabilidad primero": {"rendimiento": 0.2, "explicabilidad": 0.6, "coste": 0.2}}
pd.DataFrame({nombre: [puntuacion_global(lb, p).iloc[0]["modelo"]] for nombre, p in escenarios.items()},
             index=["campeón"]).T
```

**Qué hace cada línea:**

- `escenarios = {"solo rendimiento": {"rendimiento": 0.8, "explicabilidad": 0.…` → Guarda el valor en `escenarios`.
- `pd.DataFrame({nombre: [puntuacion_global(lb, p).iloc[0]["modelo"]] for nomb…` → `DataFrame`: crea una tabla de pandas (filas y columnas); `items`: devuelve las parejas (clave, valor) de un diccionario; `iloc`: selecciona filas/columnas por su posición.

### Celda 9 · 7. El examen final: solo el campeón, una vez · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S08_06_leaderboard_plantilla.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
