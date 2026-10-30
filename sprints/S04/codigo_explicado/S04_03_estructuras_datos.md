# Código explicado · S04.03 · Estructuras de datos: listas, tuplas, diccionarios y conjuntos

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_03_estructuras_datos.ipynb) · [descargar](../notebooks/S04_03_estructuras_datos.ipynb) · ⏱ en clase: 30 min · 🏫 4 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | 1 · Listas y tuplas | Practica `append`, `sort`, `min`, `max` y más (sección «1 · Listas y tuplas»). |
| 3 | 2 · Diccionarios | Contar categorías: patrón muy frecuente. |
| 5 | 3 · Una lista de diccionarios = una tab… | Crea `reservas`. |
| 6 | 4 · Conjuntos y comprensiones | Practica una comprensión de lista (sección «4 · Conjuntos y comprensiones»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `precios` | `[89.24, 63.5, 120.0, 95.0, 70.0]` | 1 |
| `punto` | `(28.46, -16.25)` | 1 |
| `reserva` | `{"id_reserva": 5760, "canal": "empresa", "noches": 3, "pr…` | 3 |
| `canales` | `["directo", "agencia", "directo", "web", "web", "web"]` | 3 |
| `conteo` | `{}` | 3 |
| `reservas` | `[ {"id": 1, "canal": "directo", "noches": 3, "precio_noch…` | 5 |
| `canales_distintos` | `{r["canal"] for r in reservas}` | 6 |
| `ingresos` | `[r["noches"] * r["precio_noche"] for r in reservas]` | 6 |
| `largas` | `[r["id"] for r in reservas if r["noches"] >= 4]` | 6 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `append` | Añade un elemento al final de una lista. | 1 |
| `get` | Lee un valor de un diccionario; si no existe, devuelve el valor por defecto en vez de fallar. | 3 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 3 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 1, 5 |
| `max` | Devuelve el valor más grande. | 1 |
| `min` | Devuelve el valor más pequeño. | 1 |
| `print` | Muestra un valor por pantalla. | 1, 3, 5, 6 |
| `sort` | Ordena la lista en su sitio. | 1 |
| `sum` | Suma todos los valores. | 1 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 1 · Listas y tuplas · 🏫

**Qué hace:** Practica `append`, `sort`, `min`, `max` y más (sección «1 · Listas y tuplas»).

```python
precios = [89.24, 63.5, 120.0, 95.0, 70.0]
print(precios[0], precios[-1], precios[1:3], len(precios))

precios.append(150.0)          # añade al final
precios.sort()                 # ordena la propia lista
print(precios, min(precios), max(precios), sum(precios) / len(precios))

punto = (28.46, -16.25)        # tupla: latitud, longitud de Santa Cruz de Tenerife
lat, lon = punto               # desempaquetado
print(lat, lon)
```

**Qué hace cada línea:**

- `precios = [89.24, 63.5, 120.0, 95.0, 70.0]` → Guarda el valor en `precios`.
- `print(precios[0], precios[-1], precios[1:3], len(precios))` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `precios.append(150.0) # añade al final` → `append`: añade un elemento al final de una lista.
- `precios.sort() # ordena la propia lista` → `sort`: ordena la lista en su sitio.
- `print(precios, min(precios), max(precios), sum(precios) / len(precios))` → `print`: muestra un valor por pantalla; `min`: devuelve el valor más pequeño; `max`: devuelve el valor más grande.
- `punto = (28.46, -16.25) # tupla: latitud, longitud de Santa Cruz de Tenerife` → Guarda el valor en `punto`.
- `lat, lon = punto # desempaquetado` → Guarda el valor en `lat, lon`.
- `print(lat, lon)` → `print`: muestra un valor por pantalla.

### Celda 2 · 1 · Listas y tuplas · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 3 · 2 · Diccionarios · 🏫

**Qué hace:** Contar categorías: patrón muy frecuente.

```python
reserva = {"id_reserva": 5760, "canal": "empresa", "noches": 3, "precio_noche": 89.24, "cancelada": 1}
print(reserva["canal"], reserva.get("pais", "desconocido"))
reserva["regimen"] = "media_pension"          # añadir o modificar
for clave, valor in reserva.items():
    print(f"{clave:>13} -> {valor}")

# Contar categorías: patrón muy frecuente
canales = ["directo", "agencia", "directo", "web", "web", "web"]
conteo = {}
for c in canales:
    conteo[c] = conteo.get(c, 0) + 1
print(conteo)
```

**Qué hace cada línea:**

- `reserva = {"id_reserva": 5760, "canal": "empresa", "noches": 3, "precio_noc…` → Guarda el valor en `reserva`.
- `print(reserva["canal"], reserva.get("pais", "desconocido"))` → `print`: muestra un valor por pantalla; `get`: lee un valor de un diccionario; si no existe, devuelve el valor por defecto en vez de fallar.
- `reserva["regimen"] = "media_pension" # añadir o modificar` → Guarda el valor en `reserva["regimen"]`.
- `for clave, valor in reserva.items():` → Repite el bloque de debajo para cada valor de `clave, valor` en `reserva.items()`.
- `canales = ["directo", "agencia", "directo", "web", "web", "web"]` → Guarda el valor en `canales`.
- `conteo = {}` → Guarda el valor en `conteo`.
- `for c in canales:` → Repite el bloque de debajo para cada valor de `c` en `canales`. Dentro del bloque: `get`: lee un valor de un diccionario; si no existe, devuelve el valor por defecto en vez de fallar.
- `print(conteo)` → `print`: muestra un valor por pantalla.

### Celda 4 · 2 · Diccionarios · 🏫 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 3 · Una lista de diccionarios = una tabla · 🏫

**Qué hace:** Crea `reservas`.

```python
reservas = [
    {"id": 1, "canal": "directo", "noches": 3, "precio_noche": 80.0, "cancelada": 0},
    {"id": 2, "canal": "web_intermediaria", "noches": 5, "precio_noche": 60.0, "cancelada": 1},
    {"id": 3, "canal": "agencia", "noches": 2, "precio_noche": 150.0, "cancelada": 0},
    {"id": 4, "canal": "web_intermediaria", "noches": 7, "precio_noche": 95.0, "cancelada": 1},
    {"id": 5, "canal": "directo", "noches": 4, "precio_noche": 110.0, "cancelada": 0},
    {"id": 6, "canal": "agencia", "noches": 1, "precio_noche": 70.0, "cancelada": 1},
]
print(len(reservas), reservas[0]["canal"])
```

**Qué hace cada línea:**

- `reservas = [` → Guarda el valor en `reservas`.
- `print(len(reservas), reservas[0]["canal"])` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.

### Celda 6 · 4 · Conjuntos y comprensiones · 🏫

**Qué hace:** Practica una comprensión de lista (sección «4 · Conjuntos y comprensiones»).

```python
canales_distintos = {r["canal"] for r in reservas}                    # comprensión de conjunto
ingresos = [r["noches"] * r["precio_noche"] for r in reservas]        # comprensión de lista
largas = [r["id"] for r in reservas if r["noches"] >= 4]              # con filtro
print(canales_distintos, ingresos, largas)
```

**Qué hace cada línea:**

- `canales_distintos = {r["canal"] for r in reservas} # comprensión de conjunto` → Guarda el valor en `canales_distintos`.
- `ingresos = [r["noches"] * r["precio_noche"] for r in reservas] # comprensió…` → Guarda el valor en `ingresos`.
- `largas = [r["id"] for r in reservas if r["noches"] >= 4] # con filtro` → Guarda el valor en `largas`.
- `print(canales_distintos, ingresos, largas)` → `print`: muestra un valor por pantalla.

### Celda 7 · 4 · Conjuntos y comprensiones · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4 · Conjuntos y comprensiones · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 9 · 5 · Mini-reto integrador: cancelaciones por can… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S04_03_estructuras_datos.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
