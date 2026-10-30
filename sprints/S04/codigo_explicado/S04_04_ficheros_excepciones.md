# Código explicado · S04.04 · Ficheros CSV y JSON con la biblioteca estándar, y excepciones

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_04_ficheros_excepciones.ipynb) · [descargar](../notebooks/S04_04_ficheros_excepciones.ipynb) · ⏱ en clase: 40 min · 🏫 4 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | Contexto TurisData | Practica `dato` (sección «Contexto TurisData»). |
| 2 | 1 · Leer un CSV con `csv.DictReader` | Practica `open`, `list`, `type`, `DictReader` (sección «1 · Leer un CSV con `csv.DictRead… |
| 5 | 2 · Escribir y leer JSON | Practica `mkdtemp`, `join`, `open`, `read` (sección «2 · Escribir y leer JSON»). |
| 7 | 3 · Excepciones: cuando algo falla | Practica `open` (sección «3 · Excepciones: cuando algo falla»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `ruta_reservas` | `dato("reservas_turisdata.csv")` | 1 |
| `carpeta` | `tempfile.mkdtemp()` | 5 |
| `ruta_json` | `os.path.join(carpeta, "resumen.json")` | 5 |
| `resumen` | `{"cliente": "TurisData Canarias", "reservas": 6000, "cana…` | 5 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `a_float_seguro` | Convierte a float; devuelve `defecto` si no es posible. *(La escribís vosotros en un ejercicio.)* |
| `leer_csv` | Lee un CSV y valida su cabecera. Lanza FileNotFoundError o ValueError con mensajes claros. *(La escribís vosotros en un ejercicio.)* |
| `resumen_canales` | Resume las reservas por canal ignorando filas con valores no numéricos. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `DictReader` | Lee un CSV fila a fila como diccionarios (cabecera = claves). | 2 |
| `dump` | Escribe datos de Python en un fichero JSON. | 5 |
| `float` | Convierte un valor en número decimal. | 7 |
| `join` | Une una lista de textos en uno solo con un separador. | 5 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2 |
| `list` | Crea una lista (o convierte algo en lista). | 2 |
| `load` | Lee un fichero JSON y lo convierte en datos de Python. | 5 |
| `mkdtemp` | Crea una carpeta temporal que se borra sola al acabar. | 5 |
| `open` | Abre un fichero para leerlo o escribirlo. | 2, 5, 7 |
| `print` | Muestra un valor por pantalla. | 1, 2, 5, 7 |
| `read` | Lee el contenido de un fichero. | 5 |
| `type` | Dice de qué tipo es un valor (`int`, `str`…). | 2 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏫

**Qué hace:** Practica `dato` (sección «Contexto TurisData»).

```python
import csv
import json
import os
import tempfile

ruta_reservas = dato("reservas_turisdata.csv")
print(ruta_reservas)
```

**Qué hace cada línea:**

- `import csv` → Trae `csv` para poder usarlo.
- `import json` → Trae `json` para poder usarlo.
- `import os` → Trae `os` para poder usarlo.
- `import tempfile` → Trae `tempfile` para poder usarlo.
- `ruta_reservas = dato("reservas_turisdata.csv")` → Guarda en `ruta_reservas` el resultado. `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `print(ruta_reservas)` → `print`: muestra un valor por pantalla.

### Celda 2 · 1 · Leer un CSV con `csv.DictReader` · 🏫

**Qué hace:** Practica `open`, `list`, `type`, `DictReader` (sección «1 · Leer un CSV con `csv.DictReader`»).

```python
with open(ruta_reservas, newline="", encoding="utf8") as f:
    filas = list(csv.DictReader(f))

print(len(filas), "filas")
print(filas[0])
print(type(filas[0]["noches"]), "-> hay que convertir con int()")
```

**Qué hace cada línea:**

- `with open(ruta_reservas, newline="", encoding="utf8") as f:` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `list`: crea una lista (o convierte algo en lista); `DictReader`: lee un CSV fila a fila como diccionarios (cabecera = claves).
- `print(len(filas), "filas")` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `print(filas[0])` → `print`: muestra un valor por pantalla.
- `print(type(filas[0]["noches"]), "-> hay que convertir con int()")` → `print`: muestra un valor por pantalla; `type`: dice de qué tipo es un valor (`int`, `str`…).

### Celda 3 · 1 · Leer un CSV con `csv.DictReader` · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 1 · Leer un CSV con `csv.DictReader` · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 2 · Escribir y leer JSON · 🏫

**Qué hace:** Practica `mkdtemp`, `join`, `open`, `read` (sección «2 · Escribir y leer JSON»).

```python
carpeta = tempfile.mkdtemp()
ruta_json = os.path.join(carpeta, "resumen.json")

resumen = {"cliente": "TurisData Canarias", "reservas": 6000, "canales": ["directo", "agencia"]}
with open(ruta_json, "w", encoding="utf8") as f:
    json.dump(resumen, f, ensure_ascii=False, indent=2)

print(open(ruta_json, encoding="utf8").read())
with open(ruta_json, encoding="utf8") as f:
    leido = json.load(f)
print(leido == resumen)
```

**Qué hace cada línea:**

- `carpeta = tempfile.mkdtemp()` → Guarda en `carpeta` el resultado. `mkdtemp`: crea una carpeta temporal que se borra sola al acabar.
- `ruta_json = os.path.join(carpeta, "resumen.json")` → Guarda en `ruta_json` el resultado. `join`: une una lista de textos en uno solo con un separador.
- `resumen = {"cliente": "TurisData Canarias", "reservas": 6000, "canales": ["…` → Guarda el valor en `resumen`.
- `with open(ruta_json, "w", encoding="utf8") as f:` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `dump`: escribe datos de Python en un fichero JSON.
- `print(open(ruta_json, encoding="utf8").read())` → `print`: muestra un valor por pantalla; `read`: lee el contenido de un fichero; `open`: abre un fichero para leerlo o escribirlo.
- `with open(ruta_json, encoding="utf8") as f:` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `load`: lee un fichero JSON y lo convierte en datos de Python.
- `print(leido == resumen)` → `print`: muestra un valor por pantalla.

### Celda 6 · 2 · Escribir y leer JSON · 🏫 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 3 · Excepciones: cuando algo falla · 🏫

**Qué hace:** Practica `open` (sección «3 · Excepciones: cuando algo falla»).

```python
for texto in ["89.24", "", "tres"]:
    try:
        precio = float(texto)
    except ValueError:
        print(f"{texto!r}: no es un número válido")
    else:
        print(f"{texto!r}: {precio}")
    finally:
        pass   # aquí iría la limpieza (cerrar conexiones, etc.)

try:
    open("no_existe.csv", encoding="utf8")
except FileNotFoundError as error:
    print("Aviso:", error)
```

**Qué hace cada línea:**

- `for texto in ["89.24", "", "tres"]:` → Repite el bloque de debajo para cada valor de `texto` en `["89.24", "", "tres"]`.
- `try:` → Intenta el bloque; si ocurre un error, pasa al `except` en vez de romperse. Dentro del bloque: `open`: abre un fichero para leerlo o escribirlo.

### Celda 8 · 3 · Excepciones: cuando algo falla · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 3 · Excepciones: cuando algo falla · 🏫 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 4 · Mini-reto integrador: resumen tolerante a f… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S04_04_ficheros_excepciones.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
