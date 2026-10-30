# Código explicado · S13.02 · Plantilla: informe visual de una página para dirección

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) · [descargar](../S13_02_plantilla_informe_visual.ipynb) · 🏫 5 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`, `set_theme`. |
| 2 | Parámetros del informe (edítalos) | >>> EDITA: tu mensaje y tus costes. |
| 3 | 1. Datos y modelo | Practica `read_csv`, `drop`, `train_test_split`, `tolist` y más (sección «1. Datos y mode… |
| 4 | 2. Cálculos que alimentan el panel | Practica `astype`, `confusion_matrix`, `roc_curve`, `roc_auc_score` y más (sección «2. Cá… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `TITULAR` | `"Recomendamos pedir depósito y avisar a las reservas de r…` | 2 |
| `CLIENTE` | `"TurisData Canarias · Dirección de Ingresos"` | 2 |
| `AUTORES` | `"Equipo X (nombres)"` | 2 |
| `COSTE_FN` | `50` | 2 |
| `COSTE_FP` | `30` | 2 |
| `UMBRAL` | `0.35` | 2 |
| `reservas` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 3 |
| `X` | `reservas.drop(columns=["id_reserva", "fecha_reserva", "fe…` | 3 |
| `y` | `reservas["cancelada"]` | 3 |
| `categoricas` | `X.select_dtypes("object").columns.tolist()` | 3 |
| `numericas` | `[c for c in X.columns if c not in categoricas]` | 3 |
| `prep` | `ColumnTransformer([("num", StandardScaler(), numericas),…` | 3 |
| `modelo` | `Pipeline([("prep", prep), ("m", LogisticRegression(max_it…` | 3 |
| `prob` | `modelo.predict_proba(X_test)[:, 1]` | 3 |
| `pred` | `(prob >= UMBRAL).astype(int)` | 4 |
| `cm` | `confusion_matrix(y_test, pred, normalize="true")` | 4 |
| `auc` | `roc_auc_score(y_test, prob)` | 4 |
| `res` | `permutation_importance(modelo, X_test, y_test, scoring="r…` | 4 |
| `importancias` | `pd.Series(res.importances_mean, index=X_test.columns).sor…` | 4 |
| `fn` | `int(((pred == 0) & (y_test == 1)).sum())` | 4 |
| `fp` | `int(((pred == 1) & (y_test == 0)).sum())` | 4 |
| `coste_con_modelo` | `COSTE_FN * fn + COSTE_FP * fp` | 4 |
| `coste_sin_modelo` | `COSTE_FN * int((y_test == 1).sum())` | 4 |
| `ahorro` | `coste_sin_modelo - coste_con_modelo` | 4 |
| `valores` | `[coste_sin_modelo, coste_con_modelo]` | 5 |
| `barras` | `ax[1, 1].bar(["Sin modelo", "Con modelo"], valores, color…` | 5 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 4 |
| `bar` | Dibuja barras verticales. | 5 |
| `bar_label` | Escribe el valor encima de cada barra. | 5 |
| `barh` | Dibuja barras horizontales. | 5 |
| `columns` | Nombres de las columnas. | 3, 4 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 3 |
| `confusion_matrix` | Cuenta aciertos y fallos de cada tipo (matriz de confusión). | 4 |
| `ConfusionMatrixDisplay` | Dibuja una matriz de confusión. | 5 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 3 |
| `despine` | Quita los bordes superior y derecho del gráfico. | 5 |
| `drop` | Quita columnas o filas. | 3 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 3 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 3 |
| `head` | Muestra las primeras filas. | 5 |
| `int` | Convierte un valor en número entero. | 4 |
| `legend` | Muestra la leyenda del gráfico. | 5 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 3, 4, 5 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 3 |
| `max` | Devuelve el valor más grande. | 5 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 3 |
| `permutation_importance` | Mide qué variables importan estropeándolas una a una. | 4 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 3 |
| `plot` | Dibuja una línea (o puntos unidos). | 5 |
| `predict_proba` | Pide la probabilidad de cada clase (no solo la clase). | 3 |
| `print` | Muestra un valor por pantalla. | 3, 4 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 3 |
| `roc_auc_score` | Calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar). | 3, 4 |
| `roc_curve` | Calcula los puntos de la curva ROC. | 4 |
| `round` | Redondea un número a los decimales indicados. | 3 |
| `savefig` | Guarda el gráfico como imagen. | 5 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `select_dtypes` | Selecciona las columnas de un tipo (numéricas, de texto…). | 3 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 4 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_title` | Pone el título de un gráfico. | 5 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 5 |
| `set_ylabel` | Pone el nombre del eje vertical. | 5 |
| `set_ylim` | Fija el rango del eje vertical. | 5 |
| `show` | Muestra el gráfico. | 5 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 4 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 3 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 5 |
| `sum` | Suma todos los valores. | 4 |
| `suptitle` | Pone un título general a toda la figura. | 5 |
| `text` | Escribe un texto en una posición del gráfico. | 5 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 5 |
| `tolist` | Convierte un array o una columna en una lista de Python. | 3 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 3 |

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
from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay, roc_curve, roc_auc_score,
                             precision_recall_curve, average_precision_score)
from sklearn.inspection import permutation_importance

SEMILLA = 42
np.random.seed(SEMILLA)
sns.set_theme(style="whitegrid")
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
- … y 5 más con las mismas ideas.

### Celda 2 · Parámetros del informe (edítalos) · 🏫

**Qué hace:** >>> EDITA: tu mensaje y tus costes.

```python
# >>> EDITA: tu mensaje y tus costes
TITULAR = "Recomendamos pedir depósito y avisar a las reservas de riesgo alto"
CLIENTE = "TurisData Canarias · Dirección de Ingresos"
AUTORES = "Equipo X (nombres)"
COSTE_FN = 50   # € que perdemos por cada cancelación que el modelo no detecta
COSTE_FP = 30   # € que cuesta tratar como "en riesgo" a quien sí viene
UMBRAL = 0.35   # a partir de qué probabilidad avisamos (elígelo con el gráfico de costes del laboratorio 01)
```

**Qué hace cada línea:**

- `TITULAR = "Recomendamos pedir depósito y avisar a las reservas de riesgo al…` → Guarda el valor en `TITULAR`.
- `CLIENTE = "TurisData Canarias · Dirección de Ingresos"` → Guarda el valor en `CLIENTE`.
- `AUTORES = "Equipo X (nombres)"` → Guarda el valor en `AUTORES`.
- `COSTE_FN = 50 # € que perdemos por cada cancelación que el modelo no detecta` → Guarda el valor en `COSTE_FN`.
- `COSTE_FP = 30 # € que cuesta tratar como "en riesgo" a quien sí viene` → Guarda el valor en `COSTE_FP`.
- `UMBRAL = 0.35 # a partir de qué probabilidad avisamos (elígelo con el gráfi…` → Guarda el valor en `UMBRAL`.

### Celda 3 · 1. Datos y modelo · 🏫

**Qué hace:** Practica `read_csv`, `drop`, `train_test_split`, `tolist` y más (sección «1. Datos y modelo»).

```python
reservas = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
reservas["mes_llegada"] = reservas["fecha_llegada"].dt.month
X = reservas.drop(columns=["id_reserva", "fecha_reserva", "fecha_llegada", "cancelada"])
y = reservas["cancelada"]
X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=SEMILLA)

categoricas = X.select_dtypes("object").columns.tolist()
numericas = [c for c in X.columns if c not in categoricas]
prep = ColumnTransformer([("num", StandardScaler(), numericas), ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas)])
modelo = Pipeline([("prep", prep), ("m", LogisticRegression(max_iter=2000))]).fit(X_ent, y_ent)   # >>> EDITA
prob = modelo.predict_proba(X_test)[:, 1]
print("AUC en prueba:", round(roc_auc_score(y_test, prob), 3), "· reservas de prueba:", len(y_test))
```

**Qué hace cada línea:**

- `reservas = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_…` → Guarda en `reservas` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `reservas["mes_llegada"] = reservas["fecha_llegada"].dt.month` → Guarda en `reservas["mes_llegada"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `X = reservas.drop(columns=["id_reserva", "fecha_reserva", "fecha_llegada",…` → Guarda en `X` el resultado. `drop`: quita columnas o filas.
- `y = reservas["cancelada"]` → Guarda el valor en `y`.
- `X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.25, strat…` → Guarda en `X_ent, X_test, y_ent, y…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `categoricas = X.select_dtypes("object").columns.tolist()` → Guarda en `categoricas` el resultado. `tolist`: convierte un array o una columna en una lista de Python; `columns`: nombres de las columnas; `select_dtypes`: selecciona las columnas de un tipo (numéricas, de texto…).
- `numericas = [c for c in X.columns if c not in categoricas]` → Guarda en `numericas` el resultado. `columns`: nombres de las columnas.
- `prep = ColumnTransformer([("num", StandardScaler(), numericas), ("cat", One…` → Guarda en `prep` el resultado. `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas; `StandardScaler`: escala los números para que tengan media 0 y desviación 1; `OneHotEncoder`: convierte categorías en columnas de 0/1.
- `modelo = Pipeline([("prep", prep), ("m", LogisticRegression(max_iter=2000))…` → Guarda en `modelo` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `Pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- … y 2 más con las mismas ideas.

### Celda 4 · 2. Cálculos que alimentan el panel · 🏫

**Qué hace:** Practica `astype`, `confusion_matrix`, `roc_curve`, `roc_auc_score` y más (sección «2. Cálculos que alimentan el panel»).

```python
pred = (prob >= UMBRAL).astype(int)
cm = confusion_matrix(y_test, pred, normalize="true")
fpr, tpr, _ = roc_curve(y_test, prob)
auc = roc_auc_score(y_test, prob)
res = permutation_importance(modelo, X_test, y_test, scoring="roc_auc", n_repeats=5, random_state=SEMILLA)
importancias = pd.Series(res.importances_mean, index=X_test.columns).sort_values(ascending=False)

fn = int(((pred == 0) & (y_test == 1)).sum())
fp = int(((pred == 1) & (y_test == 0)).sum())
coste_con_modelo = COSTE_FN * fn + COSTE_FP * fp
coste_sin_modelo = COSTE_FN * int((y_test == 1).sum())   # sin modelo: no detectamos ninguna cancelación
ahorro = coste_sin_modelo - coste_con_modelo
print(f"Coste sin modelo: {coste_sin_modelo:,.0f} € · con modelo: {coste_con_modelo:,.0f} € · ahorro: {ahorro:,.0f} € (en {len(y_test)} reservas de prueba)")
```

**Qué hace cada línea:**

- `pred = (prob >= UMBRAL).astype(int)` → Guarda en `pred` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número).
- `cm = confusion_matrix(y_test, pred, normalize="true")` → Guarda en `cm` el resultado. `confusion_matrix`: cuenta aciertos y fallos de cada tipo (matriz de confusión).
- `fpr, tpr, _ = roc_curve(y_test, prob)` → Guarda en `fpr, tpr, _` el resultado. `roc_curve`: calcula los puntos de la curva ROC.
- `auc = roc_auc_score(y_test, prob)` → Guarda en `auc` el resultado. `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar).
- `res = permutation_importance(modelo, X_test, y_test, scoring="roc_auc", n_r…` → Guarda en `res` el resultado. `permutation_importance`: mide qué variables importan estropeándolas una a una.
- `importancias = pd.Series(res.importances_mean, index=X_test.columns).sort_v…` → Guarda en `importancias` el resultado. `sort_values`: ordena la tabla por una o varias columnas; `Series`: crea una columna de pandas (una sola serie de valores); `columns`: nombres de las columnas.
- `fn = int(((pred == 0) & (y_test == 1)).sum())` → Guarda en `fn` el resultado. `int`: convierte un valor en número entero; `sum`: suma todos los valores.
- `fp = int(((pred == 1) & (y_test == 0)).sum())` → Guarda en `fp` el resultado. `int`: convierte un valor en número entero; `sum`: suma todos los valores.
- `coste_con_modelo = COSTE_FN * fn + COSTE_FP * fp` → Guarda el valor en `coste_con_modelo`.
- … y 3 más con las mismas ideas.

### Celda 5 · 3. El panel de una página · 🏫

**Qué hace:** (1) Fiabilidad: matriz de confusión.

```python
fig, ax = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle(TITULAR, fontsize=16, fontweight="bold", x=0.02, ha="left")

# (1) Fiabilidad: matriz de confusión
ConfusionMatrixDisplay(cm, display_labels=["No cancela", "Cancela"]).plot(ax=ax[0, 0], cmap="Blues", values_format=".0%", colorbar=False)
ax[0, 0].set_title(f"Detectamos el {cm[1, 1]:.0%} de las cancelaciones,\ncon un {cm[0, 1]:.0%} de falsas alarmas")   # >>> EDITA el título si cambian los números
ax[0, 0].set_xlabel("Lo que dijo el modelo"); ax[0, 0].set_ylabel("Lo que ocurrió")

# (2) Fiabilidad: curva ROC
ax[0, 1].plot(fpr, tpr, color="tab:blue", label=f"Modelo (AUC = {auc:.2f})")
ax[0, 1].plot([0, 1], [0, 1], "--", color="gray", label="Azar")
ax[0, 1].set_title("Acierta bastante mejor que el azar, pero no es perfecto")   # >>> EDITA
ax[0, 1].set_xlabel("Falsas alarmas"); ax[0, 1].set_ylabel("Cancelaciones detectadas"); ax[0, 1].legend(loc="lower right")

# (3) Qué mueve el resultado
importancias.head(6)[::-1].plot.barh(ax=ax[1, 0], color="tab:blue")
ax[1, 0].set_title("Lo que más pesa en una cancelación")   # >>> EDITA: nombra la variable líder
ax[1, 0].set_xlabel("Caída del AUC al desordenar la variable")

# (4) Valor para el negocio
valores = [coste_sin_modelo, coste_con_modelo]
barras = ax[1, 1].bar(["Sin modelo", "Con modelo"], valores, color=["lightgray", "tab:green"])
ax[1, 1].bar_label(barras, fmt="{:,.0f} €", padding=3)
ax[1, 1].set_title(f"Con el modelo perdemos {ahorro:,.0f} € menos en {len(y_test)} reservas")   # >>> EDITA
ax[1, 1].set_ylabel("Coste de las cancelaciones (€)"); ax[1, 1].set_ylim(0, max(valores) * 1.15)

fig.text(0.02, 0.005, f"{CLIENTE} · {AUTORES} · Datos sintéticos de TurisData · modelo: regresión logística · umbral {UMBRAL:.2f} · semilla {SEMILLA}",
         fontsize=8, color="gray")
sns.despine()
plt.tight_layout(rect=(0, 0.02, 1, 0.96))
plt.savefig("informe_visual_panel.png", dpi=150)
plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(2, 2, figsize=(13, 9))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `fig.suptitle(TITULAR, fontsize=16, fontweight="bold", x=0.02, ha="left")` → `suptitle`: pone un título general a toda la figura.
- `ConfusionMatrixDisplay(cm, display_labels=["No cancela", "Cancela"]).plot(a…` → `plot`: dibuja una línea (o puntos unidos); `ConfusionMatrixDisplay`: dibuja una matriz de confusión.
- `ax[0, 0].set_title(f"Detectamos el {cm[1, 1]:.0%} de las cancelaciones,\nco…` → `set_title`: pone el título de un gráfico.
- `ax[0, 0].set_xlabel("Lo que dijo el modelo"); ax[0, 0].set_ylabel("Lo que o…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax[0, 0].set_xlabel("Lo que dijo el modelo"); ax[0, 0].set_ylabel("Lo que o…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax[0, 1].plot(fpr, tpr, color="tab:blue", label=f"Modelo (AUC = {auc:.2f})")` → `plot`: dibuja una línea (o puntos unidos).
- `ax[0, 1].plot([0, 1], [0, 1], "--", color="gray", label="Azar")` → `plot`: dibuja una línea (o puntos unidos).
- `ax[0, 1].set_title("Acierta bastante mejor que el azar, pero no es perfecto…` → `set_title`: pone el título de un gráfico.
- … y 17 más con las mismas ideas.

---
*Generado a partir de `laboratorios/fuentes/S13_02_plantilla_informe_visual.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
