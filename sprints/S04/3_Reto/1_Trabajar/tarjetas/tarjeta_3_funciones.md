# Misión 3 · Funciones que calculan
*Meter los contadores en funciones que devuelven un resultado.*

| | |
|---|---|
| ⏱ **Cuándo** | Martes · 50 min + 40 min (la segunda parte, después de la consolidación) |
| 👥 **Cómo** | Piloto y copiloto (cambiad de papel entre las dos partes) |
| 🧰 **Usáis** | 🌐 el navegador (curso y Taller) · 📄 `kpis.py` (y `test_kpis.py`, que **no se toca**) · 💻 la terminal |
| 🏁 **Al terminar** | `4 de 4 pruebas superadas` con `python test_kpis.py 1` |

**En esta tarjeta:** [Qué lograréis](#-qué-lograréis) · [La idea en un minuto](#-la-idea-en-un-minuto) · [Paso a paso](#-paso-a-paso) · [Misión terminada cuando](#-misión-terminada-cuando) · [Si os atascáis](#-si-os-atascáis) · [Kata 1](#-kata-1--una-función-con-return) · [Siguiente](#-siguiente)

← [Volver al índice de misiones](../README.md)

## 🎯 Qué lograréis

Las **primeras funciones de `kpis.py`**, la herramienta del cliente: `tasa_cancelacion_por_canal` e `ingreso_medio_por_reserva` (y `ocupacion_proxy`, que se hace con el docente). Es lo mismo que contasteis en la misión 2, pero metido en una función que **devuelve** el resultado. Esta vez trabajáis **con pruebas** que os dicen si está bien.

## 💡 La idea en un minuto

**Una función es una máquina: entra algo, sale algo.** Aquí entra la lista de reservas y sale un número (o un diccionario).

```python
def noches_totales(reservas):          # entra: la lista de reservas
    total = 0
    for r in reservas:
        total = total + r["noches"]
    return total                       # sale: el resultado
```

- **`return` devuelve** el valor para quien llama a la función; **`print` solo lo enseña** por pantalla. Las pruebas necesitan el valor: siempre `return`.
- **Las pruebas os guían.** `test_kpis.py` llama a vuestras funciones con ejemplos y compara. Al principio fallan todas (es lo normal): las arregláis **una a una** y pasan de rojo a verde. Cada fallo dice **qué esperaba y qué recibió**: leedlo antes de tocar nada. **Nunca cambiéis `test_kpis.py` para que pase**: si una prueba falla, lo que está mal es vuestra función.

## 👣 Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| **Parte A** | | | | **50** | |
| 1 | 📚 Aprender | Funciones (ejercicios 1 y 2): `def`, parámetros y `return` | Curso: [funciones](https://www.curso.soultechlabs.io/basico/#func) | 10 | Los dos ejercicios en verde |
| 2 | 📚 Aprender | «Contar con un diccionario» e «Ingreso medio de las reservas confirmadas». **Son casi vuestras dos funciones**, montadas con piezas | Taller: [bloque 2](https://www.curso.soultechlabs.io/taller/#t-conteo) | 10 | Los dos puzles montados |
| 3 | ✅ Comprobar | Ver las pruebas en rojo. La fase 1 son **4 pruebas** y empiezan fallando: es lo normal | Terminal: `python test_kpis.py 1` | 5 | Veis «0 de 4» y qué espera cada prueba |
| 4 | 🛠️ Construir | `tasa_cancelacion_por_canal`, siguiendo los comentarios «Paso» de su docstring (ver «Paso 4», abajo) | [`kpis.py`](../reto_herramientas/kpis.py) | 20 | La función está escrita con un `return` |
| 5 | ✅ Comprobar | Ejecutar la prueba, leer qué esperaba y qué recibió, corregir y repetir | Terminal: `python test_kpis.py 1` | 5 | `test_tasa_cancelacion…` en verde |
| **Parte B** | | *(después de la consolidación)* | | **40** | |
| 6 | 🛠️ Construir | `ingreso_medio_por_reserva` (ver «Paso 6», abajo) | `kpis.py` | 17 | La función está escrita con un `return` |
| 7 | ✅ Comprobar | Ejecutar la prueba y corregir | Terminal: `python test_kpis.py 1` | 3 | `test_ingreso_medio…` en verde |
| 8 | 🛠️ Construir | `ocupacion_proxy`: el docente la hace en pantalla; vosotros **la copiáis** (ver «Paso 8», abajo) | `kpis.py` | 10 | Está copiada y cada persona sabe explicar una línea |
| 9 | ✅ Comprobar | Ejecutar todas las pruebas de la fase 1 | Terminal: `python test_kpis.py 1` | 10 | **`4 de 4 pruebas superadas`** |

**El ciclo de los pasos 4 a 7 es siempre el mismo:** escribir una función → ejecutar la prueba → leer qué esperaba y qué recibió → corregir → repetir. Es el método de los profesionales: trabajar **guiados por las pruebas**.

### Paso 4 · `tasa_cancelacion_por_canal`

**Recibe y devuelve.** La lista de reservas → un diccionario `{canal: porcentaje}`. Con 3 reservas del canal `web` y 1 cancelada: `{"web": 33.3}`. Sin reservas: `{}`.

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Crear dos diccionarios vacíos: reservas totales por canal y canceladas por canal | `total = {}` y `canceladas = {}` |
| 2 | Recorrer las reservas: sumar 1 al total de su canal y, si `cancelada` vale 1, sumar 1 a las canceladas | `total[c] = total.get(c, 0) + 1` empieza un contador |
| 3 | Por cada canal, calcular el porcentaje con 1 decimal | `round(100 * canceladas[c] / total[c], 1)` |

Se comprueba con `test_tasa_cancelacion…` (incluye el redondeo). **Pista de cuaderno:** [`S04_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_03_estructuras_datos.ipynb) (diccionarios).

### Paso 6 · `ingreso_medio_por_reserva`

**Recibe y devuelve.** La lista de reservas → un número con 2 decimales. Con reservas confirmadas de 2×100 €, 4×50 € y 1×120 €: (200 + 200 + 120) ÷ 3 = **173.33**. Sin ninguna confirmada: `0.0` (sin dividir entre cero).

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Hacer una lista con `noches × precio_noche` **solo** de las reservas no canceladas | Comprensión de lista con `if r["cancelada"] == 0` |
| 2 | Si la lista está vacía, devolver `0.0` | `if not lista:` |
| 3 | Si no, la media con 2 decimales | `round(sum(lista) / len(lista), 2)` |

Se comprueba con `test_ingreso_medio…`. **Pista de cuaderno:** `S04_03` (comprensiones de lista).

### Paso 8 · `ocupacion_proxy`

**Recibe y devuelve.** La lista de reservas y la capacidad (nº de habitaciones) → un porcentaje con 1 decimal. Ejemplo de la prueba: 7 noches confirmadas, un periodo de 10 días y 5 habitaciones → 7 ÷ (10 × 5) × 100 = **14.0**.

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Si la capacidad es ≤ 0, dar un error (no se puede dividir entre cero) | `raise ValueError("La capacidad debe ser mayor que 0")` |
| 2 | Si no hay reservas, devolver `0.0` | `if not reservas:` |
| 3 | Calcular los días del periodo: de la primera a la última llegada, **contando también el primer día** | `(max(fechas) - min(fechas)).days + 1` |
| 4 | Sumar las noches de las reservas **no canceladas** | `sum(...)` sobre una comprensión con `if` |
| 5 | Aplicar la fórmula con 1 decimal | `round(100 * noches / (dias * capacidad), 1)` |

Se comprueba con `test_ocupacion_proxy`. Vosotros **la copiáis y la explicáis con vuestras palabras**. Recordad que es un **proxy** (una medida aproximada, porque el fichero no trae la capacidad real del hotel): se explica en el README.

## ✅ Misión terminada cuando

- [ ] `python test_kpis.py 1` termina con **`4 de 4 pruebas superadas`**.
- [ ] Si `ocupacion_proxy` la ha hecho el docente, la habéis **copiado y explicado** con vuestras palabras (cada persona sabe explicar una línea).

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| La prueba dice que la función devuelve `None` | Imprime con `print` pero no termina con `return` | Terminar con `return valor`: devolver no es lo mismo que mostrar |
| `ModuleNotFoundError: kpis` (o `reservas_demo`) | Se ejecuta desde otra carpeta | Abrir la terminal **dentro** de la carpeta del reto |
| La media sale rara | Se incluyen reservas canceladas en el ingreso | **Solo las no canceladas** |
| `ZeroDivisionError` | Se divide entre 0 cuando no hay reservas | Comprobar primero si la lista está vacía |
| Queréis cambiar la prueba para que pase | Prisa | No se toca `test_kpis.py`; leed qué esperaba y qué recibió |
| Queréis probar una función a mano | — | En `python`: `from reservas_demo import RESERVAS` y llamadla con esa lista |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 3](../../3_Consultar/Solucionario_misiones.md) (se publica al acabar la clase el miércoles). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |

## 🥋 Kata 1 · Una función con `return`

⏱ 10 min · 👤 **Individual** · fin del martes · [Abrir la kata 1](https://www.curso.soultechlabs.io/taller/#kata-1)

**Cada persona sola**, sin mirar esta tarjeta ni preguntar al equipo: escribid `noches_confirmadas(reservas)`. Apuntad **cuántas pistas** habéis usado. Si no sale, no pasa nada: se repite mañana por la mañana. Sirve para comprobar que **cada persona** lo ha aprendido, no solo el equipo.

## 👉 Siguiente

[Misión 4 · Leer el CSV](tarjeta_4_ficheros.md) (miércoles): pasamos de datos puestos a mano a un fichero de verdad.
