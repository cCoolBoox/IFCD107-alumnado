# Misión 2 · Decidir y repetir

<h2 align="center">Contar con <code>if</code> y <code>for</code></h2>

| | |
|---|---|
| ⏱ **Cuándo** | Martes · 50 min |
| 👥 **Cómo** | Piloto y copiloto (cambiad de papel en cada paso) |
| 🧰 **Usáis** | 🌐 el navegador (el curso) · 📄 `mision_2_decidir.py` · 💻 la terminal (dentro de la carpeta del reto) |
| 🏁 **Al terminar** | «✅ ¡Misión 2 superada!» en la terminal |

**Esta tarjeta tiene dos partes:**

- [1 · Guía paso a paso](#1--guía-paso-a-paso): solo lo que hay que hacer.
- [2 · Explicaciones](#2--explicaciones): el porqué de cada cosa, para cuando lo necesitéis.
- Si queréis, seguid solo la parte 1.

← [Volver al índice de misiones](../README.md)

---

# 1 · Guía paso a paso

**Qué vais a hacer**

- Escribir **cuatro bucles** (`for`) con su decisión (`if`) dentro de `mision_2_decidir.py`.
- Con ellos contáis: las reservas canceladas, las noches, las reservas por canal y una lista.
- Es **la base de todo el reto**: en la misión 3 meteréis estos contadores dentro de funciones.

**Cómo se sigue**

- De arriba abajo, **un número cada vez**.
- Cada paso termina en ✅: lo que tiene que salir.
- Si no sale, no sigáis: mirad la parte 2.

**Dos reglas que evitan perderse**

1. **Los espacios del principio (la sangría)**
   - Un **nivel** son 4 espacios, o una pulsación de **Tab**.
   - Una línea que acaba en `:` abre un nivel nuevo: la siguiente va **un nivel más a la derecha**.
   - Al pulsar Intro después de un `:`, VS Code suele sangrar solo. Si no, pulsad **Tab**.
   - Si una línea queda de más a la derecha: **Shift+Tab**. De menos: **Tab**.
2. **Guardar antes de probar**
   - Pulsad **Ctrl+S**.
   - Mirad que la pestaña **no tenga un punto ●** junto al nombre.
   - Python lee el fichero **guardado**, no el que veis en pantalla.

## Parte A · Aprender (25 min)

| Paso | Qué hacéis | Min | ✅ Terminado cuando |
|---|---|---|---|
| **1** | Curso: [`elif`](https://www.curso.soultechlabs.io/basico/#elif), ejercicios 1 y 2 | 10 | Los dos en verde |
| **2** | Curso: [`for`](https://www.curso.soultechlabs.io/basico/#for), los 3 ejercicios | 15 | Los tres en verde |

## Parte B · Construir (25 min)

Piloto y copiloto **cambian de papel en cada paso**. Trabajáis con las 8 reservas de ejemplo ([`reservas_demo.py`](../reto_herramientas/reservas_demo.py)).

### Paso 3 · Abrir el fichero y ver el punto de partida (2 min)

| # | Qué hacéis |
|---|---|
| **3.1** | Abrid [`mision_2_decidir.py`](../reto_herramientas/mision_2_decidir.py) en VS Code. |
| **3.2** | Mirad los **cuatro apartados**, `# 2.1`, `# 2.2`, `# 2.3` y `# 2.4`. Cada uno tiene una variable ya escrita (`canceladas = 0`, …) y una línea `# TODO`: ahí vais a escribir. |
| **3.3** | Bajad hasta la línea `NO TOCAR: comprobación automática`. **Lo de debajo no se toca.** |
| **3.4** | En la terminal, dentro de la carpeta del reto: `python mision_2_decidir.py` |

✅ Sale `Misión 2: 0 de 4 apartados bien. Te faltan:` y cuatro líneas con ✗ (una por apartado). Es lo normal: todavía no hay nada escrito.

### Paso 4 · Apartado 2.1: contar las canceladas (5 min)

| # | Qué hacéis |
|---|---|
| **4.1** | Buscad `# 2.1` y, debajo de `canceladas = 0`, la línea que empieza por `# TODO`. |
| **4.2** | Borrad **solo** esa línea `# TODO`. |
| **4.3** | En su lugar, **al borde izquierdo** (alineada con `canceladas = 0`), escribid: `for reserva in RESERVAS:` y pulsad Intro. |
| **4.4** | **Un nivel** a la derecha (4 espacios), escribid: `if reserva["cancelada"] == 1:` y pulsad Intro. |
| **4.5** | **Dos niveles** a la derecha (8 espacios), escribid: `canceladas = canceladas + 1` |
| **4.6** | Guardad con **Ctrl+S** (sin ● en la pestaña) y ejecutad: `python mision_2_decidir.py` |

**Así tiene que quedar** (los niveles son los de la derecha):

```
canceladas = 0                              ← nivel 0
for reserva in RESERVAS:                    ← nivel 0
    if reserva["cancelada"] == 1:           ← nivel 1
        canceladas = canceladas + 1         ← nivel 2
```

✅ Sale `Canceladas: 3` y `Misión 2: 1 de 4 apartados bien. Te faltan:` (quedan 3 ✗).

### Paso 5 · Apartado 2.2: sumar las noches (5 min)

| # | Qué hacéis |
|---|---|
| **5.1** | Buscad `# 2.2` y, debajo de `noches_confirmadas = 0`, la línea `# TODO`. Borradla. |
| **5.2** | **Nivel 0**: `for reserva in RESERVAS:` y Intro. |
| **5.3** | **Nivel 1**: `if reserva["cancelada"] == 0:` y Intro. Ahora la condición es `== 0`: solo las reservas **no** canceladas. |
| **5.4** | **Nivel 2**: `noches_confirmadas = noches_confirmadas + reserva["noches"]` |
| **5.5** | **Ctrl+S** y ejecutad. |

```
noches_confirmadas = 0                                                    ← nivel 0
for reserva in RESERVAS:                                                  ← nivel 0
    if reserva["cancelada"] == 0:                                         ← nivel 1
        noches_confirmadas = noches_confirmadas + reserva["noches"]       ← nivel 2
```

✅ Sale `Noches confirmadas: 12` y `2 de 4 apartados bien`.

### Paso 6 · Apartado 2.3: contar por canal (6 min)

| # | Qué hacéis |
|---|---|
| **6.1** | Buscad `# 2.3` y, debajo de `por_canal = {}`, la línea `# TODO`. Borradla. |
| **6.2** | **Nivel 0**: `for reserva in RESERVAS:` y Intro. |
| **6.3** | **Nivel 1**: `canal = reserva["canal"]` y Intro. Guarda el canal de esta reserva en la variable `canal`. |
| **6.4** | **Nivel 1**: `por_canal[canal] = por_canal.get(canal, 0) + 1` |
| **6.5** | **Ctrl+S** y ejecutad. |

```
por_canal = {}                                                  ← nivel 0
for reserva in RESERVAS:                                        ← nivel 0
    canal = reserva["canal"]                                    ← nivel 1
    por_canal[canal] = por_canal.get(canal, 0) + 1              ← nivel 1
```

✅ Sale `Por canal: {'directo': 3, 'agencia': 2, 'web_intermediaria': 3}` y `3 de 4 apartados bien`.

### Paso 7 · Apartado 2.4: la lista de canales (7 min)

| # | Qué hacéis |
|---|---|
| **7.1** | Buscad `# 2.4` y, debajo de `largas = []`, la línea `# TODO`. Borradla. |
| **7.2** | **Nivel 0**: `for reserva in RESERVAS:` y Intro. |
| **7.3** | **Nivel 1**: `if reserva["cancelada"] == 0 and reserva["noches"] >= 3:` y Intro. Son **dos** condiciones unidas por `and`: se tienen que cumplir las dos. |
| **7.4** | **Nivel 2**: `largas.append(reserva["canal"])` |
| **7.5** | **Ctrl+S** y ejecutad. |

```
largas = []                                                         ← nivel 0
for reserva in RESERVAS:                                            ← nivel 0
    if reserva["cancelada"] == 0 and reserva["noches"] >= 3:        ← nivel 1
        largas.append(reserva["canal"])                             ← nivel 2
```

✅ Sale `Confirmadas de 3 noches o más: ['agencia', 'directo']` y **`✅ ¡Misión 2 superada!`**.

## ✅ Misión terminada cuando

- [ ] `python mision_2_decidir.py` termina con **«✅ ¡Misión 2 superada!»**.
- [ ] Los resultados son: **3 canceladas**, **12 noches** confirmadas, `{'directo': 3, 'agencia': 2, 'web_intermediaria': 3}` y `['agencia', 'directo']`.
- [ ] Cada persona sabe explicar con sus palabras qué hace **su** `for` y **su** `if`.

[Misión 3 · Funciones que calculan](tarjeta_3_funciones.md) →

---

# 2 · Explicaciones

*Para cuando una cosa no sale o queréis entender por qué se hace así. No hace falta leerlo para resolver la misión.*

## La idea: contar es siempre lo mismo

Pensad en cómo contaríais a mano las reservas canceladas de un montón de fichas.

| Pieza | En la vida real | En el código |
|---|---|---|
| **Marcador a cero** | Empezáis en 0 | `canceladas = 0` |
| **Bucle** | Cogéis las fichas **una a una** | `for reserva in RESERVAS:` |
| **Decisión** | Miráis si **esa** ficha está cancelada | `if reserva["cancelada"] == 1:` |
| **Sumar uno** | Solo entonces, apuntáis uno más | `canceladas = canceladas + 1` |

- **Contar** suma `1` cada vez. **Sumar** (las noches) suma el dato: `+ reserva["noches"]`.
- **Contar por grupos** (por canal) usa un diccionario: `por_canal.get(canal, 0) + 1` se lee «lo que llevo de ese canal, o `0` si todavía no lo he visto; le sumo 1».
- El primer paso de la misión 3 es meter esto dentro de una **función**.

## Seguimiento con el dedo: apartado 2.1

Tapad la tabla con una hoja y destapadla **fila a fila**: cada fila es **una vuelta** del `for`.

| Vuelta | `reserva["cancelada"]` | ¿`== 1`? | `canceladas` después |
|---|---|---|---|
| 1 | 0 | no | **0** |
| 2 | 1 | **sí** | **1** |
| 3 | 0 | no | 1 |
| 4 | 0 | no | 1 |
| 5 | 1 | **sí** | **2** |
| 6 | 0 | no | 2 |
| 7 | 0 | no | 2 |
| 8 | 1 | **sí** | **3** |

- Son **8 vueltas**, una por reserva; al acabar, `canceladas` vale **3**.
- El 2.2 es igual, pero con `== 0` y sumando las noches: acaba en **12**.

## Seguimiento con el dedo: apartado 2.3

Con las primeras vueltas, el diccionario va creciendo:

| Vuelta | `canal` | `por_canal.get(canal, 0)` | `por_canal` después |
|---|---|---|---|
| 1 | `directo` | 0 (todavía no está) | `{'directo': 1}` |
| 2 | `directo` | 1 | `{'directo': 2}` |
| 3 | `agencia` | 0 (todavía no está) | `{'directo': 2, 'agencia': 1}` |
| 4 | `agencia` | 1 | `{'directo': 2, 'agencia': 2}` |

- Las vueltas 5 a 8 siguen igual: acaba en `{'directo': 3, 'agencia': 2, 'web_intermediaria': 3}`.

## Las palabras de la misión

| Palabra | Qué significa |
|---|---|
| **Variable** | Una caja con nombre donde se guarda un dato: `canceladas = 0` |
| **`for reserva in RESERVAS:`** | «Para cada reserva de la lista, haz lo de abajo». En cada vuelta, `reserva` es **una** reserva |
| **`if`** | «Solo si se cumple esto, haz lo de abajo» |
| **`==`** | **Comparar**: «¿es igual?». Da sí o no |
| **`=`** | **Guardar**: mete un valor en una variable |
| **`and`** | «Y»: se tienen que cumplir **las dos** condiciones |
| **`canceladas = canceladas + 1`** | «El nuevo valor es el de antes más uno». Se puede escribir también `canceladas += 1` |
| **`.get(canal, 0)`** | Pide el valor de `canal` en el diccionario; si **todavía no está**, da `0` en vez de dar error |
| **`.append(x)`** | Añade `x` al final de una lista |
| **Nivel** | 4 espacios (o un Tab) más a la derecha: «está dentro de» la línea de arriba |

## Por qué se hace así

- **Los contadores empiezan en `0` y se crean antes del `for`.** Si se creasen dentro, volverían a 0 en cada vuelta.
- **El `if` está dentro del `for`.** Así se pregunta por **cada** reserva, no una sola vez.
- **El `+ 1` está dentro del `if`.** Sin el `if`, sumaría en **todas** las vueltas (saldrían las 8).
- **Se usa `.get(canal, 0)`** porque la primera vez que sale un canal todavía no está en el diccionario.
- **Los niveles importan.** Lo que está **más a la derecha** pertenece a la línea de arriba: el `if` es de dentro del `for`, y la suma, de dentro del `if`.
- **El orden de `largas`** es el de las reservas: la `agencia` (reserva 3) sale antes que el `directo` (reserva 7).

## Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| Sigue saliendo `0 de 4 apartados bien` aunque lo habéis escrito | El fichero **no está guardado** (punto ● en la pestaña) | **Ctrl+S** y ejecutad otra vez |
| `NameError: name 'canceladas' is not defined` | Falta crear el contador **antes** del `for`, o se ha borrado | Que quede `canceladas = 0` encima del bucle |
| `IndentationError` | Lo que va dentro del `for` o del `if` debe estar **más a la derecha**, y las líneas del mismo nivel, **igual** | Cuatro espacios por nivel; mirad la tabla «Así tiene que quedar» del paso |
| `SyntaxError` | Falta el `:` al final del `for` o del `if`, o hay un `=` donde va `==` | Mirad el final de cada línea y la comparación |
| `canceladas` sale 8 | Falta el `if`: se suma en todas las vueltas | Que el `+ 1` esté **dentro** del `if` (dos niveles) |
| `canceladas` sale 5 | Habéis puesto `== 0` en vez de `== 1`: cuenta las confirmadas | `1` = cancelada |
| `canceladas` sale 1 | Habéis escrito `canceladas = 1` en vez de `canceladas = canceladas + 1` | Sumad sobre lo que ya había |
| Cuenta de más al sumar noches (sale 22 o 10) | Falta el `if` (suma las 22), o comparáis con `== 1` (suma las 10 de las canceladas) | Solo `cancelada == 0` |
| `KeyError: 'directo'` | Habéis escrito `por_canal[canal] += 1` sin `.get`: el canal todavía no está | `por_canal[canal] = por_canal.get(canal, 0) + 1` |
| `largas` sale `['agencia']` | Habéis puesto `>` en vez de `>=` | «3 noches **o más**» es `>= 3` |
| `largas` sale con 7 canales | Habéis puesto `or` en vez de `and` | Las dos condiciones a la vez: `and` |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 2](../../3_Consultar/Solucionario_misiones.md), que tiene **los mismos pasos** (se publica al acabar la clase el martes). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |
