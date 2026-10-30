# Código explicado · S05.07 · Reto PBL «¿La ocupación depende de esto?» (plantilla del cuaderno entregable)

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_07_reto_ocupacion.ipynb) · [descargar](../S05_07_reto_ocupacion.ipynb) · 🏫 2 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | Qué debes entregar (este mismo cuaderno… | Importa las librerías que usa el cuaderno y fija `SEMILLA`. |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `RUTA_BD` | `"turisdata_reto.db"` | 1 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `gradiente_mse` | Gradiente del error cuadrático medio de y_pred = X @ w. *(La escribís vosotros en un ejercicio.)* |
| `entrenar` | Descenso del gradiente. Devuelve (w, historial de MSE). *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `close` | Cierra un fichero, una conexión o una figura. | 8 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Qué debes entregar (este mismo cuaderno, comple… · 🏫

**Qué hace:** Importa las librerías que usa el cuaderno y fija `SEMILLA`.

```python
import os
import sqlite3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats

SEMILLA = 42
RUTA_BD = "turisdata_reto.db"        # el archivo que entregarás junto al cuaderno
```

**Qué hace cada línea:**

- `import os` → Trae `os` para poder usarlo.
- `import sqlite3` → Trae `sqlite3` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import statsmodels.formula.api as smf` → Trae `statsmodels.formula.api` (lo llamamos `smf`) para poder usarlo.
- `from scipy import stats` → Trae `stats` de `scipy` para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `RUTA_BD = "turisdata_reto.db" # el archivo que entregarás junto al cuaderno` → Guarda el valor en `RUTA_BD`.

### Celda 2 · 1 · Base de datos: cargar y consultar · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 3 · 2 · Primer vistazo a los datos · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3 · Regresión lineal desde cero (descenso del g… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 3 · Regresión lineal desde cero (descenso del g… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 4 · Contraste con una librería · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 5 · Responder con estadística · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 7 · Reproducibilidad: antes de entregar · 🏫

**Qué hace:** Practica `close` (sección «7 · Reproducibilidad: antes de entregar»).

```python
con.close()
```

**Qué hace cada línea:**

- `con.close()` → `close`: cierra un fichero, una conexión o una figura.

---
*Generado a partir de `laboratorios/fuentes/S05_07_reto_ocupacion.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
