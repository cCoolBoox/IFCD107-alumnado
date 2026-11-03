# Solucionario de las misiones · Sprint 4 · «Herramientas internas»

> **Para contrastar vuestro trabajo**, cuando hayáis terminado una misión o agotado las pistas de su tarjeta. No es para copiar: **las pruebas mandan** y el docente puede preguntaros por cualquier línea. Volver al [índice de las misiones](../1_Trabajar/README.md).

## Índice

- [Cómo usarlo](#cómo-usarlo): primero intentarlo, después contrastar
- [Misión 0 · Mirar la demo](#misión-0--mirar-la-demo): qué sale y las respuestas a las cinco preguntas
- [Misión 1 · Datos en memoria](#misión-1--datos-en-memoria): los mismos pasos que la tarjeta (3 y 4.1 a 4.6), con las seis líneas, la salida y los fallos más comunes
- [Misión 2 · Decidir y repetir](#misión-2--decidir-y-repetir): los mismos pasos que la tarjeta (3 a 7), con los cuatro bucles, la salida y los fallos más comunes
- [Misión 3 · Funciones que calculan](#misión-3--funciones-que-calculan): los mismos pasos que la tarjeta (1 a 9), con el código en trozos y cada línea explicada
- [Misión 4 · Leer el CSV](#misión-4--leer-el-csv): los mismos pasos que la tarjeta (4.1 a 5.12), con el código explicado línea a línea
- [Misión 5 · Guardar y entregar](#misión-5--guardar-y-entregar): los mismos pasos que la tarjeta (2 a 5), con el código explicado, los tres errores y la comprobación cruzada
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

**Qué hay y qué no hay.** En las misiones 0 a 5 está la solución con el código **explicado línea a línea**: la parte de práctica y las funciones de `kpis.py` (calcular en la misión 3, leer el CSV en la 4, guardar y entregar en la 5), con los mismos pasos que su tarjeta, los resultados esperados y los fallos más comunes. Los cuadernos `S04_03` y `S04_04` traen, además, celdas plegadas 🆘 «Solución de referencia» con la solución de **sus propios ejercicios**. Si usáis un asistente de IA, seguid las reglas de uso de la IA de la [ficha del reto](Reto_Sprint_04.md) y declarad el uso en el README.

**Cuándo se publica cada parte.** Las misiones 0 a 2 y los mensajes de error, al acabar la clase del martes; las misiones 3 a 5, al acabar la del miércoles.

## Misión 0 · Mirar la demo

<h2 align="center">Entender el programa del cliente antes de escribir nada</h2>

> **Para contrastar**, cuando hayáis terminado el paso o agotado las pistas de la [tarjeta](../1_Trabajar/tarjetas/tarjeta_0_mirar_la_demo.md). **Tiene los mismos números de paso que la tarjeta** (1, 2.1, 3.2…): buscad el vuestro. Primero intentadlo; después de mirarlo, cerradlo y volved a explicarlo sin mirar. Lo que copiéis, tenéis que saber explicarlo.

**Esta misión no se escribe: se lee y se ejecuta.** Lo que se contrasta es qué sale y las respuestas a las cinco preguntas.

### Pasos 1 y 2 · Preparar

| Paso | Qué tiene que pasar | Fallo habitual |
|---|---|---|
| **1** | Al descomprimir, la carpeta `reto_herramientas` contiene `demo_cliente.py`, `kpis.py`, `mision_1_datos.py`, `mision_2_decidir.py`, `reservas_demo.py`, `test_kpis.py` y `reservas_turisdata.csv` | Abrir el `.zip` sin extraerlo: se ven los archivos, pero no se pueden ejecutar |
| **2.4** | `python --version` da `Python 3.11` o superior | `python` no se reconoce: probad `python3` y usadlo en todo el reto |

### Paso 3 · Dónde están las cuatro piezas en `demo_cliente.py`

| Paso | Pieza | Línea | Qué es |
|---|---|---|---|
| **3.2** | Datos | 12 | `from reservas_demo import RESERVAS`: la lista de 8 reservas |
| **3.3** | Bucle | 25 | `for reserva in RESERVAS:` recorre las reservas una a una |
| **3.4** | Decisión | 28 | `if reserva["cancelada"] == 1:` (con su `else` en la línea 30) |
| **3.5** | Mensaje | 36–41 | Los `print(...)`: el resumen final |

Además hay dos cosas que preparan el resumen:

- **Líneas 20–23:** `total`, `canceladas`, `ingreso_total` y `por_canal` empiezan vacías (en `0` o `{}`).
- **Línea 33–34:** `confirmadas = total - canceladas` y `media = ingreso_total / confirmadas`.

### Paso 5 · Ejecutarlo

`python demo_cliente.py` tiene que escribir **exactamente**:

```
=== Resumen semanal de reservas ===
Reservas analizadas: 8
Canceladas: 3 (37.5 %)
Ingreso medio por reserva confirmada: 182.00 €
  - directo: 3 reservas
  - agencia: 2 reservas
  - web_intermediaria: 3 reservas
```

| Os sale | Probablemente |
|---|---|
| `No such file or directory` o `ModuleNotFoundError: reservas_demo` | La terminal está en otra carpeta: abridla **dentro** de `reto_herramientas` (`ls` o `dir` debe mostrar `demo_cliente.py`) |
| `python` no se reconoce | Probad `python3` |
| Cifras distintas de las de arriba | Habéis cambiado algo de `demo_cliente.py` o de `reservas_demo.py`: volved a descomprimir el `.zip` |

### Paso 6 · Las cinco preguntas

| Pregunta de la tarjeta | Respuesta |
|---|---|
| 1. ¿Cuántas reservas analiza el programa y qué línea lo calcula? | **8**, con `total = len(RESERVAS)` (línea 20) |
| 2. ¿Por qué `canceladas` empieza en `0` y `por_canal` en `{}`? | Son **acumuladores**: se empieza en `0` y en `{}` porque todavía no se ha contado nada; el bucle los va rellenando |
| 3. Si la primera reserva pasara a estar cancelada (`"cancelada": 1`), ¿qué cifras cambian? | Las canceladas pasan de 3 a **4 (50.0 %)** y el ingreso medio, de 182.00 a **177.50 €** (se quitan los 200 € de esa reserva y quedan 4 confirmadas). El reparto por canal **no cambia**: cuenta todas las reservas, canceladas o no |
| 4. ¿Qué hace `:.1f` dentro de las llaves del f-string? | Muestra el número con **un decimal** (`:.2f`, con dos) |
| 5. Si `RESERVAS` estuviera vacía, ¿qué error saldría y en qué línea? | **`ZeroDivisionError: float division by zero`** en `media = ingreso_total / confirmadas` (línea 34): hay 0 confirmadas. Es el primer error que el programa debería evitar; lo retomáis en la misión 4 |

**Comprobación de la pregunta 5** (pasos 6.3 a 6.5, en la copia `demo_copia.py` con `RESERVAS = []`):

```
Traceback (most recent call last):
  File "demo_copia.py", line 34, in <module>
    media = ingreso_total / confirmadas
ZeroDivisionError: float division by zero
```

| Os sale | Probablemente |
|---|---|
| Ningún error, y el resumen sale con 8 reservas | Habéis cambiado el original y no la copia, o no guardasteis la copia (punto ● en la pestaña) |
| `NameError: name 'RESERVAS' is not defined` | Borrasteis la línea del `from … import` sin escribir `RESERVAS = []` |

### Paso 7 · El curso

Sin solución aquí: los ejercicios del curso y del Taller se corrigen solos (en verde).

### Para explicárselo a vuestra pareja

¿Qué hace el `for` de la demo, línea a línea, y por qué dentro hay un `if` con su `else`?

## Misión 1 · Datos en memoria

<h2 align="center">Leer y modificar una lista de reservas</h2>

> **Para contrastar**, cuando hayáis terminado el paso o agotado las pistas de la [tarjeta](../1_Trabajar/tarjetas/tarjeta_1_datos.md). **Tiene los mismos números de paso que la tarjeta** (3.2, 4.1… 4.6): buscad el vuestro. Primero intentadlo; después de mirarlo, cerradlo y volved a escribirlo sin mirar. Lo que copiéis, tenéis que saber explicarlo.

**Fichero:** [`mision_1_datos.py`](../1_Trabajar/reto_herramientas/mision_1_datos.py). Los apartados del archivo se llaman 1.1 a 1.6; en la tarjeta son los pasos **4.1 a 4.6**.

**Lo que no cambia en ningún apartado**

- Se escribe **pegado al borde izquierdo** (sin espacios al principio de la línea).
- Se guarda con **Ctrl+S** antes de ejecutar (sin punto ● en la pestaña).
- Se borra también el `# TODO`.

### Paso 3 · Antes de escribir nada

`python mision_1_datos.py` con el archivo tal cual tiene que dar:

```
Cantidad al empezar: None
Canal de la primera: None
Precio de la última: None
Ahora hay 3 reservas
None

Misión 1: 0 de 6 apartados bien. Te faltan:
   ✗ 1.1  `cantidad` debe valer 3 (cuéntala ANTES de añadir la reserva nueva)
   ...
```

### Paso 4 · Los seis apartados

| Paso | Qué se escribe | Qué sale al ejecutar | Fallo habitual |
|---|---|---|---|
| **4.1** (1.1) | `cantidad = len(reservas)` | `Cantidad al empezar: 3` · **1 de 6** (vale **3**: se cuenta antes de añadir la reserva del 4.5) | `len(reservas[0])` da 4: son las claves de la primera reserva, no cuántas reservas hay |
| **4.2** (1.2) | `canal_primera = reservas[0]["canal"]` | `Canal de la primera: directo` · **2 de 6** | `reservas["canal"]` → `TypeError: list indices must be integers or slices, not str`: falta el número de la reserva |
| **4.3** (1.3) | `precio_ultima = reservas[-1]["precio_noche"]` | `Precio de la última: 60.0` · **3 de 6** | `reservas[3]` → `IndexError: list index out of range`: solo hay 3 reservas (índices 0 a 2) |
| **4.4** (1.4) | `reservas[0]["cancelada"] = 1` | No se ve nada nuevo · **4 de 6** | `==` en vez de `=`: no da error y no cambia nada, y la comprobación 1.4 falla |
| **4.5** (1.5) | `reservas.append({"canal": "directo", "noches": 3, "precio_noche": 80.0, "cancelada": 0})` | `Ahora hay 4 reservas` · **5 de 6** | Olvidar una clave o cambiarle el nombre (`precio` en lugar de `precio_noche`): el diccionario no coincide y falla la 1.5 |
| **4.6** (1.6) | `texto = f"La reserva 2 es del canal {reservas[1]['canal']}: {reservas[1]['noches']} noches a {reservas[1]['precio_noche']} euros"` | `La reserva 2 es del canal agencia: 4 noches a 50.0 euros` · **6 de 6** | Olvidar la `f` (sale el texto con las llaves) o usar comillas dobles dentro de un f-string de comillas dobles: `SyntaxError` en Python 3.11 |

**Al terminar** tiene que salir:

```
Cantidad al empezar: 3
Canal de la primera: directo
Precio de la última: 60.0
Ahora hay 4 reservas
La reserva 2 es del canal agencia: 4 noches a 50.0 euros

✅ ¡Misión 1 superada! Ya sabes leer y modificar los datos del reto.
```

| Os sale | Probablemente |
|---|---|
| `KeyError: 'canl'` | Etiqueta mal escrita: tiene que ser exactamente `"canal"` (4.2) |
| `IndexError: list index out of range` | Posición que no existe: la primera es `0`, la última `-1` (4.2, 4.3) |
| Un apartado ya hecho sigue en la lista de «Te faltan» | Archivo **sin guardar** (punto ● en la pestaña): Ctrl+S y ejecutad otra vez |
| `1.1` falla con `cantidad` = 4 | Contasteis **después** de añadir la reserva (4.5): `cantidad` va antes |
| `TypeError` o el apartado sigue en la lista | Se dejó el `None`, o falta una coma o una llave |
| `ModuleNotFoundError` | La terminal no está en la carpeta del reto |

### Paso 5 · Taller

Sin solución aquí: los dos puzles se montan en el Taller y se corrigen solos.

### Para explicárselo a vuestra pareja

¿Por qué `cantidad` vale 3 si al terminar la misión hay 4 reservas?

## Misión 2 · Decidir y repetir

<h2 align="center">Contar con <code>if</code> y <code>for</code></h2>

> **Para contrastar**, cuando hayáis terminado el paso o agotado las pistas de la [tarjeta de la misión 2](../1_Trabajar/tarjetas/tarjeta_2_decidir.md). **Tiene los mismos números de paso que la tarjeta** (3.x a 7.x): buscad el vuestro. Primero intentadlo; después de mirarlo, cerradlo y volved a escribirlo sin mirar. Lo que copiéis, tenéis que saber explicarlo.

**El punto de partida**, en [`mision_2_decidir.py`](../1_Trabajar/reto_herramientas/mision_2_decidir.py) (con las 8 reservas de [`reservas_demo.py`](../1_Trabajar/reto_herramientas/reservas_demo.py)):

- Las cuatro variables ya vienen escritas: `canceladas = 0`, `noches_confirmadas = 0`, `por_canal = {}` y `largas = []`.
- En cada apartado se **sustituye la línea `# TODO`** por el bucle.
- Todo lo de debajo de `NO TOCAR: comprobación automática` se queda como está.

**Cómo escribirlo sin errores de sangría.** Cada nivel (4 espacios, o un Tab) **más a la derecha** significa «dentro de» lo de arriba. El `for` se escribe al borde izquierdo (**nivel 0**), el `if` o la línea que sigue, **un nivel** más, y lo que hay dentro del `if`, **dos**. Guardad con **Ctrl+S** antes de ejecutar (sin ● en la pestaña).

### Paso 4 · Apartado 2.1: contar las canceladas

```python
canceladas = 0
for reserva in RESERVAS:
    if reserva["cancelada"] == 1:
        canceladas = canceladas + 1
```

| Paso | Línea | Nivel | Qué hace, con palabras normales |
|---|---|---|---|
| **4.3** | `for reserva in RESERVAS:` | 0 | Coge las reservas **una a una**; en cada vuelta, `reserva` es una |
| **4.4** | `if reserva["cancelada"] == 1:` | 1 | «¿Esta reserva está cancelada?» (`1` = sí) |
| **4.5** | `canceladas = canceladas + 1` | 2 | **Solo si** lo está, suma uno al contador |

**Seguimiento con las 8 reservas** (`cancelada` de cada una: 0, 1, 0, 0, 1, 0, 0, 1):

| Vuelta | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `canceladas` después | 0 | **1** | 1 | 1 | **2** | 2 | 2 | **3** |

✅ **4.6 · Sale** `Canceladas: 3` y `Misión 2: 1 de 4 apartados bien. Te faltan:` (con las otras tres ✗).

| Os sale | Probablemente |
|---|---|
| `Canceladas: 1` | Habéis escrito `canceladas = 1` en vez de `canceladas = canceladas + 1`: se queda en 1 |
| `Canceladas: 8` | Falta el `if`: la suma queda directamente dentro del `for` y se hace en **todas** las vueltas |
| `Canceladas: 0` | El fichero **no está guardado** (● en la pestaña) |
| `Canceladas: 5` | La condición es `== 0` en vez de `== 1`: cuenta las **confirmadas** |
| `IndentationError: expected an indented block after 'if' statement` | Falta sangrar la línea de debajo del `if` (4.5): **dos niveles** |
| `SyntaxError: expected ':'` | Falta el `:` al final del `for` o del `if` |
| `SyntaxError: cannot assign to subscript here. Maybe you meant '==' instead of '='?` | Habéis escrito `=` donde va `==` |

### Paso 5 · Apartado 2.2: sumar las noches

```python
noches_confirmadas = 0
for reserva in RESERVAS:
    if reserva["cancelada"] == 0:
        noches_confirmadas = noches_confirmadas + reserva["noches"]
```

| Paso | Línea | Nivel | Qué hace, con palabras normales |
|---|---|---|---|
| **5.2** | `for reserva in RESERVAS:` | 0 | Una vuelta por reserva |
| **5.3** | `if reserva["cancelada"] == 0:` | 1 | «¿**No** está cancelada?» (`0` = confirmada) |
| **5.4** | `noches_confirmadas = noches_confirmadas + reserva["noches"]` | 2 | Suma **las noches de esa reserva** (no un `1`) |

- Las reservas confirmadas son las 1, 3, 4, 6 y 7, con 2 + 4 + 1 + 2 + 3 noches.
- El marcador va: 2, 2, 6, 7, 7, 9, 12, 12.

✅ **5.5 · Sale** `Noches confirmadas: 12` y `2 de 4 apartados bien`.

| Os sale | Probablemente |
|---|---|
| `Noches confirmadas: 22` | No hay `if`: suma las noches de **todas** (22), también de las canceladas |
| `Noches confirmadas: 10` | Habéis comparado con `== 1`: suma las noches de las **canceladas** (3 + 5 + 2) |
| `Noches confirmadas: 0` | Fichero sin guardar, o el `+ reserva["noches"]` no está |

### Paso 6 · Apartado 2.3: contar por canal

```python
por_canal = {}
for reserva in RESERVAS:
    canal = reserva["canal"]
    por_canal[canal] = por_canal.get(canal, 0) + 1
```

| Paso | Línea | Nivel | Qué hace, con palabras normales |
|---|---|---|---|
| **6.2** | `for reserva in RESERVAS:` | 0 | Una vuelta por reserva |
| **6.3** | `canal = reserva["canal"]` | 1 | Guarda el canal de **esta** reserva en `canal` |
| **6.4** | `por_canal[canal] = por_canal.get(canal, 0) + 1` | 1 | «Lo que llevo de ese canal, o `0` si todavía no está; le sumo 1 y lo guardo» |

**Seguimiento** (el diccionario va creciendo):

| Vuelta | `canal` | `por_canal` después |
|---|---|---|
| 1 | `directo` | `{'directo': 1}` |
| 2 | `directo` | `{'directo': 2}` |
| 3 | `agencia` | `{'directo': 2, 'agencia': 1}` |
| 4 | `agencia` | `{'directo': 2, 'agencia': 2}` |
| 5 a 8 | `web_intermediaria`, `web_intermediaria`, `directo`, `web_intermediaria` | `{'directo': 3, 'agencia': 2, 'web_intermediaria': 3}` |

✅ **6.5 · Sale** `Por canal: {'directo': 3, 'agencia': 2, 'web_intermediaria': 3}` y `3 de 4 apartados bien`.

| Os sale | Probablemente |
|---|---|
| `KeyError: 'directo'` | Habéis escrito `por_canal[canal] = por_canal[canal] + 1` (o `+= 1`) **sin `.get`**: la primera vez, el canal todavía no está en el diccionario |
| `Por canal: {}` | Fichero sin guardar, o el `for` queda sin esa línea dentro |
| `Por canal: {'web_intermediaria': 1}` | La línea 6.4 está **fuera** del `for` (nivel 0): solo cuenta una vez, con el último canal |

### Paso 7 · Apartado 2.4: la lista de canales

```python
largas = []
for reserva in RESERVAS:
    if reserva["cancelada"] == 0 and reserva["noches"] >= 3:
        largas.append(reserva["canal"])
```

| Paso | Línea | Nivel | Qué hace, con palabras normales |
|---|---|---|---|
| **7.2** | `for reserva in RESERVAS:` | 0 | Una vuelta por reserva |
| **7.3** | `if reserva["cancelada"] == 0 and reserva["noches"] >= 3:` | 1 | «¿Confirmada **y** de 3 noches o más?» Se tienen que cumplir **las dos** |
| **7.4** | `largas.append(reserva["canal"])` | 2 | Añade el **canal** de esa reserva al final de la lista |

- La reserva 3 (`agencia`, 4 noches) y la 7 (`directo`, 3 noches) cumplen las dos condiciones, en ese orden.
- La 2 y la 5 tienen 3 o más noches, pero están **canceladas**: no entran.

✅ **7.5 · Sale** `Confirmadas de 3 noches o más: ['agencia', 'directo']` y la línea final.

| Os sale | Probablemente |
|---|---|
| `['agencia']` | `>` en lugar de `>=`: la reserva de **3** noches se queda fuera |
| Una lista con **7** canales | `or` en lugar de `and`: entra todo lo que cumpla **una** de las dos condiciones |
| `['directo', 'web_intermediaria']` | `== 1` en vez de `== 0`: entran las **canceladas** de 3 noches o más (reservas 2 y 5) |
| `[]` | El fichero no está guardado (● en la pestaña) |
| `AttributeError: 'list' object has no attribute 'apend'` | `append` mal escrito |

### Qué tiene que salir al final

```
Canceladas: 3
Noches confirmadas: 12
Por canal: {'directo': 3, 'agencia': 2, 'web_intermediaria': 3}
Confirmadas de 3 noches o más: ['agencia', 'directo']

✅ ¡Misión 2 superada! Ya sabes contar con if y for: es la base de los KPI.
```

**Si el marcador se queda en «N de 4»:** cada ✗ nombra el apartado (`2.1`, `2.2`, `2.3` o `2.4`) y lo que `debe valer`. Mirad el paso con ese número en este solucionario.

**Para explicárselo a vuestra pareja:** en el 2.3, ¿qué pasa si quitáis el `.get(..., 0)` y escribís solo `por_canal[canal] = por_canal[canal] + 1`? ¿Por qué?

## Misión 3 · Funciones que calculan

<h2 align="center">Tres funciones que calculan, con el código explicado línea a línea</h2>

**Cómo usarlo**

- Para **contrastar**, cuando hayáis terminado el paso o agotado las pistas de la [tarjeta de la misión 3](../1_Trabajar/tarjetas/tarjeta_3_funciones.md).
- Tiene los **mismos números de paso** que la tarjeta (4.10, 4.11, 6.4…): buscad el vuestro.
- Las funciones se escriben en [`kpis.py`](../1_Trabajar/reto_herramientas/kpis.py); los datos de ejemplo están en [`reservas_demo.py`](../1_Trabajar/reto_herramientas/reservas_demo.py).
- Cada trozo de código va seguido de una tabla que explica **cada línea con palabras normales**. Si una línea no la entendéis, no la copiéis: preguntad.
- **Primero intentadlo.** Después de mirarlo, cerradlo y volved a escribirlo sin mirar.

### Pasos 1 y 2 · Aprender

- No hay nada que escribir aquí: son los ejercicios del curso y del Taller (funciones, `def`, `return`, diccionarios).
- Si el paso 4 os parece un salto, **volved al puzle «Contar con un diccionario» del Taller**: es casi la misma función.

### Paso 3 · Ver las pruebas fallar

Con la plantilla sin tocar, `python test_kpis.py 1` (pasos 3.1 y 3.2) tiene que enseñar, en rojo:

```
--- FASE 1 · funciones que calculan (datos en memoria) ---
[ERROR] test_ingreso_medio_por_reserva: NotImplementedError: TODO (misión 3): ingreso_medio_por_reserva
[ERROR] test_ocupacion_proxy: NotImplementedError: TODO (misión 3): ocupacion_proxy
[ERROR] test_tasa_cancelacion_por_canal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal
[ERROR] test_tasa_cancelacion_se_redondea_a_un_decimal: NotImplementedError: TODO (misión 3): tasa_cancelacion_por_canal

0 de 4 pruebas superadas
```

- Si lo veis así, **todo va bien**: las funciones todavía no están hechas.
- Si no sale `0 de 4`:
  - Mirad si habéis escrito el `1` al final (`python test_kpis.py 1`).
  - Mirad si la terminal está dentro de la carpeta del reto.

### Paso 4 · `tasa_cancelacion_por_canal`

**Ojo con los números:** los pasos **4.1 a 4.9** (a mano, y preparar el fichero) no llevan código. El código está en **4.10, 4.11 y 4.12**, que son los `# Paso 1, 2, 3` de los comentarios de la función.

**La idea**

- Hay que contar dos cosas por cada canal: cuántas reservas hay y cuántas están canceladas.
- Después, dividir.

**Cómo copiarla sin errores de sangría**

- En `kpis.py`, seleccionad la función entera: **desde la línea `def …` hasta la línea `raise NotImplementedError(...)`, incluida**.
- Pegad la de abajo encima.
- Guardad con Ctrl+S.
- Si pegáis solo las líneas de dentro y el cursor ya tenía 4 espacios, la primera queda con 8 y sale `IndentationError: unexpected indent`.

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

**Primera parte · preparar y contar** (4.10 y 4.11):

| Línea | Qué hace, con palabras normales |
|---|---|
| `total = {}` | Una libreta vacía donde apuntar **cuántas reservas** tiene cada canal |
| `canceladas = {}` | Otra libreta vacía para **cuántas canceladas** tiene cada canal |
| `for r in reservas:` | Coge las reservas **una a una**; en cada vuelta, `r` es la reserva de turno |
| `canal = r["canal"]` | Anota el canal de esa reserva (`"web"`, `"directo"`…) para no escribirlo cada vez |
| `total[canal] = total.get(canal, 0) + 1` | «Mira lo que lleva ese canal en `total` (si todavía no está, cuenta `0`), **suma 1** y apúntalo» |
| `if r["cancelada"] == 1:` | Solo si esta reserva está cancelada, haz lo de abajo |
| `canceladas[canal] = canceladas.get(canal, 0) + 1` | Lo mismo que con `total`, pero en la libreta de canceladas |

**Segunda parte · calcular y devolver** (4.12):

| Línea | Qué hace |
|---|---|
| `tasas = {}` | Una tercera libreta, vacía, para los porcentajes |
| `for canal in total:` | Recorre **los canales** de la libreta `total` (todos los canales que han aparecido) |
| `canceladas.get(canal, 0)` | Las canceladas de ese canal; **si ese canal no tiene ninguna, `0`** en vez de un error |
| `100 * canceladas / total[canal]` | El porcentaje: canceladas entre total, por 100 |
| `round(..., 1)` | Redondea a **1 decimal**: `33.3` en lugar de `33.333333333333336` |
| `return tasas` | **Entrega** el resultado. Sin esta línea, la función devuelve `None` |

**Seguimiento con las 4 reservas de la tarjeta** (4.3 a 4.7: web no, web **sí**, directo no, web no). Cada reserva es una vuelta del `for`:

1. Reserva 1 (web, no): `total = {"web": 1}`, `canceladas = {}`.
2. Reserva 2 (web, **sí**): `total = {"web": 2}`, `canceladas = {"web": 1}`.
3. Reserva 3 (directo, no): `total = {"web": 2, "directo": 1}`, `canceladas` igual.
4. Reserva 4 (web, no): `total = {"web": 3, "directo": 1}`, `canceladas` igual.

Después, el segundo `for`:

- `web` → 100 × 1 ÷ 3 = **33.3**.
- `directo` → 100 × **0** ÷ 1 = **0.0** (no está en `canceladas`: `.get` da `0`).
- Resultado: `{"web": 33.3, "directo": 0.0}`.

**Por qué `.get(canal, 0)` y no `canceladas[canal]`**

- `agencia` no tiene ninguna cancelada, así que **no está** en `canceladas`.
- Pedirlo con corchetes da `KeyError: 'agencia'`.
- Con `.get(canal, 0)` se dice «lo que lleve, o `0` si todavía no está».

### Paso 5 · Probar la tasa

**5.1 · A mano, con una sola línea** (en la terminal, dentro de la carpeta del reto; copiadla entera y pulsad Intro):

```
python -c "from reservas_demo import RESERVAS; from kpis import tasa_cancelacion_por_canal; print(tasa_cancelacion_por_canal(RESERVAS))"
```

✅ Sale `{'directo': 33.3, 'agencia': 0.0, 'web_intermediaria': 66.7}`.

**5.2 · La prueba:** `python test_kpis.py 1`.

- Las **dos pruebas de la tasa** salen `[OK]` en verde.
- El resumen pasa de `0 de 4` a `2 de 4`.
- No ejecutéis `python kpis.py` solo ni el botón ▶: ese fichero necesita datos y no enseña nada.

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

**La idea**

- Hacer una lista con lo que ingresa cada reserva **no cancelada** (`noches × precio_noche`).
- Calcular su media.
- Una reserva cancelada no deja dinero.
- Los pasos 6.1 y 6.2 son a mano; el código es **6.4 a 6.6**.

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

Se copia igual que la anterior: **función entera, de `def` a `raise`, pegada encima**, y Ctrl+S.

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

**Seguimiento**

- Con las 3 reservas de la tarjeta (200 €, 200 € y 120 €): 520 ÷ 3 = **173.33**.
- Con las 8 reservas de ejemplo: las no canceladas son 5 y el cajón queda `[200.0, 200.0, 120.0, 180.0, 210.0]`.
- Suman 910 y 910 ÷ 5 = **182.0**.

### Paso 7 · Probar el ingreso medio

**7.1 · A mano, con una línea** (en la terminal, dentro de la carpeta del reto):

```
python -c "from reservas_demo import RESERVAS; from kpis import ingreso_medio_por_reserva; print(ingreso_medio_por_reserva(RESERVAS))"
```

✅ Sale **`182.0`**.

**7.2 · La prueba:** `python test_kpis.py 1` → `test_ingreso_medio…` en verde (**`3 de 4`**).

**Si os sale otra cosa:**

| Os sale | Probablemente |
|---|---|
| `208.75` | Estáis sumando también las **canceladas** (1670 € entre 8): falta el `if` o está al revés |
| `113.75` | Dividís entre las 8 reservas en lugar de entre las 5 confirmadas: usad `len(ingresos)` |
| `ZeroDivisionError` con una lista vacía | Falta el `if not ingresos: return 0.0` |
| `None` | Falta el `return` del final |
| `NameError: name 'ingresos' is not defined` | Falta la primera línea, `ingresos = []` |

### Paso 8 · `ocupacion_proxy`

**La idea**

- Qué parte de las «noches posibles» (días del periodo × habitaciones) están ocupadas.
- La hace **el docente en pantalla** (8.2).
- Vosotros la copiáis (8.3) y **explicáis una línea con vuestras palabras** (8.5).

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

**Seguimiento con el dedo** (8 reservas, 5 habitaciones)

- Del 1 al 20 de enero hay **20 días** (19 de diferencia + 1).
- Las noches no canceladas son 2 + 4 + 1 + 2 + 3 = **12**.
- Entonces 100 × 12 ÷ (20 × 5) = **12.0**.

**Por qué es un «proxy»**

- El fichero no dice cuántas habitaciones tiene el hotel de verdad.
- Cada reserva cuenta sus noches el día de la llegada.
- Es una **medida aproximada**, útil para comparar, no una ocupación exacta.

### Paso 9 · Todas las pruebas

- **9.1:** `python test_kpis.py 1` termina con **`4 de 4 pruebas superadas`**, en verde.
- **9.2:** a mano, con una línea, da **`12.0`**:

```
python -c "from reservas_demo import RESERVAS; from kpis import ocupacion_proxy; print(ocupacion_proxy(RESERVAS, 5))"
```

| Os sale | Probablemente |
|---|---|
| Ocupación `12.6` | Falta el `+ 1` en los días: usáis 19 en vez de 20 |
| Ocupación `22.0` | Contáis también las noches de las canceladas (22 en vez de 12) |
| `ZeroDivisionError` con capacidad 0 | Falta la primera comprobación (`capacidad_habitaciones <= 0`) |
| `TypeError` al restar fechas | Estáis restando textos y no fechas: en las 8 reservas de ejemplo ya son fechas; en el CSV las convierte la misión 4 |

### Para explicárselo a vuestra pareja

Elegid una:

1. En la tasa de cancelación, ¿qué pasaría si usarais `canceladas[canal]` en lugar de `canceladas.get(canal, 0)`? ¿Con qué canal?
2. La tasa cuenta las reservas canceladas y las que no, pero el ingreso medio solo cuenta las no canceladas. ¿Por qué?
3. ¿Qué diferencia hay entre `print(tasas)` y `return tasas`? ¿Cuál necesita la prueba?

## Misión 4 · Leer el CSV

> **Para contrastar**, cuando hayáis terminado el paso o agotado las pistas de la [tarjeta de la misión 4](../1_Trabajar/tarjetas/tarjeta_4_ficheros.md). **Tiene los mismos números de paso que la tarjeta** (4.1, 4.2… 5.4…): buscad el vuestro. Primero intentadlo; después de mirarlo, cerradlo y volved a escribirlo sin mirar. Lo que copiéis, tenéis que saber explicarlo.

**El ejemplo (`mini.csv`)**, igual que en la tarjeta. La fila 1 es la cabecera:

```
fecha_llegada,noches,precio_noche,canal,cancelada
2025-01-01,2,100.0,directo,0               ← fila 2: buena
2025-01-03,3,,agencia,0                    ← fila 3: mala (falta el precio)
2025-01-05,0,50.0,web_intermediaria,1      ← fila 4: mala (0 noches)
```

### Paso 4 · `_convertir_fila`

**Cómo copiarla sin errores de sangría:** en `kpis.py`, seleccionad la función entera (desde `def` hasta la línea `raise NotImplementedError(...)`, incluida) y pegad la de abajo encima. Guardad con Ctrl+S.

```python
def _convertir_fila(fila):
    """Convierte una fila de textos a tipos Python. Lanza ValueError si no es válida."""
    noches = int(fila["noches"])
    precio = float(fila["precio_noche"])
    cancelada = int(fila["cancelada"])
    fecha = date.fromisoformat(fila["fecha_llegada"])
    canal = fila["canal"].strip()

    if canal == "":
        raise ValueError("canal vacío")
    if noches < 1:
        raise ValueError("noches debe ser >= 1")
    if precio <= 0:
        raise ValueError("precio_noche debe ser > 0")
    if cancelada not in (0, 1):
        raise ValueError("cancelada debe ser 0 o 1")

    return {"fecha_llegada": fecha, "noches": noches, "precio_noche": precio,
            "canal": canal, "cancelada": cancelada}
```

| Paso | Línea | Qué hace, con palabras normales |
|---|---|---|
| **4.3** | `noches = int(fila["noches"])` | Coge el texto `"2"` y lo convierte en el **número** 2 |
| **4.4** | `precio = float(fila["precio_noche"])` | `"100.0"` → 100.0. Con el precio vacío (fila 3), `float("")` da `ValueError` **solo** |
| **4.4** | `cancelada = int(fila["cancelada"])` | `"0"` → 0 |
| **4.4** | `fecha = date.fromisoformat(fila["fecha_llegada"])` | `"2025-01-01"` → una **fecha**. Si el texto no es una fecha, da `ValueError` |
| **4.5** | `canal = fila["canal"].strip()` | El canal, **sin espacios** por delante ni por detrás |
| **4.6** | `if canal == "":` + `raise ValueError(...)` | Canal vacío: **para** con ese mensaje |
| **4.6** | `if noches < 1:` + `raise ValueError(...)` | Menos de una noche (fila 4): para. `int("0")` funciona, pero 0 noches no tiene sentido |
| **4.6** | `if precio <= 0:` + `raise ValueError(...)` | Precio de 0 o negativo: para |
| **4.6** | `if cancelada not in (0, 1):` + `raise ValueError(...)` | `cancelada` solo puede ser 0 o 1 |
| **4.7** | `return {...}` | **Entrega** un diccionario con los valores ya convertidos |

**Seguimiento con las 3 filas:**

| Fila | Qué pasa | Resultado |
|---|---|---|
| 2 | Se convierte todo y pasa las 4 comprobaciones | Devuelve el diccionario con los tipos buenos |
| 3 | `float("")` falla en 4.4 | `ValueError: could not convert string to float: ''` |
| 4 | Se convierte bien, pero `noches < 1` | `ValueError: noches debe ser >= 1` |

**Probadla** (una línea, en la terminal, dentro de la carpeta del reto):

```
python -c "from kpis import _convertir_fila; print(_convertir_fila({'fecha_llegada': '2025-01-01', 'noches': '2', 'precio_noche': '100.0', 'canal': 'directo', 'cancelada': '0'}))"
```

✅ `{'fecha_llegada': datetime.date(2025, 1, 1), 'noches': 2, 'precio_noche': 100.0, 'canal': 'directo', 'cancelada': 0}`. Con `'noches': '0'`: ✅ `ValueError: noches debe ser >= 1`.

| Os sale | Probablemente |
|---|---|
| `'noches': '2'` (con comillas) | Falta el `int(...)`: se devuelve el texto (4.3) |
| `'fecha_llegada': '2025-01-01'` (con comillas) | Falta `date.fromisoformat(...)` (4.4) |
| `KeyError: 'noches'` | Clave mal escrita: tiene que ser exactamente `"noches"` |
| `NameError: name 'date' is not defined` | Falta `from datetime import date`; viene en la plantilla, no lo borréis |
| `None` | Falta el `return` (4.7) |
| `NotImplementedError` | Queda la línea `raise NotImplementedError(...)` (4.2) |
| `IndentationError` | Líneas con más o menos espacios que sus vecinas, o fichero sin guardar (4.8) |
| `kpis.py: error: the following arguments are required: entrada, salida` | Habéis pulsado el botón ▶ (Run) de VS Code: ejecuta `kpis.py` sin datos. No es un fallo: probad con las líneas `python -c "..."` de la terminal |

### Paso 5 · `leer_reservas`

**Cómo copiarla:** igual que la anterior: función entera, de `def` a `raise`, pegada encima (triple clic en la línea `raise NotImplementedError(...)` para seleccionarla entera). Cada nivel (4 espacios, o un Tab) **más a la derecha** significa «dentro de» lo de arriba. **Niveles de cada línea** (el `def` es el nivel 0):

| Nivel | Líneas |
|---|---|
| 1 | `try:` · `except FileNotFoundError:` |
| 2 | `with open(...) as f:` · el `raise FileNotFoundError(...)` |
| 3 | `lector = …` · `faltan = []` · `for columna in …:` · `if faltan:` · `reservas = []` · `avisos = []` · `for n, fila in …:` · `return reservas, avisos` |
| 4 | `if columna not in …:` · `raise ValueError(...)` · `try:` · `except ValueError as error:` |
| 5 | `faltan.append(columna)` · `reservas.append(...)` · `avisos.append(...)` |

```python
def leer_reservas(ruta):
    """Lee el CSV y devuelve (reservas, avisos)."""
    try:
        with open(ruta, newline="", encoding="utf8") as f:
            lector = csv.DictReader(f)

            faltan = []                                            # 5.4
            for columna in COLUMNAS_OBLIGATORIAS:
                if columna not in lector.fieldnames:
                    faltan.append(columna)
            if faltan:
                raise ValueError(f"Faltan columnas obligatorias: {faltan}")

            reservas = []                                          # 5.5
            avisos = []

            for n, fila in enumerate(lector, start=2):             # 5.6
                try:
                    reservas.append(_convertir_fila(fila))
                except ValueError as error:
                    avisos.append(f"Fila {n} descartada: {error}")

            return reservas, avisos                                # 5.7
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encuentra el fichero: {ruta}")   # 5.8
```

(Los `# 5.x` son solo para localizar el paso: no hace falta escribirlos.)

| Paso | Línea | Qué hace, con palabras normales |
|---|---|---|
| **5.3** | `try:` | «Intenta todo lo de abajo» |
| **5.3** | `with open(ruta, newline="", encoding="utf8") as f:` | Abre el fichero (`utf8` para que las tildes salgan bien) y **lo cierra solo** al terminar |
| **5.3** | `lector = csv.DictReader(f)` | Un lector que entrega cada fila como diccionario: `fila["noches"]` |
| **5.4** | `faltan = []` | Una lista vacía: aquí se apuntan las columnas que falten |
| **5.4** | `for columna in COLUMNAS_OBLIGATORIAS:` + `if columna not in lector.fieldnames:` + `faltan.append(columna)` | Por cada columna obligatoria, si **no está** en la cabecera, se apunta |
| **5.4** | `if faltan:` + `raise ValueError(...)` | Si falta alguna, **para** con un mensaje que las nombra |
| **5.5** | `reservas = []` y `avisos = []` | Dos listas vacías: las buenas y los avisos |
| **5.6** | `for n, fila in enumerate(lector, start=2):` | Coge las filas una a una; `n` es el **número de fila del fichero** (empieza en 2: la 1 es la cabecera) |
| **5.6** | `try:` + `reservas.append(_convertir_fila(fila))` | Intenta convertir la fila; si va bien, **la añade a las buenas** |
| **5.6** | `except ValueError as error:` | Si `_convertir_fila` ha dado `ValueError`… |
| **5.6** | `avisos.append(f"Fila {n} descartada: {error}")` | …apunta un aviso con el número de fila y el motivo, **y sigue** con la siguiente |
| **5.7** | `return reservas, avisos` | **Entrega las dos listas a la vez** |
| **5.8** | `except FileNotFoundError:` + `raise FileNotFoundError(f"...{ruta}")` | Si el fichero **no existe**, para con un mensaje claro que **incluye el nombre** |

**Seguimiento con `mini.csv`:** la fila 2 entra en `reservas`; la fila 3 da `ValueError` → aviso `Fila 3 descartada: …`; la fila 4 da `ValueError` → aviso `Fila 4 descartada: noches debe ser >= 1`. Resultado: **1 reserva y 2 avisos**.

**Probadla** (una línea, entera, en la terminal). **Antes, guardad con Ctrl+S** (si la pestaña tiene un punto ●, no está guardado y sale `NotImplementedError`).

**5.10 · Con el fichero real:**

```
python -c "from kpis import leer_reservas; reservas, avisos = leer_reservas('reservas_turisdata.csv'); print(len(reservas), len(avisos))"
```

✅ `6000 0`.

**5.12 · Con `mini.csv`** (5.11: se crea desde el Explorador de VS Code con el icono «Nuevo archivo»; si usáis el menú, elegid «Archivo de texto»):

```
python -c "from kpis import leer_reservas; reservas, avisos = leer_reservas('mini.csv'); print(len(reservas), avisos)"
```

✅
```
1 ["Fila 3 descartada: could not convert string to float: ''", 'Fila 4 descartada: noches debe ser >= 1']
```

El motivo de la fila 3 lo pone Python y puede variar; lo que tiene que coincidir es el **número de fila** y **un aviso por cada fila descartada**.

Con otros ficheros **tiene que parar con un error** (no devolver avisos):

| Fichero | ✅ Mensaje esperado |
|---|---|
| Uno que no existe (`'nada.csv'`) | `FileNotFoundError: No se encuentra el fichero: nada.csv` |
| `mini.csv` sin la columna `cancelada` | `ValueError: Faltan columnas obligatorias: ['cancelada']` |

| Os sale | Probablemente |
|---|---|
| Avisos de «Fila 2» y «Fila 3» | Contáis desde 1: falta `start=2` (5.6) |
| 2 reservas válidas (entra la de 0 noches) | Falta `if noches < 1:` en `_convertir_fila` (4.6) |
| 1 reserva válida pero `avisos` vacío | La fila mala se descarta **en silencio**: falta `avisos.append(...)` en el `except` (5.6) |
| El programa se rompe con `ValueError` en la fila 3 | Falta el `try` / `except` dentro del `for` (5.6) |
| `TypeError: list indices must be integers or slices, not str` | La función devuelve **dos** cosas y las guardáis en una variable: `reservas, avisos = leer_reservas(...)` |
| Las tildes salen rotas | Falta `encoding="utf8"` (5.3) |
| `NotImplementedError` aunque ya lo habéis escrito | El fichero **no está guardado** (punto ● en la pestaña): Python lee el guardado | Ctrl+S y repetid la línea |
| `IndentationError` | Falta un nivel de sangría, o fichero sin guardar. Mirad el esqueleto: `for` y `try` a 12, `except ValueError` a 16 |

### Paso 6 · Pruebas

`python test_kpis.py 2` pasa de **`1 de 8`** (todo en rojo, salvo una prueba opcional que se omite) a **`7 de 8 pruebas superadas`**. Solo queda en rojo `test_exportar_json_y_main`, de la misión 5. Si no hicisteis la misión 3, `test_datos_reales…` también falla y salen **`6 de 8`**.

### Para explicárselo a vuestra pareja

Elegid una:

1. ¿Por qué es mejor descartar la fila mala y apuntarla en `avisos` que parar el programa? ¿Y por qué no descartarla sin decir nada?
2. ¿Por qué `_convertir_fila` comprueba `noches < 1` si `int("0")` ya funciona?
3. ¿Qué dos cosas devuelve `leer_reservas` y cómo se recogen?

## Misión 5 · Guardar y entregar

<h2 align="center">Guardar el JSON, ponerlo en marcha con un comando y entregar</h2>

**Cómo usarlo**

- Para **contrastar**, cuando hayáis terminado el paso o agotado las pistas de la [tarjeta de la misión 5](../1_Trabajar/tarjetas/tarjeta_5_salida.md).
- Tiene los **mismos números de paso** que la tarjeta (2.1, 3.4…, 5.1…): buscad el vuestro.
- **Primero intentadlo.** Después de mirarlo, cerradlo y volved a escribirlo sin mirar.
- Lo que copiéis, tenéis que saber explicarlo.

### Paso 2 · `exportar_json`

**Cómo copiarla sin errores de sangría**

- En `kpis.py`, seleccionad la función entera: desde `def` hasta la línea `raise NotImplementedError(...)`, incluida.
- Pegad la de abajo encima.
- Guardad con Ctrl+S.

```python
def exportar_json(datos, ruta):
    """Guarda `datos` en un fichero JSON legible."""
    with open(ruta, "w", encoding="utf8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
```

| Paso | Línea | Qué hace, con palabras normales |
|---|---|---|
| **2.3** | `with open(ruta, "w", encoding="utf8") as f:` | Abre el fichero `ruta` **para escribir** (`"w"`; si existe, lo sustituye) y **lo cierra solo** al terminar. `utf8` para las tildes |
| **2.4** | `json.dump(datos, f, ensure_ascii=False, indent=2)` | Escribe `datos` en el fichero como JSON. `ensure_ascii=False` deja las tildes como son; `indent=2` lo sangra para que se lea bien |

**Probadla** (una línea, en la terminal, dentro de la carpeta del reto):

```
python -c "from kpis import exportar_json; exportar_json({'canal': 'ocupación'}, 'prueba.json')"
```

✅ `prueba.json` contiene:

```
{
  "canal": "ocupación"
}
```

| Os sale | Probablemente |
|---|---|
| `"ocupación"` | Falta `ensure_ascii=False` |
| Todo el JSON en una sola línea | Falta `indent=2` |
| `TypeError: Object of type date is not JSON serializable` | Estáis guardando una fecha: `exportar_json` solo guarda lo que le llega (números, textos, listas, diccionarios) |
| `PermissionError` o no aparece el fichero | Estáis en otra carpeta, o el fichero está abierto en otro programa |
| `NotImplementedError` | Falta guardar con Ctrl+S, o queda la línea `raise NotImplementedError(...)` |

### Paso 3 · `main`

**Cómo copiarla**

- Igual que las anteriores: función entera, de `def` a `raise`, pegada encima (triple clic en la línea `raise NotImplementedError(...)` para seleccionarla entera).
- Incluye las líneas del `parser`, que ya venían escritas en la plantilla: no las cambiéis.
- **Las dos últimas líneas del fichero** (`if __name__ == "__main__":` y `sys.exit(main())`) **se quedan como están**: son las que arrancan `main` al escribir `python kpis.py …`. No hay que copiarlas ni tocarlas.

```python
def main(argumentos=None):
    """Punto de entrada: devuelve 0 si todo va bien y 1 si hay un error."""
    parser = argparse.ArgumentParser(description="KPIs de reservas de TurisData")
    parser.add_argument("entrada", help="CSV de reservas")
    parser.add_argument("salida", help="JSON de salida")
    parser.add_argument("--capacidad", type=int, default=40, help="habitaciones disponibles (proxy de ocupación)")
    args = parser.parse_args(argumentos)
    try:
        reservas, avisos = leer_reservas(args.entrada)                                       # 3.4
        kpis = calcular_kpis(reservas, args.capacidad)                                       # 3.5
        kpis["calidad"] = {"filas_validas": len(reservas), "filas_descartadas": len(avisos),
                           "avisos": avisos[:20]}                                            # 3.6
        exportar_json(kpis, args.salida)                                                     # 3.7
    except (FileNotFoundError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)                                            # 3.8
        return 1
    print(f"OK: {len(reservas)} reservas analizadas, {len(avisos)} descartadas -> {args.salida}")   # 3.9
    return 0
```

**Niveles de cada línea** (el `def` es el nivel 0):

| Nivel | Líneas |
|---|---|
| 0 | `def main(...)` · `if __name__ == "__main__":` (las dos últimas líneas del fichero) |
| 1 | Las del `parser` y `args` · `try:` · `except …:` · el `print(f"OK…")` final · `return 0` · `sys.exit(main())` (dentro del `if __name__`) |
| 2 | Las cuatro del `try` (3.4 a 3.7) · el `print(…ERROR…)` y `return 1` (dentro del `except`) |

| Paso | Línea | Qué hace, con palabras normales |
|---|---|---|
| — | `parser … args = parser.parse_args(argumentos)` | Ya venía hecho: lee lo que se escribe tras `python kpis.py` y lo deja en `args.entrada`, `args.salida` y `args.capacidad` |
| — | `try:` | «Intenta todo lo de abajo; si falla de cierta manera, salta al `except`» |
| **3.4** | `reservas, avisos = leer_reservas(args.entrada)` | Lee el CSV. Devuelve **dos cosas**, que se recogen en dos variables |
| **3.5** | `kpis = calcular_kpis(reservas, args.capacidad)` | Calcula los tres KPI (ya venía hecha) y los deja en un diccionario |
| **3.6** | `kpis["calidad"] = {...}` | **Añade** una clave nueva al diccionario: cuántas filas buenas, cuántas descartadas y los avisos (solo los 20 primeros: `avisos[:20]`) |
| **3.7** | `exportar_json(kpis, args.salida)` | Guarda el diccionario en el fichero JSON |
| **3.8** | `except (FileNotFoundError, ValueError) as error:` | Si `leer_reservas` ha parado por fichero inexistente o columna que falta… |
| **3.8** | `print(f"ERROR: {error}", file=sys.stderr)` | …escribe el mensaje **por la salida de errores** |
| **3.8** | `return 1` | …y termina con **código 1** (mal) |
| **3.9** | `print(f"OK: …")` y `return 0` | Si no ha habido error, escribe el mensaje de éxito y termina con **código 0** (bien) |

**Seguimiento con el fichero real:** `leer_reservas` devuelve 6000 reservas y 0 avisos → `calcular_kpis` calcula → `kpis["calidad"]` dice 6000 válidas, 0 descartadas, `[]` → `exportar_json` guarda → imprime `OK: 6000 reservas analizadas, 0 descartadas -> salida.json` → devuelve 0.

| Os sale | Probablemente |
|---|---|
| `Traceback` rojo en vez de `ERROR: …` | El `except` no recoge ese tipo de error (3.8) |
| `ERROR: …` pero el código de salida es 0 | Falta el `return 1` (3.8) |
| `OK: …` pero no aparece `salida.json` | Falta `exportar_json(kpis, args.salida)` (3.7) |
| `KeyError: 'calidad'` en una prueba | Falta añadir la clave `"calidad"` (3.6) |
| La ocupación no cambia al cambiar `--capacidad` | Hay un `40` escrito a mano en lugar de `args.capacidad` (3.5) |
| `IndentationError` | Falta o sobra un nivel: mirad la tabla de niveles |
| `kpis.py: error: the following arguments are required…` | Habéis pulsado ▶ (Run) o habéis escrito `python kpis.py` sin los dos ficheros |

### Paso 4 · Probar el programa entero

**4.1** · `python kpis.py reservas_turisdata.csv salida.json --capacidad 40`

✅ `OK: 6000 reservas analizadas, 0 descartadas -> salida.json`

**4.2** · `salida.json` tiene que ser:

```json
{
  "reservas_analizadas": 6000,
  "ocupacion_proxy_pct": 42.0,
  "ingreso_medio_por_reserva": 576.04,
  "tasa_cancelacion_por_canal_pct": {
    "empresa": 43.3,
    "directo": 31.5,
    "web_intermediaria": 53.9,
    "agencia": 44.0
  },
  "calidad": {
    "filas_validas": 6000,
    "filas_descartadas": 0,
    "avisos": []
  }
}
```

**4.3** · `python test_kpis.py` ✅ **`12 de 12 pruebas superadas`** (con `kpis_pandas.py` ausente, la prueba opcional se omite y cuenta como superada).

| Os sale | Probablemente |
|---|---|
| Ocupación distinta de `42.0` | `ocupacion_proxy`: falta el `+ 1` en los días, se cuentan las canceladas, o la capacidad no es 40 |
| `ingreso_medio_por_reserva` distinto de `576.04` | `ingreso_medio_por_reserva`: se incluyen las canceladas |
| Una tasa distinta | `tasa_cancelacion_por_canal`: falta `round(..., 1)` o el `.get(canal, 0)` |
| Menos de 12 pruebas | Mirad cuál falla (en rojo) y a qué función se refiere |

**Comprobación cruzada.** La ocupación es inversamente proporcional a la capacidad. Con el CSV real:

| Orden | `ocupacion_proxy_pct` |
|---|---|
| `python kpis.py reservas_turisdata.csv salida.json --capacidad 20` | `84.0` |
| `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` | `42.0` |
| `python kpis.py reservas_turisdata.csv salida.json --capacidad 80` | `21.0` |

Si al doblar la capacidad la ocupación no se queda en la mitad, la capacidad no está llegando a `ocupacion_proxy`: revisad cómo pasáis `args.capacidad` (3.5).

### Paso 5 · Los tres errores a propósito

| Paso | Qué se ejecuta | ✅ Sale | Código de salida |
|---|---|---|---|
| **5.1** | `python kpis.py no_existe.csv salida.json` | `ERROR: No se encuentra el fichero: no_existe.csv` | `1` |
| **5.6** | `python kpis.py sin_col.csv salida_prueba.json` (con `precio` en vez de `precio_noche` en la primera línea) | `ERROR: Faltan columnas obligatorias: ['precio_noche']` | `1` |
| **5.10** | `python kpis.py con_error.csv salida_prueba.json` (con `abc` en la línea 5 y `0` noches en la línea 10) | `OK: 5998 reservas analizadas, 2 descartadas -> salida_prueba.json` | `0` |

**Comprobaciones de que el CSV editado está guardado** (5.5 y 5.9):

- `python -c "print('precio_noche' in open('sin_col.csv', encoding='utf8').readline())"` → `False`.
- `python -c "l = open('con_error.csv', encoding='utf8').read().split('\n'); print(',total,abc,' in l[4], ',114,0,2,1,' in l[9])"` → `True True`.

**5.11** · En `salida_prueba.json`, dentro de `"calidad"`:

```
"filas_validas": 5998,
"filas_descartadas": 2,
"avisos": [
  "Fila 5 descartada: could not convert string to float: 'abc'",
  "Fila 10 descartada: noches debe ser >= 1"
]
```

(El texto del primer aviso lo pone Python y puede variar; lo que tiene que coincidir son los **números de fila** y **uno por cada fila mala**.)

Otro caso: `python kpis.py reservas_turisdata.csv salida.json --capacidad 0` da ✅ `ERROR: La capacidad debe ser mayor que 0` y código `1`.

**El código de salida se mira justo después** de ejecutar:

- PowerShell: `echo $LASTEXITCODE`.
- cmd: `echo %errorlevel%`.
- Linux y Mac: `echo $?`.

| Os sale | Probablemente |
|---|---|
| En 5.10, `Traceback` en lugar de `OK` | Falta el `try` / `except ValueError` dentro del `for` de `leer_reservas` (misión 4, paso 5.6) |
| En 5.10, `OK: 6000 reservas…` | El CSV editado **no está guardado**, o los cambios no están en las líneas 5 y 10. Repetid la comprobación 5.9 |
| En 5.6, `OK` en lugar de `ERROR` | El CSV editado **no está guardado**, o habéis cambiado otra palabra. Repetid la comprobación 5.5 |
| `SyntaxError: invalid syntax` en la línea del `except` | Falta el `try:`, o el `except` no está **un nivel** a la derecha de `def` (mirad la tabla de niveles) |

### Para explicárselo a vuestra pareja

Elegid una:

1. ¿Por qué `main` recibe `argumentos=None` en vez de leer siempre lo que se escribe en la terminal?
2. ¿Por qué una fila mala termina con `OK` y código 0, y un fichero que no existe, con `ERROR` y código 1?
3. ¿Para qué sirve el código de salida si el mensaje ya dice si ha ido bien o mal?

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
