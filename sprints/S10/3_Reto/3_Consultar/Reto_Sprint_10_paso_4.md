# Paso 4 · Diagnosticar el sobreajuste (día 2, 20 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 4 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 5 →](Reto_Sprint_10_paso_5.md)
<!--/nav-->

1. Mirar las curvas de vuestra mejor red.
2. Hacer el ejercicio 3 (`diagnostico`).
3. Escribir una frase de diagnóstico.

**Cómo se hace**
- **Leer las curvas.** Hay tres formas típicas:
  - **Entrenamiento baja y validación sube:** la red memoriza (sobreajuste). Se arregla con más regularización, menos neuronas o parando antes.
  - **Las dos curvas están altas y juntas:** la red es demasiado simple (subajuste).
  - **Las dos bajan y se estabilizan juntas:** buen ajuste.
- **Ejercicio 3.** Escribid `diagnostico(historial, margen=0.03)`: devuelve `"sobreajuste"` si la pérdida de validación **final** supera a su **mínimo** en más de `margen`, o si la de entrenamiento final es menor que la de validación final en más de `0.15`; si no, `"sin sobreajuste claro"`. Los `assert` del cuaderno os dicen si va bien. Aplicadlo a las tres semillas.
- **La frase.** Una frase para vuestra mejor red, con una cifra o una época: «Con la variante X, la validación deja de mejorar en la época 11 y el entrenamiento sigue bajando: hay un poco de sobreajuste, que la parada temprana corta a tiempo».

**Qué deberíais ver.** Tres líneas `MLP semilla 1: …` con `sobreajuste` o `sin sobreajuste claro`, y vuestra frase escrita junto a la gráfica.

**Hecho cuando:** el ejercicio 3 pasa su comprobación y la frase de diagnóstico está escrita (en el cuaderno y, resumida, en el informe).

<!--nav-->
---

[← Paso 3](Reto_Sprint_10_paso_3.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 5 →](Reto_Sprint_10_paso_5.md)
<!--/nav-->
