# Paso 3 · Variantes (día 2, 25 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 3 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 4 →](Reto_Sprint_10_paso_4.md)
<!--/nav-->

1. Probar **2 o 3 variantes** del MLP cambiando un solo ajuste cada vez.
2. Compararlas mirando **solo la validación**: el test no se toca.
3. Anotar en una tabla pequeña qué ha mejorado y qué no.

**Cómo se hace**
- **Qué cambiar.** `construir_mlp` ya tiene los botones: `capas` (más o menos neuronas, por ejemplo `(32,)` o `(128, 64)`), `dropout` (por ejemplo `0.5`), `l2` (por ejemplo `0.01`) y `tasa` (la tasa de aprendizaje, por ejemplo `3e-4`). También podéis probar otra paciencia en la parada temprana. **Cambiad una sola cosa por variante**, para saber qué ha causado el efecto.
- **Cómo comparar.** Entrenad cada variante y fijaos en la pérdida (el error) y el AUC **de validación**. Una tabla basta:

| Variante | Qué cambia | Error en entrenamiento | Error en validación | AUC en validación |
|---|---|---|---|---|
| Base | `capas=(64, 32)`, `dropout=0.3`, `l2=0.003` | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |
| Variante 1 | (lo que cambiáis) | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |
| Variante 2 | (lo que cambiáis) | (vuestra cifra) | (vuestra cifra) | (vuestra cifra) |

- **Cómo elegir.** Quedaos con la variante que mejor salga **en validación**. Si dos quedan casi iguales, escoged la más sencilla. Si miráis la prueba para decidir, ya no es una prueba.

**Qué deberíais ver.** Una tabla con la base y las 2–3 variantes, y una frase por variante: «mejoró», «empeoró» o «igual», con el número al lado. Que una variante no mejore es un resultado válido: lo importante es apuntarlo.

**Hecho cuando:** tenéis la tabla rellena, habéis elegido una variante mirando solo la validación y sabéis explicar por qué.

<!--nav-->
---

[← Paso 2](Reto_Sprint_10_paso_2.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 4 →](Reto_Sprint_10_paso_4.md)
<!--/nav-->
