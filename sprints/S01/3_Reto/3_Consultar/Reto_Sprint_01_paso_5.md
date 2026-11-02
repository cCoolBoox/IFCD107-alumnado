# Paso 5 · Informe, revisión y cierre (día 2, 20 minutos)

<!--nav-->
> Sprint 1 · Reto «Auditoría de oportunidades de IA» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_01.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_01_una_pagina.md)
<!--/nav-->

1. Escribir lo que falta del informe, y al final el resumen ejecutivo y la línea de uso de IA.
2. Revisarlo con la rúbrica, por alguien que no escribió esa parte.
3. Subir lo que falte, hacer la autoevaluación, la review y la retro.

**En sencillo.** Es el paso de **cerrar el trabajo**, como revisar la maleta antes de salir de viaje. Primero se escribe lo que queda del informe, y el resumen el último, porque solo se puede resumir lo que ya está decidido. Después, alguien que no lo escribió lo lee como si fuera la directora y lo puntúa. Por último, se sube todo y se cuenta el trabajo al docente. No hay nada nuevo que aprender: es escribir claro, comprobar, subir y contar.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Resumen ejecutivo** | Cinco o seis líneas, sin jerga, para quien solo lea eso: qué recomendáis y por qué. |
| **Límites del informe** | Lo que no habéis podido comprobar y lo que habéis supuesto. Decirlo da confianza, no la quita. |
| **Rúbrica** | La tabla con la que se puntúa el reto: cuatro criterios (corrección técnica, reproducibilidad, análisis y comunicación al cliente, IA responsable), cada uno de 1 a 4. |
| **Autoevaluación y coevaluación** | Cada persona puntúa su trabajo con la rúbrica (autoevaluación) y valora el de otra persona o equipo (coevaluación). |
| **Review y retro** | La *review* es la reunión en la que cada equipo enseña su trabajo al docente. La *retro* es la conversación del equipo sobre cómo ha ido. |

**Cómo se hace**

1. **Escribir lo que falta del informe (8 minutos).** Cada persona, en su apartado de `informe_oportunidades.md` (por turnos). Ejemplos inventados, solo para ver el tono:

    - **Apartado 2 · Lo que hemos entendido (3 o 4 líneas):** qué le duele a la directora, con una frase de la entrevista, y vuestra pregunta del Sprint 0: «¿Cómo podríamos [verbo] [para quién] [para conseguir qué]?».
    - **Apartado 6 · Recomendación:** «Piloto: resumen automático de reseñas en dos alojamientos. Datos: las reseñas, sin nombres. Necesitamos del cliente: acceso a las reseñas y una persona que revise los resúmenes. Siguiente paso: reunión con la directora para confirmar qué reseñas se pueden usar. Todo, sin pasar de los 15.000 €».
    - **Apartado 7 · Límites:** «No hemos podido comprobar si las reseñas incluyen datos personales; hemos supuesto que sí».
    - **Apartado 1 · Resumen ejecutivo (el último):** «Recomendamos empezar por X porque…», sin palabras como *modalidad* o *supervisado* si no las explicáis.
    - **Uso de IA (una línea):** qué herramienta, para qué y qué se comprobó a mano. Si no se ha usado, decidlo.

    **Qué no vale:** un resumen que no diga qué recomendáis, un piloto sin datos ni siguiente paso, o dejar las notas en cursiva de la plantilla. Como guía, una página son unas 500 palabras; si pasáis de unas 1.500 (sin el checklist ni la revisión), recortad.

2. **La revisión cruzada (8 minutos).** Quien revisa **no escribió** esa parte y sigue los cinco puntos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). Pone un nivel de 1 a 4 en cada criterio, con **una frase de prueba**, en el último apartado del informe, «Revisión con la rúbrica». Si lo de un nivel se cumple a medias, se pone el de abajo. Ejemplo con dos criterios rellenos (nombre y frases inventados; en el vuestro van los **cuatro**):

    ```text
    **Revisado por:** Lucía · **Fecha:** (dd/mm/aaaa)

    | Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
    |---|---|---|
    | Corrección técnica | 3 | Los cinco casos están clasificados; en el caso 4 la modalidad es «aprendizaje», que no es un tipo de dato |
    | Reproducibilidad | 2 | Se entiende el caso recomendado, pero no cómo se puntuó la facilidad |
    | Análisis y comunicación al cliente | | |
    | IA responsable | | |

    **Lo primero que mejoraríamos:** explicar la facilidad en el apartado 4
    ```

3. **Corregir lo más fácil (4 minutos).** Arreglad lo que se pueda y dejad el resto en «Lo primero que mejoraríamos». Subid el cambio con el icono del lápiz → **Commit changes**.

**Después, 50 minutos de entrega, review y retro.** No son parte de los 20 minutos de este paso, pero se hacen a continuación:

4. **Subir y comprobar (unos 15 minutos).** Con la [guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md). En `sprint-01/` tienen que estar los ficheros de esta tabla, subidos por **personas distintas**, cada una con su cuenta (cada subida es un *commit* con su nombre):

    | Fichero | Quién lo sube |
    |---|---|
    | `informe_oportunidades.md` | La persona del informe |
    | `checklist_etico.md` | La persona del checklist |
    | `autoevaluacion_nombre.md` | Cada persona la suya |

5. **Autoevaluación y coevaluación (unos 10 minutos).** Cada persona copia la [hoja](../2_Entregar/autoevaluacion_y_coevaluacion.md) con su nombre (por ejemplo `autoevaluacion_marta.md`) y la sube a `sprint-01/`. Rellena la **Parte 1** (repaso, cuatro puntuaciones y dos frases) y la **Parte 2** sobre el trabajo de la persona o el equipo que el docente os indique. No escribáis en el archivo de otra persona.

6. **La review (5 minutos por equipo).** Repartid las partes y contad: (1) la **recomendación** en una frase y por qué es la primera; (2) **un caso que descartasteis** y por qué; (3) el **semáforo** de vuestro caso principal y la medida más importante; (4) **una duda** que dejaríais abierta para el cliente.

7. **La retro (unos 10 minutos).** Una cosa que **seguir haciendo**, una que **cambiar** y **una acción concreta** para el Sprint 2 («cada persona sube su trabajo al terminar cada sesión», no «trabajar mejor»). Apuntadla en una tarjeta del tablero. La review y la retro no se suben.

**Qué deberíais ver.** En `sprint-01/`, los dos ficheros del equipo y una hoja de autoevaluación por persona (**2 + N**), el último apartado del informe con la revisión rellena y, en el historial (el icono del reloj), *commits* de varias personas.

**Hecho cuando:** el informe está completo y revisado, los ficheros están subidos por personas distintas, cada persona ha subido su hoja y habéis hecho la review y la retro.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| El informe pasa de tres páginas | Se ha contado demasiado. | Pasad los detalles al checklist y acortad las celdas de las tablas. La revisión y el checklist no cuentan. |
| El resumen usa palabras que la directora no entendería | Se ha escrito para el docente. | Releedlo como si fuerais ella. Explicad la palabra en una frase o cambiadla. |
| Quien revisa es quien escribió esa parte | Así no se detectan fallos. | Cambiad de pareja: que revise alguien que no la escribió. |
| Solo hay *commits* de una persona | El resto no ha subido nada con su cuenta. | Repartid lo que queda: cada persona sube o edita al menos un archivo. |
| Dos personas han subido `autoevaluacion_nombre.md` con el mismo nombre | La segunda borra lo de la primera. | Poned en cada archivo el nombre de quien lo sube. |
| No da tiempo de terminar | Es normal si el checklist quedó a medias. | Subid el nivel mínimo, anotad lo pendiente en el tablero y terminadlo en vuestro tiempo de equipo antes del Sprint 2. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_01_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_01.md)
<!--/nav-->
