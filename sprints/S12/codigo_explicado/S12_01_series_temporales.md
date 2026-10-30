# Código explicado · S12.01 · Series temporales: baseline, descomposición y ARIMA/SARIMAX

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_01_series_temporales.ipynb) · [descargar](../notebooks/S12_01_series_temporales.ipynb) · ⏱ en clase: 45 min · 🏫 8 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `filterwarnings`, `seed`, `update`, `set_index` y más. |
| 2 | 1. Mirar la serie | Patrón semanal y anual, promediando. |
| 4 | 2. Partición temporal (¡sin barajar!) | Practica `date`, `iloc`, `min`, `max` (sección «2. Partición temporal (¡sin barajar!)»). |
| 5 | 3. Baselines: el rival que hay que batir | Practica `list`, `repeat`, `values`, `mean` y más (sección «3. Baselines: el rival que ha… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `ocup` | `pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["f…` | 1 |
| `por_dia` | `ocup["ocupacion_pct"].groupby(ocup.index.dayofweek).mean()` | 2 |
| `por_mes` | `ocup["ocupacion_pct"].groupby(ocup.index.month).mean()` | 2 |
| `DIAS_TEST` | `91` | 4 |
| `serie` | `ocup["ocupacion_pct"]` | 4 |
| `HORIZONTE` | `7` | 5 |
| `origenes` | `list(range(len(entrenamiento), len(serie), HORIZONTE))` | 5 |
| `desc` | `seasonal_decompose(entrenamiento, model="additive", perio…` | 7 |
| `X_todo` | `exogenas(serie.index)` | 9 |
| `X_ent` | `X_todo.iloc[:-DIAS_TEST]` | 9 |
| `modelo` | `SARIMAX(entrenamiento, exog=X_ent, order=(1, 0, 1), seaso…` | 9 |
| `res` | `modelo.fit(disp=False, maxiter=200)` | 9 |
| `comparativa` | `pd.Series({"Ingenuo": mae_ing, "Estacional (t-7)": mae_es…` | 12 |
| `n` | `len(p_sar)` | 12 |
| `ind` | `serie.index[origenes[0]:origenes[0] + n]` | 12 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `mae` | Función definida en el cuaderno. |
| `evaluar_semanal` | predictor(historia: Series, origen: int) -> array de 7 valores. Devuelve (MAE, predicciones concatenadas). |
| `pred_ingenuo` | Función definida en el cuaderno. |
| `pred_estacional` | Función definida en el cuaderno. |
| `pred_media4` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `exogenas` | Función definida en el cuaderno. |
| `pred_sarimax` | Función definida en el cuaderno. |
| `pred_sarimax_simple` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `abs` | Valor absoluto: quita el signo negativo. | 5 |
| `append` | Añade un elemento al final de una lista. | 5 |
| `apply` | Aplica una función a cada fila o a cada valor. | 10 |
| `asarray` | Convierte algo en array de NumPy sin copiarlo si ya lo es. | 5 |
| `bar` | Dibuja barras verticales. | 2 |
| `concatenate` | Une arrays uno detrás de otro. | 5 |
| `cos` | Coseno. | 9 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 9 |
| `date` | Crea una fecha (año, mes, día). | 4 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 9 |
| `float` | Convierte un valor en número decimal. | 5 |
| `forecast` | Predice los próximos pasos de la serie. | 10 |
| `groupby` | Agrupa las filas por una columna para calcular algo en cada grupo. | 2 |
| `head` | Muestra las primeras filas. | 1 |
| `iloc` | Selecciona filas/columnas por su posición. | 4, 5, 7, 9, 10 |
| `legend` | Muestra la leyenda del gráfico. | 12 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 4, 5, 12 |
| `list` | Crea una lista (o convierte algo en lista). | 5 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 9 |
| `max` | Devuelve el valor más grande. | 4 |
| `mean` | Calcula la media. | 2, 5 |
| `min` | Devuelve el valor más pequeño. | 4 |
| `plot` | Dibuja una línea (o puntos unidos). | 2, 7, 12 |
| `predictor` | La función de predicción que se pasa como argumento. | 5 |
| `print` | Muestra un valor por pantalla. | 1, 4, 5, 7, 9, 10… |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 5 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `repeat` | Repite cada elemento varias veces. | 5 |
| `round` | Redondea un número a los decimales indicados. | 7, 12 |
| `SARIMAX` | Modelo estadístico de series temporales con estacionalidad y variables externas. | 9 |
| `seasonal_decompose` | Separa una serie temporal en tendencia, estacionalidad y resto. | 7 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 12 |
| `set_index` | Convierte una columna en el índice (la etiqueta de cada fila). | 1 |
| `set_title` | Pone el título de un gráfico. | 2, 7, 12 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 2 |
| `set_ylabel` | Pone el nombre del eje vertical. | 2, 7, 12 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 1 |
| `show` | Muestra el gráfico. | 2, 7, 12 |
| `sin` | Seno. | 9 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 12 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 2, 7, 12 |
| `summary` | Muestra el resumen del modelo (en Keras, las capas y sus pesos; en statsmodels, coeficientes y p-valores). | 9 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 2, 7 |
| `to_string` | Convierte la tabla en texto para mostrarla entera. | 7, 12 |
| `update` | Añade o cambia varias claves de un diccionario. | 1 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 5, 9, 10, 12 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `filterwarnings`, `seed`, `update`, `set_index` y más.

```python
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")
SEMILLA = 42
np.random.seed(SEMILLA)
plt.rcParams.update({"figure.figsize": (10, 3.5), "axes.grid": True, "axes.spines.top": False, "axes.spines.right": False})

ocup = pd.read_csv(dato("ocupacion_diaria.csv"), parse_dates=["fecha"]).set_index("fecha")
ocup.index.freq = "D"
print(ocup.shape)
ocup.head()
```

**Qué hace cada línea:**

- `import warnings` → Trae `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from statsmodels.tsa.seasonal import seasonal_decompose` → Trae `seasonal_decompose` de `statsmodels.tsa.seasonal` para poder usarlo.
- `from statsmodels.tsa.statespace.sarimax import SARIMAX` → Trae `SARIMAX` de `statsmodels.tsa.statespace.sarimax` para poder usarlo.
- `warnings.filterwarnings("ignore")` → `filterwarnings`: silencia avisos que no aportan nada en el cuaderno.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `np.random.seed(SEMILLA)` → `seed`: fija la semilla del azar para que salga siempre lo mismo.
- … y 5 más con las mismas ideas.

### Celda 2 · 1. Mirar la serie · 🏫

**Qué hace:** Patrón semanal y anual, promediando.

```python
fig, ax = plt.subplots()
ocup["ocupacion_pct"].plot(ax=ax, lw=0.8)
ax.set_title("Ocupación diaria del alojamiento (2023-2025)")
ax.set_xlabel("Fecha"); ax.set_ylabel("Ocupación (%)")
plt.show()

# Patrón semanal y anual, promediando
por_dia = ocup["ocupacion_pct"].groupby(ocup.index.dayofweek).mean()
por_mes = ocup["ocupacion_pct"].groupby(ocup.index.month).mean()
fig, ejes = plt.subplots(1, 2, figsize=(11, 3.5))
por_dia.index = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
por_dia.plot.bar(ax=ejes[0], color="#3b7ea1"); ejes[0].set_title("Ocupación media por día de la semana")
por_mes.plot.bar(ax=ejes[1], color="#e08e45"); ejes[1].set_title("Ocupación media por mes")
ejes[0].set_ylabel("Ocupación (%)"); ejes[1].set_xlabel("Mes")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots()` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ocup["ocupacion_pct"].plot(ax=ax, lw=0.8)` → `plot`: dibuja una línea (o puntos unidos).
- `ax.set_title("Ocupación diaria del alojamiento (2023-2025)")` → `set_title`: pone el título de un gráfico.
- `ax.set_xlabel("Fecha"); ax.set_ylabel("Ocupación (%)")` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_xlabel("Fecha"); ax.set_ylabel("Ocupación (%)")` → `set_ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.
- `por_dia = ocup["ocupacion_pct"].groupby(ocup.index.dayofweek).mean()` → Guarda en `por_dia` el resultado. `mean`: calcula la media; `groupby`: agrupa las filas por una columna para calcular algo en cada grupo.
- `por_mes = ocup["ocupacion_pct"].groupby(ocup.index.month).mean()` → Guarda en `por_mes` el resultado. `mean`: calcula la media; `groupby`: agrupa las filas por una columna para calcular algo en cada grupo.
- `fig, ejes = plt.subplots(1, 2, figsize=(11, 3.5))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- … y 9 más con las mismas ideas.

### Celda 3 · 1. Mirar la serie · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Partición temporal (¡sin barajar!) · 🏫

**Qué hace:** Practica `date`, `iloc`, `min`, `max` (sección «2. Partición temporal (¡sin barajar!)»).

```python
DIAS_TEST = 91
serie = ocup["ocupacion_pct"]
entrenamiento, prueba = serie.iloc[:-DIAS_TEST], serie.iloc[-DIAS_TEST:]
print("Entrenamiento:", entrenamiento.index.min().date(), "→", entrenamiento.index.max().date(), len(entrenamiento))
print("Prueba       :", prueba.index.min().date(), "→", prueba.index.max().date(), len(prueba))
```

**Qué hace cada línea:**

- `DIAS_TEST = 91` → Guarda el valor en `DIAS_TEST`.
- `serie = ocup["ocupacion_pct"]` → Guarda el valor en `serie`.
- `entrenamiento, prueba = serie.iloc[:-DIAS_TEST], serie.iloc[-DIAS_TEST:]` → Guarda en `entrenamiento, prueba` el resultado. `iloc`: selecciona filas/columnas por su posición.
- `print("Entrenamiento:", entrenamiento.index.min().date(), "→", entrenamient…` → `print`: muestra un valor por pantalla; `date`: crea una fecha (año, mes, día); `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `print("Prueba :", prueba.index.min().date(), "→", prueba.index.max().date()…` → `print`: muestra un valor por pantalla; `date`: crea una fecha (año, mes, día); `len`: cuenta cuántos elementos tiene una lista, texto o tabla.

### Celda 5 · 3. Baselines: el rival que hay que batir · 🏫

**Qué hace:** Practica `list`, `repeat`, `values`, `mean` y más (sección «3. Baselines: el rival que hay que batir»).

```python
HORIZONTE = 7
origenes = list(range(len(entrenamiento), len(serie), HORIZONTE))   # posiciones donde empieza cada semana de test
origenes = [o for o in origenes if o + HORIZONTE <= len(serie)]

def mae(real, pred):
    return float(np.mean(np.abs(np.asarray(real) - np.asarray(pred))))

def evaluar_semanal(predictor):
    """predictor(historia: Series, origen: int) -> array de 7 valores. Devuelve (MAE, predicciones concatenadas)."""
    preds, reales = [], []
    for o in origenes:
        preds.append(np.asarray(predictor(serie.iloc[:o], o)))
        reales.append(serie.iloc[o:o + HORIZONTE].values)
    preds, reales = np.concatenate(preds), np.concatenate(reales)
    return mae(reales, preds), preds

def pred_ingenuo(historia, o):
    return np.repeat(historia.iloc[-1], HORIZONTE)

def pred_estacional(historia, o):
    return historia.iloc[-7:].values

mae_ing, p_ing = evaluar_semanal(pred_ingenuo)
mae_est, p_est = evaluar_semanal(pred_estacional)
print(f"MAE ingenuo    : {mae_ing:.2f} puntos")
print(f"MAE estacional : {mae_est:.2f} puntos")
```

**Qué hace cada línea:**

- `HORIZONTE = 7` → Guarda el valor en `HORIZONTE`.
- `origenes = list(range(len(entrenamiento), len(serie), HORIZONTE)) # posicio…` → Guarda en `origenes` el resultado. `list`: crea una lista (o convierte algo en lista); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `origenes = [o for o in origenes if o + HORIZONTE <= len(serie)]` → Guarda en `origenes` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `def mae(real, pred):` → Define la función `mae`: Función definida en el cuaderno.
- `def evaluar_semanal(predictor):` → Define la función `evaluar_semanal`: predictor(historia: Series, origen: int) -> array de 7 valores. Devuelve (MAE, predicciones concatenadas).
- `def pred_ingenuo(historia, o):` → Define la función `pred_ingenuo`: Función definida en el cuaderno.
- `def pred_estacional(historia, o):` → Define la función `pred_estacional`: Función definida en el cuaderno.
- `mae_ing, p_ing = evaluar_semanal(pred_ingenuo)` → Guarda en `mae_ing, p_ing` el resultado. `evaluar_semanal`: predictor(historia: Series, origen: int) -> array de 7 valores. Devuelve (MAE, predicciones concatenadas).
- `mae_est, p_est = evaluar_semanal(pred_estacional)` → Guarda en `mae_est, p_est` el resultado. `evaluar_semanal`: predictor(historia: Series, origen: int) -> array de 7 valores. Devuelve (MAE, predicciones concatenadas).
- … y 2 más con las mismas ideas.

### Celda 6 · 3. Baselines: el rival que hay que batir · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4. Descomposición: tendencia + estacionalidad +… · 🏫

**Qué hace:** Practica `seasonal_decompose`, `subplots`, `zip`, `set_title` y más (sección «4. Descomposición: tendencia + estacion…»).

```python
desc = seasonal_decompose(entrenamiento, model="additive", period=7)
fig, ejes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
for ax, (nombre, s) in zip(ejes, [("Observada", desc.observed), ("Tendencia", desc.trend),
                                   ("Estacionalidad semanal", desc.seasonal), ("Resto", desc.resid)]):
    ax.plot(s, lw=0.8); ax.set_ylabel(nombre)
ejes[0].set_title("Descomposición aditiva (periodo = 7 días)")
plt.tight_layout(); plt.show()
print("Efecto semanal estimado (puntos sobre/bajo la media):")
print(desc.seasonal.iloc[:7].round(1).to_string())
```

**Qué hace cada línea:**

- `desc = seasonal_decompose(entrenamiento, model="additive", period=7)` → Guarda en `desc` el resultado. `seasonal_decompose`: separa una serie temporal en tendencia, estacionalidad y resto.
- `fig, ejes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for ax, (nombre, s) in zip(ejes, [("Observada", desc.observed), ("Tendencia…` → Repite el bloque de debajo para cada valor de `ax, (nombre, s)` en `zip(ejes, [("Observada", desc.observed)…`. Dentro del bloque: `plot`: dibuja una línea (o puntos unidos); `set_ylabel`: pone el nombre del eje vertical.
- `ejes[0].set_title("Descomposición aditiva (periodo = 7 días)")` → `set_title`: pone el título de un gráfico.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.
- `print("Efecto semanal estimado (puntos sobre/bajo la media):")` → `print`: muestra un valor por pantalla.
- `print(desc.seasonal.iloc[:7].round(1).to_string())` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `round`: redondea un número a los decimales indicados.

### Celda 8 · 4. Descomposición: tendencia + estacionalidad +… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5. ARIMA y SARIMAX · 🏫

**Qué hace:** Practica `SARIMAX`, `fit`, `values`, `DataFrame` y más (sección «5. ARIMA y SARIMAX»).

```python
def exogenas(indice):
    dia_anio = indice.dayofyear.values
    X = pd.DataFrame(index=indice)
    for k in (1, 2):
        X[f"sin{k}"] = np.sin(2 * np.pi * k * dia_anio / 365.25)
        X[f"cos{k}"] = np.cos(2 * np.pi * k * dia_anio / 365.25)
    X["festivo"] = ocup.loc[indice, "festivo"].values
    return X

X_todo = exogenas(serie.index)
X_ent = X_todo.iloc[:-DIAS_TEST]

modelo = SARIMAX(entrenamiento, exog=X_ent, order=(1, 0, 1), seasonal_order=(1, 1, 1, 7),
                 enforce_stationarity=False, enforce_invertibility=False)
res = modelo.fit(disp=False, maxiter=200)
print(res.summary().tables[1])
```

**Qué hace cada línea:**

- `def exogenas(indice):` → Define la función `exogenas`: Función definida en el cuaderno.
- `X_todo = exogenas(serie.index)` → Guarda en `X_todo` el resultado. `exogenas`: función definida en el cuaderno.
- `X_ent = X_todo.iloc[:-DIAS_TEST]` → Guarda en `X_ent` el resultado. `iloc`: selecciona filas/columnas por su posición.
- `modelo = SARIMAX(entrenamiento, exog=X_ent, order=(1, 0, 1), seasonal_order…` → Guarda en `modelo` el resultado. `SARIMAX`: modelo estadístico de series temporales con estacionalidad y variables externas.
- `res = modelo.fit(disp=False, maxiter=200)` → Guarda en `res` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `print(res.summary().tables[1])` → `print`: muestra un valor por pantalla; `summary`: muestra el resumen del modelo (en Keras, las capas y sus pesos; en statsmodels, coeficientes y p-valores).

### Celda 10 · 5. ARIMA y SARIMAX · 🏫

**Qué hace:** Practica `apply`, `values`, `forecast`, `iloc` (sección «5. ARIMA y SARIMAX»).

```python
def pred_sarimax(historia, o):
    r = res.apply(historia, exog=X_todo.iloc[:o], refit=False)
    return r.forecast(HORIZONTE, exog=X_todo.iloc[o:o + HORIZONTE]).values

mae_sar, p_sar = evaluar_semanal(pred_sarimax)
print(f"MAE SARIMAX: {mae_sar:.2f}   (estacional ingenuo: {mae_est:.2f}, media 4 sem.: {mae_media4:.2f})")
```

**Qué hace cada línea:**

- `def pred_sarimax(historia, o):` → Define la función `pred_sarimax`: Función definida en el cuaderno.
- `mae_sar, p_sar = evaluar_semanal(pred_sarimax)` → Guarda en `mae_sar, p_sar` el resultado. `evaluar_semanal`: predictor(historia: Series, origen: int) -> array de 7 valores. Devuelve (MAE, predicciones concatenadas).
- `print(f"MAE SARIMAX: {mae_sar:.2f} (estacional ingenuo: {mae_est:.2f}, medi…` → `print`: muestra un valor por pantalla.

### Celda 11 · 5. ARIMA y SARIMAX · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 12 · 6. Comparar y mirar los errores · 🏫

**Qué hace:** Practica `sort_values`, `subplots`, `plot`, `set_title` y más (sección «6. Comparar y mirar los errores»).

```python
comparativa = pd.Series({"Ingenuo": mae_ing, "Estacional (t-7)": mae_est, "Media 4 semanas": mae_media4,
                         "SARIMAX sin exógenas": mae_sin_exog, "SARIMAX + festivos + Fourier": mae_sar}).sort_values()
print(comparativa.round(2).to_string())

fig, ax = plt.subplots()
ax.plot(prueba.index, prueba.values, label="Real", color="black", lw=1.2)
n = len(p_sar); ind = serie.index[origenes[0]:origenes[0] + n]
ax.plot(ind, p_est, label="Estacional t-7", alpha=.8)
ax.plot(ind, p_sar, label="SARIMAX", alpha=.9)
ax.set_title("Previsión a 7 días en las últimas 13 semanas"); ax.set_ylabel("Ocupación (%)"); ax.legend()
plt.show()
```

**Qué hace cada línea:**

- `comparativa = pd.Series({"Ingenuo": mae_ing, "Estacional (t-7)": mae_est, "…` → Guarda en `comparativa` el resultado. `sort_values`: ordena la tabla por una o varias columnas; `Series`: crea una columna de pandas (una sola serie de valores).
- `print(comparativa.round(2).to_string())` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `round`: redondea un número a los decimales indicados.
- `fig, ax = plt.subplots()` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax.plot(prueba.index, prueba.values, label="Real", color="black", lw=1.2)` → `plot`: dibuja una línea (o puntos unidos); `values`: devuelve los valores de un diccionario o de una tabla.
- `n = len(p_sar); ind = serie.index[origenes[0]:origenes[0] + n]` → Guarda en `n` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `n = len(p_sar); ind = serie.index[origenes[0]:origenes[0] + n]` → Guarda el valor en `ind`.
- `ax.plot(ind, p_est, label="Estacional t-7", alpha=.8)` → `plot`: dibuja una línea (o puntos unidos).
- `ax.plot(ind, p_sar, label="SARIMAX", alpha=.9)` → `plot`: dibuja una línea (o puntos unidos).
- `ax.set_title("Previsión a 7 días en las últimas 13 semanas"); ax.set_ylabel…` → `set_title`: pone el título de un gráfico.
- … y 3 más con las mismas ideas.

### Celda 13 · 7. Mini-reto integrador · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S12_01_series_temporales.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
