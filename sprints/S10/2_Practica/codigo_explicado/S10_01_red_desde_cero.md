# Código explicado · S10.01 · S10 · Práctica 1 — Una red neuronal desde cero, solo con NumPy

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_01_red_desde_cero.ipynb) · [descargar](../S10_01_red_desde_cero.ipynb) · ⏱ en clase: 40 min · 🏫 5 celdas de código en clase · 🏠 5 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`. |
| 2 | 1. La neurona: una suma ponderada y un… | Practica `array`, `dot`, `round`, `exp` y más (sección «1. La neurona: una suma ponderada… |
| 4 | 2. Funciones de activación | Practica `linspace`, `plot`, `ylim`, `axhline` y más (sección «2. Funciones de activación… |
| 6 | 3. Un problema que un modelo lineal no… | Practica `make_circles`, `train_test_split`, `fit`, `scatter` y más (sección «3. Un probl… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `x` | `np.array([1.5, 1.0])` | 2 |
| `pesos` | `np.array([0.8, 1.2])` | 2 |
| `sesgo` | `-1.0` | 2 |
| `z` | `np.dot(x, pesos) + sesgo` | 2 |
| `lineal` | `LogisticRegression().fit(X_ent, y_ent)` | 6 |
| `red_test` | `RedNeuronal(2, 4)` | 10 |
| `g` | `red_test.atras(X_ent, y_ent)` | 10 |
| `w` | `red_test.p["W1"][idx]` | 10 |
| `numerico` | `(perdida_con_peso(red_test, "W1", idx, w + h) - perdida_c…` | 10 |
| `resultados` | `{}` | 11 |
| `rejilla` | `np.c_[xx.ravel(), yy.ravel()]` | 12 |
| `mejor` | `resultados[8]` | 13 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `sigmoide` | Convierte cualquier número en un valor entre 0 y 1 (sirve como probabilidad). |
| `neurona` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `tanh` | Función definida en el cuaderno. |
| `relu` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `relu_derivada` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `entropia_cruzada` | Pérdida media de una clasificación binaria (menor = mejor). |
| `paso_gradiente` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `RedNeuronal` | Red de una capa oculta (ReLU) y salida sigmoide para clasificación binaria. |
| `__init__` | Función definida en el cuaderno. |
| `adelante` | Función definida en el cuaderno. |
| `atras` | Función definida en el cuaderno. |
| `entrenar` | Función definida en el cuaderno. |
| `predecir` | Función definida en el cuaderno. |
| `perdida_con_peso` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `abs` | Valor absoluto: quita el signo negativo. | 10 |
| `append` | Añade un elemento al final de una lista. | 9 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 2, 7 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 9 |
| `axhline` | Dibuja una línea horizontal de referencia. | 4 |
| `axvline` | Dibuja una línea vertical de referencia. | 4 |
| `clip` | Limita los valores a un mínimo y un máximo. | 7 |
| `contourf` | Rellena con colores las zonas de una función en 2D. | 12 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 9 |
| `dot` | Producto escalar o producto de matrices. | 2 |
| `exp` | Exponencial (e elevado a un número). | 2 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 6 |
| `float` | Convierte un valor en número decimal. | 2, 10 |
| `full` | Crea un array lleno del valor indicado. | 7 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 12 |
| `legend` | Muestra la leyenda del gráfico. | 4, 13 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 9 |
| `linspace` | Crea una secuencia de N números equiespaciados entre dos límites. | 4, 12 |
| `log` | Logaritmo natural. | 7 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 6 |
| `make_circles` | Genera datos sintéticos en forma de dos círculos concéntricos. | 6 |
| `maximum` | Máximo elemento a elemento entre dos arrays. | 4 |
| `mean` | Calcula la media. | 7, 9, 11 |
| `meshgrid` | Crea una cuadrícula de coordenadas para dibujar o evaluar funciones en 2D. | 12 |
| `normal` | Genera números aleatorios con forma de campana (normal). | 9 |
| `plot` | Dibuja una línea (o puntos unidos). | 4, 13 |
| `print` | Muestra un valor por pantalla. | 2, 6, 7, 10, 11 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 9 |
| `ravel` | Aplana un array a una sola dimensión. | 9, 12 |
| `reshape` | Cambia la forma de un array (filas × columnas) sin cambiar los datos. | 9, 12 |
| `round` | Redondea un número a los decimales indicados. | 2, 6, 7, 10 |
| `scatter` | Dibuja un gráfico de puntos. | 6, 12 |
| `score` | Calcula la nota del modelo con la métrica por defecto. | 6 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `set_title` | Pone el título de un gráfico. | 12 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 12 |
| `set_ylabel` | Pone el nombre del eje vertical. | 12 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 12 |
| `show` | Muestra el gráfico. | 4, 6, 12, 13 |
| `sqrt` | Raíz cuadrada. | 9 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 12 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 12 |
| `title` | Pone el título del gráfico. | 4, 6, 13 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 6 |
| `xlabel` | Pone el nombre del eje horizontal. | 4, 6, 13 |
| `ylabel` | Pone el nombre del eje vertical. | 4, 6, 13 |
| `ylim` | Fija el rango del eje vertical. | 4 |
| `zeros` | Crea un array lleno de ceros. | 9 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 12, 13 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `seed`.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

SEMILLA = 42
np.random.seed(SEMILLA)
plt.rcParams["figure.figsize"] = (6, 4)
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `from sklearn.datasets import make_circles` → Trae `make_circles` de `sklearn.datasets` para poder usarlo.
- `from sklearn.linear_model import LogisticRegression` → Trae `LogisticRegression` de `sklearn.linear_model` para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `np.random.seed(SEMILLA)` → `seed`: fija la semilla del azar para que salga siempre lo mismo.
- `plt.rcParams["figure.figsize"] = (6, 4)` → Guarda el valor en `plt.rcParams["figure.fi…`.

### Celda 2 · 1. La neurona: una suma ponderada y un "interru… · 🏫

**Qué hace:** Practica `array`, `dot`, `round`, `exp` y más (sección «1. La neurona: una suma ponderada y un…»).

```python
def sigmoide(z):
    """Convierte cualquier número en un valor entre 0 y 1 (sirve como probabilidad)."""
    return 1 / (1 + np.exp(-z))

x = np.array([1.5, 1.0])        # antelación 150 días, tarifa flexible
pesos = np.array([0.8, 1.2])    # inventados: la tarifa flexible pesa más
sesgo = -1.0

z = np.dot(x, pesos) + sesgo    # suma ponderada
print("z =", z, "→ salida de la neurona =", round(float(sigmoide(z)), 3))
```

**Qué hace cada línea:**

- `def sigmoide(z):` → Define la función `sigmoide`: Convierte cualquier número en un valor entre 0 y 1 (sirve como probabilidad).
- `x = np.array([1.5, 1.0]) # antelación 150 días, tarifa flexible` → Guarda en `x` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `pesos = np.array([0.8, 1.2]) # inventados: la tarifa flexible pesa más` → Guarda en `pesos` el resultado. `array`: crea una matriz o vector de NumPy (números que se pueden operar todos a la vez).
- `sesgo = -1.0` → Guarda el valor en `sesgo`.
- `z = np.dot(x, pesos) + sesgo # suma ponderada` → Guarda en `z` el resultado. `dot`: producto escalar o producto de matrices.
- `print("z =", z, "→ salida de la neurona =", round(float(sigmoide(z)), 3))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `float`: convierte un valor en número decimal.

### Celda 3 · 1. La neurona: una suma ponderada y un "interru… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2. Funciones de activación · 🏫

**Qué hace:** Practica `linspace`, `plot`, `ylim`, `axhline` y más (sección «2. Funciones de activación»).

```python
def tanh(z):
    return np.tanh(z)

z = np.linspace(-6, 6, 200)
plt.plot(z, sigmoide(z), label="sigmoide")
plt.plot(z, tanh(z), label="tanh")
plt.plot(z, np.maximum(0, z), label="ReLU")
plt.ylim(-1.5, 3); plt.axhline(0, color="gray", lw=0.5); plt.axvline(0, color="gray", lw=0.5)
plt.xlabel("valor de entrada z"); plt.ylabel("salida de la activación")
plt.title("Tres funciones de activación"); plt.legend(); plt.show()
```

**Qué hace cada línea:**

- `def tanh(z):` → Define la función `tanh`: Función definida en el cuaderno.
- `z = np.linspace(-6, 6, 200)` → Guarda en `z` el resultado. `linspace`: crea una secuencia de N números equiespaciados entre dos límites.
- `plt.plot(z, sigmoide(z), label="sigmoide")` → `plot`: dibuja una línea (o puntos unidos); `sigmoide`: convierte cualquier número en un valor entre 0 y 1 (sirve como probabilidad).
- `plt.plot(z, tanh(z), label="tanh")` → `plot`: dibuja una línea (o puntos unidos); `tanh`: función definida en el cuaderno.
- `plt.plot(z, np.maximum(0, z), label="ReLU")` → `plot`: dibuja una línea (o puntos unidos); `maximum`: máximo elemento a elemento entre dos arrays.
- `plt.ylim(-1.5, 3); plt.axhline(0, color="gray", lw=0.5); plt.axvline(0, col…` → `ylim`: fija el rango del eje vertical.
- `plt.ylim(-1.5, 3); plt.axhline(0, color="gray", lw=0.5); plt.axvline(0, col…` → `axhline`: dibuja una línea horizontal de referencia.
- `plt.ylim(-1.5, 3); plt.axhline(0, color="gray", lw=0.5); plt.axvline(0, col…` → `axvline`: dibuja una línea vertical de referencia.
- `plt.xlabel("valor de entrada z"); plt.ylabel("salida de la activación")` → `xlabel`: pone el nombre del eje horizontal.
- … y 4 más con las mismas ideas.

### Celda 5 · 2. Funciones de activación · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3. Un problema que un modelo lineal no resuelve · 🏫

**Qué hace:** Practica `make_circles`, `train_test_split`, `fit`, `scatter` y más (sección «3. Un problema que un modelo lineal no…»).

```python
X, y = make_circles(n_samples=600, noise=0.10, factor=0.45, random_state=SEMILLA)
X_ent, X_val, y_ent, y_val = train_test_split(X, y, test_size=0.3, random_state=SEMILLA, stratify=y)

lineal = LogisticRegression().fit(X_ent, y_ent)
print("Precisión de un modelo lineal en validación:", round(lineal.score(X_val, y_val), 3))

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", s=12)
plt.title("Dos grupos que ninguna recta separa"); plt.xlabel("variable 1"); plt.ylabel("variable 2"); plt.show()
```

**Qué hace cada línea:**

- `X, y = make_circles(n_samples=600, noise=0.10, factor=0.45, random_state=SE…` → Guarda en `X, y` el resultado. `make_circles`: genera datos sintéticos en forma de dos círculos concéntricos.
- `X_ent, X_val, y_ent, y_val = train_test_split(X, y, test_size=0.3, random_s…` → Guarda en `X_ent, X_val, y_ent, y_…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `lineal = LogisticRegression().fit(X_ent, y_ent)` → Guarda en `lineal` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- `print("Precisión de un modelo lineal en validación:", round(lineal.score(X_…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `score`: calcula la nota del modelo con la métrica por defecto.
- `plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", s=12)` → `scatter`: dibuja un gráfico de puntos.
- `plt.title("Dos grupos que ninguna recta separa"); plt.xlabel("variable 1");…` → `title`: pone el título del gráfico.
- `plt.title("Dos grupos que ninguna recta separa"); plt.xlabel("variable 1");…` → `xlabel`: pone el nombre del eje horizontal.
- `plt.title("Dos grupos que ninguna recta separa"); plt.xlabel("variable 1");…` → `ylabel`: pone el nombre del eje vertical.
- `plt.title("Dos grupos que ninguna recta separa"); plt.xlabel("variable 1");…` → `show`: muestra el gráfico.

### Celda 7 · 4. Propagación hacia delante: de las entradas a… · 🏫

**Qué hace:** Practica `clip`, `round`, `mean`, `array` y más (sección «4. Propagación hacia delante: de las en…»).

```python
def entropia_cruzada(y_real, prob, eps=1e-9):
    """Pérdida media de una clasificación binaria (menor = mejor)."""
    prob = np.clip(prob, eps, 1 - eps)
    return -np.mean(y_real * np.log(prob) + (1 - y_real) * np.log(1 - prob))

print("Si predices siempre 0.5, la pérdida es", round(entropia_cruzada(np.array([0, 1, 1, 0]), np.full(4, 0.5)), 3), "(= ln 2)")
print("Si aciertas con seguridad (0.99 / 0.01):", round(entropia_cruzada(np.array([1, 0]), np.array([0.99, 0.01])), 3))
print("Si fallas con seguridad (0.01 / 0.99):", round(entropia_cruzada(np.array([1, 0]), np.array([0.01, 0.99])), 3))
```

**Qué hace cada línea:**

- `def entropia_cruzada(y_real, prob, eps=1e-9):` → Define la función `entropia_cruzada`: Pérdida media de una clasificación binaria (menor = mejor).
- `print("Si predices siempre 0.5, la pérdida es", round(entropia_cruzada(np.a…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `entropia_cruzada`: pérdida media de una clasificación binaria (menor = mejor).
- `print("Si aciertas con seguridad (0.99 / 0.01):", round(entropia_cruzada(np…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `entropia_cruzada`: pérdida media de una clasificación binaria (menor = mejor).
- `print("Si fallas con seguridad (0.01 / 0.99):", round(entropia_cruzada(np.a…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `entropia_cruzada`: pérdida media de una clasificación binaria (menor = mejor).

### Celda 8 · 4. Propagación hacia delante: de las entradas a… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5. La red completa · 🏠

**Qué hace:** Practica `default_rng`, `sigmoide`, `ravel`, `mean` y más (sección «5. La red completa»).

```python
class RedNeuronal:
    """Red de una capa oculta (ReLU) y salida sigmoide para clasificación binaria."""

    def __init__(self, n_entradas, n_ocultas, semilla=SEMILLA):
        rng = np.random.default_rng(semilla)
        self.p = {
            "W1": rng.normal(0, np.sqrt(2 / n_entradas), (n_entradas, n_ocultas)),
            "b1": np.zeros(n_ocultas),
            "W2": rng.normal(0, np.sqrt(1 / n_ocultas), (n_ocultas, 1)),
            "b2": np.zeros(1),
        }
        self.historial = []

    def adelante(self, X):
        p = self.p
        self.Z1 = X @ p["W1"] + p["b1"]
        self.A1 = relu(self.Z1)
        self.Z2 = self.A1 @ p["W2"] + p["b2"]
        self.A2 = sigmoide(self.Z2)
        return self.A2.ravel()

    def atras(self, X, y):
        m = len(X)
        dZ2 = self.A2 - y.reshape(-1, 1)                 # error de la salida
        g = {"W2": self.A1.T @ dZ2 / m, "b2": dZ2.mean(axis=0)}
        dA1 = dZ2 @ self.p["W2"].T                        # el error viaja hacia atrás...
        dZ1 = dA1 * relu_derivada(self.Z1)                # ...atravesando la ReLU
        g["W1"] = X.T @ dZ1 / m
        g["b1"] = dZ1.mean(axis=0)
        return g

    def entrenar(self, X, y, epocas=1500, tasa=0.3, X_val=None, y_val=None):
        for e in range(epocas):
            prob = self.adelante(X)
            g = self.atras(X, y)
            self.p = paso_gradiente(self.p, g, tasa)
            if e % 50 == 0 or e == epocas - 1:
                perdida_val = entropia_cruzada(y_val, self.adelante(X_val)) if X_val is not None else np.nan
                self.historial.append((e, entropia_cruzada(y, prob), perdida_val))
        return self

    def predecir(self, X):
        return (self.adelante(X) >= 0.5).astype(int)
```

**Qué hace cada línea:**

- `class RedNeuronal:` → Define la clase `RedNeuronal`: Red de una capa oculta (ReLU) y salida sigmoide para clasificación binaria.

### Celda 10 · 5. La red completa · 🏠

**Qué hace:** Practica `round`, `abs` (sección «5. La red completa»).

```python
red_test = RedNeuronal(2, 4)
red_test.adelante(X_ent); g = red_test.atras(X_ent, y_ent)

def perdida_con_peso(red, clave, idx, valor):
    original = red.p[clave][idx]
    red.p[clave][idx] = valor
    perdida = entropia_cruzada(y_ent, red.adelante(X_ent))
    red.p[clave][idx] = original
    return perdida

idx, h = (0, 1), 1e-5
w = red_test.p["W1"][idx]
numerico = (perdida_con_peso(red_test, "W1", idx, w + h) - perdida_con_peso(red_test, "W1", idx, w - h)) / (2 * h)
print("Gradiente por backprop :", round(float(g["W1"][idx]), 6))
print("Gradiente numérico     :", round(float(numerico), 6))
assert abs(g["W1"][idx] - numerico) < 1e-4, "El gradiente de la red no coincide con el numérico"
```

**Qué hace cada línea:**

- `red_test = RedNeuronal(2, 4)` → Guarda en `red_test` el resultado. `RedNeuronal`: red de una capa oculta (ReLU) y salida sigmoide para clasificación binaria.
- `red_test.adelante(X_ent); g = red_test.atras(X_ent, y_ent)` → `adelante`: función definida en el cuaderno.
- `red_test.adelante(X_ent); g = red_test.atras(X_ent, y_ent)` → Guarda en `g` el resultado. `atras`: función definida en el cuaderno.
- `def perdida_con_peso(red, clave, idx, valor):` → Define la función `perdida_con_peso`: Función definida en el cuaderno.
- `idx, h = (0, 1), 1e-5` → Guarda el valor en `idx, h`.
- `w = red_test.p["W1"][idx]` → Guarda el valor en `w`.
- `numerico = (perdida_con_peso(red_test, "W1", idx, w + h) - perdida_con_peso…` → Guarda en `numerico` el resultado. `perdida_con_peso`: función definida en el cuaderno.
- `print("Gradiente por backprop :", round(float(g["W1"][idx]), 6))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `float`: convierte un valor en número decimal.
- `print("Gradiente numérico :", round(float(numerico), 6))` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `float`: convierte un valor en número decimal.
- … y 1 más con las mismas ideas.

### Celda 11 · 6. Entrenamos y comparamos tamaños de capa ocul… · 🏠

**Qué hace:** Practica `mean` (sección «6. Entrenamos y comparamos tamaños de c…»).

```python
resultados = {}
for n_ocultas in (1, 2, 8):
    red = RedNeuronal(2, n_ocultas).entrenar(X_ent, y_ent, epocas=1500, tasa=0.3, X_val=X_val, y_val=y_val)
    resultados[n_ocultas] = red
    print(f"{n_ocultas} neuronas ocultas → precisión validación: {(red.predecir(X_val) == y_val).mean():.3f}")
```

**Qué hace cada línea:**

- `resultados = {}` → Guarda el valor en `resultados`.
- `for n_ocultas in (1, 2, 8):` → Repite el bloque de debajo para cada valor de `n_ocultas` en `(1, 2, 8)`. Dentro del bloque: `entrenar`: función definida en el cuaderno; `RedNeuronal`: red de una capa oculta (ReLU) y salida sigmoide para clasificación binaria; `mean`: calcula la media.

### Celda 12 · 6. Entrenamos y comparamos tamaños de capa ocul… · 🏠

**Qué hace:** Practica `subplots`, `meshgrid`, `zip`, `tight_layout` y más (sección «6. Entrenamos y comparamos tamaños de c…»).

```python
fig, ejes = plt.subplots(1, 3, figsize=(14, 4))
xx, yy = np.meshgrid(np.linspace(-1.6, 1.6, 200), np.linspace(-1.6, 1.6, 200))
rejilla = np.c_[xx.ravel(), yy.ravel()]
for eje, (n, red) in zip(ejes, resultados.items()):
    zona = red.adelante(rejilla).reshape(xx.shape)
    eje.contourf(xx, yy, zona, levels=20, cmap="coolwarm", alpha=0.6)
    eje.scatter(X_val[:, 0], X_val[:, 1], c=y_val, cmap="coolwarm", edgecolor="k", s=15)
    eje.set_title(f"{n} neurona(s) oculta(s)"); eje.set_xlabel("variable 1"); eje.set_ylabel("variable 2")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `fig, ejes = plt.subplots(1, 3, figsize=(14, 4))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `xx, yy = np.meshgrid(np.linspace(-1.6, 1.6, 200), np.linspace(-1.6, 1.6, 20…` → Guarda en `xx, yy` el resultado. `meshgrid`: crea una cuadrícula de coordenadas para dibujar o evaluar funciones en 2D; `linspace`: crea una secuencia de N números equiespaciados entre dos límites.
- `rejilla = np.c_[xx.ravel(), yy.ravel()]` → Guarda en `rejilla` el resultado. `ravel`: aplana un array a una sola dimensión.
- `for eje, (n, red) in zip(ejes, resultados.items()):` → Repite el bloque de debajo para cada valor de `eje, (n, red)` en `zip(ejes, resultados.items())`. Dentro del bloque: `reshape`: cambia la forma de un array (filas × columnas) sin cambiar los datos; `shape`: tamaño de la tabla: (filas, columnas); `adelante`: función definida en el cuaderno.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 13 · 6. Entrenamos y comparamos tamaños de capa ocul… · 🏠

**Qué hace:** Practica `zip`, `plot`, `xlabel`, `ylabel` y más (sección «6. Entrenamos y comparamos tamaños de c…»).

```python
mejor = resultados[8]
epocas_h, perd_ent, perd_val = zip(*mejor.historial)
plt.plot(epocas_h, perd_ent, label="entrenamiento")
plt.plot(epocas_h, perd_val, label="validación")
plt.xlabel("época"); plt.ylabel("pérdida (entropía cruzada)")
plt.title("La pérdida baja: la red está aprendiendo"); plt.legend(); plt.show()
```

**Qué hace cada línea:**

- `mejor = resultados[8]` → Guarda el valor en `mejor`.
- `epocas_h, perd_ent, perd_val = zip(*mejor.historial)` → Guarda en `epocas_h, perd_ent, per…` el resultado. `zip`: recorre varias listas a la vez, emparejando sus elementos.
- `plt.plot(epocas_h, perd_ent, label="entrenamiento")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.plot(epocas_h, perd_val, label="validación")` → `plot`: dibuja una línea (o puntos unidos).
- `plt.xlabel("época"); plt.ylabel("pérdida (entropía cruzada)")` → `xlabel`: pone el nombre del eje horizontal.
- `plt.xlabel("época"); plt.ylabel("pérdida (entropía cruzada)")` → `ylabel`: pone el nombre del eje vertical.
- `plt.title("La pérdida baja: la red está aprendiendo"); plt.legend(); plt.sh…` → `title`: pone el título del gráfico.
- `plt.title("La pérdida baja: la red está aprendiendo"); plt.legend(); plt.sh…` → `legend`: muestra la leyenda del gráfico.
- `plt.title("La pérdida baja: la red está aprendiendo"); plt.legend(); plt.sh…` → `show`: muestra el gráfico.

### Celda 14 · 6. Entrenamos y comparamos tamaños de capa ocul… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 15 · 7. Mini-reto integrador · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S10_01_red_desde_cero.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
