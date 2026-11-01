# Paso 4 · Elegir el candidato sin tocar el test (día 3, 70 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 5 →](Reto_Sprint_15_paso_5.md)
<!--/nav-->

1. Calcular media ± desviación de cada modelo.
2. Comparar teniendo en cuenta la incertidumbre y añadir coste y complejidad.
3. Elegir el candidato y escribir la justificación de una página.

**Cómo se hace**
- **Media ± desviación (15 minutos).** Con el registro, haced una tabla con una fila por modelo y la mejor prueba de cada uno. Si dos modelos se **solapan** (la diferencia entre sus medias es menor que su desviación), la diferencia puede ser **ruido**.
- **Coste y complejidad (15 minutos).** Añadid el tiempo de entrenamiento (`tiempo_s`), el tamaño o la dificultad de mantenerlo y lo fácil que es explicar su decisión.
- **Elegir (15 minutos).** Si dos modelos van casi igual, **elegid el más simple y explicadlo**. No se mira el test.
- **Escribir `justificacion_candidato.md` (25 minutos).** Una página con esta tabla (rellenad con vuestras cifras) y unas líneas debajo que digan por qué gana:

| Modelo | Métrica (media ± desv.) | Tiempo | Explicabilidad | Comentario |
|---|---|---|---|---|
| Baseline | | | | |
| Modelo A | | | | |
| Modelo B | | | | |
| Neuronal | | | | |

  Si vais a por el nivel extra, añadid una **hipótesis de por qué gana**: por ejemplo, «los datos tienen relaciones no lineales entre antelación y canal que un árbol captura mejor que una regresión».

**Qué deberíais ver.** Un candidato elegido con una frase del tipo «Elegimos X (0,71 ± 0,02) frente a Y (0,72 ± 0,04): la diferencia puede ser ruido y X es 15 veces más rápido» (cifras de ejemplo).

**Hecho cuando:** `justificacion_candidato.md` tiene la tabla comparativa y el candidato razonado, y nadie ha mirado el test.

<!--nav-->
---

[← Paso 3](Reto_Sprint_15_paso_3.md) · [Ficha del reto](Reto_Sprint_15.md) · [Paso 5 →](Reto_Sprint_15_paso_5.md)
<!--/nav-->
