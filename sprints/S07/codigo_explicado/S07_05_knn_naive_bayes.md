# Código explicado · S07.05 · k vecinos (k-NN) y Naive Bayes

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_05_knn_naive_bayes.ipynb) · [descargar](../notebooks/S07_05_knn_naive_bayes.ipynb) · ⏱ en clase: 40 min · 🏫 0 celdas de código en clase · 🏠 2 en casa
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
| `cv` | `StratifiedKFold(5, shuffle=True, random_state=SEMILLA)` | 1 |
| `rng` | `np.random.default_rng(SEMILLA)` | 2 |
| `numericas` | `df[columnas_num].copy()` | 2 |
| `sin_escalar` | `reparto_distancia(numericas)` | 2 |
| `escalado` | `reparto_distancia(pd.DataFrame(StandardScaler().fit_trans…` | 2 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `prep_onehot` | Imputar + escalar (numéricas) e imputar + one-hot denso (categóricas). |
| `reparto_distancia` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1 |
| `columns` | Nombres de las columnas. | 2 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `copy` | Hace una copia independiente (si cambias la copia, el original no cambia). | 2 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 2 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 2 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 2 |
| `iloc` | Selecciona filas/columnas por su posición. | 2 |
| `integers` | Genera números enteros aleatorios. | 2 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2 |
| `mean` | Calcula la media. | 2 |
| `mul` | Multiplica cada valor por un número (aquí, para pasar de proporción a porcentaje). | 2 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 1 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `round` | Redondea un número a los decimales indicados. | 2 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 2 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 1 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 1, 2 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 1 |
| `sum` | Suma todos los valores. | 2 |
| `to_numpy` | Convierte una tabla o columna de pandas en un array de NumPy. | 2 |

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
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, CategoricalNB
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, KBinsDiscretizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)
columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["cancelada"]
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)


def prep_onehot():
    """Imputar + escalar (numéricas) e imputar + one-hot denso (categóricas)."""
    return ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), columnas_num),
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
- `from sklearn.model_selection import StratifiedKFold, cross_val_score, train…` → Trae `StratifiedKFold`, `cross_val_score`, `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.neighbors import KNeighborsClassifier` → Trae `KNeighborsClassifier` de `sklearn.neighbors` para poder usarlo.
- `from sklearn.naive_bayes import GaussianNB, CategoricalNB` → Trae `GaussianNB`, `CategoricalNB` de `sklearn.naive_bayes` para poder usarlo.
- … y 16 más con las mismas ideas.

### Celda 2 · 1. k-NN: predecir mirando a los vecinos · 🏠

**Qué hace:** ¿Qué variable manda en la distancia? Comparamos qué % de la distancia² entre pares aporta cada una.

```python
# ¿Qué variable manda en la distancia? Comparamos qué % de la distancia² entre pares aporta cada una
rng = np.random.default_rng(SEMILLA)
numericas = df[columnas_num].copy()
def reparto_distancia(tabla, n_pares=3000):
    i = rng.integers(0, len(tabla), n_pares)
    j = rng.integers(0, len(tabla), n_pares)
    cuadrados = (tabla.iloc[i].to_numpy() - tabla.iloc[j].to_numpy()) ** 2
    return pd.Series(cuadrados.mean(axis=0) / cuadrados.mean(axis=0).sum(), index=tabla.columns)

sin_escalar = reparto_distancia(numericas)
escalado = reparto_distancia(pd.DataFrame(StandardScaler().fit_transform(numericas), columns=columnas_num))
pd.DataFrame({"sin escalar": sin_escalar, "escaladas": escalado}).mul(100).round(1)
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `numericas = df[columnas_num].copy()` → Guarda en `numericas` el resultado. `copy`: hace una copia independiente (si cambias la copia, el original no cambia).
- `def reparto_distancia(tabla, n_pares=3000):` → Define la función `reparto_distancia`: Función definida en el cuaderno.
- `sin_escalar = reparto_distancia(numericas)` → Guarda en `sin_escalar` el resultado. `reparto_distancia`: función definida en el cuaderno.
- `escalado = reparto_distancia(pd.DataFrame(StandardScaler().fit_transform(nu…` → Guarda en `escalado` el resultado. `reparto_distancia`: función definida en el cuaderno; `DataFrame`: crea una tabla de pandas (filas y columnas); `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `pd.DataFrame({"sin escalar": sin_escalar, "escaladas": escalado}).mul(100).…` → `round`: redondea un número a los decimales indicados; `mul`: multiplica cada valor por un número (aquí, para pasar de proporción a porcentaje); `DataFrame`: crea una tabla de pandas (filas y columnas).

### Celda 3 · 1. k-NN: predecir mirando a los vecinos · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Elegir `k` · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 3. Naive Bayes: probabilidades multiplicadas · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Naive Bayes: probabilidades multiplicadas · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4. Mini-reto: ¿qué modelo para el equipo de res… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S07_05_knn_naive_bayes.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
