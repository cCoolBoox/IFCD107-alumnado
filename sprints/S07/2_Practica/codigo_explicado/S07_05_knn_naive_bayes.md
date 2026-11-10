# Código explicado · S07.05 · k vecinos (k-NN) y Naive Bayes

> **Para qué sirve.** Aquí está **todo el código del cuaderno explicado por escrito**, celda a celda y en el mismo orden. Cada bloque sigue siempre el mismo guion: **primero** un párrafo que dice qué vamos a hacer, por qué y qué debe salir; **después** el código, con **cada línea explicada**; y **al final** lo destacable del bloque (lo que conviene recordar y con qué se relaciona).
>
> **Cuaderno (solo para casa):** [🏠 abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_05_knn_naive_bayes.ipynb)
>
> **Cómo usarlo:** ejecuta la celda en el cuaderno; busca aquí la del mismo número (A3, A5…); lee el párrafo, sigue el código línea a línea y, al terminar, cambia algo (un número, una columna) y comprueba si pasa lo que esperabas: es la mejor manera de entender código.

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda** («coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`»). Lo que va tras `#` es un comentario: Python lo ignora. Los ejercicios (✏️) llevan aquí la **solución de referencia**: úsala **después** de intentarlo.

## La idea del cuaderno

Después de la regresión logística, conocemos otras dos familias de clasificadores muy distintas: **k-NN** («dime con quién andas…»: clasifica una reserva mirando a las **k reservas más parecidas**) y **Naive Bayes** (usa probabilidades y supone, «ingenuamente», que las variables son independientes entre sí). Los comparamos con el mismo problema —predecir cancelaciones— y la misma métrica, el **AUC**.

- **Hilo del cuaderno:** vemos por qué k-NN **exige escalar** las variables (A2, A3) → buscamos el mejor número de vecinos `k` (A4) → probamos Naive Bayes con variables numéricas (A5) y con variables **categóricas** (A6) → comparamos los cuatro modelos en AUC y en tiempo (A7).
- **Lo que te llevas:** en k-NN la **distancia** manda, y sin escalar una sola variable decide casi todo; `k` pequeño **sobreajusta** y `k` grande suaviza; Naive Bayes es muy rápido aunque su supuesto sea ingenuo; y **ningún modelo gana siempre**: se elige según precisión, velocidad y explicabilidad.

## Mapa de celdas

| Celda | Tipo | Qué hacemos | ¿Dónde? |
|---|---|---|---|
| A1 | ⚙️ Preparación | Preparar las herramientas y los datos | 🏠 |
| A2 | 👀 Ejemplo | ¿Qué variable manda en la distancia? | 🏠 |
| A3 | ✏️ Ejercicio | Poner cifras al efecto de escalar | 🏠 |
| A4 | ✏️ Ejercicio | Elegir el número de vecinos k | 🏠 |
| A5 | ✏️ Ejercicio | Naive Bayes con variables numéricas (GaussianNB) | 🏠 |
| A6 | ✏️ Ejercicio | Naive Bayes con variables categóricas (CategoricalNB) | 🏠 |
| A7 | 🎯 Mini-reto | Comparativa final: AUC, tiempo y recomendación | 🏠 |

🏫 = en clase · 🏠 = en casa. 👀 ejemplo: solo se ejecuta y se mira. ✏️ ejercicio: se completa con tu código. ⚙️ preparación: se ejecuta sola.

## Celda a celda

### ⚙️ A1 · Preparación — Preparar las herramientas y los datos

**Qué vamos a hacer y qué debe salir**

Celda de preparación: se ejecuta **la primera**. Trae las librerías (incluidos los clasificadores k-NN y Naive Bayes), carga las reservas, define las columnas de entrada (`X`) y la salida (`y`), prepara una **validación cruzada de 5 trozos** (`cv`) que se reutilizará en todo el cuaderno y define la función `prep_onehot()`, que fabrica el preprocesado estándar. **Debe salir** `Listo ✔`. Se apoya en todo lo anterior del curso: es el mismo preprocesado que en S07.03 y S07.04.

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

import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, CategoricalNB
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, KBinsDiscretizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
SEMILLA = 42
sns.set_theme(style="whitegrid")

df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)
columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
X, y = df[columnas_num + columnas_cat], df["cancelada"]
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)


def prep_onehot():
    """Imputar + escalar (numéricas) e imputar + one-hot denso (categóricas)."""
    return ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), columnas_num),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), columnas_cat),
    ])
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
- `import time`  
  Trae `time`: sirve para **medir cuánto tarda** cada modelo (se usa en A7).
- `import warnings`  
  Trae `warnings`, para silenciar avisos.
- `import numpy as np`  
  Trae **NumPy** (`np`).
- `import pandas as pd`  
  Trae **pandas** (`pd`).
- `import matplotlib.pyplot as plt`  
  Trae **matplotlib** (`plt`).
- `import seaborn as sns`  
  Trae **seaborn** (`sns`).
- `from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split`  
  Trae `StratifiedKFold` (trozos que respetan la proporción de cada clase), `cross_val_score` (nota por validación cruzada) y `train_test_split`.
- `from sklearn.neighbors import KNeighborsClassifier`  
  Trae `KNeighborsClassifier`: el clasificador de los **k vecinos más cercanos**.
- `from sklearn.naive_bayes import GaussianNB, CategoricalNB`  
  Trae los dos Naive Bayes: `GaussianNB` (variables numéricas, supone que siguen una campana) y `CategoricalNB` (variables que son categorías).
- `from sklearn.linear_model import LogisticRegression`  
  Trae `LogisticRegression`, que se usará como **referencia**.
- `from sklearn.impute import SimpleImputer`  
  Trae `SimpleImputer`: rellena huecos.
- `from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, KBinsDiscretizer`  
  Trae `StandardScaler` (escala), `OneHotEncoder` (texto → columnas 0/1), `OrdinalEncoder` (texto → números 0, 1, 2…) y `KBinsDiscretizer` (convierte un número en **tramos**).
- `from sklearn.compose import ColumnTransformer`  
  Trae `ColumnTransformer`.
- `from sklearn.pipeline import Pipeline`  
  Trae `Pipeline`.
- `warnings.filterwarnings("ignore", category=UserWarning)`  
  Oculta los avisos de tipo `UserWarning`.
- `warnings.filterwarnings("ignore", category=FutureWarning)`  
  Oculta los avisos de tipo `FutureWarning` (avisos de cambios futuros de las librerías).
- `SEMILLA = 42`  
  Número fijo (`42`) para que los sorteos salgan siempre igual.
- `sns.set_theme(style="whitegrid")`  
  Estilo visual de los gráficos.
- `df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])`  
  Lee las 6000 reservas en `df`; `parse_dates` marca las dos columnas de fecha.
- `df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)`  
  Crea `temporada_alta` (1 si el mes de llegada es 1, 2, 3, 7, 8 o 12; 0 si no).
- `columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",` … `"peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]` (2 líneas)  
  Las 9 columnas numéricas.
- `columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]`  
  Las 6 columnas de texto.
- `X, y = df[columnas_num + columnas_cat], df["cancelada"]`  
  `X` = variables para predecir; `y` = `cancelada`.
- `cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)`  
  Define la validación cruzada: 5 trozos que mantienen la proporción de cancelaciones; `shuffle=True` mezcla antes y `random_state` fija el resultado. Se **reutiliza** para que todos los modelos se comparen con **los mismos trozos**.
- `def prep_onehot():`  
  Define una función que fabrica el preprocesado «estándar».
- `"""Imputar + escalar (numéricas) e imputar + one-hot denso (categóricas)."""`  
  Descripción de la función.
- `return ColumnTransformer([` … `])` (5 líneas)  
  Devuelve un preprocesado en dos ramas: **números** (huecos con la mediana + escalado) y **texto** (huecos con el más frecuente + columnas 0/1; `sparse_output=False` entrega una tabla normal, no «dispersa»). Cada llamada fabrica **uno nuevo**.
- `print("Listo ✔")`  
  Mensaje de que todo ha ido bien.

**Lo destacable**

- La celda de preparación **se ejecuta siempre la primera**, y otra vez si Colab se reinicia: todas las demás celdas usan lo que crea aquí (`df`, `SEMILLA`, las librerías…). Si ves `NameError: name '…' is not defined`, casi siempre es que falta ejecutarla.
- **Un único `cv` para todos** los modelos: así la comparación es justa (mismos trozos, mismos datos).
- `prep_onehot()` es una **función** (no una variable) para obtener un preprocesado **nuevo** cada vez, igual que `clone(prep)` en S07.04.
- Aquí **no se hace** `train_test_split` al principio: la validación cruzada usa todos los datos y rota el papel de «test».

### 👀 A2 · Ejemplo — ¿Qué variable manda en la distancia?

**Qué vamos a hacer y qué debe salir**

k-NN clasifica una reserva mirando a las reservas **más parecidas**, y «parecido» se mide con una **distancia** (como medir con una regla en un mapa de varias dimensiones). El problema: si las variables tienen **escalas muy distintas** (antelación de 0 a 400 días, adultos de 1 a 4…), la distancia la decide la de números grandes. Aquí lo comprobamos: tomamos **3000 pares de reservas** al azar, calculamos cuánto aporta cada variable a la distancia entre ellas y lo hacemos con los datos **sin escalar** y **escalados**. **Debe salir** una tabla de 9 filas: sin escalar, `antelacion_dias` aporta el **76,6 %** de la distancia y `precio_noche` el 23,2 %: las otras siete, ≈ 0 %. Escaladas, **todas aportan alrededor del 11 %** (≈ 1/9). Es la razón por la que k-NN **exige escalar**.

```python
# ¿Qué variable manda en la distancia? Comparamos qué % de la distancia² entre pares aporta cada una
rng = np.random.default_rng(SEMILLA)
numericas = df[columnas_num].copy()
def reparto_distancia(tabla, n_pares=3000):
    i = rng.integers(0, len(tabla), n_pares)
    j = rng.integers(0, len(tabla), n_pares)
    cuadrados = (tabla.iloc[i].to_numpy() - tabla.iloc[j].to_numpy()) ** 2
    return pd.Series(cuadrados.mean(axis=0) / cuadrados.mean(axis=0).sum(), index=tabla.columns)

sin_escalar = reparto_distancia(numericas)
escalado = reparto_distancia(pd.DataFrame(StandardScaler().fit_transform(numericas), columns=columnas_num))
pd.DataFrame({"sin escalar": sin_escalar, "escaladas": escalado}).mul(100).round(1)
```

**Línea a línea**

- `# ¿Qué variable manda en la distancia? Comparamos qué % de la distancia² entre pares aporta cada una`  
  Comentario con la pregunta que responde la celda.
- `rng = np.random.default_rng(SEMILLA)`  
  Crea un generador de números aleatorios con semilla (para que el sorteo de pares se repita igual).
- `numericas = df[columnas_num].copy()`  
  Copia de las columnas numéricas de `df`.
- `def reparto_distancia(tabla, n_pares=3000):`  
  Define una función que calcula cuánto aporta cada variable a la distancia (con 3000 pares por defecto).
- `i = rng.integers(0, len(tabla), n_pares)`  
  Saca 3000 números enteros al azar entre 0 y el número de filas: los **primeros** elementos de cada par.
- `j = rng.integers(0, len(tabla), n_pares)`  
  Otros 3000: los **segundos** elementos de cada par.
- `cuadrados = (tabla.iloc[i].to_numpy() - tabla.iloc[j].to_numpy()) ** 2`  
  Para cada par, la **diferencia al cuadrado** entre las dos reservas, variable a variable (`iloc[i]` coge las filas elegidas, `to_numpy()` las pasa a matriz y `** 2` eleva al cuadrado). La distancia entre dos reservas es la raíz de la suma de esos cuadrados.
- `return pd.Series(cuadrados.mean(axis=0) / cuadrados.mean(axis=0).sum(), index=tabla.columns)`  
  Para cada variable, su **media** de cuadrados dividida entre la **suma** de todas las medias: el **porcentaje** de la distancia que explica esa variable (suman 1).
- `sin_escalar = reparto_distancia(numericas)`  
  Aplica la función a los datos **tal cual**.
- `escalado = reparto_distancia(pd.DataFrame(StandardScaler().fit_transform(numericas), columns=columnas_num))`  
  Aplica la función a los datos **escalados** (`StandardScaler().fit_transform(...)`: media 0, desviación 1), reconstruidos como tabla con sus nombres.
- `pd.DataFrame({"sin escalar": sin_escalar, "escaladas": escalado}).mul(100).round(1)`  
  Última línea: junta los dos repartos en una tabla, los pasa a porcentaje (`.mul(100)`) y los redondea a 1 decimal. Al ser la última línea, **se muestra**.

**Lo destacable**

- **Sin escalar, una variable decide casi todo:** `antelacion_dias` aporta el 77 % de la distancia; los adultos, ni el 0,1 %. k-NN **ignoraría** casi todas las variables.
- **Escaladas, reparto equilibrado:** cada una aporta ≈ 11 % (1/9).
- La distancia es una suma de **diferencias al cuadrado**: por eso las escalas grandes dominan.
- Esto afecta a todos los métodos que usan **distancias** (k-NN, clustering); no a la regresión logística ni a los árboles.

### ✏️ A3 · Ejercicio — Poner cifras al efecto de escalar

**Qué vamos a hacer y qué debe salir**

Extraemos de la tabla anterior las dos cifras que cuentan la historia (el porcentaje que aporta la antelación sin escalar y escalada) y las ponemos en una frase. **Debe salir** `Sin escalar, la antelación decide el 77 % de la distancia; escalada, el 11 %.` y `✔ Ejercicio 1 correcto`. Se apoya en `sin_escalar` y `escalado` de A2.

```python
pct_antelacion_sin_escalar = sin_escalar["antelacion_dias"] * 100
pct_antelacion_escalada = escalado["antelacion_dias"] * 100
assert pct_antelacion_sin_escalar > 60, "Sin escalar, la antelación debería dominar la distancia (más del 60 %)"
assert pct_antelacion_escalada < 25, "Escaladas, cada variable debería aportar una parte parecida"
print(f"Sin escalar, la antelación decide el {pct_antelacion_sin_escalar:.0f} % de la distancia; escalada, el {pct_antelacion_escalada:.0f} %.")
print("✔ Ejercicio 1 correcto")
```

**Línea a línea**

- `pct_antelacion_sin_escalar = sin_escalar["antelacion_dias"] * 100`  
  Lo que aporta la antelación a la distancia **sin escalar**, en porcentaje (valor × 100).
- `pct_antelacion_escalada = escalado["antelacion_dias"] * 100`  
  Lo que aporta **escalada**.
- `assert pct_antelacion_sin_escalar > 60, "Sin escalar, la antelación debería dominar la distancia (más del 60 %)"`  
  Comprobación: sin escalar, la antelación domina (más del 60 %).
- `assert pct_antelacion_escalada < 25, "Escaladas, cada variable debería aportar una parte parecida"`  
  Comprobación: escalada, aporta una parte pequeña y parecida a las demás (menos del 25 %).
- `print(f"Sin escalar, la antelación decide el {pct_antelacion_sin_escalar:.0f} % de la distancia; escalada, el {pct_antelacion_escalada:.0f} %.")`  
  Escribe las dos cifras sin decimales.
- `print("✔ Ejercicio 1 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Una frase con dos cifras** resume lo aprendido: 77 % frente a 11 %.
- `serie["nombre"]` busca un valor por su etiqueta, como en S07.03.

### ✏️ A4 · Ejercicio — Elegir el número de vecinos k

**Qué vamos a hacer y qué debe salir**

¿Cuántos vecinos hay que mirar? Con **k = 1**, el modelo copia lo que hizo **la reserva más parecida**: se aprende hasta el ruido (sobreajuste). Con **k grande**, promedia a muchos vecinos y suaviza, pero si se pasa pierde detalle. Probamos 8 valores de `k` (de 1 a 401) y para cada uno medimos el **AUC medio con validación cruzada**; el mejor será el de AUC más alto. **Debe salir** un gráfico donde el AUC **sube** al aumentar `k` y luego se aplana, y esta lista: `k = 1 → 0.585`, `5 → 0.645`, `15 → 0.690`, `31 → 0.707`, `61 → 0.722`, `101 → 0.732`, `201 → 0.740`, `401 → 0.740`, `Mejor k = 201` y `✔ Ejercicio 2 correcto`. Con estos datos —con mucho ruido— hacen falta **muchos vecinos** para promediar. Se apoya en `prep_onehot` y `cv` (A1).

```python
ks = [1, 5, 15, 31, 61, 101, 201, 401]
auc_por_k = []
for k in ks:
    modelo_k = Pipeline([("prep", prep_onehot()), ("knn", KNeighborsClassifier(n_neighbors=k))])
    auc_por_k.append(cross_val_score(modelo_k, X, y, cv=cv, scoring="roc_auc").mean())
mejor_k = ks[int(np.argmax(auc_por_k))]
assert len(auc_por_k) == len(ks), "Una media por cada k"
assert mejor_k >= 31, "Con estos datos ruidosos, los k grandes funcionan mejor (≥ 31)"
assert auc_por_k[0] < max(auc_por_k) - 0.05, "k = 1 debería ser claramente peor (sobreajuste)"

plt.figure(figsize=(7, 3.8))
plt.plot(ks, auc_por_k, marker="o", color="#2a6f97")
plt.xscale("log")
plt.axvline(mejor_k, color="#e63946", ls="--", label=f"Mejor k = {mejor_k}")
plt.title("k-NN: AUC según el número de vecinos")
plt.xlabel("k (escala logarítmica)")
plt.ylabel("AUC medio en validación cruzada")
plt.legend()
plt.show()
for k, a in zip(ks, auc_por_k):
    print(f"k = {k:>3} → AUC {a:.3f}")
print(f"Mejor k = {mejor_k}")
print("✔ Ejercicio 2 correcto")
```

**Línea a línea**

- `ks = [1, 5, 15, 31, 61, 101, 201, 401]`  
  Los valores de `k` a probar: de 1 a 401, espaciados de forma creciente.
- `auc_por_k = []`  
  Lista vacía donde se guardará el AUC de cada `k`.
- `for k in ks:`  
  Para cada `k`:
- `modelo_k = Pipeline([("prep", prep_onehot()), ("knn", KNeighborsClassifier(n_neighbors=k))])`  
  Monta un modelo nuevo: preprocesado + `KNeighborsClassifier(n_neighbors=k)` (clasifica según los `k` vecinos más cercanos).
- `auc_por_k.append(cross_val_score(modelo_k, X, y, cv=cv, scoring="roc_auc").mean())`  
  Evalúa el modelo con validación cruzada (`cross_val_score` con `scoring="roc_auc"` da un AUC por cada trozo), saca la **media** (`.mean()`) y la guarda en la lista.
- `mejor_k = ks[int(np.argmax(auc_por_k))]`  
  `np.argmax(auc_por_k)` da la **posición** del AUC más alto y `ks[...]` el valor de `k` de esa posición.
- `assert len(auc_por_k) == len(ks), "Una media por cada k"`  
  Comprobación: hay un AUC por cada `k`.
- `assert mejor_k >= 31, "Con estos datos ruidosos, los k grandes funcionan mejor (≥ 31)"`  
  Comprobación: con estos datos ruidosos, el mejor `k` es grande (≥ 31).
- `assert auc_por_k[0] < max(auc_por_k) - 0.05, "k = 1 debería ser claramente peor (sobreajuste)"`  
  Comprobación: `k = 1` es claramente peor que el mejor (más de 0,05 de AUC): sobreajuste.
- `plt.figure(figsize=(7, 3.8))`  
  Crea la figura.
- `plt.plot(ks, auc_por_k, marker="o", color="#2a6f97")`  
  Dibuja el AUC (vertical) según `k` (horizontal), con un punto por valor.
- `plt.xscale("log")`  
  Eje horizontal en escala **logarítmica**: `k` va de 1 a 401 y así se ven bien todos los valores.
- `plt.axvline(mejor_k, color="#e63946", ls="--", label=f"Mejor k = {mejor_k}")`  
  Línea vertical roja discontinua en el mejor `k`.
- `plt.title("k-NN: AUC según el número de vecinos")`  
  Título.
- `plt.xlabel("k (escala logarítmica)")`  
  Eje horizontal.
- `plt.ylabel("AUC medio en validación cruzada")`  
  Eje vertical.
- `plt.legend()`  
  Muestra la leyenda.
- `plt.show()`  
  Muestra la figura.
- `for k, a in zip(ks, auc_por_k):`  
  Recorre a la vez cada `k` y su AUC (`zip` junta las dos listas):
- `print(f"k = {k:>3} → AUC {a:.3f}")`  
  Escribe `k` (alineado a la derecha con 3 caracteres: `:>3`) y su AUC con 3 decimales.
- `print(f"Mejor k = {mejor_k}")`  
  Escribe el mejor `k`.
- `print("✔ Ejercicio 2 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **`k` es un compromiso:** pequeño = sobreajuste (0,585 con k = 1); grande = suaviza y generaliza (0,740 con k = 201).
- Con **k = 1 el AUC es peor que con k = 401**: copiar al vecino más parecido es copiar el ruido.
- A partir de k = 201 el AUC **se aplana** (0,740 y 0,740): subir más no aporta.
- `k` se elige con **validación cruzada**, no con el test: igual que `alpha` en S07.02 o el umbral en S07.03.
- `zip(a, b)` recorre dos listas a la vez.

### ✏️ A5 · Ejercicio — Naive Bayes con variables numéricas (GaussianNB)

**Qué vamos a hacer y qué debe salir**

**Naive Bayes** calcula la probabilidad de cada clase a partir de lo que se observa en cada variable, y las **combina como si fueran independientes** entre sí (de ahí lo de «ingenuo»). Es muy rápido y funciona sorprendentemente bien. `GaussianNB` supone que cada variable numérica sigue una **campana** (distribución normal) dentro de cada clase. Lo evaluamos con el mismo `cv` y el mismo AUC. **Debe salir** `AUC GaussianNB: 0.719` y `✔ Ejercicio 3 correcto`. Un 0,719 es **algo peor** que el de la regresión logística (0,757), pero a cambio es mucho más sencillo. Se apoya en `prep_onehot` y `cv` (A1).

```python
nb_gauss = Pipeline([("prep", prep_onehot()), ("nb", GaussianNB())])
auc_nb_gauss = cross_val_score(nb_gauss, X, y, cv=cv, scoring="roc_auc").mean()
assert 0.65 < auc_nb_gauss < 0.85, "El AUC de GaussianNB debería estar entre 0,65 y 0,85"
print(f"AUC GaussianNB: {auc_nb_gauss:.3f}")
print("✔ Ejercicio 3 correcto")
```

**Línea a línea**

- `nb_gauss = Pipeline([("prep", prep_onehot()), ("nb", GaussianNB())])`  
  Monta el modelo: preprocesado (escala y columnas 0/1) + `GaussianNB`.
- `auc_nb_gauss = cross_val_score(nb_gauss, X, y, cv=cv, scoring="roc_auc").mean()`  
  AUC medio con validación cruzada (`cross_val_score` con `scoring="roc_auc"`, y `.mean()`).
- `assert 0.65 < auc_nb_gauss < 0.85, "El AUC de GaussianNB debería estar entre 0,65 y 0,85"`  
  Comprobación: el AUC está entre 0,65 y 0,85.
- `print(f"AUC GaussianNB: {auc_nb_gauss:.3f}")`  
  Escribe el AUC con 3 decimales.
- `print("✔ Ejercicio 3 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **El supuesto «ingenuo» es falso** (las variables de una reserva no son independientes entre sí), **pero el modelo sigue funcionando** razonablemente.
- Las columnas 0/1 **no son campanas**: `GaussianNB` las trata como si lo fueran, lo cual no encaja bien y limita el resultado (por eso el siguiente ejercicio).
- `cross_val_score(modelo, X, y, cv=cv, scoring=...)` es la forma más corta de evaluar un modelo con validación cruzada.

### ✏️ A6 · Ejercicio — Naive Bayes con variables categóricas (CategoricalNB)

**Qué vamos a hacer y qué debe salir**

Probamos el **otro** Naive Bayes, diseñado para **categorías**. Para usarlo, hay que convertir **todo** en categorías: las variables numéricas se parten en **5 tramos con el mismo número de reservas** (`KBinsDiscretizer`, por ejemplo antelación «muy corta», «corta»…) y las de texto se codifican como números 0, 1, 2… (`OrdinalEncoder`; aquí **son etiquetas**, no cantidades). **Debe salir** `AUC GaussianNB: 0.719 · CategoricalNB: 0.742` y `✔ Ejercicio 4 correcto`. Mejora (0,719 → 0,742): ya no se obliga a las variables a ser campanas. Aun así, la regresión logística sigue por delante (0,757). Se apoya en A1 y A5.

```python
prep_cat = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("bins", KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="quantile"))]), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("ord", OrdinalEncoder())]), columnas_cat),
])
nb_cat = Pipeline([("prep", prep_cat), ("nb", CategoricalNB(min_categories=5))])
auc_nb_cat = cross_val_score(nb_cat, X, y, cv=cv, scoring="roc_auc").mean()
assert 0.65 < auc_nb_cat < 0.85, "El AUC de CategoricalNB debería estar entre 0,65 y 0,85"
print(f"AUC GaussianNB: {auc_nb_gauss:.3f} · CategoricalNB: {auc_nb_cat:.3f}")
print("✔ Ejercicio 4 correcto")
```

**Línea a línea**

- `prep_cat = ColumnTransformer([` … `])` (6 líneas)  
  Define el preprocesado: **numéricas**: huecos con la mediana y `KBinsDiscretizer` (5 tramos con el mismo número de reservas: `strategy="quantile"`; `encode="ordinal"` los numera 0 a 4). **Texto**: huecos con el más frecuente y `OrdinalEncoder` (cada categoría → un número).
- `nb_cat = Pipeline([("prep", prep_cat), ("nb", CategoricalNB(min_categories=5))])`  
  Monta el modelo: ese preprocesado + `CategoricalNB`; `min_categories=5` le dice que cada variable tiene **al menos 5 categorías posibles** (evita errores si en algún trozo falta alguna).
- `auc_nb_cat = cross_val_score(nb_cat, X, y, cv=cv, scoring="roc_auc").mean()`  
  AUC medio con validación cruzada.
- `assert 0.65 < auc_nb_cat < 0.85, "El AUC de CategoricalNB debería estar entre 0,65 y 0,85"`  
  Comprobación: el AUC está entre 0,65 y 0,85.
- `print(f"AUC GaussianNB: {auc_nb_gauss:.3f} · CategoricalNB: {auc_nb_cat:.3f}")`  
  Escribe los dos AUC (`GaussianNB` de A5 y `CategoricalNB`) para compararlos.
- `print("✔ Ejercicio 4 correcto")`  
  Aviso de que el ejercicio está bien.

**Lo destacable**

- **Discretizar** (convertir números en tramos) permite usar `CategoricalNB`, y aquí **mejora** el resultado: 0,719 → 0,742.
- `OrdinalEncoder` no significa que una categoría sea «mayor» que otra: Naive Bayes categórico las trata como **etiquetas**.
- Elegir bien **cómo se preparan los datos** puede importar tanto como elegir el modelo.

### 🎯 A7 · Mini-reto — Comparativa final: AUC, tiempo y recomendación

**Qué vamos a hacer y qué debe salir**

Mini-reto: poner los cuatro modelos en una **tabla** y recomendar uno. No solo importa el AUC: también cuánto **tarda en entrenarse** y, sobre todo, **en predecir** (si hubiera que predecir en tiempo real), y lo **explicable** que sea. Para ello medimos con `time.perf_counter()`. **Debe salir** la tabla `logística 0.757 / 0.027 / 0.005`, `knn 0.740 / 0.018 / 0.106`, `nb_gauss 0.719 / 0.027 / 0.008`, `nb_cat 0.742 / 0.023 / 0.006` (AUC, segundos de ajuste, segundos de predicción; los tiempos varían un poco en cada ordenador), la frase de recomendación y `✔ Mini-reto correcto`. Lo llamativo: **k-NN tarda ≈ 20 veces más en predecir** que los demás: no aprende nada al entrenar, sino que guarda los datos y tiene que **buscar vecinos en cada predicción**. Se apoya en todo lo anterior.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
candidatos = {
    "logistica": Pipeline([("prep", prep_onehot()), ("clf", LogisticRegression(max_iter=1000))]),
    "knn": Pipeline([("prep", prep_onehot()), ("clf", KNeighborsClassifier(n_neighbors=mejor_k))]),
    "nb_gauss": nb_gauss,
    "nb_cat": nb_cat,
}
filas = {}
for nombre, m in candidatos.items():
    auc = cross_val_score(m, X, y, cv=cv, scoring="roc_auc").mean()
    t0 = time.perf_counter()
    m.fit(X_train, y_train)
    t1 = time.perf_counter()
    m.predict_proba(X_test)
    t2 = time.perf_counter()
    filas[nombre] = {"auc_cv": auc, "segundos_ajuste": t1 - t0, "segundos_predecir": t2 - t1}
tabla = pd.DataFrame(filas).T.round(3)
recomendacion = ("La regresión logística obtiene el mejor AUC y es la más explicable (odds ratio); k-NN guarda todos los "
                 "datos y es más lento al predecir, y Naive Bayes es rapidísimo pero algo peor. Elegiría la logística.")
tabla
assert list(tabla.index) == ["logistica", "knn", "nb_gauss", "nb_cat"], "Filas en el orden pedido"
assert {"auc_cv", "segundos_ajuste", "segundos_predecir"} <= set(tabla.columns)
assert tabla["auc_cv"].between(0.6, 0.9).all(), "AUC entre 0,6 y 0,9 en todos"
assert isinstance(recomendacion, str) and len(recomendacion) > 40, "Escribe una recomendación razonada"
display(tabla)
print(recomendacion)
print("✔ Mini-reto correcto")
```

**Línea a línea**

- `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)`  
  Reparte los datos (80 % / 20 %, estratificado) para poder **medir tiempos** de entrenar y predecir.
- `candidatos = {` … `}` (6 líneas)  
  Diccionario con los cuatro modelos: la **logística** (referencia), **k-NN** con el mejor `k` de A4, y los dos Naive Bayes ya montados (`nb_gauss`, `nb_cat`).
- `filas = {}`  
  Diccionario vacío para los resultados.
- `for nombre, m in candidatos.items():`  
  Para cada modelo:
- `auc = cross_val_score(m, X, y, cv=cv, scoring="roc_auc").mean()`  
  AUC medio con validación cruzada (el mismo `cv` para todos).
- `t0 = time.perf_counter()`  
  Anota la hora de **inicio** (`perf_counter` es un cronómetro de alta precisión).
- `m.fit(X_train, y_train)`  
  Entrena el modelo con train.
- `t1 = time.perf_counter()`  
  Anota la hora al **terminar de entrenar**.
- `m.predict_proba(X_test)`  
  Predice las probabilidades de test (aquí solo interesa el **tiempo**, no se guarda el resultado).
- `t2 = time.perf_counter()`  
  Anota la hora al **terminar de predecir**.
- `filas[nombre] = {"auc_cv": auc, "segundos_ajuste": t1 - t0, "segundos_predecir": t2 - t1}`  
  Guarda el AUC y los dos tiempos: de ajuste (`t1 - t0`) y de predicción (`t2 - t1`).
- `tabla = pd.DataFrame(filas).T.round(3)`  
  Convierte el diccionario en tabla: `.T` traspone (un modelo por fila) y `.round(3)` redondea.
- `recomendacion = ("La regresión logística obtiene el mejor AUC y es la más explicable (odds ratio); k-NN guarda todos los "` … `"datos y es más lento al predecir, y Naive Bayes es rapidísimo pero algo peor. Elegiría la logística.")` (2 líneas)  
  La recomendación escrita en texto: dos frases entre paréntesis que Python une en una sola cadena.
- `tabla`  
  Línea suelta: no muestra nada (no es la última línea); la tabla se enseña con `display` más abajo.
- `assert list(tabla.index) == ["logistica", "knn", "nb_gauss", "nb_cat"], "Filas en el orden pedido"`  
  Comprobación: las filas están en el orden pedido.
- `assert {"auc_cv", "segundos_ajuste", "segundos_predecir"} <= set(tabla.columns)`  
  Comprobación: están las tres columnas.
- `assert tabla["auc_cv"].between(0.6, 0.9).all(), "AUC entre 0,6 y 0,9 en todos"`  
  Comprobación: todos los AUC están entre 0,6 y 0,9.
- `assert isinstance(recomendacion, str) and len(recomendacion) > 40, "Escribe una recomendación razonada"`  
  Comprobación: la recomendación es un texto de más de 40 caracteres.
- `display(tabla)`  
  Muestra la tabla.
- `print(recomendacion)`  
  Escribe la recomendación.
- `print("✔ Mini-reto correcto")`  
  Aviso de que el mini-reto está bien.

**Lo destacable**

- **La logística gana en AUC (0,757) y además es la más explicable** (odds ratio): por eso se recomienda. Elegir modelo no es solo elegir el AUC más alto.
- **k-NN es lento al predecir** (≈ 0,1 s frente a ≈ 0,006 s) porque no «aprende» nada: guarda todos los datos y busca vecinos cada vez. Con millones de filas, eso es un problema.
- **Naive Bayes es rapidísimo** pero algo peor; es una buena **primera aproximación** cuando hay pocos datos o se necesita velocidad.
- Los **tiempos varían** entre ordenadores y ejecuciones; lo que se mantiene es la **proporción** (k-NN, mucho más lento al predecir).
- `time.perf_counter()` antes y después de una operación mide cuánto tarda.
