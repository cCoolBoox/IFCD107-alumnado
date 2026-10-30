# Código explicado · S10.02 · S10 · Práctica 2 — Tu primer MLP en Keras: cancelaciones y precio por noche

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_02_mlp_keras.ipynb) · [descargar](../notebooks/S10_02_mlp_keras.ipynb) · ⏱ en clase: 60 min · 🏫 5 celdas de código en clase · 🏠 3 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_random_seed`. |
| 2 | 1. Preparar los datos para una red neur… | Practica `read_csv`, `head`, `dato`, `dt` y más (sección «1. Preparar los datos para una… |
| 4 | 1. Preparar los datos para una red neur… | Clasificación: el precio es un dato conocido al reservar, así que puede ser una variable… |
| 6 | 2. Un MLP para clasificar cancelaciones | Practica `fit`, `history`, `subplots`, `plot` y más (sección «Entrenar (`fit`)»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 2 |
| `hist_c` | `mlp_c.fit(Xc_ent, yc_ent, validation_data=(Xc_val, yc_val…` | 6 |
| `prob_mlp` | `mlp_c.predict(Xc_pru, verbose=0).ravel()` | 7 |
| `logistica` | `LogisticRegression(max_iter=1000).fit(Xc_ent, yc_ent)` | 7 |
| `prob_log` | `logistica.predict_proba(Xc_pru)[:, 1]` | 7 |
| `tabla` | `pd.DataFrame({ "modelo": ["Siempre 'no cancela'", "Regres…` | 7 |
| `esc` | `lambda v: ((v - media_p) / desv_p).astype("float32")` | 9 |
| `desesc` | `lambda v: v * desv_p + media_p` | 9 |
| `pred_mlp` | `desesc(mlp_r.predict(Xr_pru, verbose=0).ravel())` | 11 |
| `ridge` | `Ridge().fit(Xr_ent, yr_ent)` | 11 |
| `pred_ridge` | `ridge.predict(Xr_pru)` | 11 |
| `mae` | `lambda p: mean_absolute_error(yr_pru, p)` | 11 |
| `tabla_r` | `pd.DataFrame({ "modelo": ["Siempre el precio medio", "Reg…` | 11 |
| `lim` | `[yr_pru.min(), yr_pru.max()]` | 13 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `preparar` | Devuelve matrices ya escaladas/codificadas y el preprocesador ajustado. |
| `construir_mlp_clasificacion` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `dibujar_curvas` | Función definida en el cuaderno. |
| `construir_mlp_regresion` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `accuracy_score` | Calcula el porcentaje de aciertos. | 7 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 4, 9 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 4 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 7, 11 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `desesc` | Deshace el escalado de la predicción para volver a euros. | 11 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 2 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 13 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 6, 7, 11 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 4 |
| `full` | Crea un array lleno del valor indicado. | 11 |
| `head` | Muestra las primeras filas. | 2 |
| `history` | Guarda la evolución de las métricas época a época. | 6 |
| `legend` | Muestra la leyenda del gráfico. | 6, 13 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 11 |
| `list` | Crea una lista (o convierte algo en lista). | 4 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 7 |
| `mae` | Error medio absoluto, en las mismas unidades que lo que se predice. | 11 |
| `max` | Devuelve el valor más grande. | 13 |
| `mean` | Calcula la media. | 2, 7, 9, 11 |
| `mean_absolute_error` | Error medio absoluto (MAE): cuánto se equivoca de media, en las mismas unidades. | 11 |
| `min` | Devuelve el valor más pequeño. | 13 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 4 |
| `plot` | Dibuja una línea (o puntos unidos). | 6, 13 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 7, 11 |
| `predict_proba` | Pide la probabilidad de cada clase (no solo la clase). | 7 |
| `print` | Muestra un valor por pantalla. | 1, 2, 4 |
| `ravel` | Aplana un array a una sola dimensión. | 7, 11 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `Ridge` | Regresión lineal con penalización L2 (encoge los coeficientes). | 11 |
| `roc_auc_score` | Calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar). | 7 |
| `round` | Redondea un número a los decimales indicados. | 2, 7, 11 |
| `scatter` | Dibuja un gráfico de puntos. | 13 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 1 |
| `set_title` | Pone el título de un gráfico. | 6 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 6 |
| `set_ylabel` | Pone el nombre del eje vertical. | 6 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2, 4 |
| `show` | Muestra el gráfico. | 6, 13 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 4 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 9 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 6 |
| `suptitle` | Pone un título general a toda la figura. | 6 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 6 |
| `title` | Pone el título del gráfico. | 13 |
| `to_numpy` | Convierte una tabla o columna de pandas en un array de NumPy. | 4 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 4 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 4 |
| `upper` | Pasa el texto a mayúsculas. | 6 |
| `xlabel` | Pone el nombre del eje horizontal. | 13 |
| `ylabel` | Pone el nombre del eje vertical. | 13 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_random_seed`.

```python
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"   # menos mensajes de TensorFlow
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import roc_auc_score, accuracy_score, mean_absolute_error
from sklearn.linear_model import LogisticRegression, Ridge

SEMILLA = 42
keras.utils.set_random_seed(SEMILLA)   # fija NumPy, Python y TensorFlow a la vez
print("TensorFlow", tf.__version__)
```

**Qué hace cada línea:**

- `import os` → Trae `os` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" # menos mensajes de TensorFlow` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import tensorflow as tf` → Trae `tensorflow` (lo llamamos `tf`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- … y 6 más con las mismas ideas.

### Celda 2 · 1. Preparar los datos para una red neuronal · 🏫

**Qué hace:** Practica `read_csv`, `head`, `dato`, `dt` y más (sección «1. Preparar los datos para una red neur…»).

```python
df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
print(df.shape, "· tasa de cancelación:", round(df["cancelada"].mean(), 3))
df.head(3)
```

**Qué hace cada línea:**

- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_llegad…` → Guarda en `df` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `df["mes_llegada"] = df["fecha_llegada"].dt.month` → Guarda en `df["mes_llegada"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `print(df.shape, "· tasa de cancelación:", round(df["cancelada"].mean(), 3))` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas); `round`: redondea un número a los decimales indicados.
- `df.head(3)` → `head`: muestra las primeras filas.

### Celda 3 · 1. Preparar los datos para una red neuronal · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1. Preparar los datos para una red neuronal · 🏫

**Qué hace:** Clasificación: el precio es un dato conocido al reservar, así que puede ser una variable de entrada.

```python
def preparar(objetivo, extra_num=()):
    """Devuelve matrices ya escaladas/codificadas y el preprocesador ajustado."""
    numericas = list(cols_num) + list(extra_num)
    X = df[numericas + cols_cat]
    y = df[objetivo].to_numpy()
    estrato = y if objetivo == "cancelada" else None
    X_res, X_pru, y_res, y_pru = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=estrato)
    estrato = y_res if objetivo == "cancelada" else None
    X_ent, X_val, y_ent, y_val = train_test_split(X_res, y_res, test_size=0.2, random_state=SEMILLA, stratify=estrato)
    pre = ColumnTransformer([("num", StandardScaler(), numericas),
                             ("cat", OneHotEncoder(handle_unknown="ignore"), cols_cat)])
    A_ent = pre.fit_transform(X_ent).astype("float32")     # ajusta SOLO con entrenamiento
    A_val = pre.transform(X_val).astype("float32")
    A_pru = pre.transform(X_pru).astype("float32")
    return A_ent, A_val, A_pru, y_ent, y_val, y_pru, pre

# Clasificación: el precio es un dato conocido al reservar, así que puede ser una variable de entrada
Xc_ent, Xc_val, Xc_pru, yc_ent, yc_val, yc_pru, pre_c = preparar("cancelada", extra_num=["precio_noche"])
print("Clasificación:", Xc_ent.shape, Xc_val.shape, Xc_pru.shape)
```

**Qué hace cada línea:**

- `def preparar(objetivo, extra_num=()):` → Define la función `preparar`: Devuelve matrices ya escaladas/codificadas y el preprocesador ajustado.
- `Xc_ent, Xc_val, Xc_pru, yc_ent, yc_val, yc_pru, pre_c = preparar("cancelada…` → Guarda en `Xc_ent, Xc_val, Xc_pru,…` el resultado. `preparar`: devuelve matrices ya escaladas/codificadas y el preprocesador ajustado.
- `print("Clasificación:", Xc_ent.shape, Xc_val.shape, Xc_pru.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).

### Celda 5 · 2. Un MLP para clasificar cancelaciones · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 2. Un MLP para clasificar cancelaciones · 🏫

**Qué hace:** Practica `fit`, `history`, `subplots`, `plot` y más (sección «Entrenar (`fit`)»).

```python
hist_c = mlp_c.fit(Xc_ent, yc_ent, validation_data=(Xc_val, yc_val), epochs=30, batch_size=64, verbose=0)

def dibujar_curvas(hist, metrica, titulo):
    h = hist.history
    fig, ejes = plt.subplots(1, 2, figsize=(11, 3.8))
    ejes[0].plot(h["loss"], label="entrenamiento"); ejes[0].plot(h["val_loss"], label="validación")
    ejes[0].set_title("Pérdida"); ejes[0].set_xlabel("época"); ejes[0].set_ylabel("pérdida"); ejes[0].legend()
    ejes[1].plot(h[metrica], label="entrenamiento"); ejes[1].plot(h["val_" + metrica], label="validación")
    ejes[1].set_title(metrica.upper()); ejes[1].set_xlabel("época"); ejes[1].set_ylabel(metrica); ejes[1].legend()
    fig.suptitle(titulo); plt.tight_layout(); plt.show()

dibujar_curvas(hist_c, "auc", "MLP de cancelaciones: curvas de aprendizaje")
```

**Qué hace cada línea:**

- `hist_c = mlp_c.fit(Xc_ent, yc_ent, validation_data=(Xc_val, yc_val), epochs…` → Guarda en `hist_c` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `def dibujar_curvas(hist, metrica, titulo):` → Define la función `dibujar_curvas`: Función definida en el cuaderno.
- `dibujar_curvas(hist_c, "auc", "MLP de cancelaciones: curvas de aprendizaje")` → `dibujar_curvas`: función definida en el cuaderno.

### Celda 7 · 2. Un MLP para clasificar cancelaciones · 🏫

**Qué hace:** Practica `ravel`, `fit`, `round`, `predict_proba` y más (sección «Evaluar en prueba y comparar con una re…»).

```python
prob_mlp = mlp_c.predict(Xc_pru, verbose=0).ravel()
logistica = LogisticRegression(max_iter=1000).fit(Xc_ent, yc_ent)
prob_log = logistica.predict_proba(Xc_pru)[:, 1]

tabla = pd.DataFrame({
    "modelo": ["Siempre 'no cancela'", "Regresión logística", "MLP (32-16)"],
    "AUC": [0.5, roc_auc_score(yc_pru, prob_log), roc_auc_score(yc_pru, prob_mlp)],
    "precisión": [1 - yc_pru.mean(), accuracy_score(yc_pru, prob_log > 0.5), accuracy_score(yc_pru, prob_mlp > 0.5)],
}).round(3)
tabla
```

**Qué hace cada línea:**

- `prob_mlp = mlp_c.predict(Xc_pru, verbose=0).ravel()` → Guarda en `prob_mlp` el resultado. `ravel`: aplana un array a una sola dimensión; `predict`: pide al modelo ya entrenado que haga predicciones.
- `logistica = LogisticRegression(max_iter=1000).fit(Xc_ent, yc_ent)` → Guarda en `logistica` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- `prob_log = logistica.predict_proba(Xc_pru)[:, 1]` → Guarda en `prob_log` el resultado. `predict_proba`: pide la probabilidad de cada clase (no solo la clase).
- `tabla = pd.DataFrame({` → Guarda en `tabla` el resultado. `round`: redondea un número a los decimales indicados; `DataFrame`: crea una tabla de pandas (filas y columnas); `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar).

### Celda 8 · 2. Un MLP para clasificar cancelaciones · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 3. Un MLP para predecir el precio por noche (re… · 🏠

**Qué hace:** Practica `mean`, `std`, `astype` (sección «3. Un MLP para predecir el precio por n…»).

```python
Xr_ent, Xr_val, Xr_pru, yr_ent, yr_val, yr_pru, pre_r = preparar("precio_noche")
media_p, desv_p = yr_ent.mean(), yr_ent.std()
esc = lambda v: ((v - media_p) / desv_p).astype("float32")     # a escala estandarizada
desesc = lambda v: v * desv_p + media_p                         # de vuelta a euros
```

**Qué hace cada línea:**

- `Xr_ent, Xr_val, Xr_pru, yr_ent, yr_val, yr_pru, pre_r = preparar("precio_no…` → Guarda en `Xr_ent, Xr_val, Xr_pru,…` el resultado. `preparar`: devuelve matrices ya escaladas/codificadas y el preprocesador ajustado.
- `media_p, desv_p = yr_ent.mean(), yr_ent.std()` → Guarda en `media_p, desv_p` el resultado. `mean`: calcula la media; `std`: calcula la desviación típica (cuánto se separan los datos de la media).
- `esc = lambda v: ((v - media_p) / desv_p).astype("float32") # a escala estan…` → Guarda en `esc` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número).
- `desesc = lambda v: v * desv_p + media_p # de vuelta a euros` → Guarda el valor en `desesc`.

### Celda 10 · 3. Un MLP para predecir el precio por noche (re… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 3. Un MLP para predecir el precio por noche (re… · 🏠

**Qué hace:** Practica `desesc`, `fit`, `predict`, `round` y más (sección «3. Un MLP para predecir el precio por n…»).

```python
pred_mlp = desesc(mlp_r.predict(Xr_pru, verbose=0).ravel())
ridge = Ridge().fit(Xr_ent, yr_ent)
pred_ridge = ridge.predict(Xr_pru)
mae = lambda p: mean_absolute_error(yr_pru, p)
tabla_r = pd.DataFrame({
    "modelo": ["Siempre el precio medio", "Regresión lineal (Ridge)", "MLP (32-16)"],
    "MAE (€)": [mae(np.full(len(yr_pru), yr_ent.mean())), mae(pred_ridge), mae(pred_mlp)],
}).round(2)
tabla_r
```

**Qué hace cada línea:**

- `pred_mlp = desesc(mlp_r.predict(Xr_pru, verbose=0).ravel())` → Guarda en `pred_mlp` el resultado. `desesc`: deshace el escalado de la predicción para volver a euros; `ravel`: aplana un array a una sola dimensión; `predict`: pide al modelo ya entrenado que haga predicciones.
- `ridge = Ridge().fit(Xr_ent, yr_ent)` → Guarda en `ridge` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `Ridge`: regresión lineal con penalización L2 (encoge los coeficientes).
- `pred_ridge = ridge.predict(Xr_pru)` → Guarda en `pred_ridge` el resultado. `predict`: pide al modelo ya entrenado que haga predicciones.
- `mae = lambda p: mean_absolute_error(yr_pru, p)` → Guarda en `mae` el resultado. `mean_absolute_error`: error medio absoluto (MAE): cuánto se equivoca de media, en las mismas unidades.
- `tabla_r = pd.DataFrame({` → Guarda en `tabla_r` el resultado. `round`: redondea un número a los decimales indicados; `DataFrame`: crea una tabla de pandas (filas y columnas); `mae`: error medio absoluto, en las mismas unidades que lo que se predice.

### Celda 12 · 3. Un MLP para predecir el precio por noche (re… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 3. Un MLP para predecir el precio por noche (re… · 🏠

**Qué hace:** Practica `figure`, `scatter`, `plot`, `xlabel` y más (sección «3. Un MLP para predecir el precio por n…»).

```python
plt.figure(figsize=(5, 5))
plt.scatter(yr_pru, pred_mlp, s=8, alpha=0.4)
lim = [yr_pru.min(), yr_pru.max()]
plt.plot(lim, lim, "r--", label="predicción perfecta")
plt.xlabel("precio real (€/noche)"); plt.ylabel("precio predicho (€/noche)")
plt.title("MLP de precio: real frente a predicho"); plt.legend(); plt.show()
```

**Qué hace cada línea:**

- `plt.figure(figsize=(5, 5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.scatter(yr_pru, pred_mlp, s=8, alpha=0.4)` → `scatter`: dibuja un gráfico de puntos.
- `lim = [yr_pru.min(), yr_pru.max()]` → Guarda en `lim` el resultado. `min`: devuelve el valor más pequeño; `max`: devuelve el valor más grande.
- `plt.plot(lim, lim, "r--", label="predicción perfecta")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.xlabel("precio real (€/noche)"); plt.ylabel("precio predicho (€/noche)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.xlabel("precio real (€/noche)"); plt.ylabel("precio predicho (€/noche)")` → `ylabel`: pone el nombre del eje vertical.
- `plt.title("MLP de precio: real frente a predicho"); plt.legend(); plt.show()` → `title`: pone el título del gráfico.
- `plt.title("MLP de precio: real frente a predicho"); plt.legend(); plt.show()` → `legend`: muestra la leyenda del gráfico.
- `plt.title("MLP de precio: real frente a predicho"); plt.legend(); plt.show()` → `show`: muestra el gráfico.

### Celda 14 · 4. Mini-reto integrador · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S10_02_mlp_keras.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
