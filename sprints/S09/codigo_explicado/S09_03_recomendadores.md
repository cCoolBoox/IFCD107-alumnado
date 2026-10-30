# Código explicado · S09.03 · Recomendar experiencias a los huéspedes

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_03_recomendadores.ipynb) · [descargar](../notebooks/S09_03_recomendadores.ipynb) · ⏱ en clase: 50 min · 🏫 6 celdas de código en clase · 🏠 3 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`, `set_theme`, `read_csv`, `head` y más. |
| 2 | 1. La matriz usuario × experiencia y la… | filas = usuarios 1..300, columnas = experiencias 1..25. |
| 3 | 1. La matriz usuario × experiencia y la… | Practica `full`, `round` (sección «1. La matriz usuario × experiencia y la…»). |
| 5 | 2. Recomendador por popularidad | Practica `head`, `assign`, `sort_values`, `to_frame` y más (sección «Ejercicio 1»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `valoraciones` | `pd.read_csv(dato("valoraciones_experiencias.csv"))` | 1 |
| `experiencias` | `pd.read_csv(dato("experiencias.csv"))` | 1 |
| `prueba` | `valoraciones.sample(frac=0.2, random_state=SEMILLA)` | 2 |
| `entrenamiento` | `valoraciones.drop(prueba.index)` | 2 |
| `R` | `entrenamiento.pivot(index="id_usuario", columns="id_exper…` | 2 |
| `M` | `R.notna().values` | 2 |
| `media_global` | `entrenamiento["valoracion"].mean()` | 2 |
| `fila_p` | `prueba["id_usuario"].values - 1` | 2 |
| `col_p` | `prueba["id_experiencia"].values - 1` | 2 |
| `real_p` | `prueba["valoracion"].values` | 2 |
| `P_global` | `np.full((300, 25), media_global)` | 3 |
| `top` | `media_item.sort_values(ascending=False).head(5)` | 5 |
| `F` | `pd.get_dummies(experiencias.set_index("id_experiencia")["…` | 7 |
| `media_item_v` | `media_item.fillna(media_global).values` | 7 |
| `C` | `np.where(M, R.values - media_item_v[None, :], 0.0)` | 7 |
| `P_cont` | `media_item_v[None, :] + perfil_usuario @ F.T` | 9 |
| `P_item` | `media_item_v[None, :] + (C @ S.T) / (M.astype(float) @ np…` | 11 |
| `Su` | `cosine_similarity(C)` | 11 |
| `P_user` | `media_item_v[None, :] + (Su @ C) / (np.abs(Su) @ M.astype…` | 11 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `evaluar_rmse` | RMSE de una matriz de predicciones P (300 x 25) sobre las valoraciones de prueba. |
| `precision_k` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `factorizar` | Factorización con sesgos por mínimos cuadrados alternos. Devuelve la matriz completa de predicciones. |
| `recomendar` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `abs` | Valor absoluto: quita el signo negativo. | 11 |
| `assign` | Añade columnas nuevas sin modificar la tabla original. | 5 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 7, 11 |
| `barh` | Dibuja barras horizontales. | 14 |
| `clip` | Limita los valores a un mínimo y un máximo. | 2 |
| `cosine_similarity` | Mide cuánto se parecen dos vectores (1 = igual dirección). | 11 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 12 |
| `drop` | Quita columnas o filas. | 2 |
| `eye` | Crea la matriz identidad. | 12 |
| `fill_diagonal` | Rellena la diagonal de una matriz con un valor. | 11 |
| `fillna` | Rellena los huecos con un valor. | 7 |
| `float` | Convierte un valor en número decimal. | 2 |
| `full` | Crea un array lleno del valor indicado. | 3 |
| `get_dummies` | Convierte una columna de categorías en columnas de 0/1. | 7 |
| `head` | Muestra las primeras filas. | 1, 5 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 5 |
| `mean` | Calcula la media. | 2 |
| `nan_to_num` | Sustituye huecos e infinitos por números. | 12 |
| `nanmean` | Media ignorando los huecos. | 12 |
| `normal` | Genera números aleatorios con forma de campana (normal). | 12 |
| `notna` | Marca qué valores NO son huecos. | 2, 12 |
| `nunique` | Cuenta cuántos valores distintos hay. | 7 |
| `pivot` | Reorganiza la tabla: una columna pasa a filas, otra a columnas. | 2 |
| `print` | Muestra un valor por pantalla. | 1, 2, 3, 5, 7, 9… |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 2, 7, 12 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1 |
| `reindex` | Reordena o amplía la tabla según una lista de etiquetas. | 2, 7 |
| `round` | Redondea un número a los decimales indicados. | 2, 3, 5, 9 |
| `sample` | Elige varios elementos al azar sin repetir. | 2 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `set_index` | Convierte una columna en el índice (la etiqueta de cada fila). | 5, 7 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_title` | Pone el título de un gráfico. | 14 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 14 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 1, 2, 7, 12 |
| `show` | Muestra el gráfico. | 14 |
| `solve` | Resuelve un sistema de ecuaciones lineales. | 12 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 5 |
| `sqrt` | Raíz cuadrada. | 2 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 14 |
| `sum` | Suma todos los valores. | 12 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 14 |
| `to_frame` | Convierte una columna (Series) en una tabla de una columna. | 5 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 2, 7, 12 |
| `where` | Elige un valor u otro según una condición (como un `if` para todos los datos a la vez). | 7 |
| `zeros` | Crea un array lleno de ceros. | 12 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `seed`, `set_theme`, `read_csv`, `head` y más.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

SEMILLA = 42
np.random.seed(SEMILLA)
sns.set_theme(style="whitegrid")

valoraciones = pd.read_csv(dato("valoraciones_experiencias.csv"))
experiencias = pd.read_csv(dato("experiencias.csv"))
print(valoraciones.shape, experiencias.shape)
valoraciones.head()
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.metrics.pairwise import cosine_similarity` → Trae `cosine_similarity` de `sklearn.metrics.pairwise` para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `np.random.seed(SEMILLA)` → `seed`: fija la semilla del azar para que salga siempre lo mismo.
- `sns.set_theme(style="whitegrid")` → `set_theme`: elige un estilo visual para todos los gráficos.
- `valoraciones = pd.read_csv(dato("valoraciones_experiencias.csv"))` → Guarda en `valoraciones` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- … y 3 más con las mismas ideas.

### Celda 2 · 1. La matriz usuario × experiencia y la separac… · 🏫

**Qué hace:** filas = usuarios 1..300, columnas = experiencias 1..25.

```python
prueba = valoraciones.sample(frac=0.2, random_state=SEMILLA)
entrenamiento = valoraciones.drop(prueba.index)

# filas = usuarios 1..300, columnas = experiencias 1..25
R = entrenamiento.pivot(index="id_usuario", columns="id_experiencia", values="valoracion")
R = R.reindex(index=range(1, 301), columns=range(1, 26))
M = R.notna().values                       # True donde hay valoración (matriz de "visto")
print("Matriz:", R.shape, "· casillas con dato:", f"{M.mean():.0%}")

media_global = entrenamiento["valoracion"].mean()
print("Nota media global:", round(media_global, 2))

# posiciones (fila, columna) de las valoraciones de prueba, para evaluar
fila_p = prueba["id_usuario"].values - 1
col_p = prueba["id_experiencia"].values - 1
real_p = prueba["valoracion"].values

def evaluar_rmse(P):
    """RMSE de una matriz de predicciones P (300 x 25) sobre las valoraciones de prueba."""
    pred = np.clip(P[fila_p, col_p], 1, 5)
    return float(np.sqrt(np.mean((pred - real_p) ** 2)))
```

**Qué hace cada línea:**

- `prueba = valoraciones.sample(frac=0.2, random_state=SEMILLA)` → Guarda en `prueba` el resultado. `sample`: elige varios elementos al azar sin repetir.
- `entrenamiento = valoraciones.drop(prueba.index)` → Guarda en `entrenamiento` el resultado. `drop`: quita columnas o filas.
- `R = entrenamiento.pivot(index="id_usuario", columns="id_experiencia", value…` → Guarda en `R` el resultado. `pivot`: reorganiza la tabla: una columna pasa a filas, otra a columnas.
- `R = R.reindex(index=range(1, 301), columns=range(1, 26))` → Guarda en `R` el resultado. `reindex`: reordena o amplía la tabla según una lista de etiquetas; `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `M = R.notna().values # True donde hay valoración (matriz de "visto")` → Guarda en `M` el resultado. `values`: devuelve los valores de un diccionario o de una tabla; `notna`: marca qué valores NO son huecos.
- `print("Matriz:", R.shape, "· casillas con dato:", f"{M.mean():.0%}")` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas); `mean`: calcula la media.
- `media_global = entrenamiento["valoracion"].mean()` → Guarda en `media_global` el resultado. `mean`: calcula la media.
- `print("Nota media global:", round(media_global, 2))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados.
- `fila_p = prueba["id_usuario"].values - 1` → Guarda en `fila_p` el resultado. `values`: devuelve los valores de un diccionario o de una tabla.
- … y 3 más con las mismas ideas.

### Celda 3 · 1. La matriz usuario × experiencia y la separac… · 🏫

**Qué hace:** Practica `full`, `round` (sección «1. La matriz usuario × experiencia y la…»).

```python
P_global = np.full((300, 25), media_global)
print("RMSE prediciendo siempre la media global:", round(evaluar_rmse(P_global), 3))
```

**Qué hace cada línea:**

- `P_global = np.full((300, 25), media_global)` → Guarda en `P_global` el resultado. `full`: crea un array lleno del valor indicado.
- `print("RMSE prediciendo siempre la media global:", round(evaluar_rmse(P_glo…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `evaluar_rmse`: RMSE de una matriz de predicciones P (300 x 25) sobre las valoraciones de prueba.

### Celda 4 · 2. Recomendador por popularidad · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2. Recomendador por popularidad · 🏫

**Qué hace:** Practica `head`, `assign`, `sort_values`, `to_frame` y más (sección «Ejercicio 1»).

```python
top = media_item.sort_values(ascending=False).head(5)
print(experiencias.set_index("id_experiencia").loc[top.index, "nombre"].to_frame().assign(nota=top.round(2)))
```

**Qué hace cada línea:**

- `top = media_item.sort_values(ascending=False).head(5)` → Guarda en `top` el resultado. `head`: muestra las primeras filas; `sort_values`: ordena la tabla por una o varias columnas.
- `print(experiencias.set_index("id_experiencia").loc[top.index, "nombre"].to_…` → `print`: muestra un valor por pantalla; `assign`: añade columnas nuevas sin modificar la tabla original; `to_frame`: convierte una columna (Series) en una tabla de una columna.

### Celda 6 · 3. Métrica de ranking: precision@k · 🏫 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4. Recomendador basado en contenido · 🏫

**Qué hace:** Practica `astype`, `values`, `where`, `shape` y más (sección «4. Recomendador basado en contenido»).

```python
F = pd.get_dummies(experiencias.set_index("id_experiencia")["categoria"]).reindex(range(1, 26)).values.astype(float)
print("F (experiencia x categoría):", F.shape, "· categorías:", experiencias["categoria"].nunique())

media_item_v = media_item.fillna(media_global).values      # nota media de cada experiencia
C = np.where(M, R.values - media_item_v[None, :], 0.0)     # residuo (0 donde no hay valoración)
```

**Qué hace cada línea:**

- `F = pd.get_dummies(experiencias.set_index("id_experiencia")["categoria"]).r…` → Guarda en `F` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `values`: devuelve los valores de un diccionario o de una tabla; `reindex`: reordena o amplía la tabla según una lista de etiquetas.
- `print("F (experiencia x categoría):", F.shape, "· categorías:", experiencia…` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas); `nunique`: cuenta cuántos valores distintos hay.
- `media_item_v = media_item.fillna(media_global).values # nota media de cada…` → Guarda en `media_item_v` el resultado. `values`: devuelve los valores de un diccionario o de una tabla; `fillna`: rellena los huecos con un valor.
- `C = np.where(M, R.values - media_item_v[None, :], 0.0) # residuo (0 donde n…` → Guarda en `C` el resultado. `where`: elige un valor u otro según una condición (como un `if` para todos los datos a la vez); `values`: devuelve los valores de un diccionario o de una tabla.

### Celda 8 · 4. Recomendador basado en contenido · 🏫 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4. Recomendador basado en contenido · 🏫

**Qué hace:** Predicción por contenido: nota media de la experiencia + afinidad del usuario con su categoría.

```python
# Predicción por contenido: nota media de la experiencia + afinidad del usuario con su categoría
P_cont = media_item_v[None, :] + perfil_usuario @ F.T
print("RMSE contenido:", round(evaluar_rmse(P_cont), 3), "· precision@3:", round(precision_k(P_cont), 3))
```

**Qué hace cada línea:**

- `P_cont = media_item_v[None, :] + perfil_usuario @ F.T` → Guarda el valor en `P_cont`.
- `print("RMSE contenido:", round(evaluar_rmse(P_cont), 3), "· precision@3:",…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `evaluar_rmse`: RMSE de una matriz de predicciones P (300 x 25) sobre las valoraciones de prueba.

### Celda 10 · 5. Filtrado colaborativo: "la gente como tú tam… · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 5. Filtrado colaborativo: "la gente como tú tam… · 🏠

**Qué hace:** Predicción item-item: nota media + media ponderada de los residuos del usuario en experiencias parecidas.

```python
# Predicción item-item: nota media + media ponderada de los residuos del usuario en experiencias parecidas
P_item = media_item_v[None, :] + (C @ S.T) / (M.astype(float) @ np.abs(S).T + 1e-9)

# Predicción user-user: lo mismo mirando usuarios parecidos
Su = cosine_similarity(C)
np.fill_diagonal(Su, 0)
P_user = media_item_v[None, :] + (Su @ C) / (np.abs(Su) @ M.astype(float) + 1e-9)

for nombre, P in (("item-item", P_item), ("user-user", P_user)):
    print(f"{nombre}: RMSE = {evaluar_rmse(P):.3f} · precision@3 = {precision_k(P):.3f}")
```

**Qué hace cada línea:**

- `P_item = media_item_v[None, :] + (C @ S.T) / (M.astype(float) @ np.abs(S).T…` → Guarda en `P_item` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `abs`: valor absoluto: quita el signo negativo.
- `Su = cosine_similarity(C)` → Guarda en `Su` el resultado. `cosine_similarity`: mide cuánto se parecen dos vectores (1 = igual dirección).
- `np.fill_diagonal(Su, 0)` → `fill_diagonal`: rellena la diagonal de una matriz con un valor.
- `P_user = media_item_v[None, :] + (Su @ C) / (np.abs(Su) @ M.astype(float) +…` → Guarda en `P_user` el resultado. `abs`: valor absoluto: quita el signo negativo; `astype`: cambia el tipo de los datos (por ejemplo, de texto a número).
- `for nombre, P in (("item-item", P_item), ("user-user", P_user)):` → Repite el bloque de debajo para cada valor de `nombre, P` en `(("item-item", P_item), ("user-user", P…`. Dentro del bloque: `evaluar_rmse`: RMSE de una matriz de predicciones P (300 x 25) sobre las valoraciones de prueba; `precision_k`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.

### Celda 12 · 6. Factorización de matrices: gustos ocultos · 🏠

**Qué hace:** Practica `default_rng`, `values`, `nan_to_num`, `shape` y más (sección «6. Factorización de matrices: gustos oc…»).

```python
def factorizar(R, k=3, lam=5.0, iteraciones=30, semilla=SEMILLA):
    """Factorización con sesgos por mínimos cuadrados alternos. Devuelve la matriz completa de predicciones."""
    rng = np.random.default_rng(semilla)
    Mv = R.notna().values
    Y = np.nan_to_num(R.values)
    n_u, n_i = Y.shape
    mu = np.nanmean(R.values)
    P = rng.normal(0, 0.1, (n_u, k))          # gustos de cada usuario
    Q = rng.normal(0, 0.1, (n_i, k))          # intensidades de cada experiencia
    b_u, b_i = np.zeros(n_u), np.zeros(n_i)
    for _ in range(iteraciones):
        res = (Y - mu - b_i[None, :] - P @ Q.T) * Mv
        b_u = res.sum(1) / (Mv.sum(1) + 5)
        res = (Y - mu - b_u[:, None] - P @ Q.T) * Mv
        b_i = res.sum(0) / (Mv.sum(0) + 5)
        T = Y - mu - b_u[:, None] - b_i[None, :]
        for u in range(n_u):
            Qu = Q[Mv[u]]
            P[u] = np.linalg.solve(Qu.T @ Qu + lam * np.eye(k), Qu.T @ T[u, Mv[u]])
        for i in range(n_i):
            Pi = P[Mv[:, i]]
            Q[i] = np.linalg.solve(Pi.T @ Pi + lam * np.eye(k), Pi.T @ T[Mv[:, i], i])
    return mu + b_u[:, None] + b_i[None, :] + P @ Q.T

for k in (2, 3, 4, 6):
    print(f"k = {k} gustos ocultos → RMSE = {evaluar_rmse(factorizar(R, k=k)):.3f}")
```

**Qué hace cada línea:**

- `def factorizar(R, k=3, lam=5.0, iteraciones=30, semilla=SEMILLA):` → Define la función `factorizar`: Factorización con sesgos por mínimos cuadrados alternos. Devuelve la matriz completa de predicciones.
- `for k in (2, 3, 4, 6):` → Repite el bloque de debajo para cada valor de `k` en `(2, 3, 4, 6)`. Dentro del bloque: `evaluar_rmse`: RMSE de una matriz de predicciones P (300 x 25) sobre las valoraciones de prueba; `factorizar`: factorización con sesgos por mínimos cuadrados alternos. Devuelve la matriz completa de predicciones.

### Celda 13 · 6. Factorización de matrices: gustos ocultos · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 14 · 6. Factorización de matrices: gustos ocultos · 🏠

**Qué hace:** Practica `subplots`, `barh`, `set_title`, `set_xlabel` y más (sección «Ejercicio 5»).

```python
fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))
tabla["RMSE"].plot.barh(ax=ax[0], color="tab:blue"); ax[0].set_title("Error de la nota (RMSE) — menos es mejor"); ax[0].set_xlabel("estrellas")
tabla["precision@3"].plot.barh(ax=ax[1], color="tab:green"); ax[1].set_title("precision@3 — más es mejor"); ax[1].set_xlabel("proporción de aciertos")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `tabla["RMSE"].plot.barh(ax=ax[0], color="tab:blue"); ax[0].set_title("Error…` → `barh`: dibuja barras horizontales.
- `tabla["RMSE"].plot.barh(ax=ax[0], color="tab:blue"); ax[0].set_title("Error…` → `set_title`: pone el título de un gráfico.
- `tabla["RMSE"].plot.barh(ax=ax[0], color="tab:blue"); ax[0].set_title("Error…` → `set_xlabel`: pone el nombre del eje horizontal.
- `tabla["precision@3"].plot.barh(ax=ax[1], color="tab:green"); ax[1].set_titl…` → `barh`: dibuja barras horizontales.
- `tabla["precision@3"].plot.barh(ax=ax[1], color="tab:green"); ax[1].set_titl…` → `set_title`: pone el título de un gráfico.
- `tabla["precision@3"].plot.barh(ax=ax[1], color="tab:green"); ax[1].set_titl…` → `set_xlabel`: pone el nombre del eje horizontal.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 15 · Mini-reto integrador: el recomendador de TurisD… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S09_03_recomendadores.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
