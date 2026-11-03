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

**Qué hace.** Dice, **por cada canal**, qué porcentaje de sus reservas se ha cancelado.

**Primero, a mano y con lápiz.** Estas son 4 reservas. Dibujad en el cuaderno **dos cajas vacías**: `total` (reservas de cada canal) y `canceladas` (canceladas de cada canal).

| Reserva | Canal | ¿Cancelada? |
|---|---|---|
| 1 | web | no |
| 2 | web | **sí** |
| 3 | directo | no |
| 4 | web | no |

Ahora, **una reserva cada vez**. Tapad las de abajo con la mano:

1. **Reserva 1** (web, no): en `total` apuntad `web: 1`.
2. **Reserva 2** (web, **sí**): `total` → `web: 2`. Y en `canceladas` → `web: 1`.
3. **Reserva 3** (directo, no): `total` → `directo: 1`. `canceladas` no cambia.
4. **Reserva 4** (web, no): `total` → `web: 3`. `canceladas` no cambia.

Al final tenéis `total = {web: 3, directo: 1}` y `canceladas = {web: 1}`. Los porcentajes:

- `web`: 1 de 3 → 100 × 1 ÷ 3 = **33.3**
- `directo`: 0 de 1 → 100 × 0 ÷ 1 = **0.0**

**Lo que acabáis de hacer a mano es lo que hace la función.** Ahora, escribidlo en [`kpis.py`](../reto_herramientas/kpis.py). Borrad **solo** la línea `raise NotImplementedError(...)` y escribid con 4 espacios delante. Son los mismos `# Paso 1, 2, 3` que ya ponen los comentarios de la función.

| Paso de `kpis.py` | Lo que hacíais a mano | Pista |
|---|---|---|
| 1 | Dibujar las dos cajas vacías | `total = {}` y `canceladas = {}` |
| 2 | Mirar las reservas **una a una**: sumar 1 a `total`; si está cancelada, sumar 1 a `canceladas` | `for r in reservas:` y `total[canal] = total.get(canal, 0) + 1` |
| 3 | Calcular el porcentaje de cada canal y entregarlo | `round(100 * ... / ..., 1)` y `return` |

**Ojo:** `directo` no está en `canceladas`. Pedirlo con corchetes da `KeyError`. Con `.get(canal, 0)` decís «lo que lleve, o `0` si todavía no está».

### Paso 5 · Probar y corregir

1. Ejecutad `python test_kpis.py 1`.
2. Las dos pruebas de la tasa tienen que salir en verde: **`2 de 4`**.
3. Si falla, leed qué **debería salir** y comparadlo con lo que sale en la vuestra.

Para ver lo que sale en la vuestra, probadla a mano **con una sola línea**. En la terminal, dentro de la carpeta del reto, copiadla **entera** y pulsad Intro:

```
python -c "from reservas_demo import RESERVAS; from kpis import tasa_cancelacion_por_canal; print(tasa_cancelacion_por_canal(RESERVAS))"
```

Tiene que salir `{'directo': 33.3, 'agencia': 0.0, 'web_intermediaria': 66.7}`.

No ejecutéis `python kpis.py` solo: no enseña nada. Se prueba con `python test_kpis.py 1`.

### Paso 6 · `ingreso_medio_por_reserva`

**Qué hace.** Dice **cuánto dinero deja de media una reserva**. Las **canceladas no cuentan**: no dejan dinero.

**Primero, a mano.** Tres reservas **no canceladas**:

| Reserva | Cuenta | Dinero |
|---|---|---|
| 1 | 2 noches × 100 € | 200 € |
| 2 | 4 noches × 50 € | 200 € |
| 3 | 1 noche × 120 € | 120 € |

Se suma todo (520 €) y se divide entre 3 reservas: **173.33**. Y si no hay ninguna reserva, devuelve `0.0`.

Ahora, en `kpis.py`:

| Paso de `kpis.py` | Lo que hacíais a mano | Pista |
|---|---|---|
| 1 | Una lista vacía; por cada reserva **no cancelada**, apuntar su dinero | `ingresos = []`, `if r["cancelada"] == 0:` y `ingresos.append(...)` |
| 2 | Si no hay ninguna, devolver `0.0` | `if not ingresos:` |
| 3 | Sumar todo y dividir entre cuántas hay | `round(sum(ingresos) / len(ingresos), 2)` |

Ayuda: el puzle «Ingreso medio de las reservas confirmadas» del Taller, y el cuaderno [`S04_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_03_estructuras_datos.ipynb).

### Paso 7 · Probar y corregir

`python test_kpis.py 1`: `test_ingreso_medio…` en verde (**`3 de 4`**). A mano, con una línea, tiene que salir **`182.0`**:

```
python -c "from reservas_demo import RESERVAS; from kpis import ingreso_medio_por_reserva; print(ingreso_medio_por_reserva(RESERVAS))"
```

### Paso 8 · `ocupacion_proxy`

**Qué hace.** Dice **qué parte de las habitaciones está ocupada**, en porcentaje. **La hace el docente en pantalla**; vosotros **la copiáis** y **explicáis una línea** con vuestras palabras.

**A mano.** Un hotel con 5 habitaciones, durante 10 días, tiene 10 × 5 = **50** «noches posibles». Si se han ocupado 7 noches: 7 ÷ 50 × 100 = **14.0 %**.

| Paso de `kpis.py` | Qué hace |
|---|---|
| 1 | Si las habitaciones son 0 o menos, da un error (no se puede dividir entre 0) |
| 2 | Si no hay reservas, devuelve `0.0` |
| 3 | Cuenta los días: de la primera a la última llegada, **contando también el primer día** |
| 4 | Suma las noches de las reservas **no canceladas** |
| 5 | Calcula el porcentaje, con 1 decimal |

Es un **proxy**: una medida aproximada, porque el fichero no dice cuántas habitaciones tiene el hotel de verdad.

### Paso 9 · Todas las pruebas

`python test_kpis.py 1` tiene que terminar con **`4 de 4 pruebas superadas`**, en verde. A mano, con una línea, da **`12.0`**:

```
python -c "from reservas_demo import RESERVAS; from kpis import ocupacion_proxy; print(ocupacion_proxy(RESERVAS, 5))"
```

## ✅ Misión terminada cuando

- [ ] `python test_kpis.py 1` termina con **`4 de 4 pruebas superadas`**.
- [ ] Si `ocupacion_proxy` la ha hecho el docente, la habéis **copiado y explicado** con vuestras palabras (cada persona sabe explicar una línea).

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| La prueba dice que la función devuelve `None` | Imprime con `print` pero no termina con `return` | Terminar con `return valor`: devolver no es lo mismo que mostrar |
| `IndentationError` | Las líneas no están bien sangradas, o el fichero no está guardado | Dentro de una función, todo va con 4 espacios; dentro de un `for`, con 8. Si pegáis la solución, pegad la **función entera** (de `def` a `raise`) y guardad con Ctrl+S |
| `ParserError` o `>>>` en la terminal | Habéis pegado líneas que empiezan por `>>>` | Esas líneas son de Python por dentro: usad la línea `python -c "..."` de la tarjeta, que se pega entera |
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
