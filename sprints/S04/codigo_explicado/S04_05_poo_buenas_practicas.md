# Código explicado · S04.05 · (Opcional) Programación orientada a objetos básica, buenas prácticas y Git

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/notebooks/S04_05_poo_buenas_practicas.ipynb) · [descargar](../notebooks/S04_05_poo_buenas_practicas.ipynb) · ⏱ en clase: 50 min · 🏫 0 celdas de código en clase · 🏠 4 en casa
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
| `r` | `Reserva(5760, "empresa", 3, 89.24, cancelada=True)` | 2 |
| `fila` | `{"id_reserva": "5760", "canal": "empresa", "noches": "3",…` | 4 |
| `demo` | `ColeccionReservas([Reserva(1, "directo", 3, 80.0), Reserv…` | 6 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `Reserva` | Una reserva de TurisData. |
| `__init__` | Función definida en el cuaderno. |
| `ingreso` | Ingreso bruto de la reserva (noches por precio). |
| `__repr__` | Función definida en el cuaderno. |
| `ReservaMejorada` | Reserva con utilidades adicionales. *(La escribís vosotros en un ejercicio.)* |
| `es_larga` | True si la estancia tiene `umbral` noches o más. *(La escribís vosotros en un ejercicio.)* |
| `ReservaCSV` | Reserva que sabe construirse desde una fila del CSV. |
| `desde_fila` | Crea una reserva a partir de una fila (diccionario de textos) del CSV de TurisData. |
| `ReservaGrupo` | Reserva de grupo: 10 % de descuento. *(La escribís vosotros en un ejercicio.)* |
| `ColeccionReservas` | Conjunto de reservas con métodos de análisis. |
| `__len__` | Función definida en el cuaderno. |
| `canceladas` | Número de reservas canceladas. |
| `ColeccionKPI` | Colección con KPIs de negocio. *(La escribís vosotros en un ejercicio.)* |
| `tasa_cancelacion` | Porcentaje de reservas canceladas (1 decimal). *(La escribís vosotros en un ejercicio.)* |
| `ingreso_medio_confirmadas` | Ingreso medio (2 decimales) de las reservas no canceladas. *(La escribís vosotros en un ejercicio.)* |
| `ReservaKPI` | Reserva desde CSV (alias para la colección de KPIs). *(La escribís vosotros en un ejercicio.)* |
| `cargar_coleccion` | Lee el CSV de reservas y devuelve una ColeccionKPI. *(La escribís vosotros en un ejercicio.)* |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `cls` | La propia clase (se usa dentro de un método de clase para crear un objeto nuevo). | 4 |
| `float` | Convierte un valor en número decimal. | 4 |
| `int` | Convierte un valor en número entero. | 4 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 6 |
| `list` | Crea una lista (o convierte algo en lista). | 6 |
| `print` | Muestra un valor por pantalla. | 2, 4, 6 |
| `sum` | Suma todos los valores. | 6 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · Contexto TurisData · 🏠

**Qué hace:** Importa las librerías que usa el cuaderno.

```python
import csv
```

**Qué hace cada línea:**

- `import csv` → Trae `csv` para poder usarlo.

### Celda 2 · 1 · Clases y objetos · 🏠

**Qué hace:** Practica `ingreso` (sección «1 · Clases y objetos»).

```python
class Reserva:
    """Una reserva de TurisData."""

    def __init__(self, id_reserva, canal, noches, precio_noche, cancelada=False):
        self.id_reserva = id_reserva
        self.canal = canal
        self.noches = noches
        self.precio_noche = precio_noche
        self.cancelada = cancelada

    def ingreso(self):
        """Ingreso bruto de la reserva (noches por precio)."""
        return self.noches * self.precio_noche

    def __repr__(self):
        return f"Reserva({self.id_reserva}, {self.canal}, {self.noches} noches)"


r = Reserva(5760, "empresa", 3, 89.24, cancelada=True)
print(r, r.ingreso())
```

**Qué hace cada línea:**

- `class Reserva:` → Define la clase `Reserva`: Una reserva de TurisData.
- `r = Reserva(5760, "empresa", 3, 89.24, cancelada=True)` → Guarda en `r` el resultado. `Reserva`: una reserva de TurisData.
- `print(r, r.ingreso())` → `print`: muestra un valor por pantalla; `ingreso`: ingreso bruto de la reserva (noches por precio).

### Celda 3 · 1 · Clases y objetos · 🏠 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 2 · `@classmethod`: construir objetos desde un… · 🏠

**Qué hace:** Practica `cls` (sección «2 · `@classmethod`: construir objetos d…»).

```python
class ReservaCSV(Reserva):
    """Reserva que sabe construirse desde una fila del CSV."""

    @classmethod
    def desde_fila(cls, fila):
        """Crea una reserva a partir de una fila (diccionario de textos) del CSV de TurisData."""
        return cls(
            id_reserva=int(fila["id_reserva"]),
            canal=fila["canal"],
            noches=int(fila["noches"]),
            precio_noche=float(fila["precio_noche"]),
            cancelada=fila["cancelada"] == "1",
        )


fila = {"id_reserva": "5760", "canal": "empresa", "noches": "3", "precio_noche": "89.24", "cancelada": "1"}
print(ReservaCSV.desde_fila(fila))
```

**Qué hace cada línea:**

- `class ReservaCSV(Reserva):` → Define la clase `ReservaCSV`: Reserva que sabe construirse desde una fila del CSV.
- `fila = {"id_reserva": "5760", "canal": "empresa", "noches": "3", "precio_no…` → Guarda el valor en `fila`.
- `print(ReservaCSV.desde_fila(fila))` → `print`: muestra un valor por pantalla; `desde_fila`: crea una reserva a partir de una fila (diccionario de textos) del CSV de TurisData.

### Celda 5 · 2 · `@classmethod`: construir objetos desde un… · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 3 · Una clase que agrupa objetos · 🏠

**Qué hace:** Practica `list`, `sum` (sección «3 · Una clase que agrupa objetos»).

```python
class ColeccionReservas:
    """Conjunto de reservas con métodos de análisis."""

    def __init__(self, reservas):
        self.reservas = list(reservas)

    def __len__(self):
        return len(self.reservas)

    def canceladas(self):
        """Número de reservas canceladas."""
        return sum(1 for r in self.reservas if r.cancelada)


demo = ColeccionReservas([Reserva(1, "directo", 3, 80.0), Reserva(2, "agencia", 2, 150.0, True)])
print(len(demo), demo.canceladas())
```

**Qué hace cada línea:**

- `class ColeccionReservas:` → Define la clase `ColeccionReservas`: Conjunto de reservas con métodos de análisis.
- `demo = ColeccionReservas([Reserva(1, "directo", 3, 80.0), Reserva(2, "agenc…` → Guarda en `demo` el resultado. `ColeccionReservas`: conjunto de reservas con métodos de análisis; `Reserva`: una reserva de TurisData.
- `print(len(demo), demo.canceladas())` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `canceladas`: número de reservas canceladas.

### Celda 7 · 3 · Una clase que agrupa objetos · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 6 · Mini-reto integrador: el patrón del script · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S04_05_poo_buenas_practicas.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
