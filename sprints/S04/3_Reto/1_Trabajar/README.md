# Sprint 4 · Reto «Herramientas internas» · Cómo se trabaja

> **El reto se hace en seis misiones, y cada misión tiene su tarjeta.** No se aprende «todo Python» primero y se hace el reto después: cada tarjeta trae **justo antes** lo que necesitáis (unas pocas lecciones del curso y unos puzles del Taller) y os explica el paso a paso. Cuando una misión está hecha, la herramienta tiene una pieza más.
>
> **Tened abierta solo la tarjeta de la misión en la que estáis.** Para entregar, mirad [Entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md); si algo no queda claro, la [ficha completa](../3_Consultar/Reto_Sprint_04.md); y para contrastar lo que habéis hecho, el [solucionario de las misiones](../3_Consultar/Solucionario_misiones.md), que se publica por días y se usa **después de intentarlo**.

## Las seis misiones

| Misión | Cuándo | Qué lograréis | Se comprueba con |
|---|---|---|---|
| [**0 · Mirar la demo**](tarjetas/tarjeta_0_mirar_la_demo.md) | Martes · 35 min | Entender el programa del cliente antes de escribir nada | Cinco preguntas de lectura |
| [**1 · Datos en memoria**](tarjetas/tarjeta_1_datos.md) | Martes · 50 min | Leer y modificar una lista de reservas | `python mision_1_datos.py` |
| [**2 · Decidir y repetir**](tarjetas/tarjeta_2_decidir.md) | Martes · 50 min | Contar con `if` y `for` (los contadores de los KPI) | `python mision_2_decidir.py` |
| [**3 · Funciones que calculan**](tarjetas/tarjeta_3_funciones.md) | Martes · 50 + 40 min | Meter los contadores en funciones que devuelven un resultado: `tasa_cancelacion_por_canal`, `ingreso_medio_por_reserva` y `ocupacion_proxy` (con el docente) · **Kata 1** | `python test_kpis.py 1` |
| [**4 · Leer el CSV**](tarjetas/tarjeta_4_ficheros.md) | Miércoles · 50 + 50 min | Leer el fichero real sin que se rompa: `_convertir_fila` y `leer_reservas` | `python test_kpis.py 2` |
| [**5 · Guardar y entregar**](tarjetas/tarjeta_5_salida.md) | Miércoles · 25 + 25 min | Guardar el JSON, ponerlo en marcha con un comando y entregar: `exportar_json`, `main`, README y entrega · **Kata 2** | `python test_kpis.py` (12 de 12) |

**Martes:** misiones 0 a 3, con las reservas ya **en memoria** (sin ficheros). **Miércoles:** misiones 4 y 5: leer el CSV, avisar de los errores, guardar el JSON, README y entrega.

## Antes de empezar

| | |
|---|---|
| **Ver adónde vamos** | La [demo interactiva del reto](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S04/3_Reto/1_Trabajar/S04_demo_reto.html) enseña la herramienta final funcionando (con un CSV bueno y uno roto), deja ensuciar los datos y marca qué pieza construye cada misión. Se abre en el navegador: miradla antes de la [misión 0](tarjetas/tarjeta_0_mirar_la_demo.md). |
| **Cómo leer una tarjeta** | Todas tienen la misma forma. Arriba, una **ficha** (cuándo, cómo, qué usáis y qué veréis al terminar) y un **índice** con enlaces. Debajo, siempre en este orden: 🎯 **Qué lograréis** → 💡 **La idea en un minuto** → 👣 **Paso a paso** → ✅ **Misión terminada cuando** → 🚑 **Si os atascáis** → 👉 **Siguiente** (y, en las misiones 3 y 5, 🥋 la kata). El **paso a paso** es una tabla de pasos numerados, en el orden en que se hacen. Cada paso lleva una etiqueta: 📚 **Aprender** (curso o Taller, o leer algo: no se programa el reto) · 🛠️ **Construir** (abrís un archivo del reto y escribís) · ✅ **Comprobar** (ejecutáis y veis un resultado). Solo hay dos más, de un uso puntual: 🔧 **Preparar** (la carpeta y la terminal, en la misión 0) y 📤 **Entregar** (subir y enseñar, en la misión 5). Cada paso dice **dónde**, **cuántos minutos** y **cuándo está terminado**. |
| **Carpeta de trabajo** | Una sola descarga: [`reto_herramientas.zip`](https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/sprints/S04/3_Reto/1_Trabajar/reto_herramientas.zip). Lleva dentro la plantilla **y** el CSV `reservas_turisdata.csv`. Cómo prepararla paso a paso: [misión 0](tarjetas/tarjeta_0_mirar_la_demo.md). |
| **Parejas: piloto y copiloto** | **Piloto:** teclea. **Copiloto:** lee en voz alta lo que pide la tarjeta y comprueba. **Cambiad de papel en cada misión** (y a mitad si dura más de 25 minutos). En equipos de 3, la tercera persona **revisa** (ejecuta las pruebas y lee el docstring). |
| **Cómo sabéis que vais bien** | Cada misión termina con algo que se **ve en pantalla** (un mensaje verde, una prueba que pasa). Si no lo veis, no está hecha. |
| **Dos katas** | Al final de cada día, **cada persona sola** escribe una función en el [Taller](https://www.curso.soultechlabs.io/taller/): martes la [kata 1](https://www.curso.soultechlabs.io/taller/#kata-1) y miércoles la [kata 2](https://www.curso.soultechlabs.io/taller/#kata-2). Sirven para comprobar que **cada persona** lo ha aprendido, no solo el equipo. |
| **Si os atascáis** | 1) Leed el mensaje de la prueba que falla: dice **qué esperaba y qué recibió**. 2) Repasad la tarjeta de la misión, la lección del curso y su puzle del Taller. 3) Preguntad al equipo y, después, al docente. Cada tarjeta trae además sus errores más típicos. 4) Cuando hayáis terminado la misión (o agotado las pistas), contrastad con el [solucionario](../3_Consultar/Solucionario_misiones.md): es la última fila de «Si os atascáis» en cada tarjeta. |
| **Un asistente de IA** (opcional) | Con las reglas de la «Ayuda 1» de la [ficha completa](../3_Consultar/Reto_Sprint_04.md): lo que dé lo ejecutáis y lo entendéis, las pruebas mandan y lo declaráis en el README. |

## Cuánto del curso entra aquí (y qué queda pendiente)

En clase se hacen **21 ejercicios** del curso «Python desde cero» (los que pide el reto), de los 47 de la ruta ★ mínima. **El resto no se pierde**: son los *pendientes ★* para la consolidación de cada día y para casa (`idx` y `tuplas`, `range`, `while`, `funciones que llaman funciones`, los proyectos *Agenda telefónica* y *Tablas de multiplicar*, comprensiones, `lambda` y clases). Para el **nivel B** de Python (escribir funciones cortas, leer un CSV con `try/except`) hay que llegar **antes del 17/11**; se trabaja con un «gimnasio» de 15 minutos al día en los sprints 5 a 9.

## Para el equipo

| Misión | ¿Hecha? | Piloto | Copiloto | Observaciones |
|---|---|---|---|---|
| 0 · Mirar la demo | | | | |
| 1 · Datos en memoria | | | | |
| 2 · Decidir y repetir | | | | |
| 3 · Funciones que calculan | | | | |
| 4 · Leer el CSV | | | | |
| 5 · Guardar y entregar | | | | |

**Katas (cada persona, sola)**

| Persona | Kata 1: ¿salió? ¿cuántas pistas? | Kata 2: ¿salió? ¿cuántas pistas? |
|---|---|---|
| | | |
| | | |
| | | |
