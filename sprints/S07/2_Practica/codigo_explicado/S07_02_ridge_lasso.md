# Código explicado · S07.02 · Regularización: Ridge y Lasso

> **Para qué sirve.** Aquí está **todo el código del cuaderno explicado por escrito**, celda a celda y en el mismo orden. Cada bloque sigue siempre el mismo guion: **primero** un párrafo que dice qué vamos a hacer, por qué y qué debe salir; **después** el código, con **cada línea explicada**; y **al final** lo destacable del bloque (lo que conviene recordar y con qué se relaciona).
>
> **Cuaderno:** [🏫 en clase](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_02_ridge_lasso_en_clase.ipynb) · [🏠 completo](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_02_ridge_lasso.ipynb)
>
> **Cómo usarlo:** ejecuta la celda en el cuaderno; busca aquí la del mismo número (A3, A5…); lee el párrafo, sigue el código línea a línea y, al terminar, cambia algo (un número, una columna) y comprueba si pasa lo que esperabas: es la mejor manera de entender código.

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda** («coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`»). Lo que va tras `#` es un comentario: Python lo ignora. Los ejercicios (✏️) llevan aquí la **solución de referencia**: úsala **después** de intentarlo.

## La idea del cuaderno

TurisData abre un **alojamiento nuevo** y solo tiene **120 reservas** para estimar su tarifa. Con tan pocos datos y **muchas variables** (35 columnas y, además, todas sus combinaciones), un modelo lineal «normal» se **sobreajusta**: se aprende de memoria hasta el ruido y falla con reservas nuevas. La solución se llama **regularizar**: penalizar los coeficientes grandes para que el modelo se mantenga sencillo.

- **Hilo del cuaderno:** montamos un modelo «generoso» con 665 columnas (A2) → medimos su sobreajuste (A3) → vemos cómo **Ridge** y **Lasso** encogen los coeficientes (A4) → elegimos la fuerza de la penalización con validación cruzada (A5, A6) → miramos qué variables conserva Lasso (A7) → comparamos los tres modelos (A8) → vemos cuántos datos hacen falta (A9).
- **Lo que te llevas:** train perfecto + test mediocre = sobreajuste; **Ridge** encoge todo, **Lasso** además **anula** lo que no sirve (selecciona variables); la fuerza `alpha` se elige **dentro de train**, nunca mirando el test; y con más datos la regularización pesa menos.

## Mapa de celdas

| Celda | Tipo | Qué hacemos | ¿Dónde? |
|---|---|---|---|
| A1 | ⚙️ Preparación | Preparar las herramientas y los datos | 🏫 |
| A2 | 👀 Ejemplo | Un modelo generoso con 120 reservas | 🏫 |
| A3 | ✏️ Ejercicio | Medir la brecha de sobreajuste | 🏫 |
| A4 | 👀 Ejemplo | Trayectorias de los coeficientes: Ridge frente a Lasso | 🏫 |
| A5 | ✏️ Ejercicio | Ridge con alpha elegido por validación cruzada | 🏫 |
| A6 | ✏️ Ejercicio | Lasso: seleccionar variables | 🏫 |
| A7 | 👀 Ejemplo | Qué variables ha conservado Lasso | 🏫 |
| A8 | 👀 Ejemplo | Tabla comparativa de los tres modelos | 🏠 |
| A9 | 🎯 Mini-reto | Curva de R² según el número de reservas | 🏠 |

🏫 = en clase · 🏠 = en casa. 👀 ejemplo: solo se ejecuta y se mira. ✏️ ejercicio: se completa con tu código. ⚙️ preparación: se ejecuta sola.

## Celda a celda

### ⚙️ A1 · Preparación — Preparar las herramientas y los datos

**Qué vamos a hacer y qué debe salir**

Celda de preparación: se ejecuta **la primera** y no hace falta entenderla para empezar. Trae las librerías, carga las reservas, prepara las variables y **simula el alojamiento nuevo**: de las 6000 reservas, solo **120** se usan para entrenar y las otras **5880** para evaluar. También define `prep`, el preprocesado que **escala** las columnas numéricas y convierte las de texto en columnas 0/1. **Debe salir** `Reservas para entrenar: 120 · para evaluar: 5880` y `Listo ✔`. Todo lo que sigue usa `X_train`, `y_train`, `X_test`, `y_test` y `prep`.

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

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, RidgeCV, LassoCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.base import clone

warnings.filterwarnings("ignore", category=UserWarning)
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["mes_llegada"] = df["fecha_llegada"].dt.month
df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)
df["pais_origen"] = df["pais_origen"].fillna("desconocido")

columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especiales",
                "cliente_repetidor", "cancelaciones_previas", "mes_llegada", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["precio_noche"]

# Simulamos el alojamiento nuevo: solo 120 reservas para entrenar, el resto para evaluar
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=120, random_state=SEMILLA)
print("Reservas para entrenar:", len(X_train), "· para evaluar:", len(X_test))

prep = ColumnTransformer([("num", StandardScaler(), columnas_num),
                          ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), columnas_cat)])
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
- `import warnings`  
  Trae `warnings`, para poder silenciar avisos que no aportan nada.
- `import numpy as np`  
  Trae **NumPy** (`np`): operaciones con números.
- `import pandas as pd`  
  Trae **pandas** (`pd`): las tablas de datos.
- `import matplotlib.pyplot as plt`  
  Trae **matplotlib** (`plt`): gráficos.
- `import seaborn as sns`  
  Trae **seaborn** (`sns`): gráficos más cuidados.
- `from sklearn.model_selection import train_test_split`  
  Trae `train_test_split`: reparte los datos en entrenamiento y prueba.
- `from sklearn.linear_model import LinearRegression, Ridge, Lasso, RidgeCV, LassoCV`  
  Trae el modelo normal (`LinearRegression`), los dos regularizados (`Ridge`, `Lasso`) y sus versiones que **eligen solos la penalización** con validación cruzada (`RidgeCV`, `LassoCV`).
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures`  
  Trae `StandardScaler` (escala números), `OneHotEncoder` (texto → columnas 0/1) y `PolynomialFeatures` (crea combinaciones de columnas).
- `from sklearn.compose import ColumnTransformer`  
  Trae `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas.
- `from sklearn.pipeline import make_pipeline`  
  Trae `make_pipeline`: encadena pasos en un solo objeto.
- `from sklearn.base import clone`  
  Trae `clone`: crea una copia de un objeto sin entrenar (con los mismos ajustes).
- `warnings.filterwarnings("ignore", category=UserWarning)`  
  Oculta los avisos de tipo `UserWarning` para que la salida quede limpia.
- `SEMILLA = 42`  
  Número fijo (`42`) para que los sorteos salgan siempre igual y tus resultados coincidan con los de este documento.
- `sns.set_theme(style="whitegrid")`  
  Estilo visual de los gráficos.
- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])`  
  Lee las reservas en la tabla `df`; `parse_dates` marca esas dos columnas como fechas.
- `df["mes_llegada"] = df["fecha_llegada"].dt.month`  
  Crea la columna `mes_llegada` (1 a 12) a partir de la fecha de llegada.
- `df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)`  
  Crea `temporada_alta` (1 si el mes es 1, 2, 3, 7, 8 o 12; 0 si no).
- `df["pais_origen"] = df["pais_origen"].fillna("desconocido")`  
  Rellena con «desconocido» los países que faltan (`fillna`): un `OneHotEncoder` no admite huecos.
- `columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especiales",` … `"cliente_repetidor", "cancelaciones_previas", "mes_llegada", "temporada_alta"]` (2 líneas)  
  La lista de **columnas numéricas** (9): antelación, noches, adultos, niños, peticiones, cliente repetidor, cancelaciones previas, mes y temporada alta.
- `columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]`  
  La lista de **columnas de texto** (6): tipo de habitación, régimen, canal, país, tarifa y depósito.
- `X, y = df[columnas_num + columnas_cat], df["precio_noche"]`  
  `X` = las 15 variables con las que se predice; `y` = lo que se quiere predecir (`precio_noche`).
- `# Simulamos el alojamiento nuevo: solo 120 reservas para entrenar, el resto para evaluar`  
  Comentario: explica la línea siguiente.
- `X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=120, random_state=SEMILLA)`  
  Reparte los datos: **solo 120 reservas para entrenar** (`train_size=120`) y todas las demás para evaluar. Así se simula un alojamiento nuevo con pocos datos.
- `print("Reservas para entrenar:", len(X_train), "· para evaluar:", len(X_test))`  
  Escribe cuántas reservas hay en cada parte: 120 y 5880.
- `prep = ColumnTransformer([("num", StandardScaler(), columnas_num),` … `("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), columnas_cat)])` (2 líneas)  
  Define el preprocesado: las columnas numéricas se **escalan** (`StandardScaler`: media 0, desviación 1) y las de texto pasan a **columnas 0/1** (`OneHotEncoder`; `handle_unknown="ignore"` evita errores si en test aparece una categoría nueva; `sparse_output=False` entrega una tabla normal). Resultado: 35 columnas numéricas.
- `print("Listo ✔")`  
  Mensaje de que todo ha ido bien.

**Lo destacable**

- La celda de preparación **se ejecuta siempre la primera**, y otra vez si Colab se reinicia: todas las demás celdas usan lo que crea aquí (`df`, `SEMILLA`, las librerías…). Si ves `NameError: name '…' is not defined`, casi siempre es que falta ejecutarla.
- **Escalar** es imprescindible en esta práctica: la penalización de Ridge y Lasso es justa solo si todas las columnas están en la misma escala.
- `train_size=120` es lo que crea el problema del cuaderno: **pocos datos y muchas columnas**.

### 👀 A2 · Ejemplo — Un modelo generoso con 120 reservas

**Qué vamos a hacer y qué debe salir**

Construimos un modelo «generoso»: las 35 variables originales **y todas sus combinaciones de grado 2** (productos y cuadrados). Salen **665 columnas para solo 120 filas**, y eso es un problema: el modelo tiene tanta libertad que puede pasar por todos los puntos de entrenamiento y aprenderse hasta el ruido. Dejamos la construcción dentro de una función, `modelo_con`, para reutilizarla con distintos regresores en el resto del cuaderno. **Debe salir** `Número de columnas del modelo: 665` y `R² en entrenamiento: 1.000 · R² en prueba: 0.716`: perfecto con lo que ha visto, mediocre con lo que no. Se apoya en `prep` y en el reparto de A1.

```python
def modelo_con(regresor):
    """Preprocesado + variables de grado 2 + escalado + regresor."""
    return make_pipeline(clone(prep), PolynomialFeatures(2, include_bias=False), StandardScaler(), regresor)

ols = modelo_con(LinearRegression()).fit(X_train, y_train)
print("Número de columnas del modelo:", ols[-1].coef_.shape[0])
print(f"R² en entrenamiento: {ols.score(X_train, y_train):.3f} · R² en prueba: {ols.score(X_test, y_test):.3f}")
```

**Línea a línea**

- `def modelo_con(regresor):`  
  Define una función que recibe un **regresor** (el modelo final: lineal, Ridge, Lasso…) y devuelve el pipeline completo.
- `"""Preprocesado + variables de grado 2 + escalado + regresor."""`  
  Descripción de la función (no hace nada).
- `return make_pipeline(clone(prep), PolynomialFeatures(2, include_bias=False), StandardScaler(), regresor)`  
  Encadena 4 pasos: (1) `clone(prep)`: una copia limpia del preprocesado; (2) `PolynomialFeatures(2, include_bias=False)`: crea los cuadrados y los productos de cada par de columnas (de 35 salen 35 + 595 + 35 = **665**); (3) `StandardScaler()`: vuelve a escalar las columnas nuevas; (4) el regresor que se pasó.
- `ols = modelo_con(LinearRegression()).fit(X_train, y_train)`  
  Monta el pipeline con una regresión lineal **normal** (`LinearRegression`, sin penalizar) y lo ajusta con las 120 reservas. `ols` viene de *ordinary least squares* (mínimos cuadrados).
- `print("Número de columnas del modelo:", ols[-1].coef_.shape[0])`  
  `ols[-1]` es el **último paso** del pipeline (la regresión); `.coef_` son sus coeficientes y `.shape[0]` cuántos hay: 665, uno por columna.
- `print(f"R² en entrenamiento: {ols.score(X_train, y_train):.3f} · R² en prueba: {ols.score(X_test, y_test):.3f}")`  
  `ols.score(X, y)` da el R² del modelo con esos datos: con `X_train` mide lo que **memorizó**; con `X_test`, lo que **generaliza**.

**Lo destacable**

- **R² de 1,000 con 665 columnas y 120 filas no es una buena noticia:** el modelo se sabe las respuestas, no ha aprendido el patrón.
- Hay **muchas más columnas que filas**: ese es el escenario típico del sobreajuste.
- En el cuaderno, 96 de esas 665 columnas valen siempre 0 (productos imposibles, como dos tipos de habitación a la vez): sus coeficientes son 0 en cualquier modelo.
- `pipeline[-1]` y `pipeline[:-1]` sirven para coger el último paso o todos los anteriores: se usarán en A5, A6 y A7.

### ✏️ A3 · Ejercicio — Medir la brecha de sobreajuste

**Qué vamos a hacer y qué debe salir**

El síntoma del sobreajuste se mide con una resta: el R² en entrenamiento menos el R² en test, la **brecha**. Cerca de 0 es sano (el modelo rinde igual con datos nuevos); grande es sobreajuste. Aquí guardamos las tres cifras en variables para poder usarlas después. **Debe salir** `R² train = 1.000 · R² test = 0.716 · brecha = 0.284` y `✔ Ejercicio 1 correcto`. Una brecha de 0,28 es grande: el modelo **memoriza**. Se apoya en `ols` (A2); y `r2_test_ols` volverá como referencia en A5.

```python
r2_train_ols = ols.score(X_train, y_train)
r2_test_ols = ols.score(X_test, y_test)
brecha_ols = r2_train_ols - r2_test_ols
assert r2_train_ols > 0.99, "En train el R² debería ser casi 1: el modelo memoriza"
assert brecha_ols > 0.2, "La brecha debería ser grande (sobreajuste)"
print(f"R² train = {r2_train_ols:.3f} · R² test = {r2_test_ols:.3f} · brecha = {brecha_ols:.3f}")
print("✔ Ejercicio 1 correcto")
```

**Línea a línea**

- `r2_train_ols = ols.score(X_train, y_train)`  
  R² del modelo con los datos con los que aprendió (`X_train`, `y_train`).
- `r2_test_ols = ols.score(X_test, y_test)`  
  R² con datos que **no** ha visto (`X_test`, `y_test`).
- `brecha_ols = r2_train_ols - r2_test_ols`  
  La resta: cuánto peor funciona con datos nuevos.
- `assert r2_train_ols > 0.99, "En train el R² debería ser casi 1: el modelo memoriza"` … `assert brecha_ols > 0.2, "La brecha debería ser grande (sobreajuste)"` (2 líneas)  
  Dos comprobaciones: en train el R² debe ser casi 1 (memoriza) y la brecha debe ser grande (más de 0,2).
- `print(f"R² train = {r2_train_ols:.3f} · R² test = {r2_test_ols:.3f} · brecha = {brecha_ols:.3f}")`  
  Escribe las tres cifras con 3 decimales.
- `print("✔ Ejercicio 1 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Detector de sobreajuste:** R² train − R² test. Cerca de 0: sano. Grande: el modelo memoriza.
- Los dos remedios que verás: **penalizar** los coeficientes (Ridge y Lasso) o **conseguir más datos** (mini-reto, A9).
- `score(X_train…)` vs `score(X_test…)`: la misma función con datos distintos cuenta dos historias distintas.

### 👀 A4 · Ejemplo — Trayectorias de los coeficientes: Ridge frente a Lasso

**Qué vamos a hacer y qué debe salir**

Aquí se ve **con los ojos** la diferencia entre Ridge y Lasso. Ambos minimizan el error **más una penalización** que crece con el tamaño de los coeficientes; la fuerza de esa penalización se llama `alpha`. Ridge penaliza la **suma de cuadrados** (`alpha · Σ coef²`); Lasso, la **suma de valores absolutos** (`alpha · Σ |coef|`). Para verlo, entrenamos muchos modelos con `alpha` creciente (de 0,01 a 1000) y dibujamos cómo se mueve cada coeficiente. Se usa un modelo **sencillo** (sin polinomios: las 35 columnas de `prep`) para que el gráfico sea legible. **Debe salir** dos gráficos con muchas líneas: en Ridge se acercan **suavemente** a 0 al subir `alpha`; en Lasso van **cayendo a 0 una tras otra**, hasta que todas valen 0. Se apoya en `prep` y en el reparto de A1.

```python
Xp_train = prep.fit_transform(X_train)
nombres = prep.get_feature_names_out()
alphas = np.logspace(-2, 3, 30)
trayectoria_ridge = np.array([Ridge(alpha=a).fit(Xp_train, y_train).coef_ for a in alphas])
trayectoria_lasso = np.array([Lasso(alpha=a, max_iter=50000).fit(Xp_train, y_train).coef_ for a in alphas])

fig, ejes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)
for ax, tray, titulo in [(ejes[0], trayectoria_ridge, "Ridge (L2): los coeficientes se encogen"),
                         (ejes[1], trayectoria_lasso, "Lasso (L1): los coeficientes llegan a cero")]:
    ax.plot(alphas, tray, lw=1)
    ax.set_xscale("log")
    ax.set(title=titulo, xlabel="alpha (escala logarítmica)")
    ax.axhline(0, color="black", lw=0.8)
ejes[0].set_ylabel("Valor del coeficiente (€)")
plt.tight_layout()
plt.show()
```

**Línea a línea**

- `Xp_train = prep.fit_transform(X_train)`  
  Aplica el preprocesado a train (`fit_transform`: aprende cómo escalar y codificar **y** lo aplica). `Xp_train` es la tabla ya numérica y escalada.
- `nombres = prep.get_feature_names_out()`  
  Guarda el nombre de cada columna resultante.
- `alphas = np.logspace(-2, 3, 30)`  
  30 valores de `alpha` espaciados en escala **logarítmica** entre 0,01 (`10⁻²`) y 1000 (`10³`).
- `trayectoria_ridge = np.array([Ridge(alpha=a).fit(Xp_train, y_train).coef_ for a in alphas])`  
  Para cada `alpha`: ajusta un `Ridge`, toma sus coeficientes (`.coef_`) y los junta todos en una matriz (`np.array([... for a in alphas])`): una fila por `alpha`, una columna por variable.
- `trayectoria_lasso = np.array([Lasso(alpha=a, max_iter=50000).fit(Xp_train, y_train).coef_ for a in alphas])`  
  Lo mismo con `Lasso`; `max_iter=50000` le da margen para converger y evitar avisos.
- `fig, ejes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)`  
  Crea la figura con **dos gráficos** lado a lado; `sharey=True` hace que compartan el eje vertical para poder compararlos.
- `for ax, tray, titulo in [(ejes[0], trayectoria_ridge, "Ridge (L2): los coeficientes se encogen"),` … `(ejes[1], trayectoria_lasso, "Lasso (L1): los coeficientes llegan a cero")]:` (2 líneas)  
  Recorre dos parejas: (gráfico izquierdo, trayectoria de Ridge, su título) y (gráfico derecho, trayectoria de Lasso, su título).
- `ax.plot(alphas, tray, lw=1)`  
  Dibuja una línea por coeficiente: `alpha` en horizontal, valor del coeficiente en vertical (`lw` = grosor).
- `ax.set_xscale("log")`  
  Eje horizontal en escala **logarítmica**: `alpha` recorre cinco órdenes de magnitud y en escala normal todo quedaría apelotonado junto al 0.
- `ax.set(title=titulo, xlabel="alpha (escala logarítmica)")`  
  Pone el título y el nombre del eje horizontal.
- `ax.axhline(0, color="black", lw=0.8)`  
  Línea negra en 0: ahí «se apagan» los coeficientes.
- `ejes[0].set_ylabel("Valor del coeficiente (€)")`  
  Nombre del eje vertical (solo en el de la izquierda; el otro lo comparte).
- `plt.tight_layout()`  
  Ajusta los márgenes.
- `plt.show()`  
  Muestra la figura.

**Lo destacable**

- **Ridge encoge, Lasso anula.** Ridge reparte el peso y rara vez deja un coeficiente exactamente en 0; Lasso lleva a 0 los coeficientes de las variables poco útiles.
- `alpha` es la **fuerza** del castigo: pequeño ≈ regresión normal; grande ≈ modelo sin variables.
- Hay que **escalar** antes de penalizar; si no, las columnas de valores pequeños saldrían castigadas de más (o de menos).
- Una **lista por comprensión** (`[... for a in alphas]`) es una forma corta de repetir algo para cada valor de una lista.

### ✏️ A5 · Ejercicio — Ridge con alpha elegido por validación cruzada

**Qué vamos a hacer y qué debe salir**

En A4 se ve cómo cambia el modelo con `alpha`, pero ¿qué valor usar? **No se elige mirando el test** (sería hacer trampa: el test dejaría de ser un examen honesto). Se elige **dentro de train** con **validación cruzada**, y eso es lo que hace `RidgeCV`: prueba una lista de `alpha` (aquí 30 valores entre 0,1 y 10 000), evalúa cada uno con varios trozos de train y se queda con el mejor. Después se mide una sola vez en test. **Debe salir** `Ridge: alpha = 25.9 · R² test = 0.728` y `✔ Ejercicio 2 correcto`. Mejora de 0,716 a 0,728: **poco**, porque Ridge conserva las 665 variables (las encoge, pero no las quita). Se apoya en `modelo_con` (A2) y en `r2_test_ols` (A3).

```python
ridge = modelo_con(RidgeCV(alphas=np.logspace(-1, 4, 30))).fit(X_train, y_train)
alpha_ridge = ridge[-1].alpha_
r2_test_ridge = ridge.score(X_test, y_test)
assert alpha_ridge > 0.1, "RidgeCV debe haber elegido un alpha > 0,1"
assert r2_test_ridge > r2_test_ols, "Ridge debería mejorar al modelo sin regularizar en test"
print(f"Ridge: alpha = {alpha_ridge:.1f} · R² test = {r2_test_ridge:.3f}")
print("✔ Ejercicio 2 correcto")
```

**Línea a línea**

- `ridge = modelo_con(RidgeCV(alphas=np.logspace(-1, 4, 30))).fit(X_train, y_train)`  
  Monta el pipeline con un `RidgeCV` (`alphas=np.logspace(-1, 4, 30)`: 30 valores entre 0,1 y 10 000) y lo ajusta con train. Al hacer `.fit`, `RidgeCV` **elige el mejor `alpha`** por validación cruzada.
- `alpha_ridge = ridge[-1].alpha_`  
  `ridge[-1]` es el último paso del pipeline (el Ridge); su atributo `.alpha_` (con guion bajo final) es el valor elegido.
- `r2_test_ridge = ridge.score(X_test, y_test)`  
  R² del modelo en test: el examen final, una sola vez.
- `assert alpha_ridge > 0.1, "RidgeCV debe haber elegido un alpha > 0,1"` … `assert r2_test_ridge > r2_test_ols, "Ridge debería mejorar al modelo sin regularizar en test"` (2 líneas)  
  Dos comprobaciones: que `alpha` sea mayor que 0,1 y que Ridge mejore al modelo sin regularizar en test.
- `print(f"Ridge: alpha = {alpha_ridge:.1f} · R² test = {r2_test_ridge:.3f}")`  
  Escribe el `alpha` elegido (1 decimal) y el R² en test (3 decimales).
- `print("✔ Ejercicio 2 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **`alpha` se elige con validación cruzada dentro de train**; el test se toca **una sola vez**, al final.
- Los atributos acabados en **guion bajo** (`alpha_`, `coef_`, `intercept_`) son cosas que el modelo **aprende al ajustarse**.
- Mejora pequeña (+0,012): Ridge **reduce** el sobreajuste, pero no lo **resuelve** mientras conserve todas las variables.

### ✏️ A6 · Ejercicio — Lasso: seleccionar variables

**Qué vamos a hacer y qué debe salir**

Ahora el mismo procedimiento con **Lasso**, que además de encoger **anula** coeficientes: hace **selección de variables**. `LassoCV` elige `alpha` con validación cruzada de 5 trozos (`cv=5`) y se queda con el mejor. Después medimos el R² en test y **contamos cuántos coeficientes** quedan distintos de cero. **Debe salir** `Lasso: R² test = 0.887 · coeficientes distintos de cero: 27 de 665` y `✔ Ejercicio 3 correcto`. Salto enorme: de 0,728 (Ridge) a **0,887**, con solo **27 de las 665** columnas (un 4 %). Se apoya en `modelo_con` (A2), y compara con A3 y A5.

```python
lasso = modelo_con(LassoCV(cv=5, max_iter=50000, random_state=SEMILLA)).fit(X_train, y_train)
r2_test_lasso = lasso.score(X_test, y_test)
n_no_cero = int(np.sum(lasso[-1].coef_ != 0))
assert r2_test_lasso > 0.8, "Lasso debería superar 0,8 de R² en test"
assert n_no_cero < 80, "Lasso debería quedarse con muy pocos coeficientes de los cientos posibles"
print(f"Lasso: R² test = {r2_test_lasso:.3f} · coeficientes distintos de cero: {n_no_cero} de {lasso[-1].coef_.shape[0]}")
print("✔ Ejercicio 3 correcto")
```

**Línea a línea**

- `lasso = modelo_con(LassoCV(cv=5, max_iter=50000, random_state=SEMILLA)).fit(X_train, y_train)`  
  Monta el pipeline con un `LassoCV` y lo ajusta con train. `cv=5`: validación cruzada de 5 trozos para elegir `alpha`; `max_iter=50000`: margen para converger; `random_state`: resultado reproducible.
- `r2_test_lasso = lasso.score(X_test, y_test)`  
  R² del modelo en test.
- `n_no_cero = int(np.sum(lasso[-1].coef_ != 0))`  
  Cuenta los coeficientes distintos de cero: `lasso[-1].coef_ != 0` marca cada uno con verdadero/falso, `np.sum` cuenta los verdaderos y `int(...)` lo deja como número entero.
- `assert r2_test_lasso > 0.8, "Lasso debería superar 0,8 de R² en test"` … `assert n_no_cero < 80, "Lasso debería quedarse con muy pocos coeficientes de los cientos posibles"` (2 líneas)  
  Dos comprobaciones: R² en test superior a 0,8 y menos de 80 coeficientes conservados.
- `print(f"Lasso: R² test = {r2_test_lasso:.3f} · coeficientes distintos de cero: {n_no_cero} de {lasso[-1].coef_.shape[0]}")`  
  Escribe el R² y el recuento (`lasso[-1].coef_.shape[0]` es el total de coeficientes: 665).
- `print("✔ Ejercicio 3 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Lasso gana por mucho** porque en estos datos **pocas variables lo explican casi todo** (tipo de habitación y temporada); descarta las otras ~640 columnas de ruido, mientras Ridge las conserva todas, aunque encogidas.
- Un modelo con 27 coeficientes es **mucho más simple y fácil de explicar** que uno con 665.
- Lasso hace **selección de variables automática**: ideal si sospechas que solo unas pocas importan.

### 👀 A7 · Ejemplo — Qué variables ha conservado Lasso

**Qué vamos a hacer y qué debe salir**

Lasso dejó 27 coeficientes distintos de cero; ahora vemos **cuáles son** y cuánto pesan. Es lo que da valor de negocio: no solo un modelo que predice bien, sino una **lista corta de lo que de verdad influye**. **Debe salir** una lista de 8 filas; las tres primeras son `cat__tipo_habitacion_suite` (≈ +16,16), `cat__tipo_habitacion_estandar` (≈ −14,03) y `num__temporada_alta` (≈ +7,18). Es decir, Lasso ha **encontrado la señal real** entre 665 columnas: el tipo de habitación y la temporada. Se apoya en `lasso` (A6).

```python
# ¿Qué variables ha conservado Lasso? (las de mayor peso)
nombres_poly = lasso[:-1].get_feature_names_out()
coef_lasso = pd.Series(lasso[-1].coef_, index=nombres_poly)
principales = coef_lasso[coef_lasso != 0].sort_values(key=np.abs, ascending=False).head(8)
principales.round(2)
```

**Línea a línea**

- `# ¿Qué variables ha conservado Lasso? (las de mayor peso)`  
  Comentario con la pregunta que responde la celda.
- `nombres_poly = lasso[:-1].get_feature_names_out()`  
  `lasso[:-1]` son **todos los pasos menos el último** (preprocesado, polinomios, escalado); `.get_feature_names_out()` da el nombre de cada una de las 665 columnas (las originales y sus combinaciones).
- `coef_lasso = pd.Series(lasso[-1].coef_, index=nombres_poly)`  
  Une los coeficientes de Lasso con sus nombres en una serie (`pd.Series(valores, index=nombres)`).
- `principales = coef_lasso[coef_lasso != 0].sort_values(key=np.abs, ascending=False).head(8)`  
  Se queda con los coeficientes **no nulos** (`coef_lasso != 0`), los ordena por tamaño sin importar el signo (`sort_values(key=np.abs, ascending=False)`) y muestra los 8 primeros (`.head(8)`).
- `principales.round(2)`  
  Redondea a 2 decimales y, al ser la última línea de la celda, **la muestra**.

**Lo destacable**

- Los coeficientes están sobre variables **escaladas**: miden euros por cada desviación típica de la variable, y por eso **se pueden comparar entre sí**.
- Un nombre con dos variables (`num__ninos cat__tipo_habitacion_suite`) es una **combinación** (producto) de ambas.
- Con solo 120 reservas, los pesos pequeños son **menos fiables**: el mensaje principal viene de las variables grandes.
- En una celda, la **última línea** (si es una expresión) se muestra sola, sin necesidad de `print`.

### 👀 A8 · Ejemplo — Tabla comparativa de los tres modelos

**Qué vamos a hacer y qué debe salir**

Cerramos la comparación con una tabla que pone **lado a lado** los tres modelos y sus dos notas: R² en entrenamiento y R² en test. **Debe salir**: sin regularizar `1.000 / 0.716`; Ridge `0.998 / 0.728`; Lasso `0.957 / 0.887`. Fíjate en la brecha: Lasso **baja un poco en train** (0,957) y **gana mucho en test** (0,887): no memoriza, generaliza. Ningún método gana siempre: **Ridge** es mejor cuando **muchas** variables aportan un poco; **Lasso**, cuando **pocas** lo explican casi todo (nuestro caso); **ElasticNet** mezcla ambos castigos y sirve con variables muy correlacionadas. Se apoya en `ols`, `ridge` y `lasso`.

```python
comparativa = pd.DataFrame({
    "R² train": [ols.score(X_train, y_train), ridge.score(X_train, y_train), lasso.score(X_train, y_train)],
    "R² test": [r2_test_ols, r2_test_ridge, r2_test_lasso],
}, index=["Sin regularizar", "Ridge", "Lasso"]).round(3)
comparativa
```

**Línea a línea**

- `comparativa = pd.DataFrame({`  
  Crea una tabla a partir de un diccionario: cada clave es una columna y cada lista, sus valores.
- `"R² train": [ols.score(X_train, y_train), ridge.score(X_train, y_train), lasso.score(X_train, y_train)],`  
  Columna con el R² en **entrenamiento** de los tres modelos (sin regularizar, Ridge, Lasso), en ese orden.
- `"R² test": [r2_test_ols, r2_test_ridge, r2_test_lasso],`  
  Columna con el R² en **test** de los tres (valores ya guardados en A3, A5 y A6).
- `}, index=["Sin regularizar", "Ridge", "Lasso"]).round(3)`  
  `index` pone nombre a las filas y `.round(3)` redondea a 3 decimales.
- `comparativa`  
  Última línea de la celda: muestra la tabla.

**Lo destacable**

- La mejor señal está en la **brecha** (train − test), no solo en el R² de test: Lasso la reduce de 0,28 a 0,07.
- Tres modelos, tres historias: **sin regularizar** memoriza, **Ridge** corrige poco, **Lasso** corrige mucho.
- Qué usar en la práctica: Ridge si hay muchas variables que aportan algo; Lasso si hay pocas importantes (y quieres explicarlas).

### 🎯 A9 · Mini-reto — Curva de R² según el número de reservas

**Qué vamos a hacer y qué debe salir**

Mini-reto: ¿cuántos datos hacen falta para que regularizar deje de ser necesario? Repetimos el experimento con **cuatro tamaños de entrenamiento** (60, 120, 300 y 1000 reservas) y comparamos el modelo sin regularizar con Lasso. Para que la comparación sea justa, **todos se evalúan con las mismas 1000 reservas** apartadas desde el principio. **Debe salir** `✔ Mini-reto correcto` y la tabla `curva`: con 60 reservas `ols 0.449 / lasso 0.691`; con 120, `0.704 / 0.848`; con 300, `−1.062 / 0.913`; con 1000, `0.836 / 0.925`. Dos hechos llamativos: con **300** reservas el modelo sin regularizar da un R² **negativo** (peor que predecir la media: está justo en la zona más inestable, con 300 filas y 665 columnas); y con **1000** reservas la ventaja de Lasso casi desaparece. Se apoya en `modelo_con` (A2).

```python
tamanos = [60, 120, 300, 1000]
X_res, X_eval, y_res, y_eval = train_test_split(X, y, test_size=1000, random_state=SEMILLA)
filas = {}
for n in tamanos:
    m_ols = modelo_con(LinearRegression()).fit(X_res.iloc[:n], y_res.iloc[:n])
    m_las = modelo_con(LassoCV(cv=5, max_iter=50000, random_state=SEMILLA)).fit(X_res.iloc[:n], y_res.iloc[:n])
    filas[n] = {"ols": m_ols.score(X_eval, y_eval), "lasso": m_las.score(X_eval, y_eval)}
curva = pd.DataFrame(filas).T.round(3)
curva
assert list(curva.index) == tamanos and list(curva.columns) == ["ols", "lasso"], "Índice = tamaños; columnas 'ols' y 'lasso'"
assert curva.loc[60, "lasso"] > curva.loc[60, "ols"], "Con pocos datos, Lasso debería superar al modelo sin regularizar"
display(curva)
print("✔ Mini-reto correcto")
```

**Línea a línea**

- `tamanos = [60, 120, 300, 1000]`  
  Los tamaños de entrenamiento a probar.
- `X_res, X_eval, y_res, y_eval = train_test_split(X, y, test_size=1000, random_state=SEMILLA)`  
  Aparta **1000 reservas fijas** para evaluar (`X_eval`, `y_eval`) y deja el resto (`X_res`, `y_res`) como cantera de la que sacar los datos de entrenamiento.
- `filas = {}`  
  Diccionario vacío donde se guardarán los resultados de cada tamaño.
- `for n in tamanos:`  
  Para cada tamaño `n`:
- `m_ols = modelo_con(LinearRegression()).fit(X_res.iloc[:n], y_res.iloc[:n])`  
  Ajusta la regresión **sin regularizar** con las **primeras `n` reservas** (`X_res.iloc[:n]` = las `n` primeras filas; `y_res.iloc[:n]`, su precio).
- `m_las = modelo_con(LassoCV(cv=5, max_iter=50000, random_state=SEMILLA)).fit(X_res.iloc[:n], y_res.iloc[:n])`  
  Ajusta **Lasso** con esas mismas `n` reservas.
- `filas[n] = {"ols": m_ols.score(X_eval, y_eval), "lasso": m_las.score(X_eval, y_eval)}`  
  Guarda el R² de los dos modelos medido siempre con las **mismas 1000 reservas de evaluación**.
- `curva = pd.DataFrame(filas).T.round(3)`  
  Convierte el diccionario en tabla: `.T` la **traspone** (un tamaño por fila, un modelo por columna) y `.round(3)` redondea.
- `curva`  
  Línea suelta: aquí no hace nada visible (la tabla se muestra con `display` más abajo); es un resto del enunciado.
- `assert list(curva.index) == tamanos and list(curva.columns) == ["ols", "lasso"], "Índice = tamaños; columnas 'ols' y 'lasso'"` … `assert curva.loc[60, "lasso"] > curva.loc[60, "ols"], "Con pocos datos, Lasso debería superar al modelo sin regularizar"` (2 líneas)  
  Dos comprobaciones: la tabla tiene los tamaños como filas y las columnas `ols` y `lasso`, y con 60 reservas Lasso supera al modelo sin regularizar.
- `display(curva)`  
  Muestra la tabla (con `display` se puede mostrar una tabla aunque no sea la última línea).
- `print("✔ Mini-reto correcto")`  
  Aviso de que el mini-reto está bien.

**Lo destacable**

- **Con pocos datos, regularizar importa mucho** (60 reservas: 0,691 frente a 0,449); **con muchos, importa poco** (1000: 0,925 frente a 0,836).
- El R² puede ser **negativo**: significa que el modelo es peor que predecir siempre la media. No es un error del cuaderno.
- Evaluar con **las mismas reservas** siempre es lo que hace comparables los cuatro tamaños.
- `.iloc[:n]` = «las primeras `n` filas»; `.T` = «traspuesta»: dos herramientas de pandas que verás mucho.
