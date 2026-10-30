# Código explicado · S05.02 · Álgebra lineal con NumPy: vectores, matrices y sistemas de ecuaciones

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_02_algebra_lineal.ipynb) · [descargar](../S05_02_algebra_lineal.ipynb) · ⏱ en clase: 40 min · 🏫 0 celdas de código en clase · 🏠 6 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| — | — | Este cuaderno no tiene celdas de explicación previas: se trabaja directamente en el cuaderno. |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `noches` | `np.array([10, 4, 2])` | 2 |
| `precios` | `np.array([70.0, 95.0, 160.0])` | 2 |
| `noches_semana` | `np.array([ [10, 4, 2], # lunes [ 8, 6, 1], # martes [12,…` | 4 |
| `A` | `np.array([[10, 4], [ 8, 6]], dtype=float)` | 6 |
| `b` | `np.array([1180.0, 1240.0])` | 6 |
| `x` | `np.linalg.solve(A, b)` | 6 |
| `inversa` | `np.linalg.inv(A)` | 8 |
| `tabla` | `np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=","…` | 10 |
| `X` | `np.column_stack([np.ones(len(temperatura)), temperatura])` | 10 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 2, 4, 6 |
| `column_stack` | Une varios vectores como columnas de una matriz. | 10 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 10 |
| `det` | Calcula el determinante de una matriz. | 8 |
| `genfromtxt` | Lee un fichero de texto con números y lo convierte en array de NumPy. | 10 |
| `inv` | Calcula la matriz inversa. | 8 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 10 |
| `norm` | Calcula la longitud (norma) de un vector. | 2 |
| `ones` | Crea un array lleno de unos. | 10 |
| `print` | Muestra un valor por pantalla. | 2, 4, 6, 8, 10 |
| `round` | Redondea un número a los decimales indicados. | 2, 8 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 4, 10 |
| `solve` | Resuelve un sistema de ecuaciones lineales. | 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏠

**Qué hace:** Importa las librerías que usa el cuaderno y fija `SEMILLA`.

```python
import numpy as np

SEMILLA = 42
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.

### Celda 2 · 1 · Vectores · 🏠

**Qué hace:** Practica `array`, `round`, `norm` (sección «1 · Vectores»).

```python
noches = np.array([10, 4, 2])                 # estándar, superior, suite
precios = np.array([70.0, 95.0, 160.0])       # EUR por noche de cada tipo
print("ingreso:", noches @ precios)           # 10x70 + 4x95 + 2x160
print("suma de vectores:", noches + np.array([1, 1, 1]), "· por un escalar:", noches * 2)
print("norma (longitud):", np.linalg.norm(noches).round(3))
```

**Qué hace cada línea:**

- `noches = np.array([10, 4, 2]) # estándar, superior, suite` → Guarda en `noches` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `precios = np.array([70.0, 95.0, 160.0]) # EUR por noche de cada tipo` → Guarda en `precios` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `print("ingreso:", noches @ precios) # 10x70 + 4x95 + 2x160` → `print`: muestra un valor por pantalla.
- `print("suma de vectores:", noches + np.array([1, 1, 1]), "· por un escalar:…` → `print`: muestra un valor por pantalla; `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `print("norma (longitud):", np.linalg.norm(noches).round(3))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `norm`: calcula la longitud (norma) de un vector.

### Celda 3 · 1 · Vectores · 🏠 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2 · Matrices y producto matricial · 🏠

**Qué hace:** Practica `array`, `shape` (sección «2 · Matrices y producto matricial»).

```python
noches_semana = np.array([
    [10, 4, 2],     # lunes
    [ 8, 6, 1],     # martes
    [12, 5, 3],     # miércoles
    [ 9, 7, 4],     # jueves
])
print("forma:", noches_semana.shape, "→ traspuesta:", noches_semana.T.shape)
print("ingresos por día:", noches_semana @ precios)
```

**Qué hace cada línea:**

- `noches_semana = np.array([` → Guarda en `noches_semana` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `print("forma:", noches_semana.shape, "→ traspuesta:", noches_semana.T.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).
- `print("ingresos por día:", noches_semana @ precios)` → `print`: muestra un valor por pantalla.

### Celda 5 · 2 · Matrices y producto matricial · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3 · Sistemas de ecuaciones · 🏠

**Qué hace:** Dos días de facturación con solo dos tipos de habitación:.

```python
# Dos días de facturación con solo dos tipos de habitación:
A = np.array([[10, 4],
              [ 8, 6]], dtype=float)
b = np.array([1180.0, 1240.0])
x = np.linalg.solve(A, b)
print("precios:", x, "· comprobación:", A @ x)
```

**Qué hace cada línea:**

- `A = np.array([[10, 4],` → Guarda en `A` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `b = np.array([1180.0, 1240.0])` → Guarda en `b` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `x = np.linalg.solve(A, b)` → Guarda en `x` el resultado. `solve`: resuelve un sistema de ecuaciones lineales.
- `print("precios:", x, "· comprobación:", A @ x)` → `print`: muestra un valor por pantalla.

### Celda 7 · 3 · Sistemas de ecuaciones · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4 · Inversa e identidad · 🏠

**Qué hace:** Practica `inv`, `round`, `det` (sección «4 · Inversa e identidad»).

```python
inversa = np.linalg.inv(A)
print(np.round(A @ inversa, 10))
print("determinante:", np.linalg.det(A).round(2))
```

**Qué hace cada línea:**

- `inversa = np.linalg.inv(A)` → Guarda en `inversa` el resultado. `inv`: calcula la matriz inversa.
- `print(np.round(A @ inversa, 10))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados.
- `print("determinante:", np.linalg.det(A).round(2))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `det`: calcula el determinante de una matriz.

### Celda 9 · 4 · Inversa e identidad · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5 · Álgebra lineal y regresión: la ecuación nor… · 🏠

**Qué hace:** Practica `genfromtxt`, `column_stack`, `dato`, `shape` y más (sección «5 · Álgebra lineal y regresión: la ecua…»).

```python
tabla = np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=",", skip_header=1, usecols=(1, 2, 3, 4))
ocupacion, temperatura = tabla[:, 0], tabla[:, 1]

X = np.column_stack([np.ones(len(temperatura)), temperatura])     # columna de unos + temperatura
print("forma de X:", X.shape)
```

**Qué hace cada línea:**

- `tabla = np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=",", skip_hea…` → Guarda en `tabla` el resultado. `genfromtxt`: lee un fichero de texto con números y lo convierte en array de NumPy; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `ocupacion, temperatura = tabla[:, 0], tabla[:, 1]` → Guarda el valor en `ocupacion, temperatura`.
- `X = np.column_stack([np.ones(len(temperatura)), temperatura]) # columna de…` → Guarda en `X` el resultado. `column_stack`: une varios vectores como columnas de una matriz; `ones`: crea un array lleno de unos; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `print("forma de X:", X.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).

### Celda 11 · 5 · Álgebra lineal y regresión: la ecuación nor… · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 12 · 6 · Mini-reto integrador: varias variables a la… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S05_02_algebra_lineal.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
