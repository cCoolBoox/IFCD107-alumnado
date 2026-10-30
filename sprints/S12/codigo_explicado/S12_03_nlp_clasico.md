# Código explicado · S12.03 · NLP clásico: sentimiento y temas en las reseñas de TurisData

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_03_nlp_clasico.ipynb) · [descargar](../notebooks/S12_03_nlp_clasico.ipynb) · ⏱ en clase: 55 min · 🏫 10 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `filterwarnings`, `seed`, `update`, `read_csv` y más. |
| 2 | 1. Conocer los datos | Practica `to_string`, `round`, `sample`, `mean` y más (sección «1. Conocer los datos»). |
| 4 | 2. Limpieza y tokenización | Practica `apply`, `split` (sección «2. Limpieza y tokenización»). |
| 6 | 3. De texto a números: bolsa de palabra… | Practica `CountVectorizer`, `fit_transform`, `TfidfVectorizer`, `DataFrame` y más (secció… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `resenas` | `pd.read_csv(dato("resenas.csv"))` | 1 |
| `PALABRAS_VACIAS` | `{"a", "al", "con", "de", "del", "el", "en", "es", "esta",…` | 4 |
| `ejemplo` | `["el desayuno era escaso", "el desayuno merece la pena",…` | 6 |
| `bow` | `CountVectorizer()` | 6 |
| `M` | `bow.fit_transform(ejemplo)` | 6 |
| `tf` | `TfidfVectorizer()` | 6 |
| `M2` | `tf.fit_transform(ejemplo)` | 6 |
| `vocab` | `np.array(vec.get_feature_names_out())` | 10 |
| `pruebas` | `["La limpieza es impecable", "La limpieza no es impecable…` | 11 |
| `TEMAS` | `{ "limpieza": ["limpi", "sucia", "sucio", "pelos", "sában…` | 13 |
| `f1_por_tema` | `pd.Series({t: f1_tema(t) for t in TEMAS}).sort_values()` | 13 |
| `errores` | `resenas[resenas["temas_reales"].apply(lambda l: tema_peor…` | 15 |
| `RELLENO` | `PALABRAS_VACIAS \| {"pasamos", "semana", "aquí", "escapada…` | 16 |
| `neg` | `resenas.loc[resenas["sentimiento"] == "negativo", "texto"]` | 16 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `limpiar` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `tokenizar` | Función definida en el cuaderno. |
| `detectar_temas` | Función definida en el cuaderno. |
| `f1_tema` | Función definida en el cuaderno. |
| `sin_relleno` | Función definida en el cuaderno. |
| `top_ngramas` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `any` | Dice si ALGUNA condición es verdadera. | 13 |
| `apply` | Aplica una función a cada fila o a cada valor. | 4, 13, 15 |
| `argsort` | Devuelve las posiciones que ordenarían el array. | 10 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 10 |
| `asarray` | Convierte algo en array de NumPy sin copiarlo si ya lo es. | 16 |
| `barh` | Dibuja barras horizontales. | 10 |
| `classification_report` | Resumen de precisión, sensibilidad y F1 por clase. | 9 |
| `CountVectorizer` | Convierte textos en conteos de palabras (bolsa de palabras). | 6, 16 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 6 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `f1_score` | Calcula el F1: equilibrio entre precisión y sensibilidad. | 13 |
| `fillna` | Rellena los huecos con un valor. | 13 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 6, 16 |
| `from_predictions` | Dibuja la matriz de confusión a partir de las etiquetas reales y las predichas. | 9 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 6, 10, 16 |
| `grid` | Muestra la cuadrícula. | 9 |
| `head` | Muestra las primeras filas. | 1, 15, 16 |
| `index` | Devuelve la posición de un valor en una lista. | 10 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 13 |
| `iterrows` | Recorre la tabla fila a fila. | 15 |
| `join` | Une una lista de textos en uno solo con un separador. | 16 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2, 7, 15 |
| `list` | Crea una lista (o convierte algo en lista). | 10 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 16 |
| `mean` | Calcula la media. | 2 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 9, 11 |
| `print` | Muestra un valor por pantalla. | 1, 2, 4, 6, 7, 9… |
| `ravel` | Aplana un array a una sola dimensión. | 16 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `round` | Redondea un número a los decimales indicados. | 2, 6, 13 |
| `sample` | Elige varios elementos al azar sin repetir. | 2 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 13, 16 |
| `set_title` | Pone el título de un gráfico. | 9, 10 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 9, 10 |
| `set_ylabel` | Pone el nombre del eje vertical. | 9 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 1 |
| `show` | Muestra el gráfico. | 9, 10 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 13, 16 |
| `sorted` | Devuelve los elementos ordenados, sin cambiar el original. | 13 |
| `split` | Parte un texto en trozos por un separador. | 2, 4, 13, 16 |
| `str` | Da acceso a las operaciones de texto sobre una columna. | 2 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 9, 10 |
| `sum` | Suma todos los valores. | 16 |
| `TfidfVectorizer` | Convierte textos en números según la importancia de cada palabra (TF-IDF). | 6 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 10 |
| `to_string` | Convierte la tabla en texto para mostrarla entera. | 2, 13, 16 |
| `toarray` | Convierte una matriz dispersa en una matriz normal. | 6 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 7 |
| `update` | Añade o cambia varias claves de un diccionario. | 1 |
| `value_counts` | Cuenta cuántas veces aparece cada valor. | 2 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 10, 11 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `filterwarnings`, `seed`, `update`, `read_csv` y más.

```python
import re, unicodedata, warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay, f1_score

warnings.filterwarnings("ignore")
SEMILLA = 42
np.random.seed(SEMILLA)
plt.rcParams.update({"figure.figsize": (8, 3.5), "axes.grid": True, "axes.spines.top": False, "axes.spines.right": False})

resenas = pd.read_csv(dato("resenas.csv"))
print(resenas.shape)
resenas.head()
```

**Qué hace cada línea:**

- `import re, unicodedata, warnings` → Trae `re`, `unicodedata`, `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer` → Trae `CountVectorizer`, `TfidfVectorizer` de `sklearn.feature_extraction.text` para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.linear_model import LogisticRegression` → Trae `LogisticRegression` de `sklearn.linear_model` para poder usarlo.
- `from sklearn.naive_bayes import MultinomialNB` → Trae `MultinomialNB` de `sklearn.naive_bayes` para poder usarlo.
- `from sklearn.metrics import accuracy_score, classification_report, Confusio…` → Trae `accuracy_score`, `classification_report`, `ConfusionMatrixDisplay`, `f1_score` de `sklearn.metrics` para poder usarlo.
- … y 7 más con las mismas ideas.

### Celda 2 · 1. Conocer los datos · 🏫

**Qué hace:** Practica `to_string`, `round`, `sample`, `mean` y más (sección «1. Conocer los datos»).

```python
print(resenas["sentimiento"].value_counts(normalize=True).round(3).to_string())
resenas["longitud"] = resenas["texto"].str.split().str.len()
print("Palabras por reseña (media):", round(resenas["longitud"].mean(), 1))
for t in resenas.sample(3, random_state=SEMILLA)["texto"]:
    print("-", t)
```

**Qué hace cada línea:**

- `print(resenas["sentimiento"].value_counts(normalize=True).round(3).to_strin…` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `round`: redondea un número a los decimales indicados.
- `resenas["longitud"] = resenas["texto"].str.split().str.len()` → Guarda en `resenas["longitud"]` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `str`: da acceso a las operaciones de texto sobre una columna; `split`: parte un texto en trozos por un separador.
- `print("Palabras por reseña (media):", round(resenas["longitud"].mean(), 1))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.
- `for t in resenas.sample(3, random_state=SEMILLA)["texto"]:` → Repite el bloque de debajo para cada valor de `t` en `resenas.sample(3, random_state=SEMILLA)…`.

### Celda 3 · 2. Limpieza y tokenización · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Limpieza y tokenización · 🏫

**Qué hace:** Practica `apply`, `split` (sección «2. Limpieza y tokenización»).

```python
PALABRAS_VACIAS = {"a", "al", "con", "de", "del", "el", "en", "es", "esta", "estaba", "era", "fue", "la", "las", "lo", "los",
                   "me", "mi", "muy", "nos", "para", "por", "que", "se", "su", "un", "una", "y", "o", "u", "e"}

def tokenizar(texto, quitar_vacias=True):
    tokens = limpiar(texto).split()
    return [t for t in tokens if not (quitar_vacias and t in PALABRAS_VACIAS)]

print(tokenizar("La limpieza de la habitación era impecable!"))
resenas["limpio"] = resenas["texto"].apply(limpiar)
```

**Qué hace cada línea:**

- `PALABRAS_VACIAS = {"a", "al", "con", "de", "del", "el", "en", "es", "esta",…` → Guarda el valor en `PALABRAS_VACIAS`.
- `def tokenizar(texto, quitar_vacias=True):` → Define la función `tokenizar`: Función definida en el cuaderno.
- `print(tokenizar("La limpieza de la habitación era impecable!"))` → `print`: muestra un valor por pantalla; `tokenizar`: función definida en el cuaderno.
- `resenas["limpio"] = resenas["texto"].apply(limpiar)` → Guarda en `resenas["limpio"]` el resultado. `apply`: aplica una función a cada fila o a cada valor.

### Celda 5 · 2. Limpieza y tokenización · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. De texto a números: bolsa de palabras y TF-I… · 🏫

**Qué hace:** Practica `CountVectorizer`, `fit_transform`, `TfidfVectorizer`, `DataFrame` y más (sección «3. De texto a números: bolsa de palabra…»).

```python
ejemplo = ["el desayuno era escaso", "el desayuno merece la pena", "la habitación estaba sucia"]
bow = CountVectorizer()
M = bow.fit_transform(ejemplo)
print(pd.DataFrame(M.toarray(), columns=bow.get_feature_names_out(), index=["r1", "r2", "r3"]))
tf = TfidfVectorizer()
M2 = tf.fit_transform(ejemplo)
print(pd.DataFrame(M2.toarray().round(2), columns=tf.get_feature_names_out(), index=["r1", "r2", "r3"]))
```

**Qué hace cada línea:**

- `ejemplo = ["el desayuno era escaso", "el desayuno merece la pena", "la habi…` → Guarda el valor en `ejemplo`.
- `bow = CountVectorizer()` → Guarda en `bow` el resultado. `CountVectorizer`: convierte textos en conteos de palabras (bolsa de palabras).
- `M = bow.fit_transform(ejemplo)` → Guarda en `M` el resultado. `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `print(pd.DataFrame(M.toarray(), columns=bow.get_feature_names_out(), index=…` → `print`: muestra un valor por pantalla; `DataFrame`: crea una tabla de pandas (filas y columnas); `toarray`: convierte una matriz dispersa en una matriz normal.
- `tf = TfidfVectorizer()` → Guarda en `tf` el resultado. `TfidfVectorizer`: convierte textos en números según la importancia de cada palabra (TF-IDF).
- `M2 = tf.fit_transform(ejemplo)` → Guarda en `M2` el resultado. `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `print(pd.DataFrame(M2.toarray().round(2), columns=tf.get_feature_names_out(…` → `print`: muestra un valor por pantalla; `DataFrame`: crea una tabla de pandas (filas y columnas); `round`: redondea un número a los decimales indicados.

### Celda 7 · 4. Clasificar el sentimiento · 🏫

**Qué hace:** Practica `train_test_split` (sección «4. Clasificar el sentimiento»).

```python
from sklearn.pipeline import make_pipeline

X_ent, X_test, y_ent, y_test = train_test_split(resenas["texto"], resenas["sentimiento"], test_size=0.25,
                                                stratify=resenas["sentimiento"], random_state=SEMILLA)
print(len(X_ent), "para entrenar,", len(X_test), "para probar")
```

**Qué hace cada línea:**

- `from sklearn.pipeline import make_pipeline` → Trae `make_pipeline` de `sklearn.pipeline` para poder usarlo.
- `X_ent, X_test, y_ent, y_test = train_test_split(resenas["texto"], resenas["…` → Guarda en `X_ent, X_test, y_ent, y…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `print(len(X_ent), "para entrenar,", len(X_test), "para probar")` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.

### Celda 8 · 4. Clasificar el sentimiento · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4. Clasificar el sentimiento · 🏫

**Qué hace:** Practica `subplots`, `from_predictions`, `set_title`, `set_xlabel` y más (sección «4. Clasificar el sentimiento»).

```python
print(classification_report(y_test, modelo_lr.predict(X_test)))
fig, ax = plt.subplots(figsize=(4.5, 4))
ConfusionMatrixDisplay.from_predictions(y_test, modelo_lr.predict(X_test), ax=ax, cmap="Blues", colorbar=False)
ax.set_title("Matriz de confusión (regresión logística)"); ax.set_xlabel("Predicho"); ax.set_ylabel("Real"); ax.grid(False)
plt.show()
```

**Qué hace cada línea:**

- `print(classification_report(y_test, modelo_lr.predict(X_test)))` → `print`: muestra un valor por pantalla; `classification_report`: resumen de precisión, sensibilidad y F1 por clase; `predict`: pide al modelo ya entrenado que haga predicciones.
- `fig, ax = plt.subplots(figsize=(4.5, 4))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ConfusionMatrixDisplay.from_predictions(y_test, modelo_lr.predict(X_test),…` → `from_predictions`: dibuja la matriz de confusión a partir de las etiquetas reales y las predichas; `predict`: pide al modelo ya entrenado que haga predicciones.
- `ax.set_title("Matriz de confusión (regresión logística)"); ax.set_xlabel("P…` → `set_title`: pone el título de un gráfico.
- `ax.set_title("Matriz de confusión (regresión logística)"); ax.set_xlabel("P…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_title("Matriz de confusión (regresión logística)"); ax.set_xlabel("P…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_title("Matriz de confusión (regresión logística)"); ax.set_xlabel("P…` → `grid`: muestra la cuadrícula.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 10 · 4. Clasificar el sentimiento · 🏫

**Qué hace:** Practica `array`, `subplots`, `zip`, `tight_layout` y más (sección «¿Qué palabras pesan?»).

```python
vec, clf = modelo_lr.named_steps["tfidfvectorizer"], modelo_lr.named_steps["logisticregression"]
vocab = np.array(vec.get_feature_names_out())
fig, ejes = plt.subplots(1, 2, figsize=(11, 3.5))
for ax, clase, color in zip(ejes, ["positivo", "negativo"], ["#3b8f5a", "#c0463a"]):
    i = list(clf.classes_).index(clase)
    top = np.argsort(clf.coef_[i])[-8:]
    ax.barh(vocab[top], clf.coef_[i][top], color=color)
    ax.set_title(f"Palabras que más empujan a «{clase}»"); ax.set_xlabel("Peso en el modelo")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `vec, clf = modelo_lr.named_steps["tfidfvectorizer"], modelo_lr.named_steps[…` → Guarda el valor en `vec, clf`.
- `vocab = np.array(vec.get_feature_names_out())` → Guarda en `vocab` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez); `get_feature_names_out`: devuelve los nombres de las columnas después del preprocesado.
- `fig, ejes = plt.subplots(1, 2, figsize=(11, 3.5))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for ax, clase, color in zip(ejes, ["positivo", "negativo"], ["#3b8f5a", "#c…` → Repite el bloque de debajo para cada valor de `ax, clase, color` en `zip(ejes, ["positivo", "negativo"], ["#…`. Dentro del bloque: `index`: devuelve la posición de un valor en una lista; `list`: crea una lista (o convierte algo en lista); `argsort`: devuelve las posiciones que ordenarían el array.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 11 · 5. Los límites: negaciones · 🏫

**Qué hace:** Practica `zip`, `predict` (sección «5. Los límites: negaciones»).

```python
pruebas = ["La limpieza es impecable", "La limpieza no es impecable", "El personal fue borde", "El personal no fue borde",
           "Vistas increíbles pero un ruido constante"]
for f, p in zip(pruebas, modelo_lr.predict(pruebas)):
    print(f"{p:9s} ← {f}")
```

**Qué hace cada línea:**

- `pruebas = ["La limpieza es impecable", "La limpieza no es impecable", "El p…` → Guarda el valor en `pruebas`.
- `for f, p in zip(pruebas, modelo_lr.predict(pruebas)):` → Repite el bloque de debajo para cada valor de `f, p` en `zip(pruebas, modelo_lr.predict(pruebas))`.

### Celda 12 · 5. Los límites: negaciones · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 6. Temas por palabras clave · 🏫

**Qué hace:** Practica `apply`, `sort_values`, `sorted`, `f1_score` y más (sección «6. Temas por palabras clave»).

```python
TEMAS = {
    "limpieza":  ["limpi", "sucia", "sucio", "pelos", "sábanas", "toallas"],
    "ruido":     ["ruid", "silencio", "música", "dormir", "oye", "tranquilo"],
    "desayuno":  ["desayuno", "café", "buffet", "colas"],
    "personal":  ["personal", "recepción", "recepcionista", "trato", "borde", "atendía", "ayudó", "tardaron"],
    "ubicacion": ["ubicación", "situado", "lejos", "centro", "playa", "vistas", "coche", "zona"],
    "precio":    ["precio", "caro", "cuesta", "extras", "cobran", "compensa"],
}

def detectar_temas(texto, diccionario=TEMAS):
    t = limpiar(texto)
    return sorted(tema for tema, claves in diccionario.items() if any(c in t for c in claves))

resenas["temas_detectados"] = resenas["texto"].apply(detectar_temas)
resenas["temas_reales"] = resenas["temas"].fillna("").apply(lambda s: [x for x in s.split(",") if x])

def f1_tema(tema):
    real = resenas["temas_reales"].apply(lambda l: tema in l)
    pred = resenas["temas_detectados"].apply(lambda l: tema in l)
    return f1_score(real, pred)

f1_por_tema = pd.Series({t: f1_tema(t) for t in TEMAS}).sort_values()
print(f1_por_tema.round(2).to_string())
```

**Qué hace cada línea:**

- `TEMAS = {` → Guarda el valor en `TEMAS`.
- `def detectar_temas(texto, diccionario=TEMAS):` → Define la función `detectar_temas`: Función definida en el cuaderno.
- `resenas["temas_detectados"] = resenas["texto"].apply(detectar_temas)` → Guarda en `resenas["temas_detectad…` el resultado. `apply`: aplica una función a cada fila o a cada valor.
- `resenas["temas_reales"] = resenas["temas"].fillna("").apply(lambda s: [x fo…` → Guarda en `resenas["temas_reales"]` el resultado. `apply`: aplica una función a cada fila o a cada valor; `fillna`: rellena los huecos con un valor; `split`: parte un texto en trozos por un separador.
- `def f1_tema(tema):` → Define la función `f1_tema`: Función definida en el cuaderno.
- `f1_por_tema = pd.Series({t: f1_tema(t) for t in TEMAS}).sort_values()` → Guarda en `f1_por_tema` el resultado. `sort_values`: ordena la tabla por una o varias columnas; `Series`: crea una columna de pandas (una sola serie de valores); `f1_tema`: función definida en el cuaderno.
- `print(f1_por_tema.round(2).to_string())` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `round`: redondea un número a los decimales indicados.

### Celda 14 · 6. Temas por palabras clave · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 15 · 6. Temas por palabras clave · 🏫

**Qué hace:** Practica `iterrows`, `apply`, `head` (sección «6. Temas por palabras clave»).

```python
errores = resenas[resenas["temas_reales"].apply(lambda l: tema_peor in l) != resenas["temas_detectados"].apply(lambda l: tema_peor in l)]
print(f"{len(errores)} reseñas donde falla «{tema_peor}». Ejemplos:")
for _, fila in errores.head(5).iterrows():
    print("-", fila["texto"], "| real:", fila["temas_reales"], "| detectado:", fila["temas_detectados"])
```

**Qué hace cada línea:**

- `errores = resenas[resenas["temas_reales"].apply(lambda l: tema_peor in l) !…` → Guarda en `errores` el resultado. `apply`: aplica una función a cada fila o a cada valor.
- `print(f"{len(errores)} reseñas donde falla «{tema_peor}». Ejemplos:")` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `for _, fila in errores.head(5).iterrows():` → Repite el bloque de debajo para cada valor de `_, fila` en `errores.head(5).iterrows()`.

### Celda 16 · 7. n-gramas: expresiones que se repiten · 🏠

**Qué hace:** Palabras de "relleno" que abren muchas reseñas y no dicen nada de la estancia.

```python
# Palabras de "relleno" que abren muchas reseñas y no dicen nada de la estancia
RELLENO = PALABRAS_VACIAS | {"pasamos", "semana", "aquí", "escapada", "fin", "viajamos", "familia", "fuimos", "trabajo", "general", "todo"}

def sin_relleno(texto):
    return " ".join(t for t in limpiar(texto).split() if t not in RELLENO)

def top_ngramas(textos, n=(2, 3), k=8):
    cv = CountVectorizer(preprocessor=sin_relleno, ngram_range=n, min_df=5)
    M = cv.fit_transform(textos)
    frec = pd.Series(np.asarray(M.sum(axis=0)).ravel(), index=cv.get_feature_names_out())
    return frec.sort_values(ascending=False).head(k)

neg = resenas.loc[resenas["sentimiento"] == "negativo", "texto"]
print(top_ngramas(neg).to_string())
```

**Qué hace cada línea:**

- `RELLENO = PALABRAS_VACIAS | {"pasamos", "semana", "aquí", "escapada", "fin"…` → Guarda el valor en `RELLENO`.
- `def sin_relleno(texto):` → Define la función `sin_relleno`: Función definida en el cuaderno.
- `def top_ngramas(textos, n=(2, 3), k=8):` → Define la función `top_ngramas`: Función definida en el cuaderno.
- `neg = resenas.loc[resenas["sentimiento"] == "negativo", "texto"]` → Guarda en `neg` el resultado. `loc`: selecciona filas/columnas por su etiqueta o por una condición.
- `print(top_ngramas(neg).to_string())` → `print`: muestra un valor por pantalla; `to_string`: convierte la tabla en texto para mostrarla entera; `top_ngramas`: función definida en el cuaderno.

### Celda 17 · 8. Mini-reto integrador: panel de quejas · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S12_03_nlp_clasico.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
