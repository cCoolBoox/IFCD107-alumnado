# Código explicado · S05.01 · NumPy: arrays, vectorización y broadcasting

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_01_numpy.ipynb) · [descargar](../notebooks/S05_01_numpy.ipynb) · ⏱ en clase: 30 min · 🏫 7 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | Contexto TurisData | Importa las librerías que usa el cuaderno y fija `SEMILLA`. |
| 2 | 1 · Arrays: la estructura básica | Columnas: 0 = ocupacion_pct, 1 = temperatura_c, 2 = festivo (0/1), 3 = precio_medio. |
| 3 | 1 · Arrays: la estructura básica | Ejemplo de la sección «1 · Arrays: la estructura básica». |
| 5 | 2 · Máscaras booleanas: filtrar sin buc… | Practica `sum`, `round`, `mean` (sección «2 · Máscaras booleanas: filtrar sin buc…»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `tabla` | `np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=","…` | 2 |
| `mascara_calor` | `temperatura > 25` | 5 |
| `grande` | `np.arange(1_000_000, dtype=float)` | 7 |
| `inicio` | `time.perf_counter()` | 7 |
| `suma_bucle` | `0.0` | 7 |
| `t_bucle` | `time.perf_counter() - inicio` | 7 |
| `suma_vector` | `(grande * 2).sum()` | 7 |
| `t_vector` | `time.perf_counter() - inicio` | 7 |
| `medias` | `tabla.mean(axis=0)` | 9 |
| `centrada` | `tabla - medias` | 9 |
| `rng` | `np.random.default_rng(SEMILLA)` | 11 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `arange` | Crea una secuencia de números con un paso fijo. | 7 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 11 |
| `genfromtxt` | Lee un fichero de texto con números y lo convierte en array de NumPy. | 2 |
| `mean` | Calcula la media. | 5, 9 |
| `normal` | Genera números aleatorios con forma de campana (normal). | 11 |
| `perf_counter` | Reloj de precisión para medir cuánto tarda un trozo de código. | 7 |
| `print` | Muestra un valor por pantalla. | 2, 3, 5, 7, 9, 11 |
| `round` | Redondea un número a los decimales indicados. | 5, 9, 11 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2, 9 |
| `sum` | Suma todos los valores. | 5, 7 |
| `tolist` | Convierte un array o una columna en una lista de Python. | 7 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏫

**Qué hace:** Importa las librerías que usa el cuaderno y fija `SEMILLA`.

```python
import time

import numpy as np
import matplotlib.pyplot as plt

SEMILLA = 42
```

**Qué hace cada línea:**

- `import time` → Trae `time` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.

### Celda 2 · 1 · Arrays: la estructura básica · 🏫

**Qué hace:** Columnas: 0 = ocupacion_pct, 1 = temperatura_c, 2 = festivo (0/1), 3 = precio_medio.

```python
tabla = np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=",", skip_header=1, usecols=(1, 2, 3, 4))
print("forma:", tabla.shape, "· tipo:", tabla.dtype, "· dimensiones:", tabla.ndim)
print(tabla[:3])                     # las tres primeras filas
# Columnas: 0 = ocupacion_pct, 1 = temperatura_c, 2 = festivo (0/1), 3 = precio_medio
```

**Qué hace cada línea:**

- `tabla = np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=",", skip_hea…` → Guarda en `tabla` el resultado. `genfromtxt`: lee un fichero de texto con números y lo convierte en array de NumPy; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `print("forma:", tabla.shape, "· tipo:", tabla.dtype, "· dimensiones:", tabl…` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- `print(tabla[:3]) # las tres primeras filas` → `print`: muestra un valor por pantalla.

### Celda 3 · 1 · Arrays: la estructura básica · 🏫

**Qué hace:** Ejemplo de la sección «1 · Arrays: la estructura básica».

```python
print(tabla[0, 1], tabla[:3, 0], tabla[10:13, :2])
```

**Qué hace cada línea:**

- `print(tabla[0, 1], tabla[:3, 0], tabla[10:13, :2])` → `print`: muestra un valor por pantalla.

### Celda 4 · 1 · Arrays: la estructura básica · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2 · Máscaras booleanas: filtrar sin bucles · 🏫

**Qué hace:** Practica `sum`, `round`, `mean` (sección «2 · Máscaras booleanas: filtrar sin buc…»).

```python
mascara_calor = temperatura > 25
print("Días de más de 25 °C:", mascara_calor.sum(), "· ocupación media esos días:", ocupacion[mascara_calor].mean().round(1))
```

**Qué hace cada línea:**

- `mascara_calor = temperatura > 25` → Guarda el valor en `mascara_calor`.
- `print("Días de más de 25 °C:", mascara_calor.sum(), "· ocupación media esos…` → `print`: muestra un valor por pantalla; `sum`: suma todos los valores; `round`: redondea un número a los decimales indicados.

### Celda 6 · 2 · Máscaras booleanas: filtrar sin bucles · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 3 · Vectorización: operar con todo a la vez · 🏫

**Qué hace:** Practica `arange`, `perf_counter`, `tolist`, `sum` (sección «3 · Vectorización: operar con todo a la…»).

```python
grande = np.arange(1_000_000, dtype=float)

inicio = time.perf_counter()
suma_bucle = 0.0
for valor in grande.tolist():
    suma_bucle += valor * 2
t_bucle = time.perf_counter() - inicio

inicio = time.perf_counter()
suma_vector = (grande * 2).sum()
t_vector = time.perf_counter() - inicio

print(f"Bucle: {t_bucle*1000:.1f} ms · vectorizado: {t_vector*1000:.2f} ms · el resultado es el mismo: {suma_bucle == suma_vector}")
```

**Qué hace cada línea:**

- `grande = np.arange(1_000_000, dtype=float)` → Guarda en `grande` el resultado. `arange`: crea una secuencia de números con un paso fijo.
- `inicio = time.perf_counter()` → Guarda en `inicio` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `suma_bucle = 0.0` → Guarda el valor en `suma_bucle`.
- `for valor in grande.tolist():` → Repite el bloque de debajo para cada valor de `valor` en `grande.tolist()`.
- `t_bucle = time.perf_counter() - inicio` → Guarda en `t_bucle` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `inicio = time.perf_counter()` → Guarda en `inicio` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `suma_vector = (grande * 2).sum()` → Guarda en `suma_vector` el resultado. `sum`: suma todos los valores.
- `t_vector = time.perf_counter() - inicio` → Guarda en `t_vector` el resultado. `perf_counter`: reloj de precisión para medir cuánto tarda un trozo de código.
- `print(f"Bucle: {t_bucle*1000:.1f} ms · vectorizado: {t_vector*1000:.2f} ms…` → `print`: muestra un valor por pantalla.

### Celda 8 · 3 · Vectorización: operar con todo a la vez · 🏫 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4 · Broadcasting: arrays de distinta forma · 🏫

**Qué hace:** Practica `mean`, `round`, `shape` (sección «4 · Broadcasting: arrays de distinta fo…»).

```python
medias = tabla.mean(axis=0)          # axis=0: una media por columna -> forma (4,)
print(medias.round(2), medias.shape)
centrada = tabla - medias            # (1096, 4) - (4,) -> se resta a cada fila
print(centrada.mean(axis=0).round(6))
```

**Qué hace cada línea:**

- `medias = tabla.mean(axis=0) # axis=0: una media por columna -> forma (4,)` → Guarda en `medias` el resultado. `mean`: calcula la media.
- `print(medias.round(2), medias.shape)` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `shape`: tamaño de la tabla: (filas, columnas).
- `centrada = tabla - medias # (1096, 4) - (4,) -> se resta a cada fila` → Guarda el valor en `centrada`.
- `print(centrada.mean(axis=0).round(6))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.

### Celda 10 · 4 · Broadcasting: arrays de distinta forma · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 5 · Números aleatorios reproducibles · 🏫

**Qué hace:** Practica `default_rng`, `round`, `normal` (sección «5 · Números aleatorios reproducibles»).

```python
rng = np.random.default_rng(SEMILLA)
print(rng.normal(68, 10, 3).round(2))
rng = np.random.default_rng(SEMILLA)          # misma semilla, mismos números
print(rng.normal(68, 10, 3).round(2))
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `print(rng.normal(68, 10, 3).round(2))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `normal`: genera números aleatorios con forma de campana (normal).
- `rng = np.random.default_rng(SEMILLA) # misma semilla, mismos números` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `print(rng.normal(68, 10, 3).round(2))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `normal`: genera números aleatorios con forma de campana (normal).

### Celda 12 · 5 · Números aleatorios reproducibles · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 6 · Mini-reto integrador: media móvil de 7 días · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S05_01_numpy.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
