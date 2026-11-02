# Paso 2 · Elegir el brief (día 1, 15 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 2 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 3 →](Reto_Sprint_14_paso_3.md)
<!--/nav-->

1. Comparar los briefs candidatos con tres criterios.
2. Decidir y apuntar el brief elegido, **antes del descanso**: es el primer hito del día.

**En sencillo.** Elegir un proyecto «a ojo» suele acabar en discusiones. Para evitarlo, hacéis lo mismo que al elegir entre dos pisos: una tabla pequeña, una nota de 1 a 5 en cada criterio y se suma. Gana el que más puntos tiene y todo el mundo sabe por qué. No hay brief «correcto»: hay el que mejor encaja con vuestros datos, vuestro interés y el tiempo que tenéis. No hace falta saber de IA para puntuar; hace falta haber leído el paso anterior y los briefs.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Brief** | El encargo del cliente: una pregunta guía y unas pistas sobre datos y técnicas. |
| **Criterio** | Cada cosa por la que se compara: aquí, datos, interés y tiempo. |
| **Hito** | Un momento del plan que hay que cumplir. El de hoy: brief elegido antes del descanso y ficha subida antes de las 14:30. |
| **Brief libre** | Un proyecto propuesto por el equipo en lugar de uno de los cuatro. Tiene condiciones. |
| **Series temporales** | Datos ordenados por fechas, como la ocupación de cada día. Los briefs 1 y 4 son de este tipo. |

**Cómo se hace**

1. **Leer los cuatro briefs.** Esta tabla resume la pregunta de cada uno. El detalle (datos candidatos, técnicas y riesgos) está en la sección 2 de [`briefs_y_rubrica.md`](../../../../proyecto-final/briefs_y_rubrica.md): leed al menos el de vuestros candidatos.

    | Brief | Pregunta guía | Pensad en… |
    |---|---|---|
    | **1 · Demanda turística** | ¿Podemos predecir la llegada de turistas con 3–6 meses de antelación y qué factores la explican? | Series temporales. Carga de cómputo baja |
    | **2 · Salud de cultivos (visión)** | ¿Con qué fiabilidad se distingue una hoja sana de una enferma y cuándo no fiarnos? | Imágenes. Carga alta (GPU) |
    | **3 · Asistente de FP (LLM/RAG)** | ¿Puede un asistente responder sin inventar y cómo lo medimos? | Texto. Carga media |
    | **4 · Demanda eléctrica** | ¿Predecimos la demanda de las próximas 24 h mejor que un modelo de referencia? | Series temporales con calendario. Carga media |

2. **Puntuar de 1 a 5 en tres criterios.** Copiad la tabla en una hoja o pizarra. Cada persona puntúa **en silencio** y después sumáis las notas de todo el equipo, brief por brief:

    - **Datos reales accesibles hoy:** 1 si no conocéis ni una fuente con licencia clara; 5 si ya sabéis dónde descargarlos.
    - **Nos interesa:** 1 si os da igual; 5 si os apetece trabajar en ello cuatro sprints.
    - **Se puede terminar en el tiempo que hay:** pensad en unas 54 horas de proyecto. Un brief con GPU y mucho entrenamiento (el 2) o con documentos que preparar (el 3) puntúa más bajo si dudáis.

    ```text
    | Brief                  | Datos (1–5) | Interés (1–5) | Tiempo (1–5) | Total |
    |------------------------|-------------|---------------|--------------|-------|
    | 1 · Demanda turística  |             |               |              |       |
    | 2 · Salud de cultivos  |             |               |              |       |
    | 3 · Asistente de FP    |             |               |              |       |
    | 4 · Demanda eléctrica  |             |               |              |       |
    ```

    Ejemplo de una fila con tres personas: datos 4 + 5 + 4, interés 3 + 4 + 5, tiempo 4 + 4 + 3 → total 36. Si dos briefs empatan, desempatad con el primer criterio: sin datos no hay proyecto.

3. **Decidir y apuntar.** Marcad el brief con más puntos y escribid en la nota del equipo, en una frase, cuál es y por qué (por ejemplo, «Brief 4: es el que más puntos suma y ya sabemos dónde están los datos»). Decídselo al docente **antes del descanso**. Dos equipos pueden elegir el mismo brief, pero **cada uno define su propia pregunta y su propia métrica**: partid del *canvas* del paso 1.

4. **Brief libre (solo si queréis uno propio).** Es posible si lo presentáis en la ficha **antes de las 14:30 del día 1** y se cumple todo esto: (1) pregunta clara con métrica de éxito; (2) datos reales, accesibles y con licencia **ya identificados**; (3) cumple R1 a R11; (4) dificultad parecida a la de los otros; (5) sin datos personales sensibles. Si dudáis, elegid uno de los cuatro: no se pierde nada.

**Qué deberíais ver.** Una tabla con las puntuaciones de todo el equipo, un total por brief, un brief marcado como elegido y una frase que explica la elección.

**Hecho cuando:** el equipo ha elegido su brief, lo ha apuntado y todo el mundo sabe cuál es.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Dos briefs tienen los mismos puntos | Empate. | Desempatad con el criterio de los datos: elegid el que tenga una fuente con licencia clara. |
| Cada persona quiere un brief distinto | Falta un método para decidir. | Puntuad en silencio, sumad y aceptad el resultado; es mejor un brief que a todos les parece «bien» que uno que a uno le encanta y a los demás no. |
| Os gusta el brief 2 pero os preocupa el tiempo de entrenamiento | Necesita GPU (se pide en Colab) y el entrenamiento tarda. | Puntuad bajo el tercer criterio y hablad con el docente antes de decidir. |
| Queréis un brief libre pero aún no tenéis datos | «A la espera de datos» no se acepta. | Elegid uno de los cuatro, o encontrad primero los datos (paso 3) y presentad el libre en la ficha. |
| Otro equipo ha elegido el mismo brief | Está permitido. | Cada equipo define su propia pregunta y su propia métrica; no copiéis la del otro. |
| Se acerca el descanso y no habéis decidido | El brief es el primer hito del día. | Haced la tabla de puntuación ya y decidid con el resultado; se puede afinar la pregunta después. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_14_paso_1.md) · [Ficha del reto](Reto_Sprint_14.md) · [Paso 3 →](Reto_Sprint_14_paso_3.md)
<!--/nav-->
