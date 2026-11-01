# Paso 1 · Planning y reparto de roles (día 1, 10 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md) · [Paso 2 →](Reto_Sprint_06_paso_2.md)
<!--/nav-->

1. Elegir **Scrum Master y responsable técnico** de este sprint (no pueden repetir quienes lo fueron en el anterior).
2. Leer los apartados 1 y 3 de esta ficha y decidir hasta qué nivel queréis llegar.
3. Pasar al tablero las tareas y decidir quién empieza cada una.

**En sencillo.** Este paso no tiene código: es una reunión corta de equipo, como la de varias personas que van a cocinar juntas y, antes de encender el fuego, deciden quién lleva el tiempo, quién comprueba que la receta saldría igual otro día y quién empieza por qué plato. El cliente (TurisData) os ha mandado un fichero de reservas «sucio»; en los pasos siguientes lo vais a revisar, limpiar y probar con un modelo sencillo. Aquí solo organizáis el trabajo para no pisaros: dos roles, un nivel de ambición y un tablero con las tareas a la vista. No hace falta saber Python ni Scrum: con lo que pone esta página basta, y el reparto se puede cambiar más adelante si no funciona.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Planning** | La reunión de arranque del sprint: se lee el reto, se reparte el trabajo y se apuntan las tareas. Aquí dura 10 minutos. |
| **Scrum Master** | Quien cuida que el equipo trabaje bien: lleva el tiempo, mantiene el tablero al día y avisa si algo se atasca. No es el jefe ni quien hace más trabajo. |
| **Responsable técnico** | Quien vigila que el resultado sea correcto y se pueda repetir: que otra persona ejecute el cuaderno y obtenga lo mismo. No lo programa todo. |
| **Tablero y tarjeta** | El panel del equipo (Trello o similar) con columnas; cada tarea es una tarjeta con una persona responsable. Si no está en el tablero, para el equipo no existe. |
| **Nivel** | Hasta dónde llega el equipo en este reto: mínimo (una entrega válida), estándar o extra. |
| **Inventario de defectos** | La lista de lo que está mal en el fichero: huecos, duplicados, valores imposibles, formatos mezclados… (paso 2). |
| **Función de limpieza** | Un trozo de código con nombre que arregla el fichero siempre igual, sin tocar el original (paso 3). |
| **Pipeline** | Una cadena de pasos de preparación y modelo que se ejecuta siempre igual (paso 4). |
| **Baseline** | El modelo de referencia, muy simple: el «suelo» con el que comparar el vuestro (paso 4). |

**Cómo se hace**

1. **Elegir los dos roles (3 minutos).** Abrid la tarjeta *Roles* del tablero (columna *Información*) y elegid **Scrum Master** y **responsable técnico** para el Sprint 6. Reglas de la [guía del tablero](../../../S00/actividades/guia_tablero_trello.md): las dos personas no pueden ser las mismas que en el sprint anterior y nadie repite hasta que hayan pasado todas las personas del equipo. Apuntad los dos nombres en la fila del Sprint 6. Los roles solo reparten **quién vigila qué**: todo el equipo trabaja en el contenido.

2. **Decidir el nivel (3 minutos).** Leed el apartado 1 («Qué os pide el cliente») y el 3 («Guía paso a paso») de la [ficha del reto](Reto_Sprint_06.md); los cinco pasos resumidos están en el [reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md). Después elegid hasta dónde llegáis:

    | Nivel | Qué hay que tener |
    |---|---|
    | **Mínimo** | Tabla de **6 defectos o más** · una función `limpiar_reservas` que devuelve la tabla limpia y un resumen · el cuaderno corre con *Reiniciar y ejecutar todo* · README corto · todo subido a `sprint-06/`. Es una entrega válida y evaluable. |
    | **Estándar** | Además: un *pipeline* que ajusta solo con *train* · el modelo y el «modelo tonto» comparados con validación cruzada · 3 preguntas al cliente · IA responsable · README con versiones · revisión con la rúbrica. |
    | **Extra** | Además: 8–10 defectos · partición temporal justificada · explicar o probar qué pasa si se escala con todos los datos. |

    Si dudáis, apuntad el **mínimo** y subid de nivel si os sobra tiempo: si el tiempo aprieta, se completa el mínimo y lo demás se deja para casa. Anotad el nivel en el tablero, donde todo el equipo lo vea.

3. **Crear las seis tarjetas (3 minutos).** En la columna *Sprint backlog* cread una tarjeta por tarea, con **una persona responsable** y, en la descripción, cuándo se da por hecha:

    | Tarjeta | Se da por hecha cuando… |
    |---|---|
    | Inventario de defectos | Hay 6 o más defectos con sus datos completos (paso 2). |
    | Función de limpieza | `limpiar_reservas` devuelve tabla y resumen sin tocar el original, y *train* y *test* están separados (paso 3). |
    | *Pipeline* | El preprocesado imputa, escala y codifica ajustando solo con *train* (paso 4). |
    | *Baseline* | Hay una frase con media ± desviación, modelo frente a modelo «tonto» (paso 4). |
    | Informe | Todos los apartados del nivel elegido están rellenos (paso 5). |
    | README | Otra persona podría repetir el cuaderno con solo el README (paso 5). |

    Quien empieza una tarjeta la mueve a *En curso* (máximo 2 por persona). Al terminar, a *En revisión*; la pasa a *Hecho* otra persona: nadie revisa lo suyo.

4. **Repartir quién empieza (1 minuto).** Todo el equipo debe entender todo, así que **quien no programa una parte, la revisa**. Un reparto posible para los pasos 2 a 4:

    | Persona | Empieza por | Revisa |
    |---|---|---|
    | A | Inventario de defectos y tabla del informe | La función de limpieza |
    | B | Función `limpiar_reservas` y partición *train*/*test* | El *pipeline* |
    | C | *Pipeline*, *baseline* y validación cruzada | El inventario de defectos |
    | D (si hay 4) | README y preguntas al cliente | El informe entero |

    Si sois 3, repartid lo de D entre las otras tres personas. Para cerrar, cada persona dice en voz alta: «Empiezo por… y reviso…».

**Qué deberíais ver.** En el tablero, seis tarjetas en *Sprint backlog* (las de quien ya empieza, en *En curso*), cada una con su persona responsable y su criterio de «hecha»; los nombres del Scrum Master y del responsable técnico en la tarjeta *Roles*; y el nivel anotado. Por ejemplo:

```text
Sprint backlog                         Persona
  Inventario de defectos ............. A
  Función de limpieza ................ B
  Pipeline ........................... C
  Baseline ........................... C
  Informe ............................ A
  README ............................. D
Nivel del equipo: mínimo (subimos si sobra tiempo)
```

**Hecho cuando:** los roles están elegidos y cada persona sabe con qué tarea empieza y qué parte revisa.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| No os ponéis de acuerdo en el nivel | Cada persona tiene una idea distinta de cuánto da tiempo. | Apuntad el **mínimo** (es una entrega válida) y decidid en la *daily* si subís; el estándar es lo que describe la «Definition of Done» de la ficha completa. |
| Sois 3 y el reparto tiene 4 filas | La fila D es «si hay 4». | Repartid el README y las preguntas al cliente entre A, B y C; el informe entero lo revisa quien no lo escribió. |
| Alguien repite rol respecto al Sprint 5 | Los dos roles cambian en cada sprint. | Elegid a otras personas y anotad el relevo en la tarjeta *Roles*. |
| Todas las tarjetas acaban en la misma persona | Se confunde «rol» con «hacerlo todo». | El Scrum Master facilita, no hace todo: repartid con la tabla de arriba y no pongáis más de 2 tarjetas *En curso* por persona. |
| No tenéis tablero | No se montó en el Sprint 0 o se perdió. | Montadlo con la [guía del tablero](../../../S00/actividades/guia_tablero_trello.md); basta con las columnas *Sprint backlog*, *En curso*, *En revisión* y *Hecho*. |
| Pasan los 10 minutos y falta algo | El planning es corto a propósito. | Apuntad lo que falta como tarjeta y empezad; el reparto se ajusta en la *daily*. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_06.md) · [Paso 2 →](Reto_Sprint_06_paso_2.md)
<!--/nav-->
