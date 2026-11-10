# Código explicado · S07.04 · Curvas ROC y PR, y qué hacer con clases desbalanceadas

> **Para qué sirve.** Aquí está **todo el código del cuaderno explicado por escrito**, celda a celda y en el mismo orden. Cada bloque sigue siempre el mismo guion: **primero** un párrafo que dice qué vamos a hacer, por qué y qué debe salir; **después** el código, con **cada línea explicada**; y **al final** lo destacable del bloque (lo que conviene recordar y con qué se relaciona).
>
> **Cuaderno:** [🏫 en clase](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_04_roc_pr_desbalance_en_clase.ipynb) · [🏠 completo](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_04_roc_pr_desbalance.ipynb)
>
> **Cómo usarlo:** ejecuta la celda en el cuaderno; busca aquí la del mismo número (A3, A5…); lee el párrafo, sigue el código línea a línea y, al terminar, cambia algo (un número, una columna) y comprueba si pasa lo que esperabas: es la mejor manera de entender código.

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda** («coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`»). Lo que va tras `#` es un comentario: Python lo ignora. Los ejercicios (✏️) llevan aquí la **solución de referencia**: úsala **después** de intentarlo.

## La idea del cuaderno

Ahora la cancelación es un suceso **raro**: solo el **6 %** de las reservas se cancela. Un modelo que diga siempre «no cancela» acertaría el 94 %… y sería **inútil**. Esta práctica enseña a **no fiarse de la exactitud** cuando una clase es rara, a evaluar con **curvas ROC y PR** y a probar tres remedios: **pesos por clase**, **submuestreo** y **mover el umbral**.

- **Hilo del cuaderno:** montamos el escenario raro (A1) → vemos que el modelo «tonto» acierta el 94 % (A2) → entrenamos el modelo base (A3) → lo evaluamos con la **curva ROC** y el **AUC** (A4) → con la **curva precisión–recall** y el **AP** (A5, A6) → probamos **pesos por clase** (A7), **submuestreo** (A8) y **umbral por objetivo de recall** (A9) → comparamos todo (A10).
- **Lo que te llevas:** con clases raras la **exactitud engaña**; AUC y AP miden la calidad de las **probabilidades** sin fijar umbral; los tres remedios suben el recall a cambio de **bajar la precisión**; y cuál elegir depende de lo que cueste cada error.

## Mapa de celdas

| Celda | Tipo | Qué hacemos | ¿Dónde? |
|---|---|---|---|
| A1 | ⚙️ Preparación | Preparar los datos: un escenario con clases raras | 🏫 |
| A2 | ✏️ Ejercicio | El modelo «inútil» que acierta el 94 % | 🏠 |
| A3 | 👀 Ejemplo | El modelo base | 🏫 |
| A4 | ✏️ Ejercicio | Curva ROC y AUC | 🏫 |
| A5 | 👀 Ejemplo | Curva precisión–recall y AP | 🏠 |
| A6 | ✏️ Ejercicio | ¿Cuántas veces mejor que el azar? | 🏠 |
| A7 | ✏️ Ejercicio | Remedio 1: pesos por clase | 🏠 |
| A8 | ✏️ Ejercicio | Remedio 2: submuestreo | 🏠 |
| A9 | ✏️ Ejercicio | Remedio 3: mover el umbral hasta un objetivo de recall | 🏠 |
| A10 | 🎯 Mini-reto | Comparativa de los tres modelos | 🏠 |

🏫 = en clase · 🏠 = en casa. 👀 ejemplo: solo se ejecuta y se mira. ✏️ ejercicio: se completa con tu código. ⚙️ preparación: se ejecuta sola.

## Celda a celda

### ⚙️ A1 · Preparación — Preparar los datos: un escenario con clases raras

**Qué vamos a hacer y qué debe salir**

Celda de preparación: se ejecuta **la primera**. Además de traer librerías y cargar las reservas, **fabrica el escenario raro**: conserva todas las reservas no canceladas y solo una pequeña parte de las canceladas, de modo que las cancelaciones sean ≈ **6 %** del total. Después reparte los datos (70 % train / 30 % test, manteniendo la proporción), define el preprocesado `prep` y una función `nuevo_modelo` que crea una regresión logística lista para usar, con la opción de cambiarle ajustes. **Debe salir** `Reservas: 3453 · canceladas: 207 (6.0%)` y `Listo ✔`. Todo lo demás parte de aquí.

```python
import os, urllib.request

BASE_URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/"

def dato(nombre):
    """Devuelve la ruta local de un archivo de datos del curso (lo descarga si no está)."""
    for carpeta in ("datos", "../datos", "../../datos", "../../../datos"):
        ruta = os.path.join(carpeta, nombre)
        if os.path.exists(ruta):
            return ruta
    os.makedirs("datos", exist_ok=True)
    ruta = os.path.join("datos", nombre)
    urllib.request.urlretrieve(BASE_URL + nombre, ruta)
    return ruta

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.utils import resample
from sklearn.base import clone
from sklearn.metrics import (roc_curve, roc_auc_score, precision_recall_curve, average_precision_score,
                             precision_score, recall_score, accuracy_score)

warnings.filterwarnings("ignore", category=UserWarning)
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)

# Escenario simulado: conservamos todas las no canceladas y una parte de las canceladas (≈ 6 %)
neg = df[df["cancelada"] == 0]
pos = df[df["cancelada"] == 1].sample(n=int(len(neg) * 0.064), random_state=SEMILLA)
raro = pd.concat([neg, pos]).sample(frac=1, random_state=SEMILLA).reset_index(drop=True)
print(f"Reservas: {len(raro)} · canceladas: {raro['cancelada'].sum()} ({raro['cancelada'].mean():.1%})")

columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = raro[columnas_num + columnas_cat], raro["cancelada"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEMILLA, stratify=y)

prep = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore"))]), columnas_cat),
])

def nuevo_modelo(**kwargs):
    # clone(prep): cada modelo necesita su propia copia del preprocesado (si no, se pisarían entre sí)
    return Pipeline([("prep", clone(prep)), ("clf", LogisticRegression(max_iter=1000, **kwargs))])
print("Listo ✔")
```

**Línea a línea**

- `import os, urllib.request`  
  Trae dos herramientas de Python que ya vienen instaladas: `os` (para trabajar con carpetas y rutas de ficheros) y `urllib.request` (para descargar cosas de internet).
- `BASE_URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/"`  
  Guarda en una variable la dirección de internet donde están los datos del curso (el repositorio del alumnado). Si un fichero no está en tu ordenador, se descargará de ahí.
- `def dato(nombre):`  
  Define una **función** llamada `dato`: un trozo de código con nombre que se puede usar muchas veces. Recibe el nombre de un fichero (por ejemplo `"reservas_turisdata.csv"`) y devuelve **dónde está en tu ordenador**.
- `"""Devuelve la ruta local de un archivo de datos del curso (lo descarga si no está)."""`  
  El texto entre comillas triples es la **descripción** de la función (no hace nada, solo documenta).
- `for carpeta in ("datos", "../datos", "../../datos", "../../../datos"):`  
  Recorre una lista de carpetas posibles: `datos`, `../datos`, `../../datos`… (el cuaderno puede estar a distinta profundidad que los datos).
- `ruta = os.path.join(carpeta, nombre)`  
  Construye la ruta uniendo carpeta y nombre de fichero (`datos/reservas_turisdata.csv`).
- `if os.path.exists(ruta):`  
  Pregunta: ¿existe ese fichero en esa ruta?
- `return ruta`  
  Si existe, **devuelve la ruta y termina**: ya lo tiene.
- `os.makedirs("datos", exist_ok=True)`  
  Si no lo encontró en ninguna carpeta, crea la carpeta `datos` (`exist_ok=True`: sin error si ya existe).
- `ruta = os.path.join("datos", nombre)`  
  Prepara la ruta donde guardará el fichero descargado.
- `urllib.request.urlretrieve(BASE_URL + nombre, ruta)`  
  **Descarga** el fichero desde `BASE_URL` y lo guarda en esa ruta.
- `return ruta`  
  Devuelve la ruta del fichero recién descargado. Gracias a `dato`, el cuaderno funciona igual en Colab que en tu ordenador.
- `import warnings`  
  Trae `warnings`, para silenciar avisos que no aportan nada.
- `import numpy as np`  
  Trae **NumPy** (`np`).
- `import pandas as pd`  
  Trae **pandas** (`pd`).
- `import matplotlib.pyplot as plt`  
  Trae **matplotlib** (`plt`).
- `import seaborn as sns`  
  Trae **seaborn** (`sns`).
- `from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedKFold`  
  Trae `train_test_split`, `cross_val_predict` (predicciones por validación cruzada) y `StratifiedKFold` (trozos que respetan la proporción de cada clase).
- `from sklearn.linear_model import LogisticRegression`  
  Trae `LogisticRegression`.
- `from sklearn.dummy import DummyClassifier`  
  Trae `DummyClassifier`: un clasificador «tonto» que sirve de referencia.
- `from sklearn.impute import SimpleImputer`  
  Trae `SimpleImputer`: rellena huecos.
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder`  
  Trae `StandardScaler` y `OneHotEncoder`.
- `from sklearn.compose import ColumnTransformer`  
  Trae `ColumnTransformer`.
- `from sklearn.pipeline import Pipeline`  
  Trae `Pipeline`.
- `from sklearn.utils import resample`  
  Trae `resample`: saca una **muestra** de filas (se usará para el submuestreo).
- `from sklearn.base import clone`  
  Trae `clone`: copia sin entrenar de un objeto.
- `from sklearn.metrics import (roc_curve, roc_auc_score, precision_recall_curve, average_precision_score,` … `precision_score, recall_score, accuracy_score)` (2 líneas)  
  Trae las métricas: curva ROC y AUC (`roc_curve`, `roc_auc_score`), curva precisión–recall y AP (`precision_recall_curve`, `average_precision_score`), y `precision_score`, `recall_score`, `accuracy_score`.
- `warnings.filterwarnings("ignore", category=UserWarning)`  
  Oculta los avisos de tipo `UserWarning`.
- `SEMILLA = 42`  
  Número fijo (`42`) para que los sorteos salgan siempre igual.
- `sns.set_theme(style="whitegrid")`  
  Estilo visual de los gráficos.
- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])`  
  Lee las reservas en `df`; `parse_dates` marca las dos columnas de fecha.
- `df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)`  
  Crea `temporada_alta` (1 si el mes de llegada es 1, 2, 3, 7, 8 o 12; 0 si no) directamente a partir de la fecha.
- `# Escenario simulado: conservamos todas las no canceladas y una parte de las canceladas (≈ 6 %)`  
  Comentario: explica lo que se hace a continuación.
- `neg = df[df["cancelada"] == 0]`  
  `neg`: **todas** las reservas no canceladas.
- `pos = df[df["cancelada"] == 1].sample(n=int(len(neg) * 0.064), random_state=SEMILLA)`  
  `pos`: una **muestra** de las canceladas, del tamaño del 6,4 % de las no canceladas (`.sample(n=…)`; `random_state` fija el sorteo). Así las positivas serán ≈ 6 % del total.
- `raro = pd.concat([neg, pos]).sample(frac=1, random_state=SEMILLA).reset_index(drop=True)`  
  Une las dos partes (`pd.concat`), **mezcla** las filas (`sample(frac=1)`: todas, en otro orden) y renumera el índice (`reset_index(drop=True)`).
- `print(f"Reservas: {len(raro)} · canceladas: {raro['cancelada'].sum()} ({raro['cancelada'].mean():.1%})")`  
  Escribe el total (3453), cuántas canceladas hay (la suma de unos: 207) y el porcentaje (`mean` con `:.1%`: 6,0 %).
- `columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",` … `"peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]` (2 líneas)  
  Las 9 columnas numéricas.
- `columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]`  
  Las 6 columnas de texto.
- `X, y = raro[columnas_num + columnas_cat], raro["cancelada"]`  
  `X` = variables para predecir; `y` = `cancelada`.
- `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEMILLA, stratify=y)`  
  Reparte: 70 % para entrenar y 30 % (`test_size=0.3`) para evaluar; **`stratify=y`** mantiene el 6 % de cancelaciones en ambas partes (2417 en train y 1036 en test).
- `prep = ColumnTransformer([` … `])` (5 líneas)  
  Preprocesado en dos ramas: números (huecos con la mediana + escalado) y texto (huecos con el más frecuente + columnas 0/1).
- `def nuevo_modelo(**kwargs):`  
  Define una función que fabrica un modelo **nuevo** cada vez que se llama. `**kwargs` permite pasarle ajustes extra a la regresión logística (por ejemplo `class_weight="balanced"`).
- `# clone(prep): cada modelo necesita su propia copia del preprocesado (si no, se pisarían entre sí)`  
  Comentario: cada modelo necesita **su propia copia** del preprocesado; si no, al entrenar uno se pisaría el otro.
- `return Pipeline([("prep", clone(prep)), ("clf", LogisticRegression(max_iter=1000, **kwargs))])`  
  Devuelve un `Pipeline` con el preprocesado (una copia: `clone(prep)`) y la regresión logística con los ajustes recibidos.
- `print("Listo ✔")`  
  Mensaje de que todo ha ido bien.

**Lo destacable**

- La celda de preparación **se ejecuta siempre la primera**, y otra vez si Colab se reinicia: todas las demás celdas usan lo que crea aquí (`df`, `SEMILLA`, las librerías…). Si ves `NameError: name '…' is not defined`, casi siempre es que falta ejecutarla.
- **El escenario se fabrica a propósito:** en los datos originales las cancelaciones son casi la mitad; aquí se reducen al 6 % para simular un suceso raro (como un fraude).
- `stratify=y` es **imprescindible** con clases raras: sin él, el test podría quedarse con muy pocas positivas.
- `clone(prep)` evita que dos modelos **compartan** el mismo preprocesado.

### ✏️ A2 · Ejercicio — El modelo «inútil» que acierta el 94 %

**Qué vamos a hacer y qué debe salir**

Antes de entrenar nada, medimos el **suelo**: un clasificador que **siempre** responde la clase más frecuente (`most_frequent` = «no cancela»). No aprende nada, pero con un 6 % de cancelaciones **acierta el 94 %**. Calculamos su exactitud y su **recall** (qué parte de las cancelaciones detecta). **Debe salir** `Exactitud del modelo inútil: 94.0% · recall: 0%` y `✔ Ejercicio 1 correcto`. Moraleja: una exactitud alta **no demuestra nada** cuando una clase es rara; hay que mirar el **recall** de la clase que importa. Se apoya en A1.

```python
tonto = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
pred_tonto = tonto.predict(X_test)
acc_tonto = accuracy_score(y_test, pred_tonto)
recall_tonto = recall_score(y_test, pred_tonto)
assert acc_tonto > 0.9, "El modelo que dice siempre «no cancela» acierta más del 90 %"
assert recall_tonto == 0, "…pero no detecta ninguna cancelación (recall = 0)"
print(f"Exactitud del modelo inútil: {acc_tonto:.1%} · recall: {recall_tonto:.0%}")
print("✔ Ejercicio 1 correcto")
```

**Línea a línea**

- `tonto = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)`  
  Crea y entrena el clasificador «tonto» (`strategy="most_frequent"`: responde siempre la clase más común) con los datos de train.
- `pred_tonto = tonto.predict(X_test)`  
  Sus predicciones para test: todo ceros.
- `acc_tonto = accuracy_score(y_test, pred_tonto)`  
  **Exactitud** (*accuracy*): porcentaje de aciertos.
- `recall_tonto = recall_score(y_test, pred_tonto)`  
  **Recall**: de las cancelaciones reales, cuántas detecta.
- `assert acc_tonto > 0.9, "El modelo que dice siempre «no cancela» acierta más del 90 %"` … `assert recall_tonto == 0, "…pero no detecta ninguna cancelación (recall = 0)"` (2 líneas)  
  Dos comprobaciones: la exactitud supera el 90 % y el recall es exactamente 0.
- `print(f"Exactitud del modelo inútil: {acc_tonto:.1%} · recall: {recall_tonto:.0%}")`  
  Escribe la exactitud con 1 decimal en porcentaje (`:.1%`) y el recall sin decimales (`:.0%`).
- `print("✔ Ejercicio 1 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Exactitud alta + recall 0 = modelo inútil.** Con clases raras, la exactitud engaña.
- Un **modelo de referencia (*baseline*)** dice cuánto hay que superar: cualquier modelo real debe batir el 94 %… y, sobre todo, detectar cancelaciones.
- `assert` con un `==` exacto (`recall_tonto == 0`) funciona aquí porque el resultado es exactamente 0.

### 👀 A3 · Ejemplo — El modelo base

**Qué vamos a hacer y qué debe salir**

Entrenamos la regresión logística **sin ningún truco** y guardamos sus **probabilidades** para test: serán la materia prima de las curvas ROC y PR. **Debe salir** `Reservas de test: 1036 · canceladas: 62`: de 1036 reservas de test solo 62 son cancelaciones, y esas 62 son las que importan. Se apoya en `nuevo_modelo` (A1).

```python
base = nuevo_modelo().fit(X_train, y_train)
proba_base = base.predict_proba(X_test)[:, 1]
print("Reservas de test:", len(y_test), "· canceladas:", int(y_test.sum()))
```

**Línea a línea**

- `base = nuevo_modelo().fit(X_train, y_train)`  
  Crea un modelo nuevo (sin ajustes extra) y lo entrena con train.
- `proba_base = base.predict_proba(X_test)[:, 1]`  
  Probabilidad de cancelar para cada reserva de test (`[:, 1]` = segunda columna de `predict_proba`).
- `print("Reservas de test:", len(y_test), "· canceladas:", int(y_test.sum()))`  
  Escribe cuántas reservas hay en test y cuántas son cancelaciones (`y_test.sum()` suma los unos; `int` la deja como número entero).

**Lo destacable**

- **Solo 62 positivas en test:** cualquier métrica de la clase rara es **frágil** (unas pocas reservas cambian mucho el resultado).
- Se guardan las **probabilidades** (`proba_base`) y no las etiquetas: las curvas ROC y PR se construyen con probabilidades, para todos los umbrales a la vez.

### ✏️ A4 · Ejercicio — Curva ROC y AUC

**Qué vamos a hacer y qué debe salir**

La **curva ROC** responde a esta pregunta: *si voy bajando el umbral, ¿cuánto recall gano (eje vertical) y a cambio de cuántas falsas alarmas (eje horizontal)?* Cada punto de la curva es un umbral distinto. El **AUC** (área bajo la curva) lo resume en un número: **1** = perfecto, **0,5** = azar (la diagonal). **Debe salir** una curva por encima de la diagonal, `AUC = 0.774` y `✔ Ejercicio 2 correcto`. Un AUC de 0,77 es **razonable**: el modelo ordena bien las reservas (las que cancelan suelen tener más probabilidad que las que no), aunque esté lejos de ser perfecto. Se apoya en `proba_base` (A3).

```python
fpr, tpr, _ = roc_curve(y_test, proba_base)
auc = roc_auc_score(y_test, proba_base)
assert len(fpr) == len(tpr) and fpr[0] == 0 and tpr[-1] == 1, "fpr y tpr deben ser la curva ROC completa"
assert 0.6 < auc < 0.95, "El AUC de este modelo debería estar entre 0,6 y 0,95"

plt.figure(figsize=(5.5, 5))
plt.plot(fpr, tpr, color="#2a6f97", lw=2, label=f"Regresión logística (AUC = {auc:.2f})")
plt.plot([0, 1], [0, 1], "--", color="gray", label="Azar (AUC = 0,50)")
plt.title("Curva ROC")
plt.xlabel("Tasa de falsos positivos (falsas alarmas)")
plt.ylabel("Tasa de verdaderos positivos (recall)")
plt.legend(loc="lower right")
plt.show()
print(f"AUC = {auc:.3f}")
print("✔ Ejercicio 2 correcto")
```

**Línea a línea**

- `fpr, tpr, _ = roc_curve(y_test, proba_base)`  
  `roc_curve` calcula, para cada umbral, la **tasa de falsos positivos** (`fpr`: falsas alarmas entre las no canceladas) y la **tasa de verdaderos positivos** (`tpr` = recall). El tercer valor (los umbrales) se descarta con `_`.
- `auc = roc_auc_score(y_test, proba_base)`  
  `roc_auc_score` da el **área bajo la curva** directamente.
- `assert len(fpr) == len(tpr) and fpr[0] == 0 and tpr[-1] == 1, "fpr y tpr deben ser la curva ROC completa"` … `assert 0.6 < auc < 0.95, "El AUC de este modelo debería estar entre 0,6 y 0,95"` (2 líneas)  
  Dos comprobaciones: `fpr` y `tpr` forman la curva completa (misma longitud, empieza en 0 y termina en 1) y el AUC está entre 0,6 y 0,95.
- `plt.figure(figsize=(5.5, 5))`  
  Crea la figura (casi cuadrada: 5,5 × 5).
- `plt.plot(fpr, tpr, color="#2a6f97", lw=2, label=f"Regresión logística (AUC = {auc:.2f})")`  
  Dibuja la curva ROC; en la leyenda (`label`) se incluye el AUC con 2 decimales.
- `plt.plot([0, 1], [0, 1], "--", color="gray", label="Azar (AUC = 0,50)")`  
  Dibuja la **diagonal** (de (0,0) a (1,1)): lo que haría un modelo que adivina al azar.
- `plt.title("Curva ROC")`  
  Título.
- `plt.xlabel("Tasa de falsos positivos (falsas alarmas)")`  
  Eje horizontal: falsas alarmas.
- `plt.ylabel("Tasa de verdaderos positivos (recall)")`  
  Eje vertical: recall.
- `plt.legend(loc="lower right")`  
  Muestra la leyenda en la esquina inferior derecha (`loc`).
- `plt.show()`  
  Muestra la figura.
- `print(f"AUC = {auc:.3f}")`  
  Escribe el AUC con 3 decimales.
- `print("✔ Ejercicio 2 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **AUC = probabilidad de que el modelo dé más probabilidad a una cancelación real que a una no cancelada**, elegidas al azar. 0,5 = azar; 1 = perfecto.
- La curva **no depende del umbral**: evalúa el modelo en todos a la vez.
- **Cuidado con clases raras:** el eje horizontal divide entre los ≈ 970 negativos de test, así que muchas falsas alarmas en números absolutos se ven como una tasa pequeña y la ROC puede salir optimista.
- El `_` es el nombre que se usa para un valor que **no te interesa**.

### 👀 A5 · Ejemplo — Curva precisión–recall y AP

**Qué vamos a hacer y qué debe salir**

La **curva precisión–recall (PR)** muestra lo mismo desde otro ángulo, más útil con clases raras: *según detecto más cancelaciones (recall), ¿qué proporción de mis alarmas son acertadas (precisión)?* Su resumen es el **AP** (precisión media). La referencia del azar aquí **no es la diagonal** sino una **línea horizontal a la altura de la prevalencia** (la proporción de positivas: ≈ 0,06): si avisas al azar, solo aciertas en esa proporción. **Debe salir** una curva que **empieza alta y cae rápido**, con `AP = 0.24` en la leyenda, muy por encima de la línea de la prevalencia (0,06). Se apoya en `proba_base` (A3).

```python
prec, rec, _ = precision_recall_curve(y_test, proba_base)
ap = average_precision_score(y_test, proba_base)
prevalencia = y_test.mean()
plt.figure(figsize=(5.5, 5))
plt.plot(rec, prec, color="#2a6f97", lw=2, label=f"Regresión logística (AP = {ap:.2f})")
plt.axhline(prevalencia, ls="--", color="gray", label=f"Azar (= prevalencia {prevalencia:.2f})")
plt.title("Curva precisión–recall")
plt.xlabel("Recall (cancelaciones detectadas)")
plt.ylabel("Precisión (alarmas acertadas)")
plt.legend()
plt.show()
```

**Línea a línea**

- `prec, rec, _ = precision_recall_curve(y_test, proba_base)`  
  `precision_recall_curve` devuelve la precisión y el recall para cada umbral (el tercer valor, los umbrales, se descarta).
- `ap = average_precision_score(y_test, proba_base)`  
  `average_precision_score` resume la curva en un número: el **AP**.
- `prevalencia = y_test.mean()`  
  `y_test.mean()`: proporción de cancelaciones en test (≈ 0,06).
- `plt.figure(figsize=(5.5, 5))`  
  Crea la figura.
- `plt.plot(rec, prec, color="#2a6f97", lw=2, label=f"Regresión logística (AP = {ap:.2f})")`  
  Dibuja la curva PR: recall en horizontal, precisión en vertical (el AP va en la leyenda).
- `plt.axhline(prevalencia, ls="--", color="gray", label=f"Azar (= prevalencia {prevalencia:.2f})")`  
  Línea horizontal discontinua en la prevalencia: el **nivel del azar**.
- `plt.title("Curva precisión–recall")`  
  Título.
- `plt.xlabel("Recall (cancelaciones detectadas)")`  
  Eje horizontal: recall.
- `plt.ylabel("Precisión (alarmas acertadas)")`  
  Eje vertical: precisión.
- `plt.legend()`  
  Muestra la leyenda.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **El azar en PR es la prevalencia, no 0,5:** con clases raras el listón es muy bajo, y por eso se compara el AP con ella.
- La curva PR **se fija en la clase rara** (ignora los verdaderos negativos), así que es más sincera que la ROC cuando hay desbalanceo.
- Se lee de derecha a izquierda como un compromiso: **más recall → menos precisión**.

### ✏️ A6 · Ejercicio — ¿Cuántas veces mejor que el azar?

**Qué vamos a hacer y qué debe salir**

El AP de 0,24 solo se entiende **comparado** con el azar. Lo calculamos como un cociente: AP ÷ prevalencia. **Debe salir** `AP = 0.24: el modelo es 4.0 veces mejor que el azar en precisión.` y `✔ Ejercicio 3 correcto`. Es decir: avisando según el modelo, el 24 % de las alarmas (de media) aciertan; avisando al azar, el 6 %. **4 veces mejor** es una ventaja clara, aunque 24 % de precisión sigue siendo bajo en términos absolutos. Se apoya en A3 y A5.

```python
ap_base = average_precision_score(y_test, proba_base)
veces_mejor_que_azar = ap_base / prevalencia
assert 0 < ap_base < 1
assert veces_mejor_que_azar > 1.5, "El modelo debería ser claramente mejor que el azar"
print(f"AP = {ap_base:.2f}: el modelo es {veces_mejor_que_azar:.1f} veces mejor que el azar en precisión.")
print("✔ Ejercicio 3 correcto")
```

**Línea a línea**

- `ap_base = average_precision_score(y_test, proba_base)`  
  AP del modelo base.
- `veces_mejor_que_azar = ap_base / prevalencia`  
  Cociente: AP ÷ prevalencia (el nivel del azar).
- `assert 0 < ap_base < 1`  
  Comprobación: el AP está entre 0 y 1.
- `assert veces_mejor_que_azar > 1.5, "El modelo debería ser claramente mejor que el azar"`  
  Comprobación: el modelo es **más de 1,5 veces** mejor que el azar.
- `print(f"AP = {ap_base:.2f}: el modelo es {veces_mejor_que_azar:.1f} veces mejor que el azar en precisión.")`  
  Escribe el AP (2 decimales) y cuántas veces mejora al azar (1 decimal).
- `print("✔ Ejercicio 3 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Una métrica sin referencia no dice nada:** un AP de 0,24 es bueno o malo según la prevalencia (0,06).
- Un cociente «veces mejor que el azar» es fácil de **explicar a negocio**.
- La **precisión absoluta sigue baja**: aunque el modelo sea 4× mejor que el azar, ~3 de cada 4 alarmas serían falsas.

### ✏️ A7 · Ejercicio — Remedio 1: pesos por clase

**Qué vamos a hacer y qué debe salir**

Primer remedio: decirle al modelo que **equivocarse con una cancelación cuesta más** que equivocarse con una no cancelada. Con `class_weight="balanced"` cada reserva cancelada **pesa unas 16 veces más** que una no cancelada (así las dos clases pesan lo mismo en conjunto). El modelo se esfuerza entonces en detectar las cancelaciones. Comparamos el **recall** del modelo base y del ponderado. **Debe salir** `Recall: 3% → 73% · precisión del ponderado: 14%` y `✔ Ejercicio 4 correcto`. El recall **se dispara** (del 3 % al 73 %), pero la precisión cae al 14 %: ahora detecta casi todo lo que cancela, a cambio de muchas **falsas alarmas**. Se apoya en `nuevo_modelo` (A1) y `base` (A3).

```python
con_pesos = nuevo_modelo(class_weight="balanced").fit(X_train, y_train)
recall_base = recall_score(y_test, base.predict(X_test))
recall_pesos = recall_score(y_test, con_pesos.predict(X_test))
precision_pesos = precision_score(y_test, con_pesos.predict(X_test))
assert recall_pesos > recall_base, "Con pesos por clase el recall debería subir"
assert recall_pesos > 0.5, "El modelo ponderado debería detectar más de la mitad de las cancelaciones"
print(f"Recall: {recall_base:.0%} → {recall_pesos:.0%} · precisión del ponderado: {precision_pesos:.0%}")
print("✔ Ejercicio 4 correcto")
```

**Línea a línea**

- `con_pesos = nuevo_modelo(class_weight="balanced").fit(X_train, y_train)`  
  Crea el modelo con `class_weight="balanced"` y lo entrena con train.
- `recall_base = recall_score(y_test, base.predict(X_test))`  
  Recall del modelo base **con el umbral 0,5** (`predict` usa 0,5): solo detecta el 3 %.
- `recall_pesos = recall_score(y_test, con_pesos.predict(X_test))`  
  Recall del modelo ponderado.
- `precision_pesos = precision_score(y_test, con_pesos.predict(X_test))`  
  Precisión del modelo ponderado: de las alarmas que da, cuántas aciertan.
- `assert recall_pesos > recall_base, "Con pesos por clase el recall debería subir"`  
  Comprobación: con pesos, el recall sube.
- `assert recall_pesos > 0.5, "El modelo ponderado debería detectar más de la mitad de las cancelaciones"`  
  Comprobación: el modelo ponderado detecta más de la mitad de las cancelaciones.
- `print(f"Recall: {recall_base:.0%} → {recall_pesos:.0%} · precisión del ponderado: {precision_pesos:.0%}")`  
  Escribe el recall antes y después y la precisión del ponderado, en porcentaje sin decimales.
- `print("✔ Ejercicio 4 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **`class_weight="balanced"`:** una línea que cambia el comportamiento del modelo; la clase rara pesa más al entrenar.
- **Efecto colateral:** más recall → **menos precisión**. No hay remedio gratis.
- El modelo base con umbral 0,5 casi no avisa nunca (recall 3 %): con clases raras, **el 0,5 es un mal umbral**.

### ✏️ A8 · Ejercicio — Remedio 2: submuestreo

**Qué vamos a hacer y qué debe salir**

Segundo remedio: en vez de dar más peso a las positivas, **tirar parte de las negativas** para que el entrenamiento esté menos desequilibrado. Guardamos **todas** las cancelaciones de train (145) y solo el **doble** de no canceladas elegidas al azar (290): quedan **435 filas** en lugar de 2417, con 2 negativas por cada positiva. Entrenamos con ese conjunto reducido. **Debe salir** `X_sub: 435 filas (145 positivas y 290 negativas) · recall con submuestreo: 45%` y `✔ Ejercicio 5 correcto`. El recall sube del 3 % al 45 % (menos que con pesos), pero a costa de **tirar casi el 80 % de los datos**. Se apoya en `nuevo_modelo` (A1) y `recall_base` (A7).

```python
pos_tr = X_train[y_train == 1]
neg_tr = X_train[y_train == 0]
neg_sub = resample(neg_tr, replace=False, n_samples=2 * len(pos_tr), random_state=SEMILLA)
X_sub = pd.concat([pos_tr, neg_sub])
y_sub = pd.Series([1] * len(pos_tr) + [0] * len(neg_sub), index=X_sub.index)
con_submuestreo = nuevo_modelo().fit(X_sub, y_sub)
assert y_sub.sum() * 2 == (y_sub == 0).sum(), "Debe haber el doble de negativas que de positivas"
assert len(X_sub) < len(X_train) / 3, "El submuestreo reduce mucho el tamaño del entrenamiento"
assert recall_score(y_test, con_submuestreo.predict(X_test)) > recall_base, "El submuestreo debería subir el recall"
print(f"X_sub: {len(X_sub)} filas ({int(y_sub.sum())} positivas y {int((y_sub == 0).sum())} negativas) · recall con submuestreo: {recall_score(y_test, con_submuestreo.predict(X_test)):.0%}")
print("✔ Ejercicio 5 correcto")
```

**Línea a línea**

- `pos_tr = X_train[y_train == 1]`  
  Filas de train que son cancelaciones (145).
- `neg_tr = X_train[y_train == 0]`  
  Filas de train que no lo son.
- `neg_sub = resample(neg_tr, replace=False, n_samples=2 * len(pos_tr), random_state=SEMILLA)`  
  `resample` saca una muestra **sin repetir** (`replace=False`) de **el doble** de filas que positivas (`2 * len(pos_tr)` = 290).
- `X_sub = pd.concat([pos_tr, neg_sub])`  
  Une positivas y la muestra de negativas: el nuevo conjunto de entrenamiento.
- `y_sub = pd.Series([1] * len(pos_tr) + [0] * len(neg_sub), index=X_sub.index)`  
  Construye las etiquetas a mano: un 1 por cada positiva y un 0 por cada negativa (`[1] * n` repite el valor `n` veces), con el mismo índice que `X_sub`.
- `con_submuestreo = nuevo_modelo().fit(X_sub, y_sub)`  
  Entrena un modelo nuevo con ese conjunto reducido.
- `assert y_sub.sum() * 2 == (y_sub == 0).sum(), "Debe haber el doble de negativas que de positivas"`  
  Comprobación: hay el doble de negativas que de positivas.
- `assert len(X_sub) < len(X_train) / 3, "El submuestreo reduce mucho el tamaño del entrenamiento"`  
  Comprobación: el conjunto se ha reducido a menos de un tercio.
- `assert recall_score(y_test, con_submuestreo.predict(X_test)) > recall_base, "El submuestreo debería subir el recall"`  
  Comprobación: el recall en test supera al del modelo base.
- `print(f"X_sub: {len(X_sub)} filas ({int(y_sub.sum())} positivas y {int((y_sub == 0).sum())} negativas) · recall con submuestreo: {recall_score(y_test, con_submuestreo.predict(X_test)):.0%}")`  
  Escribe el tamaño del conjunto, cuántas positivas y negativas tiene y el recall del modelo con submuestreo.
- `print("✔ Ejercicio 5 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Submuestreo = tirar datos:** rápido y sencillo, pero se pierde información. Útil cuando hay **muchísimos** datos.
- El submuestreo se hace **solo sobre train**: el test se queda tal cual, con su 6 % real, para evaluar con honestidad.
- `[1] * n` repite una lista `n` veces: una forma corta de crear etiquetas.

### ✏️ A9 · Ejercicio — Remedio 3: mover el umbral hasta un objetivo de recall

**Qué vamos a hacer y qué debe salir**

Tercer remedio, **sin tocar el modelo**: bajar el umbral. Imaginemos que negocio exige **detectar al menos el 70 %** de las cancelaciones. Con validación cruzada dentro de train (no con el test) buscamos **el umbral más alto que todavía alcanza un recall de 0,70**, y lo aplicamos al modelo base en test. **Debe salir** `Umbral 0.048: recall en test 82%, precisión 12%` y `✔ Ejercicio 6 correcto`. El umbral es muy bajo (0,048), porque el modelo da probabilidades pequeñas a casi todas las reservas. En test el recall (82 %) **supera** el objetivo del 70 %: normal, porque con solo 62 positivas hay mucha variación. Se apoya en `nuevo_modelo` (A1) y `proba_base` (A3).

```python
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)
proba_cv = cross_val_predict(nuevo_modelo(), X_train, y_train, cv=cv, method="predict_proba")[:, 1]
p_cv, r_cv, u_cv = precision_recall_curve(y_train, proba_cv)
umbral_70 = float(u_cv[r_cv[:-1] >= 0.70].max())
pred_70 = (proba_base >= umbral_70).astype(int)
recall_test_70 = recall_score(y_test, pred_70)
precision_test_70 = precision_score(y_test, pred_70)
assert 0 < umbral_70 < 0.5, "Para alcanzar recall 0,70 con clases raras el umbral debe ser bajo (< 0,5)"
assert recall_test_70 > 0.5, "En test el recall debería aproximarse al objetivo del 70 %"
print(f"Umbral {umbral_70:.3f}: recall en test {recall_test_70:.0%}, precisión {precision_test_70:.0%}")
print("✔ Ejercicio 6 correcto")
```

**Línea a línea**

- `cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)`  
  5 trozos que mantienen la proporción de cada clase.
- `proba_cv = cross_val_predict(nuevo_modelo(), X_train, y_train, cv=cv, method="predict_proba")[:, 1]`  
  Probabilidades de train obtenidas por validación cruzada: cada reserva se predice con un modelo que no la vio.
- `p_cv, r_cv, u_cv = precision_recall_curve(y_train, proba_cv)`  
  Curva PR de esas probabilidades: precisión, recall y umbrales.
- `umbral_70 = float(u_cv[r_cv[:-1] >= 0.70].max())`  
  Se queda con los umbrales cuyo recall sea ≥ 0,70 (`r_cv[:-1] >= 0.70`: el `[:-1]` quita el último recall, que no tiene umbral asociado) y elige el **mayor** de ellos (`.max()`), el más exigente que aún cumple el objetivo.
- `pred_70 = (proba_base >= umbral_70).astype(int)`  
  Convierte las probabilidades del modelo base en test en decisiones (1 si la probabilidad ≥ umbral).
- `recall_test_70 = recall_score(y_test, pred_70)`  
  Recall en test con ese umbral.
- `precision_test_70 = precision_score(y_test, pred_70)`  
  Precisión en test con ese umbral.
- `assert 0 < umbral_70 < 0.5, "Para alcanzar recall 0,70 con clases raras el umbral debe ser bajo (< 0,5)"`  
  Comprobación: el umbral es bajo (menor que 0,5).
- `assert recall_test_70 > 0.5, "En test el recall debería aproximarse al objetivo del 70 %"`  
  Comprobación: el recall en test supera el 50 %.
- `print(f"Umbral {umbral_70:.3f}: recall en test {recall_test_70:.0%}, precisión {precision_test_70:.0%}")`  
  Escribe el umbral (3 decimales), el recall y la precisión en test.
- `print("✔ Ejercicio 6 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **El umbral se elige en train (validación cruzada) y se comprueba en test:** igual que en S07.03.
- **El mismo modelo base** pasa de recall 3 % a 82 % solo cambiando el umbral: muchas veces **no hace falta reentrenar**.
- Con solo 62 positivas, el recall en test (82 %) no coincide con el objetivo (70 %): **las cifras de una clase rara son ruidosas**.
- `[:-1]` = «todos menos el último».

### 🎯 A10 · Mini-reto — Comparativa de los tres modelos

**Qué vamos a hacer y qué debe salir**

Mini-reto: juntar todo en **una tabla** para comparar los tres modelos (base, pesos, submuestreo) con cuatro métricas: AUC, AP, recall y precisión. **Debe salir** `✔ Mini-reto correcto` y esta tabla: **base** `0.774 / 0.242 / 0.032 / 0.667`; **pesos** `0.770 / 0.245 / 0.726 / 0.136`; **submuestreo** `0.752 / 0.241 / 0.452 / 0.172`. Lo importante: el **AUC y el AP casi no cambian** (los remedios no hacen al modelo «más listo», solo **cambian dónde se corta**); lo que cambia mucho es el recall y la precisión con el umbral 0,5. Se apoya en `base`, `con_pesos` y `con_submuestreo`.

```python
modelos = {"base": base, "pesos": con_pesos, "submuestreo": con_submuestreo}
filas = {}
for nombre, m in modelos.items():
    p = m.predict_proba(X_test)[:, 1]
    yhat = m.predict(X_test)
    filas[nombre] = {"AUC": roc_auc_score(y_test, p), "AP": average_precision_score(y_test, p),
                     "recall": recall_score(y_test, yhat), "precision": precision_score(y_test, yhat, zero_division=0)}
comparativa = pd.DataFrame(filas).T.round(3)
ganadora_ap = comparativa["AP"].idxmax()
comparativa
assert list(comparativa.index) == ["base", "pesos", "submuestreo"]
assert {"AUC", "AP", "recall", "precision"} <= set(comparativa.columns)
assert ganadora_ap in comparativa.index
display(comparativa)
print("✔ Mini-reto correcto")
```

**Línea a línea**

- `modelos = {"base": base, "pesos": con_pesos, "submuestreo": con_submuestreo}`  
  Diccionario con los tres modelos y su nombre.
- `filas = {}`  
  Diccionario vacío para los resultados.
- `for nombre, m in modelos.items():`  
  Para cada modelo (nombre y objeto):
- `p = m.predict_proba(X_test)[:, 1]`  
  Sus probabilidades en test.
- `yhat = m.predict(X_test)`  
  Sus decisiones en test (con el umbral 0,5).
- `filas[nombre] = {"AUC": roc_auc_score(y_test, p), "AP": average_precision_score(y_test, p),` … `"recall": recall_score(y_test, yhat), "precision": precision_score(y_test, yhat, zero_division=0)}` (2 líneas)  
  Guarda cuatro métricas: **AUC** y **AP** (con probabilidades: no dependen del umbral) y **recall** y **precisión** (con decisiones: dependen del 0,5). `zero_division=0` evita un error si el modelo no avisara de nada.
- `comparativa = pd.DataFrame(filas).T.round(3)`  
  Convierte el diccionario en tabla: `.T` traspone (un modelo por fila) y `.round(3)` redondea.
- `ganadora_ap = comparativa["AP"].idxmax()`  
  Nombre del modelo con el mejor AP (`idxmax`).
- `comparativa`  
  Línea suelta: no muestra nada (no es la última línea); la tabla se enseña con `display` más abajo.
- `assert list(comparativa.index) == ["base", "pesos", "submuestreo"]`  
  Comprobación: las filas son `base`, `pesos` y `submuestreo`, en ese orden.
- `assert {"AUC", "AP", "recall", "precision"} <= set(comparativa.columns)`  
  Comprobación: están las cuatro columnas.
- `assert ganadora_ap in comparativa.index`  
  Comprobación: la ganadora es una de las filas.
- `display(comparativa)`  
  Muestra la tabla.
- `print("✔ Mini-reto correcto")`  
  Aviso de que el mini-reto está bien.

**Lo destacable**

- **Los remedios no mejoran el AUC ni el AP:** las probabilidades vienen a ser igual de buenas. Lo que hacen es **mover el punto de trabajo** (recall frente a precisión).
- Con umbral 0,5 el modelo base acierta cuando avisa (precisión 0,67) pero casi nunca avisa (recall 0,03); con **pesos** avisa mucho (recall 0,73) y acierta poco (precisión 0,14).
- **Qué elegir lo decide el coste de cada error**, como en S07.03: si perder una cancelación es caro, interesa un recall alto.
- Un diccionario de diccionarios + `.T` es una forma cómoda de construir una tabla comparativa.
