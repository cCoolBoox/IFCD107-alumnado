# Código explicado · S04.02 · Funciones y módulos

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_02_funciones_modulos.ipynb) · [descargar](../notebooks/S04_02_funciones_modulos.ipynb) · ⏱ en clase: 35 min · 🏫 4 celdas de código en clase · 🏠 1 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | 1 · Definir una función | Practica `help` (sección «1 · Definir una función»). |
| 2 | 1 · Definir una función | Practica `def` (sección «1 · Definir una función»). |
| 5 | 2 · `*args`, `**kwargs` y `lambda` | Practica `join`, `sorted`, `sum`, `items` (sección «2 · `*args`, `**kwargs` y `lambda`»). |
| 7 | 3 · Módulos: importar código ya escrito | Practica `date`, `sqrt`, `ceil`, `mean` y más (sección «3 · Módulos: importar código ya e… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `reservas` | `[("A", 3, 80.0), ("B", 5, 60.0), ("C", 2, 150.0)]` | 5 |
| `llegada` | `date(2025, 12, 24)` | 7 |
| `salida` | `date(2025, 12, 28)` | 7 |
| `carpeta` | `tempfile.mkdtemp()` | 9 |
| `utilidades_turisdata` | `importlib.import_module("utilidades_turisdata")` | 9 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `ingreso_reserva` | Devuelve el ingreso bruto de una reserva (noches por precio de la noche). |
| `ingreso_con_tasa` | Ingreso de la reserva incluyendo la tasa turística por noche (1,5 EUR por defecto). |
| `clasificar_antelacion` | Clasifica una reserva según los días de antelación. *(La escribís vosotros en un ejercicio.)* |
| `precio_final` | Importe de la estancia tras aplicar un descuento (0-1), redondeado a 2 decimales. *(La escribís vosotros en un ejercicio.)* |
| `media` | Media de todos los valores recibidos. |
| `ficha` | Devuelve una línea con los datos recibidos como pares clave=valor. |
| `maximo_ingreso` | Devuelve el mayor de los ingresos recibidos. *(La escribís vosotros en un ejercicio.)* |
| `noches_entre` | Noches entre dos fechas ISO (AAAA-MM-DD). *(La escribís vosotros en un ejercicio.)* |
| `tasa_cancelacion` | Porcentaje de reservas canceladas (1 decimal); 0.0 si no hay reservas. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `ceil` | Redondea hacia arriba. | 7 |
| `date` | Crea una fecha (año, mes, día). | 7 |
| `help` | Muestra la ayuda (el docstring) de una función. | 1 |
| `import_module` | Importa una librería a partir de su nombre escrito como texto. | 9 |
| `ingreso` | Calcula el ingreso de una reserva (noches × precio). | 9 |
| `insert` | Inserta elementos en una posición. | 9 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 5 |
| `join` | Une una lista de textos en uno solo con un separador. | 5, 9 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 5 |
| `mean` | Calcula la media. | 7 |
| `median` | Calcula la mediana (el valor central). | 7 |
| `mkdtemp` | Crea una carpeta temporal que se borra sola al acabar. | 9 |
| `open` | Abre un fichero para leerlo o escribirlo. | 9 |
| `pct` | Calcula un porcentaje. | 9 |
| `print` | Muestra un valor por pantalla. | 1, 2, 5, 7, 9 |
| `sorted` | Devuelve los elementos ordenados, sin cambiar el original. | 5 |
| `sqrt` | Raíz cuadrada. | 7 |
| `sum` | Suma todos los valores. | 5 |
| `write` | Escribe en un fichero. | 9 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 1 · Definir una función · 🏫

**Qué hace:** Practica `help` (sección «1 · Definir una función»).

```python
def ingreso_reserva(noches, precio_noche):
    """Devuelve el ingreso bruto de una reserva (noches por precio de la noche)."""
    return noches * precio_noche

print(ingreso_reserva(3, 89.24))
help(ingreso_reserva)     # muestra el docstring
```

**Qué hace cada línea:**

- `def ingreso_reserva(noches, precio_noche):` → Define la función `ingreso_reserva`: Devuelve el ingreso bruto de una reserva (noches por precio de la noche).
- `print(ingreso_reserva(3, 89.24))` → `print`: muestra un valor por pantalla; `ingreso_reserva`: devuelve el ingreso bruto de una reserva (noches por precio de la noche).
- `help(ingreso_reserva) # muestra el docstring` → `help`: muestra la ayuda (el docstring) de una función.

### Celda 2 · 1 · Definir una función · 🏫

**Qué hace:** Practica `def` (sección «1 · Definir una función»).

```python
def ingreso_con_tasa(noches, precio_noche, tasa_por_noche=1.5):
    """Ingreso de la reserva incluyendo la tasa turística por noche (1,5 EUR por defecto)."""
    return noches * (precio_noche + tasa_por_noche)

print(ingreso_con_tasa(4, 80))                       # usa la tasa por defecto
print(ingreso_con_tasa(4, 80, tasa_por_noche=0))     # sin tasa
```

**Qué hace cada línea:**

- `def ingreso_con_tasa(noches, precio_noche, tasa_por_noche=1.5):` → Define la función `ingreso_con_tasa`: Ingreso de la reserva incluyendo la tasa turística por noche (1,5 EUR por defecto).
- `print(ingreso_con_tasa(4, 80)) # usa la tasa por defecto` → `print`: muestra un valor por pantalla; `ingreso_con_tasa`: ingreso de la reserva incluyendo la tasa turística por noche (1,5 EUR por defecto).
- `print(ingreso_con_tasa(4, 80, tasa_por_noche=0)) # sin tasa` → `print`: muestra un valor por pantalla; `ingreso_con_tasa`: ingreso de la reserva incluyendo la tasa turística por noche (1,5 EUR por defecto).

### Celda 3 · 1 · Definir una función · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1 · Definir una función · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2 · `*args`, `**kwargs` y `lambda` · 🏫

**Qué hace:** Practica `join`, `sorted`, `sum`, `items` (sección «2 · `*args`, `**kwargs` y `lambda`»).

```python
def media(*valores):
    """Media de todos los valores recibidos."""
    return sum(valores) / len(valores)

def ficha(**datos):
    """Devuelve una línea con los datos recibidos como pares clave=valor."""
    return ", ".join(f"{k}={v}" for k, v in datos.items())

print(media(60, 72.5, 89.24))
print(ficha(canal="directo", noches=3))

reservas = [("A", 3, 80.0), ("B", 5, 60.0), ("C", 2, 150.0)]
print(sorted(reservas, key=lambda r: r[1] * r[2], reverse=True))    # ordenar por ingreso
```

**Qué hace cada línea:**

- `def media(*valores):` → Define la función `media`: Media de todos los valores recibidos.
- `def ficha(**datos):` → Define la función `ficha`: Devuelve una línea con los datos recibidos como pares clave=valor.
- `print(media(60, 72.5, 89.24))` → `print`: muestra un valor por pantalla; `media`: media de todos los valores recibidos.
- `print(ficha(canal="directo", noches=3))` → `print`: muestra un valor por pantalla; `ficha`: devuelve una línea con los datos recibidos como pares clave=valor.
- `reservas = [("A", 3, 80.0), ("B", 5, 60.0), ("C", 2, 150.0)]` → Guarda el valor en `reservas`.
- `print(sorted(reservas, key=lambda r: r[1] * r[2], reverse=True)) # ordenar…` → `print`: muestra un valor por pantalla; `sorted`: devuelve los elementos ordenados, sin cambiar el original.

### Celda 6 · 2 · `*args`, `**kwargs` y `lambda` · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 3 · Módulos: importar código ya escrito · 🏫

**Qué hace:** Practica `date`, `sqrt`, `ceil`, `mean` y más (sección «3 · Módulos: importar código ya escrito»).

```python
import math
import statistics
from datetime import date

print(math.sqrt(16), math.ceil(4.2))
print(statistics.mean([60, 72.5, 89.24]), statistics.median([60, 72.5, 89.24]))

llegada = date(2025, 12, 24)
salida = date(2025, 12, 28)
print("Noches:", (salida - llegada).days)
```

**Qué hace cada línea:**

- `import math` → Trae `math` para poder usarlo.
- `import statistics` → Trae `statistics` para poder usarlo.
- `from datetime import date` → Trae `date` de `datetime` para poder usarlo.
- `print(math.sqrt(16), math.ceil(4.2))` → `print`: muestra un valor por pantalla; `sqrt`: raíz cuadrada; `ceil`: redondea hacia arriba.
- `print(statistics.mean([60, 72.5, 89.24]), statistics.median([60, 72.5, 89.2…` → `print`: muestra un valor por pantalla; `mean`: calcula la media; `median`: calcula la mediana (el valor central).
- `llegada = date(2025, 12, 24)` → Guarda en `llegada` el resultado. `date`: crea una fecha (año, mes, día).
- `salida = date(2025, 12, 28)` → Guarda en `salida` el resultado. `date`: crea una fecha (año, mes, día).
- `print("Noches:", (salida - llegada).days)` → `print`: muestra un valor por pantalla.

### Celda 8 · 3 · Módulos: importar código ya escrito · 🏫 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 4 · Crear tu propio módulo · 🏠

**Qué hace:** Practica `mkdtemp`, `insert`, `import_module`, `open` y más (sección «4 · Crear tu propio módulo»).

```python
import importlib
import os
import sys
import tempfile

carpeta = tempfile.mkdtemp()
with open(os.path.join(carpeta, "utilidades_turisdata.py"), "w", encoding="utf8") as f:
    f.write('''"""Utilidades de TurisData."""

def ingreso(noches, precio):
    """Ingreso bruto de una reserva."""
    return noches * precio

def pct(parte, total):
    """Porcentaje con 1 decimal; 0.0 si el total es 0."""
    return round(100 * parte / total, 1) if total else 0.0
''')
sys.path.insert(0, carpeta)                 # para que Python encuentre el módulo
utilidades_turisdata = importlib.import_module("utilidades_turisdata")
print(utilidades_turisdata.ingreso(3, 80), utilidades_turisdata.pct(2754, 6000))
```

**Qué hace cada línea:**

- `import importlib` → Trae `importlib` para poder usarlo.
- `import os` → Trae `os` para poder usarlo.
- `import sys` → Trae `sys` para poder usarlo.
- `import tempfile` → Trae `tempfile` para poder usarlo.
- `carpeta = tempfile.mkdtemp()` → Guarda en `carpeta` el resultado. `mkdtemp`: crea una carpeta temporal que se borra sola al acabar.
- `with open(os.path.join(carpeta, "utilidades_turisdata.py"), "w", encoding="…` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `write`: escribe en un fichero.
- `sys.path.insert(0, carpeta) # para que Python encuentre el módulo` → `insert`: inserta elementos en una posición.
- `utilidades_turisdata = importlib.import_module("utilidades_turisdata")` → Guarda en `utilidades_turisdata` el resultado. `import_module`: importa una librería a partir de su nombre escrito como texto.
- `print(utilidades_turisdata.ingreso(3, 80), utilidades_turisdata.pct(2754, 6…` → `print`: muestra un valor por pantalla; `ingreso`: calcula el ingreso de una reserva (noches × precio); `pct`: calcula un porcentaje.

### Celda 10 · 5 · Mini-reto integrador: una función de KPI · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S04_02_funciones_modulos.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
