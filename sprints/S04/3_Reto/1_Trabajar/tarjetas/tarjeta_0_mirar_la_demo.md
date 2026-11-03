# Misión 0 · Mirar la demo

<h2 align="center">Entender el programa del cliente antes de escribir nada</h2>

| | |
|---|---|
| ⏱ **Cuándo** | Martes · 35 min |
| 👥 **Cómo** | Todo el equipo junto, una persona al teclado |
| 🧰 **Usáis** | 🌐 el navegador (el curso) · 📄 un archivo que **solo se lee**: `demo_cliente.py` · 💻 la terminal |
| 🏁 **Al terminar** | Cada persona responde, sin mirar el ordenador, las cinco preguntas del paso 6 |

**Esta tarjeta tiene dos partes:**

- [1 · Guía paso a paso](#1--guía-paso-a-paso): solo lo que hay que hacer.
- [2 · Explicaciones](#2--explicaciones): el porqué de cada cosa, para cuando lo necesitéis.
- Si queréis, seguid solo la parte 1.

← [Volver al índice de misiones](../README.md)

---

# 1 · Guía paso a paso

**Qué vais a hacer**

- **Entender** el programa que nos envía el cliente: una versión en pequeño de lo que vais a construir.
- Analiza **8 reservas** puestas a mano y escribe un resumen.
- **Todavía no se programa nada.**

**Cómo se sigue**

- De arriba abajo, **un número cada vez**.
- Cada paso termina en ✅: lo que tiene que salir.
- Si no sale, no sigáis: mirad la parte 2.

👀 **Antes de empezar, mirad adónde vamos:** la [demo interactiva del reto](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S04/3_Reto/1_Trabajar/S04_demo_reto.html) (se abre en el navegador, sin instalar nada) enseña la herramienta final funcionando. Volved a ella cuando queráis: en cada misión se ilumina la pieza que construís.

**Dos reglas de esta misión**

1. **No cambiéis nada** de `demo_cliente.py`: solo se lee y se ejecuta.
2. **La terminal tiene que estar dentro de la carpeta del reto.** Si no, no encuentra los archivos (mirad la parte 2).

## Parte A · Preparar (5 min)

### Paso 1 · Descargar (2 min)

| # | Qué hacéis |
|---|---|
| **1.1** | Descargad [`reto_herramientas.zip`](https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/sprints/S04/3_Reto/1_Trabajar/reto_herramientas.zip). |
| **1.2** | Descomprimidlo (clic derecho → *Extraer todo*). |
| **1.3** | Abrid la carpeta `reto_herramientas` que sale. |

✅ Veis `demo_cliente.py` dentro de la carpeta. (Dentro está **todo junto**: la plantilla, los archivos de las misiones y el CSV.)

### Paso 2 · Abrir VS Code y la terminal (3 min)

| # | Qué hacéis |
|---|---|
| **2.1** | Abrid VS Code. |
| **2.2** | Menú *File → Open Folder…* y elegid la carpeta `reto_herramientas`. |
| **2.3** | Menú *Terminal → New Terminal*. |
| **2.4** | En la terminal, escribid `python --version` y pulsad Intro. |

✅ Sale **3.11 o superior**. Si da error, escribid `python3 --version` y usad `python3` en lugar de `python` en **todo** el reto.

## Parte B · Mirar el programa (15 min)

### Paso 3 · Leer sin ejecutar (5 min)

| # | Qué hacéis |
|---|---|
| **3.1** | Abrid [`demo_cliente.py`](../reto_herramientas/demo_cliente.py) en VS Code. **No lo ejecutéis todavía.** |
| **3.2** | Buscad los **datos**: la línea que empieza por `from reservas_demo import RESERVAS`. Son 8 reservas ([`reservas_demo.py`](../reto_herramientas/reservas_demo.py)). |
| **3.3** | Buscad el **bucle**: la línea que empieza por `for reserva in RESERVAS:`. |
| **3.4** | Buscad la **decisión**: la línea que empieza por `if reserva["cancelada"] == 1:`. |
| **3.5** | Buscad el **mensaje**: las líneas que empiezan por `print(`. |
| **3.6** | Subrayad (con el rotulador o en vuestro cuaderno) lo que **no** entendáis. |
| **3.7** | Apuntad qué creéis que va a escribir el programa. |

✅ Tenéis apuntadas **una predicción** y **vuestras dudas**.

### Paso 4 · El docente lo comenta (5 min)

| # | Qué hacéis |
|---|---|
| **4.1** | Mirad la pantalla del aula: el docente proyecta el programa y lo comenta. |
| **4.2** | Preguntad lo que habéis subrayado. |

✅ Se han resuelto vuestras dudas.

### Paso 5 · Ejecutarlo (2 min)

| # | Qué hacéis |
|---|---|
| **5.1** | En la terminal (dentro de la carpeta), escribid `python demo_cliente.py` y pulsad Intro. |
| **5.2** | Comparad lo que sale con **vuestra predicción** del paso 3.7. |

✅ Sale **exactamente** esto:

```
=== Resumen semanal de reservas ===
Reservas analizadas: 8
Canceladas: 3 (37.5 %)
Ingreso medio por reserva confirmada: 182.00 €
  - directo: 3 reservas
  - agencia: 2 reservas
  - web_intermediaria: 3 reservas
```

### Paso 6 · Las cinco preguntas (3 min)

| # | Qué hacéis |
|---|---|
| **6.1** | **Cerrad el ordenador** o apartad la vista de la pantalla. |
| **6.2** | Cada persona responde, **con sus palabras**, las cinco preguntas de abajo. |

1. ¿Cuántas reservas analiza el programa y qué línea lo calcula?
2. ¿Por qué `canceladas` empieza en `0` y `por_canal` en `{}`?
3. Si la primera reserva pasara a estar cancelada (`"cancelada": 1`), ¿qué cifras del resumen cambiarían?
4. ¿Qué hace `:.1f` dentro de las llaves del `f-string`?
5. Si `RESERVAS` estuviera **vacía**, ¿qué error saldría y en qué línea?

**Para la pregunta 5, probadlo** (sin tocar `demo_cliente.py`):

| # | Qué hacéis |
|---|---|
| **6.3** | Copiad `demo_cliente.py` y llamad a la copia `demo_copia.py`. |
| **6.4** | En la **copia**, cambiad la línea `from reservas_demo import RESERVAS` por `RESERVAS = []`. |
| **6.5** | Guardad con **Ctrl+S** y ejecutad `python demo_copia.py`. |

✅ Sale un error en rojo. Apuntad **cómo se llama** y **en qué línea** está.

✅ Terminado cuando las cinco están respondidas y la 5 comprobada.

## Parte C · Aprender (15 min)

### Paso 7 · El curso

- `type()`: los 3 ejercicios. Curso: [`type()`](https://www.curso.soultechlabs.io/basico/#type).
- Formateo de textos: ejercicios 1 y 2 (el `f-string` y los dos decimales). Curso: [formateo](https://www.curso.soultechlabs.io/basico/#fmt).
- El docente hace el primero de cada lección en pantalla.
- ✅ Los cinco ejercicios en verde.

## ✅ Misión terminada cuando

- [ ] `python demo_cliente.py` escribe el resumen del paso 5 y coincide con vuestra predicción.
- [ ] Cada persona sabe responder, **sin mirar el ordenador**, las cinco preguntas del paso 6.
- [ ] Los cinco ejercicios del curso (paso 7) en verde.

[Misión 1 · Datos en memoria](tarjeta_1_datos.md) →

---

# 2 · Explicaciones

*Para cuando una cosa no sale o queréis entender por qué se hace así. No hace falta leerlo para resolver la misión.*

## La idea en un minuto

**Un programa de verdad son solo cuatro piezas.** Pensad en cómo revisaríais a mano un montón de fichas de papel:

| Pieza | En el reto | En la vida real sería… |
|---|---|---|
| **Datos** | La lista `RESERVAS` | El montón de fichas |
| **Bucle** (`for`) | `for reserva in RESERVAS:` | Coger las fichas una a una |
| **Decisión** (`if`) | `if reserva["cancelada"] == 1:` | Mirar si la ficha está cancelada |
| **Mensaje** (`print`) | El resumen con `f"…"` | Escribir el resultado al final |

- Todo lo que haréis en el reto es una variación de estas cuatro piezas.
- **No hace falta entender cada línea.** Lo que importa es ver las cuatro piezas.

## Las palabras de la misión

| Palabra | Qué significa |
|---|---|
| **CSV** | Una tabla guardada como texto: una fila por línea, valores separados por comas |
| **Lista** | Una caja de cosas, en orden: `[a, b, c]` |
| **Diccionario** | Una ficha con etiquetas: `{"canal": "directo"}` |
| **`for`** | Repite lo de dentro **una vez por cada** elemento de la lista |
| **`if` / `else`** | «Si pasa esto, haz esto; si no, haz esto otro» |
| **Acumulador** | Una variable que empieza en `0` (o `{}`) y el bucle va rellenando |
| **`f"…"` (f-string)** | Un texto con huecos `{ }` donde se meten valores. `:.1f` = un decimal |

## Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| `python` no se reconoce, o sale `Python 2…` | En algunos equipos el comando es otro | Probad `python3` y usadlo en todo el reto; si sigue sin funcionar, abrid **Anaconda Prompt** (ver la guía [Python en el ordenador del aula](../../../../../material/8.%20Python_en_el_ordenador_del_aula.md)) |
| `No such file or directory` o `ModuleNotFoundError: reservas_demo` | La terminal está en otra carpeta | Abrid la terminal **dentro** de la carpeta descomprimida (`ls` o `dir` debe mostrar `demo_cliente.py`) |
| No entendéis una línea | Es normal en el primer contacto | Subrayadla y preguntad al docente en el paso 4 |
| No hay Python en el aula | — | Usad Colab: subid los ficheros al panel izquierdo y poned `!` delante de cada comando |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 0](../../3_Consultar/Solucionario_misiones.md), que tiene **los mismos pasos** (se publica al acabar la clase el martes). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |
