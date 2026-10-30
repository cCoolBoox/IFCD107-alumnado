# Código explicado · S05.03 · Descenso del gradiente y regresión lineal desde cero

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_03_gradiente_regresion.ipynb) · [descargar](../notebooks/S05_03_gradiente_regresion.ipynb) · ⏱ en clase: 40 min · 🏫 7 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | Contexto TurisData | Importa las librerías que usa el cuaderno y fija `SEMILLA`. |
| 2 | 1 · La derivada: la pendiente en un pun… | Practica `def`, `for` (sección «1 · La derivada: la pendiente en un pun…»). |
| 4 | 2 · Función de coste: el error cuadráti… | Practica `genfromtxt`, `dato` (sección «2 · Función de coste: el error cuadráti…»). |
| 6 | 3 · Descenso del gradiente en una dimen… | Practica `array`, `append`, `derivada` (sección «3 · Descenso del gradiente en una dimen…… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `h` | `1e-6` | 2 |
| `tabla` | `np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=","…` | 4 |
| `derivada_f` | `lambda x: 2 * (x - 3)` | 6 |
| `temperatura_z` | `(temperatura - media_t) / desv_t` | 8 |
| `X` | `np.column_stack([np.ones(len(temperatura_z)), temperatura…` | 8 |
| `y` | `ocupacion` | 8 |
| `t_lin` | `np.linspace(temperatura.min(), temperatura.max(), 50)` | 11 |
| `pendiente_scratch` | `w_z[1] / desv_t` | 14 |
| `intercepto_scratch` | `w_z[0] - w_z[1] * media_t / desv_t` | 14 |
| `modelo` | `LinearRegression().fit(temperatura.reshape(-1, 1), ocupac…` | 14 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `f` | Función definida en el cuaderno. |
| `derivada_numerica` | Aproxima la derivada de func en x (diferencia centrada). *(La escribís vosotros en un ejercicio.)* |
| `mse` | Error cuadrático medio. *(La escribís vosotros en un ejercicio.)* |
| `descender` | Función definida en el cuaderno. |
| `gradiente_mse` | Gradiente del MSE de la regresión lineal y_pred = X @ w. *(La escribís vosotros en un ejercicio.)* |
| `entrenar` | Descenso del gradiente para la regresión lineal. Devuelve (w, historial_de_mse). *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `append` | Añade un elemento al final de una lista. | 6 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 6 |
| `column_stack` | Une varios vectores como columnas de una matriz. | 8 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 4 |
| `derivada` | La función cuya derivada se calcula (se pasa como argumento). | 6 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 12 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 14 |
| `genfromtxt` | Lee un fichero de texto con números y lo convierte en array de NumPy. | 4 |
| `legend` | Muestra la leyenda del gráfico. | 11, 12 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 4, 8 |
| `LinearRegression` | Modelo de regresión lineal: ajusta una recta (o un plano) a los datos. | 14 |
| `linspace` | Crea una secuencia de N números equiespaciados entre dos límites. | 11 |
| `max` | Devuelve el valor más grande. | 11 |
| `mean` | Calcula la media. | 8 |
| `min` | Devuelve el valor más pequeño. | 11 |
| `ones` | Crea un array lleno de unos. | 8 |
| `plot` | Dibuja una línea (o puntos unidos). | 11, 12 |
| `print` | Muestra un valor por pantalla. | 2, 4, 6, 8, 14 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 6 |
| `reshape` | Cambia la forma de un array (filas × columnas) sin cambiar los datos. | 14 |
| `scatter` | Dibuja un gráfico de puntos. | 11 |
| `set_title` | Pone el título de un gráfico. | 11 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 11 |
| `set_ylabel` | Pone el nombre del eje vertical. | 11 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 8 |
| `show` | Muestra el gráfico. | 11, 12 |
| `std` | Calcula la desviación típica (cuánto se separan los datos de la media). | 8 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 11 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 11, 12 |
| `title` | Pone el título del gráfico. | 12 |
| `xlabel` | Pone el nombre del eje horizontal. | 12 |
| `ylabel` | Pone el nombre del eje vertical. | 12 |
| `yscale` | Cambia la escala del eje vertical (por ejemplo, logarítmica). | 12 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏫

**Qué hace:** Importa las librerías que usa el cuaderno y fija `SEMILLA`.

```python
import numpy as np
import matplotlib.pyplot as plt

SEMILLA = 42
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.

### Celda 2 · 1 · La derivada: la pendiente en un punto · 🏫

**Qué hace:** Practica `def`, `for` (sección «1 · La derivada: la pendiente en un pun…»).

```python
def f(x):
    return (x - 3) ** 2 + 2       # una parábola con el mínimo en x = 3

h = 1e-6
for x in (0, 3, 5):
    pendiente = (f(x + h) - f(x - h)) / (2 * h)
    print(f"x = {x}: pendiente ≈ {pendiente:.3f}")   # negativa a la izquierda del mínimo, 0 en él, positiva a la derecha
```

**Qué hace cada línea:**

- `def f(x):` → Define la función `f`: Función definida en el cuaderno.
- `h = 1e-6` → Guarda el valor en `h`.
- `for x in (0, 3, 5):` → Repite el bloque de debajo para cada valor de `x` en `(0, 3, 5)`. Dentro del bloque: `f`: función definida en el cuaderno.

### Celda 3 · 1 · La derivada: la pendiente en un punto · 🏠 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2 · Función de coste: el error cuadrático medio… · 🏫

**Qué hace:** Practica `genfromtxt`, `dato` (sección «2 · Función de coste: el error cuadráti…»).

```python
tabla = np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=",", skip_header=1, usecols=(1, 2, 3, 4))
ocupacion, temperatura, festivo, precio = tabla[:, 0], tabla[:, 1], tabla[:, 2], tabla[:, 3]
print(len(ocupacion), "días")
```

**Qué hace cada línea:**

- `tabla = np.genfromtxt(dato("ocupacion_diaria.csv"), delimiter=",", skip_hea…` → Guarda en `tabla` el resultado. `genfromtxt`: lee un fichero de texto con números y lo convierte en array de NumPy; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `ocupacion, temperatura, festivo, precio = tabla[:, 0], tabla[:, 1], tabla[:…` → Guarda el valor en `ocupacion, temperatura,…`.
- `print(len(ocupacion), "días")` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.

### Celda 5 · 2 · Función de coste: el error cuadrático medio… · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3 · Descenso del gradiente en una dimensión · 🏫

**Qué hace:** Practica `array`, `append`, `derivada` (sección «3 · Descenso del gradiente en una dimen…»).

```python
def descender(derivada, x0, tasa, pasos):
    x = x0
    camino = [x]
    for _ in range(pasos):
        x = x - tasa * derivada(x)
        camino.append(x)
    return np.array(camino)

derivada_f = lambda x: 2 * (x - 3)          # derivada exacta de (x - 3)^2 + 2

for tasa in (0.01, 0.1, 1.05):
    camino = descender(derivada_f, x0=-4.0, tasa=tasa, pasos=30)
    print(f"tasa {tasa:>5}: x final = {camino[-1]:.3f}")
```

**Qué hace cada línea:**

- `def descender(derivada, x0, tasa, pasos):` → Define la función `descender`: Función definida en el cuaderno.
- `derivada_f = lambda x: 2 * (x - 3) # derivada exacta de (x - 3)^2 + 2` → Guarda el valor en `derivada_f`.
- `for tasa in (0.01, 0.1, 1.05):` → Repite el bloque de debajo para cada valor de `tasa` en `(0.01, 0.1, 1.05)`. Dentro del bloque: `descender`: función definida en el cuaderno.

### Celda 7 · 3 · Descenso del gradiente en una dimensión · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4 · Regresión lineal: el modelo y su gradiente · 🏫

**Qué hace:** Practica `column_stack`, `mean`, `std`, `shape` y más (sección «4 · Regresión lineal: el modelo y su gr…»).

```python
media_t, desv_t = temperatura.mean(), temperatura.std()
temperatura_z = (temperatura - media_t) / desv_t
X = np.column_stack([np.ones(len(temperatura_z)), temperatura_z])
y = ocupacion
print(X.shape)
```

**Qué hace cada línea:**

- `media_t, desv_t = temperatura.mean(), temperatura.std()` → Guarda en `media_t, desv_t` el resultado. `mean`: calcula la media; `std`: calcula la desviación típica (cuánto se separan los datos de la media).
- `temperatura_z = (temperatura - media_t) / desv_t` → Guarda el valor en `temperatura_z`.
- `X = np.column_stack([np.ones(len(temperatura_z)), temperatura_z])` → Guarda en `X` el resultado. `column_stack`: une varios vectores como columnas de una matriz; `ones`: crea un array lleno de unos; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `y = ocupacion` → Guarda el valor en `y`.
- `print(X.shape)` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).

### Celda 9 · 4 · Regresión lineal: el modelo y su gradiente · 🏫 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 4 · Regresión lineal: el modelo y su gradiente · 🏫 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 4 · Regresión lineal: el modelo y su gradiente · 🏫

**Qué hace:** Curva de aprendizaje y recta ajustada.

```python
# Curva de aprendizaje y recta ajustada
fig, ejes = plt.subplots(1, 2, figsize=(11, 3.8))
ejes[0].plot(historial)
ejes[0].set_xlabel("Época")
ejes[0].set_ylabel("MSE")
ejes[0].set_title("El error baja en cada paso")

ejes[1].scatter(temperatura, ocupacion, s=6, alpha=0.4, label="Días")
t_lin = np.linspace(temperatura.min(), temperatura.max(), 50)
ejes[1].plot(t_lin, w_z[0] + w_z[1] * (t_lin - media_t) / desv_t, color="crimson", label="Recta ajustada")
ejes[1].set_xlabel("Temperatura (°C)")
ejes[1].set_ylabel("Ocupación (%)")
ejes[1].set_title("Regresión desde cero: ocupación frente a temperatura")
ejes[1].legend()
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `fig, ejes = plt.subplots(1, 2, figsize=(11, 3.8))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ejes[0].plot(historial)` → `plot`: dibuja una línea (o puntos unidos).
- `ejes[0].set_xlabel("Época")` → `set_xlabel`: pone el nombre del eje horizontal.
- `ejes[0].set_ylabel("MSE")` → `set_ylabel`: pone el nombre del eje vertical.
- `ejes[0].set_title("El error baja en cada paso")` → `set_title`: pone el título de un gráfico.
- `ejes[1].scatter(temperatura, ocupacion, s=6, alpha=0.4, label="Días")` → `scatter`: dibuja un gráfico de puntos.
- `t_lin = np.linspace(temperatura.min(), temperatura.max(), 50)` → Guarda en `t_lin` el resultado. `linspace`: crea una secuencia de N números equiespaciados entre dos límites; `min`: devuelve el valor más pequeño; `max`: devuelve el valor más grande.
- `ejes[1].plot(t_lin, w_z[0] + w_z[1] * (t_lin - media_t) / desv_t, color="cr…` → `plot`: dibuja una línea (o puntos unidos).
- `ejes[1].set_xlabel("Temperatura (°C)")` → `set_xlabel`: pone el nombre del eje horizontal.
- … y 5 más con las mismas ideas.

### Celda 12 · 5 · La tasa de aprendizaje · 🏫

**Qué hace:** Practica `figure`, `yscale`, `xlabel`, `ylabel` y más (sección «5 · La tasa de aprendizaje»).

```python
plt.figure(figsize=(6.5, 3.8))
for tasa in (0.005, 0.1, 0.9):
    _, hist = entrenar(X, y, tasa=tasa, epocas=60)
    plt.plot(hist, label=f"tasa = {tasa}")
plt.yscale("log")
plt.xlabel("Época")
plt.ylabel("MSE (escala logarítmica)")
plt.title("Efecto de la tasa de aprendizaje")
plt.legend()
plt.tight_layout()
plt.show()
```

**Qué hace cada línea:**

- `plt.figure(figsize=(6.5, 3.8))` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `for tasa in (0.005, 0.1, 0.9):` → Repite el bloque de debajo para cada valor de `tasa` en `(0.005, 0.1, 0.9)`. Dentro del bloque: `entrenar`: descenso del gradiente para la regresión lineal. Devuelve (w, historial_de_mse). *(La escribís vosotros en un ejercicio.)*; `plot`: dibuja una línea (o puntos unidos).
- `plt.yscale("log")` → `yscale`: cambia la escala del eje vertical (por ejemplo, logarítmica).
- `plt.xlabel("Época")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.ylabel("MSE (escala logarítmica)")` → `ylabel`: pone el nombre del eje vertical.
- `plt.title("Efecto de la tasa de aprendizaje")` → `title`: pone el título del gráfico.
- `plt.legend()` → `legend`: muestra la leyenda del gráfico.
- `plt.tight_layout()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.show()` → `show`: muestra el gráfico.

### Celda 13 · 5 · La tasa de aprendizaje · 🏠 · ejercicio 6

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 14 · 6 · De vuelta a las unidades originales y compa… · 🏠

**Qué hace:** Practica `fit`, `reshape`, `LinearRegression` (sección «6 · De vuelta a las unidades originales…»).

```python
from sklearn.linear_model import LinearRegression

pendiente_scratch = w_z[1] / desv_t
intercepto_scratch = w_z[0] - w_z[1] * media_t / desv_t

modelo = LinearRegression().fit(temperatura.reshape(-1, 1), ocupacion)
print(f"Desde cero:   ocupación = {intercepto_scratch:.4f} + ({pendiente_scratch:.4f}) x temperatura")
print(f"scikit-learn: ocupación = {modelo.intercept_:.4f} + ({modelo.coef_[0]:.4f}) x temperatura")
```

**Qué hace cada línea:**

- `from sklearn.linear_model import LinearRegression` → Trae `LinearRegression` de `sklearn.linear_model` para poder usarlo.
- `pendiente_scratch = w_z[1] / desv_t` → Guarda el valor en `pendiente_scratch`.
- `intercepto_scratch = w_z[0] - w_z[1] * media_t / desv_t` → Guarda el valor en `intercepto_scratch`.
- `modelo = LinearRegression().fit(temperatura.reshape(-1, 1), ocupacion)` → Guarda en `modelo` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `reshape`: cambia la forma de un array (filas × columnas) sin cambiar los datos; `LinearRegression`: modelo de regresión lineal: ajusta una recta (o un plano) a los datos.
- `print(f"Desde cero: ocupación = {intercepto_scratch:.4f} + ({pendiente_scra…` → `print`: muestra un valor por pantalla.
- `print(f"scikit-learn: ocupación = {modelo.intercept_:.4f} + ({modelo.coef_[…` → `print`: muestra un valor por pantalla.

### Celda 15 · 6 · De vuelta a las unidades originales y compa… · 🏠 · ejercicio 7

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 16 · 7 · Mini-reto integrador: regresión múltiple de… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S05_03_gradiente_regresion.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
