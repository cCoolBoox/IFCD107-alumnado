# Código explicado · S10.04 · S10 · Reto PBL — ¿Vale la pena la red?

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb) · [descargar](../notebooks/S10_04_reto_vale_la_pena.ipynb) · 🏫 8 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_random_seed`. |
| 2 | 1. Datos y partición (la misma para tod… | Practica `read_csv`, `train_test_split`, `ColumnTransformer`, `astype` y más (sección «1.… |
| 4 | 3. La referencia: boosting de árboles | Practica `time`, `HistGradientBoostingClassifier`, `fit`, `predict_proba` y más (sección… |
| 5 | 4. El MLP, con las buenas prácticas del… | Practica `Sequential`, `add`, `compile`, `set_random_seed` y más (sección «4. El MLP, con… |

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
| `A_pru` | `pre.transform(X_pru).astype("float32")` | 2 |
| `t0` | `time.time()` | 4 |
| `boost` | `HistGradientBoostingClassifier(max_iter=200, learning_rat…` | 4 |
| `t_boost` | `time.time() - t0` | 4 |
| `prob_mlp_pru` | `np.mean([m.predict(A_pru, verbose=0).ravel() for m in mod…` | 9 |
| `tabla` | `pd.DataFrame({"Boosting de árboles": evaluar(y_pru, prob_…` | 9 |
| `rng` | `np.random.default_rng(SEMILLA)` | 10 |
| `difs` | `[]` | 10 |
| `num_r` | `[c for c in num if c != "precio_noche"]` | 12 |
| `Xr` | `df[num_r + cat]` | 12 |
| `yr` | `df["precio_noche"].to_numpy()` | 12 |
| `pre_r` | `ColumnTransformer([("n", StandardScaler(), num_r), ("c",…` | 12 |
| `Ar_res` | `pre_r.fit_transform(Xr_res).astype("float32")` | 12 |
| `Ar_pru` | `pre_r.transform(Xr_pru).astype("float32")` | 12 |
| `boost_r` | `HistGradientBoostingRegressor(max_iter=200, learning_rate…` | 12 |
| `ridge_r` | `Ridge().fit(Ar_res, yr_res)` | 12 |
| `mlp_r` | `keras.Sequential([keras.layers.Input(shape=(Ar_res.shape[…` | 12 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `evaluar` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `construir_mlp` | Función definida en el cuaderno. |
| `diagnostico` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `_H` | Clase definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `__init__` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `Adam` | Optimizador Adam: decide cómo ajustar los pesos en cada paso. | 5 |
| `add` | Añade una capa al modelo de Keras (o un elemento a un conjunto). | 5 |
| `append` | Añade un elemento al final de una lista. | 5, 10 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 2, 12 |
| `AUC` | Métrica AUC que Keras calcula mientras entrena. | 5 |
| `axvline` | Dibuja una línea vertical de referencia. | 10 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 2, 12 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 5, 12 |
| `count_params` | Cuenta cuántos pesos tiene el modelo. | 9 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 9, 12 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 10 |
| `Dense` | Capa de neuronas totalmente conectadas. | 5, 12 |
| `Dropout` | Capa que apaga neuronas al azar al entrenar para evitar el sobreajuste. | 5 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 2 |
| `EarlyStopping` | Para el entrenamiento cuando deja de mejorar la validación. | 5, 12 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 4, 5, 12 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 2, 12 |
| `hist` | Dibuja un histograma (cuántos datos caen en cada intervalo). | 10 |
| `HistGradientBoostingClassifier` | Boosting de árboles rápido de scikit-learn. | 4 |
| `HistGradientBoostingRegressor` | Boosting de árboles rápido de scikit-learn para predecir números. | 12 |
| `history` | Guarda la evolución de las métricas época a época. | 5, 7 |
| `Input` | Define la forma de los datos de entrada del modelo. | 5, 12 |
| `integers` | Genera números enteros aleatorios. | 10 |
| `l2` | Regularización L2: penaliza los pesos grandes para evitar el sobreajuste. | 5 |
| `legend` | Muestra la leyenda del gráfico. | 7, 10 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 5, 10 |
| `max` | Devuelve el valor más grande. | 5 |
| `mean` | Calcula la media. | 9, 10, 12 |
| `mean_absolute_error` | Error medio absoluto (MAE): cuánto se equivoca de media, en las mismas unidades. | 12 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 2, 12 |
| `percentile` | Calcula un percentil (el valor bajo el que queda ese % de los datos). | 10 |
| `plot` | Dibuja una línea (o puntos unidos). | 7 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 9, 12 |
| `predict_proba` | Pide la probabilidad de cada clase (no solo la clase). | 4 |
| `print` | Muestra un valor por pantalla. | 2, 4, 5, 10 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 10 |
| `ravel` | Aplana un array a una sola dimensión. | 9, 12 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `Ridge` | Regresión lineal con penalización L2 (encoge los coeficientes). | 12 |
| `roc_auc_score` | Calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar). | 4, 10 |
| `round` | Redondea un número a los decimales indicados. | 9, 12 |
| `Sequential` | Crea un modelo de red neuronal apilando capas una tras otra. | 5, 12 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 1, 5, 12 |
| `set_title` | Pone el título de un gráfico. | 7 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 7 |
| `set_ylabel` | Pone el nombre del eje vertical. | 7 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2, 5, 12 |
| `show` | Muestra el gráfico. | 7, 10 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 2, 12 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 12 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 7 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 7 |
| `time` | Devuelve la hora actual en segundos (sirve para medir cuánto tarda algo). | 4, 5 |
| `title` | Pone el título del gráfico. | 10 |
| `to_numpy` | Convierte una tabla o columna de pandas en un array de NumPy. | 2, 12 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 2, 12 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 2, 12 |
| `unique` | Devuelve los valores distintos. | 10 |
| `xlabel` | Pone el nombre del eje horizontal. | 10 |
| `ylabel` | Pone el nombre del eje vertical. | 10 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_random_seed`.

```python
import os, time
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score, accuracy_score, mean_absolute_error

SEMILLA = 42
keras.utils.set_random_seed(SEMILLA)
```

**Qué hace cada línea:**

- `import os, time` → Trae `os`, `time` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder` → Trae `StandardScaler`, `OneHotEncoder` de `sklearn.preprocessing` para poder usarlo.
- … y 5 más con las mismas ideas.

### Celda 2 · 1. Datos y partición (la misma para todos los m… · 🏫

**Qué hace:** Practica `read_csv`, `train_test_split`, `ColumnTransformer`, `astype` y más (sección «1. Datos y partición (la misma para tod…»).

```python
df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especiales", "cliente_repetidor",
       "cancelaciones_previas", "mes_llegada", "precio_noche"]
cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[num + cat], df["cancelada"].to_numpy()
X_res, X_pru, y_res, y_pru = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
X_ent, X_val, y_ent, y_val = train_test_split(X_res, y_res, test_size=0.2, random_state=SEMILLA, stratify=y_res)
pre = ColumnTransformer([("n", StandardScaler(), num), ("c", OneHotEncoder(handle_unknown="ignore"), cat)])
A_ent = pre.fit_transform(X_ent).astype("float32")
A_val = pre.transform(X_val).astype("float32")
A_pru = pre.transform(X_pru).astype("float32")
print(A_ent.shape, A_val.shape, A_pru.shape)
```

**Qué hace cada línea:**

- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_llegad…` → Guarda en `df` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `df["mes_llegada"] = df["fecha_llegada"].dt.month` → Guarda en `df["mes_llegada"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especia…` → Guarda el valor en `num`.
- `cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "dep…` → Guarda el valor en `cat`.
- `X, y = df[num + cat], df["cancelada"].to_numpy()` → Guarda en `X, y` el resultado. `to_numpy`: convierte una tabla o columna de pandas en un array de NumPy.
- `X_res, X_pru, y_res, y_pru = train_test_split(X, y, test_size=0.2, random_s…` → Guarda en `X_res, X_pru, y_res, y_…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `X_ent, X_val, y_ent, y_val = train_test_split(X_res, y_res, test_size=0.2,…` → Guarda en `X_ent, X_val, y_ent, y_…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `pre = ColumnTransformer([("n", StandardScaler(), num), ("c", OneHotEncoder(…` → Guarda en `pre` el resultado. `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas; `StandardScaler`: escala los números para que tengan media 0 y desviación 1; `OneHotEncoder`: convierte categorías en columnas de 0/1.
- `A_ent = pre.fit_transform(X_ent).astype("float32")` → Guarda en `A_ent` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- … y 3 más con las mismas ideas.

### Celda 3 · 2. Una función para evaluar a todos por igual · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3. La referencia: boosting de árboles · 🏫

**Qué hace:** Practica `time`, `HistGradientBoostingClassifier`, `fit`, `predict_proba` y más (sección «3. La referencia: boosting de árboles»).

```python
t0 = time.time()
boost = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_depth=4, random_state=SEMILLA)
boost.fit(A_ent, y_ent)
t_boost = time.time() - t0
prob_boost_val, prob_boost_pru = boost.predict_proba(A_val)[:, 1], boost.predict_proba(A_pru)[:, 1]
print(f"Boosting entrenado en {t_boost:.1f} s · AUC validación = {roc_auc_score(y_val, prob_boost_val):.3f}")
```

**Qué hace cada línea:**

- `t0 = time.time()` → Guarda en `t0` el resultado. `time`: devuelve la hora actual en segundos (sirve para medir cuánto tarda algo).
- `boost = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, ma…` → Guarda en `boost` el resultado. `HistGradientBoostingClassifier`: boosting de árboles rápido de scikit-learn.
- `boost.fit(A_ent, y_ent)` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `t_boost = time.time() - t0` → Guarda en `t_boost` el resultado. `time`: devuelve la hora actual en segundos (sirve para medir cuánto tarda algo).
- `prob_boost_val, prob_boost_pru = boost.predict_proba(A_val)[:, 1], boost.pr…` → Guarda en `prob_boost_val, prob_bo…` el resultado. `predict_proba`: pide la probabilidad de cada clase (no solo la clase).
- `print(f"Boosting entrenado en {t_boost:.1f} s · AUC validación = {roc_auc_s…` → `print`: muestra un valor por pantalla; `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar).

### Celda 5 · 4. El MLP, con las buenas prácticas del Sprint… · 🏫

**Qué hace:** Practica `Sequential`, `add`, `compile`, `set_random_seed` y más (sección «4. El MLP, con las buenas prácticas del…»).

```python
def construir_mlp(n_entradas, capas=(64, 32), l2=0.003, dropout=0.3, tasa=1e-3):
    m = keras.Sequential([keras.layers.Input(shape=(n_entradas,))])
    for u in capas:
        m.add(keras.layers.Dense(u, activation="relu", kernel_regularizer=keras.regularizers.l2(l2)))
        m.add(keras.layers.Dropout(dropout))
    m.add(keras.layers.Dense(1, activation="sigmoid"))
    m.compile(optimizer=keras.optimizers.Adam(tasa), loss="binary_crossentropy", metrics=[keras.metrics.AUC(name="auc")])
    return m

modelos_mlp, historiales, tiempos = [], [], []
for semilla in (1, 2, 3):
    keras.utils.set_random_seed(semilla)
    t0 = time.time()
    m = construir_mlp(A_ent.shape[1])
    h = m.fit(A_ent, y_ent, validation_data=(A_val, y_val), epochs=40, batch_size=64, verbose=0,
              callbacks=[keras.callbacks.EarlyStopping(monitor="val_loss", patience=6, restore_best_weights=True)])
    tiempos.append(time.time() - t0)
    modelos_mlp.append(m); historiales.append(h)
    print(f"semilla {semilla}: {len(h.history['loss'])} épocas, AUC validación = {max(h.history['val_auc']):.3f} (máx.)")
```

**Qué hace cada línea:**

- `def construir_mlp(n_entradas, capas=(64, 32), l2=0.003, dropout=0.3, tasa=1…` → Define la función `construir_mlp`: Función definida en el cuaderno.
- `modelos_mlp, historiales, tiempos = [], [], []` → Guarda el valor en `modelos_mlp, historiale…`.
- `for semilla in (1, 2, 3):` → Repite el bloque de debajo para cada valor de `semilla` en `(1, 2, 3)`. Dentro del bloque: `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados; `time`: devuelve la hora actual en segundos (sirve para medir cuánto tarda algo); `construir_mlp`: función definida en el cuaderno.

### Celda 6 · 4. El MLP, con las buenas prácticas del Sprint… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 5. Diagnóstico con curvas de aprendizaje · 🏫

**Qué hace:** Practica `subplots`, `zip`, `tight_layout`, `plot` y más (sección «5. Diagnóstico con curvas de aprendizaje»).

```python
fig, ejes = plt.subplots(1, 3, figsize=(14, 3.6), sharey=True)
for eje, h, s in zip(ejes, historiales, (1, 2, 3)):
    eje.plot(h.history["loss"], label="entrenamiento"); eje.plot(h.history["val_loss"], label="validación")
    eje.set_title(f"MLP · semilla {s}"); eje.set_xlabel("época"); eje.set_ylabel("pérdida (incluye L2)"); eje.legend()
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ejes = plt.subplots(1, 3, figsize=(14, 3.6), sharey=True)` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for eje, h, s in zip(ejes, historiales, (1, 2, 3)):` → Repite el bloque de debajo para cada valor de `eje, h, s` en `zip(ejes, historiales, (1, 2, 3))`. Dentro del bloque: `plot`: dibuja una línea (o puntos unidos); `history`: guarda la evolución de las métricas época a época; `set_title`: pone el título de un gráfico.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 8 · 5. Diagnóstico con curvas de aprendizaje · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 6. El veredicto en el conjunto de prueba · 🏫

**Qué hace:** Practica `mean`, `round`, `DataFrame`, `ravel` y más (sección «6. El veredicto en el conjunto de prueba»).

```python
prob_mlp_pru = np.mean([m.predict(A_pru, verbose=0).ravel() for m in modelos_mlp], axis=0)
tabla = pd.DataFrame({"Boosting de árboles": evaluar(y_pru, prob_boost_pru),
                      "MLP (media de 3 semillas)": evaluar(y_pru, prob_mlp_pru)}).T
tabla["entrenamiento (s)"] = [t_boost, np.mean(tiempos)]
tabla["parámetros / árboles"] = ["200 iteraciones × árboles de profundidad ≤ 4", f"{modelos_mlp[0].count_params():,} pesos"]
tabla.round(3)
```

**Qué hace cada línea:**

- `prob_mlp_pru = np.mean([m.predict(A_pru, verbose=0).ravel() for m in modelo…` → Guarda en `prob_mlp_pru` el resultado. `mean`: calcula la media; `ravel`: aplana un array a una sola dimensión; `predict`: pide al modelo ya entrenado que haga predicciones.
- `tabla = pd.DataFrame({"Boosting de árboles": evaluar(y_pru, prob_boost_pru),` → Guarda en `tabla` el resultado. `DataFrame`: crea una tabla de pandas (filas y columnas); `evaluar`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `tabla["entrenamiento (s)"] = [t_boost, np.mean(tiempos)]` → Guarda en `tabla["entrenamiento (s…` el resultado. `mean`: calcula la media.
- `tabla["parámetros / árboles"] = ["200 iteraciones × árboles de profundidad…` → Guarda en `tabla["parámetros / árb…` el resultado. `count_params`: cuenta cuántos pesos tiene el modelo.
- `tabla.round(3)` → `round`: redondea un número a los decimales indicados.

### Celda 10 · 6. El veredicto en el conjunto de prueba · 🏫

**Qué hace:** Practica `default_rng`, `percentile`, `hist`, `axvline` y más (sección «¿La diferencia es real o es ruido?»).

```python
rng = np.random.default_rng(SEMILLA)
difs = []
for _ in range(300):
    idx = rng.integers(0, len(y_pru), len(y_pru))
    if len(np.unique(y_pru[idx])) < 2:
        continue
    difs.append(roc_auc_score(y_pru[idx], prob_mlp_pru[idx]) - roc_auc_score(y_pru[idx], prob_boost_pru[idx]))
inf, sup = np.percentile(difs, [2.5, 97.5])
print(f"Diferencia de AUC (MLP − boosting): {np.mean(difs):+.3f} · intervalo 95 %: [{inf:+.3f}, {sup:+.3f}]")
plt.hist(difs, bins=25, color="steelblue"); plt.axvline(0, color="red", ls="--", label="sin diferencia")
plt.xlabel("AUC MLP − AUC boosting"); plt.ylabel("frecuencia"); plt.title("Incertidumbre de la comparación (bootstrap)")
plt.legend(); plt.show()
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `difs = []` → Guarda el valor en `difs`.
- `for _ in range(300):` → Repite el bloque de debajo para cada valor de `_` en `range(300)`. Dentro del bloque: `integers`: genera números enteros aleatorios; `unique`: devuelve los valores distintos; `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar).
- `inf, sup = np.percentile(difs, [2.5, 97.5])` → Guarda en `inf, sup` el resultado. `percentile`: calcula un percentil (el valor bajo el que queda ese % de los datos).
- `print(f"Diferencia de AUC (MLP − boosting): {np.mean(difs):+.3f} · interval…` → `print`: muestra un valor por pantalla; `mean`: calcula la media.
- `plt.hist(difs, bins=25, color="steelblue"); plt.axvline(0, color="red", ls=…` → `hist`: dibuja un histograma (cuántos datos caen en cada intervalo).
- `plt.hist(difs, bins=25, color="steelblue"); plt.axvline(0, color="red", ls=…` → `axvline`: dibuja una línea vertical de referencia.
- `plt.xlabel("AUC MLP − AUC boosting"); plt.ylabel("frecuencia"); plt.title("…` → `xlabel`: pone el nombre del eje horizontal.
- `plt.xlabel("AUC MLP − AUC boosting"); plt.ylabel("frecuencia"); plt.title("…` → `ylabel`: pone el nombre del eje vertical.
- … y 3 más con las mismas ideas.

### Celda 11 · 6. El veredicto en el conjunto de prueba · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 12 · 7. Variante de regresión (opcional, precio por… · 🏫

**Qué hace:** Practica `to_numpy`, `train_test_split`, `ColumnTransformer`, `astype` y más (sección «7. Variante de regresión (opcional, pre…»).

```python
num_r = [c for c in num if c != "precio_noche"]
Xr = df[num_r + cat]; yr = df["precio_noche"].to_numpy()
Xr_res, Xr_pru, yr_res, yr_pru = train_test_split(Xr, yr, test_size=0.2, random_state=SEMILLA)
pre_r = ColumnTransformer([("n", StandardScaler(), num_r), ("c", OneHotEncoder(handle_unknown="ignore"), cat)])
Ar_res = pre_r.fit_transform(Xr_res).astype("float32"); Ar_pru = pre_r.transform(Xr_pru).astype("float32")
mu, sd = yr_res.mean(), yr_res.std()

boost_r = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_depth=4, random_state=SEMILLA).fit(Ar_res, yr_res)
ridge_r = Ridge().fit(Ar_res, yr_res)
keras.utils.set_random_seed(SEMILLA)
mlp_r = keras.Sequential([keras.layers.Input(shape=(Ar_res.shape[1],)), keras.layers.Dense(32, activation="relu"),
                          keras.layers.Dense(16, activation="relu"), keras.layers.Dense(1)])
mlp_r.compile("adam", "mse")
mlp_r.fit(Ar_res, ((yr_res - mu) / sd).astype("float32"), validation_split=0.2, epochs=40, batch_size=64, verbose=0,
          callbacks=[keras.callbacks.EarlyStopping(patience=6, restore_best_weights=True)])
pd.DataFrame({"MAE (€)": {
    "Boosting": mean_absolute_error(yr_pru, boost_r.predict(Ar_pru)),
    "Ridge (lineal)": mean_absolute_error(yr_pru, ridge_r.predict(Ar_pru)),
    "MLP": mean_absolute_error(yr_pru, mlp_r.predict(Ar_pru, verbose=0).ravel() * sd + mu)}}).round(2)
```

**Qué hace cada línea:**

- `num_r = [c for c in num if c != "precio_noche"]` → Guarda el valor en `num_r`.
- `Xr = df[num_r + cat]; yr = df["precio_noche"].to_numpy()` → Guarda el valor en `Xr`.
- `Xr = df[num_r + cat]; yr = df["precio_noche"].to_numpy()` → Guarda en `yr` el resultado. `to_numpy`: convierte una tabla o columna de pandas en un array de NumPy.
- `Xr_res, Xr_pru, yr_res, yr_pru = train_test_split(Xr, yr, test_size=0.2, ra…` → Guarda en `Xr_res, Xr_pru, yr_res,…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `pre_r = ColumnTransformer([("n", StandardScaler(), num_r), ("c", OneHotEnco…` → Guarda en `pre_r` el resultado. `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas; `StandardScaler`: escala los números para que tengan media 0 y desviación 1; `OneHotEncoder`: convierte categorías en columnas de 0/1.
- `Ar_res = pre_r.fit_transform(Xr_res).astype("float32"); Ar_pru = pre_r.tran…` → Guarda en `Ar_res` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `Ar_res = pre_r.fit_transform(Xr_res).astype("float32"); Ar_pru = pre_r.tran…` → Guarda en `Ar_pru` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `transform`: calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado.
- `mu, sd = yr_res.mean(), yr_res.std()` → Guarda en `mu, sd` el resultado. `mean`: calcula la media; `std`: calcula la desviación típica (cuánto se separan los datos de la media).
- `boost_r = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, m…` → Guarda en `boost_r` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `HistGradientBoostingRegressor`: boosting de árboles rápido de scikit-learn para predecir números.
- … y 6 más con las mismas ideas.

---
*Generado a partir de `laboratorios/fuentes/S10_04_reto_vale_la_pena.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
