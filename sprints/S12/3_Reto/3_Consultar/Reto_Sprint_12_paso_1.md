# Paso 1 · Reparto y plan (día 1, 10 minutos, y día 2, 5 minutos)

<!--nav-->
> Sprint 12 · Reto «Escuchar al cliente» · paso 1 de 4 · [Ficha del reto](Reto_Sprint_12.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_12_una_pagina.md) · [Paso 2 →](Reto_Sprint_12_paso_2.md)
<!--/nav-->

1. Repartir las cinco áreas: reseñas, ocupación, asistente, IA responsable y coordinación.
2. Escribir en el tablero una tarjeta por entregable, con responsable y día.
3. Leer la rúbrica y decidir la pregunta de negocio de cada parte.
4. Mirar el calendario: qué entrega cada día.

**En sencillo.** Este paso no tiene código: es el plan del equipo. Pensad en una cocina con cuatro cocineros: cada uno se encarga de un plato, pero todos conocen la carta y pueden explicar cualquiera. Aquí los «platos» son lo que pide TurisData (un informe de reseñas, una previsión de ocupación, un asistente que responde con la política del alojamiento y una nota de IA responsable) más un archivo que lo une todo, el `LEEME.md`. En 15 minutos (10 hoy y 5 el día 2) dejáis escrito en el tablero quién hace qué, para qué día y qué pregunta contesta cada parte. No hace falta saber Python ni abrir todavía ningún cuaderno.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Entregable** | Cada cosa que hay que entregar al cliente: un informe, un cuaderno, una nota. |
| **Tablero y tarjeta** | El panel del equipo (Trello o similar) tiene columnas: *Por hacer → En curso → En revisión → Hecho*. Cada tarea es una tarjeta con una persona responsable. Si no está en el tablero, para el equipo no existe. |
| **Responsable** | Quien **lidera** una parte y vigila que llegue entregada. No es quien lo hace todo. |
| **Pregunta de negocio** | Lo que el cliente quiere saber, en una frase y sin jerga: «¿de qué se quejan más los huéspedes?». |
| **Rúbrica** | La tabla con la que se puntúa: cuatro criterios (corrección técnica, reproducibilidad, análisis y comunicación al cliente, IA responsable), de 1 a 4 cada uno. |
| **Niveles** | Mínimo (entrega válida), estándar y extra. El equipo decide hasta dónde llega. |
| **`LEEME.md`** | Archivo de texto de cinco líneas que explica cómo repetir todo lo que habéis hecho. |

**Cómo se hace**

1. **Abrir el tablero.** Usad el del equipo (si ya lo tenéis de otros sprints) o cread uno en Trello con las cuatro columnas *Por hacer*, *En curso*, *En revisión* y *Hecho*. Todas las tarjetas de abajo empiezan en *Por hacer*.
2. **Repartir las áreas.** Cada persona lidera una parte, pero **todas deben poder explicar cualquiera**: en la review el docente puede preguntar a cualquier persona por cualquier parte.

    | Persona | Área | Lidera |
    |---|---|---|
    | A | Reseñas | `informe_resenas.md`, `grafico_resenas.png` y `resenas.ipynb` |
    | B | Ocupación | `ocupacion.ipynb` |
    | C | Asistente | `asistente_rag.ipynb` y `evaluacion_asistente.csv` |
    | D (si hay 4) | IA responsable y coordinación | `nota_ia_responsable.md` y `LEEME.md` |

    Con 3 personas no existe la D: una de las tres asume además su área (la IA responsable y la coordinación van juntas). Decidid quién, mejor la persona con la parte más ligera. Quien coordina vigila que las cuatro piezas encajen y revisa el `LEEME.md`.

3. **Crear una tarjeta por entregable.** Son cinco, que agrupan los ocho ficheros de la Tabla A de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). Cada tarjeta lleva el nombre de quien la lidera y el día en que debe estar lista:

    | Tarjeta | Ficheros | Día |
    |---|---|---|
    | Informe de reseñas | `informe_resenas.md`, `grafico_resenas.png`, `resenas.ipynb` | Cuaderno y gráfico, día 2 · informe, día 3 |
    | Previsión de ocupación | `ocupacion.ipynb` | Día 3 |
    | Asistente con RAG | `asistente_rag.ipynb`, `evaluacion_asistente.csv` | Cuaderno, día 2 · evaluación, día 3 |
    | Nota de IA responsable | `nota_ia_responsable.md` | Día 3 |
    | `LEEME.md` | `LEEME.md` | Día 3 |

    Así queda una tarjeta (escribid esto en su descripción):

    ```text
    Asistente con RAG · responsable: C · día 2 (cuaderno) y día 3 (evaluación) · nivel: estándar
    Pregunta de negocio: ¿qué hace el asistente cuando no sabe?
    Ficheros: asistente_rag.ipynb, evaluacion_asistente.csv
    Hecho cuando: cita la fuente, responde «No consta…» a la pregunta del gimnasio y las 25 preguntas están evaluadas.
    ```

4. **Escribir la pregunta de negocio de cada parte.** Una frase que empiece por «¿qué…?», «¿cuánto…?» o «¿cómo…?» y se pueda contestar con una cifra o con un ejemplo. Por ejemplo: reseñas, «¿de qué se quejan más los huéspedes?»; ocupación, «¿cuánto mejora un modelo al método simple?»; asistente, «¿qué hace el asistente cuando no sabe?»; nota de IA responsable, «¿qué riesgos tiene el asistente y qué hicimos contra cada uno?». Si la vuestra solo se puede contestar con «sí» o «no», reescribidla.
5. **Leer la rúbrica y fijar el nivel.** Abrid [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y leed la Tabla B, que dice qué se pide en cada nivel (mínimo, estándar, extra). Apuntad en cada tarjeta el nivel al que apuntáis. Regla práctica: primero el mínimo de las tres partes y después subir. Es mejor entregar las cuatro piezas sencillas que tres perfectas y una vacía.
6. **Mirar el calendario y copiarlo al tablero.** Quien coordina pone el día en cada tarjeta:

    | Día | Qué | Minutos |
    |---|---|---|
    | 2 | Este paso (repaso del reparto) | 5 |
    | 2 | Reseñas (A) y asistente (C), en paralelo (paso 2) | 50 |
    | 3 | Ocupación (B) (paso 2) | 30 |
    | 3 | Evaluar el asistente, probar 3 ataques y medir una defensa (paso 3) | 40 |
    | 3 | Informe, nota, `LEEME.md`, revisión, subida y ensayo de la review (paso 4) | 40 |

**Qué deberíais ver.** Un tablero con cinco tarjetas (informe de reseñas, ocupación, asistente, nota de IA responsable y `LEEME.md`). Cada una tiene una persona responsable, un día, un nivel y la pregunta de negocio escrita.

**Hecho cuando:** cada persona sabe qué parte lidera, qué día entrega cada cosa y cuál es la pregunta de negocio de su parte.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Sois 3 y sobra un área | La D (IA responsable y coordinación) no tiene persona. | Una de las tres la asume además de su parte; apuntad su nombre en las dos tarjetas. |
| Una persona tiene todas las tarjetas | El reparto no se ha hecho o se ha dejado a una sola persona. | Repartid de nuevo con la tabla de arriba: una persona, una parte. |
| «No sé qué pregunta de negocio poner» | La parte se ha descrito por lo que hace («hacer un gráfico») y no por lo que el cliente quiere saber. | Mirad los ejemplos del paso 4 de arriba y cambiad el verbo: no «dibujar», sino «saber de qué se quejan». |
| Nadie tiene tablero | Es el primer reto del equipo o se perdió el de antes. | Creadlo en Trello con las cuatro columnas. Si no está en el tablero, para el equipo no existe. |
| «Yo solo me sé mi parte» | Se ha entendido «lidera» como «solo hace». | Cada persona cuenta al resto, en dos minutos, qué hace su parte. Se repite antes de la review. |
| Las cinco tarjetas no caben en el tiempo | Todas apuntan al nivel más alto. | Bajad al mínimo en las tres partes técnicas y subid solo si sobra tiempo. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_12.md) · [Paso 2 →](Reto_Sprint_12_paso_2.md)
<!--/nav-->
