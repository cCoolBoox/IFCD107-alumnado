# Sprint 4 · Reto «Herramientas internas» · Tarjetas de misión

> **Cómo se trabaja el reto del Sprint 4.** No se aprende «todo Python» primero y se hace el reto después: el reto se divide en **seis misiones** y cada una trae **justo antes** lo que necesitáis (unas pocas lecciones del curso y unos puzles del Taller). Cuando una misión está hecha, la herramienta tiene una pieza más.
>
> Estas tarjetas son para **tenerlas abiertas mientras trabajáis**. La ficha completa (rúbrica, entrega, ayudas) está en [la ficha del reto](../2_Ficha_completa/Reto_Sprint_04.md) y el resumen en [el reto en una página](../1_Reto_en_una_pagina/Reto_Sprint_04_una_pagina.md).

## Antes de empezar

| | |
|---|---|
| **Carpeta de trabajo** | Copiad la carpeta [`reto_herramientas/`](reto_herramientas/) entera, y el CSV [`reservas_turisdata.csv`](../../../../datos/reservas_turisdata.csv) dentro. Abrid la terminal **en esa carpeta** (`python --version` debe dar 3.11 o más; si no, `python3`). |
| **Parejas: piloto y copiloto** | **Piloto:** teclea. **Copiloto:** lee en voz alta lo que pide la tarjeta y comprueba. **Cambiad de papel en cada misión** (y a mitad si dura más de 25 minutos). En equipos de 3, la tercera persona **revisa** (ejecuta las pruebas y lee el docstring). |
| **Dos fases** | **Fase 1 · martes:** misiones 0 a 3, con las reservas ya **en memoria** (sin ficheros). **Fase 2 · miércoles:** misiones 4 y 5: leer el CSV, avisar de los errores, guardar el JSON, README y entrega. |
| **Cómo sabéis que vais bien** | Cada misión termina con algo que se **ve en pantalla** (un mensaje verde, una prueba que pasa). Si no lo veis, no está hecha. |
| **Dos katas** | Al final de cada día, **cada persona sola** escribe una función en el [Taller](https://www.curso.soultechlabs.io/taller/): martes la [kata 1](https://www.curso.soultechlabs.io/taller/#kata-1) y miércoles la [kata 2](https://www.curso.soultechlabs.io/taller/#kata-2). Sirven para comprobar que **cada persona** lo ha aprendido, no solo el equipo. |

**Los enlaces que vais a usar** — Curso: [`type`](https://www.curso.soultechlabs.io/basico/#type) · [`fmt`](https://www.curso.soultechlabs.io/basico/#fmt) · [`list`](https://www.curso.soultechlabs.io/basico/#list) · [`dict`](https://www.curso.soultechlabs.io/basico/#dict) · [`elif`](https://www.curso.soultechlabs.io/basico/#elif) · [`for`](https://www.curso.soultechlabs.io/basico/#for) · [`func`](https://www.curso.soultechlabs.io/basico/#func) · [`excepciones`](https://www.curso.soultechlabs.io/basico/#pi-excepciones) · [`ficheros`](https://www.curso.soultechlabs.io/basico/#pi-ficheros). Taller: [bloque 1](https://www.curso.soultechlabs.io/taller/#t-total) · [bloque 2](https://www.curso.soultechlabs.io/taller/#t-antelacion) · [bloque 3](https://www.curso.soultechlabs.io/taller/#t-leer) · [bloque 4](https://www.curso.soultechlabs.io/taller/#t-tuberia).

---

## 🅰️ Fase 1 · Martes · La lógica, con los datos en memoria

### Misión 0 · Mirar la demostración del cliente  ⏱ 35 min

**🎯 Qué construís.** Nada todavía: **entender** el programa que nos envía el cliente. Es el reto en pequeño (8 reservas puestas a mano).

**🧰 Paquete de ayuda.**
1. *(15 min)* Preparad la carpeta de trabajo (mirad «Antes de empezar»), ejecutad `python demo_cliente.py` y leed [`demo_cliente.py`](reto_herramientas/demo_cliente.py) de arriba abajo. Subrayad lo que no entendáis. El docente la comenta en pantalla durante 5 minutos.
2. *(20 min)* Curso ★ [`type()`](https://www.curso.soultechlabs.io/basico/#type) (los 3 ejercicios) y [formateo de textos](https://www.curso.soultechlabs.io/basico/#fmt) (ejercicios 1 y 2: `f-string` y dos decimales).

**✅ Hecho cuando** sabéis responder, sin mirar el ordenador, estas cinco preguntas:
1. ¿Cuántas reservas analiza el programa y qué línea lo calcula?
2. ¿Por qué `canceladas` empieza en `0` y `por_canal` en `{}`?
3. Si la primera reserva pasara a estar cancelada (`"cancelada": 1`), ¿qué cifras del resumen cambiarían?
4. ¿Qué hace `:.1f` dentro de las llaves del `f-string`?
5. Si `RESERVAS` estuviera **vacía**, ¿qué error saldría y en qué línea? (probadlo: poned `RESERVAS = []` en una copia)

**🚑 Si os atascáis.** No hace falta entender cada línea: la idea es ver que **un programa de verdad son cuatro piezas** (datos, bucle, `if`, mensaje). Preguntad al docente.

---

### Misión 1 · Los datos en memoria  ⏱ 50 min

**🎯 Qué construís.** Sabéis **leer y modificar** una lista de reservas (cada reserva es un diccionario).

**🧰 Paquete de ayuda.**
1. *(25 min)* Curso ★ [listas](https://www.curso.soultechlabs.io/basico/#list) (ejercicios 1 y 2) y [diccionarios](https://www.curso.soultechlabs.io/basico/#dict) (los 3 ejercicios).
2. *(15 min)* El archivo [`mision_1_datos.py`](reto_herramientas/mision_1_datos.py): sustituís cada `TODO` y ejecutáis `python mision_1_datos.py`.
3. *(10 min)* Taller, [bloque 1](https://www.curso.soultechlabs.io/taller/#t-total): «El total de una reserva» y «Un mensaje con f-string».

**✅ Hecho cuando** `python mision_1_datos.py` termina con **«✅ ¡Misión 1 superada!»**.

**🚑 Si os atascáis.** Una reserva es `reserva["noches"]`; la lista es `reservas[0]` (la primera) o `reservas[-1]` (la última). Si sale `KeyError`, la clave está mal escrita; si sale `IndexError`, el número de posición no existe.

---

### Misión 2 · Decidir y repetir  ⏱ 50 min

**🎯 Qué construís.** Los **contadores** que están detrás de todos los KPI: contar canceladas, sumar noches y contar por canal.

**🧰 Paquete de ayuda.**
1. *(25 min)* Curso ★ [`if / elif / else`](https://www.curso.soultechlabs.io/basico/#elif) (ejercicios 1 y 2) y [`for`](https://www.curso.soultechlabs.io/basico/#for) (los 3 ejercicios).
2. *(25 min)* El archivo [`mision_2_decidir.py`](reto_herramientas/mision_2_decidir.py), con las 8 reservas de ejemplo. Ejecutad `python mision_2_decidir.py`.

**✅ Hecho cuando** sale **«✅ ¡Misión 2 superada!»**.

**🚑 Si os atascáis.** El patrón de contar es siempre el mismo: una variable que empieza en `0`, un `for` que recorre las reservas y un `if` que suma `1` cuando toca. Para contar **por canal**, un diccionario y `por_canal.get(canal, 0) + 1` (mirad cómo lo hace `demo_cliente.py`).

---

### Misión 3 · Funciones que calculan  ⏱ 50 min + 40 min  *(la segunda parte, después de la consolidación)*

**🎯 Qué construís.** Las dos primeras funciones de `kpis.py`: `tasa_cancelacion_por_canal` e `ingreso_medio_por_reserva`. Esta vez **con pruebas** que os dicen si está bien.

**🧰 Paquete de ayuda.**
1. *(10 min)* Curso ★ [funciones](https://www.curso.soultechlabs.io/basico/#func) (ejercicios 1 y 2): `def`, parámetros y `return`.
2. *(10 min)* Taller, [bloque 2](https://www.curso.soultechlabs.io/taller/#t-conteo): «Contar con un diccionario» e «Ingreso medio de las reservas confirmadas». **Son casi vuestras dos funciones**, montadas con piezas.
3. *(Resto)* Abrid [`kpis.py`](reto_herramientas/kpis.py). Ejecutad `python test_kpis.py 1` (todo falla: es lo normal) y programad **de una en una**, siguiendo los comentarios «Paso» de cada función. Después de cada función, volved a ejecutar la prueba.
4. *(Docente, 10 min)* Se hace en pantalla `ocupacion_proxy` (la tercera función, de nivel estándar).

**✅ Hecho cuando** `python test_kpis.py 1` muestra **`4 de 4 pruebas superadas`**.

**🚑 Si os atascáis.** Leed el mensaje de la prueba: dice **qué esperaba y qué recibió**. Probad la función en `python` con la lista `RESERVAS` de `reservas_demo.py` (`from reservas_demo import RESERVAS`). Si no sale: `return` **devuelve** el valor; `print` solo lo enseña, y las pruebas necesitan el valor.

---

### 🥋 Kata 1 · Una función con `return`  ⏱ 10 min · **individual** · fin del martes

[Abrir la kata 1](https://www.curso.soultechlabs.io/taller/#kata-1): escribid **solos** `noches_confirmadas(reservas)`. Sin mirar la misión 3, sin preguntar al equipo. Apuntad **cuántas pistas** habéis usado. Si no sale, no pasa nada: se repite mañana por la mañana.

---

## 🅱️ Fase 2 · Miércoles · Ficheros, errores y entrega

### Misión 4 · Leer el CSV sin que se rompa  ⏱ 50 min + 50 min

**🎯 Qué construís.** `_convertir_fila` y `leer_reservas`: leer `reservas_turisdata.csv`, convertir los textos a números y fechas, **descartar y contar** las filas defectuosas y dar un mensaje claro si falta el fichero o una columna.

**🧰 Paquete de ayuda** *(primeros 50 minutos)*.
1. *(30 min)* Curso ★ [excepciones](https://www.curso.soultechlabs.io/basico/#pi-excepciones) (ejercicios 1 y 2) y [ficheros de texto, CSV y JSON](https://www.curso.soultechlabs.io/basico/#pi-ficheros) (ejercicios 2 y 3).
2. *(20 min)* Taller, [bloque 3](https://www.curso.soultechlabs.io/taller/#t-leer): «Leer un CSV sin que se rompa», «¿Qué error es cada uno?» y «Guardar los KPIs en JSON».

**🛠️ Trabajo** *(los otros 50 minutos)*. En `kpis.py`: primero `_convertir_fila` y después `leer_reservas`, con los comentarios «Paso». Ejecutad `python test_kpis.py 2` y mirad cuáles pasan de rojo a verde. Ojo: `leer_reservas` devuelve **dos cosas a la vez** (`return reservas, avisos`, una *tupla*); quien la llama las recoge con `reservas, avisos = leer_reservas(ruta)`.

**✅ Hecho cuando** pasan las pruebas de lectura: `test_leer_reservas_convierte_tipos`, `test_fichero_inexistente`, `test_faltan_columnas`, `test_filas_defectuosas…` y `test_valores_imposibles…`.

**🚑 Si os atascáis** *(señal de alarma a las 09:55)*. Si a las 09:55 todavía no habéis empezado `leer_reservas`, **se lo decís al docente**: la proyecta resuelta, la copiáis, **la explicáis con vuestras palabras** (línea a línea, en voz alta) y seguís con la misión 5. Es una ayuda legítima, y lo declaráis en el README («Uso de IA y límites»).

---

### Misión 5 · Guardar el resultado y ponerlo todo en marcha  ⏱ 25 min + 25 min de entrega

**🎯 Qué construís.** `exportar_json` y `main`: la herramienta de verdad, con un comando. Y la entrega.

**🧰 Paquete de ayuda** *(10 min)*. Taller, [bloque 4](https://www.curso.soultechlabs.io/taller/#t-tuberia): «Encadena las funciones» y «Escribe la función principal». Es exactamente vuestro `main`.

**🛠️ Trabajo** *(15 min)*. `exportar_json` y `main` en `kpis.py`. Ejecutad:

```
python kpis.py reservas_turisdata.csv salida.json --capacidad 40
python test_kpis.py
```

**✅ Hecho cuando** existe `salida.json` con las cifras esperadas y `python test_kpis.py` da **`12 de 12 pruebas superadas`**.

**📦 Entrega** *(25 min)*: provocar los 3 errores a propósito (la [ficha](../2_Ficha_completa/Reto_Sprint_04.md) lo explica en el paso 4 de la misión 5), README con la plantilla, revisión con la rúbrica, subida a `sprint-04/` y autoevaluación y coevaluación **de cada persona**.

---

### 🥋 Kata 2 · Leer un CSV sin que se rompa  ⏱ 10 min · **individual** · fin del miércoles

[Abrir la kata 2](https://www.curso.soultechlabs.io/taller/#kata-2): escribid **solos** `media_precio(ruta)`, que lee un CSV, ignora las filas defectuosas y devuelve `None` si el fichero no existe. Apuntad cuántas pistas habéis usado.

---

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
| 5 · Guardar y poner en marcha | | | | |

**Katas (cada persona, sola)**

| Persona | Kata 1: ¿salió? ¿cuántas pistas? | Kata 2: ¿salió? ¿cuántas pistas? |
|---|---|---|
| | | |
| | | |
| | | |
