# Misión 3 · Funciones que calculan

<h2 align="center">Meter los contadores en funciones que devuelven un resultado</h2>

| | |
|---|---|
| ⏱ **Cuándo** | Martes · 50 min + 40 min (la segunda parte, después de la consolidación) |
| 👥 **Cómo** | Piloto y copiloto (cambiad de papel entre las dos partes) |
| 🧰 **Usáis** | 🌐 el navegador (curso y Taller) · 📄 `kpis.py` (y `test_kpis.py`, que **no se toca**) · 💻 la terminal |
| 🏁 **Al terminar** | `4 de 4 pruebas superadas` con `python test_kpis.py 1` |

**Esta tarjeta tiene dos partes:**

- [1 · Guía paso a paso](#1--guía-paso-a-paso): solo lo que hay que hacer.
- [2 · Explicaciones](#2--explicaciones): el porqué de cada cosa, para cuando lo necesitéis.
- Si queréis, seguid solo la parte 1.

← [Volver al índice de misiones](../README.md)

---

# 1 · Guía paso a paso

**Qué vais a hacer:** tres funciones de [`kpis.py`](../reto_herramientas/kpis.py).

- `tasa_cancelacion_por_canal`: qué porcentaje de las reservas se cancela en cada canal.
- `ingreso_medio_por_reserva`: cuánto dinero deja una reserva, de media.
- `ocupacion_proxy`: qué porcentaje de las habitaciones está ocupado (la hace el docente y la copiáis).

**Cómo se sigue**

- De arriba abajo, **un número cada vez**.
- Cada paso termina en ✅: lo que tiene que salir.
- Si no sale, no sigáis: mirad la parte 2.
- Cada función se hace **primero a mano, con lápiz**, y después en `kpis.py`.

**Cuatro reglas que evitan perderse**

1. **Los espacios del principio (la sangría)**
   - Un **nivel** son 4 espacios, o una pulsación de **Tab**.
   - Una línea que acaba en `:` abre un nivel nuevo: la siguiente va **un nivel más a la derecha**.
   - Si una línea queda de más a la derecha: **Shift+Tab**. De menos: **Tab**.
2. **Guardar antes de probar**
   - Pulsad **Ctrl+S**.
   - Mirad que la pestaña de `kpis.py` **no tenga un punto ●** junto al nombre.
   - Python lee el fichero **guardado**, no el que veis en pantalla.
3. **No pulséis el botón ▶ (Run) de VS Code**
   - Ejecuta `kpis.py` sin datos y no enseña nada.
   - Probad **solo** con `python test_kpis.py 1` y con las líneas `python -c "..."` de la tarjeta.
4. **No se toca `test_kpis.py`**
   - Si una prueba falla, lo que está mal es **vuestra función**.

## Parte A · Aprender y empezar (50 min)

| Paso | Qué hacéis | Min | ✅ Terminado cuando |
|---|---|---|---|
| **1** | Curso: [funciones](https://www.curso.soultechlabs.io/basico/#func), ejercicios 1 y 2 | 10 | Los dos en verde |
| **2** | Taller, [bloque 2](https://www.curso.soultechlabs.io/taller/#t-conteo): «Contar con un diccionario» e «Ingreso medio de las reservas confirmadas». **Son casi vuestras dos funciones**, montadas con piezas | 10 | Los dos puzles montados |
| **3** | Ver las pruebas fallar (abajo) | 5 | Veis «0 de 4» |
| **4** | `tasa_cancelacion_por_canal` (abajo) | 20 | Función escrita con su `return` |
| **5** | Probarla (abajo) | 5 | `2 de 4` |

### Paso 3 · Ver las pruebas fallar

| # | Qué hacéis |
|---|---|
| **3.1** | Abrid una terminal **dentro de la carpeta del reto**. |
| **3.2** | Escribid: `python test_kpis.py 1` |

✅ Tiene que salir esto, en rojo:

```
--- FASE 1 · funciones que calculan (datos en memoria) ---
[ERROR] test_ingreso_medio_por_reserva: NotImplementedError: TODO (misión 3): ingreso_medio_por_reserva
[ERROR] test_ocupacion_proxy: NotImplementedError: TODO (misión 3): ocupacion_proxy
[ERROR] test_tasa_cancelacion_por_canal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal
[ERROR] test_tasa_cancelacion_se_redondea_a_un_decimal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal

0 de 4 pruebas superadas
```

- Es lo normal: todavía no hay nada escrito.
- `NotImplementedError` significa «esto está **sin hacer**».

### Paso 4 · `tasa_cancelacion_por_canal` (20 min)

**Primero, a mano y con lápiz.** Tenéis estas **4 reservas**:

| Reserva | Canal | ¿Cancelada? |
|---|---|---|
| 1 | web | no |
| 2 | web | **sí** |
| 3 | directo | no |
| 4 | web | no |

| # | Qué hacéis |
|---|---|
| **4.1** | En el cuaderno, dibujad **dos cajas vacías**: `total` (reservas de cada canal) y `canceladas` (canceladas de cada canal). |
| **4.2** | **Tapad con una hoja** las reservas de abajo. Id destapándolas **una cada vez**: cada una es una vuelta del `for` de `kpis.py`. |
| **4.3** | **Reserva 1** (web, no): en `total` apuntad `web: 1`. |
| **4.4** | **Reserva 2** (web, **sí**): `total` → `web: 2`. Y en `canceladas` → `web: 1`. |
| **4.5** | **Reserva 3** (directo, no): `total` → `directo: 1`. `canceladas` no cambia. |
| **4.6** | **Reserva 4** (web, no): `total` → `web: 3`. `canceladas` no cambia. |

✅ Tenéis `total = {web: 3, directo: 1}` y `canceladas = {web: 1}`.

| # | Qué hacéis |
|---|---|
| **4.7** | Calculad el porcentaje de cada canal: canceladas ÷ total × 100. |

✅ `web`: 1 de 3 → 100 × 1 ÷ 3 = **33.3**. `directo`: 0 de 1 → 100 × 0 ÷ 1 = **0.0**.

**Lo que acabáis de hacer a mano es lo que hace la función.** Ahora, en `kpis.py`:

| # | Qué hacéis |
|---|---|
| **4.8** | Abrid `kpis.py` y buscad `def tasa_cancelacion_por_canal`. |
| **4.9** | Borrad **solo** la línea `raise NotImplementedError(...)` de esa función. Dejad los comentarios `# Paso 1, 2, 3`: son vuestra guía. |
| **4.10** | **Paso 1 de la función (las dos cajas).** Escribid, **un nivel** a la derecha de `def`: `total = {}` y debajo `canceladas = {}`. |
| **4.11** | **Paso 2 (una reserva cada vez).** Escribid las 5 líneas de la tabla 4.11, de arriba abajo. |
| **4.12** | **Paso 3 (los porcentajes).** Escribid las 4 líneas de la tabla 4.12, de arriba abajo. |
| **4.13** | Guardad con **Ctrl+S**. |

**Tabla 4.11 · el Paso 2**

| Línea | Nivel | Pista |
|---|---|---|
| El `for` que recorre las reservas | 1 | `for r in reservas:` |
| Anotar el canal de la reserva | 2 | `canal = r["canal"]` |
| Sumar 1 a `total` de ese canal | 2 | `total[canal] = total.get(canal, 0) + 1` |
| Solo si está cancelada… | 2 | `if r["cancelada"] == 1:` |
| …sumar 1 a `canceladas` de ese canal | **3** | igual que la de `total`, pero con `canceladas` |

**Tabla 4.12 · el Paso 3**

| Línea | Nivel | Pista |
|---|---|---|
| Una tercera caja vacía, `tasas` | 1 | `tasas = {}` |
| Recorrer los canales de `total` | 1 | `for canal in total:` |
| Guardar el porcentaje de ese canal | 2 | `tasas[canal] = round(100 * ... / ..., 1)` |
| Entregar el resultado | 1 | `return tasas` |

- Nivel 1 = 4 espacios (a la derecha de `def`). Nivel 2 = 8. Nivel 3 = 12.
- `directo` no está en `canceladas`: pedirlo con corchetes da `KeyError`. Con `.get(canal, 0)` se dice «lo que lleve, o `0` si todavía no está».

### Paso 5 · Probar la tasa (5 min)

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **5.1** | En la terminal, dentro de la carpeta del reto, copiad **entera** esta línea y pulsad Intro (abajo) | `{'directo': 33.3, 'agencia': 0.0, 'web_intermediaria': 66.7}` |
| **5.2** | Escribid: `python test_kpis.py 1` | Las dos pruebas de la tasa en verde: **`2 de 4`** |
| **5.3** | Si falla, leed qué **debería salir** y comparadlo con lo que sale en la vuestra. | — |

```
python -c "from reservas_demo import RESERVAS; from kpis import tasa_cancelacion_por_canal; print(tasa_cancelacion_por_canal(RESERVAS))"
```

## Parte B · Dos funciones más (40 min)

*Después de la consolidación. Cambiad de papel: quien era piloto, ahora es copiloto.*

| Paso | Qué hacéis | Min | ✅ Terminado cuando |
|---|---|---|---|
| **6** | `ingreso_medio_por_reserva` (abajo) | 17 | Función escrita con su `return` |
| **7** | Probarla (abajo) | 3 | `3 de 4` |
| **8** | `ocupacion_proxy`: la hace el docente; vosotros **la copiáis** | 10 | Copiada, y cada persona explica una línea |
| **9** | Todas las pruebas de la fase 1 | 10 | **`4 de 4 pruebas superadas`** |

### Paso 6 · `ingreso_medio_por_reserva` (17 min)

**Primero, a mano.** Tenéis 3 reservas **no canceladas**:

| Reserva | Cuenta | Dinero |
|---|---|---|
| 1 | 2 noches × 100 € | 200 € |
| 2 | 4 noches × 50 € | 200 € |
| 3 | 1 noche × 120 € | 120 € |

| # | Qué hacéis |
|---|---|
| **6.1** | Sumad el dinero de las tres. |
| **6.2** | Dividid entre cuántas reservas son. |

✅ 200 + 200 + 120 = **520 €**. 520 ÷ 3 = **173.33**.

- Las **canceladas no cuentan**: no dejan dinero.
- Si no hay **ninguna** reserva confirmada, la función devuelve `0.0`.

Ahora, en `kpis.py`:

| # | Qué hacéis |
|---|---|
| **6.3** | Buscad `def ingreso_medio_por_reserva` y borrad **solo** su línea `raise NotImplementedError(...)`. |
| **6.4** | **Paso 1 (la lista).** Escribid las 4 líneas de la tabla 6.4, de arriba abajo. |
| **6.5** | **Paso 2 (si no hay ninguna).** Escribid las 2 líneas de la tabla 6.5. |
| **6.6** | **Paso 3 (la media).** Escribid la línea de la tabla 6.6. |
| **6.7** | Guardad con **Ctrl+S**. |

**Tabla 6.4 · el Paso 1**

| Línea | Nivel | Pista |
|---|---|---|
| Una lista vacía | 1 | `ingresos = []` |
| Recorrer las reservas | 1 | `for r in reservas:` |
| Solo si **no** está cancelada… | 2 | `if r["cancelada"] == 0:` |
| …meter su dinero (noches por precio) en la lista | **3** | `ingresos.append(...)` |

**Tabla 6.5 · el Paso 2**

| Línea | Nivel | Pista |
|---|---|---|
| Si la lista está vacía… | 1 | `if not ingresos:` |
| …entregar `0.0` | **2** | `return 0.0` |

**Tabla 6.6 · el Paso 3**

| Línea | Nivel | Pista |
|---|---|---|
| Entregar la media con 2 decimales | 1 | `return round(sum(ingresos) / len(ingresos), 2)` |

Ayuda: el puzle «Ingreso medio de las reservas confirmadas» del Taller y el cuaderno [`S04_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_03_estructuras_datos.ipynb).

### Paso 7 · Probar el ingreso medio (3 min)

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **7.1** | En la terminal, copiad **entera** esta línea y pulsad Intro (abajo) | **`182.0`** |
| **7.2** | Escribid: `python test_kpis.py 1` | `test_ingreso_medio…` en verde: **`3 de 4`** |

```
python -c "from reservas_demo import RESERVAS; from kpis import ingreso_medio_por_reserva; print(ingreso_medio_por_reserva(RESERVAS))"
```

### Paso 8 · `ocupacion_proxy` (10 min)

*La hace el docente en pantalla; vosotros la copiáis y explicáis una línea con vuestras palabras.*

| # | Qué hacéis |
|---|---|
| **8.1** | **A mano.** Un hotel con 5 habitaciones, durante 10 días, tiene 10 × 5 = **50** «noches posibles». Si se han ocupado 7 noches: 7 ÷ 50 × 100. |
| **8.2** | Mirad cómo el docente escribe la función, **línea a línea**. |
| **8.3** | Buscad `def ocupacion_proxy` en `kpis.py`, borrad **solo** su `raise NotImplementedError(...)` y copiad lo que ha escrito el docente. |
| **8.4** | Guardad con **Ctrl+S**. |
| **8.5** | Cada persona elige **una línea** y se la explica a su pareja con sus palabras. |

✅ 7 ÷ 50 × 100 = **14.0 %**. La función está copiada y cada persona sabe explicar una línea.

### Paso 9 · Todas las pruebas (10 min)

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **9.1** | En la terminal: `python test_kpis.py 1` | **`4 de 4 pruebas superadas`**, en verde |
| **9.2** | Copiad **entera** esta línea y pulsad Intro (abajo) | **`12.0`** |

```
python -c "from reservas_demo import RESERVAS; from kpis import ocupacion_proxy; print(ocupacion_proxy(RESERVAS, 5))"
```

## ✅ Misión terminada cuando

- [ ] `python test_kpis.py 1` termina con **`4 de 4 pruebas superadas`**.
- [ ] Habéis **copiado y explicado** `ocupacion_proxy`: cada persona sabe explicar una línea.

## 🥋 Kata 1 · Una función con `return`

⏱ 10 min · 👤 **Individual** · fin del martes · [Abrir la kata 1](https://www.curso.soultechlabs.io/taller/#kata-1)

- **Cada persona sola**, sin mirar esta tarjeta ni preguntar al equipo.
- Escribid `noches_confirmadas(reservas)`.
- Apuntad **cuántas pistas** habéis usado.
- Si no sale, no pasa nada: se repite mañana por la mañana.

## 👉 Siguiente

[Misión 4 · Leer el CSV](tarjeta_4_ficheros.md) (miércoles): pasamos de datos puestos a mano a un fichero de verdad.

---

# 2 · Explicaciones

*Para cuando una cosa no sale o queréis entender por qué se hace así. No hace falta leerlo para resolver la misión.*

## La idea: una función es una máquina

- Entra algo, sale algo.
- Aquí entra la lista de reservas y sale un número (o un diccionario).
- Es lo mismo que contasteis en la misión 2, pero guardado en una **función** para usarlo cuando queráis.

```python
def noches_totales(reservas):          # def = «voy a crear una función»; reservas = lo que entra
    total = 0                          # el marcador empieza en cero
    for r in reservas:                 # coge las reservas una a una
        total = total + r["noches"]    # suma las noches de cada una
    return total                       # return = lo que sale
```

## Las palabras de la misión

| Palabra | Qué significa |
|---|---|
| **`def`** | «Voy a crear una función», seguida de su nombre y de lo que recibe |
| **Parámetro** | Lo que entra en la función. Aquí, `reservas` |
| **`return`** | Lo que **devuelve** la función. Sin `return`, la función no entrega nada |
| **`print`** | Solo **enseña** algo por la pantalla. Las pruebas necesitan el `return`, no el `print` |
| **Prueba** | Un programa que llama a vuestra función con un ejemplo y comprueba si sale lo que debe |
| **Diccionario** | Una lista de parejas «nombre: valor» entre llaves, como `{"web": 33.3}` |
| **`.get(canal, 0)`** | «Lo que lleve ese canal, o `0` si todavía no está» |

## Las pruebas os guían

- Al principio fallan todas: es lo normal.
- Se arreglan **una a una**.
- Cada fallo os dice **qué debería salir**; para ver **qué sale en la vuestra**, la probáis a mano con la línea `python -c "..."`.
- **Nunca cambiéis `test_kpis.py` para que pase.**
- El ciclo de los pasos 4 a 7 es siempre el mismo: escribir una función → ejecutar la prueba → leer qué debería salir → corregir → repetir.
- Es el método de los profesionales: trabajar **guiados por las pruebas**.

## Por qué se hace así

- **A mano primero:** si sabéis hacerlo con lápiz, escribirlo en Python es traducirlo.
- **`canceladas.get(canal, 0)`** y no `canceladas[canal]`: `directo` no tiene ninguna cancelada, así que **no está** en `canceladas`. Con corchetes da `KeyError`.
- **`round(..., 1)`:** da `33.3` en lugar de `33.333333333333336`.
- **`if not ingresos`:** sin reservas confirmadas no se puede dividir entre 0; se devuelve `0.0`.
- **Las canceladas no cuentan para el ingreso:** no dejan dinero. Sí cuentan para la tasa de cancelación.
- **`return` y no `print`:** las pruebas leen lo que la función devuelve, no lo que enseña.

## `ocupacion_proxy`, paso a paso (la hace el docente)

| Paso de `kpis.py` | Qué hace |
|---|---|
| 1 | Si las habitaciones son 0 o menos, da un error (no se puede dividir entre 0) |
| 2 | Si no hay reservas, devuelve `0.0` |
| 3 | Cuenta los días: de la primera a la última llegada, **contando también el primer día** |
| 4 | Suma las noches de las reservas **no canceladas** |
| 5 | Calcula el porcentaje, con 1 decimal |

- Es un **proxy**: una medida aproximada, porque el fichero no dice cuántas habitaciones tiene el hotel de verdad.

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| La prueba dice que la función devuelve `None` | Imprime con `print` pero no termina con `return` | Terminad con `return valor`: devolver no es lo mismo que mostrar |
| `IndentationError` | Las líneas no están bien sangradas, o el fichero no está guardado | Dentro de una función, todo va con 4 espacios; dentro de un `for`, con 8. Si pegáis la solución, pegad la **función entera** (de `def` a `raise`) y guardad con Ctrl+S |
| `ParserError` o `>>>` en la terminal | Habéis pegado líneas que empiezan por `>>>` | Esas líneas son de Python por dentro: usad la línea `python -c "..."` de la tarjeta, que se pega entera |
| Sigue saliendo `NotImplementedError` | No habéis borrado la línea `raise NotImplementedError(...)` o el fichero no está guardado | Borradla (queda **solo vuestro código**) y guardad con Ctrl+S |
| `KeyError` | Se pide un canal que todavía no está en el diccionario | Usad `.get(canal, 0)` |
| `ModuleNotFoundError: kpis` (o `reservas_demo`) | Se ejecuta desde otra carpeta | Abrid la terminal **dentro** de la carpeta del reto |
| La media sale rara | Se incluyen reservas canceladas en el ingreso | **Solo las no canceladas** |
| `ZeroDivisionError` | Se divide entre 0 cuando no hay reservas | Comprobad primero si la lista está vacía |
| Queréis cambiar la prueba para que pase | Prisa | No se toca `test_kpis.py`; leed qué debería salir |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 3](../../3_Consultar/Solucionario_misiones.md), que tiene **los mismos pasos que esta tarjeta**. Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |
