# Código explicado · S08.03 · Boosting: Gradient Boosting, XGBoost y LightGBM

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_03_boosting_xgboost_lightgbm.ipynb) · [descargar](../notebooks/S08_03_boosting_xgboost_lightgbm.ipynb) · ⏱ en clase: 25 min · 🏫 1 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Para la parada temprana necesitamos un conjunto de VALIDACIÓN aparte (sacado de train, no… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 1 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 1 |
| `prep` | `ColumnTransformer([ ("num", SimpleImputer(strategy="media…` | 1 |
| `Xtr` | `prep.fit_transform(X_train)` | 1 |
| `Xte` | `prep.transform(X_test)` | 1 |
| `nombres` | `prep.get_feature_names_out()` | 1 |
| `gb` | `GradientBoostingClassifier(n_estimators=300, learning_rat…` | 2 |
| `auc_val_por_arbol` | `[roc_auc_score(yval, p[:, 1]) for p in gb.staged_predict_…` | 2 |
| `auc_fit_por_arbol` | `[roc_auc_score(yfit, p[:, 1]) for p in gb.staged_predict_…` | 2 |
| `imp` | `pd.Series(modelo_xgb.feature_importances_, index=nombres)…` | 6 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 2, 6 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 2 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 1 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 1 |
| `GradientBoostingClassifier` | Árboles en cadena, cada uno corrige los fallos del anterior. | 2 |
| `head` | Muestra las primeras filas. | 6 |
| `iloc` | Selecciona filas/columnas por su posición. | 6 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `legend` | Muestra la leyenda del gráfico. | 2 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 1 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 1 |
| `plot` | Dibuja una línea (o puntos unidos). | 2, 6 |
| `print` | Muestra un valor por pantalla. | 1 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 2 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `roc_auc_score` | Calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar). | 2 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 6 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `show` | Muestra el gráfico. | 2, 6 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 1 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 6 |
| `staged_predict_proba` | Da las probabilidades del boosting después de cada árbol añadido (para ver cuándo deja de mejorar). | 2 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 6 |
| `title` | Pone el título del gráfico. | 2, 6 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 1 |
| `xlabel` | Pone el nombre del eje horizontal. | 2, 6 |
| `ylabel` | Pone el nombre del eje vertical. | 2, 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Para la parada temprana necesitamos un conjunto de VALIDACIÓN aparte (sacado de train, no del test).

```python
import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
import xgboost as xgb
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

prep = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), columnas_cat),
])
Xtr = prep.fit_transform(X_train)
Xte = prep.transform(X_test)
nombres = prep.get_feature_names_out()

# Para la parada temprana necesitamos un conjunto de VALIDACIÓN aparte (sacado de train, no del test)
Xfit, Xval, yfit, yval = train_test_split(Xtr, y_train, test_size=0.2, random_state=SEMILLA, stratify=y_train)
print("Entrenar:", len(Xfit), "· validar:", len(Xval), "· probar (test, intacto):", len(Xte))
```

**Qué hace cada línea:**

- `import time` → Trae `time` para poder usarlo.
- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.ensemble import GradientBoostingClassifier` → Trae `GradientBoostingClassifier` de `sklearn.ensemble` para poder usarlo.
- `from sklearn.impute import SimpleImputer` → Trae `SimpleImputer` de `sklearn.impute` para poder usarlo.
- … y 21 más con las mismas ideas.

### Celda 2 · 2. Sobreajuste por exceso de árboles · 🏠

**Qué hace:** Practica `fit`, `figure`, `plot`, `title` y más (sección «2. Sobreajuste por exceso de árboles»).

```python
gb = GradientBoostingClassifier(n_estimators=300, learning_rate=0.2, max_depth=3, random_state=SEMILLA).fit(Xfit, yfit)
auc_val_por_arbol = [roc_auc_score(yval, p[:, 1]) for p in gb.staged_predict_proba(Xval)]
auc_fit_por_arbol = [roc_auc_score(yfit, p[:, 1]) for p in gb.staged_predict_proba(Xfit)]
plt.figure(figsize=(8, 4))
plt.plot(range(1, 301), auc_fit_por_arbol, label="Entrenamiento")
plt.plot(range(1, 301), auc_val_por_arbol, label="Validación")
plt.title("Gradient Boosting: AUC según el número de árboles")
plt.xlabel("Número de árboles")
plt.ylabel("AUC")
plt.legend()
plt.show()
```

**Qué hace cada línea:**

- `gb = GradientBoostingClassifier(n_estimators=300, learning_rate=0.2, max_de…` → Guarda en `gb` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `GradientBoostingClassifier`: árboles en cadena, cada uno corrige los fallos del anterior.
- `auc_val_por_arbol = [roc_auc_score(yval, p[:, 1]) for p in gb.staged_predic…` → Guarda en `auc_val_por_arbol` el resultado. `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar); `staged_predict_proba`: da las probabilidades del boosting después de cada árbol añadido (para ver cuándo deja de mejorar).
- `auc_fit_por_arbol = [roc_auc_score(yfit, p[:, 1]) for p in gb.staged_predic…` → Guarda en `auc_fit_por_arbol` el resultado. `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar); `staged_predict_proba`: da las probabilidades del boosting después de cada árbol añadido (para ver cuándo deja de mejorar).
- `plt.figure(figsize=(8, 4))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.plot(range(1, 301), auc_fit_por_arbol, label="Entrenamiento")` → `plot`: dibuja una línea (o puntos unidos); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `plt.plot(range(1, 301), auc_val_por_arbol, label="Validación")` → `plot`: dibuja una línea (o puntos unidos); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `plt.title("Gradient Boosting: AUC según el número de árboles")` → `title`: pone el título del gráfico.
- `plt.xlabel("Número de árboles")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("AUC")` → `ylabel`: pone el nombre del eje vertical.
- … y 2 más con las mismas ideas.

### Celda 3 · 2. Sobreajuste por exceso de árboles · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3. XGBoost · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 4. LightGBM · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 5. Qué mira el modelo · 🏠

**Qué hace:** Practica `head`, `figure`, `plot`, `title` y más (sección «5. Qué mira el modelo»).

```python
imp = pd.Series(modelo_xgb.feature_importances_, index=nombres).sort_values(ascending=False).head(8)
plt.figure(figsize=(7, 4))
imp.iloc[::-1].plot(kind="barh", color="#2a6f97")
plt.title("XGBoost: importancia de variables (top 8)")
plt.xlabel("Importancia (ganancia relativa)")
plt.ylabel("")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `imp = pd.Series(modelo_xgb.feature_importances_, index=nombres).sort_values…` → Guarda en `imp` el resultado. `head`: muestra las primeras filas; `sort_values`: ordena la tabla por una o varias columnas; `Series`: crea una columna de pandas (una sola serie de valores).
- `plt.figure(figsize=(7, 4))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `imp.iloc[::-1].plot(kind="barh", color="#2a6f97")` → `plot`: dibuja una línea (o puntos unidos); `iloc`: selecciona filas/columnas por su posición.
- `plt.title("XGBoost: importancia de variables (top 8)")` → `title`: pone el título del gráfico.
- `plt.xlabel("Importancia (ganancia relativa)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("")` → `ylabel`: pone el nombre del eje vertical.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 7 · 6. Mini-reto: comparativa de las tres implement… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S08_03_boosting_xgboost_lightgbm.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
