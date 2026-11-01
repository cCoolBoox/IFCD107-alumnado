# Paso 3 · Comprobar que no hay fugas y tutoría (día 2, 60 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 4 →](Reto_Sprint_15_paso_4.md)
<!--/nav-->

1. Contestar la lista de fugas en una celda de texto de `03_modelos.ipynb`.
2. Corregir lo que falle y repetir las pruebas afectadas.
3. Ir a la tutoría técnica de 20 minutos con el docente.

**Cómo se hace**
- **La lista (20 minutos).** Copiad estas cinco preguntas a una celda de texto titulada «Comprobación de fugas» y contestad Sí / No con una frase:
  1. ¿Las variables se conocerían **en el momento de decidir**?
  2. ¿El escalado, la imputación y la codificación se aprenden **solo con el entrenamiento** (dentro de un `Pipeline`)?
  3. ¿La partición respeta el **tiempo** o los **grupos**?
  4. ¿Se ha ajustado algo mirando el test? Si sí, hay que rehacer la evaluación.
  5. ¿La métrica es **demasiado buena para ser verdad**? Sospechad.
- **Si algo falla,** corregid y repetid esas pruebas; en el registro, anotad en `notas` que la fila anterior tenía una fuga.
- **Tutoría (20 minutos, el docente indica la franja).** Llevad la tabla del registro y contad **qué comparación estáis haciendo** y **qué fuga podría haber**. Anotad las respuestas.
- **El resto (20 minutos):** repasad el registro: columnas vacías, filas duplicadas y nombres de modelo distintos para el mismo modelo.

**Qué deberíais ver.** La celda «Comprobación de fugas» con cinco respuestas, un registro limpio y, si ha habido una fuga, una fila anotada que lo explica. Ninguna prueba con un resultado casi perfecto sin explicación.

**Hecho cuando:** la lista está contestada, el registro está limpio y la tutoría ha quedado anotada.

<!--nav-->
---

[← Paso 2](Reto_Sprint_15_paso_2.md) · [Ficha del reto](Reto_Sprint_15.md) · [Paso 4 →](Reto_Sprint_15_paso_4.md)
<!--/nav-->
