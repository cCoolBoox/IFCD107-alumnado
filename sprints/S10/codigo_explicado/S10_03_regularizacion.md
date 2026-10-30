# Código explicado · S10.03 · S10 · Práctica 3 — Entrenar bien: sobreajuste, regularización y callbacks

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_03_regularizacion.ipynb) · [descargar](../notebooks/S10_03_regularizacion.ipynb) · ⏱ en clase: 55 min · 🏫 6 celdas de código en clase · 🏠 3 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_random_seed`. |
| 2 | 0. Datos: el mismo preprocesado de la p… | Practica `read_csv`, `train_test_split`, `ColumnTransformer`, `astype` y más (sección «0.… |
| 3 | 1. Provocar y diagnosticar el sobreajus… | Practica `Sequential`, `add`, `compile`, `set_random_seed` y más (sección «1. Provocar y… |
| 4 | 1. Provocar y diagnosticar el sobreajus… | Practica `figure` (sección «1. Provocar y diagnosticar el sobreajus…»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 2 |
| `num` | `["antelacion_dias", "noches", "adultos", "ninos", "petici…` | 2 |
| `cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 2 |
| `pre` | `ColumnTransformer([("n", StandardScaler(), num), ("c", On…` | 2 |
| `A_ent` | `pre.fit_transform(X_ent).astype("float32")` | 2 |
| `A_val` | `pre.transform(X_val).astype("float32")` | 2 |
| `configs` | `{ "Sin regularizar": dict(), "L2 = 0.01": dict(l2=0.01),…` | 7 |
| `resultados` | `{}` | 7 |
| `resumen` | `pd.DataFrame({ nombre: {"mejor pérdida val.": min(h["val_…` | 7 |
| `filas` | `[]` | 10 |
| `perdida_referencia` | `h_ref.history["val_loss"][-1]` | 13 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `construir` | MLP de clasificación con regularización opcional. |
| `entrenar` | Función definida en el cuaderno. |
| `curvas` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `Activation` | Capa que aplica una función de activación. | 3 |
| `Adam` | Optimizador Adam: decide cómo ajustar los pesos en cada paso. | 3 |
| `add` | Añade una capa al modelo de Keras (o un elemento a un conjunto). | 3 |
| `append` | Añade un elemento al final de una lista. | 10 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 2 |
| `AUC` | Métrica AUC que Keras calcula mientras entrena. | 3 |
| `BatchNormalization` | Capa que normaliza lo que recibe para estabilizar el entrenamiento. | 3 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 2 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 3 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 7, 10 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `Dense` | Capa de neuronas totalmente conectadas. | 3 |
| `dict` | Crea un diccionario (parejas nombre: valor). | 7 |
| `Dropout` | Capa que apaga neuronas al azar al entrenar para evitar el sobreajuste. | 3 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 2 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 4 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 3 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 2 |
| `gca` | Obtiene el eje (gráfico) activo. | 3 |
| `history` | Guarda la evolución de las métricas época a época. | 3, 7, 9, 10, 13 |
| `Input` | Define la forma de los datos de entrada del modelo. | 3 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 7 |
| `l2` | Regularización L2: penaliza los pesos grandes para evitar el sobreajuste. | 3 |
| `legend` | Muestra la leyenda del gráfico. | 3, 10 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 7 |
| `max` | Devuelve el valor más grande. | 7 |
| `min` | Devuelve el valor más pequeño. | 7, 13 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 2 |
| `plot` | Dibuja una línea (o puntos unidos). | 3, 9, 10 |
| `print` | Muestra un valor por pantalla. | 2, 13 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `rmtree` | Borra una carpeta con todo lo que contiene. | 12 |
| `round` | Redondea un número a los decimales indicados. | 7, 10, 13 |
| `Sequential` | Crea un modelo de red neuronal apilando capas una tras otra. | 3 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 1, 3 |
| `set_title` | Pone el título de un gráfico. | 3, 9, 10 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 3, 9, 10 |
| `set_ylabel` | Pone el nombre del eje vertical. | 3, 9, 10 |
| `set_yscale` | Cambia la escala del eje vertical (por ejemplo, logarítmica). | 9 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2, 3 |
| `show` | Muestra el gráfico. | 4, 7, 9, 10 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 2 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 7, 9, 10 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 7, 9, 10 |
| `time` | Devuelve la hora actual en segundos (sirve para medir cuánto tarda algo). | 10 |
| `to_numpy` | Convierte una tabla o columna de pandas en un array de NumPy. | 2 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 2 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 2 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_random_seed`.

```python
import os, tempfile
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

SEMILLA = 42
keras.utils.set_random_seed(SEMILLA)
```

**Qué hace cada línea:**

- `import os, tempfile` → Trae `os`, `tempfile` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder` → Trae `StandardScaler`, `OneHotEncoder` de `sklearn.preprocessing` para poder usarlo.
- … y 2 más con las mismas ideas.

### Celda 2 · 0. Datos: el mismo preprocesado de la práctica… · 🏫

**Qué hace:** Practica `read_csv`, `train_test_split`, `ColumnTransformer`, `astype` y más (sección «0. Datos: el mismo preprocesado de la p…»).

```python
df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especiales", "cliente_repetidor",
       "cancelaciones_previas", "mes_llegada", "precio_noche"]
cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[num + cat], df["cancelada"].to_numpy()
X_res, _, y_res, _ = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)   # se descarta la prueba
X_ent, X_val, y_ent, y_val = train_test_split(X_res, y_res, test_size=0.2, random_state=SEMILLA, stratify=y_res)
pre = ColumnTransformer([("n", StandardScaler(), num), ("c", OneHotEncoder(handle_unknown="ignore"), cat)])
A_ent = pre.fit_transform(X_ent).astype("float32")
A_val = pre.transform(X_val).astype("float32")

A_peq, y_peq = A_ent[:800], y_ent[:800]     # entrenamiento pequeño para provocar sobreajuste
print("Entrenamiento pequeño:", A_peq.shape, "· Entrenamiento completo:", A_ent.shape, "· Validación:", A_val.shape)
```

**Qué hace cada línea:**

- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_llegad…` → Guarda en `df` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `df["mes_llegada"] = df["fecha_llegada"].dt.month` → Guarda en `df["mes_llegada"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especia…` → Guarda el valor en `num`.
- `cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "dep…` → Guarda el valor en `cat`.
- `X, y = df[num + cat], df["cancelada"].to_numpy()` → Guarda en `X, y` el resultado. `to_numpy`: convierte una tabla o columna de pandas en un array de NumPy.
- `X_res, _, y_res, _ = train_test_split(X, y, test_size=0.2, random_state=SEM…` → Guarda en `X_res, _, y_res, _` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `X_ent, X_val, y_ent, y_val = train_test_split(X_res, y_res, test_size=0.2,…` → Guarda en `X_ent, X_val, y_ent, y_…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `pre = ColumnTransformer([("n", StandardScaler(), num), ("c", OneHotEncoder(…` → Guarda en `pre` el resultado. `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas; `StandardScaler`: escala los números para que tengan media 0 y desviación 1; `OneHotEncoder`: convierte categorías en columnas de 0/1.
- `A_ent = pre.fit_transform(X_ent).astype("float32")` → Guarda en `A_ent` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- … y 3 más con las mismas ideas.

### Celda 3 · 1. Provocar y diagnosticar el sobreajuste · 🏫

**Qué hace:** Practica `Sequential`, `add`, `compile`, `set_random_seed` y más (sección «1. Provocar y diagnosticar el sobreajus…»).

```python
def construir(n_entradas, capas=(256, 128), l2=0.0, dropout=0.0, batchnorm=False, tasa=1e-3):
    """MLP de clasificación con regularización opcional."""
    reg = keras.regularizers.l2(l2) if l2 > 0 else None
    m = keras.Sequential([keras.layers.Input(shape=(n_entradas,))])
    for u in capas:
        m.add(keras.layers.Dense(u, activation="relu", kernel_regularizer=reg, use_bias=not batchnorm))
        if batchnorm:
            m.add(keras.layers.BatchNormalization())
            m.add(keras.layers.Activation("relu"))   # (se vuelve a aplicar ReLU tras normalizar)
        if dropout > 0:
            m.add(keras.layers.Dropout(dropout))
    m.add(keras.layers.Dense(1, activation="sigmoid"))
    m.compile(optimizer=keras.optimizers.Adam(tasa), loss="binary_crossentropy",
              metrics=[keras.metrics.AUC(name="auc")])
    return m

def entrenar(A, y_, epocas=60, lote=32, callbacks=None, **cfg):
    keras.utils.set_random_seed(SEMILLA)
    m = construir(A.shape[1], **cfg)
    h = m.fit(A, y_, validation_data=(A_val, y_val), epochs=epocas, batch_size=lote,
              callbacks=callbacks, verbose=0)
    return m, h

def curvas(h, titulo, ax=None):
    ax = ax or plt.gca()
    ax.plot(h.history["loss"], label="entrenamiento")
    ax.plot(h.history["val_loss"], label="validación")
    ax.set_xlabel("época"); ax.set_ylabel("pérdida"); ax.set_title(titulo); ax.legend()
```

**Qué hace cada línea:**

- `def construir(n_entradas, capas=(256, 128), l2=0.0, dropout=0.0, batchnorm=…` → Define la función `construir`: MLP de clasificación con regularización opcional.
- `def entrenar(A, y_, epocas=60, lote=32, callbacks=None, **cfg):` → Define la función `entrenar`: Función definida en el cuaderno.
- `def curvas(h, titulo, ax=None):` → Define la función `curvas`: Función definida en el cuaderno.

### Celda 4 · 1. Provocar y diagnosticar el sobreajuste · 🏫

**Qué hace:** Practica `figure` (sección «1. Provocar y diagnosticar el sobreajus…»).

```python
m_base, h_base = entrenar(A_peq, y_peq, epocas=60)
plt.figure(figsize=(6, 4)); curvas(h_base, "Red grande y pocos datos: sobreajuste"); plt.show()
```

**Qué hace cada línea:**

- `m_base, h_base = entrenar(A_peq, y_peq, epocas=60)` → Guarda en `m_base, h_base` el resultado. `entrenar`: función definida en el cuaderno.
- `plt.figure(figsize=(6, 4)); curvas(h_base, "Red grande y pocos datos: sobre…` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.figure(figsize=(6, 4)); curvas(h_base, "Red grande y pocos datos: sobre…` → `curvas`: función definida en el cuaderno.
- `plt.figure(figsize=(6, 4)); curvas(h_base, "Red grande y pocos datos: sobre…` → `show`: muestra el gráfico.

### Celda 5 · 1. Provocar y diagnosticar el sobreajuste · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 2. Las herramientas de regularización · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 2. Las herramientas de regularización · 🏫

**Qué hace:** Practica `subplots`, `zip`, `tight_layout`, `round` y más (sección «2. Las herramientas de regularización»).

```python
configs = {
    "Sin regularizar": dict(),
    "L2 = 0.01": dict(l2=0.01),
    "Dropout 0.4": dict(dropout=0.4),
    "BatchNorm": dict(batchnorm=True),
    "L2 + Dropout": dict(l2=0.005, dropout=0.3),
}
resultados = {}
fig, ejes = plt.subplots(1, len(configs), figsize=(4 * len(configs), 3.6), sharey=True)
for eje, (nombre, cfg) in zip(ejes, configs.items()):
    m, h = entrenar(A_peq, y_peq, epocas=60, **cfg)
    resultados[nombre] = h.history
    curvas(h, nombre, eje)
plt.tight_layout(); plt.show()

resumen = pd.DataFrame({
    nombre: {"mejor pérdida val.": min(h["val_loss"]), "pérdida val. final": h["val_loss"][-1],
             "AUC val. final": h["val_auc"][-1], "AUC val. máximo": max(h["val_auc"])}
    for nombre, h in resultados.items()
}).T.round(3)
resumen
```

**Qué hace cada línea:**

- `configs = {` → Guarda en `configs` el resultado. `dict`: crea un diccionario (parejas nombre: valor).
- `resultados = {}` → Guarda el valor en `resultados`.
- `fig, ejes = plt.subplots(1, len(configs), figsize=(4 * len(configs), 3.6),…` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `for eje, (nombre, cfg) in zip(ejes, configs.items()):` → Repite el bloque de debajo para cada valor de `eje, (nombre, cfg)` en `zip(ejes, configs.items())`. Dentro del bloque: `entrenar`: función definida en el cuaderno; `history`: guarda la evolución de las métricas época a época; `curvas`: función definida en el cuaderno.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.
- `resumen = pd.DataFrame({` → Guarda en `resumen` el resultado. `round`: redondea un número a los decimales indicados; `DataFrame`: crea una tabla de pandas (filas y columnas); `min`: devuelve el valor más pequeño.

### Celda 8 · 3. Parada temprana y callbacks · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 3. Parada temprana y callbacks · 🏫

**Qué hace:** Practica `subplots`, `tight_layout`, `history`, `plot` y más (sección «3. Parada temprana y callbacks»).

```python
fig, ejes = plt.subplots(1, 2, figsize=(11, 3.6))
curvas(h_es, "Con EarlyStopping y ReduceLROnPlateau", ejes[0])
if "learning_rate" in h_es.history:
    ejes[1].plot(h_es.history["learning_rate"]); ejes[1].set_yscale("log")
    ejes[1].set_xlabel("época"); ejes[1].set_ylabel("tasa de aprendizaje"); ejes[1].set_title("Cómo bajó la tasa")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ejes = plt.subplots(1, 2, figsize=(11, 3.6))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `curvas(h_es, "Con EarlyStopping y ReduceLROnPlateau", ejes[0])` → `curvas`: función definida en el cuaderno.
- `if "learning_rate" in h_es.history:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `plot`: dibuja una línea (o puntos unidos); `history`: guarda la evolución de las métricas época a época; `set_yscale`: cambia la escala del eje vertical (por ejemplo, logarítmica).
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 10 · 4. Tasa de aprendizaje y tamaño de lote · 🏠

**Qué hace:** Practica `subplots`, `set_xlabel`, `set_ylabel`, `set_title` y más (sección «4. Tasa de aprendizaje y tamaño de lote»).

```python
import time
filas = []
fig, ejes = plt.subplots(1, 2, figsize=(11, 3.8))
for tasa in (1e-1, 1e-2, 1e-3, 1e-4):
    t0 = time.time()
    _, h = entrenar(A_ent, y_ent, epocas=15, lote=64, capas=(64, 32), tasa=tasa)
    ejes[0].plot(h.history["val_loss"], label=f"tasa {tasa:g}")
    filas.append({"parámetro": f"tasa {tasa:g}", "AUC val. final": h.history["val_auc"][-1], "segundos": time.time() - t0})
ejes[0].set_xlabel("época"); ejes[0].set_ylabel("pérdida de validación"); ejes[0].set_title("Efecto de la tasa de aprendizaje"); ejes[0].legend()
for lote in (32, 128, 512):
    t0 = time.time()
    _, h = entrenar(A_ent, y_ent, epocas=15, lote=lote, capas=(64, 32))
    ejes[1].plot(h.history["val_loss"], label=f"lote {lote}")
    filas.append({"parámetro": f"lote {lote}", "AUC val. final": h.history["val_auc"][-1], "segundos": time.time() - t0})
ejes[1].set_xlabel("época"); ejes[1].set_ylabel("pérdida de validación"); ejes[1].set_title("Efecto del tamaño de lote"); ejes[1].legend()
plt.tight_layout(); plt.show()
pd.DataFrame(filas).round(3)
```

**Qué hace cada línea:**

- `import time` → Trae `time` para poder usarlo.
- `filas = []` → Guarda el valor en `filas`.
- `fig, ejes = plt.subplots(1, 2, figsize=(11, 3.8))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for tasa in (1e-1, 1e-2, 1e-3, 1e-4):` → Repite el bloque de debajo para cada valor de `tasa` en `(1e-1, 1e-2, 1e-3, 1e-4)`. Dentro del bloque: `time`: devuelve la hora actual en segundos (sirve para medir cuánto tarda algo); `entrenar`: función definida en el cuaderno; `plot`: dibuja una línea (o puntos unidos).
- `ejes[0].set_xlabel("época"); ejes[0].set_ylabel("pérdida de validación"); e…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ejes[0].set_xlabel("época"); ejes[0].set_ylabel("pérdida de validación"); e…` → `set_ylabel`: pone el nombre del eje vertical.
- `ejes[0].set_xlabel("época"); ejes[0].set_ylabel("pérdida de validación"); e…` → `set_title`: pone el título de un gráfico.
- `ejes[0].set_xlabel("época"); ejes[0].set_ylabel("pérdida de validación"); e…` → `legend`: muestra la leyenda del gráfico.
- `for lote in (32, 128, 512):` → Repite el bloque de debajo para cada valor de `lote` en `(32, 128, 512)`. Dentro del bloque: `time`: devuelve la hora actual en segundos (sirve para medir cuánto tarda algo); `entrenar`: función definida en el cuaderno; `plot`: dibuja una línea (o puntos unidos).
- … y 7 más con las mismas ideas.

### Celda 11 · 5. Guardar y cargar un modelo · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 12 · 5. Guardar y cargar un modelo · 🏠

**Qué hace:** Limpieza del archivo temporal (en tu proyecto real, conserva el modelo).

```python
# Limpieza del archivo temporal (en tu proyecto real, conserva el modelo)
import shutil
shutil.rmtree(carpeta_tmp, ignore_errors=True)
```

**Qué hace cada línea:**

- `import shutil` → Trae `shutil` para poder usarlo.
- `shutil.rmtree(carpeta_tmp, ignore_errors=True)` → `rmtree`: borra una carpeta con todo lo que contiene.

### Celda 13 · 6. Mini-reto integrador: gana la red · 🏠

**Qué hace:** Practica `round`, `history`, `min` (sección «6. Mini-reto integrador: gana la red»).

```python
_, h_ref = entrenar(A_ent, y_ent, epocas=40, lote=64, capas=(256, 128))
perdida_referencia = h_ref.history["val_loss"][-1]     # lo que obtendrías entrenando "a ciegas" hasta el final
print("Referencia (sin regularizar), pérdida de validación tras 40 épocas:", round(perdida_referencia, 4),
      "· la mejor había sido", round(min(h_ref.history["val_loss"]), 4))
```

**Qué hace cada línea:**

- `_, h_ref = entrenar(A_ent, y_ent, epocas=40, lote=64, capas=(256, 128))` → Guarda en `_, h_ref` el resultado. `entrenar`: función definida en el cuaderno.
- `perdida_referencia = h_ref.history["val_loss"][-1] # lo que obtendrías entr…` → Guarda en `perdida_referencia` el resultado. `history`: guarda la evolución de las métricas época a época.
- `print("Referencia (sin regularizar), pérdida de validación tras 40 épocas:"…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `min`: devuelve el valor más pequeño.

### Celda 14 · 6. Mini-reto integrador: gana la red · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S10_03_regularizacion.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
