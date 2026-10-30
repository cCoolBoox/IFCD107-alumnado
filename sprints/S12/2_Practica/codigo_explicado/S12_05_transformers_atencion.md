# Código explicado · S12.05 · Transformers y LLM: tokenización y atención paso a paso

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/S12_05_transformers_atencion.ipynb) · [descargar](../S12_05_transformers_atencion.ipynb) · ⏱ en clase: 40 min · 🏫 7 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `filterwarnings`, `seed`, `set_printoptions`, `update`. |
| 2 | 1. Tokenización: cómo "lee" un LLM | Practica `Counter`, `zip` (sección «1. Tokenización: cómo "lee" un LLM»). |
| 4 | 1. Tokenización: cómo "lee" un LLM | Practica `zip`, `list`, `append`, `most_common` (sección «1. Tokenización: cómo "lee" un… |
| 6 | 2. Autoatención paso a paso (con número… | Embeddings inventados (una fila por palabra, 4 dimensiones). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `corpus` | `["desayuno", "desayunos", "desayunar", "limpio", "limpiez…` | 2 |
| `palabras` | `["hotel", "muy", "limpio"]` | 6 |
| `X` | `np.array([[1., 0., 1., 0.], [0., 2., 0., 2.], [1., 1., 0.…` | 6 |
| `Wq` | `np.array([[1., 0.], [0., 1.], [1., 0.], [0., 1.]])` | 6 |
| `Wk` | `np.array([[1., 0.], [0., 1.], [0., 1.], [1., 0.]])` | 6 |
| `Wv` | `np.array([[1., 2.], [0., 1.], [1., 0.], [0., 1.]])` | 6 |
| `puntuaciones` | `Q @ K.T` | 7 |
| `d` | `K.shape[1]` | 9 |
| `pesos` | `softmax(puntuaciones / np.sqrt(d))` | 9 |
| `im` | `ax.imshow(pesos, cmap="Blues", vmin=0, vmax=1)` | 11 |
| `siguiente` | `["limpio", "ruidoso", "caro", "cerca", "agradable"]` | 13 |
| `logits` | `np.array([[3.0, 1.0, 0.5, 2.0, 2.5]])` | 13 |
| `USAR_HUGGING_FACE` | `False` | 16 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `contar_pares` | palabras: lista de listas de símbolos. Devuelve un Counter con la frecuencia de cada par de símbolos consecutivos. |
| `entrenar_bpe` | Aplica n_fusiones: en cada paso fusiona el par más frecuente en un solo símbolo. |
| `softmax` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `atencion` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `atencion_causal` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `append` | Añade un elemento al final de una lista. | 4 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 6, 13 |
| `bar` | Dibuja barras verticales. | 13 |
| `clasificador` | El clasificador de opiniones ya cargado (transformers). | 16 |
| `Counter` | Cuenta cuántas veces aparece cada elemento. | 2 |
| `filterwarnings` | Silencia avisos que no aportan nada en el cuaderno. | 1 |
| `imshow` | Muestra una imagen o una matriz como imagen. | 11 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 4 |
| `list` | Crea una lista (o convierte algo en lista). | 4 |
| `most_common` | Devuelve los elementos más frecuentes de un contador. | 4 |
| `pipeline` | Atajo de la librería transformers para cargar un modelo ya entrenado y usarlo. | 16 |
| `print` | Muestra un valor por pantalla. | 4, 6, 7, 9, 16 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 4, 11 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `set_printoptions` | Cambia cómo NumPy muestra los números por pantalla. | 1 |
| `set_title` | Pone el título de un gráfico. | 11, 13 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 11 |
| `set_xticklabels` | Pone texto en las marcas del eje horizontal. | 11 |
| `set_xticks` | Fija las marcas del eje horizontal. | 11 |
| `set_ylabel` | Pone el nombre del eje vertical. | 11, 13 |
| `set_yticklabels` | Pone texto en las marcas del eje vertical. | 11 |
| `set_yticks` | Fija las marcas del eje vertical. | 11 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 9 |
| `show` | Muestra el gráfico. | 11, 13 |
| `sqrt` | Raíz cuadrada. | 9 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 11, 13 |
| `text` | Escribe un texto en una posición del gráfico. | 11 |
| `tick_params` | Ajusta el aspecto de las marcas de los ejes. | 13 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 11, 13 |
| `update` | Añade o cambia varias claves de un diccionario. | 1 |
| `zero` | Clasificador «de cero ejemplos»: asigna etiquetas que no ha visto al entrenar. | 16 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 2, 4, 13 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `filterwarnings`, `seed`, `set_printoptions`, `update`.

```python
import re, warnings
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
SEMILLA = 42
np.random.seed(SEMILLA)
np.set_printoptions(precision=2, suppress=True)
plt.rcParams.update({"figure.figsize": (7, 4), "axes.spines.top": False, "axes.spines.right": False})
```

**Qué hace cada línea:**

- `import re, warnings` → Trae `re`, `warnings` para poder usarlo.
- `from collections import Counter` → Trae `Counter` de `collections` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `warnings.filterwarnings("ignore")` → `filterwarnings`: silencia avisos que no aportan nada en el cuaderno.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `np.random.seed(SEMILLA)` → `seed`: fija la semilla del azar para que salga siempre lo mismo.
- `np.set_printoptions(precision=2, suppress=True)` → `set_printoptions`: cambia cómo NumPy muestra los números por pantalla.
- `plt.rcParams.update({"figure.figsize": (7, 4), "axes.spines.top": False, "a…` → `update`: añade o cambia varias claves de un diccionario.

### Celda 2 · 1. Tokenización: cómo "lee" un LLM · 🏫

**Qué hace:** Practica `Counter`, `zip` (sección «1. Tokenización: cómo "lee" un LLM»).

```python
corpus = ["desayuno", "desayunos", "desayunar", "limpio", "limpieza", "limpiar", "limpiamos", "desayunamos"]

def contar_pares(palabras):
    """palabras: lista de listas de símbolos. Devuelve un Counter con la frecuencia de cada par de símbolos consecutivos."""
    pares = Counter()
    for simbolos in palabras:
        for par in zip(simbolos, simbolos[1:]):
            pares[par] += 1
    return pares
```

**Qué hace cada línea:**

- `corpus = ["desayuno", "desayunos", "desayunar", "limpio", "limpieza", "limp…` → Guarda el valor en `corpus`.
- `def contar_pares(palabras):` → Define la función `contar_pares`: palabras: lista de listas de símbolos. Devuelve un Counter con la frecuencia de cada par de símbolos consecutivos.

### Celda 3 · 1. Tokenización: cómo "lee" un LLM · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1. Tokenización: cómo "lee" un LLM · 🏫

**Qué hace:** Practica `zip`, `list`, `append`, `most_common` (sección «1. Tokenización: cómo "lee" un LLM»).

```python
def entrenar_bpe(palabras, n_fusiones):
    """Aplica n_fusiones: en cada paso fusiona el par más frecuente en un solo símbolo."""
    palabras = [list(p) for p in palabras]
    fusiones = []
    for _ in range(n_fusiones):
        pares = contar_pares(palabras)
        if not pares:
            break
        a, b = pares.most_common(1)[0][0]
        fusiones.append((a, b))
        nuevas = []
        for simbolos in palabras:
            i, salida = 0, []
            while i < len(simbolos):
                if i < len(simbolos) - 1 and simbolos[i] == a and simbolos[i + 1] == b:
                    salida.append(a + b); i += 2
                else:
                    salida.append(simbolos[i]); i += 1
            nuevas.append(salida)
        palabras = nuevas
    return fusiones, palabras

fusiones, tokens = entrenar_bpe(corpus, 12)
print("Fusiones aprendidas:", fusiones)
for p, t in zip(corpus, tokens):
    print(f"{p:12s} → {t}")
```

**Qué hace cada línea:**

- `def entrenar_bpe(palabras, n_fusiones):` → Define la función `entrenar_bpe`: Aplica n_fusiones: en cada paso fusiona el par más frecuente en un solo símbolo.
- `fusiones, tokens = entrenar_bpe(corpus, 12)` → Guarda en `fusiones, tokens` el resultado. `entrenar_bpe`: aplica n_fusiones: en cada paso fusiona el par más frecuente en un solo símbolo.
- `print("Fusiones aprendidas:", fusiones)` → `print`: muestra un valor por pantalla.
- `for p, t in zip(corpus, tokens):` → Repite el bloque de debajo para cada valor de `p, t` en `zip(corpus, tokens)`.

### Celda 5 · 1. Tokenización: cómo "lee" un LLM · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 2. Autoatención paso a paso (con números pequeñ… · 🏫

**Qué hace:** Embeddings inventados (una fila por palabra, 4 dimensiones).

```python
palabras = ["hotel", "muy", "limpio"]
# Embeddings inventados (una fila por palabra, 4 dimensiones)
X = np.array([[1., 0., 1., 0.],
              [0., 2., 0., 2.],
              [1., 1., 0., 1.]])

# Matrices de proyección (4 → 2). En un modelo real se APRENDEN durante el entrenamiento.
Wq = np.array([[1., 0.], [0., 1.], [1., 0.], [0., 1.]])
Wk = np.array([[1., 0.], [0., 1.], [0., 1.], [1., 0.]])
Wv = np.array([[1., 2.], [0., 1.], [1., 0.], [0., 1.]])

Q, K, V = X @ Wq, X @ Wk, X @ Wv
print("Q =\n", Q, "\nK =\n", K, "\nV =\n", V)
```

**Qué hace cada línea:**

- `palabras = ["hotel", "muy", "limpio"]` → Guarda el valor en `palabras`.
- `X = np.array([[1., 0., 1., 0.],` → Guarda en `X` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `Wq = np.array([[1., 0.], [0., 1.], [1., 0.], [0., 1.]])` → Guarda en `Wq` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `Wk = np.array([[1., 0.], [0., 1.], [0., 1.], [1., 0.]])` → Guarda en `Wk` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `Wv = np.array([[1., 2.], [0., 1.], [1., 0.], [0., 1.]])` → Guarda en `Wv` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `Q, K, V = X @ Wq, X @ Wk, X @ Wv` → Guarda el valor en `Q, K, V`.
- `print("Q =\n", Q, "\nK =\n", K, "\nV =\n", V)` → `print`: muestra un valor por pantalla.

### Celda 7 · 2. Autoatención paso a paso (con números pequeñ… · 🏫

**Qué hace:** Crea `puntuaciones`.

```python
puntuaciones = Q @ K.T
print(puntuaciones)
```

**Qué hace cada línea:**

- `puntuaciones = Q @ K.T` → Guarda el valor en `puntuaciones`.
- `print(puntuaciones)` → `print`: muestra un valor por pantalla.

### Celda 8 · 2. Autoatención paso a paso (con números pequeñ… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 2. Autoatención paso a paso (con números pequeñ… · 🏫

**Qué hace:** Practica `softmax`, `shape`, `sqrt` (sección «2. Autoatención paso a paso (con número…»).

```python
d = K.shape[1]
pesos = softmax(puntuaciones / np.sqrt(d))
print("Pesos de atención (cada fila suma 1):\n", pesos)
```

**Qué hace cada línea:**

- `d = K.shape[1]` → Guarda en `d` el resultado. `shape`: tamaño de la tabla: (filas, columnas).
- `pesos = softmax(puntuaciones / np.sqrt(d))` → Guarda en `pesos` el resultado. `softmax`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*; `sqrt`: raíz cuadrada.
- `print("Pesos de atención (cada fila suma 1):\n", pesos)` → `print`: muestra un valor por pantalla.

### Celda 10 · 2. Autoatención paso a paso (con números pequeñ… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 2. Autoatención paso a paso (con números pequeñ… · 🏫

**Qué hace:** Practica `subplots`, `imshow`, `set_xticks`, `set_xticklabels` y más (sección «2. Autoatención paso a paso (con número…»).

```python
fig, ax = plt.subplots(figsize=(4.5, 4))
im = ax.imshow(pesos, cmap="Blues", vmin=0, vmax=1)
ax.set_xticks(range(3)); ax.set_xticklabels(palabras); ax.set_yticks(range(3)); ax.set_yticklabels(palabras)
for i in range(3):
    for j in range(3):
        ax.text(j, i, f"{pesos[i, j]:.2f}", ha="center", va="center", color="black" if pesos[i, j] < .6 else "white")
ax.set_xlabel("Mira a…"); ax.set_ylabel("Palabra que pregunta"); ax.set_title("Pesos de atención")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(figsize=(4.5, 4))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `im = ax.imshow(pesos, cmap="Blues", vmin=0, vmax=1)` → Guarda en `im` el resultado. `imshow`: muestra una imagen o una matriz como imagen.
- `ax.set_xticks(range(3)); ax.set_xticklabels(palabras); ax.set_yticks(range(…` → `set_xticks`: fija las marcas del eje horizontal; `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `ax.set_xticks(range(3)); ax.set_xticklabels(palabras); ax.set_yticks(range(…` → `set_xticklabels`: pone texto en las marcas del eje horizontal.
- `ax.set_xticks(range(3)); ax.set_xticklabels(palabras); ax.set_yticks(range(…` → `set_yticks`: fija las marcas del eje vertical; `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `ax.set_xticks(range(3)); ax.set_xticklabels(palabras); ax.set_yticks(range(…` → `set_yticklabels`: pone texto en las marcas del eje vertical.
- `for i in range(3):` → Repite el bloque de debajo para cada valor de `i` en `range(3)`. Dentro del bloque: `text`: escribe un texto en una posición del gráfico.
- `ax.set_xlabel("Mira a…"); ax.set_ylabel("Palabra que pregunta"); ax.set_tit…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_xlabel("Mira a…"); ax.set_ylabel("Palabra que pregunta"); ax.set_tit…` → `set_ylabel`: pone el nombre del eje vertical.
- … y 3 más con las mismas ideas.

### Celda 12 · 3. Máscara causal: mirar solo hacia atrás · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 4. Del cálculo a la generación: logits, softmax… · 🏠

**Qué hace:** Practica `array`, `subplots`, `zip`, `set_ylabel` y más (sección «4. Del cálculo a la generación: logits,…»).

```python
siguiente = ["limpio", "ruidoso", "caro", "cerca", "agradable"]
logits = np.array([[3.0, 1.0, 0.5, 2.0, 2.5]])
fig, ejes = plt.subplots(1, 3, figsize=(11, 3), sharey=True)
for ax, T in zip(ejes, [0.3, 1.0, 2.5]):
    p = softmax(logits / T)[0]
    ax.bar(siguiente, p, color="#3b7ea1"); ax.set_title(f"Temperatura {T}"); ax.tick_params(axis="x", rotation=45)
ejes[0].set_ylabel("Probabilidad")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `siguiente = ["limpio", "ruidoso", "caro", "cerca", "agradable"]` → Guarda el valor en `siguiente`.
- `logits = np.array([[3.0, 1.0, 0.5, 2.0, 2.5]])` → Guarda en `logits` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `fig, ejes = plt.subplots(1, 3, figsize=(11, 3), sharey=True)` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for ax, T in zip(ejes, [0.3, 1.0, 2.5]):` → Repite el bloque de debajo para cada valor de `ax, T` en `zip(ejes, [0.3, 1.0, 2.5])`. Dentro del bloque: `softmax`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*; `bar`: dibuja barras verticales; `set_title`: pone el título de un gráfico.
- `ejes[0].set_ylabel("Probabilidad")` → `set_ylabel`: pone el nombre del eje vertical.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 14 · 4. Del cálculo a la generación: logits, softmax… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 15 · 5. Mini-reto integrador: ¿de qué depende que un… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 16 · 6. OPCIONAL · Hugging Face en Colab: sentimient… · 🏠

**Qué hace:** NO VERIFICADO: requiere internet y descarga de modelos.

```python
USAR_HUGGING_FACE = False   # ← True solo en Colab con internet

if USAR_HUGGING_FACE:
    # NO VERIFICADO: requiere internet y descarga de modelos
# %pip install -q transformers
    from transformers import pipeline
    opiniones = ["El desayuno era delicioso y el personal encantador", "Ruido toda la noche y nadie atendía en recepción"]
    clasificador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    print(clasificador(opiniones))
    zero = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
    print(zero("Nadie atendía en recepción", candidate_labels=["limpieza", "personal", "ruido", "precio"],
               hypothesis_template="Esta reseña trata de {}."))
else:
    print("Parte opcional omitida (USAR_HUGGING_FACE = False).")
```

**Qué hace cada línea:**

- `USAR_HUGGING_FACE = False # ← True solo en Colab con internet` → Guarda el valor en `USAR_HUGGING_FACE`.
- `if USAR_HUGGING_FACE:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `pipeline`: atajo de la librería transformers para cargar un modelo ya entrenado y usarlo; `clasificador`: el clasificador de opiniones ya cargado (transformers); `zero`: clasificador «de cero ejemplos»: asigna etiquetas que no ha visto al entrenar.

---
*Generado a partir de `laboratorios/fuentes/S12_05_transformers_atencion.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
