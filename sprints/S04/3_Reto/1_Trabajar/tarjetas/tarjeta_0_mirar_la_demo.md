# Misión 0 · Mirar la demostración del cliente

> ⏱ **35 minutos** · 🅰️ Fase 1 · martes · 👥 Todo el equipo junto, una persona al teclado · [Volver al índice](../README.md)

## 🎯 Qué construís

Nada todavía. Esta misión es para **entender** el programa que nos envía el cliente: una versión en pequeño de lo que vais a construir (analiza 8 reservas puestas a mano y escribe un resumen). Si lo entendéis, el resto del reto es ir haciéndolo más grande y más robusto.

## 💡 La idea clave

**Un programa de verdad son solo cuatro piezas.** Pensad en cómo revisaríais a mano un montón de fichas de papel:

| Pieza | En el reto | En la vida real sería… |
|---|---|---|
| **Datos** | La lista `RESERVAS` | El montón de fichas |
| **Bucle** (`for`) | `for reserva in RESERVAS:` | Coger las fichas una a una |
| **Decisión** (`if`) | `if reserva["cancelada"] == 1:` | Mirar si la ficha está cancelada |
| **Mensaje** (`print`) | El resumen con `f"…"` | Escribir el resultado al final |

Todo lo que haréis en el reto es una variación de estas cuatro piezas.

## 🧰 Antes de tocar nada

1. **Preparad la carpeta de trabajo** *(5 min)*. Descargad [`reto_herramientas.zip`](https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/sprints/S04/3_Reto/1_Trabajar/reto_herramientas.zip) y descomprimidlo. Dentro está **todo junto**: la plantilla, los archivos de las misiones y el CSV `reservas_turisdata.csv`.
2. **Abrid la terminal en esa carpeta** *(5 min)*. En VS Code: *File → Open Folder…* (elegid la carpeta descomprimida) y *Terminal → New Terminal*. Si el aula no tuviera Python, usad Colab: subid los ficheros al panel izquierdo y poned `!` delante de cada comando.
3. **Comprobad Python.** Escribid `python --version`: debe salir **3.11 o superior**. Si da error, probad `python3 --version` y usad `python3` en lugar de `python` en todo el reto.

## 🛠️ Paso a paso

1. **Leed `demo_cliente.py` de arriba abajo, sin ejecutarlo** *(10 min)*. Abrid [`demo_cliente.py`](../reto_herramientas/demo_cliente.py): es **el programa**, no su resultado. Los 8 datos de ejemplo están en [`reservas_demo.py`](../reto_herramientas/reservas_demo.py); no hace falta tocarlos. Intentad encontrar las cuatro piezas de la tabla y **subrayad lo que no entendáis**. Apuntad también qué creéis que va a escribir.
2. **El docente lo proyecta y lo comenta** *(5 min)*. Es el momento de preguntar lo que habíais subrayado.
3. **Ejecutadlo** con `python demo_cliente.py` y comparad: ¿sale lo que habíais pensado?
4. **Responded a las cinco preguntas** de «Hecho cuando», **sin mirar el ordenador**. Cada persona con sus palabras, no solo la que teclea.
5. **Curso «Python desde cero»** *(20 min)*. [`type()`](https://www.curso.soultechlabs.io/basico/#type) (los 3 ejercicios) y [formateo de textos](https://www.curso.soultechlabs.io/basico/#fmt) (ejercicios 1 y 2: el `f-string` y los dos decimales). El docente hace en pantalla el primer ejercicio de cada lección.

## 👀 Qué deberíais ver

Al ejecutar la demostración:

```
=== Resumen semanal de reservas ===
Reservas analizadas: 8
Canceladas: 3 (37.5 %)
Ingreso medio por reserva confirmada: 182.00 €
  - directo: 3 reservas
  - agencia: 2 reservas
  - web_intermediaria: 3 reservas
```

## ✅ Hecho cuando

Cada persona sabe responder, sin mirar el ordenador, estas cinco preguntas:

1. ¿Cuántas reservas analiza el programa y qué línea lo calcula?
2. ¿Por qué `canceladas` empieza en `0` y `por_canal` en `{}`?
3. Si la primera reserva pasara a estar cancelada (`"cancelada": 1`), ¿qué cifras del resumen cambiarían?
4. ¿Qué hace `:.1f` dentro de las llaves del `f-string`?
5. Si `RESERVAS` estuviera **vacía**, ¿qué error saldría y en qué línea? *(probadlo: poned `RESERVAS = []` en una copia)*

## 🚑 Si os atascáis

**No hace falta entender cada línea.** Lo que importa es ver las cuatro piezas. Si algo no sale:

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| `python` no se reconoce, o sale `Python 2…` | En algunos equipos el comando es otro | Probad `python3` y usadlo en todo el reto |
| `No such file or directory` o `ModuleNotFoundError: reservas_demo` | La terminal está en otra carpeta | Abrid la terminal **dentro** de la carpeta descomprimida (`ls` o `dir` debe mostrar `demo_cliente.py`) |
| No entendéis una línea | Es normal en el primer contacto | Subrayadla y preguntad al docente en el momento de los 5 minutos |

## ➡️ Siguiente

[Misión 1 · Los datos en memoria](tarjeta_1_datos.md): aprenderéis a leer y modificar la lista de reservas.
