# Paso 4 · Matriz de priorización y checklist ético (día 2, 30 minutos)

<!--nav-->
> Sprint 1 · Reto «Auditoría de oportunidades de IA» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_01.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_01_una_pagina.md) · [Paso 5 →](Reto_Sprint_01_paso_5.md)
<!--/nav-->

1. Puntuar los cinco casos en impacto y facilidad y elegir los dos que van primero.
2. Pasar el checklist ético: completo en esos dos casos y resumido en los otros tres.
3. Poner un semáforo a cada caso y llevar la matriz y los semáforos al informe.

**En sencillo.** Primero decidís **qué conviene hacer antes** (la matriz) y después **qué podría salir mal** (el checklist). Es como elegir un viaje: miráis lo que os apetece y lo fácil que es llegar, y luego repasáis los riesgos. No se calcula nada: son notas del 1 al 5 y frases. No hace falta saber de leyes: el checklist dice qué preguntar y los apuntes explican las palabras.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Matriz de priorización** | Una tabla que ordena los casos con dos notas: **impacto** (cuánto ayudaría a TurisData) y **facilidad** (si el cliente ya tiene los datos y se podría probar con un piloto pequeño). |
| **Checklist ético** | Un formulario de preguntas sobre riesgos (datos, sesgos, decisiones sin personas, normas). En cada una se anota una **evidencia o acción**: algo comprobable. |
| **(★)** | Marca de las 13 preguntas más importantes del checklist, las que no se pueden saltar. |
| **Semáforo** | Verde: se puede avanzar. Ámbar: se puede avanzar con medidas. Rojo: no avanzar sin cambiar el caso. |
| **Dato personal** | Cualquier dato que permita saber de qué persona se trata: nombre, correo, teléfono, una foto de una cara, una reserva con nombre. |
| **Sesgo y proxy** | Un sesgo es un trato injusto hacia un grupo. Un proxy es una variable que «adivina» sin querer algo sensible: el país de origen puede hacer de sustituto de la nacionalidad. |
| **AI Act** | La norma europea de IA. Clasifica los sistemas por riesgo (inaceptable, alto, limitado, mínimo). Los plazos son escalonados: *verificar calendario vigente*. |

**Cómo se hace**

1. **Puntuar los casos y elegir dos (7 minutos).** Poned los cinco casos en una tabla con una nota de **impacto** y otra de **facilidad** (de 1, poco, a 5, mucho) y **una frase** de por qué. Cada persona puntúa en silencio y luego lo comparáis; si dos notas se llevan más de un punto, hablad un minuto y quedaos con un número. Ejemplo (inventado: no son vuestros casos ni vuestras notas):

    | Caso (ejemplo inventado) | Impacto | Facilidad | Por qué está ahí |
    |---|---|---|---|
    | Previsión de ocupación | 5 | 4 | Afecta a los precios de casi todo el año y ya hay reservas guardadas |
    | Resumen de reseñas | 4 | 4 | La dirección no las lee y el texto ya existe |
    | Recordatorio de cancelación (sin IA) | 3 | 5 | Basta una regla, no hay que entrenar nada |
    | Chatbot de reservas | 4 | 2 | Ayudaría mucho, pero faltan conversaciones reales de clientes |

    Escribid también el **criterio** en una frase («facilidad = el cliente ya tiene los datos y se puede probar con un piloto pequeño»). Los **dos casos con más impacto × facilidad** (aquí, 20 y 16) son los **priorizados**. Si hay empate, pasa primero el de **menos riesgo ético**.

2. **Preparar el fichero del checklist (4 minutos).** La persona encargada de `checklist_etico.md`:

    - Abre [`checklist_etico_v1.md`](../1_Trabajar/plantillas/checklist_etico_v1.md) y pulsa **Raw**.
    - Haz clic justo antes de «## 0. Ficha rápida del caso» y, con la tecla **Mayús** pulsada, haz clic al final de la última línea («Qué actualizaremos en el proyecto final»). Copia con `Ctrl + C`: es el formulario de **un** caso.
    - En el repositorio del equipo, entra en **`sprint-01`**, pulsa *Add file → Create new file*, llámalo `checklist_etico.md`, escribe el principio como abajo, pega el formulario (`Ctrl + V`) y pulsa **Commit changes**.

    ```text
    # Checklist ético · TurisData Canarias

    ## Caso 1 · Previsión de ocupación
    **Revisado por (otra persona):** Ana

    ## 0. Ficha rápida del caso
    ```

    Para cada caso siguiente, pegad otra copia debajo con su título `## Caso 2 · …`.

3. **Contestar los dos casos priorizados (10 minutos).** Trabajad de dos en dos: una persona **lee** cada pregunta y otra, que **no inventó ese caso**, la contesta y escribe. Empezad por las filas con **(★)**. En la columna `S/N/NA/?` ponéis **S** (sí), **N** (no), **NA** (no aplica) o **?** (no lo sé), y en la siguiente, una evidencia o acción que valga **solo para ese caso**:

    | Vale | No vale |
    |---|---|
    | «Las reseñas pueden contener nombres de personas; se quitan antes de analizarlas» | «Hay que cumplir el RGPD» |
    | «El país de origen podría hacer de sustituto de la nacionalidad; no se usará para decidir depósitos» | «Se evitarán los sesgos» |

    Cada **N** o **?** en una pregunta (★) se apunta en la tabla de riesgos del apartado 10. En GitHub se edita **por turnos**: mientras una pareja escribe, la otra prepara sus respuestas en la nota del equipo; antes de editar, recargad la página. Si no da tiempo de contestar todo, cerrad las filas (★) y dejad el resto para vuestro tiempo de equipo antes del Sprint 2.

4. **Los tres casos resumidos (4 minutos).** Pegad otra copia del formulario por caso, con el título `## Caso 3 · … (resumido)`. Rellenad solo el apartado 0, las filas (★) y el apartado 10; las demás filas pueden quedar vacías.

5. **Semáforo y paso al informe (5 minutos).** En el apartado 10 de cada caso marcad **verde, ámbar o rojo** y escribid la justificación en tres líneas (ejemplo, ámbar: «las reseñas pueden incluir nombres; se quitan antes de analizarlas y la directora revisa el resumen»). Después, la persona del informe pasa a `informe_oportunidades.md`:

    - **Apartado 4:** las notas de impacto y facilidad, la frase de cada caso y el criterio.
    - **Apartado 5:** por caso, el semáforo, un riesgo propio con su medida y el **nivel del AI Act** orientativo (un chatbot de reservas es de nivel *limitado*, porque hay que avisar de que es una máquina; mirad el apartado 20 de los [apuntes](../../1_Teoria/apuntes/apuntes_ia_conceptos_y_etica.md)). Dejad la advertencia «verificar calendario vigente».

**Qué deberíais ver.** En `sprint-01/`, `checklist_etico.md` con cinco bloques: dos completos y tres con «(resumido)», cada uno con su semáforo y su justificación. Y en `informe_oportunidades.md`, los apartados 4 y 5 con una fila por caso, sin riesgos del tipo «cumplir el RGPD».

**Hecho cuando:** los cinco casos tienen notas, frase y semáforo, y los dos priorizados tienen el checklist completo (si el tiempo no llega, al menos las filas (★), con lo pendiente anotado en el tablero).

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| No sabemos si hay datos personales | No siempre se ve a simple vista. | Buscad nombres, correos, teléfonos, fotos de caras o reservas con nombre. Si hay, anotad cuáles y cómo los quitaréis (apartado 19 de los apuntes). |
| Todo está en «S» y sin evidencia | El checklist se ha convertido en un trámite. | Escribid en cada fila de qué dato o de qué persona se trata. Sin evidencia, cambiad a **?** y apuntad el riesgo. |
| No sabemos qué nivel del AI Act poner | Es una norma larga. | Poned el más probable según los ejemplos del apartado 20 de los apuntes y añadid «verificar calendario vigente». |
| Un caso priorizado sale en rojo | El riesgo es alto tal como está planteado. | No es un fallo: decidid si cambiáis el caso o pasáis al siguiente de la matriz, y escribid el porqué. |
| No da tiempo de terminar los dos checklists | El formulario tiene muchas preguntas. | Cerrad las filas (★) y el apartado 10, anotad lo pendiente en una tarjeta y completadlo en vuestro tiempo de equipo. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_01_paso_3.md) · [Ficha del reto](Reto_Sprint_01.md) · [Paso 5 →](Reto_Sprint_01_paso_5.md)
<!--/nav-->
