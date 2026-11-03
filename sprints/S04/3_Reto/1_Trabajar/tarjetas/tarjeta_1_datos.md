# Misión 1 · Datos en memoria

<h2 align="center">Leer y modificar una lista de reservas</h2>

| | |
|---|---|
| ⏱ **Cuándo** | Martes · 50 min |
| 👥 **Cómo** | Piloto y copiloto (cambiad de papel respecto a la misión 0) |
| 🧰 **Usáis** | 🌐 el navegador (curso y Taller) · 📄 `mision_1_datos.py` · 💻 la terminal |
| 🏁 **Al terminar** | «✅ ¡Misión 1 superada!» en la terminal |

**Esta tarjeta tiene dos partes:**

- [1 · Guía paso a paso](#1--guía-paso-a-paso): solo lo que hay que hacer.
- [2 · Explicaciones](#2--explicaciones): el porqué de cada cosa, para cuando lo necesitéis.
- Si queréis, seguid solo la parte 1.

← [Volver al índice de misiones](../README.md)

---

# 1 · Guía paso a paso

**Qué vais a hacer**

- Saber **cuántas** reservas hay.
- **Mirar** un dato de una reserva concreta.
- **Cambiarlo**.
- **Añadir** una reserva nueva.
- Es el «abecé» de lo que viene después: los KPI no son más que cálculos sobre esta lista.

**Cómo se sigue**

- De arriba abajo, **un número cada vez**.
- Cada paso termina en ✅: lo que tiene que salir.
- Si no sale, no sigáis: mirad la parte 2.

**Tres reglas que evitan perderse**

1. **Lo que escribís empieza pegado al borde izquierdo**
   - En este archivo **no hay espacios al principio** de ninguna línea nueva.
   - Si una línea sale con espacios delante, borradlos (**Shift+Tab**).
2. **Guardar antes de probar**
   - Pulsad **Ctrl+S**.
   - Mirad que la pestaña de `mision_1_datos.py` **no tenga un punto ●** junto al nombre.
   - Python lee el fichero **guardado**, no el que veis en pantalla.
3. **Probad después de cada apartado**, no al final. Así sabéis cuál falla.

## Parte A · Aprender (25 min)

| Paso | Qué hacéis | Min | ✅ Terminado cuando |
|---|---|---|---|
| **1** | Curso: [listas](https://www.curso.soultechlabs.io/basico/#list), ejercicios 1 y 2 | 15 | Los dos en verde |
| **2** | Curso: [diccionarios](https://www.curso.soultechlabs.io/basico/#dict), los 3 ejercicios | 10 | Los tres en verde |

## Parte B · Construir (25 min)

### Paso 3 · Abrir el archivo (3 min)

| # | Qué hacéis |
|---|---|
| **3.1** | En VS Code, abrid [`mision_1_datos.py`](../reto_herramientas/mision_1_datos.py). |
| **3.2** | En la terminal (dentro de la carpeta del reto), escribid `python mision_1_datos.py` y pulsad Intro. |

✅ Sale `Misión 1: 0 de 6 apartados bien` y la lista de lo que falta. **Es lo normal**: cada apartado que arregléis desaparece de la lista.

**Qué es un `TODO`**

- Es un aviso de «aquí falta algo».
- A veces hay que cambiar el `None` (significa «vacío»).
- A veces hay que escribir líneas nuevas.
- Cuando lo arregléis, **borrad también la palabra `# TODO`**.

### Paso 4 · Los seis apartados (22 min)

En cada apartado: **escribid → guardad con Ctrl+S → ejecutad `python mision_1_datos.py` → mirad el ✅**.

| # | Apartado del archivo | Qué hacéis | ✅ Sale |
|---|---|---|---|
| **4.1** | `# 1.1` | En `cantidad = None`, cambiad `None` por `len(…)` con **la lista de reservas** dentro del paréntesis. | `Cantidad al empezar: 3` y `1 de 6 apartados bien` |
| **4.2** | `# 1.2` | En `canal_primera = None`, cambiad `None` por **la primera reserva** (posición `0`) y, a continuación, la etiqueta `"canal"` entre corchetes. | `Canal de la primera: directo` y `2 de 6` |
| **4.3** | `# 1.3` | En `precio_ultima = None`, lo mismo, pero con **la última reserva** (posición `-1`) y la etiqueta `"precio_noche"`. | `Precio de la última: 60.0` y `3 de 6` |
| **4.4** | `# 1.4` | Debajo de la pista, **borrad** la línea `# TODO` y escribid: la primera reserva, su etiqueta `"cancelada"` y `= 1`. | `4 de 6` |
| **4.5** | `# 1.5` | Debajo de la pista, **borrad** la línea `# TODO` y escribid `reservas.append(…)` con **una reserva nueva** dentro del paréntesis: canal `"directo"`, `3` noches, `80.0` el precio, `0` cancelada. | `Ahora hay 4 reservas` y `5 de 6` |
| **4.6** | `# 1.6` | En `texto = None`, cambiad `None` por un `f"…"` con el mensaje de la pista, **sacando los datos de la segunda reserva** (posición `1`). | `La reserva 2 es del canal agencia: 4 noches a 50.0 euros` |

**Ayudas por apartado**

- **4.1:** `cantidad` vale **3** aunque luego añadáis una reserva: se cuenta **antes** de añadirla (el 4.5 va después).
- **4.2 y 4.3:** se lee de izquierda a derecha: «de la reserva número…, la etiqueta…» → `reservas[número]["etiqueta"]`.
- **4.4:** es una **asignación** con **un solo** `=`.
- **4.5:** el diccionario va entre llaves `{ }` y cada etiqueta lleva sus dos puntos: `"canal": "directo"`.
- **4.6:** dentro de las llaves del `f"…"`, las etiquetas van con **comillas simples** (`'canal'`).

### Paso 5 · Taller (10 min)

- Taller, [bloque 1](https://www.curso.soultechlabs.io/taller/#t-total): «El total de una reserva» y «Un mensaje con f-string».
- Es lo mismo que acabáis de hacer, montado con piezas.
- ✅ Los dos puzles montados.

## ✅ Misión terminada cuando

- [ ] `python mision_1_datos.py` termina con **«✅ ¡Misión 1 superada!»**.
- [ ] Ya no queda ningún `# TODO` en el archivo.

[Misión 2 · Decidir y repetir](tarjeta_2_decidir.md) →

---

# 2 · Explicaciones

*Para cuando una cosa no sale o queréis entender por qué se hace así. No hace falta leerlo para resolver la misión.*

## La idea en un minuto

- **Una reserva es una ficha con etiquetas** (un *diccionario*).
- **Muchas reservas son una caja de fichas** (una *lista*).

```python
reserva = {"canal": "directo", "noches": 2}   # una ficha con etiquetas
reservas = [reserva, otra_reserva]            # la caja de fichas
len(reservas)             # cuántas fichas hay
reservas[0]["canal"]      # de la PRIMERA (se cuenta desde 0), la etiqueta canal
reservas[-1]              # la ÚLTIMA
reserva["noches"] = 3     # cambia lo que pone en esa etiqueta
reservas.append({...})    # mete una ficha nueva al final de la caja
```

- `reservas[0]["canal"]` se lee de izquierda a derecha: «de la primera reserva, el canal».

## Qué pide cada apartado

| Apartado | Qué pide | En qué os fijáis |
|---|---|---|
| 1.1 | Guardar **cuántas reservas** hay | `len(...)` |
| 1.2 | El canal de la **primera** reserva | Posición `0` y etiqueta `"canal"` |
| 1.3 | El precio por noche de la **última** | El índice `-1` |
| 1.4 | **Cambiar** a 1 la cancelación de la primera | Una asignación con `=` |
| 1.5 | **Añadir** una reserva nueva al final | `append` con un diccionario completo |
| 1.6 | Un **mensaje** con datos de la segunda reserva | Un `f-string` (el de la misión 0) |

## Por qué se hace así

- **Se cuenta desde 0.** La primera reserva es la posición `0`; la última, `-1` (empezando por detrás). La segunda es la `1`.
- **`=` cambia, `==` pregunta.** Con `==` no da error pero tampoco cambia nada.
- **`append` solo añade al final**, y no devuelve nada: se escribe suelto, sin `=`.
- **`cantidad` se cuenta antes de añadir**, por eso vale 3 aunque al terminar haya 4 reservas.

## Las palabras de la misión

| Palabra | Qué significa |
|---|---|
| **Lista** | Una caja de cosas, en orden: `[a, b, c]` |
| **Diccionario** | Una ficha con etiquetas: `{"canal": "directo"}` |
| **Índice** | El número de posición: `0` la primera, `-1` la última |
| `len(x)` | Cuántas cosas hay en `x` |
| `None` | «Vacío»: todavía no hay nada |
| **`TODO`** | Aviso de «aquí falta algo» |

## Si os atascáis

| Qué sale | Por qué | Qué hacer |
|---|---|---|
| `KeyError: 'canl'` | La etiqueta está mal escrita o no existe | Copiad la etiqueta tal cual de la reserva de ejemplo |
| `IndexError: list index out of range` | Esa posición no existe en la lista | Recordad: la primera es `0` y la última `-1` |
| `TypeError` o el apartado sigue en la lista | Dejasteis el `None` o falta una coma o una llave | Releed la línea en voz alta, símbolo a símbolo |
| Un apartado que ya hicisteis sigue en rojo | El archivo **no está guardado** (punto ● en la pestaña) | **Ctrl+S** y ejecutad otra vez |
| `SyntaxError` en el 4.6 | Comillas dobles dentro de un `f"…"` con comillas dobles | Dentro de las llaves, usad comillas **simples** |
| `ModuleNotFoundError` | La terminal no está en la carpeta del reto | Abridla **dentro** de la carpeta descomprimida |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 1](../../3_Consultar/Solucionario_misiones.md), que tiene **los mismos pasos** (se publica al acabar la clase el martes). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |
