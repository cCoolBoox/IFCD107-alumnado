# Código explicado · S12.04 · Embeddings: representar el significado con vectores (LSA)

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_04_embeddings_lsa.ipynb) · [descargar](../notebooks/S12_04_embeddings_lsa.ipynb) · ⏱ en clase: 50 min · 🏫 0 celdas de código en clase · 🏠 6 en casa
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
| `resenas` | `pd.read_csv(dato("resenas.csv"))` | 1 |
| `VACIAS` | `{"a", "al", "con", "de", "del", "el", "en", "es", "esta",…` | 1 |
| `tfidf` | `TfidfVectorizer(preprocessor=limpiar, min_df=2)` | 2 |
| `M` | `tfidf.fit_transform(resenas["texto"])` | 2 |
| `terminos` | `np.array(tfidf.get_feature_names_out())` | 4 |
| `Z2` | `TruncatedSVD(n_components=2, random_state=SEMILLA).fit_tr…` | 7 |
| `colores` | `{"positivo": "#3b8f5a", "neutro": "#999999", "negativo":…` | 7 |
| `USAR_SENTENCE_TRANSFORMERS` | `False` | 10 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `limpiar` | Función definida en el cuaderno. |
| `parecidas` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `buscar` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `argsort` | Devuelve las posiciones que ordenarían el array. | 4, 10 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 4, 5 |
| `cosine_similarity` | Mide cuánto se parecen dos vectores (1 = igual dirección). | 5 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `encode` | Convierte texto en bytes. | 10 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 2, 7 |
| `float` | Convierte un valor en número decimal. | 5 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 4 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 7 |
| `join` | Une una lista de textos en uno solo con un separador. | 1, 4 |
| `legend` | Muestra la leyenda del gráfico. | 7 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 10 |
| `lower` | Pasa el texto a minúsculas. | 1 |
| `print` | Muestra un valor por pantalla. | 2, 4, 5, 10 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 4 |
| `ravel` | Aplana un array a una sola dimensión. | 10 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `round` | Redondea un número a los decimales indicados. | 2, 5 |
| `scatter` | Dibuja un gráfico de puntos. | 7 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `SentenceTransformer` | Modelo que convierte frases en vectores (embeddings) que reflejan su significado. | 10 |
| `set_title` | Pone el título de un gráfico. | 7 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 7 |
| `set_ylabel` | Pone el nombre del eje vertical. | 7 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2 |
| `show` | Muestra el gráfico. | 7 |
| `split` | Parte un texto en trozos por un separador. | 1 |
| `sub` | Sustituye texto con una expresión regular. | 1 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 7 |
| `TfidfVectorizer` | Convierte textos en números según la importancia de cada palabra (TF-IDF). | 2 |
| `tolist` | Convierte un array o una columna en una lista de Python. | 10 |
| `TruncatedSVD` | Reduce dimensiones de matrices grandes (por ejemplo, de texto). | 7 |
| `update` | Añade o cambia varias claves de un diccionario. | 1 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏠

**Qué hace:** Palabras vacías y de "relleno" (frases que abren muchas reseñas sin decir nada de la estancia). No quitamos «no».

```python
import re, warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

warnings.filterwarnings("ignore")
SEMILLA = 42
np.random.seed(SEMILLA)
plt.rcParams.update({"figure.figsize": (8, 4.5), "axes.grid": True, "axes.spines.top": False, "axes.spines.right": False})

resenas = pd.read_csv(dato("resenas.csv"))

# Palabras vacías y de "relleno" (frases que abren muchas reseñas sin decir nada de la estancia). No quitamos «no».
VACIAS = {"a", "al", "con", "de", "del", "el", "en", "es", "esta", "estaba", "era", "fue", "la", "las", "lo", "los", "me", "mi",
          "muy", "nos", "para", "por", "que", "se", "su", "un", "una", "y", "o", "pasamos", "semana", "aquí", "escapada", "fin",
          "viajamos", "familia", "fuimos", "trabajo", "general", "todo", "estancia", "sin", "más"}

def limpiar(texto):
    palabras = re.sub(r"[^a-záéíóúüñ\s]", " ", texto.lower()).split()
    return " ".join(p for p in palabras if p not in VACIAS)
```

**Qué hace cada línea:**

- `import re, warnings` → Trae `re`, `warnings` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from sklearn.feature_extraction.text import TfidfVectorizer` → Trae `TfidfVectorizer` de `sklearn.feature_extraction.text` para poder usarlo.
- `from sklearn.decomposition import TruncatedSVD` → Trae `TruncatedSVD` de `sklearn.decomposition` para poder usarlo.
- `from sklearn.metrics.pairwise import cosine_similarity` → Trae `cosine_similarity` de `sklearn.metrics.pairwise` para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.linear_model import LogisticRegression` → Trae `LogisticRegression` de `sklearn.linear_model` para poder usarlo.
- … y 8 más con las mismas ideas.

### Celda 2 · 1. Idea: de la bolsa de palabras al vector denso · 🏠

**Qué hace:** Practica `TfidfVectorizer`, `fit_transform`, `shape`, `round` (sección «1. Idea: de la bolsa de palabras al vec…»).

```python
tfidf = TfidfVectorizer(preprocessor=limpiar, min_df=2)
M = tfidf.fit_transform(resenas["texto"])
print("TF-IDF:", M.shape, "→ proporción de ceros:", round(1 - M.nnz / (M.shape[0] * M.shape[1]), 3))
```

**Qué hace cada línea:**

- `tfidf = TfidfVectorizer(preprocessor=limpiar, min_df=2)` → Guarda en `tfidf` el resultado. `TfidfVectorizer`: convierte textos en números según la importancia de cada palabra (TF-IDF).
- `M = tfidf.fit_transform(resenas["texto"])` → Guarda en `M` el resultado. `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `print("TF-IDF:", M.shape, "→ proporción de ceros:", round(1 - M.nnz / (M.sh…` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas); `round`: redondea un número a los decimales indicados.

### Celda 3 · 1. Idea: de la bolsa de palabras al vector denso · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. ¿Qué "significa" cada eje? Palabras que van… · 🏠

**Qué hace:** Practica `array`, `get_feature_names_out`, `argsort`, `join` (sección «2. ¿Qué "significa" cada eje? Palabras…»).

```python
terminos = np.array(tfidf.get_feature_names_out())
for i in range(5):
    peso = lsa.components_[i]
    arriba = terminos[np.argsort(peso)[-6:][::-1]]
    print(f"Eje {i + 1}: {', '.join(arriba)}")
```

**Qué hace cada línea:**

- `terminos = np.array(tfidf.get_feature_names_out())` → Guarda en `terminos` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez); `get_feature_names_out`: devuelve los nombres de las columnas después del preprocesado.
- `for i in range(5):` → Repite el bloque de debajo para cada valor de `i` en `range(5)`. Dentro del bloque: `argsort`: devuelve las posiciones que ordenarían el array; `join`: une una lista de textos en uno solo con un separador.

### Celda 5 · 3. Similitud del coseno · 🏠

**Qué hace:** Practica `array`, `round`, `cosine_similarity` (sección «3. Similitud del coseno»).

```python
a, b, c = np.array([1, 0]), np.array([1, 1]), np.array([0, 1])
print("coseno(a, b) =", round(float(cosine_similarity([a], [b])[0, 0]), 3), "(45°)")
print("coseno(a, c) =", round(float(cosine_similarity([a], [c])[0, 0]), 3), "(90°, nada en común)")
```

**Qué hace cada línea:**

- `a, b, c = np.array([1, 0]), np.array([1, 1]), np.array([0, 1])` → Guarda en `a, b, c` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `print("coseno(a, b) =", round(float(cosine_similarity([a], [b])[0, 0]), 3),…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `float`: convierte un valor en número decimal.
- `print("coseno(a, c) =", round(float(cosine_similarity([a], [c])[0, 0]), 3),…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `float`: convierte un valor en número decimal.

### Celda 6 · 3. Similitud del coseno · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4. Mapa de reseñas en 2 dimensiones · 🏠

**Qué hace:** Practica `fit_transform`, `subplots`, `items`, `set_title` y más (sección «4. Mapa de reseñas en 2 dimensiones»).

```python
Z2 = TruncatedSVD(n_components=2, random_state=SEMILLA).fit_transform(M)
colores = {"positivo": "#3b8f5a", "neutro": "#999999", "negativo": "#c0463a"}
fig, ax = plt.subplots()
for s, col in colores.items():
    m = (resenas["sentimiento"] == s).values
    ax.scatter(Z2[m, 0], Z2[m, 1], s=12, alpha=.5, c=col, label=s)
ax.set_title("Reseñas en 2 dimensiones (LSA)"); ax.set_xlabel("Eje 1"); ax.set_ylabel("Eje 2"); ax.legend()
plt.show()
```

**Qué hace cada línea:**

- `Z2 = TruncatedSVD(n_components=2, random_state=SEMILLA).fit_transform(M)` → Guarda en `Z2` el resultado. `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez; `TruncatedSVD`: reduce dimensiones de matrices grandes (por ejemplo, de texto).
- `colores = {"positivo": "#3b8f5a", "neutro": "#999999", "negativo": "#c0463a…` → Guarda el valor en `colores`.
- `fig, ax = plt.subplots()` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for s, col in colores.items():` → Repite el bloque de debajo para cada valor de `s, col` en `colores.items()`. Dentro del bloque: `values`: devuelve los valores de un diccionario o de una tabla; `scatter`: dibuja un gráfico de puntos.
- `ax.set_title("Reseñas en 2 dimensiones (LSA)"); ax.set_xlabel("Eje 1"); ax.…` → `set_title`: pone el título de un gráfico.
- `ax.set_title("Reseñas en 2 dimensiones (LSA)"); ax.set_xlabel("Eje 1"); ax.…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_title("Reseñas en 2 dimensiones (LSA)"); ax.set_xlabel("Eje 1"); ax.…` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_title("Reseñas en 2 dimensiones (LSA)"); ax.set_xlabel("Eje 1"); ax.…` → `legend`: muestra la leyenda del gráfico.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 8 · 5. Embeddings como entrada de un clasificador · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 6. Mini-reto integrador: buscador semántico de… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 7. OPCIONAL · Embeddings neuronales con `senten… · 🏠

**Qué hace:** NO VERIFICADO: requiere internet.

```python
USAR_SENTENCE_TRANSFORMERS = False   # ← cámbialo a True solo si tienes internet (Colab)

if USAR_SENTENCE_TRANSFORMERS:
    # NO VERIFICADO: requiere internet
# %pip install -q sentence-transformers
    from sentence_transformers import SentenceTransformer
    modelo_st = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    E = modelo_st.encode(resenas["texto"].tolist(), show_progress_bar=False, normalize_embeddings=True)
    q = modelo_st.encode(["no me dejó dormir el ruido"], normalize_embeddings=True)
    mejores = np.argsort((E @ q.T).ravel())[::-1][:3]
    for i in mejores:
        print("-", resenas.loc[i, "texto"])
else:
    print("Parte opcional omitida (USAR_SENTENCE_TRANSFORMERS = False).")
```

**Qué hace cada línea:**

- `USAR_SENTENCE_TRANSFORMERS = False # ← cámbialo a True solo si tienes inter…` → Guarda el valor en `USAR_SENTENCE_TRANSFORM…`.
- `if USAR_SENTENCE_TRANSFORMERS:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `SentenceTransformer`: modelo que convierte frases en vectores (embeddings) que reflejan su significado; `encode`: convierte texto en bytes; `tolist`: convierte un array o una columna en una lista de Python.

---
*Generado a partir de `laboratorios/fuentes/S12_04_embeddings_lsa.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
