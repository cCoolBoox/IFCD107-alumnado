# Código explicado · S07.04 · Curvas ROC y PR, y qué hacer con clases desbalanceadas

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_04_roc_pr_desbalance.ipynb) · [descargar](../notebooks/S07_04_roc_pr_desbalance.ipynb) · ⏱ en clase: 25 min · 🏫 2 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Escenario simulado: conservamos todas las no canceladas y una parte de las canceladas (≈… |
| 3 | 2. Curva ROC y AUC | Practica `fit`, `predict_proba` (sección «2. Curva ROC y AUC»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `neg` | `df[df["cancelada"] == 0]` | 1 |
| `pos` | `df[df["cancelada"] == 1].sample(n=int(len(neg) * 0.064),…` | 1 |
| `raro` | `pd.concat([neg, pos]).sample(frac=1, random_state=SEMILLA…` | 1 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 1 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 1 |
| `prep` | `ColumnTransformer([ ("num", Pipeline([("imp", SimpleImput…` | 1 |
| `base` | `nuevo_modelo().fit(X_train, y_train)` | 3 |
| `proba_base` | `base.predict_proba(X_test)[:, 1]` | 3 |
| `ap` | `average_precision_score(y_test, proba_base)` | 5 |
| `prevalencia` | `y_test.mean()` | 5 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `nuevo_modelo` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1 |
| `average_precision_score` | Resumen de la curva precisión–sensibilidad en un solo número. | 5 |
| `axhline` | Dibuja una línea horizontal de referencia. | 5 |
| `clone` | Crea una copia del modelo con los mismos ajustes pero sin entrenar. | 1 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `concat` | Pega tablas una debajo de otra (o una al lado de otra). | 1 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 5 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 3 |
| `int` | Convierte un valor en número entero. | 1 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `legend` | Muestra la leyenda del gráfico. | 5 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 1 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 1 |
| `mean` | Calcula la media. | 1, 5 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 1 |
| `plot` | Dibuja una línea (o puntos unidos). | 5 |
| `precision_recall_curve` | Calcula los puntos de la curva precisión–sensibilidad. | 5 |
| `predict_proba` | Pide la probabilidad de cada clase (no solo la clase). | 3 |
| `print` | Muestra un valor por pantalla. | 1 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `reset_index` | Devuelve el índice de la tabla a 0, 1, 2… | 1 |
| `sample` | Elige varios elementos al azar sin repetir. | 1 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `show` | Muestra el gráfico. | 5 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 1 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 1 |
| `sum` | Suma todos los valores. | 1 |
| `title` | Pone el título del gráfico. | 5 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |
| `xlabel` | Pone el nombre del eje horizontal. | 5 |
| `ylabel` | Pone el nombre del eje vertical. | 5 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Escenario simulado: conservamos todas las no canceladas y una parte de las canceladas (≈ 6 %).

```python
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.utils import resample
from sklearn.base import clone
from sklearn.metrics import (roc_curve, roc_auc_score, precision_recall_curve, average_precision_score,
                             precision_score, recall_score, accuracy_score)

warnings.filterwarnings("ignore", category=UserWarning)
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)

# Escenario simulado: conservamos todas las no canceladas y una parte de las canceladas (≈ 6 %)
neg = df[df["cancelada"] == 0]
pos = df[df["cancelada"] == 1].sample(n=int(len(neg) * 0.064), random_state=SEMILLA)
raro = pd.concat([neg, pos]).sample(frac=1, random_state=SEMILLA).reset_index(drop=True)
print(f"Reservas: {len(raro)} · canceladas: {raro['cancelada'].sum()} ({raro['cancelada'].mean():.1%})")

columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = raro[columnas_num + columnas_cat], raro["cancelada"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEMILLA, stratify=y)

prep = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore"))]), columnas_cat),
])

def nuevo_modelo(**kwargs):
    # clone(prep): cada modelo necesita su propia copia del preprocesado (si no, se pisarían entre sí)
    return Pipeline([("prep", clone(prep)), ("clf", LogisticRegression(max_iter=1000, **kwargs))])
```

**Qué hace cada línea:**

- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split, cross_val_predict, St…` → Trae `train_test_split`, `cross_val_predict`, `StratifiedKFold` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.linear_model import LogisticRegression` → Trae `LogisticRegression` de `sklearn.linear_model` para poder usarlo.
- `from sklearn.dummy import DummyClassifier` → Trae `DummyClassifier` de `sklearn.dummy` para poder usarlo.
- `from sklearn.impute import SimpleImputer` → Trae `SimpleImputer` de `sklearn.impute` para poder usarlo.
- … y 21 más con las mismas ideas.

### Celda 2 · 1. La paradoja de la exactitud · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 3 · 2. Curva ROC y AUC · 🏫

**Qué hace:** Practica `fit`, `predict_proba` (sección «2. Curva ROC y AUC»).

```python
base = nuevo_modelo().fit(X_train, y_train)
proba_base = base.predict_proba(X_test)[:, 1]
```

**Qué hace cada línea:**

- `base = nuevo_modelo().fit(X_train, y_train)` → Guarda en `base` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `nuevo_modelo`: función definida en el cuaderno.
- `proba_base = base.predict_proba(X_test)[:, 1]` → Guarda en `proba_base` el resultado. `predict_proba`: pide la probabilidad de cada clase (no solo la clase).

### Celda 4 · 2. Curva ROC y AUC · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 3. Curva precisión–recall (PR) y *average preci… · 🏠

**Qué hace:** Practica `precision_recall_curve`, `average_precision_score`, `mean`, `figure` y más (sección «3. Curva precisión–recall (PR) y *avera…»).

```python
prec, rec, _ = precision_recall_curve(y_test, proba_base)
ap = average_precision_score(y_test, proba_base)
prevalencia = y_test.mean()
plt.figure(figsize=(5.5, 5))
plt.plot(rec, prec, color="#2a6f97", lw=2, label=f"Regresión logística (AP = {ap:.2f})")
plt.axhline(prevalencia, ls="--", color="gray", label=f"Azar (= prevalencia {prevalencia:.2f})")
plt.title("Curva precisión–recall")
plt.xlabel("Recall (cancelaciones detectadas)")
plt.ylabel("Precisión (alarmas acertadas)")
plt.legend()
plt.show()
```

**Qué hace cada línea:**

- `prec, rec, _ = precision_recall_curve(y_test, proba_base)` → Guarda en `prec, rec, _` el resultado. `precision_recall_curve`: calcula los puntos de la curva precisión–sensibilidad.
- `ap = average_precision_score(y_test, proba_base)` → Guarda en `ap` el resultado. `average_precision_score`: resumen de la curva precisión–sensibilidad en un solo número.
- `prevalencia = y_test.mean()` → Guarda en `prevalencia` el resultado. `mean`: calcula la media.
- `plt.figure(figsize=(5.5, 5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.plot(rec, prec, color="#2a6f97", lw=2, label=f"Regresión logística (AP…` → `plot`: dibuja una línea (o puntos unidos).
- `plt.axhline(prevalencia, ls="--", color="gray", label=f"Azar (= prevalencia…` → `axhline`: dibuja una línea horizontal de referencia.
- `plt.title("Curva precisión–recall")` → `title`: pone el título del gráfico.
- `plt.xlabel("Recall (cancelaciones detectadas)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("Precisión (alarmas acertadas)")` → `ylabel`: pone el nombre del eje vertical.
- … y 2 más con las mismas ideas.

### Celda 6 · 3. Curva precisión–recall (PR) y *average preci… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4. Tres remedios para el desbalance · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4. Tres remedios para el desbalance · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5. Ajustar el umbral con la curva PR · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 6. Mini-reto: comparativa de estrategias · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S07_04_roc_pr_desbalance.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
