# Código explicado · S09.01 · Segmentar huéspedes con clustering

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_01_clustering.ipynb) · [descargar](../S09_01_clustering.ipynb) · ⏱ en clase: 45 min · 🏫 5 celdas de código en clase · 🏠 5 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`, `set_theme`, `read_csv`, `head` y más. |
| 3 | 1. Escalar: que todas las variables "pe… | Practica `std`, `round`, `mean` (sección «1. Escalar: que todas las variables "pe…»). |
| 5 | 2. k-means: agrupar alrededor de centros | Practica `fit`, `bincount`, `round`, `KMeans` (sección «2. k-means: agrupar alrededor de… |
| 7 | 2. k-means: agrupar alrededor de centros | Practica `subplots`, `plot`, `axvline`, `set_xlabel` y más (sección «Ejercicio 2»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `huespedes` | `pd.read_csv(dato("huespedes.csv"))` | 1 |
| `edad` | `huespedes["edad"]` | 3 |
| `edad_escalada` | `(edad - edad.mean()) / edad.std()` | 3 |
| `km3` | `KMeans(n_clusters=3, n_init=10, random_state=SEMILLA).fit…` | 5 |
| `km` | `KMeans(n_clusters=k_mejor, n_init=10, random_state=SEMILL…` | 8 |
| `perfil` | `huespedes.groupby("grupo")[variables].mean().round(1)` | 8 |
| `perfil_z` | `pd.DataFrame(km.cluster_centers_, columns=variables)` | 9 |
| `muestra` | `np.random.default_rng(SEMILLA).choice(len(X), size=150, r…` | 11 |
| `Z` | `linkage(X[muestra], method="ward")` | 11 |
| `real` | `pd.read_csv(dato("_solucion_huespedes.csv"))` | 16 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `adjusted_rand_score` | Mide cuánto coinciden dos agrupaciones (1 = idénticas). | 16 |
| `axvline` | Dibuja una línea vertical de referencia. | 7 |
| `bincount` | Cuenta cuántas veces aparece cada entero. | 5 |
| `choice` | Elige un elemento al azar. | 11 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 9 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1, 16 |
| `DBSCAN` | Agrupa por densidad y marca el ruido como −1. | 13 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 11 |
| `dendrogram` | Dibuja el árbol de uniones del clustering jerárquico. | 11 |
| `describe` | Resumen estadístico de las columnas (media, mínimo, máximo…). | 2 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 5, 8 |
| `fit_predict` | Entrena y devuelve el grupo asignado a cada dato (clustering). | 13 |
| `groupby` | Agrupa las filas por una columna para calcular algo en cada grupo. | 8 |
| `head` | Muestra las primeras filas. | 1 |
| `heatmap` | Dibuja una matriz como un mapa de colores. | 9 |
| `KMeans` | Agrupa los datos en K grupos (clustering). | 5, 8 |
| `legend` | Muestra la leyenda del gráfico. | 7 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 11, 13 |
| `linkage` | Calcula cómo se van uniendo los datos en el clustering jerárquico. | 11 |
| `list` | Crea una lista (o convierte algo en lista). | 7 |
| `mean` | Calcula la media. | 3, 8, 13 |
| `plot` | Dibuja una línea (o puntos unidos). | 7 |
| `print` | Muestra un valor por pantalla. | 1, 3, 5, 13, 16 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 1, 16 |
| `round` | Redondea un número a los decimales indicados. | 2, 3, 5, 8, 16 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 13 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_title` | Pone el título de un gráfico. | 7, 9, 11 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 7 |
| `set_ylabel` | Pone el nombre del eje vertical. | 7, 9, 11 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 1 |
| `show` | Muestra el gráfico. | 7, 9, 11 |
| `sort_index` | Ordena la tabla por su índice. | 8 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 3 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 7, 9, 11 |
| `value_counts` | Cuenta cuántas veces aparece cada valor. | 8 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `seed`, `set_theme`, `read_csv`, `head` y más.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram

SEMILLA = 42
np.random.seed(SEMILLA)
sns.set_theme(style="whitegrid")

huespedes = pd.read_csv(dato("huespedes.csv"))
print(huespedes.shape)
huespedes.head()
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.preprocessing import StandardScaler` → Trae `StandardScaler` de `sklearn.preprocessing` para poder usarlo.
- `from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN` → Trae `KMeans`, `AgglomerativeClustering`, `DBSCAN` de `sklearn.cluster` para poder usarlo.
- `from sklearn.metrics import silhouette_score` → Trae `silhouette_score` de `sklearn.metrics` para poder usarlo.
- `from scipy.cluster.hierarchy import linkage, dendrogram` → Trae `linkage`, `dendrogram` de `scipy.cluster.hierarchy` para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- … y 5 más con las mismas ideas.

### Celda 2 · 🏫

**Qué hace:** Practica `round`, `describe`.

```python
huespedes.describe().round(1).T
```

**Qué hace cada línea:**

- `huespedes.describe().round(1).T` → `round`: redondea un número a los decimales indicados; `describe`: resumen estadístico de las columnas (media, mínimo, máximo…).

### Celda 3 · 1. Escalar: que todas las variables "pesen" lo… · 🏫

**Qué hace:** Practica `std`, `round`, `mean` (sección «1. Escalar: que todas las variables "pe…»).

```python
edad = huespedes["edad"]
edad_escalada = (edad - edad.mean()) / edad.std()
print("media:", round(edad_escalada.mean(), 3), "· desviación:", round(edad_escalada.std(), 3))
```

**Qué hace cada línea:**

- `edad = huespedes["edad"]` → Guarda el valor en `edad`.
- `edad_escalada = (edad - edad.mean()) / edad.std()` → Guarda en `edad_escalada` el resultado. `std`: calcula la desviación típica (cuánto se separan los datos de la media); `mean`: calcula la media.
- `print("media:", round(edad_escalada.mean(), 3), "· desviación:", round(edad…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.

### Celda 4 · 1. Escalar: que todas las variables "pesen" lo… · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2. k-means: agrupar alrededor de centros · 🏫

**Qué hace:** Practica `fit`, `bincount`, `round`, `KMeans` (sección «2. k-means: agrupar alrededor de centros»).

```python
km3 = KMeans(n_clusters=3, n_init=10, random_state=SEMILLA).fit(X)
print("Tamaño de cada grupo:", np.bincount(km3.labels_))
print("Inercia (suma de distancias al centro):", round(km3.inertia_))
```

**Qué hace cada línea:**

- `km3 = KMeans(n_clusters=3, n_init=10, random_state=SEMILLA).fit(X)` → Guarda en `km3` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `KMeans`: agrupa los datos en K grupos (clustering).
- `print("Tamaño de cada grupo:", np.bincount(km3.labels_))` → `print`: muestra un valor por pantalla; `bincount`: cuenta cuántas veces aparece cada entero.
- `print("Inercia (suma de distancias al centro):", round(km3.inertia_))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados.

### Celda 6 · 2. k-means: agrupar alrededor de centros · 🏫 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 2. k-means: agrupar alrededor de centros · 🏫

**Qué hace:** Practica `subplots`, `plot`, `axvline`, `set_xlabel` y más (sección «Ejercicio 2»).

```python
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(list(siluetas), list(siluetas.values()), marker="o")
ax.axvline(k_mejor, color="tab:red", linestyle="--", label=f"mejor k = {k_mejor}")
ax.set_xlabel("Número de grupos (k)")
ax.set_ylabel("Silueta media")
ax.set_title("¿Cuántos segmentos de huéspedes hay?")
ax.legend()
plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(figsize=(6, 3.5))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax.plot(list(siluetas), list(siluetas.values()), marker="o")` → `plot`: dibuja una línea (o puntos unidos); `list`: crea una lista (o convierte algo en lista); `values`: devuelve los valores de un diccionario o de una tabla.
- `ax.axvline(k_mejor, color="tab:red", linestyle="--", label=f"mejor k = {k_m…` → `axvline`: dibuja una línea vertical de referencia.
- `ax.set_xlabel("Número de grupos (k)")` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_ylabel("Silueta media")` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_title("¿Cuántos segmentos de huéspedes hay?")` → `set_title`: pone el título de un gráfico.
- `ax.legend()` → `legend`: muestra la leyenda del gráfico.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 8 · 3. Interpretar: ¿quién es cada grupo? · 🏠

**Qué hace:** Practica `fit`, `round`, `sort_index`, `KMeans` y más (sección «3. Interpretar: ¿quién es cada grupo?»).

```python
km = KMeans(n_clusters=k_mejor, n_init=10, random_state=SEMILLA).fit(X)
huespedes["grupo"] = km.labels_
perfil = huespedes.groupby("grupo")[variables].mean().round(1)
perfil["n_huespedes"] = huespedes["grupo"].value_counts().sort_index()
perfil
```

**Qué hace cada línea:**

- `km = KMeans(n_clusters=k_mejor, n_init=10, random_state=SEMILLA).fit(X)` → Guarda en `km` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `KMeans`: agrupa los datos en K grupos (clustering).
- `huespedes["grupo"] = km.labels_` → Guarda el valor en `huespedes["grupo"]`.
- `perfil = huespedes.groupby("grupo")[variables].mean().round(1)` → Guarda en `perfil` el resultado. `round`: redondea un número a los decimales indicados; `mean`: calcula la media; `groupby`: agrupa las filas por una columna para calcular algo en cada grupo.
- `perfil["n_huespedes"] = huespedes["grupo"].value_counts().sort_index()` → Guarda en `perfil["n_huespedes"]` el resultado. `sort_index`: ordena la tabla por su índice; `value_counts`: cuenta cuántas veces aparece cada valor.

### Celda 9 · 3. Interpretar: ¿quién es cada grupo? · 🏠

**Qué hace:** Mapa de calor con los perfiles estandarizados (comparables entre variables).

```python
# Mapa de calor con los perfiles estandarizados (comparables entre variables)
perfil_z = pd.DataFrame(km.cluster_centers_, columns=variables)
fig, ax = plt.subplots(figsize=(9, 3.5))
sns.heatmap(perfil_z, annot=True, fmt=".1f", cmap="RdBu_r", center=0, ax=ax)
ax.set_title("Perfil de cada grupo (en desviaciones típicas respecto a la media)")
ax.set_ylabel("Grupo")
plt.show()
```

**Qué hace cada línea:**

- `perfil_z = pd.DataFrame(km.cluster_centers_, columns=variables)` → Guarda en `perfil_z` el resultado. `DataFrame`: crea una tabla de pandas (filas y columnas).
- `fig, ax = plt.subplots(figsize=(9, 3.5))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `sns.heatmap(perfil_z, annot=True, fmt=".1f", cmap="RdBu_r", center=0, ax=ax)` → `heatmap`: dibuja una matriz como un mapa de colores.
- `ax.set_title("Perfil de cada grupo (en desviaciones típicas respecto a la m…` → `set_title`: pone el título de un gráfico.
- `ax.set_ylabel("Grupo")` → `set_ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 10 · 3. Interpretar: ¿quién es cada grupo? · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 4. Clustering jerárquico: un árbol de parecidos · 🏠

**Qué hace:** Practica `choice`, `linkage`, `subplots`, `dendrogram` y más (sección «4. Clustering jerárquico: un árbol de p…»).

```python
muestra = np.random.default_rng(SEMILLA).choice(len(X), size=150, replace=False)
Z = linkage(X[muestra], method="ward")
fig, ax = plt.subplots(figsize=(10, 4))
dendrogram(Z, no_labels=True, color_threshold=Z[-4, 2], ax=ax)
ax.set_title("Dendrograma (150 huéspedes): los saltos grandes indican grupos distintos")
ax.set_ylabel("Distancia de fusión")
plt.show()
```

**Qué hace cada línea:**

- `muestra = np.random.default_rng(SEMILLA).choice(len(X), size=150, replace=F…` → Guarda en `muestra` el resultado. `choice`: elige un elemento al azar; `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `Z = linkage(X[muestra], method="ward")` → Guarda en `Z` el resultado. `linkage`: calcula cómo se van uniendo los datos en el clustering jerárquico.
- `fig, ax = plt.subplots(figsize=(10, 4))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `dendrogram(Z, no_labels=True, color_threshold=Z[-4, 2], ax=ax)` → `dendrogram`: dibuja el árbol de uniones del clustering jerárquico.
- `ax.set_title("Dendrograma (150 huéspedes): los saltos grandes indican grupo…` → `set_title`: pone el título de un gráfico.
- `ax.set_ylabel("Distancia de fusión")` → `set_ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 12 · 4. Clustering jerárquico: un árbol de parecidos · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 5. DBSCAN: grupos por densidad (y ruido) · 🏠

**Qué hace:** Practica `fit_predict`, `DBSCAN`, `set`, `mean` (sección «5. DBSCAN: grupos por densidad (y ruido)»).

```python
for eps in (0.6, 0.8, 1.0, 1.2, 1.5):
    et = DBSCAN(eps=eps, min_samples=10).fit_predict(X)
    n_grupos = len(set(et)) - (1 if -1 in et else 0)
    print(f"eps={eps}: {n_grupos} grupos, {np.mean(et == -1):.0%} de ruido")
```

**Qué hace cada línea:**

- `for eps in (0.6, 0.8, 1.0, 1.2, 1.5):` → Repite el bloque de debajo para cada valor de `eps` en `(0.6, 0.8, 1.0, 1.2, 1.5)`. Dentro del bloque: `fit_predict`: entrena y devuelve el grupo asignado a cada dato (clustering); `DBSCAN`: agrupa por densidad y marca el ruido como −1; `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.

### Celda 14 · 5. DBSCAN: grupos por densidad (y ruido) · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 15 · Mini-reto integrador: ponle nombre a tus segmen… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 16 · Qué has aprendido · 🏠

**Qué hace:** Solo docente: contraste con el segmento real.

```python
# Solo docente: contraste con el segmento real
from sklearn.metrics import adjusted_rand_score
real = pd.read_csv(dato("_solucion_huespedes.csv"))
print("ARI k-means:", round(adjusted_rand_score(real["segmento_real"], huespedes["grupo"]), 3))
print("ARI jerárquico:", round(adjusted_rand_score(real["segmento_real"], etiquetas_jer), 3))
```

**Qué hace cada línea:**

- `from sklearn.metrics import adjusted_rand_score` → Trae `adjusted_rand_score` de `sklearn.metrics` para poder usarlo.
- `real = pd.read_csv(dato("_solucion_huespedes.csv"))` → Guarda en `real` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `print("ARI k-means:", round(adjusted_rand_score(real["segmento_real"], hues…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `adjusted_rand_score`: mide cuánto coinciden dos agrupaciones (1 = idénticas).
- `print("ARI jerárquico:", round(adjusted_rand_score(real["segmento_real"], e…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `adjusted_rand_score`: mide cuánto coinciden dos agrupaciones (1 = idénticas).

---
*Generado a partir de `laboratorios/fuentes/S09_01_clustering.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
