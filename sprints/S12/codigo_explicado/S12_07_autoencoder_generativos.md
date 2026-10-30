# Código explicado · S12.07 · Autoencoders y modelos generativos (GAN y difusión)

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_07_autoencoder_generativos.ipynb) · [descargar](../notebooks/S12_07_autoencoder_generativos.ipynb) · ⏱ en clase: 50 min · 🏫 0 celdas de código en clase · 🏠 7 en casa
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
| `ocup` | `pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["f…` | 1 |
| `serie` | `ocup["ocupacion_pct"]` | 2 |
| `n_semanas` | `len(serie) // 7` | 2 |
| `semanas` | `serie.values[:n_semanas * 7].reshape(n_semanas, 7)` | 2 |
| `fechas_semana` | `serie.index[:n_semanas * 7:7]` | 2 |
| `ae` | `construir_autoencoder()` | 4 |
| `i` | `5` | 7 |
| `original` | `sem_test[i:i + 1]` | 7 |
| `recons` | `ae.predict(original, verbose=0)` | 7 |
| `dias` | `["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]` | 7 |
| `normal` | `semanas[corte:corte + 3].copy()` | 9 |
| `raras` | `np.array([np.full(7, 15.0), # apagón normal[0].copy(), #…` | 9 |
| `raras_esc` | `escalador.transform(raras)` | 9 |
| `err_raras` | `error_recons(ae, raras_esc)` | 9 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `construir_autoencoder` | Función definida en el cuaderno. |
| `error_recons` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `Adam` | Optimizador Adam: decide cómo ajustar los pesos en cada paso. | 4 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 9 |
| `axhline` | Dibuja una línea horizontal de referencia. | 11 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 4 |
| `copy` | Hace una copia independiente (si cambias la copia, el original no cambia). | 9 |
| `date` | Crea una fecha (año, mes, día). | 2 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `Dense` | Capa de neuronas totalmente conectadas. | 4 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `full` | Crea un array lleno del valor indicado. | 9 |
| `history` | Guarda la evolución de las métricas época a época. | 6 |
| `Input` | Define la forma de los datos de entrada del modelo. | 4 |
| `inverse_transform` | Deshace una transformación (por ejemplo, vuelve a la escala original). | 7 |
| `legend` | Muestra la leyenda del gráfico. | 6, 7, 11 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2 |
| `Model` | Crea un modelo de Keras indicando entradas y salidas. | 4 |
| `plot` | Dibuja una línea (o puntos unidos). | 6, 7, 11 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 7 |
| `print` | Muestra un valor por pantalla. | 2, 4, 9 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `reshape` | Cambia la forma de un array (filas × columnas) sin cambiar los datos. | 2 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `set_index` | Convierte una columna en el índice (la etiqueta de cada fila). | 1 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 1, 4 |
| `set_title` | Pone el título de un gráfico. | 6, 7, 11 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 6, 11 |
| `set_ylabel` | Pone el nombre del eje vertical. | 6, 7, 11 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2 |
| `show` | Muestra el gráfico. | 6, 7, 11 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 6, 7, 11 |
| `summary` | Muestra el resumen del modelo (en Keras, las capas y sus pesos; en statsmodels, coeficientes y p-valores). | 4 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 9 |
| `update` | Añade o cambia varias claves de un diccionario. | 1 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 2 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 9 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏠

**Qué hace:** Practica `filterwarnings`, `seed`, `set_random_seed`, `update` y más.

```python
import os, random, warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore")
SEMILLA = 42
random.seed(SEMILLA); np.random.seed(SEMILLA); keras.utils.set_random_seed(SEMILLA)
plt.rcParams.update({"figure.figsize": (10, 3.5), "axes.grid": True, "axes.spines.top": False, "axes.spines.right": False})

ocup = pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["fecha"]).set_index("fecha")
```

**Qué hace cada línea:**

- `import os, random, warnings` → Trae `os`, `random`, `warnings` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `from tensorflow.keras import layers` → Trae `layers` de `tensorflow.keras` para poder usarlo.
- `from sklearn.preprocessing import MinMaxScaler` → Trae `MinMaxScaler` de `sklearn.preprocessing` para poder usarlo.
- `warnings.filterwarnings("ignore")` → `filterwarnings`: silencia avisos que no aportan nada en el cuaderno.
- … y 6 más con las mismas ideas.

### Celda 2 · 1. Idea: comprimir y reconstruir · 🏠

**Qué hace:** Practica `reshape`, `shape`, `date`, `values` (sección «1. Idea: comprimir y reconstruir»).

```python
serie = ocup["ocupacion_pct"]
n_semanas = len(serie) // 7
semanas = serie.values[:n_semanas * 7].reshape(n_semanas, 7)
fechas_semana = serie.index[:n_semanas * 7:7]
print("Semanas:", semanas.shape, "| primera semana empieza el", fechas_semana[0].date())
```

**Qué hace cada línea:**

- `serie = ocup["ocupacion_pct"]` → Guarda el valor en `serie`.
- `n_semanas = len(serie) // 7` → Guarda en `n_semanas` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `semanas = serie.values[:n_semanas * 7].reshape(n_semanas, 7)` → Guarda en `semanas` el resultado. `reshape`: cambia la forma de un array (filas × columnas) sin cambiar los datos; `values`: devuelve los valores de un diccionario o de una tabla.
- `fechas_semana = serie.index[:n_semanas * 7:7]` → Guarda el valor en `fechas_semana`.
- `print("Semanas:", semanas.shape, "| primera semana empieza el", fechas_sema…` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas); `date`: crea una fecha (año, mes, día).

### Celda 3 · 1. Idea: comprimir y reconstruir · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Construir y entrenar el autoencoder · 🏠

**Qué hace:** Practica `set_random_seed`, `summary`, `Input`, `Model` y más (sección «2. Construir y entrenar el autoencoder»).

```python
def construir_autoencoder(cuello=2):
    entrada = keras.Input(shape=(7,))
    x = layers.Dense(4, activation="relu")(entrada)
    z = layers.Dense(cuello, activation="relu", name="cuello")(x)
    x = layers.Dense(4, activation="relu")(z)
    salida = layers.Dense(7, activation="sigmoid")(x)
    modelo = keras.Model(entrada, salida)
    modelo.compile(optimizer=keras.optimizers.Adam(0.01), loss="mse")
    return modelo

keras.utils.set_random_seed(SEMILLA)
ae = construir_autoencoder()
ae.summary(print_fn=lambda l: print(l))
```

**Qué hace cada línea:**

- `def construir_autoencoder(cuello=2):` → Define la función `construir_autoencoder`: Función definida en el cuaderno.
- `keras.utils.set_random_seed(SEMILLA)` → `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados.
- `ae = construir_autoencoder()` → Guarda en `ae` el resultado. `construir_autoencoder`: función definida en el cuaderno.
- `ae.summary(print_fn=lambda l: print(l))` → `summary`: muestra el resumen del modelo (en Keras, las capas y sus pesos; en statsmodels, coeficientes y p-valores); `print`: muestra un valor por pantalla.

### Celda 5 · 2. Construir y entrenar el autoencoder · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 2. Construir y entrenar el autoencoder · 🏠

**Qué hace:** Practica `subplots`, `plot`, `set_title`, `set_xlabel` y más (sección «2. Construir y entrenar el autoencoder»).

```python
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(historial.history["loss"], label="entrenamiento"); ax.plot(historial.history["val_loss"], label="validación")
ax.set_title("Error de reconstrucción durante el entrenamiento"); ax.set_xlabel("Época"); ax.set_ylabel("Error cuadrático medio"); ax.legend()
plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(figsize=(7, 3))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax.plot(historial.history["loss"], label="entrenamiento"); ax.plot(historia…` → `plot`: dibuja una línea (o puntos unidos); `history`: guarda la evolución de las métricas época a época.
- `ax.plot(historial.history["loss"], label="entrenamiento"); ax.plot(historia…` → `plot`: dibuja una línea (o puntos unidos); `history`: guarda la evolución de las métricas época a época.
- `ax.set_title("Error de reconstrucción durante el entrenamiento"); ax.set_xl…` → `set_title`: pone el título de un gráfico.
- `ax.set_title("Error de reconstrucción durante el entrenamiento"); ax.set_xl…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_title("Error de reconstrucción durante el entrenamiento"); ax.set_xl…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_title("Error de reconstrucción durante el entrenamiento"); ax.set_xl…` → `legend`: muestra la leyenda del gráfico.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 7 · 3. Ver una reconstrucción · 🏠

**Qué hace:** Practica `predict`, `subplots`, `plot`, `set_ylabel` y más (sección «3. Ver una reconstrucción»).

```python
i = 5
original = sem_test[i:i + 1]
recons = ae.predict(original, verbose=0)
dias = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(dias, escalador.inverse_transform(original)[0], "o-", label="Real")
ax.plot(dias, escalador.inverse_transform(recons)[0], "s--", label="Reconstruida")
ax.set_ylabel("Ocupación (%)"); ax.set_title("Una semana de prueba"); ax.legend()
plt.show()
```

**Qué hace cada línea:**

- `i = 5` → Guarda el valor en `i`.
- `original = sem_test[i:i + 1]` → Guarda el valor en `original`.
- `recons = ae.predict(original, verbose=0)` → Guarda en `recons` el resultado. `predict`: pide al modelo ya entrenado que haga predicciones.
- `dias = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]` → Guarda el valor en `dias`.
- `fig, ax = plt.subplots(figsize=(6, 3))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax.plot(dias, escalador.inverse_transform(original)[0], "o-", label="Real")` → `plot`: dibuja una línea (o puntos unidos); `inverse_transform`: deshace una transformación (por ejemplo, vuelve a la escala original).
- `ax.plot(dias, escalador.inverse_transform(recons)[0], "s--", label="Reconst…` → `plot`: dibuja una línea (o puntos unidos); `inverse_transform`: deshace una transformación (por ejemplo, vuelve a la escala original).
- `ax.set_ylabel("Ocupación (%)"); ax.set_title("Una semana de prueba"); ax.le…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_ylabel("Ocupación (%)"); ax.set_title("Una semana de prueba"); ax.le…` → `set_title`: pone el título de un gráfico.
- … y 2 más con las mismas ideas.

### Celda 8 · 4. Detección de anomalías · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4. Detección de anomalías · 🏠

**Qué hace:** Practica `copy`, `array`, `transform`, `zip` y más (sección «Probamos con anomalías inyectadas»).

```python
normal = semanas[corte:corte + 3].copy()
raras = np.array([np.full(7, 15.0),                              # apagón
                  normal[0].copy(),                               # día roto
                  np.array([55., 52., 54., 53., 100., 55., 53.])])  # pico irreal
raras[1, 3] = 0.0
raras_esc = escalador.transform(raras)
err_raras = error_recons(ae, raras_esc)
for nombre, e in zip(["Apagón", "Día roto", "Pico irreal"], err_raras):
    print(f"{nombre:12s} error = {e:.4f}  →  {'ANOMALÍA' if e > umbral else 'normal'}")
```

**Qué hace cada línea:**

- `normal = semanas[corte:corte + 3].copy()` → Guarda en `normal` el resultado. `copy`: hace una copia independiente (si cambias la copia, el original no cambia).
- `raras = np.array([np.full(7, 15.0), # apagón` → Guarda en `raras` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez); `full`: crea un array lleno del valor indicado; `copy`: hace una copia independiente (si cambias la copia, el original no cambia).
- `raras[1, 3] = 0.0` → Guarda el valor en `raras[1, 3]`.
- `raras_esc = escalador.transform(raras)` → Guarda en `raras_esc` el resultado. `transform`: calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado.
- `err_raras = error_recons(ae, raras_esc)` → Guarda en `err_raras` el resultado. `error_recons`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `for nombre, e in zip(["Apagón", "Día roto", "Pico irreal"], err_raras):` → Repite el bloque de debajo para cada valor de `nombre, e` en `zip(["Apagón", "Día roto", "Pico irreal…`.

### Celda 10 · 4. Detección de anomalías · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 4. Detección de anomalías · 🏠

**Qué hace:** Practica `subplots`, `plot`, `axhline`, `set_title` y más (sección «Probamos con anomalías inyectadas»).

```python
fig, ax = plt.subplots()
ax.plot(fechas_semana[corte:], err_test, "o-", ms=3, label="Semanas reales (prueba)")
ax.axhline(umbral, color="red", ls="--", label="Umbral (p95 entrenamiento)")
ax.set_title("Error de reconstrucción por semana (prueba)"); ax.set_ylabel("Error"); ax.set_xlabel("Fecha"); ax.legend()
plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots()` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax.plot(fechas_semana[corte:], err_test, "o-", ms=3, label="Semanas reales…` → `plot`: dibuja una línea (o puntos unidos).
- `ax.axhline(umbral, color="red", ls="--", label="Umbral (p95 entrenamiento)")` → `axhline`: dibuja una línea horizontal de referencia.
- `ax.set_title("Error de reconstrucción por semana (prueba)"); ax.set_ylabel(…` → `set_title`: pone el título de un gráfico.
- `ax.set_title("Error de reconstrucción por semana (prueba)"); ax.set_ylabel(…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_title("Error de reconstrucción por semana (prueba)"); ax.set_ylabel(…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_title("Error de reconstrucción por semana (prueba)"); ax.set_ylabel(…` → `legend`: muestra la leyenda del gráfico.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 12 · 5. Mini-reto integrador: ¿qué semanas reales re… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 6. Otros modelos generativos: ideas (sin entren… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S12_07_autoencoder_generativos.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
