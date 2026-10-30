# Código explicado · S13.01 · Contar lo que hace el modelo: visualización de resultados

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_01_visualizacion_resultados.ipynb) · [descargar](../S13_01_visualizacion_resultados.ipynb) · ⏱ en clase: 35 min · 🏫 6 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`, `set_theme`. |
| 2 | 0. Punto de partida: dos modelos sencil… | Practica `read_csv`, `drop`, `train_test_split`, `tolist` y más (sección «0. Punto de par… |
| 4 | 1. Matriz de confusión: ¿en qué acierta… | Practica `subplots`, `plot`, `set_title`, `set_xlabel` y más (sección «Ejercicio 1»). |
| 6 | 2. Curvas ROC y precisión-exhaustividad… | Practica `subplots`, `plot`, `set_xlabel`, `set_ylabel` y más (sección «Ejercicio 2»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `reservas` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 2 |
| `X` | `reservas.drop(columns=["id_reserva", "fecha_reserva", "fe…` | 2 |
| `y` | `reservas["cancelada"]` | 2 |
| `categoricas` | `X.select_dtypes("object").columns.tolist()` | 2 |
| `numericas` | `[c for c in X.columns if c not in categoricas]` | 2 |
| `prep` | `ColumnTransformer([("num", StandardScaler(), numericas),…` | 2 |
| `modelo_lr` | `Pipeline([("prep", prep), ("m", LogisticRegression(max_it…` | 2 |
| `modelo_rf` | `Pipeline([("prep", prep), ("m", RandomForestClassifier(30…` | 2 |
| `prob_lr` | `modelo_lr.predict_proba(X_test)[:, 1]` | 2 |
| `prob_rf` | `modelo_rf.predict_proba(X_test)[:, 1]` | 2 |
| `tasa_tarifa` | `reservas.groupby("tarifa")["cancelada"].mean().mul(100)` | 11 |
| `barras` | `ax[1].bar(["Flexible", "No reembolsable"], tasa_tarifa[["…` | 11 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `coste_total` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `annotate` | Escribe una nota con flecha en el gráfico. | 10 |
| `average_precision_score` | Resumen de la curva precisión–sensibilidad en un solo número. | 6 |
| `axhline` | Dibuja una línea horizontal de referencia. | 6 |
| `bar` | Dibuja barras verticales. | 11 |
| `bar_label` | Escribe el valor encima de cada barra. | 11 |
| `barh` | Dibuja barras horizontales. | 8 |
| `columns` | Nombres de las columnas. | 2 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 2 |
| `ConfusionMatrixDisplay` | Dibuja una matriz de confusión. | 4 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `despine` | Quita los bordes superior y derecho del gráfico. | 11 |
| `dict` | Crea un diccionario (parejas nombre: valor). | 10 |
| `drop` | Quita columnas o filas. | 2 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 2 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 2 |
| `groupby` | Agrupa las filas por una columna para calcular algo en cada grupo. | 11 |
| `head` | Muestra las primeras filas. | 8 |
| `legend` | Muestra la leyenda del gráfico. | 6 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 2 |
| `max` | Devuelve el valor más grande. | 10 |
| `mean` | Calcula la media. | 2, 6, 11 |
| `min` | Devuelve el valor más pequeño. | 10 |
| `mul` | Multiplica cada valor por un número (aquí, para pasar de proporción a porcentaje). | 11 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 2 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 2 |
| `plot` | Dibuja una línea (o puntos unidos). | 4, 6, 10 |
| `precision_recall_curve` | Calcula los puntos de la curva precisión–sensibilidad. | 6 |
| `predict_proba` | Pide la probabilidad de cada clase (no solo la clase). | 2 |
| `print` | Muestra un valor por pantalla. | 2 |
| `RandomForestClassifier` | Bosque de muchos árboles que votan. | 2 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `roc_auc_score` | Calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar). | 6 |
| `roc_curve` | Calcula los puntos de la curva ROC. | 6 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `select_dtypes` | Selecciona las columnas de un tipo (numéricas, de texto…). | 2 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_title` | Pone el título de un gráfico. | 4, 6, 8, 10, 11 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 4, 6, 8, 10, 11 |
| `set_ylabel` | Pone el nombre del eje vertical. | 4, 6, 10, 11 |
| `set_ylim` | Fija el rango del eje vertical. | 6, 11 |
| `show` | Muestra el gráfico. | 4, 6, 8, 10, 11 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 2 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 4, 6, 8, 10, 11 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 4, 6, 8, 10, 11 |
| `tolist` | Convierte un array o una columna en una lista de Python. | 2 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 2 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 11 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `seed`, `set_theme`.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay, roc_curve, roc_auc_score,
                             precision_recall_curve, average_precision_score, recall_score)
from sklearn.inspection import permutation_importance

SEMILLA = 42
np.random.seed(SEMILLA)
sns.set_theme(style="whitegrid", font_scale=1.0)
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- `from sklearn.pipeline import Pipeline` → Trae `Pipeline` de `sklearn.pipeline` para poder usarlo.
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder` → Trae `StandardScaler`, `OneHotEncoder` de `sklearn.preprocessing` para poder usarlo.
- `from sklearn.linear_model import LogisticRegression` → Trae `LogisticRegression` de `sklearn.linear_model` para poder usarlo.
- … y 6 más con las mismas ideas.

### Celda 2 · 0. Punto de partida: dos modelos sencillos · 🏫

**Qué hace:** Practica `read_csv`, `drop`, `train_test_split`, `tolist` y más (sección «0. Punto de partida: dos modelos sencil…»).

```python
reservas = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
reservas["mes_llegada"] = reservas["fecha_llegada"].dt.month
X = reservas.drop(columns=["id_reserva", "fecha_reserva", "fecha_llegada", "cancelada"])
y = reservas["cancelada"]
X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=SEMILLA)

categoricas = X.select_dtypes("object").columns.tolist()
numericas = [c for c in X.columns if c not in categoricas]
prep = ColumnTransformer([("num", StandardScaler(), numericas),
                          ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas)])

modelo_lr = Pipeline([("prep", prep), ("m", LogisticRegression(max_iter=2000))]).fit(X_ent, y_ent)
modelo_rf = Pipeline([("prep", prep), ("m", RandomForestClassifier(300, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2))]).fit(X_ent, y_ent)

prob_lr = modelo_lr.predict_proba(X_test)[:, 1]     # probabilidad de cancelar
prob_rf = modelo_rf.predict_proba(X_test)[:, 1]
print(f"Reservas de prueba: {len(y_test)} · tasa real de cancelación: {y_test.mean():.1%}")
```

**Qué hace cada línea:**

- `reservas = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_…` → Guarda en `reservas` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `reservas["mes_llegada"] = reservas["fecha_llegada"].dt.month` → Guarda en `reservas["mes_llegada"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `X = reservas.drop(columns=["id_reserva", "fecha_reserva", "fecha_llegada",…` → Guarda en `X` el resultado. `drop`: quita columnas o filas.
- `y = reservas["cancelada"]` → Guarda el valor en `y`.
- `X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.25, strat…` → Guarda en `X_ent, X_test, y_ent, y…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `categoricas = X.select_dtypes("object").columns.tolist()` → Guarda en `categoricas` el resultado. `tolist`: convierte un array o una columna en una lista de Python; `columns`: nombres de las columnas; `select_dtypes`: selecciona las columnas de un tipo (numéricas, de texto…).
- `numericas = [c for c in X.columns if c not in categoricas]` → Guarda en `numericas` el resultado. `columns`: nombres de las columnas.
- `prep = ColumnTransformer([("num", StandardScaler(), numericas),` → Guarda en `prep` el resultado. `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas; `StandardScaler`: escala los números para que tengan media 0 y desviación 1; `OneHotEncoder`: convierte categorías en columnas de 0/1.
- `modelo_lr = Pipeline([("prep", prep), ("m", LogisticRegression(max_iter=200…` → Guarda en `modelo_lr` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `Pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- … y 4 más con las mismas ideas.

### Celda 3 · 1. Matriz de confusión: ¿en qué acierta y en qu… · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1. Matriz de confusión: ¿en qué acierta y en qu… · 🏫

**Qué hace:** Practica `subplots`, `plot`, `set_title`, `set_xlabel` y más (sección «Ejercicio 1»).

```python
fig, ax = plt.subplots(figsize=(4.5, 4))
ConfusionMatrixDisplay(cm, display_labels=["No cancela", "Cancela"]).plot(ax=ax, cmap="Blues", values_format=".0%", colorbar=False)
ax.set_title("Matriz de confusión (% de cada clase real)")
ax.set_xlabel("Lo que dijo el modelo"); ax.set_ylabel("Lo que ocurrió")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(figsize=(4.5, 4))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ConfusionMatrixDisplay(cm, display_labels=["No cancela", "Cancela"]).plot(a…` → `plot`: dibuja una línea (o puntos unidos); `ConfusionMatrixDisplay`: dibuja una matriz de confusión.
- `ax.set_title("Matriz de confusión (% de cada clase real)")` → `set_title`: pone el título de un gráfico.
- `ax.set_xlabel("Lo que dijo el modelo"); ax.set_ylabel("Lo que ocurrió")` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_xlabel("Lo que dijo el modelo"); ax.set_ylabel("Lo que ocurrió")` → `set_ylabel`: pone el nombre del eje vertical.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 5 · 2. Curvas ROC y precisión-exhaustividad (PR) · 🏫 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 2. Curvas ROC y precisión-exhaustividad (PR) · 🏫

**Qué hace:** Practica `subplots`, `plot`, `set_xlabel`, `set_ylabel` y más (sección «Ejercicio 2»).

```python
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
for nombre, prob, color in (("Regresión logística", prob_lr, "tab:blue"), ("Bosque aleatorio", prob_rf, "tab:orange")):
    fpr, tpr, _ = roc_curve(y_test, prob)
    ax[0].plot(fpr, tpr, color=color, label=f"{nombre} (AUC = {roc_auc_score(y_test, prob):.2f})")
    prec, rec, _ = precision_recall_curve(y_test, prob)
    ax[1].plot(rec, prec, color=color, label=f"{nombre} (AP = {average_precision_score(y_test, prob):.2f})")
ax[0].plot([0, 1], [0, 1], "--", color="gray", label="Azar")
ax[0].set_xlabel("Falsas alarmas (% de no cancelaciones avisadas)"); ax[0].set_ylabel("Cancelaciones detectadas")
ax[0].set_title("Curva ROC"); ax[0].legend(loc="lower right")
ax[1].axhline(y_test.mean(), linestyle="--", color="gray", label="Azar (tasa de cancelación)")
ax[1].set_xlabel("Exhaustividad (cancelaciones detectadas)"); ax[1].set_ylabel("Precisión (avisos que eran ciertos)")
ax[1].set_title("Curva precisión-exhaustividad"); ax[1].legend(loc="upper right"); ax[1].set_ylim(0, 1)
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for nombre, prob, color in (("Regresión logística", prob_lr, "tab:blue"), (…` → Repite el bloque de debajo para cada valor de `nombre, prob, color` en `(("Regresión logística", prob_lr, "tab:…`. Dentro del bloque: `roc_curve`: calcula los puntos de la curva ROC; `plot`: dibuja una línea (o puntos unidos); `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar).
- `ax[0].plot([0, 1], [0, 1], "--", color="gray", label="Azar")` → `plot`: dibuja una línea (o puntos unidos).
- `ax[0].set_xlabel("Falsas alarmas (% de no cancelaciones avisadas)"); ax[0].…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax[0].set_xlabel("Falsas alarmas (% de no cancelaciones avisadas)"); ax[0].…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax[0].set_title("Curva ROC"); ax[0].legend(loc="lower right")` → `set_title`: pone el título de un gráfico.
- `ax[0].set_title("Curva ROC"); ax[0].legend(loc="lower right")` → `legend`: muestra la leyenda del gráfico.
- `ax[1].axhline(y_test.mean(), linestyle="--", color="gray", label="Azar (tas…` → `axhline`: dibuja una línea horizontal de referencia; `mean`: calcula la media.
- `ax[1].set_xlabel("Exhaustividad (cancelaciones detectadas)"); ax[1].set_yla…` → `set_xlabel`: pone el nombre del eje horizontal.
- … y 6 más con las mismas ideas.

### Celda 7 · 3. ¿Qué variables importan? Importancia por per… · 🏫 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 3. ¿Qué variables importan? Importancia por per… · 🏫

**Qué hace:** Practica `subplots`, `barh`, `set_xlabel`, `set_title` y más (sección «Ejercicio 3»).

```python
fig, ax = plt.subplots(figsize=(7, 4))
importancias.head(8)[::-1].plot.barh(ax=ax, color="tab:blue")
ax.set_xlabel("Caída del AUC al desordenar la variable")
ax.set_title("La antelación de la reserva es lo que más pesa en una cancelación")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(figsize=(7, 4))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `importancias.head(8)[::-1].plot.barh(ax=ax, color="tab:blue")` → `barh`: dibuja barras horizontales; `head`: muestra las primeras filas.
- `ax.set_xlabel("Caída del AUC al desordenar la variable")` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_title("La antelación de la reserva es lo que más pesa en una cancela…` → `set_title`: pone el título de un gráfico.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 9 · 4. Elegir el umbral con el coste del negocio · 🏫 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 4. Elegir el umbral con el coste del negocio · 🏫

**Qué hace:** Practica `subplots`, `plot`, `annotate`, `set_xlabel` y más (sección «Ejercicio 4»).

```python
fig, ax = plt.subplots(figsize=(7, 3.8))
ax.plot(umbrales, costes, color="tab:blue")
ax.plot(umbral_optimo, coste_minimo, "o", color="tab:red")
ax.annotate(f"Umbral óptimo {umbral_optimo:.2f}\n{coste_minimo:,.0f} €", (umbral_optimo, coste_minimo),
            xytext=(umbral_optimo + 0.12, coste_minimo + 0.08 * (max(costes) - min(costes))),
            arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("Umbral (avisamos si la probabilidad supera este valor)"); ax.set_ylabel("Coste total en la muestra de prueba (€)")
ax.set_title("Un umbral algo más bajo que 0,5 es el que menos cuesta")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(figsize=(7, 3.8))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax.plot(umbrales, costes, color="tab:blue")` → `plot`: dibuja una línea (o puntos unidos).
- `ax.plot(umbral_optimo, coste_minimo, "o", color="tab:red")` → `plot`: dibuja una línea (o puntos unidos).
- `ax.annotate(f"Umbral óptimo {umbral_optimo:.2f}\n{coste_minimo:,.0f} €", (u…` → `annotate`: escribe una nota con flecha en el gráfico; `dict`: crea un diccionario (parejas nombre: valor); `max`: devuelve el valor más grande.
- `ax.set_xlabel("Umbral (avisamos si la probabilidad supera este valor)"); ax…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_xlabel("Umbral (avisamos si la probabilidad supera este valor)"); ax…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_title("Un umbral algo más bajo que 0,5 es el que menos cuesta")` → `set_title`: pone el título de un gráfico.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 11 · 5. Buenas prácticas: de gráfico técnico a gráfi… · 🏠

**Qué hace:** MAL: eje recortado, título descriptivo, sin etiquetas.

```python
tasa_tarifa = reservas.groupby("tarifa")["cancelada"].mean().mul(100)
fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
# MAL: eje recortado, título descriptivo, sin etiquetas
ax[0].bar(tasa_tarifa.index, tasa_tarifa.values, color=["red", "green"])
ax[0].set_ylim(35, 53); ax[0].set_title("cancelada por tarifa")
ax[0].set_xlabel("")
# BIEN: eje desde 0, mensaje en el título, valores etiquetados, un color de énfasis
barras = ax[1].bar(["Flexible", "No reembolsable"], tasa_tarifa[["flexible", "no_reembolsable"]].values, color=["tab:red", "lightgray"])
ax[1].bar_label(barras, fmt="%.0f %%", padding=3)
ax[1].set_ylim(0, 65); ax[1].set_ylabel("Reservas canceladas (%)")
ax[1].set_title("La tarifa flexible se cancela 15 puntos más")
sns.despine(); plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `tasa_tarifa = reservas.groupby("tarifa")["cancelada"].mean().mul(100)` → Guarda en `tasa_tarifa` el resultado. `mul`: multiplica cada valor por un número (aquí, para pasar de proporción a porcentaje); `mean`: calcula la media; `groupby`: agrupa las filas por una columna para calcular algo en cada grupo.
- `fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax[0].bar(tasa_tarifa.index, tasa_tarifa.values, color=["red", "green"])` → `bar`: dibuja barras verticales; `values`: devuelve los valores de un diccionario o de una tabla.
- `ax[0].set_ylim(35, 53); ax[0].set_title("cancelada por tarifa")` → `set_ylim`: fija el rango del eje vertical.
- `ax[0].set_ylim(35, 53); ax[0].set_title("cancelada por tarifa")` → `set_title`: pone el título de un gráfico.
- `ax[0].set_xlabel("")` → `set_xlabel`: pone el nombre del eje horizontal.
- `barras = ax[1].bar(["Flexible", "No reembolsable"], tasa_tarifa[["flexible"…` → Guarda en `barras` el resultado. `bar`: dibuja barras verticales; `values`: devuelve los valores de un diccionario o de una tabla.
- `ax[1].bar_label(barras, fmt="%.0f %%", padding=3)` → `bar_label`: escribe el valor encima de cada barra.
- `ax[1].set_ylim(0, 65); ax[1].set_ylabel("Reservas canceladas (%)")` → `set_ylim`: fija el rango del eje vertical.
- … y 5 más con las mismas ideas.

### Celda 12 · 5. Buenas prácticas: de gráfico técnico a gráfi… · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S13_01_visualizacion_resultados.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
