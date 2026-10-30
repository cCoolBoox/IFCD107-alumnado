# Código explicado · S08.01 · Árboles de decisión: sobreajuste, poda e importancia

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/notebooks/S08_01_arboles_decision.ipynb) · [descargar](../notebooks/S08_01_arboles_decision.ipynb) · ⏱ en clase: 35 min · 🏫 4 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Los árboles NO necesitan escalar; solo imputar nulos y codificar las categóricas. |
| 2 | 1. La idea: preguntas de sí/no encadena… | Practica `fit`, `figure`, `plot_tree`, `title` y más (sección «1. La idea: preguntas de s… |
| 3 | 1. La idea: preguntas de sí/no encadena… | Practica `export_text`, `list` (sección «1. La idea: preguntas de sí/no encadena…»). |
| 6 | 3. Poda: frenar el crecimiento | Practica `figure`, `plot`, `xscale`, `title` y más (sección «3. Poda: frenar el crecimien… |

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
| `arbol_peq` | `DecisionTreeClassifier(max_depth=3, random_state=SEMILLA)…` | 2 |
| `hojas_min` | `[1, 5, 10, 20, 40, 80, 160, 320]` | 6 |
| `auc_cv_hojas` | `[]` | 6 |
| `importancias` | `pd.Series(arbol_podado.feature_importances_, index=nombre…` | 8 |
| `predicciones` | `[]` | 10 |
| `desacuerdo` | `(predicciones.min(axis=0) != predicciones.max(axis=0)).me…` | 10 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `append` | Añade un elemento al final de una lista. | 6, 10 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 10 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1 |
| `choice` | Elige un elemento al azar. | 10 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `cross_val_score` | Evalúa el modelo con validación cruzada (varias particiones). | 6 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `DecisionTreeClassifier` | Árbol de decisión para clasificar (reglas «si… entonces…»). | 2, 6, 10 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 10 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `export_text` | Muestra las reglas de un árbol como texto. | 3 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 2, 6, 8 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 2, 10 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 1 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 1 |
| `head` | Muestra las primeras filas. | 8 |
| `iloc` | Selecciona filas/columnas por su posición. | 8 |
| `int` | Convierte un valor en número entero. | 10 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 1, 10 |
| `list` | Crea una lista (o convierte algo en lista). | 2, 3 |
| `max` | Devuelve el valor más grande. | 10 |
| `mean` | Calcula la media. | 6, 10 |
| `min` | Devuelve el valor más pequeño. | 10 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 1, 6 |
| `plot` | Dibuja una línea (o puntos unidos). | 6, 8 |
| `plot_tree` | Dibuja el árbol de decisión. | 2 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 10 |
| `print` | Muestra un valor por pantalla. | 1, 3, 10 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 10 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 8 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `show` | Muestra el gráfico. | 2, 6, 8 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 1 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 8 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 1 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 8 |
| `title` | Pone el título del gráfico. | 2, 6, 8 |
| `to_numpy` | Convierte una tabla o columna de pandas en un array de NumPy. | 10 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 1 |
| `xlabel` | Pone el nombre del eje horizontal. | 6, 8 |
| `xscale` | Cambia la escala del eje horizontal (por ejemplo, logarítmica). | 6 |
| `ylabel` | Pone el nombre del eje vertical. | 6, 8 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Los árboles NO necesitan escalar; solo imputar nulos y codificar las categóricas.

```python
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
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

# Los árboles NO necesitan escalar; solo imputar nulos y codificar las categóricas
prep = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), columnas_cat),
])
Xtr = prep.fit_transform(X_train)
Xte = prep.transform(X_test)
nombres = prep.get_feature_names_out()
print("Columnas tras el preprocesado:", len(nombres))
```

**Qué hace cada línea:**

- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split, StratifiedKFold, cros…` → Trae `train_test_split`, `StratifiedKFold`, `cross_val_score` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text` → Trae `DecisionTreeClassifier`, `plot_tree`, `export_text` de `sklearn.tree` para poder usarlo.
- `from sklearn.impute import SimpleImputer` → Trae `SimpleImputer` de `sklearn.impute` para poder usarlo.
- `from sklearn.preprocessing import OneHotEncoder` → Trae `OneHotEncoder` de `sklearn.preprocessing` para poder usarlo.
- … y 18 más con las mismas ideas.

### Celda 2 · 1. La idea: preguntas de sí/no encadenadas · 🏫

**Qué hace:** Practica `fit`, `figure`, `plot_tree`, `title` y más (sección «1. La idea: preguntas de sí/no encadena…»).

```python
arbol_peq = DecisionTreeClassifier(max_depth=3, random_state=SEMILLA).fit(Xtr, y_train)
plt.figure(figsize=(16, 6))
plot_tree(arbol_peq, feature_names=list(nombres), class_names=["se mantiene", "cancela"],
          filled=True, rounded=True, fontsize=8, proportion=True)
plt.title("Árbol de decisión de profundidad 3")
plt.show()
```

**Qué hace cada línea:**

- `arbol_peq = DecisionTreeClassifier(max_depth=3, random_state=SEMILLA).fit(X…` → Guarda en `arbol_peq` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `DecisionTreeClassifier`: árbol de decisión para clasificar (reglas «si… entonces…»).
- `plt.figure(figsize=(16, 6))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plot_tree(arbol_peq, feature_names=list(nombres), class_names=["se mantiene…` → `plot_tree`: dibuja el árbol de decisión; `list`: crea una lista (o convierte algo en lista).
- `plt.title("Árbol de decisión de profundidad 3")` → `title`: pone el título del gráfico.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 3 · 1. La idea: preguntas de sí/no encadenadas · 🏫

**Qué hace:** Practica `export_text`, `list` (sección «1. La idea: preguntas de sí/no encadena…»).

```python
print(export_text(arbol_peq, feature_names=list(nombres), max_depth=3))
```

**Qué hace cada línea:**

- `print(export_text(arbol_peq, feature_names=list(nombres), max_depth=3))` → `print`: muestra un valor por pantalla; `export_text`: muestra las reglas de un árbol como texto; `list`: crea una lista (o convierte algo en lista).

### Celda 4 · 1. La idea: preguntas de sí/no encadenadas · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2. Sobreajuste: el árbol libre · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Poda: frenar el crecimiento · 🏫

**Qué hace:** Practica `figure`, `plot`, `xscale`, `title` y más (sección «3. Poda: frenar el crecimiento»).

```python
hojas_min = [1, 5, 10, 20, 40, 80, 160, 320]
auc_cv_hojas = []
for m in hojas_min:
    arb = Pipeline([("prep", prep), ("arbol", DecisionTreeClassifier(min_samples_leaf=m, random_state=SEMILLA))])
    auc_cv_hojas.append(cross_val_score(arb, X_train, y_train, cv=cv, scoring="roc_auc").mean())
plt.figure(figsize=(7, 3.8))
plt.plot(hojas_min, auc_cv_hojas, marker="o", color="#2a6f97")
plt.xscale("log")
plt.title("Poda: AUC (validación cruzada) según el mínimo de reservas por hoja")
plt.xlabel("min_samples_leaf (escala logarítmica)")
plt.ylabel("AUC medio en validación cruzada")
plt.show()
```

**Qué hace cada línea:**

- `hojas_min = [1, 5, 10, 20, 40, 80, 160, 320]` → Guarda el valor en `hojas_min`.
- `auc_cv_hojas = []` → Guarda el valor en `auc_cv_hojas`.
- `for m in hojas_min:` → Repite el bloque de debajo para cada valor de `m` en `hojas_min`. Dentro del bloque: `Pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `DecisionTreeClassifier`: árbol de decisión para clasificar (reglas «si… entonces…»); `mean`: calcula la media.
- `plt.figure(figsize=(7, 3.8))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.plot(hojas_min, auc_cv_hojas, marker="o", color="#2a6f97")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.xscale("log")` → `xscale`: cambia la escala del eje horizontal (por ejemplo, logarítmica).
- `plt.title("Poda: AUC (validación cruzada) según el mínimo de reservas por h…` → `title`: pone el título del gráfico.
- `plt.xlabel("min_samples_leaf (escala logarítmica)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("AUC medio en validación cruzada")` → `ylabel`: pone el nombre del eje vertical.
- … y 1 más con las mismas ideas.

### Celda 7 · 3. Poda: frenar el crecimiento · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4. Importancia de variables · 🏠

**Qué hace:** Practica `sort_values`, `figure`, `plot`, `title` y más (sección «4. Importancia de variables»).

```python
importancias = pd.Series(arbol_podado.feature_importances_, index=nombres).sort_values(ascending=False)
plt.figure(figsize=(7, 4.5))
importancias.head(10).iloc[::-1].plot(kind="barh", color="#2a6f97")
plt.title("Importancia de variables del árbol podado (top 10)")
plt.xlabel("Importancia (reducción de impureza)")
plt.ylabel("")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `importancias = pd.Series(arbol_podado.feature_importances_, index=nombres).…` → Guarda en `importancias` el resultado. `sort_values`: ordena la tabla por una o varias columnas; `Series`: crea una columna de pandas (una sola serie de valores).
- `plt.figure(figsize=(7, 4.5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `importancias.head(10).iloc[::-1].plot(kind="barh", color="#2a6f97")` → `plot`: dibuja una línea (o puntos unidos); `iloc`: selecciona filas/columnas por su posición; `head`: muestra las primeras filas.
- `plt.title("Importancia de variables del árbol podado (top 10)")` → `title`: pone el título del gráfico.
- `plt.xlabel("Importancia (reducción de impureza)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("")` → `ylabel`: pone el nombre del eje vertical.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 9 · 4. Importancia de variables · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5. Inestabilidad: el gran defecto · 🏠

**Qué hace:** % de reservas de test en las que los 5 árboles NO se ponen de acuerdo.

```python
predicciones = []
for semilla in range(5):
    idx = np.random.default_rng(semilla).choice(len(Xtr), int(0.8 * len(Xtr)), replace=False)
    a = DecisionTreeClassifier(min_samples_leaf=10, random_state=SEMILLA).fit(Xtr[idx], y_train.to_numpy()[idx])
    predicciones.append(a.predict(Xte))
predicciones = np.array(predicciones)
# % de reservas de test en las que los 5 árboles NO se ponen de acuerdo
desacuerdo = (predicciones.min(axis=0) != predicciones.max(axis=0)).mean()
print(f"En el {desacuerdo:.0%} de las reservas de test, los 5 árboles no coinciden en la predicción.")
```

**Qué hace cada línea:**

- `predicciones = []` → Guarda el valor en `predicciones`.
- `for semilla in range(5):` → Repite el bloque de debajo para cada valor de `semilla` en `range(5)`. Dentro del bloque: `choice`: elige un elemento al azar; `default_rng`: crea un generador de números aleatorios reproducible (con semilla); `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `predicciones = np.array(predicciones)` → Guarda en `predicciones` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `desacuerdo = (predicciones.min(axis=0) != predicciones.max(axis=0)).mean()` → Guarda en `desacuerdo` el resultado. `mean`: calcula la media; `min`: devuelve el valor más pequeño; `max`: devuelve el valor más grande.
- `print(f"En el {desacuerdo:.0%} de las reservas de test, los 5 árboles no co…` → `print`: muestra un valor por pantalla.

### Celda 11 · 6. Mini-reto: reglas para el gerente · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S08_01_arboles_decision.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
