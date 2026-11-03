# Solucionario de las misiones · Sprint 4 · «Herramientas internas»

> **Para contrastar vuestro trabajo**, cuando hayáis terminado una misión o agotado las pistas de su tarjeta. No es para copiar: **las pruebas mandan** y el docente puede preguntaros por cualquier línea. Volver al [índice de las misiones](../1_Trabajar/README.md).

## Índice

- [Cómo usarlo](#cómo-usarlo): primero intentarlo, después contrastar
- [Misión 0 · Mirar la demo](#misión-0--mirar-la-demo): qué sale y las respuestas a las cinco preguntas
- [Misión 1 · Datos en memoria](#misión-1--datos-en-memoria): las seis líneas, la salida y los fallos más comunes
- [Misión 2 · Decidir y repetir](#misión-2--decidir-y-repetir): los cuatro bucles, la salida y los fallos más comunes
- [Misión 3 · Funciones que calculan](#misión-3--funciones-que-calculan): los mismos pasos que la tarjeta, con el código en trozos y cada línea explicada
- [Misión 4 · Leer el CSV](#misión-4--leer-el-csv): un CSV pequeño resuelto a mano y fallos reconocibles
- [Misión 5 · Guardar y entregar](#misión-5--guardar-y-entregar): una comprobación cruzada de cifras y fallos reconocibles
- [Mensajes de error: qué significan](#mensajes-de-error-qué-significan): los errores más comunes de Python en el reto y cómo se arreglan

## Cómo usarlo

**Primero intentadlo.** Cuando algo no sale, seguid siempre este orden:

| Escalón | Qué hacéis |
|---|---|
| 1 | Leed el mensaje de la prueba: dice **qué debería salir**; comparadlo con lo que sale en la vuestra |
| 2 | Repasad la tarjeta de la misión (su «Si os atascáis») y la lección del curso |
| 3 | Preguntad al equipo |
| 4 | Preguntad al docente |
| 5 | **Este solucionario**, para contrastar o desbloquearos |

**Después de mirarlo, cerradlo y volved a escribirlo sin mirar.** Copiar una línea no es saberla: la prueba de que la sabéis es poder explicársela a vuestra pareja con vuestras palabras. Cada misión termina con una pregunta para eso.

**Qué hay y qué no hay.** En las misiones 0 a 3 está la solución con el código **explicado línea a línea**: es la parte de práctica y la primera mitad de `kpis.py` (las funciones que calculan). En las misiones 4 y 5, que completan `kpis.py` (leer el CSV, guardar y entregar), **no hay código**: hay cifras para comprobar a mano, los fallos más comunes reconocibles por el número que sale y una pregunta para explicar. Los cuadernos `S04_03` y `S04_04` traen, además, celdas plegadas 🆘 «Solución de referencia» con la solución de **sus propios ejercicios**. Si usáis un asistente de IA, seguid las reglas de uso de la IA de la [ficha del reto](Reto_Sprint_04.md) y declarad el uso en el README.

**Cuándo se publica cada parte.** Las misiones 0 a 2 y los mensajes de error, al acabar la clase del martes; las misiones 3 a 5, al acabar la del miércoles.

## Misión 0 · Mirar la demo

Tarjeta: [Misión 0](../1_Trabajar/tarjetas/tarjeta_0_mirar_la_demo.md).

**Qué tiene que salir** al ejecutar `python demo_cliente.py`:

```
=== Resumen semanal de reservas ===
Reservas analizadas: 8
Canceladas: 3 (37.5 %)
Ingreso medio por reserva confirmada: 182.00 €
  - directo: 3 reservas
  - agencia: 2 reservas
  - web_intermediaria: 3 reservas
```

| Pregunta de la tarjeta | Respuesta |
|---|---|
| 1. ¿Cuántas reservas analiza el programa y qué línea lo calcula? | **8**, con `total = len(RESERVAS)` |
| 2. ¿Por qué `canceladas` empieza en `0` y `por_canal` en `{}`? | Son **acumuladores**: se empieza en `0` y en `{}` porque todavía no se ha contado nada; el bucle los va rellenando |
| 3. Si la primera reserva pasara a estar cancelada (`"cancelada": 1`), ¿qué cifras cambian? | Las canceladas pasan de 3 a **4 (50.0 %)** y el ingreso medio, de 182.00 a **177.50 €** (se quitan los 200 € de esa reserva y quedan 4 confirmadas). El reparto por canal **no cambia**: cuenta todas las reservas, canceladas o no |
| 4. ¿Qué hace `:.1f` dentro de las llaves del f-string? | Muestra el número con **un decimal** (`:.2f`, con dos) |
| 5. Si `RESERVAS` estuviera vacía, ¿qué error saldría y en qué línea? | **`ZeroDivisionError: float division by zero`** en `media = ingreso_total / confirmadas` (línea 34): hay 0 confirmadas. Es el primer error que el programa debería evitar; lo retomáis en la misión 4 |

**Para explicárselo a vuestra pareja:** ¿qué hace el `for` de la demo, línea a línea, y por qué dentro hay un `if` con su `else`?

## Misión 1 · Datos en memoria

Tarjeta: [Misión 1](../1_Trabajar/tarjetas/tarjeta_1_datos.md). Fichero: [`mision_1_datos.py`](../1_Trabajar/reto_herramientas/mision_1_datos.py). En cada apartado se sustituye el `None` o se escribe la línea que falta.

| Apartado | Qué se escribe | Fallo habitual |
|---|---|---|
| 1.1 | `cantidad = len(reservas)` (vale **3**: se cuenta antes de añadir la reserva del 1.5) | `len(reservas[0])` da 4: son las claves de la primera reserva, no cuántas reservas hay |
| 1.2 | `canal_primera = reservas[0]["canal"]` (`'directo'`) | `reservas["canal"]` → `TypeError: list indices must be integers or slices, not str`: falta el número de la reserva |
| 1.3 | `precio_ultima = reservas[-1]["precio_noche"]` (`60.0`) | `reservas[3]` → `IndexError: list index out of range`: solo hay 3 reservas (índices 0 a 2) |
| 1.4 | `reservas[0]["cancelada"] = 1` | `==` en vez de `=`: no da error y no cambia nada, y la comprobación 1.4 falla |
| 1.5 | `reservas.append({"canal": "directo", "noches": 3, "precio_noche": 80.0, "cancelada": 0})` | Olvidar una clave o cambiarle el nombre (`precio` en lugar de `precio_noche`): el diccionario no coincide y falla la 1.5 |
| 1.6 | `texto = f"La reserva 2 es del canal {reservas[1]['canal']}: {reservas[1]['noches']} noches a {reservas[1]['precio_noche']} euros"` | Olvidar la `f` (sale el texto con las llaves) o usar comillas dobles dentro de un f-string de comillas dobles: `SyntaxError` en Python 3.11 |

**Qué tiene que salir:**

```
Cantidad al empezar: 3
Canal de la primera: directo
Precio de la última: 60.0
Ahora hay 4 reservas
La reserva 2 es del canal agencia: 4 noches a 50.0 euros

✅ ¡Misión 1 superada! Ya sabes leer y modificar los datos del reto.
```

**Para explicárselo a vuestra pareja:** ¿por qué `cantidad` vale 3 si al terminar la misión hay 4 reservas?

## Misión 2 · Decidir y repetir

Tarjeta: [Misión 2](../1_Trabajar/tarjetas/tarjeta_2_decidir.md). Fichero: [`mision_2_decidir.py`](../1_Trabajar/reto_herramientas/mision_2_decidir.py), con las 8 reservas de [`reservas_demo.py`](../1_Trabajar/reto_herramientas/reservas_demo.py). Las variables (`canceladas = 0`, `noches_confirmadas = 0`, `por_canal = {}`, `largas = []`) ya vienen escritas; en cada apartado se sustituye el `TODO` por el bucle.

```python
# 2.1  Reservas canceladas
for r in RESERVAS:
    if r["cancelada"] == 1:
        canceladas += 1

# 2.2  Noches de las reservas NO canceladas
for r in RESERVAS:
    if r["cancelada"] == 0:
        noches_confirmadas += r["noches"]

# 2.3  Reservas por canal
for r in RESERVAS:
    por_canal[r["canal"]] = por_canal.get(r["canal"], 0) + 1

# 2.4  Canal de las confirmadas de 3 noches o más
for r in RESERVAS:
    if r["cancelada"] == 0 and r["noches"] >= 3:
        largas.append(r["canal"])
```

| Apartado | Valor esperado | Fallo habitual |
|---|---|---|
| 2.1 | `canceladas == 3` | `canceladas = 1` en lugar de `+= 1` (se queda en 1), o el `+= 1` fuera del `if` (cuenta las 8) |
| 2.2 | `noches_confirmadas == 12` | Comparar con `== 1` (suma 10 noches: las de las canceladas) o no poner el `if` (suma las 22) |
| 2.3 | `{'directo': 3, 'agencia': 2, 'web_intermediaria': 3}` | `por_canal[canal] += 1` sin `get` → `KeyError: 'directo'`: el canal todavía no está en el diccionario |
| 2.4 | `['agencia', 'directo']` | `>` en lugar de `>=` (sale solo `['agencia']`), o `or` en lugar de `and` (salen 7 canales en vez de 2) |

**Qué tiene que salir:**

```
Canceladas: 3
Noches confirmadas: 12
Por canal: {'directo': 3, 'agencia': 2, 'web_intermediaria': 3}
Confirmadas de 3 noches o más: ['agencia', 'directo']

✅ ¡Misión 2 superada! Ya sabes contar con if y for: es la base de los KPI.
```

**Para explicárselo a vuestra pareja:** en el 2.3, ¿qué pasa si quitáis el `.get(..., 0)` y escribís solo `por_canal[canal] += 1`? ¿Por qué?

## Misión 3 · Funciones que calculan

Tarjeta: [Misión 3](../1_Trabajar/tarjetas/tarjeta_3_funciones.md). **Tiene los mismos pasos que este apartado, con los mismos números**: leed el paso en la tarjeta, intentadlo y, si no sale, venid al mismo paso de aquí. Las funciones se escriben en [`kpis.py`](../1_Trabajar/reto_herramientas/kpis.py) y los datos de ejemplo están en [`reservas_demo.py`](../1_Trabajar/reto_herramientas/reservas_demo.py).

**Cómo leer el código de aquí:** cada trozo va seguido de una tabla que explica **cada línea con palabras normales**. Si una línea no la entendéis, no la copiéis: preguntad.

### Pasos 1 y 2 · Aprender

No hay nada que escribir aquí. Son los ejercicios del curso y del Taller (funciones, `def`, `return`, diccionarios). Si el paso 4 os parece un salto, **volved al puzle «Contar con un diccionario» del Taller**: es casi la misma función.

### Paso 3 · Ver las pruebas fallar

Con la plantilla sin tocar, `python test_kpis.py 1` tiene que enseñar, en rojo:

```
--- FASE 1 · funciones que calculan (datos en memoria) ---
[ERROR] test_ingreso_medio_por_reserva: NotImplementedError: TODO (misión 3): ingreso_medio_por_reserva
[ERROR] test_ocupacion_proxy: NotImplementedError: TODO (misión 3): ocupacion_proxy
[ERROR] test_tasa_cancelacion_por_canal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal
[ERROR] test_tasa_cancelacion_se_redondea_a_un_decimal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal

0 de 4 pruebas superadas
```

Si lo veis así, **todo va bien**: las funciones todavía no están hechas. Si no sale `0 de 4`, mirad si habéis escrito el `1` al final (`python test_kpis.py 1`) y si la terminal está dentro de la carpeta del reto.

### Paso 4 · `tasa_cancelacion_por_canal`

**Ojo con los números:** el «Paso 4» es el de la tarjeta (de los 9); los `# Paso 1, 2, 3` son los comentarios de dentro de la función en `kpis.py`.

**La idea.** Hay que contar dos cosas por cada canal: cuántas reservas hay y cuántas están canceladas. Después, dividir.

**Cómo copiarla sin errores de sangría.** En `kpis.py`, seleccionad la función entera, **desde la línea `def …` hasta la línea `raise NotImplementedError(...)` (incluida)**, y pegad encima. Así no se mezclan los espacios. (Si pegáis solo las líneas de dentro y el cursor ya tenía 4 espacios, la primera línea queda con 8 y sale `IndentationError: unexpected indent`.)

```python
def tasa_cancelacion_por_canal(reservas):
    """Devuelve {canal: porcentaje de reservas canceladas, con 1 decimal}."""
    total = {}
    canceladas = {}
    for r in reservas:
        canal = r["canal"]
        total[canal] = total.get(canal, 0) + 1
        if r["cancelada"] == 1:
            canceladas[canal] = canceladas.get(canal, 0) + 1
    tasas = {}
    for canal in total:
        tasas[canal] = round(100 * canceladas.get(canal, 0) / total[canal], 1)
    return tasas
```

**Primera parte · preparar y contar** (pasos 1 y 2 de los comentarios de `kpis.py`):

| Línea | Qué hace, con palabras normales |
|---|---|
| `total = {}` | Una libreta vacía donde apuntar **cuántas reservas** tiene cada canal |
| `canceladas = {}` | Otra libreta vacía para **cuántas canceladas** tiene cada canal |
| `for r in reservas:` | Coge las reservas **una a una**; en cada vuelta, `r` es la reserva de turno |
| `canal = r["canal"]` | Anota el canal de esa reserva (`"web"`, `"directo"`…) para no escribirlo cada vez |
| `total[canal] = total.get(canal, 0) + 1` | «Mira lo que lleva ese canal en `total` (si todavía no está, cuenta `0`), **suma 1** y apúntalo» |
| `if r["cancelada"] == 1:` | Solo si esta reserva está cancelada, haz lo de abajo |
| `canceladas[canal] = canceladas.get(canal, 0) + 1` | Lo mismo que con `total`, pero en la libreta de canceladas |

**Segunda parte · calcular y devolver** (paso 3 de los comentarios de `kpis.py`):

| Línea | Qué hace |
|---|---|
| `tasas = {}` | Una tercera libreta, vacía, para los porcentajes |
| `for canal in total:` | Recorre **los canales** de la libreta `total` (todos los canales que han aparecido) |
| `canceladas.get(canal, 0)` | Las canceladas de ese canal; **si ese canal no tiene ninguna, `0`** en vez de un error |
| `100 * canceladas / total[canal]` | El porcentaje: canceladas entre total, por 100 |
| `round(..., 1)` | Redondea a **1 decimal**: `33.3` en lugar de `33.333333333333336` |
| `return tasas` | **Entrega** el resultado. Sin esta línea, la función devuelve `None` |

**Seguimiento con las 4 reservas de la tarjeta** (web no, web **sí**, directo no, web no). Cada reserva es una vuelta del `for`:

1. Reserva 1 (web, no): `total = {"web": 1}`, `canceladas = {}`.
2. Reserva 2 (web, **sí**): `total = {"web": 2}`, `canceladas = {"web": 1}`.
3. Reserva 3 (directo, no): `total = {"web": 2, "directo": 1}`, `canceladas` igual.
4. Reserva 4 (web, no): `total = {"web": 3, "directo": 1}`, `canceladas` igual.

Después, el segundo `for`: `web` → 100 × 1 ÷ 3 = **33.3** y `directo` → 100 × **0** ÷ 1 = **0.0** (`directo` no está en `canceladas`: `.get` da `0`). Resultado: `{"web": 33.3, "directo": 0.0}`.

**Por qué `.get(canal, 0)` y no `canceladas[canal]`:** `agencia` no tiene ninguna cancelada, así que **no está** en `canceladas`. Pedirlo con corchetes da `KeyError: 'agencia'`. Con `.get(canal, 0)` se dice «lo que lleve, o `0` si todavía no está».

### Paso 5 · Probar y corregir

A mano, con **una sola línea** en la terminal, dentro de la carpeta del reto (copiadla entera y pulsad Intro):

```
python -c "from reservas_demo import RESERVAS; from kpis import tasa_cancelacion_por_canal; print(tasa_cancelacion_por_canal(RESERVAS))"
```

Tiene que salir `{'directo': 33.3, 'agencia': 0.0, 'web_intermediaria': 66.7}`. (No ejecutéis `python kpis.py` solo: ese fichero necesita datos y no enseña nada.) Después `python test_kpis.py 1`: las **dos pruebas de la tasa** tienen que salir `[OK]` en verde y el resumen pasa de `0 de 4` a `2 de 4`.

**Si os sale otra cosa:**

| Os sale | Probablemente |
|---|---|
| `{'directo': 33.333333333333336, …}` | Falta el `round(..., 1)` |
| `KeyError: 'agencia'` | Escribís `canceladas[canal]` en lugar de `canceladas.get(canal, 0)` |
| `None` (o la prueba dice que no es un diccionario) | Falta el `return tasas`, o está dentro del `for` (con 8 espacios) |
| `IndentationError` | Habéis pegado solo las líneas de dentro con el cursor ya sangrado (la primera queda con 8 espacios), o el fichero **no está guardado** (mirad si la pestaña tiene un punto): pegad la función entera y guardad con Ctrl+S |
| Sigue `NotImplementedError` | No habéis borrado la línea `raise NotImplementedError(...)` |
| `ZeroDivisionError` | Dividís entre un `total` de 0: no pasa si recorréis `total`, que solo tiene canales que han aparecido |

### Paso 6 · `ingreso_medio_por_reserva`

**La idea.** Hacer una lista con lo que ingresa cada reserva **no cancelada** (`noches × precio_noche`) y calcular su media. Una reserva cancelada no deja dinero.

```python
def ingreso_medio_por_reserva(reservas):
    """Ingreso medio de las reservas NO canceladas, con 2 decimales."""
    ingresos = []
    for r in reservas:
        if r["cancelada"] == 0:
            ingresos.append(r["noches"] * r["precio_noche"])
    if not ingresos:
        return 0.0
    return round(sum(ingresos) / len(ingresos), 2)
```

(Se copia igual que la anterior: función entera, de `def` a `raise`, pegada encima.)

| Línea | Qué hace |
|---|---|
| `ingresos = []` | Una lista vacía: un cajón donde irán los importes |
| `for r in reservas:` | Coge las reservas una a una |
| `if r["cancelada"] == 0:` | **Solo** si la reserva **no** está cancelada… |
| `ingresos.append(r["noches"] * r["precio_noche"])` | …calcula lo que ingresa (noches por precio) y **lo mete en el cajón** |
| `if not ingresos:` | «Si el cajón está vacío» (no hay ninguna confirmada) |
| `return 0.0` | …entrega `0.0` y termina: así **no se divide entre cero** |
| `sum(ingresos) / len(ingresos)` | La media: la **suma** de los importes entre **cuántos hay** |
| `round(..., 2)` | Redondea a 2 decimales (son euros) |

**Seguimiento.** Con las 3 reservas de la tarjeta (200 €, 200 € y 120 €): 520 ÷ 3 = **173.33**. Con las 8 reservas de ejemplo: las no canceladas son 5, y el cajón queda `[200.0, 200.0, 120.0, 180.0, 210.0]`. Suman 910 y 910 ÷ 5 = **182.0**.

### Paso 7 · Probar y corregir

A mano, con una línea (en la terminal, dentro de la carpeta del reto):

```
python -c "from reservas_demo import RESERVAS; from kpis import ingreso_medio_por_reserva; print(ingreso_medio_por_reserva(RESERVAS))"
```

Tiene que salir **`182.0`**. Después `python test_kpis.py 1`: `test_ingreso_medio…` en verde (**`3 de 4`**).

| Os sale | Probablemente |
|---|---|
| `208.75` | Estáis sumando también las **canceladas** (1670 € entre 8): falta el `if` o está al revés |
| `113.75` | Dividís entre las 8 reservas en lugar de entre las 5 confirmadas: usad `len(ingresos)` |
| `ZeroDivisionError` con una lista vacía | Falta el `if not ingresos: return 0.0` |
| `None` | Falta el `return` del final |
| `NameError: name 'ingresos' is not defined` | Falta la primera línea, `ingresos = []` |

### Paso 8 · `ocupacion_proxy`

**La idea.** Qué parte de las «noches posibles» (días del periodo × habitaciones) están ocupadas. Esta la hace **el docente en pantalla**; vosotros la copiáis y **explicáis una línea con vuestras palabras**.

```python
def ocupacion_proxy(reservas, capacidad_habitaciones):
    """Ocupación aproximada en %, con 1 decimal."""
    if capacidad_habitaciones <= 0:
        raise ValueError("La capacidad debe ser mayor que 0")
    if not reservas:
        return 0.0
    fechas = []
    for r in reservas:
        fechas.append(r["fecha_llegada"])
    dias = (max(fechas) - min(fechas)).days + 1
    noches = 0
    for r in reservas:
        if r["cancelada"] == 0:
            noches = noches + r["noches"]
    return round(100 * noches / (dias * capacidad_habitaciones), 1)
```

| Líneas | Qué hacen |
|---|---|
| `if capacidad_habitaciones <= 0:` y `raise ValueError(...)` | Si las habitaciones son 0 o menos, **no tiene sentido** calcular: se para con un error y un mensaje claro |
| `if not reservas:` y `return 0.0` | Si no hay reservas, la ocupación es `0.0` y se termina |
| `fechas = []` y el `for` con `append` | Un cajón con **la fecha de llegada de cada reserva** |
| `dias = (max(fechas) - min(fechas)).days + 1` | Días del periodo: de la **última** a la **primera** fecha, **más 1** para contar también el primer día |
| `noches = 0` y el `for` con `if` | Suma las noches de las reservas **no canceladas** (el marcador empieza en 0) |
| `return round(100 * noches / (dias * capacidad_habitaciones), 1)` | La fórmula: noches ocupadas entre noches posibles, por 100, con 1 decimal |

**Seguimiento con el dedo** (8 reservas, 5 habitaciones): del 1 al 20 de enero hay **20 días** (19 de diferencia + 1). Las noches no canceladas son 2 + 4 + 1 + 2 + 3 = **12**. Entonces 100 × 12 ÷ (20 × 5) = **12.0**.

**Por qué es un «proxy»:** el fichero no dice cuántas habitaciones tiene el hotel de verdad y cada reserva cuenta sus noches el día de la llegada. Es una **medida aproximada**, útil para comparar, no una ocupación exacta.

### Paso 9 · Todas las pruebas

`python test_kpis.py 1` termina con **`4 de 4 pruebas superadas`**, en verde, y a mano, con una línea, da **`12.0`**:

```
python -c "from reservas_demo import RESERVAS; from kpis import ocupacion_proxy; print(ocupacion_proxy(RESERVAS, 5))"
```

| Os sale | Probablemente |
|---|---|
| Ocupación `12.6` | Falta el `+ 1` en los días: usáis 19 en vez de 20 |
| Ocupación `22.0` | Contáis también las noches de las canceladas (22 en vez de 12) |
| `ZeroDivisionError` con capacidad 0 | Falta la primera comprobación (`capacidad_habitaciones <= 0`) |
| `TypeError` al restar fechas | Estáis restando textos y no fechas: en las 8 reservas de ejemplo ya son fechas; en el CSV las convierte la misión 4 |

**Para explicárselo a vuestra pareja** (elegid una):

1. En la tasa de cancelación, ¿qué pasaría si usarais `canceladas[canal]` en lugar de `canceladas.get(canal, 0)`? ¿Con qué canal?
2. La tasa cuenta las reservas canceladas y las que no, pero el ingreso medio solo cuenta las no canceladas. ¿Por qué?
3. ¿Qué diferencia hay entre `print(tasas)` y `return tasas`? ¿Cuál necesita la prueba?

## Misión 4 · Leer el CSV

Tarjeta: [Misión 4](../1_Trabajar/tarjetas/tarjeta_4_ficheros.md). Tampoco aquí hay código: se da un **fichero pequeño con la respuesta resuelta a mano**. Guardad estas cuatro líneas como `mini.csv` junto a `kpis.py`:

```
fecha_llegada,noches,precio_noche,canal,cancelada
2025-01-01,2,100.0,directo,0
2025-01-03,3,,agencia,0
2025-01-05,0,50.0,web_intermediaria,1
```

Y en `python`:

```python
from kpis import leer_reservas
reservas, avisos = leer_reservas("mini.csv")
print(len(reservas), avisos)
```

Tiene que salir **1 reserva válida** (la de la fila 2) y **dos avisos**, uno por cada fila mala:

```
1 ["Fila 3 descartada: could not convert string to float: ''", 'Fila 4 descartada: noches debe ser >= 1']
```

El texto exacto del motivo puede variar según cómo lo hayáis escrito (el primero es el mensaje de Python); lo que tiene que coincidir es el **número de fila** (la cabecera es la fila 1) y que haya un aviso por cada fila descartada.

Con otros ficheros, `leer_reservas` tiene que **lanzar un error** (no devolver avisos) con un mensaje claro:

| Fichero | Mensaje esperado |
|---|---|
| Uno que no existe (`leer_reservas("nada.csv")`) | `FileNotFoundError: No se encuentra el fichero: nada.csv` (incluye la ruta) |
| El mismo `mini.csv` sin la columna `cancelada` | `ValueError: Faltan columnas obligatorias: ['cancelada']` (nombra las que faltan) |

**Si os sale otro resultado:**

| Os sale | Probablemente |
|---|---|
| Avisos de «Fila 2» y «Fila 3» | Numeráis desde 1: la cabecera es la fila 1, los datos empiezan en la 2 |
| 2 reservas válidas (entra la de 0 noches) | Solo convertís los tipos: falta validar el **valor** (`noches` mayor o igual que 1) |
| 1 reserva válida pero `avisos` vacío | Descartáis las filas malas **en silencio**: hay que guardar un aviso por cada una |
| `TypeError: list indices must be integers or slices, not str` al recorrer lo que devuelve `leer_reservas` | La función devuelve **dos** cosas y las estáis guardando en una sola variable: `reservas, avisos = leer_reservas(...)` |

**Para explicárselo a vuestra pareja:** ¿por qué es mejor descartar la fila mala y apuntarla en `avisos` que parar el programa? ¿Y por qué no descartarla sin decir nada?

## Misión 5 · Guardar y entregar

Tarjeta: [Misión 5](../1_Trabajar/tarjetas/tarjeta_5_salida.md). La salida esperada con el CSV real ya está en «Misión terminada cuando» de la tarjeta. Aquí, una **comprobación cruzada**: la ocupación es inversamente proporcional a la capacidad, así que con el CSV real:

| Orden | `ocupacion_proxy_pct` |
|---|---|
| `python kpis.py reservas_turisdata.csv salida.json --capacidad 20` | `84.0` |
| `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` | `42.0` |
| `python kpis.py reservas_turisdata.csv salida.json --capacidad 80` | `21.0` |

Si al doblar la capacidad la ocupación no se queda en la mitad, la capacidad no está llegando a `ocupacion_proxy` (revisad cómo pasáis `args.capacidad`).

**Código de salida.** Tras un error provocado a propósito (fichero que no existe, capacidad 0), el programa tiene que terminar con **código 1**, y con un fichero correcto, con **0**. Se ve con `echo $?` (Linux y Mac), `echo %errorlevel%` (cmd de Windows) o `$LASTEXITCODE` (PowerShell).

| Os pasa | Probablemente |
|---|---|
| Sale `ERROR: …` pero el código de salida es 0 | `main` no devuelve 1 cuando captura el error (la plantilla ya hace `sys.exit(main())`: lo que devuelva `main` es el código) |
| La ocupación no cambia al cambiar `--capacidad` | Hay un `40` escrito a mano en algún sitio en lugar de usar `args.capacidad` |

**Para explicárselo a vuestra pareja:** ¿por qué `main` recibe `argumentos=None` en vez de leer siempre lo que se escribe en la terminal?

## Mensajes de error: qué significan

| Mensaje | Qué significa | Cómo se arregla |
|---|---|---|
| `TypeError: list indices must be integers or slices, not str` | Pedís a la lista algo por nombre (`reservas["canal"]`) | Primero el número de la reserva y después el nombre: `reservas[0]["canal"]` |
| `IndexError: list index out of range` | Pedís una posición que no existe (con 3 reservas, `reservas[3]`) | Los índices van de 0 a la cantidad menos 1; la última es `[-1]` |
| `KeyError: 'directo'` | Preguntáis a un diccionario por una clave que todavía no tiene | `dic.get(clave, 0)` o comprobar antes con `if clave in dic` |
| `ZeroDivisionError: float division by zero` | Estáis dividiendo entre 0 (por ejemplo, la media de 0 reservas) | Comprobar antes que no hay 0 |
| `ValueError: could not convert string to float: ''` | El texto no es un número: está vacío, o lleva coma decimal (`'52,7'`) | Al leer el CSV, capturarlo con `except ValueError` y descartar la fila avisando |
| `ValueError: invalid literal for int() with base 10: 'abc'` | Lo mismo con un entero | Lo mismo |
| `FileNotFoundError: [Errno 2] No such file or directory: 'nada.csv'` | El fichero no está en esa ruta, o la terminal está en otra carpeta | Revisar el nombre y abrir la terminal dentro de la carpeta del reto |
| `ModuleNotFoundError: No module named 'reservas_demo'` | Se ejecuta desde otra carpeta | Abrir la terminal dentro de la carpeta del reto |
| `SyntaxError: f-string: unmatched '['` (Python 3.11) | Comillas dobles dentro de un f-string con comillas dobles | Comillas simples por dentro: `f"…{reservas[1]['canal']}…"` |

Los mensajes de las pruebas (`test_kpis.py`) son distintos: dicen **qué debería salir**. Leedlos antes de tocar nada y comparadlos con lo que sale en la vuestra.
