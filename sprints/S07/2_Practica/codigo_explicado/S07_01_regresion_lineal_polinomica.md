# Código explicado · S07.01 · Regresión lineal y polinómica: predecir el precio por noche

> **Para qué sirve.** Aquí está **todo el código del cuaderno explicado por escrito**, celda a celda y en el mismo orden. Cada bloque sigue siempre el mismo guion: **primero** un párrafo que dice qué vamos a hacer, por qué y qué debe salir; **después** el código, con **cada línea explicada**; y **al final** lo destacable del bloque (lo que conviene recordar y con qué se relaciona).
>
> **Cuaderno:** [🏫 en clase](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_01_regresion_lineal_polinomica_en_clase.ipynb) · [🏠 completo](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_01_regresion_lineal_polinomica.ipynb)
>
> **Cómo usarlo:** ejecuta la celda en el cuaderno; busca aquí la del mismo número (A3, A5…); lee el párrafo, sigue el código línea a línea y, al terminar, cambia algo (un número, una columna) y comprueba si pasa lo que esperabas: es la mejor manera de entender código.

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda** («coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`»). Lo que va tras `#` es un comentario: Python lo ignora. Los ejercicios (✏️) llevan aquí la **solución de referencia**: úsala **después** de intentarlo.

## La idea del cuaderno

TurisData quiere una **tarifa de referencia**: ¿cuánto debería costar la noche de una reserva según el **tipo de habitación** y la **época del año**? Predecir un número (euros) es un problema de **regresión**, y empezamos por el modelo más sencillo y más fácil de explicar: la **regresión lineal**.

- **Hilo del cuaderno:** preparamos las variables (A1, A2) → ajustamos la recta (A3) → la comparamos con un modelo «tonto» (A4) → leemos sus coeficientes en euros (A5) → miramos dónde se equivoca (A6) → probamos las **interacciones** para corregirlo (A7, A8) → vemos qué pasa con **polinomios** de grado alto (A9, A10) → ponemos el modelo a trabajar en una función (A11).
- **Lo que te llevas:** un modelo lineal se lee como una **tabla de precios** (un coeficiente por variable, en euros); las métricas R², MAE y RMSE dicen cuánto se equivoca; y «más complicado» (más grado, más columnas) **no siempre es mejor**.

## Mapa de celdas

| Celda | Tipo | Qué hacemos | ¿Dónde? |
|---|---|---|---|
| A1 | ⚙️ Preparación | Preparar las herramientas y los datos | 🏫 |
| A2 | 👀 Ejemplo | Preparar X e y con variables dummy | 🏫 |
| A3 | ✏️ Ejercicio | Ajustar la regresión lineal | 🏫 |
| A4 | 👀 Ejemplo | El baseline: predecir siempre la media | 🏫 |
| A5 | ✏️ Ejercicio | Leer los coeficientes en euros | 🏫 |
| A6 | 👀 Ejemplo | Residuos del modelo lineal | 🏫 |
| A7 | 👀 Ejemplo | Interacciones con validación cruzada | 🏫 |
| A8 | ✏️ Ejercicio | Error de las interacciones en test | 🏫 |
| A9 | 👀 Ejemplo | Polinomios de grado 1 a 12 | 🏠 |
| A10 | ✏️ Ejercicio | Polinomio sobre el mes o variable temporada_alta | 🏠 |
| A11 | 🎯 Mini-reto | Función precio_recomendado | 🏠 |

🏫 = en clase · 🏠 = en casa. 👀 ejemplo: solo se ejecuta y se mira. ✏️ ejercicio: se completa con tu código. ⚙️ preparación: se ejecuta sola.

## Celda a celda

### ⚙️ A1 · Preparación — Preparar las herramientas y los datos

**Qué vamos a hacer y qué debe salir**

Esta celda **no tienes que entenderla para empezar**: solo ejecutarla la primera. Prepara el terreno: trae las librerías, define cómo encontrar los ficheros de datos y carga las **6000 reservas** de TurisData en una tabla llamada `df`. Además crea dos columnas nuevas que usaremos todo el cuaderno: `mes_llegada` (1 a 12) y `temporada_alta` (1 si la llegada es en enero, febrero, marzo, julio, agosto o diciembre; 0 si no). **Debe salir** `(6000, 20)` —6000 filas y 20 columnas— y `Listo ✔`. Se relaciona con todo lo que viene después: cada celda siguiente parte de `df` y de las librerías que se importan aquí.

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
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)
print(df.shape)
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
  Trae **NumPy** (lo llamamos `np`): operaciones con números y matrices.
- `import pandas as pd`  
  Trae **pandas** (`pd`): las tablas de datos (`DataFrame`).
- `import matplotlib.pyplot as plt`  
  Trae **matplotlib** (`plt`): para dibujar gráficos.
- `import seaborn as sns`  
  Trae **seaborn** (`sns`): gráficos más bonitos y rápidos, sobre matplotlib.
- `from sklearn.model_selection import train_test_split, cross_val_score`  
  De **scikit-learn** trae `train_test_split` (reparte los datos en entrenamiento y prueba) y `cross_val_score` (validación cruzada).
- `from sklearn.linear_model import LinearRegression`  
  Trae `LinearRegression`, el modelo de regresión lineal.
- `from sklearn.dummy import DummyRegressor`  
  Trae `DummyRegressor`, un modelo «tonto» que sirve de referencia (el *baseline*).
- `from sklearn.preprocessing import PolynomialFeatures, StandardScaler`  
  Trae `PolynomialFeatures` (crea columnas con potencias y productos) y `StandardScaler` (pone las columnas en la misma escala).
- `from sklearn.pipeline import make_pipeline`  
  Trae `make_pipeline`, para encadenar pasos (preparar → modelo) en un solo objeto.
- `from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score`  
  Trae las tres métricas de error: `mean_absolute_error` (MAE), `mean_squared_error` (para el RMSE) y `r2_score` (R²).
- `SEMILLA = 42`  
  Fija un número (`42`) para que **los sorteos salgan igual en cada ejecución**: así tu resultado coincide con el de este documento.
- `sns.set_theme(style="whitegrid")`  
  Elige el estilo visual de todos los gráficos (fondo claro con cuadrícula).
- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])`  
  Lee `reservas_turisdata.csv` y lo guarda en `df`. `dato(...)` encuentra el fichero; `parse_dates=[...]` dice que esas dos columnas son **fechas**, no texto.
- `df["mes_llegada"] = df["fecha_llegada"].dt.month`  
  Crea la columna `mes_llegada`: de la fecha de llegada (`.dt`) se queda con el número de mes (`.month`).
- `df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)`  
  Crea `temporada_alta`: `.isin([1, 2, 3, 7, 8, 12])` da verdadero/falso según si el mes está en la lista, y `.astype(int)` lo convierte en 1 / 0.
- `print(df.shape)`  
  Escribe el tamaño de la tabla: `(6000, 20)`.
- `print("Listo ✔")`  
  Mensaje de que todo ha ido bien.

**Lo destacable**

- La celda de preparación **se ejecuta siempre la primera**, y otra vez si Colab se reinicia: todas las demás celdas usan lo que crea aquí (`df`, `SEMILLA`, las librerías…). Si ves `NameError: name '…' is not defined`, casi siempre es que falta ejecutarla.
- `temporada_alta` convierte una idea del negocio («en invierno y verano suben los precios») en **una columna de 0 y 1**: así un modelo puede usarla.
- `random_state`/`SEMILLA` es lo que hace que el cuaderno sea **reproducible**.

### 👀 A2 · Ejemplo — Preparar X e y con variables dummy

**Qué vamos a hacer y qué debe salir**

Un modelo solo entiende **números**, y `tipo_habitacion` es texto («estandar», «suite»…). La solución se llama **variables dummy** (o *one-hot*): una columna de 0 y 1 por cada tipo. Aquí prepararemos las dos piezas de todo modelo de *machine learning*: **`X`** (las variables con las que predecimos: tipo de habitación y temporada) e **`y`** (lo que queremos predecir: el precio por noche). **Debe salir** una tabla de 5 filas con 4 columnas: `tipo_habitacion_familiar`, `tipo_habitacion_suite`, `tipo_habitacion_superior` y `temporada_alta`. Fíjate en que **falta** la columna de «estándar»: no es un olvido, es `drop_first=True`, y explica por qué luego el «precio de partida» del modelo es el de una estándar. Se apoya en A1 (`df`) y alimenta a todos los ejercicios.

```python
X = pd.get_dummies(df[["tipo_habitacion"]], drop_first=True).astype(int)
X["temporada_alta"] = df["temporada_alta"]
y = df["precio_noche"]
X.head()
```

**Línea a línea**

- `X = pd.get_dummies(df[["tipo_habitacion"]], drop_first=True).astype(int)`  
  `pd.get_dummies(...)` convierte `tipo_habitacion` en una columna 0/1 por tipo. `drop_first=True` **quita la primera categoría** (estándar): si una reserva tiene 0 en familiar, suite y superior, es una estándar, así que esa columna sobra (y evita que unas columnas se puedan deducir de otras). `.astype(int)` deja 0 y 1 en lugar de falso/verdadero.
- `X["temporada_alta"] = df["temporada_alta"]`  
  Añade a `X` la columna `temporada_alta` tal cual está en `df`.
- `y = df["precio_noche"]`  
  `y` es la columna que queremos predecir: el precio por noche.
- `X.head()`  
  Muestra las 5 primeras filas de `X` para comprobar que tiene el aspecto esperado.

**Lo destacable**

- **Convención:** `X` en mayúscula (tabla de varias variables) e `y` en minúscula (una sola columna).
- `drop_first=True`: la categoría que se quita pasa a ser la **referencia**; los coeficientes del modelo se leerán como «cuánto más (o menos) que una estándar».
- Es el mismo truco de «texto → columnas 0/1» que verás en el `Pipeline` de S06 (`OneHotEncoder`): aquí a mano, allí automático.

### ✏️ A3 · Ejercicio — Ajustar la regresión lineal

**Qué vamos a hacer y qué debe salir**

Primer ejercicio: **entrenar el modelo y ver cuánto acierta**. Para saber si un modelo sirve hay que probarlo con datos que **no ha visto**, así que primero separamos las reservas: el 80 % (4800) para que el modelo aprenda (*train*) y el 20 % (1200) para examinarlo (*test*). Después ajustamos una `LinearRegression`, predecimos el precio de las reservas de test y medimos el error con tres métricas. **Debe salir** `R² = 0.915 · MAE = 7.24 € · RMSE = 9.70 €` y `✔ Ejercicio 1 correcto`. Se lee así: solo con el tipo de habitación y la temporada, el modelo explica el **91,5 %** de la variación del precio, y de media se equivoca en unos **7 €** por noche. Se apoya en `X` e `y` de A2; y la comparación con el modelo tonto (A4) dirá si 7,24 € es mucho o poco.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA)
modelo_lin = LinearRegression().fit(X_train, y_train)
pred = modelo_lin.predict(X_test)
r2_test = r2_score(y_test, pred)
mae_test = mean_absolute_error(y_test, pred)
assert len(X_test) == 1200, "Con 6000 filas y test_size=0.2 el test debe tener 1200 filas"
assert r2_test > 0.85, "R² debería superar 0,85: revisa que uses tipo de habitación y temporada"
assert 5 < mae_test < 15, "El MAE debería estar entre 5 y 15 euros"
print(f"R² = {r2_test:.3f} · MAE = {mae_test:.2f} € · RMSE = {mean_squared_error(y_test, pred) ** 0.5:.2f} €")
print("✔ Ejercicio 1 correcto")
```

**Línea a línea**

- `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA)`  
  `train_test_split` reparte `X` e `y` en cuatro piezas: `X_train`/`y_train` (para aprender) y `X_test`/`y_test` (para examinar). `test_size=0.2` reserva el 20 % para test y `random_state=SEMILLA` fija el sorteo.
- `modelo_lin = LinearRegression().fit(X_train, y_train)`  
  Crea la regresión lineal (`LinearRegression()`) y la **ajusta** con `.fit(X_train, y_train)`: aquí es donde el modelo «aprende» los coeficientes. El resultado se guarda en `modelo_lin`.
- `pred = modelo_lin.predict(X_test)`  
  `.predict(X_test)` pide al modelo el precio de cada reserva de test, **sin enseñarle la respuesta**. Son las predicciones (`pred`).
- `r2_test = r2_score(y_test, pred)`  
  **R²**: qué parte de la variación del precio explica el modelo (1 = todo, 0 = nada mejor que la media). Compara lo predicho (`pred`) con lo real (`y_test`).
- `mae_test = mean_absolute_error(y_test, pred)`  
  **MAE** (error absoluto medio): de media, cuántos euros se equivoca el modelo, sin importar el signo.
- `assert len(X_test) == 1200, "Con 6000 filas y test_size=0.2 el test debe tener 1200 filas"` … `assert 5 < mae_test < 15, "El MAE debería estar entre 5 y 15 euros"` (3 líneas)  
  Tres **comprobaciones** (`assert`): que el test tiene 1200 filas, que el R² supera 0,85 y que el MAE está entre 5 y 15 €. Si alguna falla, el cuaderno se para y muestra el mensaje que va tras la coma: es la pista de qué revisar.
- `print(f"R² = {r2_test:.3f} · MAE = {mae_test:.2f} € · RMSE = {mean_squared_error(y_test, pred) ** 0.5:.2f} €")`  
  Escribe las tres métricas. El **RMSE** no se guardó antes: se calcula aquí al vuelo con `mean_squared_error(...) ** 0.5` (la raíz del error cuadrático medio). Las `:.3f` y `:.2f` son los decimales que se muestran.
- `print("✔ Ejercicio 1 correcto")`  
  Si ninguna comprobación falló, llega aquí y avisa de que el ejercicio está bien.

**Lo destacable**

- **Nunca se mide con los datos de entrenamiento:** el examen siempre es con `X_test`, que el modelo no ha visto.
- `fit` = aprender; `predict` = usar lo aprendido. Esa pareja se repetirá en **todos** los modelos del curso.
- **MAE vs RMSE:** el RMSE (9,70) sale mayor que el MAE (7,24) porque eleva los errores al cuadrado y **castiga más los grandes**.
- R² alto no es la meta en sí: hay que compararlo con un modelo de referencia (siguiente celda).

### 👀 A4 · Ejemplo — El baseline: predecir siempre la media

**Qué vamos a hacer y qué debe salir**

¿Es bueno un MAE de 7,24 €? Depende de con qué se compare. El **baseline** (modelo de referencia) más simple posible es un modelo «tonto» que **dice siempre el precio medio**, sin mirar la reserva. Si nuestro modelo no le gana claramente, no sirve para nada. **Debe salir** `Baseline: MAE = 25.56 € · R² = -0.002`: el modelo tonto se equivoca en unos 25 € de media y su R² es prácticamente 0 (explica nada). Es decir, la regresión lineal **reduce el error de 25,56 € a 7,24 €**. Se apoya en A3 (usa los mismos `X_train`, `X_test`, `y_train`, `y_test`) y es una idea que se repite en todos los modelos: **siempre hay que compararse con un baseline**.

```python
base = DummyRegressor(strategy="mean").fit(X_train, y_train)
print(f"Baseline: MAE = {mean_absolute_error(y_test, base.predict(X_test)):.2f} € · R² = {r2_score(y_test, base.predict(X_test)):.3f}")
```

**Línea a línea**

- `base = DummyRegressor(strategy="mean").fit(X_train, y_train)`  
  `DummyRegressor(strategy="mean")` es el modelo tonto: al hacer `.fit` solo calcula **la media** del precio en train. Después predecirá siempre ese mismo número.
- `print(f"Baseline: MAE = {mean_absolute_error(y_test, base.predict(X_test)):.2f} € · R² = {r2_score(y_test, base.predict(X_test)):.3f}")`  
  Calcula y escribe su MAE y su R² en test. `base.predict(X_test)` devuelve la media repetida 1200 veces.

**Lo destacable**

- Un **R² ≈ 0** significa «no mejora a predecir siempre la media»: es el suelo; el R² del modelo (0,915) hay que leerlo desde ahí.
- El baseline da el **listón mínimo**: cualquier modelo que no lo supere no merece usarse.
- En clasificación (S07_03 y S07_04) hará de baseline el modelo que dice siempre «no cancela».

### ✏️ A5 · Ejercicio — Leer los coeficientes en euros

**Qué vamos a hacer y qué debe salir**

La gran ventaja de la regresión lineal es que **se puede leer**: cada variable tiene un **coeficiente** que dice cuántos euros suma (o resta) al precio. Aquí los sacamos del modelo y los ponemos en una tabla con el nombre de cada variable. **Debe salir** `familiar 45.0`, `suite 101.2`, `superior 28.4`, `temporada_alta 22.4` y una ordenada en el origen de `67.3 €`, seguido de `✔ Ejercicio 2 correcto`. Léelo como una **tabla de precios**: el modelo parte de unos **67,3 €** (lo que predice para una estándar en temporada baja), y suma **45** si es familiar, **101** si es suite, **28** si es superior y **22** si es temporada alta. Se apoya en `modelo_lin` (A3) y en las columnas de `X` (A2).

```python
coefs = pd.Series(modelo_lin.coef_, index=X.columns)
extra_suite = coefs["tipo_habitacion_suite"]
efecto_temporada_alta = coefs["temporada_alta"]
assert 90 < extra_suite < 115, "Una suite cuesta unos 100 € más que una estándar (coeficiente de tipo_habitacion_suite)"
assert 15 < efecto_temporada_alta < 30, "La temporada alta añade unos 20-25 €"
print(coefs.round(1))
print("Ordenada en el origen (lo que predice el modelo para una estándar en temporada baja):", round(modelo_lin.intercept_, 1), "€")
print("✔ Ejercicio 2 correcto")
```

**Línea a línea**

- `coefs = pd.Series(modelo_lin.coef_, index=X.columns)`  
  `modelo_lin.coef_` es la lista de coeficientes (uno por columna de `X`). `pd.Series(..., index=X.columns)` les pone **nombre**: así sabemos a qué variable corresponde cada número.
- `extra_suite = coefs["tipo_habitacion_suite"]`  
  Guarda el coeficiente de la suite: lo que sube el precio (en €) una suite respecto a una estándar.
- `efecto_temporada_alta = coefs["temporada_alta"]`  
  Guarda el coeficiente de la temporada alta: lo que sube el precio en esa época.
- `assert 90 < extra_suite < 115, "Una suite cuesta unos 100 € más que una estándar (coeficiente de tipo_habitacion_suite)"` … `assert 15 < efecto_temporada_alta < 30, "La temporada alta añade unos 20-25 €"` (2 líneas)  
  Dos comprobaciones: la suite debe costar unos 100 € más (coeficiente entre 90 y 115) y la temporada alta unos 20-25 € (entre 15 y 30).
- `print(coefs.round(1))`  
  Escribe la tabla de coeficientes redondeada a 1 decimal.
- `print("Ordenada en el origen (lo que predice el modelo para una estándar en temporada baja):", round(modelo_lin.intercept_, 1), "€")`  
  `modelo_lin.intercept_` es la **ordenada en el origen**: lo que el modelo predice cuando todas las variables valen 0, es decir, para una estándar en temporada baja. Ojo: es la salida del **ajuste conjunto** (67,3 €), no el precio medio real de esa habitación (que ronda los 70 €).
- `print("✔ Ejercicio 2 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Cómo se lee:** precio ≈ 67,3 + 45·familiar + 101,2·suite + 28,4·superior + 22,4·temporada_alta.
- Los coeficientes son **diferencias respecto a la categoría de referencia** (la estándar que se quitó en A2).
- Que se pueda leer así es lo que hace a la regresión lineal tan útil para explicar al cliente **por qué** el modelo cobra lo que cobra.
- Los coeficientes asumen que cada efecto **se suma** sin importar los demás: esa hipótesis se pone a prueba en A6 y A7.

### 👀 A6 · Ejemplo — Residuos del modelo lineal

**Qué vamos a hacer y qué debe salir**

Un buen R² no lo cuenta todo: hay que mirar **dónde se equivoca** el modelo. El error de cada reserva se llama **residuo** (precio real − precio predicho). Si el modelo está bien planteado, los residuos deben parecerse a ruido: repartidos al azar alrededor de 0. **Debe salir** una figura con dos gráficos. A la izquierda, residuos frente a la predicción: una nube con forma de **embudo** (se abre hacia los precios altos). A la derecha, el histograma de los residuos: una campana centrada cerca de 0. El embudo es la pista: el modelo falla **más en las reservas caras** (las suites en temporada alta), porque el efecto de la temporada no es el mismo en todas las habitaciones. Eso lo corregirán las interacciones (A7). Se apoya en `pred` (A3).

```python
residuos = y_test - pred
fig, ejes = plt.subplots(1, 2, figsize=(11, 4))
ejes[0].scatter(pred, residuos, s=10, alpha=0.4, color="#2a6f97")
ejes[0].axhline(0, color="black", lw=1)
ejes[0].set(title="Residuos frente a predicción", xlabel="Precio predicho (€)", ylabel="Residuo (€)")
sns.histplot(residuos, bins=30, ax=ejes[1], color="#2a6f97")
ejes[1].set(title="Distribución de los residuos", xlabel="Residuo (€)", ylabel="Reservas")
plt.tight_layout()
plt.show()
```

**Línea a línea**

- `residuos = y_test - pred`  
  El residuo de cada reserva de test: lo real menos lo predicho. Positivo = el modelo se quedó corto; negativo = se pasó.
- `fig, ejes = plt.subplots(1, 2, figsize=(11, 4))`  
  Crea una figura con **1 fila y 2 gráficos** (`ejes[0]` a la izquierda, `ejes[1]` a la derecha), de 11×4 pulgadas.
- `ejes[0].scatter(pred, residuos, s=10, alpha=0.4, color="#2a6f97")`  
  Dibuja una nube de puntos: precio predicho (horizontal) frente a residuo (vertical). `s` es el tamaño del punto, `alpha` la transparencia y `color` el azul del curso.
- `ejes[0].axhline(0, color="black", lw=1)`  
  Traza una línea horizontal negra en 0: el error «perfecto».
- `ejes[0].set(title="Residuos frente a predicción", xlabel="Precio predicho (€)", ylabel="Residuo (€)")`  
  Pone título y nombre a los ejes del gráfico izquierdo.
- `sns.histplot(residuos, bins=30, ax=ejes[1], color="#2a6f97")`  
  Dibuja en el gráfico derecho el **histograma** de los residuos: cuántas reservas tienen cada tamaño de error (`bins=30` = 30 barras).
- `ejes[1].set(title="Distribución de los residuos", xlabel="Residuo (€)", ylabel="Reservas")`  
  Título y nombres de ejes del gráfico derecho.
- `plt.tight_layout()`  
  Ajusta los márgenes para que no se solapen los textos.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **Embudo = el error crece con el precio.** Es una señal de que al modelo le falta algo (aquí, interacciones entre habitación y temporada).
- Una campana centrada en 0 es buena señal, pero **no sustituye** a mirar la nube de la izquierda.
- Mirar los residuos es la forma de **diagnosticar** un modelo: no basta con un número (R²).

### 👀 A7 · Ejemplo — Interacciones con validación cruzada

**Qué vamos a hacer y qué debe salir**

El embudo de A6 sugiere que el efecto de la temporada alta **depende** del tipo de habitación: sube más en una suite que en una estándar. Un modelo lineal puro no puede expresarlo (solo suma efectos), pero se arregla añadiendo **interacciones**: columnas nuevas que son el **producto** de dos variables (por ejemplo, `suite × temporada_alta`). Para comparar con honestidad usamos **validación cruzada**: en vez de un único examen, se parte el entrenamiento en 5 trozos y se entrena y evalúa 5 veces, rotando el trozo de examen; la nota es la media. **Debe salir** `R² CV lineal: 0.924 · con interacciones: 0.933`: las interacciones mejoran algo. Se apoya en `X` e `y` (A2) y prepara el ejercicio 3.

```python
lineal = LinearRegression()
con_interacciones = make_pipeline(PolynomialFeatures(degree=2, interaction_only=True, include_bias=False),
                                  LinearRegression())
r2_lineal_cv = cross_val_score(lineal, X, y, cv=5, scoring="r2").mean()
r2_inter_cv = cross_val_score(con_interacciones, X, y, cv=5, scoring="r2").mean()
print(f"R² CV lineal: {r2_lineal_cv:.3f} · con interacciones: {r2_inter_cv:.3f}")
```

**Línea a línea**

- `lineal = LinearRegression()`  
  El modelo lineal normal, sin ajustar todavía.
- `con_interacciones = make_pipeline(PolynomialFeatures(degree=2, interaction_only=True, include_bias=False),` … `LinearRegression())` (2 líneas)  
  Un **pipeline** de dos pasos: primero `PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)` crea las columnas de productos (solo **interacciones**, sin cuadrados y sin la columna de unos); después `LinearRegression()` ajusta sobre todo ello. Con 4 columnas salen 4 originales + 6 productos; de esos productos, los útiles son los de cada habitación con `temporada_alta` (los productos entre dos tipos de habitación valen siempre 0, porque una reserva no es de dos tipos a la vez).
- `r2_lineal_cv = cross_val_score(lineal, X, y, cv=5, scoring="r2").mean()`  
  `cross_val_score(..., cv=5, scoring="r2")` entrena y puntúa 5 veces y devuelve 5 notas; `.mean()` las promedia. Es el R² del modelo lineal.
- `r2_inter_cv = cross_val_score(con_interacciones, X, y, cv=5, scoring="r2").mean()`  
  Lo mismo con el pipeline de interacciones.
- `print(f"R² CV lineal: {r2_lineal_cv:.3f} · con interacciones: {r2_inter_cv:.3f}")`  
  Escribe las dos notas para compararlas.

**Lo destacable**

- **Interacción** = el efecto de una variable **depende** de otra. Se crea multiplicando columnas.
- La validación cruzada da una nota **más fiable** que un solo reparto train/test.
- El pipeline hace que el modelo con interacciones se use **igual** que uno normal (`fit`, `predict`).

### ✏️ A8 · Ejercicio — Error de las interacciones en test

**Qué vamos a hacer y qué debe salir**

Ahora comprobamos la mejora con el mismo examen de test de A3, para comparar **el mismo error (MAE) en las mismas reservas**. Ajustamos el pipeline `con_interacciones` con train, medimos su MAE en test y calculamos cuántos euros se gana respecto al modelo lineal de A3. **Debe salir** `MAE sin interacciones: 7.24 € · con interacciones: 6.76 € · mejora: 0.48 €` y `✔ Ejercicio 3 correcto`. La mejora es modesta (un 7 % menos de error): las interacciones corrigen **solo una parte** del embudo. Se apoya en `con_interacciones` (A7) y en `mae_test` (A3).

```python
con_interacciones.fit(X_train, y_train)
mae_inter_test = mean_absolute_error(y_test, con_interacciones.predict(X_test))
mejora_mae = mae_test - mae_inter_test
assert mae_inter_test < mae_test, "Las interacciones deberían reducir el error"
assert mejora_mae > 0.3, "La mejora debería ser apreciable (más de 0,3 €)"
print(f"MAE sin interacciones: {mae_test:.2f} € · con interacciones: {mae_inter_test:.2f} € · mejora: {mejora_mae:.2f} €")
print("✔ Ejercicio 3 correcto")
```

**Línea a línea**

- `con_interacciones.fit(X_train, y_train)`  
  Ajusta el pipeline con las reservas de train: primero crea las columnas de interacción y luego aprende los coeficientes.
- `mae_inter_test = mean_absolute_error(y_test, con_interacciones.predict(X_test))`  
  Mide su MAE en test: `predict(X_test)` aplica el mismo pipeline (crea las interacciones y predice).
- `mejora_mae = mae_test - mae_inter_test`  
  Resta el MAE nuevo al anterior: positivo = mejora, en euros por noche.
- `assert mae_inter_test < mae_test, "Las interacciones deberían reducir el error"` … `assert mejora_mae > 0.3, "La mejora debería ser apreciable (más de 0,3 €)"` (2 líneas)  
  Dos comprobaciones: el error debe bajar y la mejora debe ser apreciable (más de 0,3 €).
- `print(f"MAE sin interacciones: {mae_test:.2f} € · con interacciones: {mae_inter_test:.2f} € · mejora: {mejora_mae:.2f} €")`  
  Escribe el MAE sin y con interacciones y la mejora.
- `print("✔ Ejercicio 3 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- Se compara **con el mismo test y la misma métrica**: así la mejora (0,48 €) es honesta.
- Un modelo algo más rico mejora, pero **no mágicamente**: aquí 0,48 € por noche.
- `fit` sobre el pipeline entrena **todos** sus pasos; `predict` los aplica en el mismo orden.

### 👀 A9 · Ejemplo — Polinomios de grado 1 a 12

**Qué vamos a hacer y qué debe salir**

¿Y si, en vez de interacciones, dejamos al modelo **curvarse**? Un **polinomio** de grado `g` añade columnas con la variable elevada a 2, 3… g, y permite curvas más flexibles. Lo probamos con el **mes de llegada** para predecir el precio de las habitaciones estándar, con grados del 1 al 12. **Debe salir** dos gráficos. A la izquierda, la nube de reservas estándar por mes con dos curvas: grado 2 (roja) y grado 8 (azul). A la derecha, el R² en validación cruzada según el grado, que sube de 0,03 (grado 1) hasta unos 0,60 (grado 12) y se estabiliza. La lección: **a más grado, más flexible, y más riesgo de memorizar el ruido**; la nota de validación cruzada es la que dice si realmente mejora. Y atención: el grado 2 solo llega a 0,09, un mal resultado que se aprovecha en el ejercicio 4.

```python
est = df[df["tipo_habitacion"] == "estandar"]
X_mes, y_est = est[["mes_llegada"]], est["precio_noche"]
grados = list(range(1, 13))
r2_por_grado = []
for g in grados:
    m = make_pipeline(PolynomialFeatures(g), StandardScaler(), LinearRegression())
    r2_por_grado.append(cross_val_score(m, X_mes, y_est, cv=5, scoring="r2").mean())

mes_ord = pd.DataFrame({"mes_llegada": range(1, 13)})
plt.figure(figsize=(11, 4))
plt.subplot(1, 2, 1)
plt.scatter(est["mes_llegada"], est["precio_noche"], s=8, alpha=0.3, color="gray", label="Reservas estándar")
for g, c in [(2, "#e63946"), (8, "#2a6f97")]:
    m = make_pipeline(PolynomialFeatures(g), StandardScaler(), LinearRegression()).fit(X_mes, y_est)
    plt.plot(mes_ord, m.predict(mes_ord), color=c, lw=2, label=f"Grado {g}")
plt.title("Precio de la estándar según el mes")
plt.xlabel("Mes de llegada")
plt.ylabel("Precio por noche (€)")
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(grados, r2_por_grado, marker="o", color="#2a6f97")
plt.title("R² (validación cruzada) según el grado")
plt.xlabel("Grado del polinomio")
plt.ylabel("R²")
plt.tight_layout()
plt.show()
```

**Línea a línea**

- `est = df[df["tipo_habitacion"] == "estandar"]`  
  Se queda solo con las reservas de habitación estándar (`df[condición]` filtra filas): así el precio solo depende de la época.
- `X_mes, y_est = est[["mes_llegada"]], est["precio_noche"]`  
  `X_mes` es la única variable (el mes, entre dobles corchetes para que sea una tabla) e `y_est` el precio de esas reservas.
- `grados = list(range(1, 13))`  
  La lista de grados a probar: del 1 al 12 (`range(1, 13)` llega hasta el 12).
- `r2_por_grado = []`  
  Lista vacía donde se guardará el R² de cada grado.
- `for g in grados:` … `r2_por_grado.append(cross_val_score(m, X_mes, y_est, cv=5, scoring="r2").mean())` (3 líneas)  
  Bucle: para cada grado `g` monta un pipeline (polinomio de grado `g` → escalado → regresión lineal) y calcula su R² en validación cruzada con 5 trozos; el resultado se añade con `append` a `r2_por_grado`. El **escalado** (`StandardScaler`) es necesario porque con grados altos los valores (mes elevado a 12) se disparan y el cálculo se vuelve inestable.
- `mes_ord = pd.DataFrame({"mes_llegada": range(1, 13)})`  
  Tabla con los meses del 1 al 12, para dibujar las curvas suavemente.
- `plt.figure(figsize=(11, 4))`  
  Crea la figura (11×4 pulgadas).
- `plt.subplot(1, 2, 1)`  
  Empieza el primer gráfico (1 fila, 2 columnas, el primero).
- `plt.scatter(est["mes_llegada"], est["precio_noche"], s=8, alpha=0.3, color="gray", label="Reservas estándar")`  
  Dibuja la nube de reservas estándar: mes (horizontal) frente a precio (vertical), en gris y transparente.
- `for g, c in [(2, "#e63946"), (8, "#2a6f97")]:` … `plt.plot(mes_ord, m.predict(mes_ord), color=c, lw=2, label=f"Grado {g}")` (3 líneas)  
  Para el grado 2 (rojo) y el 8 (azul): ajusta ese polinomio con todos los datos, predice el precio de cada mes y dibuja la curva con `plt.plot`.
- `plt.title("Precio de la estándar según el mes")` … `plt.legend()` (4 líneas)  
  Título, nombres de los ejes y leyenda del primer gráfico.
- `plt.subplot(1, 2, 2)`  
  Empieza el segundo gráfico.
- `plt.plot(grados, r2_por_grado, marker="o", color="#2a6f97")`  
  Dibuja el R² de validación cruzada según el grado, con un punto en cada grado (`marker="o"`).
- `plt.title("R² (validación cruzada) según el grado")` … `plt.ylabel("R²")` (3 líneas)  
  Título y nombres de ejes del segundo gráfico.
- `plt.tight_layout()`  
  Ajusta márgenes.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **Más grado ≠ mejor:** el grado 8 se ajusta a la nube pero puede estar memorizando el ruido; la validación cruzada es el árbitro.
- Con polinomios hay que **escalar** (`StandardScaler`), o los números enormes desestabilizan el modelo.
- El R² del grado 2 (0,09) frente a otras opciones es clave para el ejercicio siguiente: **elegir una buena variable vale más que subir el grado**.

### ✏️ A10 · Ejercicio — Polinomio sobre el mes o variable temporada_alta

**Qué vamos a hacer y qué debe salir**

Cierre del bloque de polinomios: comparar dos formas de usar la época del año en la estándar. Una es un **polinomio de grado 2 sobre el mes** (curva). La otra es **una sola columna**, `temporada_alta` (0/1), que resume lo que sabemos del negocio. **Debe salir** `Grado 2 sobre el mes: R² = 0.09 · temporada_alta (1 columna): R² = 0.65` y `✔ Ejercicio 4 correcto`. Gana de largo la variable simple: **7 veces más R²** con una sola columna. La lección es de fondo: antes de complicar el modelo (más grado, más columnas), conviene **pensar mejor la variable**. Se apoya en `est`, `y_est` y `cross_val_score` de A9.

```python
r2_grado2 = cross_val_score(make_pipeline(PolynomialFeatures(2), LinearRegression()),
                            est[["mes_llegada"]], y_est, cv=5, scoring="r2").mean()
r2_alta = cross_val_score(LinearRegression(), est[["temporada_alta"]], y_est, cv=5, scoring="r2").mean()
assert r2_alta > r2_grado2, "La variable temporada_alta debería rendir más que un polinomio de grado 2 sobre el mes"
assert r2_alta > 0.5, "temporada_alta debería explicar más de la mitad de la variación del precio de la estándar"
print(f"Grado 2 sobre el mes: R² = {r2_grado2:.2f} · temporada_alta (1 columna): R² = {r2_alta:.2f}")
print("✔ Ejercicio 4 correcto")
```

**Línea a línea**

- `r2_grado2 = cross_val_score(make_pipeline(PolynomialFeatures(2), LinearRegression()),` … `est[["mes_llegada"]], y_est, cv=5, scoring="r2").mean()` (2 líneas)  
  R² en validación cruzada de un pipeline con `PolynomialFeatures(2)` + regresión lineal, usando solo el mes como variable.
- `r2_alta = cross_val_score(LinearRegression(), est[["temporada_alta"]], y_est, cv=5, scoring="r2").mean()`  
  R² en validación cruzada de una regresión lineal con la columna `temporada_alta`.
- `assert r2_alta > r2_grado2, "La variable temporada_alta debería rendir más que un polinomio de grado 2 sobre el mes"` … `assert r2_alta > 0.5, "temporada_alta debería explicar más de la mitad de la variación del precio de la estándar"` (2 líneas)  
  Dos comprobaciones: `temporada_alta` debe rendir más que el polinomio de grado 2 y explicar más de la mitad de la variación del precio.
- `print(f"Grado 2 sobre el mes: R² = {r2_grado2:.2f} · temporada_alta (1 columna): R² = {r2_alta:.2f}")`  
  Escribe los dos R² para compararlos.
- `print("✔ Ejercicio 4 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Una variable bien pensada (`temporada_alta`) vence a un modelo más complejo.** Esto se llama *feature engineering*: crear buenas columnas.
- Un precio que sube en bloque en unos meses y no en otros se parece más a un **escalón** (0/1) que a una **curva** suave.
- Se mide siempre con validación cruzada, no a ojo del gráfico.

### 🎯 A11 · Mini-reto — Función precio_recomendado

**Qué vamos a hacer y qué debe salir**

Mini-reto: ponemos el modelo a trabajar. En lugar de leer coeficientes, creamos una **función** que, dado un tipo de habitación y si es temporada alta, devuelve el **precio recomendado** en euros: algo que cualquiera del equipo de reservas podría usar. **Debe salir** `Estándar en baja: 67 € · Suite en alta: 191 €` y `✔ Mini-reto correcto`. Salen de sumar los coeficientes de A5: 67,3 para la estándar en temporada baja; 67,3 + 101,2 + 22,4 = 190,9 ≈ 191 para una suite en temporada alta. Se apoya en `modelo_lin` (A3), en las columnas de `X` (A2) y en la lectura de coeficientes (A5).

```python
def precio_recomendado(tipo, alta):
    fila = pd.DataFrame([{c: 0 for c in X.columns}])
    if f"tipo_habitacion_{tipo}" in fila.columns:
        fila[f"tipo_habitacion_{tipo}"] = 1
    fila["temporada_alta"] = alta
    return float(modelo_lin.predict(fila)[0])
p_std_baja = precio_recomendado("estandar", 0)
p_suite_alta = precio_recomendado("suite", 1)
assert 60 < p_std_baja < 80, "Una estándar en temporada baja ronda 70 €"
assert p_suite_alta > 180, "Una suite en temporada alta debería superar los 180 €"
print(f"Estándar en baja: {p_std_baja:.0f} € · Suite en alta: {p_suite_alta:.0f} €")
print("✔ Mini-reto correcto")
```

**Línea a línea**

- `def precio_recomendado(tipo, alta):`  
  Define la función: recibe el `tipo` de habitación y `alta` (1 si es temporada alta, 0 si no).
- `fila = pd.DataFrame([{c: 0 for c in X.columns}])`  
  Crea una tabla de **una sola fila** con todas las columnas de `X` a 0 (`{c: 0 for c in X.columns}` es un diccionario columna → 0).
- `if f"tipo_habitacion_{tipo}" in fila.columns:` … `fila[f"tipo_habitacion_{tipo}"] = 1` (2 líneas)  
  Si existe la columna de ese tipo (por ejemplo `tipo_habitacion_suite`), pone un 1. La **estándar no tiene columna** (se quitó con `drop_first`), así que se queda todo a 0: eso ya la representa.
- `fila["temporada_alta"] = alta`  
  Rellena la época: 1 o 0.
- `return float(modelo_lin.predict(fila)[0])`  
  Pide el precio al modelo (`predict` devuelve una lista; `[0]` toma el primer valor) y lo devuelve como número.
- `p_std_baja = precio_recomendado("estandar", 0)`  
  Usa la función: estándar en temporada baja.
- `p_suite_alta = precio_recomendado("suite", 1)`  
  Usa la función: suite en temporada alta.
- `assert 60 < p_std_baja < 80, "Una estándar en temporada baja ronda 70 €"` … `assert p_suite_alta > 180, "Una suite en temporada alta debería superar los 180 €"` (2 líneas)  
  Dos comprobaciones: la estándar en baja ronda los 70 € y la suite en alta supera los 180 €.
- `print(f"Estándar en baja: {p_std_baja:.0f} € · Suite en alta: {p_suite_alta:.0f} €")`  
  Escribe los dos precios redondeados (`:.0f` = sin decimales).
- `print("✔ Mini-reto correcto")`  
  Aviso de que el mini-reto está bien.

**Lo destacable**

- Una **función** envuelve un modelo para que se use sin saber cómo está hecho: ese es el paso de «análisis» a «herramienta».
- La fila que se pasa a `predict` debe tener **las mismas columnas y en el mismo orden** que `X`: por eso se parte de una fila con todas las columnas a 0.
- Los 67 € de la estándar en baja no coinciden con el precio real (≈ 70 €): es lo que **el ajuste conjunto** predice, y es normal que difiera un poco.
