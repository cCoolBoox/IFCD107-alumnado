# Código explicado · S05.06 · CRUD desde Python: `sqlite3` y `pymongo` / `mongomock`

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/notebooks/S05_06_crud_python.ipynb) · [descargar](../notebooks/S05_06_crud_python.ipynb) · ⏱ en clase: 25 min · 🏫 3 celdas de código en clase · 🏠 3 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | Contexto TurisData | Copia de trabajo de la base de datos (así puedes equivocarte sin miedo). |
| 2 | 1 · Conectar y leer (R de CRUD) | Practica `connect`, `read_sql_query`, `fetchone`, `fetchall` y más (sección «1 · Conectar… |
| 5 | 3 · Crear (C): insertar filas y cargar… | Practica `execute`, `commit`, `fetchall` (sección «3 · Crear (C): insertar filas y cargar… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `carpeta` | `tempfile.mkdtemp()` | 1 |
| `ruta_bd` | `os.path.join(carpeta, "turisdata_copia.db")` | 1 |
| `con` | `sqlite3.connect(ruta_bd)` | 2 |
| `cur` | `con.execute("UPDATE alojamientos SET plazas = plazas + 2…` | 7 |
| `docs` | `[dict(f) for f in con.execute("SELECT id_reserva AS _id,…` | 11 |
| `cliente` | `mongomock.MongoClient()` | 11 |
| `coleccion` | `cliente["turisdata"]["reservas_muestra"]` | 11 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `reservas_de_cliente` | Devuelve la lista ordenada de id_reserva del cliente. *(La escribís vosotros en un ejercicio.)* |
| `contar_por_canal_sql` | {canal: número de reservas} leído de SQLite. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `close` | Cierra un fichero, una conexión o una figura. | 10, 11 |
| `commit` | Confirma y guarda los cambios hechos en la base de datos. | 5, 7 |
| `connect` | Abre la conexión con la base de datos. | 2, 11 |
| `copy` | Hace una copia independiente (si cambias la copia, el original no cambia). | 1 |
| `count_documents` | Cuenta los documentos que cumplen una condición. | 11 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 1 |
| `dict` | Crea un diccionario (parejas nombre: valor). | 11 |
| `execute` | Ejecuta una instrucción SQL. | 2, 5, 7, 11 |
| `fetchall` | Recupera todas las filas del resultado. | 2, 5 |
| `fetchone` | Recupera una fila del resultado. | 2 |
| `find_one` | Busca un documento en MongoDB. | 11 |
| `find_spec` | Comprueba si una librería está instalada sin importarla. | 11 |
| `insert_many` | Inserta varios documentos en MongoDB. | 11 |
| `join` | Une una lista de textos en uno solo con un separador. | 1 |
| `mkdtemp` | Crea una carpeta temporal que se borra sola al acabar. | 1 |
| `MongoClient` | Abre la conexión con MongoDB (aquí, simulada con mongomock). | 11 |
| `print` | Muestra un valor por pantalla. | 1, 2, 5, 7, 11 |
| `read_sql_query` | Ejecuta una consulta SQL y devuelve el resultado como tabla. | 2 |
| `run` | Ejecuta un comando del sistema (subprocess) y espera a que acabe. | 11 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏫

**Qué hace:** Copia de trabajo de la base de datos (así puedes equivocarte sin miedo).

```python
import os
import shutil
import sqlite3
import tempfile

import pandas as pd

SEMILLA = 42

# Copia de trabajo de la base de datos (así puedes equivocarte sin miedo)
carpeta = tempfile.mkdtemp()
ruta_bd = os.path.join(carpeta, "turisdata_copia.db")
shutil.copy(dato("turisdata.db"), ruta_bd)
print("Base de trabajo:", ruta_bd)
```

**Qué hace cada línea:**

- `import os` → Trae `os` para poder usarlo.
- `import shutil` → Trae `shutil` para poder usarlo.
- `import sqlite3` → Trae `sqlite3` para poder usarlo.
- `import tempfile` → Trae `tempfile` para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `carpeta = tempfile.mkdtemp()` → Guarda en `carpeta` el resultado. `mkdtemp`: crea una carpeta temporal que se borra sola al acabar.
- `ruta_bd = os.path.join(carpeta, "turisdata_copia.db")` → Guarda en `ruta_bd` el resultado. `join`: une una lista de textos en uno solo con un separador.
- `shutil.copy(dato("turisdata.db"), ruta_bd)` → `copy`: hace una copia independiente (si cambias la copia, el original no cambia); `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- … y 1 más con las mismas ideas.

### Celda 2 · 1 · Conectar y leer (R de CRUD) · 🏫

**Qué hace:** Practica `connect`, `read_sql_query`, `fetchone`, `fetchall` y más (sección «1 · Conectar y leer (R de CRUD)»).

```python
con = sqlite3.connect(ruta_bd)
print(con.execute("SELECT COUNT(*) FROM reservas").fetchone())
print(con.execute("SELECT id_alojamiento, nombre, isla FROM alojamientos LIMIT 3").fetchall())

pd.read_sql_query("SELECT canal, COUNT(*) AS reservas FROM reservas GROUP BY canal", con)
```

**Qué hace cada línea:**

- `con = sqlite3.connect(ruta_bd)` → Guarda en `con` el resultado. `connect`: abre la conexión con la base de datos.
- `print(con.execute("SELECT COUNT(*) FROM reservas").fetchone())` → `print`: muestra un valor por pantalla; `fetchone`: recupera una fila del resultado; `execute`: ejecuta una instrucción SQL.
- `print(con.execute("SELECT id_alojamiento, nombre, isla FROM alojamientos LI…` → `print`: muestra un valor por pantalla; `fetchall`: recupera todas las filas del resultado; `execute`: ejecuta una instrucción SQL.
- `pd.read_sql_query("SELECT canal, COUNT(*) AS reservas FROM reservas GROUP B…` → `read_sql_query`: ejecuta una consulta SQL y devuelve el resultado como tabla.

### Celda 3 · 1 · Conectar y leer (R de CRUD) · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2 · Consultas con parámetros (¡nunca pegues tex… · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 3 · Crear (C): insertar filas y cargar un CSV e… · 🏫

**Qué hace:** Practica `execute`, `commit`, `fetchall` (sección «3 · Crear (C): insertar filas y cargar…»).

```python
con.execute("INSERT INTO alojamientos (id_alojamiento, nombre, isla, categoria, plazas) VALUES (?, ?, ?, ?, ?)",
            (21, "Alojamiento 21", "El Hierro", "casa rural", 12))
con.commit()
print(con.execute("SELECT * FROM alojamientos WHERE id_alojamiento = 21").fetchall())
```

**Qué hace cada línea:**

- `con.execute("INSERT INTO alojamientos (id_alojamiento, nombre, isla, catego…` → `execute`: ejecuta una instrucción SQL.
- `con.commit()` → `commit`: confirma y guarda los cambios hechos en la base de datos.
- `print(con.execute("SELECT * FROM alojamientos WHERE id_alojamiento = 21").f…` → `print`: muestra un valor por pantalla; `fetchall`: recupera todas las filas del resultado; `execute`: ejecuta una instrucción SQL.

### Celda 6 · 3 · Crear (C): insertar filas y cargar un CSV e… · 🏫 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 4 · Actualizar (U) y borrar (D), con transaccio… · 🏠

**Qué hace:** Practica `execute`, `commit` (sección «4 · Actualizar (U) y borrar (D), con tr…»).

```python
cur = con.execute("UPDATE alojamientos SET plazas = plazas + 2 WHERE id_alojamiento = ?", (21,))
print("Filas modificadas:", cur.rowcount)
con.commit()
```

**Qué hace cada línea:**

- `cur = con.execute("UPDATE alojamientos SET plazas = plazas + 2 WHERE id_alo…` → Guarda en `cur` el resultado. `execute`: ejecuta una instrucción SQL.
- `print("Filas modificadas:", cur.rowcount)` → `print`: muestra un valor por pantalla.
- `con.commit()` → `commit`: confirma y guarda los cambios hechos en la base de datos.

### Celda 8 · 4 · Actualizar (U) y borrar (D), con transaccio… · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5 · Consultar la base para analizar (de SQL a p… · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5 · Consultar la base para analizar (de SQL a p… · 🏠

**Qué hace:** Practica `close` (sección «Ejercicio 5 · Ocupación media por mes d…»).

```python
con.close()      # cerrar la conexión al terminar con SQLite
```

**Qué hace cada línea:**

- `con.close() # cerrar la conexión al terminar con SQLite` → `close`: cierra un fichero, una conexión o una figura.

### Celda 11 · 6 · El mismo CRUD en MongoDB (`pymongo`) · 🏠

**Qué hace:** Practica `connect`, `close`, `MongoClient`, `insert_many` y más (sección «6 · El mismo CRUD en MongoDB (`pymongo`)»).

```python
import importlib.util
import subprocess
import sys
if importlib.util.find_spec("mongomock") is None:      # solo hace falta en Colab (necesita internet)
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pymongo", "mongomock"], check=True)
import mongomock

con = sqlite3.connect(ruta_bd)
con.row_factory = sqlite3.Row
docs = [dict(f) for f in con.execute("SELECT id_reserva AS _id, canal, noches, precio_noche, cancelada FROM reservas LIMIT 200")]
con.close()

cliente = mongomock.MongoClient()
coleccion = cliente["turisdata"]["reservas_muestra"]
coleccion.insert_many(docs)
print(coleccion.count_documents({}), coleccion.find_one({}))
```

**Qué hace cada línea:**

- `import importlib.util` → Trae `importlib.util` para poder usarlo.
- `import subprocess` → Trae `subprocess` para poder usarlo.
- `import sys` → Trae `sys` para poder usarlo.
- `if importlib.util.find_spec("mongomock") is None: # solo hace falta en Cola…` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `run`: ejecuta un comando del sistema (subprocess) y espera a que acabe.
- `import mongomock` → Trae `mongomock` para poder usarlo.
- `con = sqlite3.connect(ruta_bd)` → Guarda en `con` el resultado. `connect`: abre la conexión con la base de datos.
- `con.row_factory = sqlite3.Row` → Guarda el valor en `con.row_factory`.
- `docs = [dict(f) for f in con.execute("SELECT id_reserva AS _id, canal, noch…` → Guarda en `docs` el resultado. `dict`: crea un diccionario (parejas nombre: valor); `execute`: ejecuta una instrucción SQL.
- `con.close()` → `close`: cierra un fichero, una conexión o una figura.
- … y 4 más con las mismas ideas.

### Celda 12 · 6 · El mismo CRUD en MongoDB (`pymongo`) · 🏠 · ejercicio 6

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 13 · 7 · Mini-reto integrador: «reservas por canal»… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S05_06_crud_python.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
