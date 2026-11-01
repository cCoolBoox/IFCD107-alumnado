# Misión 3 · Funciones que calculan

> ⏱ **50 minutos + 40 minutos** (la segunda parte, después de la consolidación) · 🅰️ Fase 1 · martes · 👥 Piloto y copiloto (cambiad de papel entre las dos partes) · [Volver al índice](../README.md)

## 🎯 Qué construís

Las **primeras funciones de `kpis.py`**, la herramienta del cliente: `tasa_cancelacion_por_canal` e `ingreso_medio_por_reserva` (y `ocupacion_proxy`, que se hace con el docente). Es lo mismo que contasteis en la misión 2, pero metido en una función que **devuelve** el resultado. Esta vez trabajáis **con pruebas** que os dicen si está bien.

## 💡 La idea clave

**Una función es una máquina: entra algo, sale algo.** Aquí entra la lista de reservas y sale un número (o un diccionario).

```python
def noches_totales(reservas):          # entra: la lista de reservas
    total = 0
    for r in reservas:
        total = total + r["noches"]
    return total                       # sale: el resultado
```

- **`return` devuelve** el valor para que quien llama a la función pueda usarlo. **`print` solo lo enseña** por pantalla. Las pruebas necesitan el valor, así que siempre `return`.
- **Las pruebas os guían.** `test_kpis.py` llama a vuestras funciones con ejemplos y compara. Al principio fallan todas (es lo normal): vais arreglándolas **una a una** y veis cómo pasan de rojo a verde. Cada fallo dice **qué esperaba y qué recibió**: leedlo antes de tocar nada.
- **Nunca cambiéis `test_kpis.py` para que pase.** Si una prueba falla, lo que está mal es vuestra función.

## 🧰 Antes de tocar el código

1. **Curso «Python desde cero»** *(10 min)*: [funciones](https://www.curso.soultechlabs.io/basico/#func) (ejercicios 1 y 2): `def`, parámetros y `return`.
2. **Taller de bloques** *(10 min)*: [bloque 2](https://www.curso.soultechlabs.io/taller/#t-conteo), «Contar con un diccionario» e «Ingreso medio de las reservas confirmadas». **Son casi vuestras dos funciones**, montadas con piezas.

## 🛠️ Paso a paso

### Parte A · 30 minutos (de los 50)

1. **Abrid [`kpis.py`](../reto_herramientas/kpis.py)** y ejecutad `python test_kpis.py 1`. La fase 1 son **4 pruebas** y empiezan fallando.
2. **Programad una función cada vez**, siguiendo los comentarios «Paso» de su docstring. El ciclo es: ejecutar la prueba → leer qué esperaba y qué recibió → corregir → repetir. Es el método de los profesionales: trabajar **guiados por las pruebas**.

#### 3.1 · `tasa_cancelacion_por_canal` (25 min)

**Recibe y devuelve.** La lista de reservas → un diccionario `{canal: porcentaje}`. Con 3 reservas del canal `web` y 1 cancelada: `{"web": 33.3}`. Sin reservas: `{}`.

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Crear dos diccionarios vacíos: reservas totales por canal y canceladas por canal | `total = {}` y `canceladas = {}` |
| 2 | Recorrer las reservas: sumar 1 al total de su canal y, si `cancelada` vale 1, sumar 1 a las canceladas | `total[c] = total.get(c, 0) + 1` empieza un contador |
| 3 | Por cada canal, calcular el porcentaje con 1 decimal | `round(100 * canceladas[c] / total[c], 1)` |

Se comprueba con `test_tasa_cancelacion…` (incluye el redondeo). **Pista de cuaderno:** [`S04_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_03_estructuras_datos.ipynb) (diccionarios).

### Parte B · 40 minutos (después de la consolidación)

#### 3.2 · `ingreso_medio_por_reserva` (20 min)

**Recibe y devuelve.** La lista de reservas → un número con 2 decimales. Con reservas confirmadas de 2×100 €, 4×50 € y 1×120 €: (200 + 200 + 120) ÷ 3 = **173.33**. Sin ninguna confirmada: `0.0` (sin dividir entre cero).

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Hacer una lista con `noches × precio_noche` **solo** de las reservas no canceladas | Comprensión de lista con `if r["cancelada"] == 0` |
| 2 | Si la lista está vacía, devolver `0.0` | `if not lista:` |
| 3 | Si no, la media con 2 decimales | `round(sum(lista) / len(lista), 2)` |

Se comprueba con `test_ingreso_medio…`. **Pista de cuaderno:** `S04_03` (comprensiones de lista).

#### 3.3 · `ocupacion_proxy` (10 min, con el docente)

**Recibe y devuelve.** La lista de reservas y la capacidad (nº de habitaciones) → un porcentaje con 1 decimal. Ejemplo de la prueba: 7 noches confirmadas, un periodo de 10 días y 5 habitaciones → 7 ÷ (10 × 5) × 100 = **14.0**.

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Si la capacidad es ≤ 0, dar un error (no se puede dividir entre cero) | `raise ValueError("La capacidad debe ser mayor que 0")` |
| 2 | Si no hay reservas, devolver `0.0` | `if not reservas:` |
| 3 | Calcular los días del periodo: de la primera a la última llegada, **contando también el primer día** | `(max(fechas) - min(fechas)).days + 1` |
| 4 | Sumar las noches de las reservas **no canceladas** | `sum(...)` sobre una comprensión con `if` |
| 5 | Aplicar la fórmula con 1 decimal | `round(100 * noches / (dias * capacidad), 1)` |

Se comprueba con `test_ocupacion_proxy`. El docente la hace en pantalla; vosotros **la copiáis y la explicáis con vuestras palabras**. Recordad que es un **proxy** (una medida aproximada, porque el fichero no trae la capacidad real del hotel): se explica en el README.

## 👀 Qué deberíais ver

Al terminar la misión, `python test_kpis.py 1` termina con **`4 de 4 pruebas superadas`**.

## ✅ Hecho cuando

Pasan las cuatro pruebas de la fase 1. Si `ocupacion_proxy` la ha hecho el docente, la habéis **copiado y explicado** con vuestras palabras.

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| La prueba dice que la función devuelve `None` | Imprime con `print` pero no termina con `return` | Terminar con `return valor`: devolver no es lo mismo que mostrar |
| `ModuleNotFoundError: kpis` (o `reservas_demo`) | Se ejecuta desde otra carpeta | Abrir la terminal **dentro** de la carpeta del reto |
| La media sale rara | Se incluyen reservas canceladas en el ingreso | **Solo las no canceladas** |
| `ZeroDivisionError` | Se divide entre 0 cuando no hay reservas | Comprobar primero si la lista está vacía |
| Queréis cambiar la prueba para que pase | Prisa | No se toca `test_kpis.py`; leed qué esperaba y qué recibió |

Para probar una función a mano: en `python`, `from reservas_demo import RESERVAS` y llamadla con esa lista. Si seguís sin avanzar, preguntad primero al equipo y luego al docente.

## 🥋 Kata 1 · Una función con `return` — 10 min, **individual**, fin del martes

[Abrir la kata 1](https://www.curso.soultechlabs.io/taller/#kata-1). **Cada persona sola**, sin mirar esta tarjeta ni preguntar al equipo: escribid `noches_confirmadas(reservas)`. Apuntad **cuántas pistas** habéis usado. Si no sale, no pasa nada: se repite mañana por la mañana. Sirve para comprobar que **cada persona** lo ha aprendido, no solo el equipo.

## ➡️ Siguiente

[Misión 4 · Leer el CSV sin que se rompa](tarjeta_4_ficheros.md) (miércoles): pasamos de datos puestos a mano a un fichero de verdad.
