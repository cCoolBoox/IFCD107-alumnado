# Misión 0 · Mirar la demostración del cliente

> ⏱ **35 minutos** · 🅰️ Fase 1 · martes · 👥 Todo el equipo junto, una persona al teclado · [Volver al índice](../README.md)
>
> **En esta misión usáis:** 🌐 el navegador (el curso) · 📄 un archivo que **solo se lee**: `demo_cliente.py` · 💻 la terminal

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

## 🛠️ Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| 1 | 🔧 Preparar | Descargar y descomprimir. Dentro está **todo junto**: la plantilla, los archivos de las misiones y el CSV | [`reto_herramientas.zip`](https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/sprints/S04/3_Reto/1_Trabajar/reto_herramientas.zip) | 2 | Veis `demo_cliente.py` dentro de la carpeta |
| 2 | 🔧 Preparar | Abrir la carpeta en VS Code y abrir una terminal **en ella**; comprobar la versión de Python | VS Code: *File → Open Folder…* y *Terminal → New Terminal*; después `python --version` | 3 | Sale **3.11 o superior** (si da error, probad `python3` y usadlo en todo el reto) |
| 3 | 📚 Aprender | Leer el programa **de arriba abajo, sin ejecutarlo**. Buscar las cuatro piezas, subrayar lo que no entendáis y apuntar qué creéis que va a escribir | [`demo_cliente.py`](../reto_herramientas/demo_cliente.py) (sus 8 datos: [`reservas_demo.py`](../reto_herramientas/reservas_demo.py)) | 5 | Tenéis apuntadas una predicción y vuestras dudas |
| 4 | 📚 Aprender | El docente lo proyecta y lo comenta. Es el momento de preguntar lo subrayado | La pantalla del aula | 5 | Se han resuelto vuestras dudas |
| 5 | ✅ Comprobar | Ejecutarlo y comparar con vuestra predicción | Terminal: `python demo_cliente.py` | 2 | Sale el resumen de «Qué deberíais ver» |
| 6 | ✅ Comprobar | Responder, **sin mirar el ordenador**, las cinco preguntas de «Hecho cuando» (cada persona, con sus palabras) | Esta tarjeta | 3 | Las cinco respondidas |
| 7 | 📚 Aprender | `type()` (los 3 ejercicios) y formateo de textos (ejercicios 1 y 2: el `f-string` y los dos decimales). El docente hace el primero de cada lección en pantalla | Curso: [`type()`](https://www.curso.soultechlabs.io/basico/#type) y [formateo](https://www.curso.soultechlabs.io/basico/#fmt) | 15 | Los cinco ejercicios en verde |

Si el aula no tuviera Python, usad Colab: subid los ficheros al panel izquierdo y poned `!` delante de cada comando.

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

📖 **Para contrastar**, cuando hayáis terminado o agotado las pistas: [solucionario de la misión 0](../../3_Consultar/Solucionario_misiones.md) (se publica al acabar la clase el martes). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo.

## ➡️ Siguiente

[Misión 1 · Los datos en memoria](tarjeta_1_datos.md): aprenderéis a leer y modificar la lista de reservas.
