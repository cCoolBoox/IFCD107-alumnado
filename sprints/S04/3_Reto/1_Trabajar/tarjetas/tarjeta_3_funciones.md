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

Tres funciones de `kpis.py` (herramienta del cliente):

- `tasa_cancelacion_por_canal`: qué porcentaje de las reservas se cancela en cada canal.
- `ingreso_medio_por_reserva`: cuánto dinero deja una reserva, de media.
- `ocupacion_proxy`: qué porcentaje de las habitaciones está ocupado (la hace el docente y la copiáis).

Es lo mismo que contasteis en la misión 2, pero guardado en una **función** para poder usarlo cuando queráis. Esta vez trabajáis **con pruebas** que os dicen si está bien.

## 💡 La idea en un minuto

**Una función es una máquina: entra algo, sale algo.** Aquí entra la lista de reservas y sale un número (o un diccionario).

```python
def noches_totales(reservas):          # def = «voy a crear una función»; reservas = lo que entra
    total = 0                          # el marcador empieza en cero
    for r in reservas:                 # coge las reservas una a una
        total = total + r["noches"]    # suma las noches de cada una
    return total                       # return = lo que sale
```

| Palabra | Qué significa |
|---|---|
| **`def`** | «Voy a crear una función», seguida de su nombre y de lo que recibe. |
| **Parámetro** | Lo que entra en la función. Aquí, `reservas`. |
| **`return`** | Lo que **devuelve** la función. Sin `return`, la función no entrega nada. |
| **`print`** | Solo **enseña** algo por la pantalla. Las pruebas necesitan el `return`, no el `print`. |
| **Prueba** | Un programa que llama a vuestra función con un ejemplo y comprueba si sale lo que debe. |
| **Diccionario** | Una lista de parejas «nombre: valor» entre llaves, como `{"web": 33.3}`. |

**Las pruebas os guían.** Al principio fallan todas: es lo normal, todavía no habéis escrito nada. Las arregláis **una a una**. Cada fallo os dice **qué debería salir**; para ver **qué sale en la vuestra**, la probáis a mano (paso 5). **Nunca cambiéis `test_kpis.py` para que pase**: si una prueba falla, lo que está mal es vuestra función.

## 👣 Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| **Parte A** | | | | **50** | |
| 1 | 📚 Aprender | Funciones (ejercicios 1 y 2): `def`, parámetros y `return` | Curso: [funciones](https://www.curso.soultechlabs.io/basico/#func) | 10 | Los dos ejercicios en verde |
| 2 | 📚 Aprender | «Contar con un diccionario» e «Ingreso medio de las reservas confirmadas». **Son casi vuestras dos funciones**, montadas con piezas | Taller: [bloque 2](https://www.curso.soultechlabs.io/taller/#t-conteo) | 10 | Los dos puzles montados |
| 3 | ✅ Comprobar | Ver las pruebas fallar. La fase 1 son **4 pruebas** y empiezan fallando: es lo normal | Terminal: `python test_kpis.py 1` | 5 | Veis «0 de 4» |
| 4 | 🛠️ Construir | `tasa_cancelacion_por_canal` (ver «Paso 4», abajo) | [`kpis.py`](../reto_herramientas/kpis.py) | 20 | La función está escrita con un `return` |
| 5 | ✅ Comprobar | Probarla a mano, ejecutar la prueba y corregir | Terminal: `python test_kpis.py 1` | 5 | `test_tasa_cancelacion…` en verde (2 pruebas) |
| **Parte B** | | *(después de la consolidación)* | | **40** | |
| 6 | 🛠️ Construir | `ingreso_medio_por_reserva` (ver «Paso 6», abajo) | `kpis.py` | 17 | La función está escrita con un `return` |
| 7 | ✅ Comprobar | Probarla a mano, ejecutar la prueba y corregir | Terminal: `python test_kpis.py 1` | 3 | `test_ingreso_medio…` en verde |
| 8 | 🛠️ Construir | `ocupacion_proxy`: el docente la hace en pantalla; vosotros **la copiáis** (ver «Paso 8», abajo) | `kpis.py` | 10 | Está copiada y cada persona sabe explicar una línea |
| 9 | ✅ Comprobar | Ejecutar todas las pruebas de la fase 1 | Terminal: `python test_kpis.py 1` | 10 | **`4 de 4 pruebas superadas`** |

**El ciclo de los pasos 4 a 7 es siempre el mismo:** escribir una función → ejecutar la prueba → leer qué debería salir → corregir → repetir. Es el método de los profesionales: trabajar **guiados por las pruebas**. En el [solucionario](../../3_Consultar/Solucionario_misiones.md) cada paso tiene su apartado con **el mismo número**.

### Paso 3 · Ver las pruebas fallar

Abrid la terminal **dentro de la carpeta del reto** y escribid `python test_kpis.py 1`. Tiene que salir esto, en rojo:

```
--- FASE 1 · funciones que calculan (datos en memoria) ---
[ERROR] test_ingreso_medio_por_reserva: NotImplementedError: TODO (misión 3): ingreso_medio_por_reserva
[ERROR] test_ocupacion_proxy: NotImplementedError: TODO (misión 3): ocupacion_proxy
[ERROR] test_tasa_cancelacion_por_canal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal
[ERROR] test_tasa_cancelacion_se_redondea_a_un_decimal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal

0 de 4 pruebas superadas
```

Es lo normal. `NotImplementedError` significa «esto está **sin hacer**»: es la línea `raise NotImplementedError(...)` que viene en cada función. Hay **4 pruebas para 3 funciones**: la tasa de cancelación tiene dos.

### Paso 4 · `tasa_cancelacion_por_canal`

**Qué hace.** Recibe la lista de reservas y devuelve un diccionario con el porcentaje de canceladas de cada canal. Con 3 reservas de `web` y 1 cancelada: `{"web": 33.3}`. Sin reservas: `{}`.

**Seguid un ejemplo con el dedo.** Cuatro reservas: `web` (no cancelada), `web` (cancelada), `directo` (no cancelada) y `web` (no cancelada). Al terminar el `for`, los dos diccionarios quedan así:

| Diccionario | Contenido | Cómo se llega a él |
|---|---|---|
| `total` | `{"web": 3, "directo": 1}` | cada reserva suma 1 a **su** canal, esté o no cancelada |
| `canceladas` | `{"web": 1}` | solo suma 1 la reserva con `cancelada == 1`; **`directo` no aparece** |

Y el resultado: `web` → 100 × 1 ÷ 3 = **33.3** y `directo` → 100 × 0 ÷ 1 = **0.0**.

**Qué tocáis en `kpis.py`.** Dejad el `def` y el texto entre comillas triples. **Borrad solo la línea `raise NotImplementedError(...)`** y escribid vuestras líneas en su lugar, con 4 espacios al principio. Terminad con `return`.

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Crear dos diccionarios vacíos: las reservas de cada canal y las canceladas de cada canal | `total = {}` y `canceladas = {}` |
| 2 | Recorrer las reservas con un `for`. Cada una suma 1 al total de **su** canal; si `cancelada` vale 1, suma 1 también a las canceladas | `total[canal] = total.get(canal, 0) + 1` |
| 3 | Crear un diccionario vacío y, por cada canal, calcular el porcentaje con 1 decimal | `round(100 * canceladas.get(canal, 0) / total[canal], 1)` |
| 4 | Devolver ese diccionario | `return tasas` |

**La trampa habitual.** `directo` no está en `canceladas`, y `canceladas["directo"]` da `KeyError`. Con `.get(canal, 0)` se pide «lo que lleve ese canal, o `0` si todavía no está».

### Paso 5 · Probar y corregir

1. **Probadla a mano**, con las 8 reservas de ejemplo. En la terminal, dentro de la carpeta del reto:

   ```
   python
   >>> from reservas_demo import RESERVAS
   >>> from kpis import tasa_cancelacion_por_canal
   >>> tasa_cancelacion_por_canal(RESERVAS)
   ```

   Tiene que salir `{'directo': 33.3, 'agencia': 0.0, 'web_intermediaria': 66.7}`. Para salir, `exit()`. Si cambiáis `kpis.py`, salid y volved a entrar.
2. Ejecutad `python test_kpis.py 1`. Las dos pruebas de la tasa tienen que salir `[OK]` en verde.
3. Si falla, leed el mensaje (dice **qué debería salir**), comparadlo con lo que sale a mano y corregid.

### Paso 6 · `ingreso_medio_por_reserva`

**Qué hace.** Recibe la lista de reservas y devuelve **cuánto ingresa de media una reserva**, con 2 decimales. Solo cuentan las **no canceladas**: una reserva cancelada no deja dinero. Con confirmadas de 2 noches a 100 €, 4 noches a 50 € y 1 noche a 120 €: (200 + 200 + 120) ÷ 3 = **173.33**. Sin ninguna confirmada: `0.0`.

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Crear una lista vacía y, con un `for` y un `if`, añadir `noches × precio_noche` de cada reserva **no cancelada** | `ingresos = []` y `ingresos.append(...)`; el `if` mira `r["cancelada"] == 0` |
| 2 | Si la lista está vacía, devolver `0.0` (no se puede dividir entre cero) | `if not ingresos:` |
| 3 | Si no, devolver la suma dividida entre cuántos hay, con 2 decimales | `round(sum(ingresos) / len(ingresos), 2)` |

Es casi el puzle «Ingreso medio de las reservas confirmadas» del Taller. **Pista de cuaderno:** [`S04_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_03_estructuras_datos.ipynb) (listas y bucles `for` con `if`).

### Paso 7 · Probar y corregir

Igual que el paso 5. A mano, con las 8 reservas de ejemplo, tiene que salir **`182.0`** (200 + 200 + 120 + 180 + 210 = 910 €, entre 5 reservas). Después, `python test_kpis.py 1`: `test_ingreso_medio…` en verde.

### Paso 8 · `ocupacion_proxy`

**Qué hace.** Recibe la lista de reservas y el número de habitaciones, y devuelve **qué porcentaje de las habitaciones está ocupado**, con 1 decimal. Ejemplo de la prueba: 7 noches confirmadas, 10 días y 5 habitaciones → 7 ÷ (10 × 5) × 100 = **14.0**.

| Orden | Qué hacéis | Pista de Python |
|---|---|---|
| 1 | Si las habitaciones son 0 o menos, dar un error (no se divide entre cero) | `raise ValueError("La capacidad debe ser mayor que 0")` |
| 2 | Si no hay reservas, devolver `0.0` | `if not reservas:` |
| 3 | Contar los días del periodo, de la primera a la última llegada, **incluido el primer día** | `(max(fechas) - min(fechas)).days + 1` |
| 4 | Sumar las noches de las reservas **no canceladas** | un `for` con `if`, como en el paso 6 |
| 5 | Aplicar la fórmula con 1 decimal | `round(100 * noches / (dias * capacidad), 1)` |

Esta la **hace el docente en pantalla** y vosotros **la copiáis y la explicáis con vuestras palabras**. Es un **proxy** (una medida aproximada, porque el fichero no trae la capacidad real del hotel): se explica en el README.

### Paso 9 · Todas las pruebas

`python test_kpis.py 1` tiene que terminar con **`4 de 4 pruebas superadas`**, en verde. A mano, con las 8 reservas, `ocupacion_proxy(RESERVAS, 5)` da **`12.0`**.

## ✅ Misión terminada cuando

- [ ] `python test_kpis.py 1` termina con **`4 de 4 pruebas superadas`**.
- [ ] Si `ocupacion_proxy` la ha hecho el docente, la habéis **copiado y explicado** con vuestras palabras (cada persona sabe explicar una línea).

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| La prueba dice que la función devuelve `None` | Imprime con `print` pero no termina con `return` | Terminar con `return valor`: devolver no es lo mismo que mostrar |
| `IndentationError` | Las líneas nuevas no tienen los 4 espacios del principio | Dentro de una función, todo va con 4 espacios; dentro de un `for`, con 8 |
| Sigue saliendo `NotImplementedError` | No habéis borrado la línea `raise NotImplementedError(...)` | Borradla: queda **solo vuestro código** |
| `KeyError` | Se pide un canal que todavía no está en el diccionario | Usad `.get(canal, 0)` |
| `ModuleNotFoundError: kpis` (o `reservas_demo`) | Se ejecuta desde otra carpeta | Abrir la terminal **dentro** de la carpeta del reto |
| La media sale rara | Se incluyen reservas canceladas en el ingreso | **Solo las no canceladas** |
| `ZeroDivisionError` | Se divide entre 0 cuando no hay reservas | Comprobar primero si la lista está vacía |
| Queréis cambiar la prueba para que pase | Prisa | No se toca `test_kpis.py`; leed qué debería salir |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 3](../../3_Consultar/Solucionario_misiones.md), que tiene **los mismos pasos que esta tarjeta**. Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |

## 🥋 Kata 1 · Una función con `return`

⏱ 10 min · 👤 **Individual** · fin del martes · [Abrir la kata 1](https://www.curso.soultechlabs.io/taller/#kata-1)

**Cada persona sola**, sin mirar esta tarjeta ni preguntar al equipo: escribid `noches_confirmadas(reservas)`. Apuntad **cuántas pistas** habéis usado. Si no sale, no pasa nada: se repite mañana por la mañana. Sirve para comprobar que **cada persona** lo ha aprendido, no solo el equipo.

## 👉 Siguiente

[Misión 4 · Leer el CSV](tarjeta_4_ficheros.md) (miércoles): pasamos de datos puestos a mano a un fichero de verdad.
