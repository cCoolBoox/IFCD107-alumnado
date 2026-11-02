# Paso 1 · Teoría de storytelling (día 1, 20 minutos)

<!--nav-->
> Sprint 17 · Reto «La defensa» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_17.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_17_una_pagina.md) · [Paso 2 →](Reto_Sprint_17_paso_2.md)
<!--/nav-->

1. Escuchar la estructura de una buena historia: audiencia, mensaje, orden de las ideas.
2. Tomar notas **pensando en vuestro proyecto**, no en uno cualquiera.
3. Leer juntos los apuntes y repartir quién cuenta qué parte del relato.

**En sencillo.** Ya no queda nada por construir: el modelo y la memoria están terminados. Falta **contarlo** para que lo entienda quien escucha. Contar un proyecto técnico se parece a explicar a un vecino por qué le compensa cambiar de caldera: no le interesa el motor, quiere saber cuánto ahorra, qué riesgos hay y qué tiene que hacer mañana. En este paso se escucha la presentación del docente, se leen unos apuntes entre todas las personas y se contestan tres preguntas en voz alta. No hace falta saber nada nuevo de IA ni de programación: solo escuchar, apuntar y hablar con el equipo.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Tribunal** | Quien escucha y evalúa vuestra defensa: el cliente y su equipo directivo (el docente y, si procede, personas invitadas). **No son técnicos**. |
| **Audiencia** | Las personas a las que habláis. Antes de escribir nada hay que saber quiénes son, qué saben y qué les preocupa. |
| **Mensaje único** | Una sola frase que la audiencia pueda repetir mañana. Todo lo demás de la presentación la apoya o sobra. |
| **Pirámide de la comunicación** | Un orden de arriba abajo: primero la conclusión, después tres argumentos y al final los datos que los sostienen. |
| **Arco narrativo** | El orden en el que se cuenta la historia, en siete momentos: situación, complicación, pregunta, resolución, demostración, límites y riesgos, y llamada a la acción. |
| **Memoria congelada** | La memoria técnica del Sprint 16, que ya no se cambia. Es la **única fuente de cifras**: no se presentan resultados nuevos. |
| **Traducir la jerga** | Poner a cada término técnico una frase que entienda alguien sin formación en IA. |

**Cómo se hace**

1. **Escuchar y apuntar tres ideas.** El docente presenta [`S17_01_presentacion_Storytelling_y_defensa.pdf`](../../1_Teoria/S17_01_presentacion_Storytelling_y_defensa.pdf). **Cada persona** (no una por equipo) apunta, en una hoja o en el móvil, tres ideas que pueda usar en su proyecto, con este formato de dos columnas: lo que dice la charla y lo que haré yo. Un ejemplo de cómo quedan, con ideas que salen de los apuntes (las vuestras hablarán de **vuestro** proyecto):

    | Lo que dice la charla | Cómo lo uso en mi proyecto |
    |---|---|
    | «Habla para quien escucha, no para ti» | En vez de «exhaustividad de 0,70», diré «de cada 10 reservas que se cancelan, detectamos 7» |
    | «Si solo recuerdan una frase, ¿cuál es?» | Tengo que poder acabar la frase «Gracias a nuestro trabajo, el cliente puede ___, pero no debe ___» |
    | «Un resultado honesto cuenta mejor que un número bonito sin contexto» | Voy a decir dónde falla nuestro modelo en vez de esconderlo |

    Una nota como «hay que hablar claro» **no vale**: no dice qué haréis distinto. Una nota vale cuando nombra algo concreto de vuestro proyecto (una cifra, un gráfico, un término técnico).

2. **Leer los apuntes repartiéndoos las secciones.** Abrid los [apuntes](../../1_Teoria/apuntes/apuntes_storytelling_y_defensa.md). Cada persona lee **una sección** y se la cuenta al resto en dos frases, sin leer. Con 4 personas, una sección cada una; con 3, una persona lee las secciones 3 y 4. Lo que hay que sacar de cada una:

    | Sección | Qué buscar |
    |---|---|
    | 1 · La audiencia | La tabla «hablas para ti» frente a «hablas para ellos»: elegid una pareja y reescribid una frase vuestra de la misma manera |
    | 2 · El mensaje único | La fórmula (acción, evidencia y límite) y la diferencia entre «93 % de acierto» y «8 de cada 10, pero en móvil 6 de cada 10» |
    | 3 · La pirámide | Conclusión arriba, tres argumentos debajo y la evidencia de cada uno |
    | 4 · El arco narrativo | Los siete momentos y por qué pirámide y arco no se contradicen: la pirámide dice **cómo ordenar** (la conclusión, al principio) y el arco dice **cómo se desarrolla** el relato después |

    Si una palabra no se entiende, está en la «chuleta de vocabulario» (sección 13 de los apuntes).

3. **Contestar en voz alta a las tres preguntas.** Cada persona responde y después el equipo se pone de acuerdo en **una sola respuesta**, que una persona escribe en el móvil o en papel (en el paso 2 pasará a la plantilla):

    - **¿Quién escucha el día 14?**
    - **¿Qué decisión tiene que tomar?**
    - **¿Qué le asusta?**

    Los apuntes dan una pista para un directivo que no es técnico: decide **si se usa o no** el modelo; le importan **dinero, tiempo, riesgos y qué hacer mañana**; sabe su negocio muy bien y la IA, poco o nada; y le asusta **equivocarse, que le vendan humo y los riesgos legales**. Una respuesta de equipo podría quedar así (es el ejemplo de los apuntes, el hotel que planifica su plantilla; la vuestra será otra):

    ```text
    Escucha: el director del hotel y su equipo directivo.
    Decisión: si usar el modelo para planificar la plantilla.
    Le asusta: pagar horas extra o dejar huéspedes sin servicio por una previsión que falla.
    ```

4. **Escribir las cuatro cosas que el tribunal tiene que saber.** El tribunal sale sabiendo cuatro cosas. Cada persona escribe **una frase por cada una**, mirando la memoria congelada, y las comparáis. Con el hotel de los apuntes quedarían así:

    | Qué tiene que saber el tribunal | Ejemplo de frase |
    |---|---|
    | Qué problema resolvéis | El hotel planifica la plantilla a ojo y se equivoca un 20 % arriba o abajo |
    | Qué habéis encontrado | Un modelo sencillo prevé la ocupación con 3 meses de antelación con un error del 7 % |
    | Qué recomendáis hacer | Usarlo para planificar la plantilla |
    | De qué no debe fiarse | No sirve para fijar precios y falla con eventos atípicos |

    Si las frases de las personas no coinciden, **todavía no hay mensaje común**: es normal, se resuelve en el paso 2.

5. **Repartir un primer borrador de quién cuenta qué.** Con las cuatro frases de arriba, apuntad **a lápiz** qué persona contaría cada parte (el problema, lo hecho y lo aprendido, la demo y los límites, la propuesta). Se confirmará en el paso 2. Todas las personas deben conocer **todo** el proyecto, porque las preguntas pueden ir a cualquiera.

6. **Comprobar que sabéis explicarlo.** Cada persona dice en una frase qué es un mensaje único, una pirámide y un arco narrativo, con sus palabras. Si alguien no puede, lo explica quien sí, y se repite.

**Qué deberíais ver.** Cada persona con tres notas concretas sobre su proyecto; el equipo con una respuesta común a «¿quién escucha y qué le importa?» (dinero, tiempo, riesgos y qué hacer mañana), las cuatro frases de lo que el tribunal tiene que saber y un reparto provisional escrito a lápiz.

**Hecho cuando:** cada persona sabe explicar con sus palabras qué es un mensaje único, una pirámide y un arco narrativo, y el equipo ha dicho en voz alta quién es su audiencia.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Mis tres notas son frases generales («hablar claro», «ser breve») | No dicen qué vais a cambiar en vuestro proyecto | Añadid «en mi proyecto, esto significa…» y una cifra, un gráfico o un término concreto |
| El equipo piensa que el público es «el profesor» | Se olvida que es el cliente y su equipo directivo, que no son técnicos | Releed la tabla del punto 3: decide si se usa el modelo y no sabe de IA. Si dudáis de quién es el cliente, preguntad al docente (hace de cliente) |
| No sabéis todavía cuál es vuestro mensaje | Es normal: el mensaje único se escribe en el paso 2 | Hoy basta con las cuatro frases. Si hace falta, completad «Gracias a nuestro trabajo, el cliente puede ___, pero no debe ___» |
| No entendéis la diferencia entre pirámide y arco | Se mezclan dos ideas parecidas | La pirámide ordena la información (conclusión primero, en la apertura); el arco cuenta la historia que la justifica, después |
| Las cuatro frases no coinciden entre personas | Cada una recuerda una parte distinta del proyecto | Releed juntas la conclusión de la memoria congelada y escoged una frase por cada punto |
| Se acaba el tiempo sin haber leído las secciones 3 y 4 | La charla y la lectura ocupan más de lo previsto | Leedlas al empezar el paso 2, antes de rellenar la pirámide y el arco |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_17.md) · [Paso 2 →](Reto_Sprint_17_paso_2.md)
<!--/nav-->
