# Código explicado · S12.02 · Redes recurrentes (RNN, LSTM, GRU) para predecir la ocupación

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_02_redes_recurrentes.ipynb) · [descargar](../notebooks/S12_02_redes_recurrentes.ipynb) · ⏱ en clase: 45 min · 🏫 8 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `filterwarnings`, `seed`, `set_random_seed`, `update` y más. |
| 2 | 2. Variables de entrada y partición tem… | Practica `DataFrame`, `values`, `sin`, `cos` (sección «2. Variables de entrada y partició… |
| 4 | 3. Escalado SIN fuga | Practica `copy`, `astype`, `shape`, `values` (sección «3. Escalado SIN fuga»). |
| 6 | 4. Ventanas deslizantes | Practica `date`, `max` (sección «4. Ventanas deslizantes»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `ocup` | `pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["f…` | 1 |
| `df` | `pd.DataFrame(index=ocup.index)` | 2 |
| `n_ent` | `len(df) - DIAS_TEST` | 2 |
| `X_feat` | `df.copy()` | 4 |
| `matriz` | `X_feat.values.astype("float32")` | 4 |
| `objetivo` | `ocup_esc.astype("float32")` | 4 |
| `pred_base` | `np.array([objetivo[o - 7:o] for o in orig_test])` | 7 |
| `mae_base` | `mae_puntos(y_test, pred_base)` | 7 |
| `mejor` | `min(resultados, key=resultados.get)` | 11 |
| `comp` | `pd.Series({**resultados, "Baseline estacional": mae_base}…` | 11 |
| `m` | `modelos[mejor][0]` | 11 |
| `pred` | `m.predict(X_test, verbose=0)` | 11 |
| `rango` | `escalador.data_max_[0] - escalador.data_min_[0]` | 11 |
| `inv` | `lambda a: a * rango + escalador.data_min_[0]` | 11 |
| `real_cont` | `inv(y_test).ravel()` | 11 |
| `pred_cont` | `inv(pred).ravel()` | 11 |
| `base_cont` | `inv(pred_base).ravel()` | 11 |
| `ind` | `df.index[orig_test[0]:orig_test[0] + len(real_cont)]` | 11 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `crear_ventanas` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `mae_puntos` | Error absoluto medio en puntos de ocupación (deshaciendo el escalado). |
| `construir` | Función definida en el cuaderno. |
| `entrenar` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `abs` | Valor absoluto: quita el signo negativo. | 7 |
| `Adam` | Optimizador Adam: decide cómo ajustar los pesos en cada paso. | 8 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 7 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 4 |
| `capa` | La clase de capa recurrente elegida (SimpleRNN, GRU o LSTM). | 8 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 8 |
| `copy` | Hace una copia independiente (si cambias la copia, el original no cambia). | 4 |
| `cos` | Coseno. | 2 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 2 |
| `date` | Crea una fecha (año, mes, día). | 6 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `Dense` | Capa de neuronas totalmente conectadas. | 8 |
| `EarlyStopping` | Para el entrenamiento cuando deja de mejorar la validación. | 8 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 8 |
| `float` | Convierte un valor en número decimal. | 7 |
| `history` | Guarda la evolución de las métricas época a época. | 10 |
| `Input` | Define la forma de los datos de entrada del modelo. | 8 |
| `inv` | Calcula la matriz inversa. | 11 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 10 |
| `legend` | Muestra la leyenda del gráfico. | 10, 11 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 1, 2, 11 |
| `max` | Devuelve el valor más grande. | 6 |
| `mean` | Calcula la media. | 7 |
| `min` | Devuelve el valor más pequeño. | 11 |
| `plot` | Dibuja una línea (o puntos unidos). | 10, 11 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 11 |
| `print` | Muestra un valor por pantalla. | 1, 2, 4, 6, 7, 11 |
| `ravel` | Aplana un array a una sola dimensión. | 11 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `round` | Redondea un número a los decimales indicados. | 11 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `Sequential` | Crea un modelo de red neuronal apilando capas una tras otra. | 8 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 11 |
| `set_index` | Convierte una columna en el índice (la etiqueta de cada fila). | 1 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 1, 8 |
| `set_title` | Pone el título de un gráfico. | 10, 11 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 10 |
| `set_ylabel` | Pone el nombre del eje vertical. | 10, 11 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 4 |
| `show` | Muestra el gráfico. | 10, 11 |
| `sin` | Seno. | 2 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 11 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 10, 11 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 10 |
| `to_string` | Convierte la tabla en texto para mostrarla entera. | 11 |
| `update` | Añade o cambia varias claves de un diccionario. | 1 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 2, 4 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 10 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `filterwarnings`, `seed`, `set_random_seed`, `update` y más.

```python
import os, random, warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore")
SEMILLA = 42
random.seed(SEMILLA); np.random.seed(SEMILLA); keras.utils.set_random_seed(SEMILLA)
plt.rcParams.update({"figure.figsize": (10, 3.5), "axes.grid": True, "axes.spines.top": False, "axes.spines.right": False})

ocup = pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["fecha"]).set_index("fecha")
print("TensorFlow", tf.__version__, "| filas:", len(ocup))
```

**Qué hace cada línea:**

- `import os, random, warnings` → Trae `os`, `random`, `warnings` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import tensorflow as tf` → Trae `tensorflow` (lo llamamos `tf`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `from tensorflow.keras import layers` → Trae `layers` de `tensorflow.keras` para poder usarlo.
- `from sklearn.preprocessing import MinMaxScaler` → Trae `MinMaxScaler` de `sklearn.preprocessing` para poder usarlo.
- … y 8 más con las mismas ideas.

### Celda 2 · 2. Variables de entrada y partición temporal · 🏫

**Qué hace:** Practica `DataFrame`, `values`, `sin`, `cos` (sección «2. Variables de entrada y partición tem…»).

```python
DIAS_TEST, VENTANA, HORIZONTE = 91, 28, 7

df = pd.DataFrame(index=ocup.index)
df["ocupacion"] = ocup["ocupacion_pct"]
df["festivo"] = ocup["festivo"]
dsem, danio = ocup.index.dayofweek.values, ocup.index.dayofyear.values
df["sem_sin"], df["sem_cos"] = np.sin(2 * np.pi * dsem / 7), np.cos(2 * np.pi * dsem / 7)
df["anio_sin"], df["anio_cos"] = np.sin(2 * np.pi * danio / 365.25), np.cos(2 * np.pi * danio / 365.25)

n_ent = len(df) - DIAS_TEST
print("Días de entrenamiento:", n_ent, "| días de prueba:", DIAS_TEST)
```

**Qué hace cada línea:**

- `DIAS_TEST, VENTANA, HORIZONTE = 91, 28, 7` → Guarda el valor en `DIAS_TEST, VENTANA, HOR…`.
- `df = pd.DataFrame(index=ocup.index)` → Guarda en `df` el resultado. `DataFrame`: crea una tabla de pandas (filas y columnas).
- `df["ocupacion"] = ocup["ocupacion_pct"]` → Guarda el valor en `df["ocupacion"]`.
- `df["festivo"] = ocup["festivo"]` → Guarda el valor en `df["festivo"]`.
- `dsem, danio = ocup.index.dayofweek.values, ocup.index.dayofyear.values` → Guarda en `dsem, danio` el resultado. `values`: devuelve los valores de un diccionario o de una tabla.
- `df["sem_sin"], df["sem_cos"] = np.sin(2 * np.pi * dsem / 7), np.cos(2 * np.…` → Guarda en `df["sem_sin"], df["sem_…` el resultado. `sin`: seno; `cos`: coseno.
- `df["anio_sin"], df["anio_cos"] = np.sin(2 * np.pi * danio / 365.25), np.cos…` → Guarda en `df["anio_sin"], df["ani…` el resultado. `sin`: seno; `cos`: coseno.
- `n_ent = len(df) - DIAS_TEST` → Guarda en `n_ent` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `print("Días de entrenamiento:", n_ent, "| días de prueba:", DIAS_TEST)` → `print`: muestra un valor por pantalla.

### Celda 3 · 3. Escalado SIN fuga · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3. Escalado SIN fuga · 🏫

**Qué hace:** Practica `copy`, `astype`, `shape`, `values` (sección «3. Escalado SIN fuga»).

```python
X_feat = df.copy()
X_feat["ocupacion"] = ocup_esc
matriz = X_feat.values.astype("float32")          # (días, 6 variables)
objetivo = ocup_esc.astype("float32")             # lo que queremos predecir
print("Matriz de variables:", matriz.shape)
```

**Qué hace cada línea:**

- `X_feat = df.copy()` → Guarda en `X_feat` el resultado. `copy`: hace una copia independiente (si cambias la copia, el original no cambia).
- `X_feat["ocupacion"] = ocup_esc` → Guarda el valor en `X_feat["ocupacion"]`.
- `matriz = X_feat.values.astype("float32") # (días, 6 variables)` → Guarda en `matriz` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `values`: devuelve los valores de un diccionario o de una tabla.
- `objetivo = ocup_esc.astype("float32") # lo que queremos predecir` → Guarda en `objetivo` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número).
- `print("Matriz de variables:", matriz.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).

### Celda 5 · 4. Ventanas deslizantes · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 4. Ventanas deslizantes · 🏫

**Qué hace:** Practica `date`, `max` (sección «4. Ventanas deslizantes»).

```python
assert max(orig_ent) + HORIZONTE - 1 < n_ent, "Fuga: una ventana de entrenamiento llega a días de prueba."
print("Sin fuga: el último día usado en entrenamiento es", df.index[max(orig_ent) + HORIZONTE - 1].date(),
      "y la prueba empieza el", df.index[n_ent].date())
```

**Qué hace cada línea:**

- `assert max(orig_ent) + HORIZONTE - 1 < n_ent, "Fuga: una ventana de entrena…` → Comprueba que es verdad; si no, para con un mensaje.
- `print("Sin fuga: el último día usado en entrenamiento es", df.index[max(ori…` → `print`: muestra un valor por pantalla; `date`: crea una fecha (año, mes, día); `max`: devuelve el valor más grande.

### Celda 7 · 5. Baseline en la misma escala de evaluación · 🏫

**Qué hace:** Practica `array`, `mean`, `abs` (sección «5. Baseline en la misma escala de evalu…»).

```python
def mae_puntos(y_esc, pred_esc):
    """Error absoluto medio en puntos de ocupación (deshaciendo el escalado)."""
    rango = escalador.data_max_[0] - escalador.data_min_[0]
    return float(np.mean(np.abs(y_esc - pred_esc)) * rango)

pred_base = np.array([objetivo[o - 7:o] for o in orig_test])       # última semana conocida
mae_base = mae_puntos(y_test, pred_base)
print(f"MAE baseline estacional: {mae_base:.2f} puntos")
```

**Qué hace cada línea:**

- `def mae_puntos(y_esc, pred_esc):` → Define la función `mae_puntos`: Error absoluto medio en puntos de ocupación (deshaciendo el escalado).
- `pred_base = np.array([objetivo[o - 7:o] for o in orig_test]) # última seman…` → Guarda en `pred_base` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `mae_base = mae_puntos(y_test, pred_base)` → Guarda en `mae_base` el resultado. `mae_puntos`: error absoluto medio en puntos de ocupación (deshaciendo el escalado).
- `print(f"MAE baseline estacional: {mae_base:.2f} puntos")` → `print`: muestra un valor por pantalla.

### Celda 8 · 6. Construir y entrenar las tres redes · 🏫

**Qué hace:** Practica `Sequential`, `compile`, `set_random_seed`, `EarlyStopping` y más (sección «6. Construir y entrenar las tres redes»).

```python
def construir(tipo):
    capa = {"SimpleRNN": layers.SimpleRNN, "LSTM": layers.LSTM, "GRU": layers.GRU}[tipo]
    modelo = keras.Sequential([
        layers.Input(shape=(VENTANA, 6)),
        capa(32),
        layers.Dense(HORIZONTE),
    ])
    modelo.compile(optimizer=keras.optimizers.Adam(0.005), loss="mae")
    return modelo

def entrenar(tipo, epocas=40):
    keras.utils.set_random_seed(SEMILLA)
    m = construir(tipo)
    n_val = 60
    parada = keras.callbacks.EarlyStopping(patience=6, restore_best_weights=True, monitor="val_loss")
    h = m.fit(X_ent[:-n_val], y_ent[:-n_val], validation_data=(X_ent[-n_val:], y_ent[-n_val:]),
              epochs=epocas, batch_size=32, shuffle=True, callbacks=[parada], verbose=0)
    return m, h
```

**Qué hace cada línea:**

- `def construir(tipo):` → Define la función `construir`: Función definida en el cuaderno.
- `def entrenar(tipo, epocas=40):` → Define la función `entrenar`: Función definida en el cuaderno.

### Celda 9 · 6. Construir y entrenar las tres redes · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 6. Construir y entrenar las tres redes · 🏫

**Qué hace:** Practica `subplots`, `zip`, `set_ylabel`, `legend` y más (sección «6. Construir y entrenar las tres redes»).

```python
fig, ejes = plt.subplots(1, 3, figsize=(12, 3), sharey=True)
for ax, (nombre, (m, h)) in zip(ejes, modelos.items()):
    ax.plot(h.history["loss"], label="entrenamiento"); ax.plot(h.history["val_loss"], label="validación")
    ax.set_title(nombre); ax.set_xlabel("Época")
ejes[0].set_ylabel("Error (MAE, escala 0-1)"); ejes[0].legend()
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ejes = plt.subplots(1, 3, figsize=(12, 3), sharey=True)` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for ax, (nombre, (m, h)) in zip(ejes, modelos.items()):` → Repite el bloque de debajo para cada valor de `ax, (nombre, (m, h))` en `zip(ejes, modelos.items())`. Dentro del bloque: `plot`: dibuja una línea (o puntos unidos); `history`: guarda la evolución de las métricas época a época; `set_title`: pone el título de un gráfico.
- `ejes[0].set_ylabel("Error (MAE, escala 0-1)"); ejes[0].legend()` → `set_ylabel`: pone el nombre del eje vertical.
- `ejes[0].set_ylabel("Error (MAE, escala 0-1)"); ejes[0].legend()` → `legend`: muestra la leyenda del gráfico.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 11 · 7. Comparar con el baseline y mirar una previsi… · 🏫

**Qué hace:** Practica `min`, `sort_values`, `predict`, `subplots` y más (sección «7. Comparar con el baseline y mirar una…»).

```python
mejor = min(resultados, key=resultados.get)
comp = pd.Series({**resultados, "Baseline estacional": mae_base}).sort_values()
print(comp.round(2).to_string())

m = modelos[mejor][0]
pred = m.predict(X_test, verbose=0)
rango = escalador.data_max_[0] - escalador.data_min_[0]
inv = lambda a: a * rango + escalador.data_min_[0]
fig, ax = plt.subplots()
real_cont = inv(y_test).ravel(); pred_cont = inv(pred).ravel(); base_cont = inv(pred_base).ravel()
ind = df.index[orig_test[0]:orig_test[0] + len(real_cont)]
ax.plot(ind, real_cont, color="black", label="Real"); ax.plot(ind, base_cont, alpha=.7, label="Baseline t-7")
ax.plot(ind, pred_cont, label=f"Red {mejor}")
ax.set_title("Previsión a 7 días (últimas 13 semanas)"); ax.set_ylabel("Ocupación (%)"); ax.legend()
plt.show()
```

**Qué hace cada línea:**

- `mejor = min(resultados, key=resultados.get)` → Guarda en `mejor` el resultado. `min`: devuelve el valor más pequeño.
- `comp = pd.Series({**resultados, "Baseline estacional": mae_base}).sort_valu…` → Guarda en `comp` el resultado. `sort_values`: ordena la tabla por una o varias columnas; `Series`: crea una columna de pandas (una sola serie de valores).
- `print(comp.round(2).to_string())` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `round`: redondea un número a los decimales indicados.
- `m = modelos[mejor][0]` → Guarda el valor en `m`.
- `pred = m.predict(X_test, verbose=0)` → Guarda en `pred` el resultado. `predict`: pide al modelo ya entrenado que haga predicciones.
- `rango = escalador.data_max_[0] - escalador.data_min_[0]` → Guarda el valor en `rango`.
- `inv = lambda a: a * rango + escalador.data_min_[0]` → Guarda el valor en `inv`.
- `fig, ax = plt.subplots()` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `real_cont = inv(y_test).ravel(); pred_cont = inv(pred).ravel(); base_cont =…` → Guarda en `real_cont` el resultado. `ravel`: aplana un array a una sola dimensión; `inv`: calcula la matriz inversa.
- … y 10 más con las mismas ideas.

### Celda 12 · 8. Mini-reto integrador · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S12_02_redes_recurrentes.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
