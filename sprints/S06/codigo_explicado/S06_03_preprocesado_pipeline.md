# Código explicado · S06.03 · Preprocesado y *pipelines* reproducibles

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/notebooks/S06_03_preprocesado_pipeline.ipynb) · [descargar](../notebooks/S06_03_preprocesado_pipeline.ipynb) · ⏱ en clase: 40 min · 🏫 5 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_theme`. |
| 2 | 1. Punto de partida: datos ya limpiados | Practica `copy`, `to_numeric`, `to_datetime`, `fillna` y más (sección «1. Punto de partid… |
| 3 | 2. Separar entrenamiento y prueba | Crea `columnas_num`, `columnas_cat`, `X` y más. |
| 5 | 3. Escalado | Practica `SimpleImputer`, `StandardScaler`, `fit_transform`, `transform` y más (sección «… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `EQUIV_PAIS` | `{"es": "ES", "españa": "ES", "uk": "UK", "reino unido": "…` | 2 |
| `reservas` | `limpiar_reservas(pd.read_csv(dato("reservas_sucio.csv")))` | 2 |
| `columnas_num` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 3 |
| `columnas_cat` | `["tipo_habitacion", "regimen", "canal", "pais_origen", "t…` | 3 |
| `X` | `reservas[columnas_num + columnas_cat]` | 3 |
| `y` | `reservas["cancelada"]` | 3 |
| `imputador` | `SimpleImputer(strategy="median")` | 5 |
| `escalador` | `StandardScaler()` | 5 |
| `num_train` | `escalador.fit_transform(imputador.fit_transform(X_train[c…` | 5 |
| `num_test` | `escalador.transform(imputador.transform(X_test[columnas_n…` | 5 |
| `onehot` | `OneHotEncoder(handle_unknown="ignore", sparse_output=Fals…` | 7 |
| `esc_mal` | `StandardScaler().fit(reservas[["precio_noche"]].fillna(re…` | 11 |
| `esc_bien` | `StandardScaler().fit(X_train[["precio_noche"]].fillna(X_t…` | 11 |
| `pca` | `PCA(n_components=5, random_state=SEMILLA).fit(num_train)` | 12 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `limpiar_reservas` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 2 |
| `bar` | Dibuja barras verticales. | 12 |
| `between` | Marca los valores que están entre dos límites. | 2 |
| `copy` | Hace una copia independiente (si cambias la copia, el original no cambia). | 2 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `drop_duplicates` | Quita las filas repetidas. | 2 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 2 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 12 |
| `fillna` | Rellena los huecos con un valor. | 2, 11 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 7, 11, 12 |
| `fit_transform` | Ajusta el preprocesado con estos datos y los transforma, todo a la vez. | 5 |
| `get_feature_names_out` | Devuelve los nombres de las columnas después del preprocesado. | 7 |
| `isna` | Marca qué valores son huecos (nulos). | 2 |
| `lower` | Pasa el texto a minúsculas. | 2 |
| `map` | Cambia cada valor según un diccionario o función. | 2 |
| `mean` | Calcula la media. | 5 |
| `median` | Calcula la mediana (el valor central). | 11 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 7 |
| `PCA` | Reduce las columnas a unas pocas combinaciones que conservan la mayor parte de la información. | 12 |
| `print` | Muestra un valor por pantalla. | 2, 5, 7, 11 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 12 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `replace` | Sustituye un trozo de texto (o valores de una tabla) por otro. | 2 |
| `reset_index` | Devuelve el índice de la tabla a 0, 1, 2… | 2 |
| `round` | Redondea un número a los decimales indicados. | 5, 11 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2 |
| `show` | Muestra el gráfico. | 12 |
| `SimpleImputer` | Rellena huecos con la media, la mediana o el valor más frecuente. | 5 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 5, 11 |
| `str` | Da acceso a las operaciones de texto sobre una columna. | 2 |
| `strip` | Quita espacios al principio y al final de un texto. | 2 |
| `sum` | Suma todos los valores. | 2 |
| `title` | Pone el título del gráfico. | 12 |
| `to_datetime` | Convierte un texto en fecha. | 2 |
| `to_numeric` | Convierte un texto en número (los fallos se pueden marcar como hueco). | 2 |
| `transform` | Calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado. | 5 |
| `where` | Elige un valor u otro según una condición (como un `if` para todos los datos a la vez). | 2 |
| `xlabel` | Pone el nombre del eje horizontal. | 12 |
| `ylabel` | Pone el nombre del eje vertical. | 12 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_theme`.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.base import clone

SEMILLA = 42
sns.set_theme(style="whitegrid")
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.impute import SimpleImputer` → Trae `SimpleImputer` de `sklearn.impute` para poder usarlo.
- `from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncod…` → Trae `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `OrdinalEncoder` de `sklearn.preprocessing` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- `from sklearn.pipeline import Pipeline` → Trae `Pipeline` de `sklearn.pipeline` para poder usarlo.
- … y 5 más con las mismas ideas.

### Celda 2 · 1. Punto de partida: datos ya limpiados · 🏫

**Qué hace:** Practica `copy`, `to_numeric`, `to_datetime`, `fillna` y más (sección «1. Punto de partida: datos ya limpiados»).

```python
EQUIV_PAIS = {"es": "ES", "españa": "ES", "uk": "UK", "reino unido": "UK", "de": "DE",
              "nl": "NL", "it": "IT", "fr": "FR", "nordicos": "Nordicos", "otros": "otros"}

def limpiar_reservas(tabla):
    t = tabla.drop_duplicates().reset_index(drop=True).copy()
    t["precio_noche"] = pd.to_numeric(t["precio_noche"].astype(str).str.replace(",", "."), errors="coerce")
    iso = pd.to_datetime(t["fecha_reserva"], format="%Y-%m-%d", errors="coerce")
    esp = pd.to_datetime(t["fecha_reserva"], format="%d/%m/%Y", errors="coerce")
    t["fecha_reserva"] = iso.fillna(esp)
    t["fecha_llegada"] = pd.to_datetime(t["fecha_llegada"], format="%Y-%m-%d")
    t["canal"] = t["canal"].str.strip().str.lower().str.replace(" ", "_")
    t["pais_origen"] = t["pais_origen"].str.strip().str.lower().map(EQUIV_PAIS)
    t["precio_noche"] = t["precio_noche"].where(t["precio_noche"].between(20, 1000))
    t["noches"] = t["noches"].where(t["noches"].between(1, 60))
    t["antelacion_dias"] = (t["fecha_llegada"] - t["fecha_reserva"]).dt.days
    t["mes_llegada"] = t["fecha_llegada"].dt.month
    return t

reservas = limpiar_reservas(pd.read_csv(dato("reservas_sucio.csv")))
print(reservas.shape)
reservas.isna().sum()[lambda s: s > 0]
```

**Qué hace cada línea:**

- `EQUIV_PAIS = {"es": "ES", "españa": "ES", "uk": "UK", "reino unido": "UK",…` → Guarda el valor en `EQUIV_PAIS`.
- `def limpiar_reservas(tabla):` → Define la función `limpiar_reservas`: Función definida en el cuaderno.
- `reservas = limpiar_reservas(pd.read_csv(dato("reservas_sucio.csv")))` → Guarda en `reservas` el resultado. `limpiar_reservas`: función definida en el cuaderno; `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `print(reservas.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- `reservas.isna().sum()[lambda s: s > 0]` → `sum`: suma todos los valores; `isna`: marca qué valores son huecos (nulos).

### Celda 3 · 2. Separar entrenamiento y prueba · 🏫

**Qué hace:** Crea `columnas_num`, `columnas_cat`, `X` y más.

```python
columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "mes_llegada"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X = reservas[columnas_num + columnas_cat]
y = reservas["cancelada"]
```

**Qué hace cada línea:**

- `columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_no…` → Guarda el valor en `columnas_num`.
- `columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tari…` → Guarda el valor en `columnas_cat`.
- `X = reservas[columnas_num + columnas_cat]` → Guarda el valor en `X`.
- `y = reservas["cancelada"]` → Guarda el valor en `y`.

### Celda 4 · 2. Separar entrenamiento y prueba · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 3. Escalado · 🏫

**Qué hace:** Practica `SimpleImputer`, `StandardScaler`, `fit_transform`, `transform` y más (sección «3. Escalado»).

```python
imputador = SimpleImputer(strategy="median")
escalador = StandardScaler()
num_train = escalador.fit_transform(imputador.fit_transform(X_train[columnas_num]))
num_test = escalador.transform(imputador.transform(X_test[columnas_num]))
print("Media de cada columna en train (≈0):", num_train.mean(axis=0).round(2))
print("Media en test (no tiene por qué ser 0):", num_test.mean(axis=0).round(2))
```

**Qué hace cada línea:**

- `imputador = SimpleImputer(strategy="median")` → Guarda en `imputador` el resultado. `SimpleImputer`: rellena huecos con la media, la mediana o el valor más frecuente.
- `escalador = StandardScaler()` → Guarda en `escalador` el resultado. `StandardScaler`: escala los números para que tengan media 0 y desviación 1.
- `num_train = escalador.fit_transform(imputador.fit_transform(X_train[columna…` → Guarda en `num_train` el resultado. `fit_transform`: ajusta el preprocesado con estos datos y los transforma, todo a la vez.
- `num_test = escalador.transform(imputador.transform(X_test[columnas_num]))` → Guarda en `num_test` el resultado. `transform`: calcula algo por grupo y lo devuelve con la forma original; en scikit-learn, aplica un preprocesado ya ajustado.
- `print("Media de cada columna en train (≈0):", num_train.mean(axis=0).round(…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.
- `print("Media en test (no tiene por qué ser 0):", num_test.mean(axis=0).roun…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.

### Celda 6 · 3. Escalado · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4. Codificación de categóricas · 🏫

**Qué hace:** Practica `OneHotEncoder`, `fit`, `get_feature_names_out` (sección «4. Codificación de categóricas»).

```python
onehot = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
onehot.fit(X_train[["canal"]])
print(onehot.get_feature_names_out())
```

**Qué hace cada línea:**

- `onehot = OneHotEncoder(handle_unknown="ignore", sparse_output=False)` → Guarda en `onehot` el resultado. `OneHotEncoder`: convierte categorías en columnas de 0/1.
- `onehot.fit(X_train[["canal"]])` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `print(onehot.get_feature_names_out())` → `print`: muestra un valor por pantalla; `get_feature_names_out`: devuelve los nombres de las columnas después del preprocesado.

### Celda 8 · 4. Codificación de categóricas · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5. `ColumnTransformer` y `Pipeline`: la receta… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5. `ColumnTransformer` y `Pipeline`: la receta… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 6. Fuga de datos en el preprocesado · 🏠

**Qué hace:** MAL: el escalador "ve" también las filas de test.

```python
# MAL: el escalador "ve" también las filas de test
esc_mal = StandardScaler().fit(reservas[["precio_noche"]].fillna(reservas["precio_noche"].median()))
# BIEN: solo train
esc_bien = StandardScaler().fit(X_train[["precio_noche"]].fillna(X_train["precio_noche"].median()))
print("Media aprendida (mal, con todo):", esc_mal.mean_[0].round(3))
print("Media aprendida (bien, solo train):", esc_bien.mean_[0].round(3))
```

**Qué hace cada línea:**

- `esc_mal = StandardScaler().fit(reservas[["precio_noche"]].fillna(reservas["…` → Guarda en `esc_mal` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `fillna`: rellena los huecos con un valor; `StandardScaler`: escala los números para que tengan media 0 y desviación 1.
- `esc_bien = StandardScaler().fit(X_train[["precio_noche"]].fillna(X_train["p…` → Guarda en `esc_bien` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `fillna`: rellena los huecos con un valor; `StandardScaler`: escala los números para que tengan media 0 y desviación 1.
- `print("Media aprendida (mal, con todo):", esc_mal.mean_[0].round(3))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados.
- `print("Media aprendida (bien, solo train):", esc_bien.mean_[0].round(3))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados.

### Celda 12 · 7. Un vistazo a la reducción de dimensionalidad… · 🏠

**Qué hace:** Practica `fit`, `figure`, `bar`, `title` y más (sección «7. Un vistazo a la reducción de dimensi…»).

```python
pca = PCA(n_components=5, random_state=SEMILLA).fit(num_train)
plt.figure(figsize=(6, 3.5))
plt.bar(range(1, 6), pca.explained_variance_ratio_, color="#2a6f97")
plt.title("Varianza explicada por componente (PCA)")
plt.xlabel("Componente")
plt.ylabel("Proporción de la varianza")
plt.show()
```

**Qué hace cada línea:**

- `pca = PCA(n_components=5, random_state=SEMILLA).fit(num_train)` → Guarda en `pca` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `PCA`: reduce las columnas a unas pocas combinaciones que conservan la mayor parte de la información.
- `plt.figure(figsize=(6, 3.5))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.bar(range(1, 6), pca.explained_variance_ratio_, color="#2a6f97")` → `bar`: dibuja barras verticales; `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `plt.title("Varianza explicada por componente (PCA)")` → `title`: pone el título del gráfico.
- `plt.xlabel("Componente")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("Proporción de la varianza")` → `ylabel`: pone el nombre del eje vertical.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 13 · 8. Mini-reto: comprueba que tu pipeline es repr… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S06_03_preprocesado_pipeline.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
