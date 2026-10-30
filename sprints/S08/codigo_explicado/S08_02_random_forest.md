# Código explicado · S08.02 · Random Forest: la sabiduría de muchos árboles

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_02_random_forest.ipynb) · [descargar](../notebooks/S08_02_random_forest.ipynb) · ⏱ en clase: 30 min · 🏫 3 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `filterwarnings`, `set_theme`, `read_csv`, `astype` y más. |
| 2 | 1. La idea: bagging + variables al azar | Cuántas reservas quedan fuera de una muestra bootstrap: ≈ 36,8 %. |
| 4 | 2. Cuántos árboles y de qué tamaño | oob_decision_function_ contiene la probabilidad OOB de cada reserva de train. |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 1 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 1 |
| `cv` | `StratifiedKFold(5, shuffle=True, random_state=SEMILLA)` | 1 |
| `prep` | `ColumnTransformer([ ("num", SimpleImputer(strategy="media…` | 1 |
| `Xtr` | `prep.fit_transform(X_train)` | 1 |
| `Xte` | `prep.transform(X_test)` | 1 |
| `nombres` | `prep.get_feature_names_out()` | 1 |
| `rng` | `np.random.default_rng(SEMILLA)` | 2 |
| `n` | `5000` | 2 |
| `fuera` | `len(set(range(n)) - set(rng.integers(0, n, n))) / n` | 2 |
| `n_arboles` | `[5, 10, 25, 50, 100, 200, 400]` | 4 |
| `oob_auc` | `[]` | 4 |
| `modelo_bosque` | `Pipeline([("prep", prep), ("rf", RandomForestClassifier(n…` | 6 |
| `perm` | `permutation_importance(modelo_bosque, X_test, y_test, sco…` | 6 |
| `imp_perm` | `pd.Series(perm.importances_mean, index=X_test.columns).so…` | 6 |
| `t0` | `time.perf_counter()` | 8 |
| `t_bosque` | `time.perf_counter() - t0` | 8 |
| `t_arbol` | `time.perf_counter() - t0` | 8 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `append` | Añade un elemento al final de una lista. | 4 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1 |
| `columns` | Nombres de las columnas. | 6 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `DecisionTreeClassifier` | Árbol de decisión para clasificar (reglas «si… entonces…»). | 8 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 2 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 4, 6 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 4, 6, 8 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 1 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 1 |
| `iloc` | Selecciona filas/columnas por su posición. | 6 |
| `integers` | Genera números enteros aleatorios. | 2 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2 |
| `nan_to_num` | Sustituye huecos e infinitos por números. | 4 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `perf_counter` | Reloj de precisión para medir cuánto tarda un trozo de código. | 8 |
| `permutation_importance` | Mide qué variables importan estropeándolas una a una. | 6 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 1, 6 |
| `plot` | Dibuja una línea (o puntos unidos). | 4, 6 |
| `print` | Muestra un valor por pantalla. | 2, 8 |
| `RandomForestClassifier` | Bosque de muchos árboles que votan. | 4, 6, 8 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 2 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `roc_auc_score` | Calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar). | 4 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 6 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 2 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `show` | Muestra el gráfico. | 4, 6 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 1 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 6 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 1 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 6 |
| `title` | Pone el título del gráfico. | 4, 6 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 1 |
| `xlabel` | Pone el nombre del eje horizontal. | 4, 6 |
| `xscale` | Cambia la escala del eje horizontal (por ejemplo, logarítmica). | 4 |
| `ylabel` | Pone el nombre del eje vertical. | 4, 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `filterwarnings`, `set_theme`, `read_csv`, `astype` y más.

```python
import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score

warnings.filterwarnings("ignore", category=UserWarning)
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)
columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["cancelada"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)

prep = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), columnas_cat),
])
Xtr = prep.fit_transform(X_train)
Xte = prep.transform(X_test)
nombres = prep.get_feature_names_out()
```

**Qué hace cada línea:**

- `import time` → Trae `time` para poder usarlo.
- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split, StratifiedKFold, cros…` → Trae `train_test_split`, `StratifiedKFold`, `cross_val_score` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.tree import DecisionTreeClassifier` → Trae `DecisionTreeClassifier` de `sklearn.tree` para poder usarlo.
- `from sklearn.ensemble import RandomForestClassifier` → Trae `RandomForestClassifier` de `sklearn.ensemble` para poder usarlo.
- … y 21 más con las mismas ideas.

### Celda 2 · 1. La idea: bagging + variables al azar · 🏫

**Qué hace:** Cuántas reservas quedan fuera de una muestra bootstrap: ≈ 36,8 %.

```python
# Cuántas reservas quedan fuera de una muestra bootstrap: ≈ 36,8 %
rng = np.random.default_rng(SEMILLA)
n = 5000
fuera = len(set(range(n)) - set(rng.integers(0, n, n))) / n
print(f"Reservas que NO entran en una muestra bootstrap: {fuera:.1%}")
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `n = 5000` → Guarda el valor en `n`.
- `fuera = len(set(range(n)) - set(rng.integers(0, n, n))) / n` → Guarda en `fuera` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez; `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `print(f"Reservas que NO entran en una muestra bootstrap: {fuera:.1%}")` → `print`: muestra un valor por pantalla.

### Celda 3 · 1. La idea: bagging + variables al azar · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Cuántos árboles y de qué tamaño · 🏫

**Qué hace:** oob_decision_function_ contiene la probabilidad OOB de cada reserva de train.

```python
n_arboles = [5, 10, 25, 50, 100, 200, 400]
oob_auc = []
for k in n_arboles:
    b = RandomForestClassifier(n_estimators=k, min_samples_leaf=5, oob_score=True,
                               random_state=SEMILLA, n_jobs=2).fit(Xtr, y_train)
    # oob_decision_function_ contiene la probabilidad OOB de cada reserva de train
    oob_auc.append(roc_auc_score(y_train, np.nan_to_num(b.oob_decision_function_[:, 1], nan=0.5)))
plt.figure(figsize=(7, 3.8))
plt.plot(n_arboles, oob_auc, marker="o", color="#2a6f97")
plt.xscale("log")
plt.title("Random Forest: AUC out-of-bag según el número de árboles")
plt.xlabel("Número de árboles (escala logarítmica)")
plt.ylabel("AUC out-of-bag")
plt.show()
```

**Qué hace cada línea:**

- `n_arboles = [5, 10, 25, 50, 100, 200, 400]` → Guarda el valor en `n_arboles`.
- `oob_auc = []` → Guarda el valor en `oob_auc`.
- `for k in n_arboles:` → Repite el bloque de debajo para cada valor de `k` en `n_arboles`. Dentro del bloque: `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `RandomForestClassifier`: bosque de muchos árboles que votan; `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar).
- `plt.figure(figsize=(7, 3.8))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.plot(n_arboles, oob_auc, marker="o", color="#2a6f97")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.xscale("log")` → `xscale`: cambia la escala del eje horizontal (por ejemplo, logarítmica).
- `plt.title("Random Forest: AUC out-of-bag según el número de árboles")` → `title`: pone el título del gráfico.
- `plt.xlabel("Número de árboles (escala logarítmica)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("AUC out-of-bag")` → `ylabel`: pone el nombre del eje vertical.
- … y 1 más con las mismas ideas.

### Celda 5 · 2. Cuántos árboles y de qué tamaño · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Importancia de variables: dos formas de medi… · 🏠

**Qué hace:** Practica `Pipeline`, `fit`, `permutation_importance`, `sort_values` y más (sección «3. Importancia de variables: dos formas…»).

```python
modelo_bosque = Pipeline([("prep", prep), ("rf", RandomForestClassifier(n_estimators=300, min_samples_leaf=5,
                                                                        random_state=SEMILLA, n_jobs=2))])
modelo_bosque.fit(X_train, y_train)
perm = permutation_importance(modelo_bosque, X_test, y_test, scoring="roc_auc", n_repeats=5,
                              random_state=SEMILLA, n_jobs=1)
imp_perm = pd.Series(perm.importances_mean, index=X_test.columns).sort_values(ascending=False)
plt.figure(figsize=(7, 4.5))
imp_perm.iloc[::-1].plot(kind="barh", color="#2a6f97", xerr=pd.Series(perm.importances_std, index=X_test.columns)[imp_perm.iloc[::-1].index])
plt.title("Importancia por permutación (caída del AUC en test)")
plt.xlabel("Caída media del AUC al barajar la variable")
plt.ylabel("")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `modelo_bosque = Pipeline([("prep", prep), ("rf", RandomForestClassifier(n_e…` → Guarda en `modelo_bosque` el resultado. `Pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `RandomForestClassifier`: bosque de muchos árboles que votan.
- `modelo_bosque.fit(X_train, y_train)` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `perm = permutation_importance(modelo_bosque, X_test, y_test, scoring="roc_a…` → Guarda en `perm` el resultado. `permutation_importance`: mide qué variables importan estropeándolas una a una.
- `imp_perm = pd.Series(perm.importances_mean, index=X_test.columns).sort_valu…` → Guarda en `imp_perm` el resultado. `sort_values`: ordena la tabla por una o varias columnas; `Series`: crea una columna de pandas (una sola serie de valores); `columns`: nombres de las columnas.
- `plt.figure(figsize=(7, 4.5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `imp_perm.iloc[::-1].plot(kind="barh", color="#2a6f97", xerr=pd.Series(perm.…` → `plot`: dibuja una línea (o puntos unidos); `iloc`: selecciona filas/columnas por su posición; `Series`: crea una columna de pandas (una sola serie de valores).
- `plt.title("Importancia por permutación (caída del AUC en test)")` → `title`: pone el título del gráfico.
- `plt.xlabel("Caída media del AUC al barajar la variable")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("")` → `ylabel`: pone el nombre del eje vertical.
- … y 2 más con las mismas ideas.

### Celda 7 · 3. Importancia de variables: dos formas de medi… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4. Coste del bosque · 🏠

**Qué hace:** Practica `perf_counter`, `fit`, `RandomForestClassifier`, `DecisionTreeClassifier` (sección «4. Coste del bosque»).

```python
t0 = time.perf_counter()
RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2).fit(Xtr, y_train)
t_bosque = time.perf_counter() - t0
t0 = time.perf_counter()
DecisionTreeClassifier(min_samples_leaf=80, random_state=SEMILLA).fit(Xtr, y_train)
t_arbol = time.perf_counter() - t0
print(f"Tiempo de ajuste: árbol {t_arbol * 1000:.0f} ms · bosque {t_bosque * 1000:.0f} ms (≈ {t_bosque / t_arbol:.0f} veces más)")
```

**Qué hace cada línea:**

- `t0 = time.perf_counter()` → Guarda en `t0` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=S…` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `RandomForestClassifier`: bosque de muchos árboles que votan.
- `t_bosque = time.perf_counter() - t0` → Guarda en `t_bosque` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `t0 = time.perf_counter()` → Guarda en `t0` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `DecisionTreeClassifier(min_samples_leaf=80, random_state=SEMILLA).fit(Xtr,…` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `DecisionTreeClassifier`: árbol de decisión para clasificar (reglas «si… entonces…»).
- `t_arbol = time.perf_counter() - t0` → Guarda en `t_arbol` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `print(f"Tiempo de ajuste: árbol {t_arbol * 1000:.0f} ms · bosque {t_bosque…` → `print`: muestra un valor por pantalla.

### Celda 9 · 5. Mini-reto: ¿compensa el bosque frente a la r… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S08_02_random_forest.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
