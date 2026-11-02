# Paso 3 · La afirmación 2, paso a paso (día 1, 25 minutos)

<!--nav-->
> Sprint 2 · Reto «¿Nos fiamos de este informe?» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_02.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_02_una_pagina.md) · [Paso 4 →](Reto_Sprint_02_paso_4.md)
<!--/nav-->

1. Calcular la tasa de cancelación de cada fila en la hoja de cálculo.
2. Comprobar las dos cifras del informe (26,7 % y 15,8 %): salen bien.
3. Separar por tarifa, descubrir por qué el resultado se da la vuelta y explicarlo con palabras.
4. Elegir la carta y escribir la recomendación de tres líneas sobre el canal.

**En sencillo.** El informe dice que las reservas de la web intermediaria se cancelan menos que las del canal directo y que, por eso, conviene priorizarla. Lo comprobáis con la hoja de cálculo. Primero rehacéis las cuentas del informe y **salen bien**. Entonces, ¿dónde está el fallo? Pensad en dos cocineros: si uno cocina sobre todo platos fáciles, se le quema menos, pero no es mejor cocinero, solo cocina cosas fáciles. Aquí los «platos fáciles» son las reservas que casi nadie cancela. La solución es **separar por grupos y comparar dentro de cada grupo**. No hace falta Python ni fórmulas raras: solo sumar y dividir.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Tarifa flexible / no reembolsable** | La flexible permite cancelar. La no reembolsable no devuelve el dinero si se cancela. |
| **Canal directo / intermediaria** | Directo: se reserva con el propio alojamiento. Intermediaria: se reserva a través de una web de terceros que vende las habitaciones. |
| **Total y grupo** | El total junta todas las filas; un grupo es una parte (una tarifa, un canal). |
| **Celda y fórmula** | Cada casilla de la hoja es una celda: `D2` es la columna D, fila 2. Una fórmula empieza por `=`. |
| **Variable que confunde** | Un factor escondido que explica la diferencia sin que se vea. Aquí es la tarifa. |
| **Punto porcentual** | La diferencia entre dos porcentajes: de 30 % a 35 % hay 5 puntos porcentuales (se dice «5 puntos»). |

**Cómo se hace**

1. **Calcular la tasa de cada fila (5 minutos).** Con los datos del paso 1 en las columnas A a D, filas 2 a 5, escribid en `E1` el título `tasa` y en `E2` esta fórmula; pulsad Intro:

    ```text
    =D2/C2
    ```

    Qué hace cada línea:

    - `=` avisa a la hoja de que lo que sigue es una cuenta.
    - `D2/C2` divide las cancelaciones de la fila 2 entre las reservas de esa misma fila.

    Copiadla hasta `E5` (arrastrad hacia abajo la esquina de la celda, o copiad `E2` y pegad en `E3:E5`). Seleccionad `E2:E5` y pulsad el botón `%` de la barra de herramientas para verlas como porcentaje.

2. **Comprobar las cifras del informe (5 minutos).** El informe dice que el canal directo cancela el 26,7 % y la intermediaria el 15,8 %. Rehacedlo en dos celdas libres (por ejemplo, `A7` con el texto `directo` y `B7` con la fórmula; `A8` con `intermediaria` y `B8`), en formato porcentaje:

    ```text
    =(D2+D4)/(C2+C4)
    =(D3+D5)/(C3+C5)
    ```

    Qué hace cada línea:

    - La primera suma las cancelaciones de las filas 2 y 4 (las dos del canal directo) y las divide entre la suma de sus reservas. **No es la media de las tasas**: cada grupo pesa según sus reservas.
    - La segunda hace lo mismo con las filas 3 y 5 (las dos de la intermediaria).

    ¿Coinciden con el informe? Sí: **la cuenta está bien**. Entonces, ¿nos fiamos de la conclusión? No contestéis todavía; probad las pistas **de una en una**.

3. **Pista 1: comparar dentro de cada tarifa (5 minutos).** El informe solo mira el total. Mirad la columna E de dos en dos: `E2` y `E3` (tarifa flexible, directo frente a intermediaria) y `E4` y `E5` (no reembolsable). Preguntaos: dentro de cada tarifa, ¿qué canal cancela más? Apuntad las cuatro tasas en una tabla de vuestro borrador (tarifa, directo, intermediaria).

4. **Pista 2: quién vende qué (5 minutos).** ¿Qué parte de las reservas de cada canal es de tarifa flexible? Escribid, en celdas libres y en formato porcentaje:

    ```text
    =C2/(C2+C4)
    =C3/(C3+C5)
    ```

    Qué hace cada línea:

    - La primera divide las reservas flexibles del canal directo (`C2`) entre todas las del directo (`C2 + C4`).
    - La segunda hace lo mismo con la intermediaria (`C3` entre `C3 + C5`).

    **Pista 3.** Mirad otra vez `E2:E5`: ¿qué tarifa se cancela mucho más, la flexible o la no reembolsable? Juntad las dos pistas: ¿qué tarifa vende sobre todo cada canal?

5. **Completar la explicación (3 minutos).** Con estas palabras (*flexible · no reembolsable · mucho · poco · peor · mejor*), rellenad los huecos en vuestro borrador:

    > Dentro de cada tarifa, la intermediaria cancela …… que el directo. En el total parece …… porque vende sobre todo tarifa ……, que se cancela ……

6. **Elegir la carta, el veredicto y la recomendación (2 minutos).** La carta es la que dice «si separo por grupos, cambia el resultado» (tabla del [paso 2](Reto_Sprint_02_paso_2.md)). Para el veredicto, recordad que la cuenta sale pero los datos contradicen la conclusión. La recomendación son tres líneas con este molde, para el borrador:

    ```text
    Recomendamos …… (priorizar la intermediaria / no priorizarla / seguir mirando), porque ……
    Antes de decidir habría que mirar …… (por ejemplo, el coste o el margen de cada canal).
    ```

    Todo esto pasa a `dictamen.md` en el paso 5. Hoy se queda en el borrador.

**Qué deberíais ver.** En la columna E, las tasas 30 %, 35 %, 10 % y 12 % (filas 2 a 5). Los totales, 26,7 % para el directo y 15,8 % para la intermediaria (la hoja puede mostrar 26,67 % y 15,83 %). Que el 83 % de las reservas del directo son de tarifa flexible (1000 de 1200) y solo el 17 % de las de la intermediaria (200 de 1200). La explicación completada así: dentro de cada tarifa la intermediaria cancela **más** (35 frente a 30 y 12 frente a 10); en el total parece **mejor** porque vende sobre todo tarifa **no reembolsable**, que se cancela **poco**: la tarifa es la variable que confunde. La carta es la 2 · Paradoja de Simpson, el veredicto es *no fiable* y la recomendación no prioriza la intermediaria por su tasa de cancelación.

**Qué no vale.** Priorizar la intermediaria porque «cancela menos»; decir que «la intermediaria es peor y punto» (la diferencia es de 5 y 2 puntos: escribid «cancela algo más»); promediar 30 % y 10 %; dividir entre las 2.400 reservas del total.

**Hecho cuando:** tenéis las cuatro tasas, los dos totales y las dos partes de tarifa flexible en la hoja, y la explicación y la recomendación en el borrador.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `#DIV/0!` (o `#¡DIV/0!` en Excel) en la columna E | Se divide entre una celda vacía: los datos no están en `C` y `D` o la fórmula apunta a otra fila. | Comprobad que los datos están en las columnas A a D, filas 2 a 5, y que `E2` es `=D2/C2`. |
| Veis 0,3 en vez de 30 % | La celda está en formato número. | Seleccionad `E2:E5` y pulsad el botón `%`. |
| El directo da 13,3 % y la intermediaria 7,9 % | Habéis dividido entre las 2.400 reservas del total. | Dividid entre las reservas **de ese canal**: `=(D2+D4)/(C2+C4)`. |
| El directo os da 20 % | Habéis hecho la media de 30 % y 10 %. | Promediar tasas no vale, porque los grupos pesan distinto (1000 y 200 reservas). Sumad cancelaciones y reservas por separado. |
| La fórmula de `E4` o `E5` da un valor raro | La copia ha movido mal la referencia. | Seleccionad `E2`, copiadla y pegadla en `E3:E5`; `E5` debe ser `=D5/C5`. |
| La intermediaria sale peor en las dos tarifas y creéis que os habéis equivocado | Es el resultado correcto: es la paradoja de Simpson. | Repasad la pista 2: el directo vende sobre todo tarifa flexible, que se cancela más. |
| Las cifras de la hoja no coinciden con las del informe | Algún dato está mal escrito. | Comparadlo con `informe_cliente.csv`: reservas 1000, 200, 200, 1000 y cancelaciones 300, 70, 20, 120. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_02_paso_2.md) · [Ficha del reto](Reto_Sprint_02.md) · [Paso 4 →](Reto_Sprint_02_paso_4.md)
<!--/nav-->
