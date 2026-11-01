# Paso 3 · Mitigar el sesgo y volver a medir (día 2, 80 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 3 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 4 →](Reto_Sprint_16_paso_4.md)
<!--/nav-->

1. Elegir una medida de mitigación para el sesgo que detectasteis.
2. Aplicarla y volver a medir, por subgrupo, antes y después.
3. Anotar los resultados en el cuaderno y en el registro de experimentos.

**Cómo se hace**
- **Elegir (5 minutos).** Una de estas, la que mejor encaje con vuestro sesgo:

| Medida | En qué consiste |
|---|---|
| Reponderar | Dar más peso al entrenar a los ejemplos del subgrupo que va peor |
| Ajustar el umbral por grupo | Decidir «cancelará» con una probabilidad mínima distinta para cada grupo |
| Añadir datos | Conseguir más ejemplos del subgrupo que falta |
| Limitar el uso | Decir en el aviso del demostrador: «no usar el modelo para el grupo X» |

- **Aplicar y medir (60 minutos).** Repetid la medición del paso 1 con la mitigación puesta y comparad **antes y después**, subgrupo a subgrupo. Mirad también el precio que se paga: si el *recall* sube, quizá la precisión baje y haya más falsas alarmas. No hay mitigación gratis; la memoria explica ese equilibrio.
- **Si el sesgo no se puede arreglar.** Faltan datos y no hay forma de conseguirlos: entonces se documenta como limitación, se avisa en el demostrador y se limita el uso. Esconderlo no es una opción.
- **Registro (15 minutos).** Apuntad la medida, las cifras de antes y de después y la decisión en el registro de experimentos del proyecto, y copiad la tabla al cuaderno.

**Qué deberíais ver.** Una tabla con el antes y el después por subgrupo y una frase de lectura honesta, del estilo: «El *recall* de móvil sube del 58 % al 68 % y el de web baja un punto; a cambio hay más falsas alarmas» (cifras de ejemplo).

**Hecho cuando:** hay una mitigación aplicada, medida por subgrupo y anotada en el cuaderno y en el registro de experimentos.

<!--nav-->
---

[← Paso 2](Reto_Sprint_16_paso_2.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 4 →](Reto_Sprint_16_paso_4.md)
<!--/nav-->
