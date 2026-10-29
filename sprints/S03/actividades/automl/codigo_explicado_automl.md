# Solucionario del código · AutoML (cuaderno `S3.5_lab_autogluon`)

> **Para quién:** alumnado de IFCD107. **Qué es:** el cuaderno de AutoML **explicado línea a línea**. Cada celda que habéis ejecutado, con su código, **qué hace cada línea**, **qué debe salir** y una pequeña prueba para comprobar que lo habéis entendido. No hace falta saber programar: está pensado para leerlo **mientras** o **después** de ejecutar cada celda.
> Va con la [guía en parejas](guia_automl_en_parejas.md), el [listado de pasos](listado_pasos_automl.md) y el [solucionario de las preguntas](soluciones_automl_paso_a_paso.md) (ese responde a *«¿qué significa este resultado?»*; este responde a *«¿qué hace este código?»*).

## Cómo usar este documento

1. **Ejecutad la celda primero** y mirad qué sale.
2. Buscad aquí **el mismo paso** (los títulos coinciden con los del cuaderno: *Instalación, 0, 1, 2… 11*).
3. Leed **«Qué hace cada línea»** con el código delante. Si una palabra os suena rara, está en el [mini-glosario de Python](#1-el-python-que-aparece-mini-glosario).
4. Haced **«Probad vosotros»**: cambiáis una cosa y comprobáis si pasa lo que esperabais. **Es la mejor manera de entender código.**
5. Al terminar, la [comprobación final](#comprobación-final-siete-preguntas-de-código) tiene siete preguntas con su respuesta.

**Cómo se lee una línea de código.** Casi todo sigue la misma forma: `resultado = objeto.acción(opciones)`. Se lee de **derecha a izquierda**: *«coge este objeto, hazle esta acción con estas opciones, y guarda lo que salga en `resultado`»*.

**Los datos:** [`reservas_turisdata.csv`](../../Reto_S03/laboratorio_automl/reservas_turisdata.csv), 6.000 reservas y 18 columnas, **sintéticas**. Las columnas están en el [esquema de turisdata.db](../esquema_turisdata/esquema_turisdata.md). Las cifras que salen aquí son de una ejecución real; las vuestras pueden variar un poco.

---

## 1. El Python que aparece (mini-glosario)

| Palabra | Qué es, en sencillo | Ejemplo del cuaderno |
|---|---|---|
| **Variable** | Un nombre que guarda un valor. Se crea con `=` | `OBJETIVO = "cancelada"` |
| **Constante** | Una variable que no se piensa cambiar; por costumbre, en MAYÚSCULAS | `LIMITE_TIEMPO = 120` |
| **Texto** | Palabras entre comillas | `"fecha_reserva"` |
| **Lista** | Varios valores seguidos, entre corchetes `[ ]` | `["fecha_reserva", "fecha_llegada"]` |
| **Tupla** | Como una lista, entre paréntesis `( )` | `(0.5, 0.3)` |
| **Diccionario** | Parejas *nombre: valor*, entre llaves `{ }` | `{"umbral": 0.5, "alertas": 540}` |
| **DataFrame** | Una **tabla** de pandas (filas y columnas), como una hoja de cálculo | `datos`, `entrenamiento`, `prueba` |
| **Columna** | Se saca con corchetes y su nombre | `datos["canal"]` |
| **Método** | Una acción que sabe hacer un objeto; lleva punto y paréntesis | `datos.head()` |
| **Función** | Un bloque de código con nombre que se define con `def` y se **llama** después | `predecir_cancelacion(ejemplo)` |
| **Bucle `for`** | Repite un bloque para cada valor de una lista | `for u in (0.1, 0.2, 0.3):` |
| **f-string** | Un texto con `f` delante que mete valores entre `{ }` | `f"Tiempo: {segundos:.0f} s"` |
| **`import`** | Trae una librería para usarla | `import pandas as pd` |
| **Comentario** | Texto tras `#` que Python **ignora**; es para las personas | `# probabilidad de cancelar` |
| **`!` al principio** | Solo en Colab: la celda ejecuta un comando del sistema, no Python | `!pip install ...` |

**Dos librerías que salen siempre:** `pandas` (se importa como `pd`) trabaja con **tablas**; `numpy` (como `np`) trabaja con **números y listas de números**.

---

## 2. Mapa: qué guarda cada variable

El cuaderno va **pasando datos de una variable a otra**. Si os perdéis, volved aquí.

```
reservas_turisdata.csv
        │  (paso 1: pd.read_csv)
        ▼
     datos ───────── 6.000 reservas, 18 columnas
        │  (paso 3: sort_values + iloc + drop)
        ├──► entrenamiento ─ 4.800 reservas más antiguas ─┐
        └──► prueba ──────── 1.200 reservas más recientes  │
                                                           │ (paso 4: .fit)
                                                           ▼
                                                      predictor ── el modelo entrenado
                                                           │
        prueba (sin la columna cancelada) ──► .predict_proba ──► prob ── probabilidad de cada reserva
        prueba[OBJETIVO] ───────────────────────────────────────► y_real ─ lo que pasó de verdad
                                       prob + y_real ──► métricas (pasos 6 y 6b)

   predictor.save() ──► carpeta modelo_cancelaciones ──► predictor_recargado ──► predecir_cancelacion ──► API
```

| Variable | Qué contiene | Se crea en |
|---|---|---|
| `datos` | Las 6.000 reservas (tabla) | Paso 1 |
| `entrenamiento` | Las 4.800 reservas más antiguas, **con** la respuesta (`cancelada`) para que el modelo aprenda | Paso 3 |
| `prueba` | Las 1.200 más recientes; el modelo **no las ve** al entrenar | Paso 3 |
| `predictor` | El modelo entrenado por AutoGluon | Paso 4 |
| `clasificacion` | La tabla de modelos candidatos (leaderboard) | Paso 5 |
| `y_real` | La columna `cancelada` de la prueba: **lo que pasó de verdad** | Paso 6 |
| `prob` | La **probabilidad de cancelar** que el modelo da a cada reserva de la prueba | Paso 6 |
| `pred` | La **decisión** (1 = alerta, 0 = no alerta) para un umbral | Pasos 6 y 6b |
| `tabla_costes` | El coste de cada umbral | Paso 6b |
| `importancia` | Cuánto pesa cada columna | Paso 7 |
| `predictor_recargado` | El mismo modelo, cargado desde la carpeta | Paso 8 |
| `api`, `cliente` | La API y el «cliente de pruebas» que la llama | Paso 10 |

---

## Instalación · traer las piezas que faltan

**Para qué sirve:** Colab no trae AutoGluon. Esta celda lo instala (una sola vez por sesión).

```python
!pip install -q "autogluon.tabular[lightgbm,xgboost,catboost]" fastapi httpx
```

**Qué hace cada línea:**

| Trozo | Qué hace |
|---|---|
| `!` | La celda ejecuta un **comando del sistema**, no código Python |
| `pip install` | El instalador de librerías de Python |
| `-q` | *quiet*: que no llene la pantalla de mensajes |
| `"autogluon.tabular[...]"` | **AutoGluon para tablas.** Entre corchetes van tres librerías de modelos que instala a la vez: `lightgbm`, `xgboost` y `catboost`. Las **comillas** hacen falta por los corchetes |
| `fastapi` | La librería para crear la **API** (paso 10) |
| `httpx` | La necesita FastAPI para poder **probar la API desde el propio cuaderno** (`TestClient`) |

**Qué debe salir:** casi nada (por el `-q`). Tarda **2 o 3 minutos**. Si Colab pide **reiniciar el entorno**, aceptad y seguid desde el paso 0.

**Probad vosotros:** quitad el `-q` y ejecutad otra vez. ¿Qué cambia? *Sale mucho más texto (una línea por paquete). Funciona igual; solo es más ruidoso.*

**Por qué hay que volver a ejecutarla a veces:** el entorno de Colab es **temporal**. Si se desconecta o lo eliminan, **se pierde lo instalado**. Si solo reiniciáis la sesión, se pierden las **variables** (por eso hay que ejecutar otra vez desde el paso 0), pero no la instalación.

---

## Paso 0 · Configuración

**Para qué sirve:** preparar las herramientas y los **ajustes** que usa el resto del cuaderno, en un solo sitio. Si queréis cambiar algo (por ejemplo, el tiempo de entrenamiento), se hace **aquí**.

```python
# Descarga de archivos del laboratorio (si no están ya en la carpeta de trabajo)
import os, urllib.request
BASE_URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/sprints/S03/Reto_S03/laboratorio_automl/"
def archivo(nombre):
    """Devuelve el nombre del archivo; si no está en esta carpeta, lo descarga del repositorio del curso."""
    if not os.path.exists(nombre):
        urllib.request.urlretrieve(BASE_URL + nombre, nombre)
    return nombre

import time

import numpy as np
import pandas as pd

RUTA_DATOS = archivo("reservas_turisdata.csv")
LIMITE_TIEMPO = 120   # segundos de entrenamiento (poned 15 para un ensayo rápido)
CARPETA_MODELO = "modelo_cancelaciones"
OBJETIVO = "cancelada"
SEMILLA = 42
np.random.seed(SEMILLA)
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `import os, urllib.request` | Trae dos herramientas que ya vienen con Python: `os` (trabajar con archivos y carpetas) y `urllib.request` (**descargar** cosas de internet) |
| `BASE_URL = "..."` | La dirección de internet donde están los archivos del laboratorio, en GitHub |
| `def archivo(nombre):` | **Define una función** llamada `archivo` que recibe un nombre de archivo. Define = «aquí explico cómo se hace»; todavía no se ejecuta |
| `"""Devuelve..."""` | Un texto explicativo de lo que hace la función (no hace nada, es documentación) |
| `if not os.path.exists(nombre):` | *«Si el archivo **no existe** en esta carpeta…»* |
| `urllib.request.urlretrieve(BASE_URL + nombre, nombre)` | *«…descárgalo de esa dirección (`BASE_URL` + el nombre) y guárdalo con ese nombre»* |
| `return nombre` | La función **devuelve** el nombre del archivo, para que quien la llame lo pueda usar |
| `import time` | Para medir **cuánto tarda** el entrenamiento (paso 4) |
| `import numpy as np` | `numpy`, con el apodo `np` |
| `import pandas as pd` | `pandas` (tablas), con el apodo `pd` |
| `RUTA_DATOS = archivo("reservas_turisdata.csv")` | **Llama** a la función: descarga el CSV (si no está) y guarda su nombre en `RUTA_DATOS` |
| `LIMITE_TIEMPO = 120` | Máximo de **segundos** de entrenamiento |
| `CARPETA_MODELO = "modelo_cancelaciones"` | Nombre de la carpeta donde se guardará el modelo |
| `OBJETIVO = "cancelada"` | La columna que queremos **predecir** |
| `SEMILLA = 42` | Un número para que el azar sea **repetible** |
| `np.random.seed(SEMILLA)` | Fija el generador de números aleatorios de numpy. AutoGluon además trae su propia semilla fija, por eso **dos ejecuciones dan casi lo mismo** |

**Qué debe salir:** nada. Una celda sin `print` no escribe nada, pero **es imprescindible**: si la saltáis, el resto falla con `NameError`.

**Probad vosotros:**
1. Subid vuestro propio `reservas_turisdata.csv` al panel de archivos de Colab y ejecutad la celda. ¿Lo descarga otra vez? *No: `os.path.exists` ve que ya está y se salta la descarga.*
2. Poned `LIMITE_TIEMPO = 15` y ejecutad **desde esta celda** en adelante. El entrenamiento será más corto.

---

## Paso 1 · Cargar los datos

**Para qué sirve:** leer el CSV y comprobar que es el que esperamos.

```python
# Si no tienes el CSV, genéralo con:  python generar_reservas_turisdata.py
datos = pd.read_csv(RUTA_DATOS, parse_dates=["fecha_reserva", "fecha_llegada"])
print(datos.shape)
print(datos.head())
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `datos = pd.read_csv(RUTA_DATOS, ...)` | Lee el archivo CSV y lo convierte en una **tabla** (`DataFrame`) llamada `datos` |
| `parse_dates=["fecha_reserva", "fecha_llegada"]` | Le dice que esas dos columnas son **fechas**, no texto. Con fechas de verdad se puede **ordenar**, **restar** y pedir la más antigua (`.min()`) y la más reciente (`.max()`) |
| `print(datos.shape)` | `shape` es el **tamaño** de la tabla: *(filas, columnas)* |
| `print(datos.head())` | `head()` enseña las **5 primeras filas** |

**Qué debe salir:** `(6000, 18)` y una tabla de 5 filas con las columnas `id_reserva`, `fecha_reserva`, `fecha_llegada`, `antelacion_dias`… hasta `cancelada`. Si Python pone `...` en medio de la tabla, es solo que no cabe en pantalla.

**Probad vosotros:** cambiad `datos.head()` por `datos.head(10)` y por `datos.tail()`. *El primero enseña 10 filas; el segundo, las 5 últimas.*

---

## Paso 2 · Explorar y mirar la calidad del dato

**Para qué sirve:** conocer los datos **antes** de entrenar: de qué tipo es cada columna, qué falta y cuántas reservas se cancelan.

```python
print("\nTipos de dato:\n", datos.dtypes)
print("\nNulos por columna:\n", datos.isna().sum()[datos.isna().sum() > 0])
print("\nProporción de cancelaciones:", round(datos[OBJETIVO].mean(), 3))
print("\nResumen numérico:\n", datos.describe().T[["mean", "std", "min", "max"]])
# Preguntas para el informe:
#  - ¿Está desbalanceada la clase objetivo? ¿Qué métrica conviene?
#  - ¿Qué columnas podrían provocar fuga de datos (información posterior al desenlace)?
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `print("\nTipos de dato:\n", datos.dtypes)` | `dtypes` = **tipo** de cada columna: números enteros, decimales, texto, fecha. `\n` es un **salto de línea** para que la salida no quede pegada. `print` con una coma escribe los dos trozos seguidos |
| `datos.isna().sum()[datos.isna().sum() > 0]` | Se lee **de dentro hacia fuera** (ver abajo). Resultado: solo las columnas con **datos que faltan** |
| `round(datos[OBJETIVO].mean(), 3)` | `datos[OBJETIVO]` es la columna `cancelada` (de 0 y 1). Su **media** es la **proporción de unos**: el % de reservas canceladas. `round(…, 3)` deja 3 decimales |
| `datos.describe().T[["mean", "std", "min", "max"]]` | `describe()` calcula estadísticas de cada columna numérica. `.T` **gira** la tabla (filas ↔ columnas) para leerla mejor. Los corchetes con la lista se quedan **solo con 4 columnas**: media, desviación, mínimo y máximo |
| `# Preguntas para el informe: …` | Comentarios: no se ejecutan; son las preguntas que hay que contestar |

**Cómo se lee `datos.isna().sum()[datos.isna().sum() > 0]`:**

1. `datos.isna()` → una tabla igual de grande con `True` donde falta un dato y `False` donde no.
2. `.sum()` → **cuenta** los `True` de cada columna (en Python, `True` vale 1).
3. `... > 0` → para cada columna, ¿hay más de 0 vacíos? Da `True` o `False`.
4. `[ ... ]` → **filtra**: se queda solo con las columnas en las que salió `True`.

**Qué debe salir:**
- Las fechas aparecen como `datetime64`.
- Nulos: **solo `pais_origen`, con 138**.
- `Proporción de cancelaciones: 0.459` (el 45,9 %).
- Una tabla con la media, desviación, mínimo y máximo de cada columna numérica.

**Probad vosotros:** en una celda nueva escribid `datos["canal"].value_counts()`. *Cuenta las reservas de cada canal: `web_intermediaria` 3.020, `directo` 1.462, `agencia` 1.190 y `empresa` 328 (suman 6.000).*

---

## Paso 3 · Partición temporal: pasado para entrenar, futuro para probar

**Para qué sirve:** separar las reservas en dos grupos **por fecha**. Con el grupo antiguo se entrena el modelo; con el reciente se comprueba si acierta **de verdad**.

```python
datos = datos.sort_values("fecha_reserva").reset_index(drop=True)
corte = int(len(datos) * 0.8)
entrenamiento = datos.iloc[:corte].drop(columns=["id_reserva"])
prueba = datos.iloc[corte:].drop(columns=["id_reserva"])
print(f"\nEntrenamiento: {len(entrenamiento)} filas ({entrenamiento.fecha_reserva.min().date()} a "
      f"{entrenamiento.fecha_reserva.max().date()})")
print(f"Prueba:        {len(prueba)} filas ({prueba.fecha_reserva.min().date()} a "
      f"{prueba.fecha_reserva.max().date()})")
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `datos = datos.sort_values("fecha_reserva").reset_index(drop=True)` | **Ordena** la tabla de la reserva más antigua a la más reciente. `reset_index(drop=True)` vuelve a numerar las filas 0, 1, 2… (y tira la numeración vieja) |
| `corte = int(len(datos) * 0.8)` | `len(datos)` = 6.000 filas. `× 0.8` = 4.800,0. `int(…)` lo convierte en un **entero**: 4.800. Es el **punto de corte** |
| `entrenamiento = datos.iloc[:corte]…` | `iloc` selecciona **por posición**. `[:corte]` significa *«desde el principio hasta la fila 4.800»*: las **4.800 más antiguas** |
| `prueba = datos.iloc[corte:]…` | `[corte:]` significa *«desde la fila 4.800 hasta el final»*: las **1.200 más recientes** |
| `.drop(columns=["id_reserva"])` | **Quita** la columna `id_reserva` (un número de serie que no explica nada). Devuelve una tabla nueva |
| `print(f"…{len(entrenamiento)}…")` | Un **f-string**: lo que va entre `{ }` se sustituye por su valor |
| `entrenamiento.fecha_reserva.min().date()` | La fecha de reserva **más antigua** del grupo; `.date()` quita la hora |

**Qué debe salir:**

```
Entrenamiento: 4800 filas (2024-01-01 a 2025-08-06)
Prueba:        1200 filas (2025-08-06 a 2025-12-30)
```

**Fijaos:** las dos tablas **conservan** la columna `cancelada`. En `entrenamiento` hace falta, porque el modelo aprende de ella. En `prueba` también, para **comparar** después lo que el modelo diga con lo que pasó. Al predecir (paso 6) se la **taparemos**.

**Probad vosotros:** en una celda nueva, `len(entrenamiento) + len(prueba)`. *Da 6.000: no se ha perdido ninguna reserva.* Después quitad la primera línea (`sort_values`) y volved a mirar las fechas: *el «futuro» y el «pasado» salen mezclados* (es el error del que avisa la guía).

---

## Paso 4 · Entrenar con AutoML

**Para qué sirve:** es **el paso central**. AutoGluon prueba varios modelos con las reservas de `entrenamiento` y se queda con el mejor.

```python
from autogluon.tabular import TabularPredictor

inicio = time.time()
predictor = TabularPredictor(
    label=OBJETIVO,
    problem_type="binary",
    eval_metric="roc_auc",
    path=CARPETA_MODELO,
).fit(
    train_data=entrenamiento,
    time_limit=LIMITE_TIEMPO,
    presets="medium_quality",
)
tiempo_entrenamiento = time.time() - inicio
print(f"\nTiempo de entrenamiento: {tiempo_entrenamiento:.0f} s")
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `from autogluon.tabular import TabularPredictor` | Trae de AutoGluon la herramienta `TabularPredictor`, la que entrena modelos para tablas |
| `inicio = time.time()` | Apunta **la hora actual** (como pulsar el cronómetro) |
| `TabularPredictor(` … `)` | **Crea** el predictor y le dice cómo trabajar. Todavía **no entrena** |
| `label=OBJETIVO` | La columna que hay que predecir: `cancelada` |
| `problem_type="binary"` | Solo hay **dos** respuestas posibles: cancela o no cancela |
| `eval_metric="roc_auc"` | La «nota» con la que AutoGluon **elige el mejor modelo** (el AUC) |
| `path=CARPETA_MODELO` | La carpeta donde **guarda** lo que entrena |
| `.fit(` … `)` | **Aquí empieza el entrenamiento.** `fit` significa *ajustar*. El punto antes de `fit` significa que se le pide al predictor que acabamos de crear |
| `train_data=entrenamiento` | Las reservas con las que aprende |
| `time_limit=LIMITE_TIEMPO` | Máximo de segundos (120). Si acaba antes, se para antes |
| `presets="medium_quality"` | Un ajuste que equilibra **calidad y rapidez** |
| `predictor = …` | Guarda el predictor entrenado en la variable `predictor`. Es el **modelo** que usaremos en el resto del cuaderno |
| `time.time() - inicio` | Hora de ahora **menos** la de antes: los **segundos** que ha tardado |
| `{tiempo_entrenamiento:.0f}` | Dentro de un f-string, `:.0f` significa *«con 0 decimales»* |

**Qué pasa por dentro** (no lo escribís vosotros, lo hace AutoGluon):
1. Se **guarda una parte** de las reservas de entrenamiento para validar.
2. Entrena **varios modelos** distintos (LightGBM, CatBoost, XGBoost, Random Forest, Extra Trees…) y puntúa cada uno con la parte guardada.
3. Construye un **ensamblado** (`WeightedEnsemble`): un modelo que **combina** a los mejores y reparte el voto entre ellos.

**Qué debe salir:** **mucho texto** (una línea por cada modelo que prueba; es normal) y al final `Best model: WeightedEnsemble_L2` y `Tiempo de entrenamiento: 36 s` (entre 20 y 90). Si salen `Warning` o `Failed to import torch…`, **no son errores**: AutoGluon se salta ese modelo y sigue.

**Por qué el cuaderno se llama «AutoML»:** vosotros **no elegís** el algoritmo. Elegís **qué predecir** (`label`), **con qué nota** (`eval_metric`), **cuánto tiempo** (`time_limit`) y **con qué datos** (`train_data`).

**Probad vosotros:** poned `LIMITE_TIEMPO = 15` en el paso 0 y volved a ejecutar los pasos 0, 3 y 4. *Tarda menos; en nuestras pruebas el mejor modelo y sus notas salieron iguales.*

---

## Paso 5 · Leaderboard: la tabla de candidatos

**Para qué sirve:** ver **todos los modelos** que ha probado, comparados con las reservas de prueba.

```python
clasificacion = predictor.leaderboard(prueba, silent=True)
print(clasificacion[["model", "score_test", "score_val", "fit_time"]].head(10))
# Preguntas: ¿el mejor modelo es un ensamblado? ¿Cuánto tarda cada uno? ¿Merece la pena el coste de cómputo?
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `predictor.leaderboard(prueba, silent=True)` | Pide al predictor la **tabla de modelos**, puntuándolos también con `prueba` (por eso aparece `score_test`). `silent=True` evita que imprima por su cuenta una tabla enorme |
| `clasificacion = …` | La guarda en una variable |
| `clasificacion[["model", "score_test", "score_val", "fit_time"]]` | Corchetes con **una lista de nombres**: se queda solo con esas 4 columnas |
| `.head(10)` | Y solo con las **10 primeras filas** (los 10 mejores) |

**Qué significa cada columna:**

| Columna | Qué es |
|---|---|
| `model` | Nombre del modelo |
| `score_test` | AUC con las reservas de **prueba** (el futuro): **la nota que vale** |
| `score_val` | AUC con la parte que AutoGluon guardó **del entrenamiento**: más optimista |
| `fit_time` | Segundos que tardó en entrenar ese modelo |

**Qué debe salir:** una tabla de unos 10 modelos. En nuestra ejecución, `WeightedEnsemble_L2` arriba con `score_test` ≈ 0,722 y `score_val` ≈ 0,779; después `CatBoost` (0,719), `XGBoost` (0,719) y `LightGBMXT` (0,717). Fijaos en la columna `fit_time`: `XGBoost` entrena en menos de 1 segundo.

**Probad vosotros:** cambiad `.head(10)` por `.head(3)`. *Salen solo los tres primeros.* Y cambiad `"fit_time"` por `"pred_time_val"`: *aparece otra columna, la que mide cuánto tarda en predecir.*

---

## Paso 6 · Evaluar el modelo con dos umbrales

**Para qué sirve:** medir **cuánto acierta** de verdad con las reservas de prueba, y ver cómo cambia al mover el umbral.

```python
from sklearn.metrics import (classification_report, confusion_matrix, f1_score,
                             precision_score, recall_score, roc_auc_score)

y_real = prueba[OBJETIVO]
prob = predictor.predict_proba(prueba.drop(columns=[OBJETIVO]))[1]  # probabilidad de cancelar
for umbral in (0.5, 0.3):
    pred = (prob >= umbral).astype(int)
    print(f"\nUmbral {umbral}: precisión={precision_score(y_real, pred):.3f} "
          f"recall={recall_score(y_real, pred):.3f} F1={f1_score(y_real, pred):.3f}")
print("\nROC-AUC:", round(roc_auc_score(y_real, prob), 3))
print("\nMatriz de confusión (umbral 0.5):\n", confusion_matrix(y_real, (prob >= 0.5).astype(int)))
print("\n", classification_report(y_real, (prob >= 0.5).astype(int), digits=3))
# Pregunta de negocio: ¿qué cuesta más, una cancelación no prevista o una alerta falsa? ¿Qué umbral elegirías?
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `from sklearn.metrics import (…)` | Trae seis **funciones de medida** de la librería `scikit-learn` (los paréntesis permiten escribirlas en varias líneas) |
| `y_real = prueba[OBJETIVO]` | Guarda **lo que pasó de verdad**: la columna `cancelada` de la prueba |
| `prueba.drop(columns=[OBJETIVO])` | La misma tabla **sin la columna de la respuesta**. Se la tapamos al modelo para que **no pueda copiar** |
| `predictor.predict_proba(…)` | Para cada reserva da **dos probabilidades**: la de no cancelar (columna `0`) y la de cancelar (columna `1`) |
| `[1]` | Se queda con **la columna 1**: la **probabilidad de cancelar**. Lo guarda en `prob` |
| `for umbral in (0.5, 0.3):` | **Repite** lo de dentro dos veces: primero con `umbral = 0.5` y luego con `0.3`. Lo de dentro va **sangrado** (con espacios a la izquierda) |
| `pred = (prob >= umbral).astype(int)` | Compara cada probabilidad con el umbral y da `True`/`False`; `.astype(int)` lo cambia a **1 y 0**. `1` = «damos la alerta» |
| `precision_score(y_real, pred)` | De las alertas que dimos, ¿qué fracción acertó? |
| `recall_score(y_real, pred)` | De las cancelaciones reales, ¿qué fracción detectamos? |
| `f1_score(y_real, pred)` | Una **media** entre precisión y recall en un solo número |
| `{…:.3f}` | Tres decimales |
| `roc_auc_score(y_real, prob)` | El AUC. **Usa `prob`, no `pred`**: mide si el modelo **ordena** bien, sin necesidad de umbral |
| `confusion_matrix(y_real, …)` | La **matriz de confusión**: una tabla 2×2 que cuenta aciertos y fallos |
| `classification_report(…, digits=3)` | Un informe completo con precisión, recall y F1 de cada clase |

**Un mini-ejemplo de `(prob >= umbral).astype(int)`.** Con cuatro reservas y umbral 0,5:

| | Reserva A | Reserva B | Reserva C | Reserva D |
|---|---|---|---|---|
| `prob` | 0,20 | 0,60 | 0,45 | 0,90 |
| `prob >= 0.5` | `False` | `True` | `False` | `True` |
| `.astype(int)` | 0 | 1 | 0 | 1 |

**Cómo leer la matriz de confusión** (filas = lo que pasó, columnas = lo que dijo el modelo):

```
[[430 193]      fila 0 (no canceló):  430 acertó "no cancela" · 193 alertas falsas
 [230 347]]     fila 1 (canceló):     230 cancelaciones no previstas · 347 acertó "cancela"
```

**Qué debe salir:**

```
Umbral 0.5: precisión=0.643 recall=0.601 F1=0.621
Umbral 0.3: precisión=0.567 recall=0.882 F1=0.691
ROC-AUC: 0.722
```

más la matriz y el informe. Con el umbral **más bajo** (0,3) damos **más alertas**: detectamos más cancelaciones (recall sube de 0,60 a 0,88) pero con más alertas falsas (precisión baja de 0,64 a 0,57).

**Probad vosotros:** cambiad `(0.5, 0.3)` por `(0.5, 0.3, 0.1)`. *Con 0,1 casi todo es alerta: precisión ≈ 0,50 y recall ≈ 0,99.*

---

## Paso 6b · Elegir el umbral con costes

**Para qué sirve:** poner **precio en euros** a los dos tipos de error y calcular **cuánto costaría cada umbral**.

```python
COSTE_NO_PREVISTA = 100    # euros que cuesta una cancelación que no avisamos (noche vacía)
COSTE_ALERTA_FALSA = 40    # euros que cuesta una alerta que no hacía falta (p. ej. un descuento regalado)
y_array = y_real.to_numpy()
filas = []
for u in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7):
    pred = (prob >= u).astype(int)
    no_previstas = int(((pred == 0) & (y_array == 1)).sum())
    falsas = int(((pred == 1) & (y_array == 0)).sum())
    filas.append({"umbral": u, "alertas": int(pred.sum()), "no_previstas": no_previstas,
                  "alertas_falsas": falsas, "coste_euros": COSTE_NO_PREVISTA * no_previstas + COSTE_ALERTA_FALSA * falsas})
tabla_costes = pd.DataFrame(filas)
print("\n", tabla_costes.to_string(index=False))
print("\nUmbral con menos coste (de los probados):", tabla_costes.loc[tabla_costes["coste_euros"].idxmin(), "umbral"])
print("Umbral teórico = alerta falsa / (alerta falsa + no prevista) =",
      round(COSTE_ALERTA_FALSA / (COSTE_ALERTA_FALSA + COSTE_NO_PREVISTA), 2))
print("Comparación: no avisar nunca =", COSTE_NO_PREVISTA * int(y_array.sum()), "euros · avisar a todos =",
      COSTE_ALERTA_FALSA * int((y_array == 0).sum()), "euros")
# Pregunta: ¿gana el modelo a «avisar a todos»? ¿Y si la alerta falsa costara 5 euros en vez de 40?
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `COSTE_NO_PREVISTA = 100` | Lo que cuesta una cancelación que **no avisamos**: 100 € (la habitación se queda vacía). **Es un ejemplo: cambiadlo** |
| `COSTE_ALERTA_FALSA = 40` | Lo que cuesta una alerta que **no hacía falta**: 40 € (por ejemplo, un descuento regalado). **También es un ejemplo** |
| `y_array = y_real.to_numpy()` | Convierte la columna `y_real` en una **lista de números** simple (array de numpy), más cómoda para comparar |
| `filas = []` | Una **lista vacía** donde iremos guardando una fila por cada umbral |
| `for u in (0.1, 0.2, …, 0.7):` | Repite lo de dentro **siete veces**, una por cada umbral `u` |
| `pred = (prob >= u).astype(int)` | Igual que en el paso 6: 1 si damos alerta, 0 si no |
| `(pred == 0) & (y_array == 1)` | *«No dimos alerta **y** la reserva se canceló»*: una cancelación **no prevista**. `==` pregunta *«¿es igual?»*; `&` es *«y»* y se aplica **reserva por reserva**; los paréntesis son obligatorios |
| `.sum()` | Cuenta los `True` (cada `True` vale 1). `int(…)` lo deja como número entero |
| `(pred == 1) & (y_array == 0)` | *«Dimos alerta **y** no se canceló»*: una **alerta falsa** |
| `filas.append({…})` | **Añade** a la lista un **diccionario** con los datos de este umbral. El último campo es el coste: `100 × no_previstas + 40 × falsas` |
| `pd.DataFrame(filas)` | Convierte la lista de diccionarios en una **tabla** |
| `.to_string(index=False)` | La imprime completa y **sin la columna de números de fila** |
| `…["coste_euros"].idxmin()` | `idxmin` da **la posición del coste más pequeño** |
| `tabla_costes.loc[…, "umbral"]` | Con esa posición, lee **qué umbral** es. Es el umbral más barato **de los que hemos probado** |
| `COSTE_ALERTA_FALSA / (COSTE_ALERTA_FALSA + COSTE_NO_PREVISTA)` | La **regla del umbral**: 40 ÷ (40 + 100) = 0,29 |
| `COSTE_NO_PREVISTA * int(y_array.sum())` | **No avisar nunca**: todas las cancelaciones reales (577) cuestan 100 € → **57.700 €** |
| `COSTE_ALERTA_FALSA * int((y_array == 0).sum())` | **Avisar a todos**: todas las reservas que no se cancelan (623) generan una alerta falsa de 40 € → **24.920 €** |

**Un ejemplo con números** (la fila del umbral 0,5): 230 cancelaciones no previstas y 193 alertas falsas → `100 × 230 + 40 × 193 = 23.000 + 7.720 =` **30.720 €**.

**Qué debe salir:**

| umbral | alertas | no_previstas | alertas_falsas | coste_euros |
|---|---|---|---|---|
| 0.1 | 1156 | 4 | 583 | 23720 |
| **0.2** | 1044 | 24 | 491 | **22040** |
| 0.3 | 897 | 68 | 388 | 22320 |
| 0.4 | 717 | 137 | 277 | 24780 |
| 0.5 | 540 | 230 | 193 | 30720 |
| 0.6 | 380 | 316 | 119 | 36360 |
| 0.7 | 240 | 389 | 52 | 40980 |

Y debajo: umbral con menos coste **0,2**, umbral teórico **0,29**, «no avisar nunca» **57.700 €** y «avisar a todos» **24.920 €**.

**Probad vosotros:**
1. Poned `COSTE_ALERTA_FALSA = 5` y volved a ejecutar solo esta celda. *El umbral más barato pasa a ser **0,1** (3.315 €), el teórico baja a **0,05**, y «avisar a todos» cuesta **3.115 €**: **gana al modelo**.* Cuando la alerta casi no cuesta, avisar a todos es mejor.
2. Cambiad la tupla de umbrales por `(0.25, 0.3)`. *Sale una tabla más corta, solo con esos dos.*

---

## Paso 7 · Qué variables pesan más

**Para qué sirve:** saber **en qué columnas se fija** el modelo para decidir. Sirve para comprobar que **tiene sentido** y que no hay fuga de datos.

```python
importancia = predictor.feature_importance(prueba, num_shuffle_sets=3, subsample_size=1000, silent=True)
print(importancia[["importance", "stddev"]].head(10))
# Pregunta: ¿tienen sentido las variables más importantes para el negocio? ¿Alguna sospechosa de fuga?
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `predictor.feature_importance(prueba, …)` | Calcula la **importancia de cada columna**. El método: **baraja** los valores de una columna (la «estropea») y mide **cuánto empeora** el modelo. Si empeora mucho, esa columna era importante |
| `num_shuffle_sets=3` | Repite el barajado **3 veces** y promedia, para no fiarse de un solo intento |
| `subsample_size=1000` | Usa solo **1.000 reservas** de la prueba, para que sea más rápido |
| `silent=True` | Que no imprima de más |
| `importancia[["importance", "stddev"]].head(10)` | Se queda con 2 columnas: la **importancia** y cuánto **varía** (`stddev`) entre repeticiones, y con las **10 primeras filas** |

**Qué debe salir:** arriba **`antelacion_dias`** (≈ 0,07), **`deposito`** (≈ 0,06), **`canal`** (≈ 0,04) y **`tarifa`** (≈ 0,02). El resto, casi 0. Como se usan solo 1.000 reservas elegidas al azar, **los decimales pueden cambiar** de una ejecución a otra; el orden, no.

**Probad vosotros:** cambiad `num_shuffle_sets=3` por `num_shuffle_sets=1`. *Va más rápido y los números varían algo más entre ejecuciones.* Después cambiad `head(10)` por `head(18)` para ver todas las columnas.

---

## Paso 8 · Guardar y recargar el modelo

**Para qué sirve:** dejar el modelo **guardado en una carpeta**, para usarlo después **sin volver a entrenar**. Es lo que hará un servicio real.

```python
predictor.save()
predictor_recargado = TabularPredictor.load(CARPETA_MODELO)
comprobacion = predictor_recargado.predict_proba(prueba.drop(columns=[OBJETIVO]).head(5))[1]
print("\nModelo recargado. Probabilidades de ejemplo:", comprobacion.round(3).tolist())
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `predictor.save()` | **Guarda** el modelo en la carpeta `modelo_cancelaciones` (la de `path=` del paso 4) |
| `TabularPredictor.load(CARPETA_MODELO)` | **Carga** el modelo desde esa carpeta y lo guarda en `predictor_recargado`. Es como **abrir otra vez** un documento guardado |
| `prueba.drop(columns=[OBJETIVO]).head(5)` | Las **5 primeras** reservas de la prueba, sin la respuesta |
| `predict_proba(…)[1]` | Su probabilidad de cancelar (columna 1, como en el paso 6) |
| `comprobacion.round(3).tolist()` | `round(3)` deja 3 decimales; `tolist()` lo convierte en una **lista** de Python para imprimirla |

**Qué debe salir:** `Modelo recargado. Probabilidades de ejemplo: [0.457, 0.644, 0.543, 0.352, 0.123]`.

**Para qué se recarga:** para **comprobar** que lo guardado funciona. Si las probabilidades son razonables, el modelo se puede usar desde cualquier sitio que tenga la carpeta.

**Probad vosotros:** en una celda nueva, `import os; print(os.listdir("modelo_cancelaciones"))`. *Enseña lo que hay dentro de la carpeta: los archivos y subcarpetas del modelo.* Y mirad el panel de archivos de Colab: la carpeta pesa unos 225 MB.

---

## Paso 9 · Una función para predecir una reserva suelta

**Para qué sirve:** convertir el modelo en algo **fácil de usar**: le pasas **una reserva** y te dice la **probabilidad** y si hay **alerta**.

```python
def predecir_cancelacion(reserva: dict) -> dict:
    """Recibe una reserva (dict con las columnas de entrada) y devuelve la probabilidad de cancelación."""
    fila = pd.DataFrame([reserva])
    fila["fecha_reserva"] = pd.to_datetime(fila["fecha_reserva"])
    fila["fecha_llegada"] = pd.to_datetime(fila["fecha_llegada"])
    p = float(predictor_recargado.predict_proba(fila)[1].iloc[0])
    return {"probabilidad_cancelacion": round(p, 4), "alerta": p >= 0.5}


ejemplo = prueba.drop(columns=[OBJETIVO]).iloc[0].to_dict()
print("\nEjemplo de predicción:", predecir_cancelacion(ejemplo))
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `def predecir_cancelacion(reserva: dict) -> dict:` | **Define** la función. Recibe `reserva` (un diccionario, `: dict`) y **devuelve** otro diccionario (`-> dict`). Esas indicaciones son solo **ayuda para quien lee** |
| `fila = pd.DataFrame([reserva])` | Convierte el diccionario en una **tabla de una sola fila**. Los corchetes `[ ]` son importantes: *«una lista con una reserva»* |
| `fila["fecha_reserva"] = pd.to_datetime(…)` | Convierte el **texto** de la fecha en una **fecha de verdad** (como en el paso 1). Si llega un texto, el modelo no lo entendería como fecha. Lo mismo para `fecha_llegada` |
| `predictor_recargado.predict_proba(fila)[1]` | La probabilidad de cancelar de esa fila (columna 1) |
| `.iloc[0]` | De esa columna, **el primer valor** (el único) |
| `float(…)` | Lo convierte en un **número decimal** normal |
| `return {…}` | **Devuelve** un diccionario con la probabilidad (redondeada a 4 decimales) y `alerta`: `True` si `p >= 0.5` |
| `ejemplo = prueba.drop(…).iloc[0].to_dict()` | Toma **la primera reserva** de la prueba (sin la respuesta) y la convierte en **diccionario** |
| `predecir_cancelacion(ejemplo)` | **Llama** a la función con ese ejemplo |

**Definir y llamar.** Definir una función es **explicar cómo se hace** (no hace nada todavía). **Llamarla** (`predecir_cancelacion(ejemplo)`) es **pedir que lo haga** con unos datos concretos.

**Qué debe salir:** `Ejemplo de predicción: {'probabilidad_cancelacion': 0.457, 'alerta': False}`. Coincide con la primera probabilidad del paso 8 (0,457).

**Probad vosotros:** cambiad `p >= 0.5` por `p >= 0.3`, ejecutad otra vez la celda y fijaos en `alerta`. *Ahora sale `True`: 0,457 supera 0,3.* Mismo modelo, **otro umbral, otra decisión**.

---

## Paso 10 · Servir el modelo por API

**Para qué sirve:** una **API** es un servicio al que **otro programa** le manda una reserva y recibe la predicción. Aquí **lo probamos desde el propio cuaderno**.

```python
# En Colab no se puede abrir http://127.0.0.1:8000/docs desde tu navegador: usamos TestClient,
# que llama a la API "por dentro", igual que lo haría un cliente. En local: uvicorn api_cancelaciones:app --reload
import importlib, sys
archivo("api_cancelaciones.py")
sys.path.insert(0, os.getcwd())
api = importlib.import_module("api_cancelaciones")
from fastapi.testclient import TestClient
cliente = TestClient(api.app)
print(cliente.get("/salud").json())
reserva_ejemplo = {"fecha_reserva": "2025-11-03", "fecha_llegada": "2026-01-15", "antelacion_dias": 73, "noches": 5,
                   "adultos": 2, "ninos": 0, "tipo_habitacion": "estandar", "regimen": "desayuno",
                   "canal": "web_intermediaria", "pais_origen": "UK", "tarifa": "flexible",
                   "deposito": "sin_deposito", "precio_noche": 85.0, "peticiones_especiales": 0,
                   "cliente_repetidor": 0, "cancelaciones_previas": 0}
respuesta = cliente.post("/predecir", json=reserva_ejemplo)
print(respuesta.status_code, respuesta.json())
# Prueba también una reserva con datos imposibles (por ejemplo "noches": 0) y mira el error 422.
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `import importlib, sys` | Trae herramientas para **importar un archivo por su nombre** |
| `archivo("api_cancelaciones.py")` | Descarga el archivo de la API (si no está), con la función del paso 0 |
| `sys.path.insert(0, os.getcwd())` | Le dice a Python que **busque también en la carpeta actual**, donde está ese archivo |
| `api = importlib.import_module("api_cancelaciones")` | **Importa** `api_cancelaciones.py`. Al importarlo se ejecuta: **carga el modelo** de la carpeta `modelo_cancelaciones` y crea la API |
| `TestClient(api.app)` | Crea un **cliente de pruebas**: un «programa» que llama a la API **por dentro**, sin abrir el navegador. En Colab hace falta, porque no se puede abrir `http://127.0.0.1:8000/docs` desde vuestro navegador |
| `cliente.get("/salud").json()` | Hace una petición **GET** a `/salud` («¿estás vivo?») y muestra la respuesta como diccionario |
| `reserva_ejemplo = {…}` | Una reserva inventada, con las 16 columnas de entrada |
| `cliente.post("/predecir", json=reserva_ejemplo)` | Hace una petición **POST** a `/predecir` **enviando** la reserva en formato JSON |
| `respuesta.status_code` | El **código de la respuesta**: `200` = todo bien |
| `respuesta.json()` | La respuesta de la API, como diccionario |

**Qué debe salir:**

```
{'estado': 'ok', 'modelo': 'modelo_cancelaciones'}
200 {'probabilidad_cancelacion': 0.79, 'alerta': True, 'umbral': 0.5}
```

La probabilidad puede ser 0,78 o 0,79 según el equipo. Esta reserva es de **alto riesgo**: canal `web_intermediaria`, tarifa `flexible`, `sin_deposito` y 73 días de antelación; justo lo que el paso 7 decía que empuja a cancelar.

### Qué hay dentro de `api_cancelaciones.py`

El archivo [`api_cancelaciones.py`](../../Reto_S03/laboratorio_automl/api_cancelaciones.py) tiene tres partes:

| Parte | Qué hace |
|---|---|
| `predictor = TabularPredictor.load(CARPETA_MODELO)` | **Carga el modelo** al arrancar. Por eso **hay que haber hecho el paso 8**: sin la carpeta, da `FileNotFoundError` |
| `UMBRAL = float(os.environ.get("UMBRAL", "0.5"))` | El umbral sale de una **variable de entorno** llamada `UMBRAL`; si no existe, usa `0.5`. Así se cambia **sin tocar el código** |
| `class Reserva(BaseModel):` | La **plantilla** de una reserva válida: qué campos tiene, de qué tipo y con qué reglas |
| `@app.get("/salud")` | El `@` registra la función de debajo como la respuesta a `GET /salud` |
| `@app.post("/predecir")` | Registra la función de debajo como la respuesta a `POST /predecir`. Su parámetro `reserva: Reserva` hace que FastAPI **compruebe los datos antes de entrar** |
| `reserva.model_dump()` | Convierte la reserva ya comprobada en un diccionario, para pasarla a pandas |
| `return {…}` | Devuelve un diccionario; FastAPI lo convierte en **JSON** |

**Las reglas de la plantilla `Reserva`:**

| Escrito así | Significa |
|---|---|
| `noches: int = Field(..., ge=1)` | Obligatorio (`...`), entero, **mayor o igual que 1** (`ge` = *greater or equal*) |
| `precio_noche: float = Field(..., gt=0)` | Obligatorio, decimal, **mayor que 0** (`gt` = *greater than*) |
| `ninos: int = Field(0, ge=0)` | Opcional: si no viene, vale `0`; no puede ser negativo |
| `cliente_repetidor: … ge=0, le=1` | Solo puede ser `0` o `1` (`le` = *less or equal*) |
| `pais_origen: str \| None = None` | **Opcional**: puede ser un texto o no venir |
| `fecha_reserva: str` | Las fechas llegan como **texto**, porque el formato JSON no tiene fechas; se convierten dentro con `pd.to_datetime` |

**Por qué responde 422 con `"noches": 0`:** la plantilla exige `noches ≥ 1`. FastAPI **rechaza la reserva antes** de llegar al modelo y responde **422** («datos no válidos») con el campo que falla. **No es un fallo del cuaderno: es la API protegiendo al modelo de datos imposibles.**

**Probad vosotros:** copiad la reserva, cambiad `"noches": 5` por `"noches": 0` y volved a llamar a `cliente.post(...)`. *Sale `422` y un mensaje que dice `Input should be greater than or equal to 1`.* Probad también `"adultos": 0`, `"precio_noche": 0` o `"cliente_repetidor": 2`: *los tres dan 422 por la misma razón.*

---

## Paso 11 · Informe de recursos

**Para qué sirve:** dejar por escrito **lo que ha costado** el experimento (tiempo, espacio y dinero) y **recordar cerrar** lo que quede abierto.

```python
tamano_mb = sum(
    os.path.getsize(os.path.join(raiz, f))
    for raiz, _, ficheros in os.walk(CARPETA_MODELO) for f in ficheros
) / 1e6
print("\n--- Informe de recursos ---")
print(f"Tiempo de entrenamiento: {tiempo_entrenamiento:.0f} s (límite fijado: {LIMITE_TIEMPO} s)")
print(f"Tamaño del modelo en disco: {tamano_mb:.1f} MB")
print("Coste económico: 0 EUR (Colab gratuito o equipo local)")
print("Recursos que hay que cerrar: la sesión de Colab (Entorno de ejecución > Desconectar).")
```

**Qué hace cada línea:**

| Línea | Qué hace |
|---|---|
| `os.walk(CARPETA_MODELO)` | **Recorre** la carpeta del modelo y **todas sus subcarpetas**. En cada una da su ruta (`raiz`), sus subcarpetas (`_`, que no usamos; por costumbre se llama así lo que se ignora) y sus archivos (`ficheros`) |
| `for raiz, _, ficheros in … for f in ficheros` | Dos bucles seguidos: *«para cada carpeta, para cada archivo de esa carpeta»* |
| `os.path.join(raiz, f)` | Une la carpeta y el nombre para tener la **ruta completa** del archivo |
| `os.path.getsize(…)` | El **tamaño** de ese archivo, en bytes |
| `sum( … )` | **Suma** los tamaños de todos los archivos |
| `/ 1e6` | Divide entre un millón (`1e6`): de bytes a **megabytes** |
| `{tamano_mb:.1f}` | Un decimal |
| `print("Coste económico: 0 EUR …")` | Un texto fijo: este laboratorio **no cuesta dinero** |

**Qué debe salir:**

```
--- Informe de recursos ---
Tiempo de entrenamiento: 36 s (límite fijado: 120 s)
Tamaño del modelo en disco: 225.7 MB
Coste económico: 0 EUR (Colab gratuito o equipo local)
Recursos que hay que cerrar: la sesión de Colab (Entorno de ejecución > Desconectar).
```

Los segundos y los MB pueden variar un poco en vuestro equipo. **La última línea no es decoración**: en Colab, cerrad con *Entorno de ejecución → Desconectar y eliminar entorno de ejecución* y haced una **captura** como prueba.

---

## Comprobación final: siete preguntas de código

Contestadlas **sin mirar** y luego comparad.

**1. ¿Qué diferencia hay entre `entrenamiento` y `prueba`?**
*`entrenamiento` son las 4.800 reservas más antiguas, con las que **aprende** el modelo. `prueba` son las 1.200 más recientes, que el modelo **no ve** al entrenar y sirven para medir si acierta de verdad.*

**2. En `predictor.predict_proba(…)[1]`, ¿qué es el `[1]`?**
*`predict_proba` devuelve dos columnas: la `0` (probabilidad de no cancelar) y la `1` (probabilidad de cancelar). `[1]` elige la segunda.*

**3. ¿Por qué se hace `drop(columns=[OBJETIVO])` antes de predecir?**
*Para **taparle la respuesta** al modelo. Si la columna `cancelada` estuviera, el modelo podría copiarla y la nota no valdría nada.*

**4. ¿Qué diferencia hay entre `&` y `and` en `(pred == 0) & (y_array == 1)`?**
*`&` compara **reserva por reserva** (miles de comparaciones a la vez). `and` no sirve con tablas y listas de números: Python se queja con `ValueError`. Y los paréntesis son obligatorios porque `&` se evalúa antes que `==`.*

**5. ¿Cómo cambiaríais el umbral de la API **sin tocar el código**?**
*Con la variable de entorno `UMBRAL`, por ejemplo (Linux o Mac) `UMBRAL=0.3 uvicorn api_cancelaciones:app`. El archivo la lee con `os.environ.get("UMBRAL", "0.5")` y, si no existe, usa 0,5.*

**6. ¿Por qué la API responde 422 con `"noches": 0`, y qué parte del código lo decide?**
*La plantilla `Reserva` dice `noches: int = Field(..., ge=1)`: «como mínimo 1». FastAPI comprueba los datos **antes** de ejecutar la función `predecir`, y rechaza lo que no cumple.*

**7. ¿Qué pasaría si quitáramos `sort_values("fecha_reserva")` del paso 3?**
*`iloc[:corte]` cogería las primeras 4.800 filas **del archivo**, sin ordenar por fecha: pasado y futuro quedarían mezclados y el resultado saldría **más optimista** que en la vida real.*

---

## Errores típicos de código

| Qué ves | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'datos' is not defined` | Usas una variable que **no se ha creado**: te saltaste una celda o se reinició el entorno | Ejecutad **desde el paso 0** hasta donde estabais |
| `ModuleNotFoundError: No module named 'autogluon'` | La instalación no se hizo o se perdió | Ejecutad **otra vez** la celda de instalación |
| `KeyError: 'Cancelada'` | El nombre de la columna está mal escrito: Python distingue **mayúsculas y minúsculas** (es `cancelada`) | Comprobad el nombre con `datos.columns` |
| `SyntaxError` | Falta o sobra un **paréntesis, comilla o coma** | Mirad la línea que señala el error y la anterior |
| `IndentationError` | Los **espacios a la izquierda** (el sangrado) están mal, por ejemplo dentro de un `for` o un `def` | Dejad el mismo sangrado en todas las líneas del bloque |
| `ValueError: The truth value of a Series is ambiguous` | Se usó `and`/`or` entre tablas en vez de `&`/`\|` | Usad `&` (y) y `\|` (o), con paréntesis |
| `FileNotFoundError: … modelo_cancelaciones` | No existe la carpeta del modelo | Ejecutad los pasos 4 y 8 antes del paso 10 |
| La celda **no acaba** y no sale nada | Es el paso 4 entrenando | Esperad hasta 2 minutos; para un ensayo, `LIMITE_TIEMPO = 15` |

**Un truco para leer cualquier error:** mirad **la última línea** (dice qué ha pasado) y **la flecha `---->`** (señala la línea donde ha pasado).
