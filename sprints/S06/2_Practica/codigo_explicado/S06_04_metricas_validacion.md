# Código explicado · S06.04 · scikit-learn básico: métricas y validación

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_04_metricas_validacion.ipynb) · [descargar](../S06_04_metricas_validacion.ipynb) · ⏱ en clase: 45 min · 🏫 6 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_theme`, `read_csv`, `train_test_split`, `dato` y más. |
| 2 | 1. La API de scikit-learn y el *baselin… | Practica `fit`, `round`, `DummyClassifier`, `score` (sección «1. La API de scikit-learn y… |
| 4 | 2. Métricas: ¿cómo de bueno es? | Practica `predict`, `accuracy_score`, `precision_score`, `recall_score` y más (sección «2… |
| 6 | 3. Sobreajuste y sesgo-varianza | Practica `fit_transform`, `transform`, `figure`, `plot` y más (sección «3. Sobreajuste y… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 1 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 1 |
| `tonto` | `DummyClassifier(strategy="most_frequent").fit(X_train, y_…` | 2 |
| `pred` | `logistica.predict(X_test)` | 4 |
| `prep_arbol` | `hacer_preprocesado()` | 6 |
| `Xtr_p` | `prep_arbol.fit_transform(X_train)` | 6 |
| `Xte_p` | `prep_arbol.transform(X_test)` | 6 |
| `profundidades` | `range(1, 21)` | 6 |
| `cv` | `StratifiedKFold(n_splits=5, shuffle=True, random_state=SE…` | 8 |
| `puntuaciones` | `cross_val_score(logistica, X_train, y_train, cv=cv, scori…` | 8 |
| `rng` | `np.random.default_rng(SEMILLA)` | 10 |
| `X_fuga` | `X.copy()` | 10 |
| `prep_fuga` | `hacer_preprocesado(num=columnas_num + ["reembolso_emitido…` | 10 |
| `modelo_fuga` | `Pipeline([("prep", prep_fuga), ("clf", LogisticRegression…` | 10 |
| `auc_fuga` | `cross_val_score(modelo_fuga, X_fuga, y, cv=cv, scoring="r…` | 10 |
| `auc_real` | `cross_val_score(logistica, X, y, cv=cv, scoring="roc_auc"…` | 10 |
| `df_ord` | `df.sort_values("fecha_reserva").reset_index(drop=True)` | 12 |
| `corte` | `int(len(df_ord) * 0.8)` | 12 |
| `mod_t` | `Pipeline([("prep", hacer_preprocesado()), ("clf", Logisti…` | 12 |
| `rejilla` | `{"clf__C": [0.01, 0.1, 1, 10]}` | 14 |
| `busqueda` | `GridSearchCV(logistica, rejilla, cv=cv, scoring="roc_auc"…` | 14 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `hacer_preprocesado` | Receta estándar: imputar + escalar (num) e imputar + one-hot (cat). |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `accuracy_score` | Calcula el porcentaje de aciertos. | 4 |
| `append` | Añade un elemento al final de una lista. | 6 |
| `choice` | Elige un elemento al azar. | 10 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 1 |
| `copy` | Hace una copia independiente (si cambias la copia, el original no cambia). | 10 |
| `cross_val_score` | Evalúa el modelo con validación cruzada (varias particiones). | 8, 10 |
| `date` | Crea una fecha (año, mes, día). | 12 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `DecisionTreeClassifier` | Árbol de decisión para clasificar (reglas «si… entonces…»). | 6 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 10 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `DummyClassifier` | Modelo «tonto» de referencia (por ejemplo, siempre la clase más común). | 2 |
| `f1_score` | Calcula el F1: equilibrio entre precisión y sensibilidad. | 4 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 6 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 2, 6, 12, 14 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 6 |
| `GridSearchCV` | Prueba todas las combinaciones de ajustes y se queda con la mejor. | 14 |
| `iloc` | Selecciona filas/columnas por su posición. | 12 |
| `int` | Convierte un valor en número entero. | 12 |
| `legend` | Muestra la leyenda del gráfico. | 6 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 10, 12 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 12 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 10, 12 |
| `mean` | Calcula la media. | 1, 8, 10 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 1 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 1, 10, 12 |
| `plot` | Dibuja una línea (o puntos unidos). | 6 |
| `precision_score` | Calcula la precisión: de lo que dijo «sí», cuánto era cierto. | 4 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 4 |
| `print` | Muestra un valor por pantalla. | 1, 2, 4, 8, 10, 12… |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 6 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `recall_score` | Calcula la sensibilidad: de lo que era «sí», cuánto detectó. | 4 |
| `reset_index` | Devuelve el índice de la tabla a 0, 1, 2… | 12 |
| `round` | Redondea un número a los decimales indicados. | 1, 2, 8, 12, 14 |
| `score` | Calcula la nota del modelo con la métrica por defecto. | 2, 6, 12 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `show` | Muestra el gráfico. | 6 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 1 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 12 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 1 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 8 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 8 |
| `title` | Pone el título del gráfico. | 6 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 6 |
| `where` | Elige un valor u otro según una condición (como un `if` para todos los datos a la vez). | 10 |
| `xlabel` | Pone el nombre del eje horizontal. | 6 |
| `ylabel` | Pone el nombre del eje vertical. | 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_theme`, `read_csv`, `train_test_split`, `dato` y más.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import (train_test_split, cross_val_score, StratifiedKFold,
                                     TimeSeriesSplit, GridSearchCV)
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             mean_absolute_error, mean_squared_error, r2_score)

SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "mes_llegada"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]


def hacer_preprocesado(num=columnas_num, cat=columnas_cat):
    """Receta estándar: imputar + escalar (num) e imputar + one-hot (cat)."""
    return ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), num),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat),
    ])


X, y = df[columnas_num + columnas_cat], df["cancelada"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
print("Tasa de cancelación:", y.mean().round(3))
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import (train_test_split, cross_val_score, Str…` → Trae `train_test_split`, `cross_val_score`, `StratifiedKFold`, `TimeSeriesSplit`, `GridSearchCV` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.dummy import DummyClassifier` → Trae `DummyClassifier` de `sklearn.dummy` para poder usarlo.
- `from sklearn.linear_model import LogisticRegression, LinearRegression` → Trae `LogisticRegression`, `LinearRegression` de `sklearn.linear_model` para poder usarlo.
- `from sklearn.tree import DecisionTreeClassifier` → Trae `DecisionTreeClassifier` de `sklearn.tree` para poder usarlo.
- `from sklearn.impute import SimpleImputer` → Trae `SimpleImputer` de `sklearn.impute` para poder usarlo.
- … y 14 más con las mismas ideas.

### Celda 2 · 1. La API de scikit-learn y el *baseline* · 🏫

**Qué hace:** Practica `fit`, `round`, `DummyClassifier`, `score` (sección «1. La API de scikit-learn y el *baselin…»).

```python
tonto = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print("Exactitud del baseline:", round(tonto.score(X_test, y_test), 3))
```

**Qué hace cada línea:**

- `tonto = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)` → Guarda en `tonto` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `DummyClassifier`: modelo «tonto» de referencia (por ejemplo, siempre la clase más común).
- `print("Exactitud del baseline:", round(tonto.score(X_test, y_test), 3))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `score`: calcula la nota del modelo con la métrica por defecto.

### Celda 3 · 1. La API de scikit-learn y el *baseline* · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Métricas: ¿cómo de bueno es? · 🏫

**Qué hace:** Practica `predict`, `accuracy_score`, `precision_score`, `recall_score` y más (sección «2. Métricas: ¿cómo de bueno es?»).

```python
pred = logistica.predict(X_test)
print(f"Exactitud {accuracy_score(y_test, pred):.3f} · Precisión {precision_score(y_test, pred):.3f} "
      f"· Recall {recall_score(y_test, pred):.3f} · F1 {f1_score(y_test, pred):.3f}")
```

**Qué hace cada línea:**

- `pred = logistica.predict(X_test)` → Guarda en `pred` el resultado. `predict`: pide al modelo ya entrenado que haga predicciones.
- `print(f"Exactitud {accuracy_score(y_test, pred):.3f} · Precisión {precision…` → `print`: muestra un valor por pantalla; `accuracy_score`: calcula el porcentaje de aciertos; `precision_score`: calcula la precisión: de lo que dijo «sí», cuánto era cierto.

### Celda 5 · 2. Métricas: ¿cómo de bueno es? · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Sobreajuste y sesgo-varianza · 🏫

**Qué hace:** Practica `fit_transform`, `transform`, `figure`, `plot` y más (sección «3. Sobreajuste y sesgo-varianza»).

```python
prep_arbol = hacer_preprocesado()
Xtr_p = prep_arbol.fit_transform(X_train)
Xte_p = prep_arbol.transform(X_test)
profundidades = range(1, 21)
acc_tr, acc_te = [], []
for p in profundidades:
    arbol = DecisionTreeClassifier(max_depth=p, random_state=SEMILLA).fit(Xtr_p, y_train)
    acc_tr.append(arbol.score(Xtr_p, y_train))
    acc_te.append(arbol.score(Xte_p, y_test))
plt.figure(figsize=(8, 4))
plt.plot(profundidades, acc_tr, marker="o", label="Entrenamiento")
plt.plot(profundidades, acc_te, marker="s", label="Prueba")
plt.title("Sobreajuste: profundidad del árbol vs. exactitud")
plt.xlabel("Profundidad máxima del árbol")
plt.ylabel("Exactitud")
plt.legend()
plt.show()
```

**Qué hace cada línea:**

- `prep_arbol = hacer_preprocesado()` → Guarda en `prep_arbol` el resultado. `hacer_preprocesado`: receta estándar: imputar + escalar (num) e imputar + one-hot (cat).
- `Xtr_p = prep_arbol.fit_transform(X_train)` → Guarda en `Xtr_p` el resultado. `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `Xte_p = prep_arbol.transform(X_test)` → Guarda en `Xte_p` el resultado. `transform`: calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado.
- `profundidades = range(1, 21)` → Guarda en `profundidades` el resultado. `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `acc_tr, acc_te = [], []` → Guarda el valor en `acc_tr, acc_te`.
- `for p in profundidades:` → Repite el bloque de debajo para cada valor de `p` en `profundidades`. Dentro del bloque: `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `DecisionTreeClassifier`: árbol de decisión para clasificar (reglas «si… entonces…»); `score`: calcula la nota del modelo con la métrica por defecto.
- `plt.figure(figsize=(8, 4))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.plot(profundidades, acc_tr, marker="o", label="Entrenamiento")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.plot(profundidades, acc_te, marker="s", label="Prueba")` → `plot`: dibuja una línea (o puntos unidos).
- … y 5 más con las mismas ideas.

### Celda 7 · 3. Sobreajuste y sesgo-varianza · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4. Validación cruzada · 🏫

**Qué hace:** Practica `StratifiedKFold`, `cross_val_score`, `round`, `mean` y más (sección «4. Validación cruzada»).

```python
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMILLA)
puntuaciones = cross_val_score(logistica, X_train, y_train, cv=cv, scoring="accuracy")
print("Exactitud por fold:", puntuaciones.round(3))
print(f"Media {puntuaciones.mean():.3f} ± {puntuaciones.std():.3f}")
```

**Qué hace cada línea:**

- `cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMILLA)` → Guarda en `cv` el resultado. `StratifiedKFold`: crea particiones de validación cruzada que mantienen la proporción de clases.
- `puntuaciones = cross_val_score(logistica, X_train, y_train, cv=cv, scoring=…` → Guarda en `puntuaciones` el resultado. `cross_val_score`: evalúa el modelo con validación cruzada (varias particiones).
- `print("Exactitud por fold:", puntuaciones.round(3))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados.
- `print(f"Media {puntuaciones.mean():.3f} ± {puntuaciones.std():.3f}")` → `print`: muestra un valor por pantalla; `mean`: calcula la media; `std`: calcula la desviación típica (cuánto se separan los datos de la media).

### Celda 9 · 4. Validación cruzada · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5. Fuga de datos (*data leakage*) · 🏫

**Qué hace:** Practica `default_rng`, `copy`, `where`, `Pipeline` y más (sección «5. Fuga de datos (*data leakage*)»).

```python
rng = np.random.default_rng(SEMILLA)
X_fuga = X.copy()
X_fuga["reembolso_emitido"] = np.where(y == 1, rng.choice([1, 1, 1, 0], len(y)), 0)  # casi = cancelada
prep_fuga = hacer_preprocesado(num=columnas_num + ["reembolso_emitido"])
modelo_fuga = Pipeline([("prep", prep_fuga), ("clf", LogisticRegression(max_iter=1000))])
auc_fuga = cross_val_score(modelo_fuga, X_fuga, y, cv=cv, scoring="roc_auc").mean()
auc_real = cross_val_score(logistica, X, y, cv=cv, scoring="roc_auc").mean()
print(f"AUC sin la columna: {auc_real:.3f} · AUC con la columna que 'delata' el resultado: {auc_fuga:.3f}")
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `X_fuga = X.copy()` → Guarda en `X_fuga` el resultado. `copy`: hace una copia independiente (si cambias la copia, el original no cambia).
- `X_fuga["reembolso_emitido"] = np.where(y == 1, rng.choice([1, 1, 1, 0], len…` → Guarda en `X_fuga["reembolso_emiti…` el resultado. `where`: elige un valor u otro según una condición (como un `if` para todos los datos a la vez); `choice`: elige un elemento al azar; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `prep_fuga = hacer_preprocesado(num=columnas_num + ["reembolso_emitido"])` → Guarda en `prep_fuga` el resultado. `hacer_preprocesado`: receta estándar: imputar + escalar (num) e imputar + one-hot (cat).
- `modelo_fuga = Pipeline([("prep", prep_fuga), ("clf", LogisticRegression(max…` → Guarda en `modelo_fuga` el resultado. `Pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- `auc_fuga = cross_val_score(modelo_fuga, X_fuga, y, cv=cv, scoring="roc_auc"…` → Guarda en `auc_fuga` el resultado. `mean`: calcula la media; `cross_val_score`: evalúa el modelo con validación cruzada (varias particiones).
- `auc_real = cross_val_score(logistica, X, y, cv=cv, scoring="roc_auc").mean()` → Guarda en `auc_real` el resultado. `mean`: calcula la media; `cross_val_score`: evalúa el modelo con validación cruzada (varias particiones).
- `print(f"AUC sin la columna: {auc_real:.3f} · AUC con la columna que 'delata…` → `print`: muestra un valor por pantalla.

### Celda 11 · 5. Fuga de datos (*data leakage*) · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 12 · 6. Partición temporal · 🏠

**Qué hace:** Practica `reset_index`, `Pipeline`, `fit`, `date` y más (sección «6. Partición temporal»).

```python
df_ord = df.sort_values("fecha_reserva").reset_index(drop=True)
corte = int(len(df_ord) * 0.8)
Xo, yo = df_ord[columnas_num + columnas_cat], df_ord["cancelada"]
mod_t = Pipeline([("prep", hacer_preprocesado()), ("clf", LogisticRegression(max_iter=1000))])
mod_t.fit(Xo.iloc[:corte], yo.iloc[:corte])
print("Fecha de corte:", df_ord.loc[corte, "fecha_reserva"].date())
print("Exactitud en el futuro (partición temporal):", round(mod_t.score(Xo.iloc[corte:], yo.iloc[corte:]), 3))
```

**Qué hace cada línea:**

- `df_ord = df.sort_values("fecha_reserva").reset_index(drop=True)` → Guarda en `df_ord` el resultado. `reset_index`: devuelve el índice de la tabla a 0, 1, 2…; `sort_values`: ordena la tabla por una o varias columnas.
- `corte = int(len(df_ord) * 0.8)` → Guarda en `corte` el resultado. `int`: convierte un valor en número entero; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `Xo, yo = df_ord[columnas_num + columnas_cat], df_ord["cancelada"]` → Guarda el valor en `Xo, yo`.
- `mod_t = Pipeline([("prep", hacer_preprocesado()), ("clf", LogisticRegressio…` → Guarda en `mod_t` el resultado. `Pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `hacer_preprocesado`: receta estándar: imputar + escalar (num) e imputar + one-hot (cat); `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- `mod_t.fit(Xo.iloc[:corte], yo.iloc[:corte])` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `iloc`: selecciona filas/columnas por su posición.
- `print("Fecha de corte:", df_ord.loc[corte, "fecha_reserva"].date())` → `print`: muestra un valor por pantalla; `date`: crea una fecha (año, mes, día); `loc`: selecciona filas/columnas por su etiqueta o por una condición.
- `print("Exactitud en el futuro (partición temporal):", round(mod_t.score(Xo.…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `score`: calcula la nota del modelo con la métrica por defecto.

### Celda 13 · 6. Partición temporal · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 14 · 7. Buscar la mejor configuración: `GridSearchCV` · 🏠

**Qué hace:** Practica `fit`, `round`, `GridSearchCV` (sección «7. Buscar la mejor configuración: `Grid…»).

```python
rejilla = {"clf__C": [0.01, 0.1, 1, 10]}
busqueda = GridSearchCV(logistica, rejilla, cv=cv, scoring="roc_auc").fit(X_train, y_train)
print("Mejor C:", busqueda.best_params_, "· AUC en validación:", round(busqueda.best_score_, 3))
```

**Qué hace cada línea:**

- `rejilla = {"clf__C": [0.01, 0.1, 1, 10]}` → Guarda el valor en `rejilla`.
- `busqueda = GridSearchCV(logistica, rejilla, cv=cv, scoring="roc_auc").fit(X…` → Guarda en `busqueda` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `GridSearchCV`: prueba todas las combinaciones de ajustes y se queda con la mejor.
- `print("Mejor C:", busqueda.best_params_, "· AUC en validación:", round(busq…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados.

### Celda 15 · 8. Mini-reto: tabla de resultados honesta · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S06_04_metricas_validacion.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
