# Paso 4 · Recomendador de experiencias (día 2, 30 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 5 →](Reto_Sprint_09_paso_5.md)
<!--/nav-->

1. Separar valoraciones de entrenamiento y de prueba.
2. Montar al menos dos métodos y evaluarlos con RMSE y precision@3.
3. Programar `recomendar(id_usuario, n)`.
4. Probarla con 3 usuarios.

**Cómo se hace.** Es el trabajo de `S09_03`: reutilizad su código y comprobad que lo entendéis.

| Orden | Qué hacéis | Pista |
|---|---|---|
| 1 | Esconder el 20 % de las valoraciones como prueba y construir la matriz usuario × experiencia solo con el 80 % restante | `valoraciones.sample(frac=0.2, random_state=SEMILLA)`; las casillas vacías son `NaN` |
| 2 | Primer método: **popularidad** (la nota media de cada experiencia, igual para todos) | Es la referencia que hay que batir y la única opción para un huésped nuevo (*arranque en frío*) |
| 3 | Segundo método: **contenido** (se hace en clase en `S09_03`) o, si lo habéis hecho en casa, filtrado colaborativo o factorización | Cualquiera sirve, pero tiene que ser distinto de la popularidad |
| 4 | Medir los dos con **RMSE** (error de la nota, menos es mejor) y **precision@3** (de las 3 recomendadas, cuántas le gustaban, más es mejor) | Con pocos usuarios evaluables, una diferencia de 0,01 es ruido: no la vendáis como mejora |
| 5 | Una tabla *método · RMSE · precision@3* y una frase que explica cuál elegís | «Elegimos … porque su precision@3 es …» |
| 6 | Programar `recomendar(id_usuario, n)`: las `n` mejores experiencias **que el usuario no ha valorado**, con nombre, categoría, isla y nota prevista | Poned `-inf` en lo ya valorado antes de ordenar; es el mini-reto de `S09_03` |

Probad `recomendar` con **3 usuarios distintos** y comprobad dos cosas: que ninguna experiencia recomendada estaba ya valorada y que las recomendaciones cambian de una persona a otra. Solo los usuarios 1 a 300 tienen valoraciones.

**Qué deberíais ver.** La tabla comparativa de los dos métodos, la frase de elección y tres listas de `n` experiencias, distintas entre sí.

**Hecho cuando:** el recomendador está evaluado con valoraciones escondidas, `recomendar` funciona con 3 usuarios y no propone nada ya valorado.

<!--nav-->
---

[← Paso 3](Reto_Sprint_09_paso_3.md) · [Ficha del reto](Reto_Sprint_09.md) · [Paso 5 →](Reto_Sprint_09_paso_5.md)
<!--/nav-->
