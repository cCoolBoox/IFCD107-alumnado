# Código explicado · S15.01 · Seguimiento de experimentos y reproducibilidad

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/2_Practica/para_casa/S15_01_seguimiento_experimentos.ipynb) · [descargar](../para_casa/S15_01_seguimiento_experimentos.ipynb) · ⏱ en clase: 50 min · 🏫 4 celdas de código en clase · 🏠 2 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_theme`. |
| 3 | 1. Reproducibilidad: semillas y version… | Ficha del entorno: cópiala en la memoria técnica y en el README del equipo. |
| 5 | 3. Experimentos: baseline y modelos con… | huella de los datos: si alguien cambia el CSV, el hash cambia y lo sabremos. |
| 7 | 3. Experimentos: baseline y modelos con… | Practica `subplots`, `sort_values`, `barh`, `axvline` y más (sección «Ejercicio 3»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `ENTORNO` | `{"python": sys.version.split()[0], "numpy": np.__version_…` | 3 |
| `reservas` | `pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=[…` | 5 |
| `X` | `reservas.drop(columns=["id_reserva", "fecha_reserva", "fe…` | 5 |
| `y` | `reservas["cancelada"]` | 5 |
| `DATOS_HASH` | `hashlib.md5(pd.util.hash_pandas_object(reservas, index=Tr…` | 5 |
| `categoricas` | `X.select_dtypes("object").columns.tolist()` | 5 |
| `cv` | `StratifiedKFold(n_splits=5, shuffle=True, random_state=SE…` | 5 |
| `t` | `tabla.sort_values("valor_cv")` | 7 |
| `X_fuga` | `X_ent.copy()` | 9 |
| `mejor_sin_fuga` | `pd.read_csv(RUTA_REGISTRO).query("modelo != 'LogisticaCon…` | 9 |
| `USAR_MLFLOW` | `False` | 11 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `fijar_semillas` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `registrar` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `crear_pipeline` | Función definida en el cuaderno. |
| `experimento` | Evalúa con CV (AUC), mide el tiempo y registra la fila. Devuelve (media, desviación). |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 9 |
| `axvline` | Dibuja una línea vertical de referencia. | 7 |
| `barh` | Dibuja barras horizontales. | 7 |
| `columns` | Nombres de las columnas. | 5 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 5 |
| `copy` | Hace una copia independiente (si cambias la copia, el original no cambia). | 9 |
| `cross_val_score` | Evalúa el modelo con validación cruzada (varias particiones). | 5 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 5 |
| `drop` | Quita columnas o filas. | 5 |
| `dt` | Da acceso a las operaciones de fecha sobre una columna. | 5 |
| `DummyClassifier` | Modelo «tonto» de referencia (por ejemplo, siempre la clase más común). | 5 |
| `dumps` | Convierte datos de Python en texto JSON. | 3 |
| `float` | Convierte un valor en número decimal. | 11 |
| `hash_pandas_object` | Calcula una huella numérica de cada fila de la tabla; sirve para saber si los datos han cambiado. | 5 |
| `hexdigest` | Devuelve la huella calculada como un texto corto de letras y números. | 5 |
| `legend` | Muestra la leyenda del gráfico. | 7 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 9 |
| `log_metric` | MLflow: guarda una medida de la prueba (por ejemplo, el AUC). | 11 |
| `log_params` | MLflow: guarda los ajustes de la prueba (hiperparámetros). | 11 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 5, 9 |
| `max` | Devuelve el valor más grande. | 9 |
| `md5` | Convierte unos datos en una huella corta; si los datos cambian, la huella cambia. | 5 |
| `mean` | Calcula la media. | 5 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 5 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 5 |
| `print` | Muestra un valor por pantalla. | 3, 5, 9, 11 |
| `query` | Filtra filas con una condición escrita como texto. | 9 |
| `random` | Número aleatorio entre 0 y 1. | 9 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 5, 9 |
| `select_dtypes` | Selecciona las columnas de un tipo (numéricas, de texto…). | 5 |
| `set_experiment` | MLflow: elige (o crea) el experimento al que pertenecen las pruebas. | 11 |
| `set_tag` | MLflow: añade una etiqueta a la prueba para encontrarla luego. | 11 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_title` | Pone el título de un gráfico. | 7 |
| `set_tracking_uri` | MLflow: indica dónde se guardan los experimentos (aquí, una carpeta local). | 11 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 7 |
| `set_xlim` | Fija el rango del eje horizontal. | 7 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 5 |
| `show` | Muestra el gráfico. | 7 |
| `sort_values` | Ordena la tabla por una o varias columnas. | 7 |
| `split` | Parte un texto en trozos por un separador. | 3 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 5 |
| `start_run` | MLflow: abre una prueba nueva; todo lo que se anote después se guarda en ella. | 11 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 5 |
| `StratifiedKFold` | Crea particiones de validación cruzada que mantienen la proporción de clases. | 5 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 7 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 7 |
| `time` | Devuelve la hora actual en segundos (sirve para medir cuánto tarda algo). | 5 |
| `tobytes` | Convierte los números de una tabla en una secuencia de bytes, que es lo que necesita `md5`. | 5 |
| `tolist` | Convierte un array o una columna en una lista de Python. | 5 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 5 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 5 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_theme`.

```python
import os, sys, time, json, random, hashlib
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score

sns.set_theme(style="whitegrid")
```

**Qué hace cada línea:**

- `import os, sys, time, json, random, hashlib` → Trae `os`, `sys`, `time`, `json`, `random`, `hashlib` para poder usarlo.
- `from datetime import datetime` → Trae `datetime` de `datetime` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `import sklearn` → Trae `sklearn` para poder usarlo.
- `from sklearn.model_selection import train_test_split, StratifiedKFold, cros…` → Trae `train_test_split`, `StratifiedKFold`, `cross_val_score` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- … y 7 más con las mismas ideas.

### Celda 2 · 1. Reproducibilidad: semillas y versiones · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 3 · 1. Reproducibilidad: semillas y versiones · 🏫

**Qué hace:** Ficha del entorno: cópiala en la memoria técnica y en el README del equipo.

```python
# Ficha del entorno: cópiala en la memoria técnica y en el README del equipo
ENTORNO = {"python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__, "scikit-learn": sklearn.__version__}
print(json.dumps(ENTORNO, indent=2))
```

**Qué hace cada línea:**

- `ENTORNO = {"python": sys.version.split()[0], "numpy": np.__version__, "pand…` → Guarda en `ENTORNO` el resultado. `split`: parte un texto en trozos por un separador.
- `print(json.dumps(ENTORNO, indent=2))` → `print`: muestra un valor por pantalla; `dumps`: convierte datos de Python en texto JSON.

### Celda 4 · 2. El registro de experimentos: una fila por pr… · 🏫 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 3. Experimentos: baseline y modelos con validac… · 🏫

**Qué hace:** huella de los datos: si alguien cambia el CSV, el hash cambia y lo sabremos.

```python
reservas = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
reservas["mes_llegada"] = reservas["fecha_llegada"].dt.month
X = reservas.drop(columns=["id_reserva", "fecha_reserva", "fecha_llegada", "cancelada"])
y = reservas["cancelada"]
X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEMILLA)

# huella de los datos: si alguien cambia el CSV, el hash cambia y lo sabremos
DATOS_HASH = hashlib.md5(pd.util.hash_pandas_object(reservas, index=True).values.tobytes()).hexdigest()[:8]
print("Huella de los datos:", DATOS_HASH, "· entrenamiento:", X_ent.shape, "· test (sin tocar):", X_test.shape)

categoricas = X.select_dtypes("object").columns.tolist()
def crear_pipeline(estimador, columnas):
    numericas = [c for c in columnas if c not in categoricas]
    prep = ColumnTransformer([("num", StandardScaler(), numericas), ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas)])
    return Pipeline([("prep", prep), ("m", estimador)])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMILLA)

def experimento(nombre, estimador, hiperparametros, responsable="equipo", notas="", Xd=None):
    """Evalúa con CV (AUC), mide el tiempo y registra la fila. Devuelve (media, desviación)."""
    Xd = X_ent if Xd is None else Xd
    t0 = time.time()
    puntuaciones = cross_val_score(crear_pipeline(estimador, Xd.columns), Xd, y_ent, cv=cv, scoring="roc_auc")
    registrar(responsable, nombre, hiperparametros, DATOS_HASH, SEMILLA, "AUC", puntuaciones.mean(), puntuaciones.std(), time.time() - t0, notas)
    return puntuaciones.mean(), puntuaciones.std()

print("Baseline (predice la clase más frecuente):", experimento("Baseline", DummyClassifier(strategy="prior"), {"strategy": "prior"}, notas="referencia mínima"))
print("Regresión logística:", experimento("RegresionLogistica", LogisticRegression(max_iter=2000), {"C": 1.0}))
```

**Qué hace cada línea:**

- `reservas = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_…` → Guarda en `reservas` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `reservas["mes_llegada"] = reservas["fecha_llegada"].dt.month` → Guarda en `reservas["mes_llegada"]` el resultado. `dt`: da acceso a las operaciones de fecha sobre una columna.
- `X = reservas.drop(columns=["id_reserva", "fecha_reserva", "fecha_llegada",…` → Guarda en `X` el resultado. `drop`: quita columnas o filas.
- `y = reservas["cancelada"]` → Guarda el valor en `y`.
- `X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.2, strati…` → Guarda en `X_ent, X_test, y_ent, y…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `DATOS_HASH = hashlib.md5(pd.util.hash_pandas_object(reservas, index=True).v…` → Guarda en `DATOS_HASH` el resultado. `hexdigest`: devuelve la huella calculada como un texto corto de letras y números; `md5`: convierte unos datos en una huella corta; si los datos cambian, la huella cambia; `tobytes`: convierte los números de una tabla en una secuencia de bytes, que es lo que necesita `md5`.
- `print("Huella de los datos:", DATOS_HASH, "· entrenamiento:", X_ent.shape,…` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- `categoricas = X.select_dtypes("object").columns.tolist()` → Guarda en `categoricas` el resultado. `tolist`: convierte un array o una columna en una lista de Python; `columns`: nombres de las columnas; `select_dtypes`: selecciona las columnas de un tipo (numéricas, de texto…).
- `def crear_pipeline(estimador, columnas):` → Define la función `crear_pipeline`: Función definida en el cuaderno.
- … y 4 más con las mismas ideas.

### Celda 6 · 3. Experimentos: baseline y modelos con validac… · 🏫 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 3. Experimentos: baseline y modelos con validac… · 🏫

**Qué hace:** Practica `subplots`, `sort_values`, `barh`, `axvline` y más (sección «Ejercicio 3»).

```python
fig, ax = plt.subplots(figsize=(7, 3.5))
t = tabla.sort_values("valor_cv")
ax.barh(t["modelo"], t["valor_cv"], xerr=t["desv_cv"], color="tab:blue", capsize=4)
ax.axvline(0.5, color="gray", linestyle="--", label="Azar (AUC 0,5)")
ax.set_xlim(0.4, 0.85); ax.set_xlabel("AUC medio en validación cruzada (± desviación)")
ax.set_title("Comparativa de modelos (validación cruzada, sin usar el test)"); ax.legend(loc="lower right")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ax = plt.subplots(figsize=(7, 3.5))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `t = tabla.sort_values("valor_cv")` → Guarda en `t` el resultado. `sort_values`: ordena la tabla por una o varias columnas.
- `ax.barh(t["modelo"], t["valor_cv"], xerr=t["desv_cv"], color="tab:blue", ca…` → `barh`: dibuja barras horizontales.
- `ax.axvline(0.5, color="gray", linestyle="--", label="Azar (AUC 0,5)")` → `axvline`: dibuja una línea vertical de referencia.
- `ax.set_xlim(0.4, 0.85); ax.set_xlabel("AUC medio en validación cruzada (± d…` → `set_xlim`: fija el rango del eje horizontal.
- `ax.set_xlim(0.4, 0.85); ax.set_xlabel("AUC medio en validación cruzada (± d…` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_title("Comparativa de modelos (validación cruzada, sin usar el test)…` → `set_title`: pone el título de un gráfico.
- `ax.set_title("Comparativa de modelos (validación cruzada, sin usar el test)…` → `legend`: muestra la leyenda del gráfico.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- … y 1 más con las mismas ideas.

### Celda 8 · 4. Ajuste de hiperparámetros, también registrado · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5. Alarma: una métrica demasiado buena (fuga de… · 🏠

**Qué hace:** Practica `copy`, `astype`, `max`, `LogisticRegression` y más (sección «5. Alarma: una métrica demasiado buena…»).

```python
X_fuga = X_ent.copy()
X_fuga["reembolso_emitido"] = ((y_ent == 1) & (rng.random(len(y_ent)) < 0.9)).astype(int)
m, d = experimento("LogisticaConFuga", LogisticRegression(max_iter=2000), {"C": 1.0}, notas="ALARMA: AUC sospechosamente alto (fuga: reembolso_emitido)", Xd=X_fuga)
mejor_sin_fuga = pd.read_csv(RUTA_REGISTRO).query("modelo != 'LogisticaConFuga'")["valor_cv"].max()
print(f"AUC con la variable con fuga: {m:.3f} (frente a {mejor_sin_fuga:.3f} del mejor modelo sin ella) → ¡descártala y anótalo en el registro!")
```

**Qué hace cada línea:**

- `X_fuga = X_ent.copy()` → Guarda en `X_fuga` el resultado. `copy`: hace una copia independiente (si cambias la copia, el original no cambia).
- `X_fuga["reembolso_emitido"] = ((y_ent == 1) & (rng.random(len(y_ent)) < 0.9…` → Guarda en `X_fuga["reembolso_emiti…` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `random`: número aleatorio entre 0 y 1; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `m, d = experimento("LogisticaConFuga", LogisticRegression(max_iter=2000), {…` → Guarda en `m, d` el resultado. `experimento`: evalúa con CV (AUC), mide el tiempo y registra la fila. Devuelve (media, desviación); `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- `mejor_sin_fuga = pd.read_csv(RUTA_REGISTRO).query("modelo != 'LogisticaConF…` → Guarda en `mejor_sin_fuga` el resultado. `max`: devuelve el valor más grande; `query`: filtra filas con una condición escrita como texto; `read_csv`: lee un fichero CSV y lo convierte en una tabla.
- `print(f"AUC con la variable con fuga: {m:.3f} (frente a {mejor_sin_fuga:.3f…` → `print`: muestra un valor por pantalla.

### Celda 10 · 6. Evaluar el candidato en el test, una sola vez · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 7. (Opcional) MLflow en local · 🏠

**Qué hace:** %pip install -q mlflow # <- descomenta en Colab; en local: pip install mlflow.

```python
USAR_MLFLOW = False        # OPCIONAL: cámbialo a True solo si tu equipo quiere probar MLflow (necesita internet para instalarlo)

if USAR_MLFLOW:
    # %pip install -q mlflow       # <- descomenta en Colab; en local: pip install mlflow
    import mlflow
    try:
        import sqlalchemy                                  # instalado con MLflow completo: usamos la base de datos local
        URI = "sqlite:///mlflow.db"
    except ImportError:                                    # instalación ligera: carpeta local mlruns/
        os.environ["MLFLOW_ALLOW_FILE_STORE"] = "true"
        URI = "file:./mlruns"
    mlflow.set_tracking_uri(URI)
    mlflow.set_experiment("turisdata_cancelaciones")
    with mlflow.start_run(run_name="RandomForest_demo"):
        mlflow.log_params({"n_estimators": 200, "min_samples_leaf": 5, "semilla": SEMILLA})
        mlflow.log_metric("auc_cv", float(fila["valor_cv"]))
        mlflow.log_metric("auc_test", float(auc_test))
        mlflow.set_tag("datos_hash", DATOS_HASH)
    print(f"Registrado en {URI}. Para verlo, en una terminal:  mlflow ui --backend-store-uri {URI}  y visita http://127.0.0.1:5000")
else:
    print("MLflow desactivado (opcional). El registro en CSV ya cumple lo que pide la rúbrica.")
```

**Qué hace cada línea:**

- `USAR_MLFLOW = False # OPCIONAL: cámbialo a True solo si tu equipo quiere pr…` → Guarda el valor en `USAR_MLFLOW`.
- `if USAR_MLFLOW:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `set_tracking_uri`: MLflow: indica dónde se guardan los experimentos (aquí, una carpeta local); `set_experiment`: MLflow: elige (o crea) el experimento al que pertenecen las pruebas; `start_run`: MLflow: abre una prueba nueva; todo lo que se anote después se guarda en ella.

---
*Generado a partir de `laboratorios/fuentes/S15_01_seguimiento_experimentos.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
