# Solucionario de las misiones · Sprint 4 · «Herramientas internas»

> **Para contrastar vuestro trabajo**, cuando hayáis terminado una misión o agotado las pistas de su tarjeta. No es para copiar: **las pruebas mandan** y el docente puede preguntaros por cualquier línea. Volver al [índice de las misiones](../1_Trabajar/README.md).

## Índice

- [Cómo usarlo](#cómo-usarlo): primero intentarlo, después contrastar
- [Misión 0 · Mirar la demo](#misión-0--mirar-la-demo): qué sale y las respuestas a las cinco preguntas
- [Misión 1 · Datos en memoria](#misión-1--datos-en-memoria): las seis líneas, la salida y los fallos más comunes
- [Misión 2 · Decidir y repetir](#misión-2--decidir-y-repetir): los cuatro bucles, la salida y los fallos más comunes
- [Misión 3 · Funciones que calculan](#misión-3--funciones-que-calculan): cifras para comprobar a mano y fallos reconocibles por el número
- [Misión 4 · Leer el CSV](#misión-4--leer-el-csv): un CSV pequeño resuelto a mano y fallos reconocibles
- [Misión 5 · Guardar y entregar](#misión-5--guardar-y-entregar): una comprobación cruzada de cifras y fallos reconocibles
- [Mensajes de error: qué significan](#mensajes-de-error-qué-significan): los errores más comunes de Python en el reto y cómo se arreglan

## Cómo usarlo

**Primero intentadlo.** Cuando algo no sale, seguid siempre este orden:

| Escalón | Qué hacéis |
|---|---|
| 1 | Leed el mensaje de la prueba: dice **qué esperaba y qué recibió** |
| 2 | Repasad la tarjeta de la misión (su «Si os atascáis») y la lección del curso |
| 3 | Preguntad al equipo |
| 4 | Preguntad al docente |
| 5 | **Este solucionario**, para contrastar o desbloquearos |

**Después de mirarlo, cerradlo y volved a escribirlo sin mirar.** Copiar una línea no es saberla: la prueba de que la sabéis es poder explicársela a vuestra pareja con vuestras palabras. Cada misión termina con una pregunta para eso.

**Qué hay y qué no hay.** En las misiones 0 a 2 (ejercicios de práctica) está la solución completa. En las misiones 3 a 5, que es lo que se evalúa en `kpis.py`, **no hay código**: hay cifras para comprobar a mano, los fallos más comunes reconocibles por el número que sale y una pregunta para explicar. Los cuadernos `S04_03` y `S04_04` traen, además, celdas plegadas 🆘 «Solución de referencia» con la solución de **sus propios ejercicios**: sirven para seguir si os atascáis en el cuaderno y no son las funciones de `kpis.py`, que escribís vosotros. Si usáis un asistente de IA, seguid las reglas de uso de la IA de la [ficha del reto](Reto_Sprint_04.md) y declarad el uso en el README.

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

Tarjeta: [Misión 3](../1_Trabajar/tarjetas/tarjeta_3_funciones.md). Aquí **no se da el código** de `kpis.py`: es lo que se evalúa. Se dan las cifras con las 8 reservas de [`reservas_demo.py`](../1_Trabajar/reto_herramientas/reservas_demo.py) para que comprobéis **a mano** antes de pasar la prueba (en `python`: `from reservas_demo import RESERVAS` y llamad a la función con esa lista).

| Función | Cómo se calcula con las 8 reservas | Resultado |
|---|---|---|
| `tasa_cancelacion_por_canal(RESERVAS)` | `directo`: 1 cancelada de 3 = 33,3 %; `agencia`: 0 de 2 = 0,0 %; `web_intermediaria`: 2 de 3 = 66,7 % | `{'directo': 33.3, 'agencia': 0.0, 'web_intermediaria': 66.7}` |
| `ingreso_medio_por_reserva(RESERVAS)` | Solo las no canceladas: 200 + 200 + 120 + 180 + 210 = 910 € entre 5 reservas | `182.0` |
| `ocupacion_proxy(RESERVAS, 5)` | Días: del 1 al 20 de enero son **20** (cuenta también el primer día). Noches confirmadas: 12. Fórmula: 100 × 12 ÷ (20 × 5) | `12.0` |

**Si os sale otro número:**

| Os sale | Probablemente |
|---|---|
| Ingreso medio `208.75` | Sumáis también las canceladas (1670 € entre 8) |
| Ingreso medio `113.75` | Dividís entre las 8 reservas en vez de entre las 5 confirmadas |
| Ocupación `12.6` | Falta el `+ 1` en los días: usáis 19 en vez de 20 |
| Ocupación `22.0` | Contáis también las noches de las canceladas (22 en vez de 12) |
| Una tasa como `33.333333333333336` | Falta el `round(..., 1)` |
| `ZeroDivisionError` con una lista vacía, o con capacidad 0 | Falta comprobar antes: lista vacía → `0.0`; capacidad menor o igual que 0 → `ValueError` con mensaje |

**Para explicárselo a vuestra pareja:** la tasa de cancelación cuenta las reservas canceladas y las que no, pero el ingreso medio solo cuenta las no canceladas. ¿Por qué?

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

Los mensajes de las pruebas (`test_kpis.py`) son distintos: dicen **qué esperaba y qué recibió**. Se leen antes de tocar nada.
