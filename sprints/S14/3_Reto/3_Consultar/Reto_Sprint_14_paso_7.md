# Paso 7 · Revisión, entrega, review y retro (día 3, 60 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 7 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md)
<!--/nav-->

1. Revisar el trabajo con la rúbrica, por alguien que no escribió esa parte, y anotar el resultado en el README.
2. Subir lo que falte a `sprint-14/` y cada persona su autoevaluación y coevaluación.
3. Enseñar el sprint en la review: 5 minutos por equipo.
4. Hacer la retro (15 minutos) y apuntarla.

**En sencillo.** Es el paso de **cerrar el sprint**, como repasar la maleta antes de salir de viaje. Primero, una persona que no escribió una parte la revisa con una tabla de cuatro criterios (así se detectan fallos que quien lo escribió ya no ve). Después, se comprueba que todo está subido y que cada persona sube su hoja personal. Luego, cinco minutos para enseñar el trabajo al docente y, por último, una conversación corta sobre cómo habéis trabajado y qué cambiar. No hay código ni nada nuevo que aprender: es comprobar, subir, contar y anotar.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Rúbrica** | La tabla con la que se puntúa el reto: cuatro criterios (corrección técnica, reproducibilidad, análisis y comunicación al cliente, IA responsable), cada uno de 1 a 4. |
| **Autoevaluación** | Cada persona puntúa su propio trabajo con la rúbrica. |
| **Coevaluación** | Valoráis el trabajo de otra persona o equipo, con respeto y sin juzgar a la persona. |
| **Review** | La reunión en la que cada equipo enseña lo que ha hecho al docente (el cliente). |
| **Retro** (retrospectiva) | La conversación del equipo sobre cómo ha ido el trabajo: qué seguir, qué cambiar y qué acción concreta tomar. |
| **Raíz del repositorio** | La carpeta principal, la que se ve al abrir el repositorio, antes de entrar en `sprint-14`. |

**Cómo se hace**

1. **La revisión con la rúbrica (10 minutos).** Quien revisa **no escribió** esa parte y sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md):

    - **Ejecutar** lo que dice el README: descargar los datos y ejecutar `01_eda.ipynb` y `02_baseline.ipynb` en orden, en un Colab limpio. Anotar si algo falla o si la métrica del baseline no sale igual.
    - **Leer la ficha como si fuera el cliente:** ¿se entiende la pregunta, la decisión que apoya y cuándo habrá éxito?
    - **Comprobar datos y riesgos:** abrir el enlace de cada fuente, leer la licencia y ver que coincide con el plan de datos; leer los cinco riesgos y ver si valdrían para cualquier proyecto (si sí, son genéricos).
    - **Poner un nivel de 1 a 4 en cada criterio, con una frase de prueba.** Se elige el nivel cuya descripción en la rúbrica **se cumple entera**; si se cumple a medias, es el de abajo. Sin prueba escrita, el nivel no vale. Ejemplos: «3 · la métrica se escribió antes, pero falta el informe de duplicados»; «2 · el README no dice cómo descargar los datos».
    - **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final del `README.md` (ya viene en la plantilla) y arreglar lo más fácil. Lo demás queda como «lo primero que mejoraríamos».

    ```text
    **Revisado por:** Lucía · **Fecha:** (dd/mm/aaaa)

    | Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
    |---|---|---|
    | Corrección técnica | 3 | Los dos cuadernos se ejecutan; la métrica se definió antes, pero falta el informe de duplicados |
    | Reproducibilidad | 2 | El README no dice cómo descargar los datos |
    | Análisis y comunicación al cliente | | |
    | IA responsable | | |

    **Lo primero que mejoraríamos:** añadir al README el enlace de descarga de los datos
    ```

    Es un ejemplo con dos criterios rellenos (nombre y frases inventados): en el vuestro van los **cuatro**.

2. **Subir lo que falte (15 minutos).** Con la [guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md). Comprobad esta lista y **subid en subidas hechas por personas distintas** (cada subida es un *commit* con su nombre):

    | Fichero | Dónde |
    |---|---|
    | `ficha_proyecto.md`, `plan_datos_licencias.md`, `01_eda.ipynb`, `02_baseline.ipynb`, `backlog_y_sprints.md`, `riesgos_eticos.md` | carpeta `sprint-14/` (los seis del equipo) |
    | `README.md` y `requirements.txt` | **raíz** del repositorio, no en `sprint-14/` |
    | `autoevaluacion_nombre.md` | carpeta `sprint-14/`, **uno por persona** |

    Los cuadernos de Colab se descargan con *Archivo → Descargar → Descargar .ipynb* (después de *Reiniciar y ejecutar todo*). Los nombres, en minúsculas y sin espacios ni tildes. Si no subís los datos, el `descargar_datos.py` (o el enlace de descarga en el README) permite repetirlos.

3. **La autoevaluación y la coevaluación (10 minutos).** Cada persona copia la hoja [autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md) con su nombre (`autoevaluacion_marta.md`, por ejemplo) y la sube a `sprint-14/`. Rellena la **Parte 1** (nueve preguntas de repaso con Sí / No / A medias, las cuatro puntuaciones de 1 a 4 con «por qué» y «qué haría para subir un punto», y dos frases sobre lo que más costó y el uso de IA) y la **Parte 2** (coevaluación del trabajo de la persona o equipo que el docente os indique en la review). Cada cual sube lo suyo: no escribáis en el archivo de otra persona.

4. **La review (5 minutos por equipo).** Contad, por este orden: (1) la pregunta de negocio y la decisión que apoyará; (2) los datos y **un hallazgo del EDA que cambia el enfoque**; (3) el baseline y su métrica; (4) tres riesgos éticos; (5) el backlog de los próximos sprints. Repartid las partes entre personas. Los cambios de alcance después del *go* se negocian aquí con el docente.

5. **La retro (15 minutos).** Hablad de tres cosas: una que **seguir haciendo**, una que **cambiar** y **una acción concreta** para el sprint 15 («cada persona sube su trabajo al terminar cada día», no «trabajar mejor»). Anotadlas en la tabla del apartado 5 de `backlog_y_sprints.md`, fila del sprint 14 (la última columna, «¿se cumplió la acción anterior?», lleva `—`). En las retros siguientes, empezad comprobando si cumplisteis la acción anterior. Subid el archivo editado (icono del lápiz → **Commit changes**).

**Qué deberíais ver.** En `sprint-14/` del repositorio, los seis ficheros del equipo y una hoja de autoevaluación por persona (**6 + N**); en la raíz, el README con la sección de revisión rellena y el `requirements.txt`; y en el historial (el icono del reloj), *commits* de todas las personas.

**Hecho cuando:** la sección «Revisión con la rúbrica» está rellena, todos los ficheros están subidos, cada persona ha subido su autoevaluación y coevaluación y habéis hecho la review y la retro.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| No sabéis qué nivel poner en un criterio | La rúbrica describe cuatro niveles por criterio. | Leed la fila en [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md); elegid el nivel cuyo texto se cumple entero y escribid la prueba. |
| Al ejecutar el cuaderno en un Colab limpio falla | Falta un archivo, una librería o el cuaderno depende de una celda que no está. | Anotadlo como hallazgo, corregid lo más fácil y repetid *Reiniciar y ejecutar todo*. |
| Subisteis `README.md` a `sprint-14/` | Debe estar en la raíz. | Abrid el archivo → icono del lápiz → borrad `sprint-14/` de la ruta de arriba → **Commit changes**. |
| `autoevaluacion_nombre.md` se ha sobrescrito | Dos personas usaron el mismo nombre de archivo y la segunda borró lo de la primera. | Usad un nombre distinto por persona (nombre propio, minúsculas, sin tildes) y rellenad de nuevo. |
| Los números de la tabla de la autoevaluación se han descolocado | Se borró alguna barra vertical de la tabla. | Pulsad **Preview** y comprobad que cada fila tiene todas sus barras. |
| Solo hay *commits* de una persona | El resto no ha subido nada con su cuenta. | Repartid las subidas que quedan: cada persona sube o edita al menos un archivo. |
| En la retro surgen quejas sin salida | Falta una acción concreta. | Convertid la queja en una acción con quién y cuándo, y apuntadla en el apartado 5 del backlog. |

<!--nav-->
---

[← Paso 6](Reto_Sprint_14_paso_6.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_14.md)
<!--/nav-->
