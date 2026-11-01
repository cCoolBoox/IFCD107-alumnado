# Paso 1 · Planning, píldora y taller (día 1, 75 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 1 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 2 →](Reto_Sprint_14_paso_2.md)
<!--/nav-->

1. Leer las reglas del proyecto y repartir los roles del sprint.
2. Escuchar la píldora de teoría sobre cómo formular un proyecto de IA.
3. Hacer el taller de Design Thinking y salir con uno o dos briefs candidatos y un *canvas* borrador.

**En sencillo.** Hoy **no se programa**. Empieza el proyecto final: cuatro sprints en los que vais a hacer, como una consultora, un proyecto de IA entero. Antes de construir una casa se decide para quién es y qué necesita; aquí pasa igual. Hoy decidís **qué problema real vais a resolver, para quién y cómo sabréis que lo habéis resuelto**. Casi todos los proyectos de IA que fracasan lo hacen por una pregunta mal planteada, no por el modelo. Al acabar el día tendréis una hoja a lápiz (el *canvas*) y una o dos ideas candidatas. No hace falta saber Python ni IA: hace falta hablar, escuchar y anotar.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Brief** | El encargo del cliente en pocas líneas: una pregunta guía y unas pistas. Hay cuatro (turismo, cultivos, asistente de FP, energía) y se puede proponer uno libre. |
| **Cliente y Product Owner** | El docente. Decide qué le sirve y responde a vuestra ficha con un *go / no-go* (seguir o ajustar). |
| **R1 a R11** | Los once requisitos que cumple todo proyecto: métrica, datos con licencia, baseline, tres modelos, una red neuronal, demostrador, repositorio… |
| **Rúbrica de 100 puntos** | La tabla con la que se puntúa el proyecto final. |
| **Rol** | Un encargo dentro del equipo. Hay cuatro: *Scrum Master*, responsable técnico, responsable de datos y responsable de IA responsable. |
| **Rotar** | Cambiar de rol en cada sprint, para que todas las personas pasen por todo. |
| **Design Thinking** | Una forma de pensar un problema empezando por las personas que lo sufren. |
| **Canvas** | Una hoja con casillas donde cabe todo el proyecto: pregunta, cliente, decisión, datos y métrica. |

**Cómo se hace**

1. **Leer las reglas (parte de los 10 minutos de planning).** Abrid [`briefs_y_rubrica.md`](../../../../proyecto-final/briefs_y_rubrica.md) y leed solo dos cosas: la sección 1 (reglas comunes y la tabla de requisitos **R1 a R11**) y la sección 5 (la rúbrica de 100 puntos). Los briefs los miraréis en el paso 2. Anotad en una hoja **tres cosas que no entendáis** y preguntadlas ahora; no hace falta memorizar nada, solo saber qué se os va a pedir.

2. **Repartir los roles (el resto de los 10 minutos).** Son cuatro, y cada persona asume uno durante este sprint:

    - **Scrum Master:** cuida que el equipo trabaje bien y mantiene el tablero al día.
    - **Responsable técnico:** cuida que todo se pueda repetir (cuadernos que se ejecutan, versiones anotadas).
    - **Responsable de datos:** lleva las fuentes, las licencias y la calidad del dato.
    - **Responsable de IA responsable:** lleva los riesgos y la ética.

    Con tres personas, una asume dos roles. Los roles **rotan en cada sprint**, así que decidid ya la rotación de los sprints 15 y 16 y apuntadla en una nota del equipo; la copiaréis en la ficha del paso 4. Ejemplo con cuatro personas (nombres inventados):

    | Persona | Sprint 14 | Sprint 15 | Sprint 16 |
    |---|---|---|---|
    | Marta | Scrum Master | Responsable técnica | Responsable de datos |
    | Luis | Responsable técnico | Responsable de datos | Responsable de IA responsable |
    | Ana | Responsable de datos | Responsable de IA responsable | Scrum Master |
    | Pablo | Responsable de IA responsable | Scrum Master | Responsable técnico |

3. **Escuchar la píldora (25 minutos).** El docente explica cómo se formula un proyecto de IA. Mientras tanto, cada persona anota en su hoja las cinco casillas del *canvas*: la **pregunta de negocio**, **quién usa el resultado**, la **decisión que mejora**, los **datos** y la **métrica**. Si queréis repasar luego, están los [apuntes de la píldora](../../1_Teoria/apuntes/apuntes_formular_un_proyecto_de_ia.md).

4. **Hacer el taller de Design Thinking (40 minutos).** Seguid este orden:

    - **Empatía.** Pensad en un problema **real y cercano**. Preguntaos: ¿quién lo sufre?, ¿qué decisión se toma hoy sin datos?
    - **«¿Cómo podríamos…?».** Convertid el problema en preguntas abiertas, por ejemplo «¿Cómo podríamos saber con antelación qué reservas se van a cancelar?». Escribid cuantas queráis.
    - **Dos candidatos.** Quedaos con **uno o dos briefs** que encajen con vuestras preguntas (los cuatro briefs se detallan en el paso 2).
    - **Canvas borrador.** Copiad esta plantilla en papel o en una pizarra y rellenadla a lápiz para cada candidato:

    ```text
    CANVAS BORRADOR
    Pregunta de negocio (una frase): ¿Podemos ... para que ...?
    Quién usará el resultado:
    Decisión que mejora (y qué pasa hoy sin el modelo):
    Datos posibles (de dónde y si tienen licencia):
    Métrica con la que sabremos que funciona:
    ```

    Un ejemplo bien relleno (de los apuntes de la píldora): pregunta «¿Podemos predecir qué reservas se cancelarán para que la dirección decida qué habitaciones ofrecer con descuento?»; quién usa el resultado: la directora del alojamiento; decisión: cada lunes decide qué habitaciones ofrecer con descuento y hoy lo hace sin saber qué reservas se cancelarán; métrica: de negocio, «evitar X habitaciones vacías al mes»; técnica, por ejemplo el AUC. **Prueba de la decisión:** si no sabéis decir **quién hace qué de forma distinta gracias al modelo**, todavía no tenéis proyecto: reformulad.

**Qué deberíais ver.** Una nota del equipo con los cuatro roles, cada uno con su nombre, y la rotación prevista. Un *canvas* (a lápiz vale) con las cinco casillas rellenas para uno o dos briefs candidatos, donde la pregunta de negocio cabe en **una frase** y nombra a quien usará el resultado.

**Hecho cuando:** cada persona sabe su rol y tenéis uno o dos briefs candidatos con su *canvas*.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Somos tres personas y hay cuatro roles | Es lo previsto en tres personas. | Una persona asume dos roles; en la rotación, que no sea siempre la misma. |
| La pregunta dice «analizar el turismo» o «hacer algo con IA» | Es una pregunta vaga: no dice qué decisión mejora. | Aplicad la prueba de la decisión: ¿quién hace qué distinto gracias al modelo? Reescribid la pregunta con esa persona y esa decisión. |
| No se nos ocurre ningún problema | Falta un punto de partida. | Leed la pregunta guía de cada uno de los cuatro briefs (paso 2) y partid de la que más os llame; después adaptadla a algo cercano. |
| Nuestra idea necesita datos que no sabemos dónde conseguir | Sin datos accesibles no hay proyecto. | Apuntadlo en la casilla de datos como duda; se resuelve en el paso 3. Un proyecto «a la espera de datos» no se acepta. |
| No entendemos un requisito (R4, R6…) | Es normal el primer día. | Subrayadlo y preguntadlo en el planning; cada requisito se trabaja más adelante. |
| Hay dos ideas igual de buenas | Es lo que se resuelve en el paso 2. | Guardad las dos como candidatas: en el paso 2 las puntuáis y decidís. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_14.md) · [Paso 2 →](Reto_Sprint_14_paso_2.md)
<!--/nav-->
