# Paso 2 · Lluvia de ideas y elección de casos (día 1, 25 minutos)

<!--nav-->
> Sprint 1 · Reto «Auditoría de oportunidades de IA» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_01.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_01_una_pagina.md) · [Paso 3 →](Reto_Sprint_01_paso_3.md)
<!--/nav-->

1. Poner las 22 tarjetas sobre la mesa y elegir las que sirvan a TurisData.
2. Inventar al menos 2 casos propios y quedaros con 8 candidatos.
3. Descartar hasta tener 5 casos (3 descartes, con su motivo) y comprobar la mezcla: 3 modalidades, 2 casos propios y 1 sin IA.

**En sencillo.** Es como preparar la lista de la compra: primero apuntáis todo lo que se os ocurra, sin juzgar, y después os quedáis con lo que de verdad importa. Elegís ideas **para TurisData**, no para cualquier empresa. Hoy no hay que clasificar nada con rigor: solo decidir qué cinco casos vais a estudiar. No hace falta saber de IA; cada tarjeta cuenta su caso en dos o tres líneas.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Tarjeta de caso de uso** | Una ficha corta que describe una situación concreta donde podría ayudar la IA. Hay 22, de la C01 a la C22. |
| **Candidato** | Un caso que aún puede entrar o no entre los cinco. |
| **Caso propio** | El que inventáis vosotros a partir de un problema real del cliente. Si podéis señalar la tarjeta de la que sale, no es propio. |
| **Modalidad** | El tipo de dato con el que trabaja la IA: visión (imágenes), lenguaje (texto), voz, recomendación, datos tabulares o series, generativa (crea texto o imágenes) o robótica. |
| **Regla** | Una instrucción fija del tipo «si pasa X, haz Y». Si basta una regla, el caso no necesita IA. |

**Cómo se hace**

1. **Poner las tarjetas sobre la mesa (3 minutos).** Abrid [`tarjetas_casos_uso.md`](../../2_Practica/tarjetas_casos_uso.md) o la [versión para recortar](../../2_Practica/tarjetas_casos_uso_recortables.pdf). Hay **22 casos**: los 11 que trabajasteis en clase (C01, C02, C03, C04, C06, C07, C09, C13, C16, C18 y C22) y los otros 11, el «banco de ideas del reto» (C05, C08, C10, C11, C12, C14, C15, C17, C19, C20 y C21), que están en las dos últimas hojas del PDF. Podéis usar cualquiera.

2. **Elegir las útiles para TurisData (6 minutos).** Cada persona elige 2 o 3 que le parezcan **útiles para TurisData** y las relaciona con los dolores que contó el cliente en el Sprint 0. Tiene que poder decir en una frase por qué le sirve a la directora. Anotadlas en una tabla de la nota del equipo (o en una tarjeta del tablero) como esta, que usaréis de nuevo al final del paso:

    | Candidata | ¿Tarjeta o propia? | ¿Se queda? | Por qué |
    |---|---|---|---|
    | (ejemplo inventado) Resumen de las reseñas | Propia | Sí | Hay miles de reseñas y nadie las lee |
    | (ejemplo inventado) C08 · Contar personas en una excursión | Tarjeta | No | Ayuda poco a TurisData y exige muchas fotos |

3. **Inventar al menos 2 casos propios (7 minutos).** Partid de una **frustración del cliente** («las reseñas son miles y nadie las lee») y preguntaos «¿se podría ayudar con IA?». Cada caso propio, en una o dos frases: el problema real y lo que haría el sistema. **No vale** cambiar el nombre a una tarjeta, ni escribir solo una solución sin problema («hacer un chatbot»: ¿para qué problema?).

4. **Incluir un caso que no necesite IA (3 minutos).** Buscad uno que se resuelva mejor con una regla sencilla, por ejemplo «enviar un recordatorio 48 horas antes de que caduque la cancelación gratuita». Dos de las tarjetas de clase (C16 y C22) son de este tipo, y podéis inventar el vuestro: si lo inventáis, cuenta también como propio. Saber decir «aquí no hace falta IA» demuestra criterio.

5. **Quedaros con 5 y descartar 3 (6 minutos).** Si tenéis ocho candidatas, descartad tres según el **valor** para TurisData, los **datos** que haría falta conseguir y el **riesgo**. Después comprobad la mezcla y cambiad un caso si no se cumple:

    - **Al menos 3 modalidades** distintas entre los cinco.
    - **Al menos 2 casos propios.**
    - **Al menos 1 caso sin IA.**

    Apuntad **por qué** descartáis cada uno de los tres: lo contaréis en la *review*.

**Qué deberíais ver.** La tabla del equipo con las 8 candidatas (cada una marcada como tarjeta o propia), 5 con «Sí» y 3 con «No» y su motivo, y debajo una línea con la comprobación: «Modalidades: …; propios: …; sin IA: …». Los cinco casos no deben parecerse entre sí.

**Hecho cuando:** tenéis 5 casos elegidos (3 modalidades, 2 propios y 1 sin IA) y los 3 descartes con su motivo.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Los cinco casos son casi «predecir cancelaciones» | Todos piensan en lo mismo. | Que cada persona busque un tipo de dato distinto: texto (reseñas, correo), imágenes, recomendación… |
| No se nos ocurren casos propios | Falta un punto de partida. | Releed la entrevista del Sprint 0, elegid una frase del cliente y preguntaos «¿qué haría una persona para resolver esto hoy?». Ahí suele haber un caso. |
| Dudamos de si un caso es propio | Puede ser una tarjeta con otras palabras. | Buscad la tarjeta de la que sale: si existe, no es propio; cambiad el problema o el dato y decidid de nuevo. |
| No sabemos si un caso necesita IA | Hay que distinguir regla y aprendizaje. | Preguntaos si se puede escribir una regla («si pasa X, haz Y») sin ejemplos del pasado. Si sí, no hace falta IA (apartado 6 de los [apuntes](../../1_Teoria/apuntes/apuntes_ia_conceptos_y_etica.md)). |
| Nos gustan seis casos | Hay que descartar con un criterio, no con prisa. | Descartad el de menos valor para TurisData, el que exige datos que no existen o el de más riesgo, y anotad cuál fue el motivo. |
| No cuadra ninguna combinación de modalidades | Los casos se parecen en el tipo de dato. | Sustituid uno por una tarjeta de otra modalidad (visión, voz, recomendación…) y comprobad que sigue sirviendo a TurisData. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_01_paso_1.md) · [Ficha del reto](Reto_Sprint_01.md) · [Paso 3 →](Reto_Sprint_01_paso_3.md)
<!--/nav-->
