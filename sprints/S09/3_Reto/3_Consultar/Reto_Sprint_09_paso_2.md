# Paso 2 · Segmentar y elegir k (día 1, 20 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 3 →](Reto_Sprint_09_paso_3.md)
<!--/nav-->

1. Probar k-means con `k` de 2 a 8.
2. Calcular la silueta de cada `k` y dibujar la curva.
3. Elegir `k` con una razón técnica **y** una de negocio.
4. Escribir esa razón en una frase.

**Cómo se hace.** Es el mismo trabajo del ejercicio 2 de `S09_01`: podéis copiar de ahí la idea y adaptarla a vuestro cuaderno.

| Orden | Qué hacéis | Pista |
|---|---|---|
| 1 | Para cada `k` de 2 a 8, entrenar k-means sobre `X` | `KMeans(n_clusters=k, n_init=10, random_state=SEMILLA)` |
| 2 | Guardar la silueta media de cada `k` en un diccionario | `silhouette_score(X, etiquetas)`; va de −1 a 1 y **más alto es mejor** |
| 3 | Dibujar la curva: `k` en el eje horizontal y silueta en el vertical | Título y nombres de ejes, como en `S09_01` |
| 4 | Preguntaos si Lucía puede actuar con ese número de grupos | Entre 3 y 5 segmentos suele ser manejable; 12 no lo serían |
| 5 | Escribir **una frase con las dos razones** y ponerla en el cuaderno y en la cabecera de la ficha | «Elegimos k = … porque la silueta es … y, para el negocio, … grupos se pueden gestionar» |

**Qué deberíais ver.** Una curva con siluetas para `k` = 2, 3, …, 8 y un `k` elegido entre 3 y 5 (en `S09_01` el de mejor silueta cae en ese rango). No elijáis `k` **solo** por el número más alto de la silueta.

**Hecho cuando:** hay curva de silueta, un `k` elegido y la frase con las dos razones.

<!--nav-->
---

[← Paso 1](Reto_Sprint_09_paso_1.md) · [Ficha del reto](Reto_Sprint_09.md) · [Paso 3 →](Reto_Sprint_09_paso_3.md)
<!--/nav-->
