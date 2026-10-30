# Código explicado · S04.01 · Python desde cero: entorno, variables, tipos y control de flujo

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_01_entorno_sintaxis.ipynb) · [descargar](../S04_01_entorno_sintaxis.ipynb) · ⏱ en clase: 35 min · 🏫 5 celdas de código en clase
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 | 1 · El cuaderno y el entorno | Tu primera celda: print muestra un resultado por pantalla. |
| 2 | 2 · Variables y tipos | Ejemplo resuelto: los datos de una reserva. |
| 4 | 3 · Operadores y texto | Practica `upper`, `replace`, `startswith` (sección «3 · Operadores y texto»). |
| 6 | 4 · Decisiones: `if`, `elif`, `else` | Practica `if`/`elif`/`else` (sección «4 · Decisiones: `if`, `elif`, `else`»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `id_reserva` | `5760` | 2 |
| `noches` | `3` | 2 |
| `precio_noche` | `89.24` | 2 |
| `canal` | `"empresa"` | 2 |
| `cancelada` | `True` | 2 |
| `ingreso` | `noches * precio_noche` | 2 |
| `antelacion_dias` | `45` | 4 |
| `texto` | `"web_intermediaria"` | 4 |
| `ocupadas` | `0` | 8 |

## 3. Palabras de código de este cuaderno

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 4 |
| `print` | Muestra un valor por pantalla. | 1, 2, 4, 6, 8 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 8 |
| `replace` | Sustituye un trozo de texto (o valores de una tabla) por otro. | 4 |
| `startswith` | Comprueba si un texto empieza por algo. | 4 |
| `type` | Dice de qué tipo es un valor (`int`, `str`…). | 2 |
| `upper` | Pasa el texto a mayúsculas. | 4 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 1 · El cuaderno y el entorno · 🏫

**Qué hace:** Tu primera celda: print muestra un resultado por pantalla.

```python
# Tu primera celda: print muestra un resultado por pantalla
print("Hola, TurisData")
2 + 3   # la última expresión de la celda se muestra sola
```

**Qué hace cada línea:**

- `print("Hola, TurisData")` → `print`: muestra un valor por pantalla.

### Celda 2 · 2 · Variables y tipos · 🏫

**Qué hace:** Ejemplo resuelto: los datos de una reserva.

```python
# Ejemplo resuelto: los datos de una reserva
id_reserva = 5760
noches = 3
precio_noche = 89.24          # float: el decimal lleva punto, no coma
canal = "empresa"
cancelada = True

print(type(id_reserva), type(precio_noche), type(canal), type(cancelada))

ingreso = noches * precio_noche
print(f"La reserva {id_reserva} ({canal}) suma {ingreso:.2f} EUR")   # :.2f = 2 decimales
```

**Qué hace cada línea:**

- `id_reserva = 5760` → Guarda el valor en `id_reserva`.
- `noches = 3` → Guarda el valor en `noches`.
- `precio_noche = 89.24 # float: el decimal lleva punto, no coma` → Guarda el valor en `precio_noche`.
- `canal = "empresa"` → Guarda el valor en `canal`.
- `cancelada = True` → Guarda el valor en `cancelada`.
- `print(type(id_reserva), type(precio_noche), type(canal), type(cancelada))` → `print`: muestra un valor por pantalla; `type`: dice de qué tipo es un valor (`int`, `str`…).
- `ingreso = noches * precio_noche` → Guarda el valor en `ingreso`.
- `print(f"La reserva {id_reserva} ({canal}) suma {ingreso:.2f} EUR") # :.2f =…` → `print`: muestra un valor por pantalla.

### Celda 3 · 2 · Variables y tipos · 🏫 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 3 · Operadores y texto · 🏫

**Qué hace:** Practica `upper`, `replace`, `startswith` (sección «3 · Operadores y texto»).

```python
print(7 / 2, 7 // 2, 7 % 2, 2 ** 3)
antelacion_dias = 45
print(antelacion_dias > 30 and antelacion_dias <= 60)

texto = "web_intermediaria"
print(texto.upper(), texto.replace("_", " "), len(texto), texto.startswith("web"))
```

**Qué hace cada línea:**

- `print(7 / 2, 7 // 2, 7 % 2, 2 ** 3)` → `print`: muestra un valor por pantalla.
- `antelacion_dias = 45` → Guarda el valor en `antelacion_dias`.
- `print(antelacion_dias > 30 and antelacion_dias <= 60)` → `print`: muestra un valor por pantalla.
- `texto = "web_intermediaria"` → Guarda el valor en `texto`.
- `print(texto.upper(), texto.replace("_", " "), len(texto), texto.startswith(…` → `print`: muestra un valor por pantalla; `upper`: pasa el texto a mayúsculas; `replace`: sustituye un trozo de texto (o valores de una tabla) por otro.

### Celda 5 · 3 · Operadores y texto · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 4 · Decisiones: `if`, `elif`, `else` · 🏫

**Qué hace:** Practica `if`/`elif`/`else` (sección «4 · Decisiones: `if`, `elif`, `else`»).

```python
antelacion_dias = 45
if antelacion_dias >= 90:
    grupo = "muy anticipada"
elif antelacion_dias >= 30:
    grupo = "anticipada"
else:
    grupo = "última hora"
print(grupo)
```

**Qué hace cada línea:**

- `antelacion_dias = 45` → Guarda el valor en `antelacion_dias`.
- `if antelacion_dias >= 90:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no).
- `print(grupo)` → `print`: muestra un valor por pantalla.

### Celda 7 · 4 · Decisiones: `if`, `elif`, `else` · 🏫 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 5 · Repetir: `for` y `while` · 🏫

**Qué hace:** Practica `for`, `while` (sección «5 · Repetir: `for` y `while`»).

```python
for noche in range(1, 4):
    print("Noche", noche)

ocupadas = 0
while ocupadas < 3:
    ocupadas += 1          # forma corta de ocupadas = ocupadas + 1
print("Habitaciones ocupadas:", ocupadas)
```

**Qué hace cada línea:**

- `for noche in range(1, 4):` → Repite el bloque de debajo para cada valor de `noche` en `range(1, 4)`.
- `ocupadas = 0` → Guarda el valor en `ocupadas`.
- `while ocupadas < 3:` → Repite el bloque de debajo mientras se cumpla la condición.
- `print("Habitaciones ocupadas:", ocupadas)` → `print`: muestra un valor por pantalla.

### Celda 9 · 5 · Repetir: `for` y `while` · 🏠 · ejercicio 4

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5 · Repetir: `for` y `while` · 🏠 · ejercicio 5

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 6 · Mini-reto integrador: presupuesto de una re… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S04_01_entorno_sintaxis.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
