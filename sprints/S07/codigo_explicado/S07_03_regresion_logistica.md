# Código explicado · S07.03 · Regresión logística: predecir cancelaciones

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_03_regresion_logistica.ipynb) · [descargar](../notebooks/S07_03_regresion_logistica.ipynb) · ⏱ en clase: 45 min · 🏫 4 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_theme`, `read_csv`, `astype`, `train_test_split` y más. |
| 2 | 1. La idea: de una suma ponderada a una… | Practica `linspace`, `figure`, `plot`, `axhline` y más (sección «1. La idea: de una suma… |
| 4 | 3. Interpretar: coeficientes y *odds ra… | Practica `get_feature_names_out`, `Series`, `sort_values`, `figure` y más (sección «3. In… |
| 6 | 4. El umbral y la matriz de confusión | Practica `subplots`, `zip`, `tight_layout`, `astype` y más (sección «4. El umbral y la ma… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `df` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 1 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 1 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 1 |
| `z` | `np.linspace(-6, 6, 200)` | 2 |
| `nombres` | `logit[:-1].get_feature_names_out()` | 4 |
| `coefs` | `pd.Series(logit[-1].coef_[0], index=nombres)` | 4 |
| `odds` | `np.exp(coefs).sort_values(ascending=False)` | 4 |
| `cv` | `StratifiedKFold(5, shuffle=True, random_state=SEMILLA)` | 8 |
| `proba_cv` | `cross_val_predict(logit, X_train, y_train, cv=cv, method=…` | 8 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `metricas_umbral` | Matriz de confusión y métricas para un umbral dado. |
| `coste_total` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 1, 6 |
| `axhline` | Dibuja una línea horizontal de referencia. | 2 |
| `axvline` | Dibuja una línea vertical de referencia. | 4, 10 |
| `confusion_matrix` | Cuenta aciertos y fallos de cada tipo (matriz de confusión). | 6 |
| `cross_val_predict` | Predicciones de cada dato hechas por un modelo que no lo ha visto. | 8 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 1 |
| `exp` | Exponencial (e elevado a un número). | 2, 4 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 2, 4, 10 |
| `from_predictions` | Dibuja la matriz de confusión a partir de las etiquetas reales y las predichas. | 6 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 4 |
| `iloc` | Selecciona filas/columnas por su posición. | 4 |
| `isin` | Marca los valores que están en una lista. | 1 |
| `legend` | Muestra la leyenda del gráfico. | 10 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 1 |
| `linspace` | Crea una secuencia de N números equiespaciados entre dos límites. | 2 |
| `mean` | Calcula la media. | 1 |
| `plot` | Dibuja una línea (o puntos unidos). | 2, 4, 10 |
| `print` | Muestra un valor por pantalla. | 1 |
| `ravel` | Aplana un array a una sola dimensión. | 6 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 4 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_title` | Pone el título de un gráfico. | 6 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 6 |
| `set_ylabel` | Pone el nombre del eje vertical. | 6 |
| `show` | Muestra el gráfico. | 2, 4, 6, 10 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 4 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 8 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 6 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 4, 6 |
| `title` | Pone el título del gráfico. | 2, 4, 10 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 1 |
| `xlabel` | Pone el nombre del eje horizontal. | 2, 4, 10 |
| `ylabel` | Pone el nombre del eje vertical. | 2, 4, 10 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_theme`, `read_csv`, `astype`, `train_test_split` y más.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score

SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)

columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["cancelada"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
print(f"Tasa de cancelación: {y.mean():.1%} · train {len(X_train)} · test {len(X_test)}")
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split, cross_val_predict, St…` → Trae `train_test_split`, `cross_val_predict`, `StratifiedKFold` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.linear_model import LogisticRegression` → Trae `LogisticRegression` de `sklearn.linear_model` para poder usarlo.
- `from sklearn.impute import SimpleImputer` → Trae `SimpleImputer` de `sklearn.impute` para poder usarlo.
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder` → Trae `StandardScaler`, `OneHotEncoder` de `sklearn.preprocessing` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- … y 12 más con las mismas ideas.

### Celda 2 · 1. La idea: de una suma ponderada a una probabi… · 🏫

**Qué hace:** Practica `linspace`, `figure`, `plot`, `axhline` y más (sección «1. La idea: de una suma ponderada a una…»).

```python
z = np.linspace(-6, 6, 200)
plt.figure(figsize=(6, 3.5))
plt.plot(z, 1 / (1 + np.exp(-z)), color="#2a6f97", lw=2)
plt.axhline(0.5, color="gray", ls="--")
plt.title("Función sigmoide: convierte cualquier número en una probabilidad")
plt.xlabel("Suma ponderada z")
plt.ylabel("Probabilidad")
plt.show()
```

**Qué hace cada línea:**

- `z = np.linspace(-6, 6, 200)` → Guarda en `z` el resultado. `linspace`: crea una secuencia de N números equiespaciados entre dos límites.
- `plt.figure(figsize=(6, 3.5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.plot(z, 1 / (1 + np.exp(-z)), color="#2a6f97", lw=2)` → `plot`: dibuja una línea (o puntos unidos); `exp`: exponencial (e elevado a un número).
- `plt.axhline(0.5, color="gray", ls="--")` → `axhline`: dibuja una línea horizontal de referencia.
- `plt.title("Función sigmoide: convierte cualquier número en una probabilidad…` → `title`: pone el título del gráfico.
- `plt.xlabel("Suma ponderada z")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("Probabilidad")` → `ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 3 · 2. Entrenar el modelo · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3. Interpretar: coeficientes y *odds ratios* · 🏫

**Qué hace:** Practica `get_feature_names_out`, `Series`, `sort_values`, `figure` y más (sección «3. Interpretar: coeficientes y *odds ra…»).

```python
nombres = logit[:-1].get_feature_names_out()
coefs = pd.Series(logit[-1].coef_[0], index=nombres)
odds = np.exp(coefs).sort_values(ascending=False)
plt.figure(figsize=(7, 6))
odds.iloc[::-1].plot(kind="barh", color=["#e63946" if v > 1 else "#2a6f97" for v in odds.iloc[::-1]])
plt.axvline(1, color="black", lw=1)
plt.title("Odds ratio de cada variable (rojo = más riesgo de cancelar)")
plt.xlabel("Odds ratio")
plt.ylabel("")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `nombres = logit[:-1].get_feature_names_out()` → Guarda en `nombres` el resultado. `get_feature_names_out`: devuelve los nombres de las columnas después del preprocesado.
- `coefs = pd.Series(logit[-1].coef_[0], index=nombres)` → Guarda en `coefs` el resultado. `Series`: crea una columna de pandas (una sola serie de valores).
- `odds = np.exp(coefs).sort_values(ascending=False)` → Guarda en `odds` el resultado. `sort_values`: ordena la tabla por una o varias columnas; `exp`: exponencial (e elevado a un número).
- `plt.figure(figsize=(7, 6))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `odds.iloc[::-1].plot(kind="barh", color=["#e63946" if v > 1 else "#2a6f97"…` → `plot`: dibuja una línea (o puntos unidos); `iloc`: selecciona filas/columnas por su posición.
- `plt.axvline(1, color="black", lw=1)` → `axvline`: dibuja una línea vertical de referencia.
- `plt.title("Odds ratio de cada variable (rojo = más riesgo de cancelar)")` → `title`: pone el título del gráfico.
- `plt.xlabel("Odds ratio")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("")` → `ylabel`: pone el nombre del eje vertical.
- … y 2 más con las mismas ideas.

### Celda 5 · 3. Interpretar: coeficientes y *odds ratios* · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 4. El umbral y la matriz de confusión · 🏫

**Qué hace:** Practica `subplots`, `zip`, `tight_layout`, `astype` y más (sección «4. El umbral y la matriz de confusión»).

```python
def metricas_umbral(y_real, proba, umbral):
    """Matriz de confusión y métricas para un umbral dado."""
    pred = (proba >= umbral).astype(int)
    vn, fp, fn, vp = confusion_matrix(y_real, pred).ravel()
    return {"umbral": umbral, "VN": vn, "FP": fp, "FN": fn, "VP": vp,
            "precision": vp / (vp + fp) if (vp + fp) else np.nan,
            "recall": vp / (vp + fn)}

fig, ejes = plt.subplots(1, 2, figsize=(10, 4))
for ax, u in zip(ejes, [0.5, 0.3]):
    ConfusionMatrixDisplay.from_predictions(y_test, (proba_test >= u).astype(int), ax=ax,
                                            display_labels=["Se mantiene", "Cancela"], cmap="Blues", colorbar=False)
    ax.set_title(f"Umbral {u}")
    ax.set_xlabel("Predicho")
    ax.set_ylabel("Real")
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `def metricas_umbral(y_real, proba, umbral):` → Define la función `metricas_umbral`: Matriz de confusión y métricas para un umbral dado.
- `fig, ejes = plt.subplots(1, 2, figsize=(10, 4))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for ax, u in zip(ejes, [0.5, 0.3]):` → Repite el bloque de debajo para cada valor de `ax, u` en `zip(ejes, [0.5, 0.3])`. Dentro del bloque: `from_predictions`: dibuja la matriz de confusión a partir de las etiquetas reales y las predichas; `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `set_title`: pone el título de un gráfico.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 7 · 4. El umbral y la matriz de confusión · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 5. Elegir el umbral según el coste · 🏠

**Qué hace:** Practica `StratifiedKFold`, `cross_val_predict` (sección «5. Elegir el umbral según el coste»).

```python
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)
proba_cv = cross_val_predict(logit, X_train, y_train, cv=cv, method="predict_proba")[:, 1]

def coste_total(y_real, proba, umbral, coste_fn=3.0, coste_fp=1.0):
    m = metricas_umbral(y_real, proba, umbral)
    return m["FN"] * coste_fn + m["FP"] * coste_fp
```

**Qué hace cada línea:**

- `cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)` → Guarda en `cv` el resultado. `StratifiedKFold`: crea particiones de validación cruzada que mantienen la proporción de clases.
- `proba_cv = cross_val_predict(logit, X_train, y_train, cv=cv, method="predic…` → Guarda en `proba_cv` el resultado. `cross_val_predict`: predicciones de cada dato hechas por un modelo que no lo ha visto.
- `def coste_total(y_real, proba, umbral, coste_fn=3.0, coste_fp=1.0):` → Define la función `coste_total`: Función definida en el cuaderno.

### Celda 9 · 5. Elegir el umbral según el coste · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5. Elegir el umbral según el coste · 🏠

**Qué hace:** Practica `figure`, `plot`, `axvline`, `title` y más (sección «5. Elegir el umbral según el coste»).

```python
plt.figure(figsize=(7, 3.8))
plt.plot(umbrales, costes, marker="o", color="#2a6f97")
plt.axvline(mejor_umbral, color="#e63946", ls="--", label=f"Mínimo: {mejor_umbral:.2f}")
plt.title("Coste total según el umbral (FN cuesta 3 veces más que FP)")
plt.xlabel("Umbral de decisión")
plt.ylabel("Coste (unidades relativas)")
plt.legend()
plt.show()
```

**Qué hace cada línea:**

- `plt.figure(figsize=(7, 3.8))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.plot(umbrales, costes, marker="o", color="#2a6f97")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.axvline(mejor_umbral, color="#e63946", ls="--", label=f"Mínimo: {mejor_…` → `axvline`: dibuja una línea vertical de referencia.
- `plt.title("Coste total según el umbral (FN cuesta 3 veces más que FP)")` → `title`: pone el título del gráfico.
- `plt.xlabel("Umbral de decisión")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("Coste (unidades relativas)")` → `ylabel`: pone el nombre del eje vertical.
- `plt.legend()` → `legend`: muestra la leyenda del gráfico.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 11 · 6. Mini-reto: tabla para el gerente · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S07_03_regresion_logistica.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
