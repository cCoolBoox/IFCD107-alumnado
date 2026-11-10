# Código explicado · S07.03 · Regresión logística: predecir cancelaciones

> **Para qué sirve.** Aquí está **todo el código del cuaderno explicado por escrito**, celda a celda y en el mismo orden. Cada bloque sigue siempre el mismo guion: **primero** un párrafo que dice qué vamos a hacer, por qué y qué debe salir; **después** el código, con **cada línea explicada**; y **al final** lo destacable del bloque (lo que conviene recordar y con qué se relaciona).
>
> **Cuaderno:** [🏫 en clase](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_03_regresion_logistica_en_clase.ipynb) · [🏠 completo](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_03_regresion_logistica.ipynb)
>
> **Cómo usarlo:** ejecuta la celda en el cuaderno; busca aquí la del mismo número (A3, A5…); lee el párrafo, sigue el código línea a línea y, al terminar, cambia algo (un número, una columna) y comprueba si pasa lo que esperabas: es la mejor manera de entender código.

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda** («coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`»). Lo que va tras `#` es un comentario: Python lo ignora. Los ejercicios (✏️) llevan aquí la **solución de referencia**: úsala **después** de intentarlo.

## La idea del cuaderno

TurisData quiere saber **qué reservas se van a cancelar** para actuar antes (confirmar, pedir depósito, reasignar la habitación). Ahora no se predice un número sino una **categoría** (cancela / se mantiene): es un problema de **clasificación**, y empezamos por el modelo más usado y más fácil de explicar: la **regresión logística**.

- **Hilo del cuaderno:** vemos la función sigmoide, que convierte una suma en probabilidad (A2) → entrenamos el modelo y obtenemos una probabilidad por reserva (A3) → leemos qué variables aumentan el riesgo con los *odds ratio* (A4, A5) → comprobamos cómo cambia el resultado al mover el **umbral** de decisión (A6, A7) → elegimos el umbral con un **coste de negocio** (A8, A9, A10) → lo resumimos en una recomendación (A11).
- **Lo que te llevas:** el modelo no devuelve «sí/no» sino una **probabilidad**; el **umbral** (0,5 por defecto) lo decide el negocio, no el modelo; bajarlo detecta más cancelaciones a cambio de más falsas alarmas; y cada error cuesta distinto (una habitación vacía suele costar más que una llamada de más).

## Mapa de celdas

| Celda | Tipo | Qué hacemos | ¿Dónde? |
|---|---|---|---|
| A1 | ⚙️ Preparación | Preparar las herramientas y los datos | 🏫 |
| A2 | 👀 Ejemplo | La función sigmoide | 🏫 |
| A3 | ✏️ Ejercicio | Entrenar el modelo y obtener probabilidades | 🏫 |
| A4 | 👀 Ejemplo | Odds ratio: qué variables aumentan el riesgo | 🏫 |
| A5 | ✏️ Ejercicio | Leer dos odds ratio | 🏫 |
| A6 | 👀 Ejemplo | Matrices de confusión con dos umbrales | 🏫 |
| A7 | ✏️ Ejercicio | Cuánto sube el recall y cuánto baja la precisión | 🏫 |
| A8 | 👀 Ejemplo | Preparar el coste de cada error | 🏠 |
| A9 | ✏️ Ejercicio | Elegir el umbral que cuesta menos | 🏠 |
| A10 | 👀 Ejemplo | Curva de coste según el umbral | 🏠 |
| A11 | 🎯 Mini-reto | Tabla de umbrales y recomendación | 🏠 |

🏫 = en clase · 🏠 = en casa. 👀 ejemplo: solo se ejecuta y se mira. ✏️ ejercicio: se completa con tu código. ⚙️ preparación: se ejecuta sola.

## Celda a celda

### ⚙️ A1 · Preparación — Preparar las herramientas y los datos

**Qué vamos a hacer y qué debe salir**

Celda de preparación: se ejecuta **la primera** y no hace falta entenderla para empezar. Trae las librerías, carga las **6000 reservas** y define qué columnas se usan para **predecir** (`X`) y qué columna se quiere **predecir** (`y` = `cancelada`: 1 si se canceló, 0 si no). Después **reparte los datos**: 4800 reservas para entrenar y 1200 para evaluar, manteniendo la misma proporción de cancelaciones en ambas. **Debe salir** `Tasa de cancelación: 45.9 % · train 4800 · test 1200` (en el cuaderno se ve `45.9%`) y `Listo ✔`. Es la base de todo lo que sigue.

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
- `import numpy as np`  
  Trae **NumPy** (`np`): operaciones con números.
- `import pandas as pd`  
  Trae **pandas** (`pd`): las tablas de datos.
- `import matplotlib.pyplot as plt`  
  Trae **matplotlib** (`plt`): gráficos.
- `import seaborn as sns`  
  Trae **seaborn** (`sns`): gráficos más cuidados.
- `from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedKFold`  
  Trae `train_test_split` (reparte los datos), `cross_val_predict` (predicciones por validación cruzada) y `StratifiedKFold` (trozos que respetan la proporción de cada clase).
- `from sklearn.linear_model import LogisticRegression`  
  Trae `LogisticRegression`, el modelo de regresión logística.
- `from sklearn.impute import SimpleImputer`  
  Trae `SimpleImputer`: rellena huecos (valores que faltan).
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder`  
  Trae `StandardScaler` (escala números) y `OneHotEncoder` (texto → columnas 0/1).
- `from sklearn.compose import ColumnTransformer`  
  Trae `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas.
- `from sklearn.pipeline import Pipeline`  
  Trae `Pipeline`: encadena pasos en un solo objeto.
- `from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score`  
  Trae las herramientas para evaluar un clasificador: la matriz de confusión (`confusion_matrix`, `ConfusionMatrixDisplay`) y las métricas `precision_score`, `recall_score` y `accuracy_score`.
- `SEMILLA = 42`  
  Número fijo (`42`) para que los sorteos salgan siempre igual.
- `sns.set_theme(style="whitegrid")`  
  Estilo visual de los gráficos.
- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])`  
  Lee las reservas en `df`; `parse_dates` marca las dos columnas de fecha.
- `df["mes_llegada"] = df["fecha_llegada"].dt.month`  
  Crea `mes_llegada` (1 a 12) a partir de la fecha de llegada.
- `df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)`  
  Crea `temporada_alta` (1 si el mes es 1, 2, 3, 7, 8 o 12; 0 si no).
- `columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",` … `"peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]` (2 líneas)  
  Lista de las **9 columnas numéricas** que usará el modelo (incluye el precio por noche y la temporada).
- `columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]`  
  Lista de las **6 columnas de texto** (habitación, régimen, canal, país, tarifa, depósito).
- `X, y = df[columnas_num + columnas_cat], df["cancelada"]`  
  `X` = las variables con las que se predice; `y` = lo que se quiere predecir: la columna `cancelada`.
- `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)`  
  Reparte los datos: 80 % para entrenar y 20 % (`test_size=0.2`) para evaluar. **`stratify=y`** mantiene en train y test la **misma proporción de cancelaciones** (aprox. 46 %).
- `print(f"Tasa de cancelación: {y.mean():.1%} · train {len(X_train)} · test {len(X_test)}")`  
  Escribe la tasa de cancelación de todo el conjunto (`y.mean()` es la media de ceros y unos = proporción de unos; `:.1%` la da en porcentaje) y el tamaño de cada parte.
- `print("Listo ✔")`  
  Mensaje de que todo ha ido bien.

**Lo destacable**

- La celda de preparación **se ejecuta siempre la primera**, y otra vez si Colab se reinicia: todas las demás celdas usan lo que crea aquí (`df`, `SEMILLA`, las librerías…). Si ves `NameError: name '…' is not defined`, casi siempre es que falta ejecutarla.
- **`stratify=y`**: con clases desiguales conviene que train y test tengan la misma proporción; si no, la evaluación podría salir sesgada.
- Casi la mitad de las reservas se cancela (**45,9 %**): un problema con clases **bastante equilibradas** (en S07.04 verás el caso contrario).
- La media de una columna de ceros y unos **es** la proporción de unos.

### 👀 A2 · Ejemplo — La función sigmoide

**Qué vamos a hacer y qué debe salir**

La regresión logística empieza como una regresión lineal: calcula una **suma ponderada** `z` de las variables. Pero `z` puede valer cualquier número (−50, 3, 200…) y nosotros queremos una **probabilidad** entre 0 y 1. La función **sigmoide**, `1 / (1 + e⁻ᶻ)`, hace esa conversión: los valores muy negativos dan casi 0, los muy positivos casi 1, y `z = 0` da exactamente 0,5. **Debe salir** una curva en forma de «S» que cruza la línea discontinua en 0,5 cuando `z` vale 0. No depende de los datos: es solo la idea matemática.

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

**Línea a línea**

- `z = np.linspace(-6, 6, 200)`  
  200 valores de `z` repartidos de −6 a 6: el eje horizontal.
- `plt.figure(figsize=(6, 3.5))`  
  Crea la figura de 6 × 3,5 pulgadas.
- `plt.plot(z, 1 / (1 + np.exp(-z)), color="#2a6f97", lw=2)`  
  Dibuja la sigmoide: para cada `z`, calcula `1 / (1 + e^(−z))` (`np.exp` es la exponencial). `color` y `lw` (grosor) son estética.
- `plt.axhline(0.5, color="gray", ls="--")`  
  Línea horizontal discontinua (`ls="--"`) a altura 0,5: el **umbral habitual** de decisión.
- `plt.title("Función sigmoide: convierte cualquier número en una probabilidad")`  
  Título del gráfico.
- `plt.xlabel("Suma ponderada z")`  
  Nombre del eje horizontal.
- `plt.ylabel("Probabilidad")`  
  Nombre del eje vertical.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **La sigmoide convierte cualquier número en una probabilidad** (siempre entre 0 y 1): esa es la diferencia clave con la regresión lineal.
- `z = 0` ↔ probabilidad 0,5: ahí está la frontera entre «cancela» y «no cancela» si el umbral es 0,5.
- Cuanto más lejos de 0 está `z`, **más segura** es la predicción.

### ✏️ A3 · Ejercicio — Entrenar el modelo y obtener probabilidades

**Qué vamos a hacer y qué debe salir**

Montamos y entrenamos la regresión logística. Antes hay que **preparar los datos** igual que en las prácticas anteriores, con una novedad: rellenamos los huecos (`SimpleImputer`) y convertimos los textos en columnas 0/1. Todo se mete en un `Pipeline` (preprocesado + modelo) para que lo que se aprende **solo con train** se aplique igual a test. Después pedimos al modelo **probabilidades**, no etiquetas: `predict_proba` devuelve dos columnas (probabilidad de «no cancela» y de «cancela») y nos quedamos con la segunda. **Debe salir** `1200 probabilidades, de 0.03 a 0.99 · media = 0.466` y `✔ Ejercicio 1 correcto`. Fíjate: la media de las probabilidades (0,466) casi coincide con la tasa real de cancelación (0,459), buena señal. Se apoya en `X_train`, `y_train` y `X_test` de A1.

```python
prep = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore", drop="if_binary"))]), columnas_cat),
])
logit = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))]).fit(X_train, y_train)
proba_test = logit.predict_proba(X_test)[:, 1]
assert proba_test.shape == (len(X_test),), "Debe haber una probabilidad por reserva de test"
assert 0 <= proba_test.min() and proba_test.max() <= 1, "Son probabilidades: entre 0 y 1"
assert 0.35 < proba_test.mean() < 0.55, "La probabilidad media debería rondar la tasa de cancelación (≈0,46)"
print(f"{len(proba_test)} probabilidades, de {proba_test.min():.2f} a {proba_test.max():.2f} · media = {proba_test.mean():.3f}")
print("✔ Ejercicio 1 correcto")
```

**Línea a línea**

- `prep = ColumnTransformer([` … `])` (5 líneas)  
  Define el preprocesado en dos ramas. **Numéricas:** huecos rellenos con la **mediana** (`SimpleImputer`) y luego escalado (`StandardScaler`). **Texto:** huecos con el valor **más frecuente** y conversión a columnas 0/1 (`OneHotEncoder`; `handle_unknown="ignore"` tolera categorías nuevas; `drop="if_binary"` deja **una sola columna** cuando solo hay dos valores, como en `deposito` o `tarifa`).
- `logit = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))]).fit(X_train, y_train)`  
  Une el preprocesado y el modelo (`LogisticRegression`; `max_iter=1000` da margen de iteraciones para converger) y lo entrena con train (`.fit`).
- `proba_test = logit.predict_proba(X_test)[:, 1]`  
  `predict_proba` da, por reserva, dos columnas: P(no cancela) y P(cancela). `[:, 1]` se queda con **todas las filas de la segunda columna**: la probabilidad de cancelar.
- `assert proba_test.shape == (len(X_test),), "Debe haber una probabilidad por reserva de test"` … `assert 0.35 < proba_test.mean() < 0.55, "La probabilidad media debería rondar la tasa de cancelación (≈0,46)"` (3 líneas)  
  Tres comprobaciones: hay **una probabilidad por reserva** de test, todas están **entre 0 y 1**, y su media ronda la tasa real de cancelación (entre 0,35 y 0,55).
- `print(f"{len(proba_test)} probabilidades, de {proba_test.min():.2f} a {proba_test.max():.2f} · media = {proba_test.mean():.3f}")`  
  Escribe cuántas probabilidades hay, el mínimo y el máximo (2 decimales) y la media (3 decimales).
- `print("✔ Ejercicio 1 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **`predict_proba` devuelve probabilidades, `predict` solo la etiqueta final.** Quedarse con las probabilidades da libertad para elegir el umbral después.
- `[:, 1]` = «todas las filas, la columna 1»: la probabilidad de la clase positiva (cancela).
- El `Pipeline` evita la **fuga de datos**: la mediana, la media y las categorías se aprenden solo con train.
- Una probabilidad media (0,466) cercana a la tasa real (0,459) indica que el modelo está **razonablemente calibrado** en conjunto.

### 👀 A4 · Ejemplo — Odds ratio: qué variables aumentan el riesgo

**Qué vamos a hacer y qué debe salir**

¿Qué hace que una reserva sea más o menos arriesgada? El modelo guarda un **coeficiente** por variable, pero están en una escala poco intuitiva (logaritmo de *odds*). Al aplicarles la exponencial se convierten en **odds ratio**: cuántas veces se multiplican los *odds* de cancelar cuando la variable sube una unidad. Si vale **más de 1**, aumenta el riesgo; si **menos de 1**, lo reduce; **1** = no influye. **Debe salir** un gráfico de barras horizontales: en rojo las variables que aumentan el riesgo (arriba: `antelacion_dias` ≈ 2,12, `deposito_sin_deposito` ≈ 2,01, `canal_web_intermediaria` ≈ 1,70) y en azul las que lo reducen (abajo: `tarifa_no_reembolsable` ≈ 0,44, `deposito_total` ≈ 0,46). Se apoya en el modelo `logit` de A3.

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

**Línea a línea**

- `nombres = logit[:-1].get_feature_names_out()`  
  `logit[:-1]` son **todos los pasos menos el último** (el preprocesado); `.get_feature_names_out()` da el nombre de cada columna resultante (con prefijo `num__` o `cat__`).
- `coefs = pd.Series(logit[-1].coef_[0], index=nombres)`  
  Une los coeficientes del modelo (`logit[-1].coef_[0]`: el último paso, la regresión, y su primera fila) con sus nombres.
- `odds = np.exp(coefs).sort_values(ascending=False)`  
  `np.exp(coefs)` los convierte en *odds ratio*; `sort_values(ascending=False)` los ordena de mayor a menor.
- `plt.figure(figsize=(7, 6))`  
  Crea la figura de 7 × 6 pulgadas.
- `odds.iloc[::-1].plot(kind="barh", color=["#e63946" if v > 1 else "#2a6f97" for v in odds.iloc[::-1]])`  
  Dibuja barras horizontales (`kind="barh"`). `iloc[::-1]` **da la vuelta** a la serie para que la mayor quede arriba. El color es una lista: **rojo** si el odds ratio es mayor que 1 y **azul** si no.
- `plt.axvline(1, color="black", lw=1)`  
  Línea vertical negra en 1: la frontera entre «aumenta» y «reduce» el riesgo.
- `plt.title("Odds ratio de cada variable (rojo = más riesgo de cancelar)")`  
  Título del gráfico (con la leyenda de colores).
- `plt.xlabel("Odds ratio")`  
  Nombre del eje horizontal.
- `plt.ylabel("")`  
  Quita el nombre del eje vertical (cadena vacía): ya lo dice cada barra.
- `plt.tight_layout()`  
  Ajusta los márgenes para que quepan los nombres largos.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **Odds ratio > 1 aumenta el riesgo; < 1 lo reduce.** Es la forma más clara de explicar un modelo logístico a negocio.
- Las variables numéricas están **escaladas**: 2,12 significa «por cada desviación típica más de antelación, los *odds* de cancelar se multiplican por 2,12».
- Los *odds* no son probabilidades: **×2** en odds no es «el doble de probabilidad». Sirven para **comparar** variables, no para predecir un porcentaje exacto.
- Tarifa no reembolsable y depósito total **reducen** la cancelación: tiene sentido, porque cancelar sale caro.

### ✏️ A5 · Ejercicio — Leer dos odds ratio

**Qué vamos a hacer y qué debe salir**

Pasamos de mirar el gráfico a **extraer cifras concretas** y escribirlas en una frase. Cogemos el odds ratio de dos variables de negocio (tarifa no reembolsable y depósito total) y buscamos cuál es la variable que **más** aumenta el riesgo. **Debe salir** `Tarifa no reembolsable: los odds de cancelar se multiplican por 0.44`, `Depósito total: … por 0.46` y `✔ Ejercicio 2 correcto`. Es decir, esas tarifas **reducen más de la mitad** los odds de cancelar. Se apoya en `odds` de A4.

```python
or_no_reembolsable = odds["cat__tarifa_no_reembolsable"]
or_deposito_total = odds["cat__deposito_total"]
mas_riesgo = odds.idxmax()
assert or_no_reembolsable < 1, "La tarifa no reembolsable reduce el riesgo de cancelar (odds ratio < 1)"
assert or_deposito_total < 1, "Un depósito total reduce el riesgo de cancelar (odds ratio < 1)"
assert isinstance(mas_riesgo, str) and odds[mas_riesgo] > 1
print(f"Tarifa no reembolsable: los odds de cancelar se multiplican por {or_no_reembolsable:.2f}")
print(f"Depósito total: los odds de cancelar se multiplican por {or_deposito_total:.2f}")
print("✔ Ejercicio 2 correcto")
```

**Línea a línea**

- `or_no_reembolsable = odds["cat__tarifa_no_reembolsable"]`  
  Busca en la serie `odds` el valor de la variable `cat__tarifa_no_reembolsable`.
- `or_deposito_total = odds["cat__deposito_total"]`  
  Lo mismo con `cat__deposito_total`.
- `mas_riesgo = odds.idxmax()`  
  `idxmax()` devuelve el **nombre** de la variable con el odds ratio más alto (la que más aumenta el riesgo).
- `assert or_no_reembolsable < 1, "La tarifa no reembolsable reduce el riesgo de cancelar (odds ratio < 1)"` … `assert isinstance(mas_riesgo, str) and odds[mas_riesgo] > 1` (3 líneas)  
  Tres comprobaciones: los dos odds ratio son menores que 1 (reducen el riesgo) y `mas_riesgo` es un nombre (texto) cuyo odds ratio es mayor que 1.
- `print(f"Tarifa no reembolsable: los odds de cancelar se multiplican por {or_no_reembolsable:.2f}")`  
  Escribe el odds ratio de la tarifa no reembolsable con 2 decimales.
- `print(f"Depósito total: los odds de cancelar se multiplican por {or_deposito_total:.2f}")`  
  Escribe el odds ratio del depósito total.
- `print("✔ Ejercicio 2 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **`serie["nombre"]`** busca un valor por su etiqueta; **`idxmax()`** devuelve la **etiqueta** del máximo (`max()` devolvería el valor).
- Un odds ratio de 0,44 se lee: «los odds de cancelar son un 56 % menores» (1 − 0,44).
- Interpretar bien un odds ratio es más importante que calcularlo: es lo que se cuenta al cliente.

### 👀 A6 · Ejemplo — Matrices de confusión con dos umbrales

**Qué vamos a hacer y qué debe salir**

El modelo da una probabilidad, pero para actuar hay que decidir un **umbral**: «si la probabilidad es ≥ umbral, avisamos de que cancelará». Por defecto es 0,5, pero no es sagrado. Aquí definimos una función que, dado un umbral, calcula la **matriz de confusión** (aciertos y errores de cada tipo) y las métricas **precisión** y **recall**, y dibujamos las matrices con 0,5 y con 0,3. **Debe salir** dos matrices lado a lado. Con **0,5**: VN 472 · FP 177 · FN 212 · VP 339. Con **0,3**: VN 262 · FP 387 · FN 69 · VP 482. Al bajar el umbral **detectamos más cancelaciones** (los falsos negativos bajan de 212 a 69) pero **molestamos a más clientes** (los falsos positivos suben de 177 a 387). Se apoya en `proba_test` de A3.

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

**Línea a línea**

- `def metricas_umbral(y_real, proba, umbral):`  
  Define una función que, con las respuestas reales, las probabilidades y un umbral, devuelve las métricas.
- `"""Matriz de confusión y métricas para un umbral dado."""`  
  Descripción de la función.
- `pred = (proba >= umbral).astype(int)`  
  Convierte probabilidades en decisiones: `proba >= umbral` da verdadero/falso y `.astype(int)` lo pasa a 1/0 (1 = «cancelará»).
- `vn, fp, fn, vp = confusion_matrix(y_real, pred).ravel()`  
  `confusion_matrix` cuenta los cuatro casos; `.ravel()` los aplana en una lista de 4 números que se reparten en cuatro variables: **VN** (no cancela y se acierta), **FP** (falsa alarma), **FN** (cancelación no detectada) y **VP** (cancelación detectada).
- `return {"umbral": umbral, "VN": vn, "FP": fp, "FN": fn, "VP": vp,` … `"recall": vp / (vp + fn)}` (3 líneas)  
  Devuelve un diccionario con el umbral, los cuatro recuentos y las dos métricas: **precisión** = VP / (VP + FP) («de los que avisé, cuántos cancelaron») y **recall** = VP / (VP + FN) («de los que cancelaron, cuántos detecté»). Si no se avisó a nadie (`vp + fp = 0`), la precisión es `np.nan` («no definido») en lugar de fallar con una división por cero.
- `fig, ejes = plt.subplots(1, 2, figsize=(10, 4))`  
  Crea la figura con **dos gráficos** lado a lado.
- `for ax, u in zip(ejes, [0.5, 0.3]):`  
  Recorre dos parejas (gráfico, umbral): el primero con 0,5 y el segundo con 0,3.
- `ConfusionMatrixDisplay.from_predictions(y_test, (proba_test >= u).astype(int), ax=ax,` … `display_labels=["Se mantiene", "Cancela"], cmap="Blues", colorbar=False)` (2 líneas)  
  Dibuja la matriz de confusión: compara lo real (`y_test`) con las decisiones tomadas con ese umbral. `display_labels` pone nombres a las dos clases, `cmap="Blues"` elige los colores y `colorbar=False` quita la barra lateral.
- `ax.set_title(f"Umbral {u}")`  
  Título de cada gráfico con su umbral.
- `ax.set_xlabel("Predicho")`  
  Nombre del eje horizontal: lo **predicho**.
- `ax.set_ylabel("Real")`  
  Nombre del eje vertical: lo **real**.
- `plt.tight_layout()`  
  Ajusta los márgenes.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **El umbral es una decisión, no una propiedad del modelo.** El mismo modelo con dos umbrales da dos comportamientos distintos.
- **Bajar el umbral:** más cancelaciones detectadas (sube el recall), más falsas alarmas (baja la precisión). **Subirlo:** al revés.
- Las cuatro casillas: **VN, FP, FN, VP**. Conviene saber de memoria cuál es cada una.
- `metricas_umbral` es una función **reutilizable**: la usarás en A7, A8 y A11 sin repetir código.

### ✏️ A7 · Ejercicio — Cuánto sube el recall y cuánto baja la precisión

**Qué vamos a hacer y qué debe salir**

Ponemos cifras a lo que se vio en las matrices: calculamos las métricas con los umbrales 0,5 y 0,3 y restamos para ver **cuánto se gana y cuánto se pierde**. **Debe salir** `Con umbral 0,3 detectas 26 puntos más de las cancelaciones, pero tu precisión baja 10 puntos.` y `✔ Ejercicio 3 correcto`. Detrás: el recall pasa de 0,615 a 0,875 y la precisión de 0,657 a 0,555. Se apoya en `metricas_umbral` (A6) y `proba_test` (A3).

```python
m05 = metricas_umbral(y_test, proba_test, 0.5)
m03 = metricas_umbral(y_test, proba_test, 0.3)
sube_recall = m03["recall"] - m05["recall"]
baja_precision = m05["precision"] - m03["precision"]
assert m05["VN"] + m05["FP"] + m05["FN"] + m05["VP"] == len(y_test), "La matriz debe sumar todas las reservas de test"
assert sube_recall > 0, "Bajar el umbral debe subir el recall"
assert baja_precision > 0, "Bajar el umbral suele bajar la precisión"
print(f"Con umbral 0,3 detectas {sube_recall*100:.0f} puntos más de las cancelaciones, pero tu precisión baja {baja_precision*100:.0f} puntos.")
print("✔ Ejercicio 3 correcto")
```

**Línea a línea**

- `m05 = metricas_umbral(y_test, proba_test, 0.5)`  
  Métricas con el umbral 0,5 (un diccionario con VN, FP, FN, VP, precisión y recall).
- `m03 = metricas_umbral(y_test, proba_test, 0.3)`  
  Métricas con el umbral 0,3.
- `sube_recall = m03["recall"] - m05["recall"]`  
  Diferencia de recall: 0,3 menos 0,5 (positiva si detectamos más).
- `baja_precision = m05["precision"] - m03["precision"]`  
  Diferencia de precisión: 0,5 menos 0,3 (positiva si perdemos precisión).
- `assert m05["VN"] + m05["FP"] + m05["FN"] + m05["VP"] == len(y_test), "La matriz debe sumar todas las reservas de test"` … `assert baja_precision > 0, "Bajar el umbral suele bajar la precisión"` (3 líneas)  
  Tres comprobaciones: las cuatro casillas suman **todas** las reservas de test; bajar el umbral **sube** el recall; y **baja** la precisión.
- `print(f"Con umbral 0,3 detectas {sube_recall*100:.0f} puntos más de las cancelaciones, pero tu precisión baja {baja_precision*100:.0f} puntos.")`  
  Escribe las dos diferencias en **puntos porcentuales** (multiplicadas por 100, sin decimales).
- `print("✔ Ejercicio 3 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **No hay umbral gratis:** lo que ganas en recall lo pagas en precisión.
- Que las cuatro casillas sumen el total es una buena **comprobación de cordura** de cualquier matriz de confusión.
- Un diccionario (`m05["recall"]`) permite guardar varios resultados juntos y sacarlos por nombre.

### 👀 A8 · Ejemplo — Preparar el coste de cada error

**Qué vamos a hacer y qué debe salir**

Falta una pieza: **¿qué umbral es el mejor?** Depende de lo que **cueste cada error**. Un falso negativo (cancelación que no detectamos) deja una habitación vacía; un falso positivo (falsa alarma) cuesta una llamada o un correo. Aquí ponemos que el primero cuesta **3 veces** más que el segundo (son **supuestos de negocio**, no datos del modelo). Además, el umbral **no se debe elegir mirando el test** (sería hacer trampa), así que se obtienen **probabilidades con validación cruzada dentro de train** (`proba_cv`): cada reserva se predice con un modelo que **no la vio**. **Debe salir** `Probabilidades de validación cruzada: (4800,) · coste FN: 3.0 · coste FP: 1.0`. Se apoya en `logit` (A3) y `metricas_umbral` (A6).

```python
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)
proba_cv = cross_val_predict(logit, X_train, y_train, cv=cv, method="predict_proba")[:, 1]

# Lo que cuesta, en unidades relativas, cada error. Son decisiones de negocio: no tienen valor por defecto.
COSTE_FN, COSTE_FP = 3.0, 1.0   # FN = cancelación que no detectamos · FP = falsa alarma

def coste_total(y_real, proba, umbral, coste_fn, coste_fp):
    m = metricas_umbral(y_real, proba, umbral)
    return m["FN"] * coste_fn + m["FP"] * coste_fp
print("Probabilidades de validación cruzada:", proba_cv.shape, "· coste FN:", COSTE_FN, "· coste FP:", COSTE_FP)
```

**Línea a línea**

- `cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)`  
  Define 5 trozos que mantienen la proporción de cada clase; `shuffle=True` mezcla antes de trocear y `random_state` fija el resultado.
- `proba_cv = cross_val_predict(logit, X_train, y_train, cv=cv, method="predict_proba")[:, 1]`  
  Para cada reserva de train, entrena el modelo con los otros 4 trozos y le pide la probabilidad de cancelar (`method="predict_proba"`); `[:, 1]` se queda con la de «cancela». Resultado: una probabilidad **honesta** por cada una de las 4800 reservas.
- `# Lo que cuesta, en unidades relativas, cada error. Son decisiones de negocio: no tienen valor por defecto.`  
  Comentario: los costes son **decisiones de negocio**, no tienen valor por defecto.
- `COSTE_FN, COSTE_FP = 3.0, 1.0   # FN = cancelación que no detectamos · FP = falsa alarma`  
  Asigna los costes (en unidades relativas): perder una cancelación vale **3**, una falsa alarma vale **1**. Las mayúsculas indican que son **constantes** que se pueden cambiar.
- `def coste_total(y_real, proba, umbral, coste_fn, coste_fp):`  
  Define una función que calcula el **coste total** de usar un umbral.
- `m = metricas_umbral(y_real, proba, umbral)`  
  Reutiliza la función de A6 para obtener los recuentos con ese umbral.
- `return m["FN"] * coste_fn + m["FP"] * coste_fp`  
  Coste total = número de FN × su coste + número de FP × su coste.
- `print("Probabilidades de validación cruzada:", proba_cv.shape, "· coste FN:", COSTE_FN, "· coste FP:", COSTE_FP)`  
  Escribe la forma de `proba_cv` (4800 probabilidades) y los dos costes.

**Lo destacable**

- **Elegir el umbral con el test sería hacer trampa:** se elige con validación cruzada dentro de train y el test se usa **una sola vez** al final.
- **Los costes son una decisión de negocio:** con otros valores (por ejemplo 1 y 1) el mejor umbral sería otro. Preguntarlo al cliente es parte del trabajo.
- `cross_val_predict` da una predicción **fuera de muestra** para cada fila de train.

### ✏️ A9 · Ejercicio — Elegir el umbral que cuesta menos

**Qué vamos a hacer y qué debe salir**

Ahora sí: probamos **19 umbrales** (de 0,05 a 0,95 de 0,05 en 0,05), calculamos el coste total de cada uno con las probabilidades de validación cruzada y nos quedamos con el **más barato**. Después comprobamos esa elección **una sola vez** en test y la comparamos con el 0,5 por defecto. **Debe salir** `Umbral elegido: 0.25 · coste en test: 577 (con 0,5: 813)` y `✔ Ejercicio 4 correcto`. Un umbral bajo es lo esperable: como perder una cancelación cuesta el triple, compensa avisar de más. El ahorro: **813 → 577** (un 29 % menos). Se apoya en A6 y A8.

```python
umbrales = np.arange(0.05, 0.96, 0.05)
costes = [coste_total(y_train, proba_cv, u, COSTE_FN, COSTE_FP) for u in umbrales]
mejor_umbral = float(umbrales[int(np.argmin(costes))])
coste_test = coste_total(y_test, proba_test, mejor_umbral, COSTE_FN, COSTE_FP)
assert 0.1 <= mejor_umbral <= 0.4, "Con FN 3 veces más caro que FP, el umbral óptimo debería ser bajo (≈0,25)"
assert coste_test < coste_total(y_test, proba_test, 0.5, COSTE_FN, COSTE_FP), "El umbral elegido debería costar menos que el 0,5 por defecto"
print(f"Umbral elegido: {mejor_umbral:.2f} · coste en test: {coste_test:.0f} (con 0,5: {coste_total(y_test, proba_test, 0.5, COSTE_FN, COSTE_FP):.0f})")
print("✔ Ejercicio 4 correcto")
```

**Línea a línea**

- `umbrales = np.arange(0.05, 0.96, 0.05)`  
  Los umbrales a probar: de 0,05 a 0,95 en pasos de 0,05 (`np.arange` no incluye el final, por eso el límite es 0,96).
- `costes = [coste_total(y_train, proba_cv, u, COSTE_FN, COSTE_FP) for u in umbrales]`  
  Para cada umbral calcula el coste total sobre **train con validación cruzada** (lista por comprensión).
- `mejor_umbral = float(umbrales[int(np.argmin(costes))])`  
  `np.argmin(costes)` da la **posición** del coste más bajo y `umbrales[...]` el umbral de esa posición; `float(...)` lo convierte en número normal.
- `coste_test = coste_total(y_test, proba_test, mejor_umbral, COSTE_FN, COSTE_FP)`  
  Coste que tendría ese umbral en el test: la comprobación final, una sola vez.
- `assert 0.1 <= mejor_umbral <= 0.4, "Con FN 3 veces más caro que FP, el umbral óptimo debería ser bajo (≈0,25)"` … `assert coste_test < coste_total(y_test, proba_test, 0.5, COSTE_FN, COSTE_FP), "El umbral elegido debería costar menos que el 0,5 por defecto"` (2 líneas)  
  Dos comprobaciones: el umbral óptimo es bajo (entre 0,1 y 0,4) y cuesta menos que el 0,5 por defecto en test.
- `print(f"Umbral elegido: {mejor_umbral:.2f} · coste en test: {coste_test:.0f} (con 0,5: {coste_total(y_test, proba_test, 0.5, COSTE_FN, COSTE_FP):.0f})")`  
  Escribe el umbral elegido, su coste en test y el coste con 0,5 para comparar.
- `print("✔ Ejercicio 4 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **`argmin` da la posición; `min` da el valor.** Para saber *qué umbral* es el mejor se usa la posición.
- Se **elige en train** (validación cruzada) y se **comprueba en test**: el test confirma, no decide.
- El resultado depende de los costes de A8: si los errores costaran igual, el umbral óptimo estaría cerca de 0,5.

### 👀 A10 · Ejemplo — Curva de coste según el umbral

**Qué vamos a hacer y qué debe salir**

Dibujamos el coste de cada umbral para **ver** por qué el mejor es el que es. **Debe salir** una curva en forma de «U» con puntos en cada umbral probado y una línea roja discontinua en el mínimo (0,25). A la izquierda (umbrales muy bajos) el coste sube porque se avisa de casi todo y hay demasiadas falsas alarmas; a la derecha, porque se dejan escapar demasiadas cancelaciones, que cuestan el triple. Se apoya en `umbrales`, `costes` y `mejor_umbral` de A9.

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

**Línea a línea**

- `plt.figure(figsize=(7, 3.8))`  
  Crea la figura de 7 × 3,8 pulgadas.
- `plt.plot(umbrales, costes, marker="o", color="#2a6f97")`  
  Dibuja el coste (vertical) frente al umbral (horizontal); `marker="o"` pone un punto en cada valor probado.
- `plt.axvline(mejor_umbral, color="#e63946", ls="--", label=f"Mínimo: {mejor_umbral:.2f}")`  
  Línea vertical roja discontinua en el mejor umbral; `label` es el texto que saldrá en la leyenda.
- `plt.title("Coste total según el umbral (FN cuesta 3 veces más que FP)")`  
  Título del gráfico.
- `plt.xlabel("Umbral de decisión")`  
  Nombre del eje horizontal.
- `plt.ylabel("Coste (unidades relativas)")`  
  Nombre del eje vertical.
- `plt.legend()`  
  Muestra la leyenda con el texto del mínimo.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **Forma de «U»:** tanto avisar de todo como avisar de nada salen caros; el óptimo está en el fondo.
- El mínimo queda **a la izquierda del 0,5** porque los falsos negativos pesan más.
- Un gráfico así es el mejor argumento para explicar al negocio **por qué no se usa 0,5**.

### 🎯 A11 · Mini-reto — Tabla de umbrales y recomendación

**Qué vamos a hacer y qué debe salir**

Mini-reto: resumir todo en una **tabla de decisión** para negocio. Comparamos tres umbrales (el 0,5 por defecto, el 0,3 «intuitivo» y el óptimo de A9) con cuatro columnas: umbral, recall, precisión y coste en test; y escribimos la **recomendación** en una frase con una cifra. **Debe salir** la tabla `0.50 → .615 / .657 / 813`, `0.30 → .875 / .555 / 594`, `0.25 → .920 / .533 / 577`, la frase `Recomiendo el umbral 0.25: detecta el 92% de las cancelaciones …` y `✔ Mini-reto correcto`. Se apoya en A3, A6, A8 y A9.

```python
filas = []
for u in [0.5, 0.3, mejor_umbral]:
    m = metricas_umbral(y_test, proba_test, u)
    filas.append({"umbral": round(u, 2), "recall": round(m["recall"], 3),
                  "precision": round(m["precision"], 3), "coste": coste_total(y_test, proba_test, u, COSTE_FN, COSTE_FP)})
tabla_umbrales = pd.DataFrame(filas)
recomendacion = (f"Recomiendo el umbral {mejor_umbral:.2f}: detecta el {tabla_umbrales.iloc[2]['recall']:.0%} de las "
                 "cancelaciones a cambio de más falsas alarmas, porque una habitación vacía cuesta más que una alerta innecesaria.")
tabla_umbrales
assert tabla_umbrales.shape[0] == 3, "Debe haber tres filas"
assert {"umbral", "recall", "precision", "coste"} <= set(tabla_umbrales.columns)
assert isinstance(recomendacion, str) and any(c.isdigit() for c in recomendacion), "La recomendación debe ser texto con al menos una cifra"
display(tabla_umbrales)
print(recomendacion)
print("✔ Mini-reto correcto")
```

**Línea a línea**

- `filas = []`  
  Lista vacía donde se irán guardando las filas de la tabla.
- `for u in [0.5, 0.3, mejor_umbral]:`  
  Para cada uno de los tres umbrales:
- `m = metricas_umbral(y_test, proba_test, u)`  
  Calcula sus métricas **en test** (función de A6).
- `filas.append({"umbral": round(u, 2), "recall": round(m["recall"], 3),` … `"precision": round(m["precision"], 3), "coste": coste_total(y_test, proba_test, u, COSTE_FN, COSTE_FP)})` (2 líneas)  
  Añade una fila (un diccionario) con el umbral, el recall y la precisión redondeados a 3 decimales, y el coste total en test.
- `tabla_umbrales = pd.DataFrame(filas)`  
  Convierte la lista de filas en una tabla de pandas.
- `recomendacion = (f"Recomiendo el umbral {mejor_umbral:.2f}: detecta el {tabla_umbrales.iloc[2]['recall']:.0%} de las "` … `"cancelaciones a cambio de más falsas alarmas, porque una habitación vacía cuesta más que una alerta innecesaria.")` (2 líneas)  
  Construye la frase de recomendación con una **f-string**: inserta el umbral elegido y el recall de la **tercera fila** (`iloc[2]`, porque se empieza a contar en 0) en porcentaje sin decimales (`:.0%`). Los dos trozos de texto entre paréntesis se unen en una sola cadena.
- `tabla_umbrales`  
  Línea suelta con el nombre de la tabla: aquí no muestra nada (no es la última línea de la celda); la tabla se muestra con `display` más abajo.
- `assert tabla_umbrales.shape[0] == 3, "Debe haber tres filas"` … `assert isinstance(recomendacion, str) and any(c.isdigit() for c in recomendacion), "La recomendación debe ser texto con al menos una cifra"` (3 líneas)  
  Tres comprobaciones: la tabla tiene **3 filas**, incluye las columnas `umbral`, `recall`, `precision` y `coste`, y la recomendación es **texto con al menos una cifra**.
- `display(tabla_umbrales)`  
  Muestra la tabla.
- `print(recomendacion)`  
  Escribe la frase de recomendación.
- `print("✔ Mini-reto correcto")`  
  Aviso de que el mini-reto está bien.

**Lo destacable**

- **Una tabla de 3 filas resume la decisión:** el umbral 0,25 detecta el 92 % de las cancelaciones y reduce el coste de 813 a 577.
- **La recomendación debe poder leerla alguien sin conocimientos técnicos:** una frase, una cifra y una razón de negocio.
- El modelo no decide: **recomienda**; la decisión final (cuánto cuesta cada error) es del negocio.
- `iloc[2]` = «la fila en la posición 2»: en programación se empieza a contar en 0.
