# Código explicado · S09.04 · Aprendizaje por refuerzo: Q-learning en el hotel

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_04_q_learning.ipynb) · [descargar](../S09_04_q_learning.ipynb) · ⏱ en clase: 25 min · 🏫 4 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`, `set_theme`. |
| 2 | 1. El entorno: el pasillo del hotel | Practica `class`, `for`, `def` (sección «1. El entorno: el pasillo del hotel»). |
| 5 | 4. Entrenar al agente | Practica `default_rng`, `zeros`, `round`, `append` y más (sección «4. Entrenar al agente»… |
| 6 | 4. Entrenar al agente | Practica `mean`, `subplots`, `plot`, `set_xlabel` y más (sección «4. Entrenar al agente»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `entorno` | `EntornoHotel()` | 2 |
| `s` | `entorno.reset()` | 2 |
| `suave` | `pd.Series(recompensas).rolling(30).mean()` | 6 |
| `flechas` | `{0: "↑", 1: "↓", 2: "←", 3: "→"}` | 8 |
| `mapa` | `np.full((4, 5), "", dtype=object)` | 8 |
| `valores` | `Q.max(axis=1).reshape(4, 5)` | 8 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `EntornoHotel` | Cuadrícula sencilla con la misma interfaz que Gymnasium: reset() y step(accion). |
| `__init__` | Función definida en el cuaderno. |
| `reset` | Función definida en el cuaderno. |
| `estado` | Función definida en el cuaderno. |
| `step` | Función definida en el cuaderno. |
| `actualizar_q` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `elegir_accion` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `entrenar` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `append` | Añade un elemento al final de una lista. | 5 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 5 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 5 |
| `despine` | Quita los bordes superior y derecho del gráfico. | 6 |
| `full` | Crea un array lleno del valor indicado. | 8 |
| `heatmap` | Dibuja una matriz como un mapa de colores. | 8 |
| `legend` | Muestra la leyenda del gráfico. | 6 |
| `max` | Devuelve el valor más grande. | 8 |
| `mean` | Calcula la media. | 5, 6 |
| `plot` | Dibuja una línea (o puntos unidos). | 6 |
| `print` | Muestra un valor por pantalla. | 2, 5 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 5, 8 |
| `reshape` | Cambia la forma de un array (filas × columnas) sin cambiar los datos. | 8 |
| `rolling` | Calcula una media (u otra cosa) en ventanas móviles. | 6 |
| `round` | Redondea un número a los decimales indicados. | 5 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 6 |
| `set_theme` | Elige un estilo visual para todos los gráficos. | 1 |
| `set_title` | Pone el título de un gráfico. | 6, 8 |
| `set_xlabel` | Pone el nombre del eje horizontal. | 6 |
| `set_xticks` | Fija las marcas del eje horizontal. | 8 |
| `set_ylabel` | Pone el nombre del eje vertical. | 6 |
| `set_yticks` | Fija las marcas del eje vertical. | 8 |
| `show` | Muestra el gráfico. | 6, 8 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 6, 8 |
| `text` | Escribe un texto en una posición del gráfico. | 8 |
| `zeros` | Crea un array lleno de ceros. | 5 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `seed`, `set_theme`.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SEMILLA = 42
np.random.seed(SEMILLA)
sns.set_theme(style="white")
```

**Qué hace cada línea:**

- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import seaborn as sns` → Trae `seaborn` (lo llamamos `sns`) para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `np.random.seed(SEMILLA)` → `seed`: fija la semilla del azar para que salga siempre lo mismo.
- `sns.set_theme(style="white")` → `set_theme`: elige un estilo visual para todos los gráficos.

### Celda 2 · 1. El entorno: el pasillo del hotel · 🏫

**Qué hace:** Practica `class`, `for`, `def` (sección «1. El entorno: el pasillo del hotel»).

```python
class EntornoHotel:
    """Cuadrícula sencilla con la misma interfaz que Gymnasium: reset() y step(accion)."""
    FILAS, COLUMNAS = 4, 5
    N_ESTADOS, N_ACCIONES = 20, 4
    PAREDES = {(1, 1), (1, 2), (3, 1)}
    OBRAS = (1, 4)
    META = (3, 4)
    MOVIMIENTOS = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
    NOMBRES_ACCION = ["arriba", "abajo", "izquierda", "derecha"]

    def __init__(self, coste_paso=1.0):
        self.coste_paso = coste_paso      # lo que "cuesta" cada paso (1.0 por defecto)

    def reset(self):
        self.pos = (0, 0)
        return self.estado()

    def estado(self):
        return self.pos[0] * self.COLUMNAS + self.pos[1]

    def step(self, accion):
        df, dc = self.MOVIMIENTOS[accion]
        nueva = (self.pos[0] + df, self.pos[1] + dc)
        dentro = 0 <= nueva[0] < self.FILAS and 0 <= nueva[1] < self.COLUMNAS
        if dentro and nueva not in self.PAREDES:
            self.pos = nueva
        recompensa = -self.coste_paso
        if self.pos == self.OBRAS:
            recompensa -= 5.0
        terminado = self.pos == self.META
        if terminado:
            recompensa += 10.0
        return self.estado(), recompensa, terminado


entorno = EntornoHotel()
s = entorno.reset()
print("Estado inicial:", s)
for a in (3, 3, 1):   # derecha, derecha, abajo (choca con la pared)
    s, r, fin = entorno.step(a)
    print(f"acción {EntornoHotel.NOMBRES_ACCION[a]:>9} → estado {s:>2}, recompensa {r:+.0f}, fin={fin}")
```

**Qué hace cada línea:**

- `class EntornoHotel:` → Define la clase `EntornoHotel`: Cuadrícula sencilla con la misma interfaz que Gymnasium: reset() y step(accion).
- `entorno = EntornoHotel()` → Guarda en `entorno` el resultado. `EntornoHotel`: cuadrícula sencilla con la misma interfaz que Gymnasium: reset() y step(accion).
- `s = entorno.reset()` → Guarda en `s` el resultado. `reset`: función definida en el cuaderno.
- `print("Estado inicial:", s)` → `print`: muestra un valor por pantalla.
- `for a in (3, 3, 1): # derecha, derecha, abajo (choca con la pared)` → Repite el bloque de debajo para cada valor de `a` en `(3, 3, 1)`. Dentro del bloque: `step`: función definida en el cuaderno.

### Celda 3 · 2. La tabla Q y su regla de actualización · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3. Explorar o explotar: epsilon-greedy · 🏫 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 4. Entrenar al agente · 🏫

**Qué hace:** Practica `default_rng`, `zeros`, `round`, `append` y más (sección «4. Entrenar al agente»).

```python
def entrenar(episodios=1500, alpha=0.2, gamma=0.95, epsilon=0.2, semilla=SEMILLA, max_pasos=50, coste_paso=1.0):
    rng = np.random.default_rng(semilla)
    env = EntornoHotel(coste_paso)
    Q = np.zeros((env.N_ESTADOS, env.N_ACCIONES))
    recompensas = []
    for _ in range(episodios):
        s = env.reset()
        total = 0.0
        for _ in range(max_pasos):
            a = elegir_accion(Q, s, epsilon, rng)
            s2, r, fin = env.step(a)
            actualizar_q(Q, s, a, r, s2, alpha, gamma)
            total += r
            s = s2
            if fin:
                break
        recompensas.append(total)
    return Q, np.array(recompensas)

Q, recompensas = entrenar()
print("Recompensa media de los primeros 50 episodios:", recompensas[:50].mean().round(1))
print("Recompensa media de los últimos 50 episodios: ", recompensas[-50:].mean().round(1))
```

**Qué hace cada línea:**

- `def entrenar(episodios=1500, alpha=0.2, gamma=0.95, epsilon=0.2, semilla=SE…` → Define la función `entrenar`: Función definida en el cuaderno.
- `Q, recompensas = entrenar()` → Guarda en `Q, recompensas` el resultado. `entrenar`: función definida en el cuaderno.
- `print("Recompensa media de los primeros 50 episodios:", recompensas[:50].me…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.
- `print("Recompensa media de los últimos 50 episodios: ", recompensas[-50:].m…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.

### Celda 6 · 4. Entrenar al agente · 🏫

**Qué hace:** Practica `mean`, `subplots`, `plot`, `set_xlabel` y más (sección «4. Entrenar al agente»).

```python
suave = pd.Series(recompensas).rolling(30).mean()
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(recompensas, alpha=0.25, label="cada episodio")
ax.plot(suave, color="tab:red", label="media móvil (30)")
ax.set_xlabel("Episodio"); ax.set_ylabel("Recompensa total")
ax.set_title("El agente mejora con la experiencia"); ax.legend()
sns.despine(); plt.show()
```

**Qué hace cada línea:**

- `suave = pd.Series(recompensas).rolling(30).mean()` → Guarda en `suave` el resultado. `mean`: calcula la media; `rolling`: calcula una media (u otra cosa) en ventanas móviles; `Series`: crea una columna de pandas (una sola serie de valores).
- `fig, ax = plt.subplots(figsize=(7, 3.5))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ax.plot(recompensas, alpha=0.25, label="cada episodio")` → `plot`: dibuja una línea (o puntos unidos).
- `ax.plot(suave, color="tab:red", label="media móvil (30)")` → `plot`: dibuja una línea (o puntos unidos).
- `ax.set_xlabel("Episodio"); ax.set_ylabel("Recompensa total")` → `set_xlabel`: pone el nombre del eje horizontal.
- `ax.set_xlabel("Episodio"); ax.set_ylabel("Recompensa total")` → `set_ylabel`: pone el nombre del eje vertical.
- `ax.set_title("El agente mejora con la experiencia"); ax.legend()` → `set_title`: pone el título de un gráfico.
- `ax.set_title("El agente mejora con la experiencia"); ax.legend()` → `legend`: muestra la leyenda del gráfico.
- `sns.despine(); plt.show()` → `despine`: quita los bordes superior y derecho del gráfico.
- … y 1 más con las mismas ideas.

### Celda 7 · 5. Leer la política aprendida · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 5. Leer la política aprendida · 🏠

**Qué hace:** Dibujo de la política: flechas sobre la cuadrícula.

```python
# Dibujo de la política: flechas sobre la cuadrícula
flechas = {0: "↑", 1: "↓", 2: "←", 3: "→"}
mapa = np.full((4, 5), "", dtype=object)
fig, ax = plt.subplots(figsize=(6, 4.5))
valores = Q.max(axis=1).reshape(4, 5)
sns.heatmap(valores, annot=False, cmap="YlGn", cbar_kws={"label": "valor del estado (max Q)"}, ax=ax, linewidths=1, linecolor="white")
for f in range(4):
    for c in range(5):
        if (f, c) in EntornoHotel.PAREDES:
            texto = "PARED"
        elif (f, c) == EntornoHotel.META:
            texto = "META"
        else:
            texto = flechas[politica[f * 5 + c]] + ("\nOBRAS" if (f, c) == EntornoHotel.OBRAS else "")
        ax.text(c + 0.5, f + 0.5, texto, ha="center", va="center", fontsize=13)
ax.set_title("Política aprendida y valor de cada casilla"); ax.set_xticks([]); ax.set_yticks([])
plt.show()
```

**Qué hace cada línea:**

- `flechas = {0: "↑", 1: "↓", 2: "←", 3: "→"}` → Guarda el valor en `flechas`.
- `mapa = np.full((4, 5), "", dtype=object)` → Guarda en `mapa` el resultado. `full`: crea un array lleno del valor indicado.
- `fig, ax = plt.subplots(figsize=(6, 4.5))` → Guarda en `fig, ax` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `valores = Q.max(axis=1).reshape(4, 5)` → Guarda en `valores` el resultado. `reshape`: cambia la forma de un array (filas × columnas) sin cambiar los datos; `max`: devuelve el valor más grande.
- `sns.heatmap(valores, annot=False, cmap="YlGn", cbar_kws={"label": "valor de…` → `heatmap`: dibuja una matriz como un mapa de colores.
- `for f in range(4):` → Repite el bloque de debajo para cada valor de `f` en `range(4)`. Dentro del bloque: `text`: escribe un texto en una posición del gráfico.
- `ax.set_title("Política aprendida y valor de cada casilla"); ax.set_xticks([…` → `set_title`: pone el título de un gráfico.
- `ax.set_title("Política aprendida y valor de cada casilla"); ax.set_xticks([…` → `set_xticks`: fija las marcas del eje horizontal.
- `ax.set_title("Política aprendida y valor de cada casilla"); ax.set_xticks([…` → `set_yticks`: fija las marcas del eje vertical.
- … y 1 más con las mismas ideas.

### Celda 9 · 6. Experimento: ¿qué pasa sin exploración? · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S09_04_q_learning.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
