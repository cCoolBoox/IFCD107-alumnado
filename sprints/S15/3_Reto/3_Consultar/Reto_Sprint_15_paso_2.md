# Paso 2 · Probar los modelos clásicos y el neuronal (día 2, 140 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 3 →](Reto_Sprint_15_paso_3.md)
<!--/nav-->

1. Entrenar al menos 3 modelos clásicos con la misma partición y anotar cada prueba.
2. Entrenar al menos un modelo neuronal (o el asistente LLM/RAG en el brief 3).
3. Ajustar 1–2 hiperparámetros clave de cada familia, solo con validación.
4. Comprobar que cada persona ha anotado al menos una fila.

**Cómo se hace**

Un reparto posible, si sois 3 o 4:

| Persona | Qué prueba | Minutos |
|---|---|---|
| A | Segundo y tercer modelo clásico (por ejemplo, bosque y boosting) | 50 |
| B | Modelo neuronal (o RAG/LLM en el brief 3) | 60 |
| C | Ajuste de 1–2 hiperparámetros de las familias de A (profundidad, número de árboles…) | 40 |
| D (si hay 4) | Repetir una prueba de otra persona con su código para comprobar que sale igual | 40 |

- **Cada prueba se anota nada más terminarla**, con `experimento(...)`; no esperéis al final del día. Si tarda mucho o usa una API de pago, trabajad con un subconjunto de datos y **anotad el coste en `notas`**.
- **Ajustar sin trampa.** Probad 2 o 3 valores de un hiperparámetro y anotad **cada valor como una fila**. Anotad también lo que no mejora («empeoró al aumentar la profundidad: sobreajuste»): también es información.
- **Si una prueba la ha generado una IA,** escribidlo en `notas`.
- **Que cada persona toque algo:** si una persona se queda sin fila, que pruebe un hiperparámetro de otra y la anote con su nombre.

**Qué deberíais ver.** Un `registro.csv` con unas 8–12 filas de personas distintas, con valores de `valor_cv` y `desv_cv` rellenos. Si dos modelos tienen medias casi iguales y desviaciones parecidas, es normal.

**Hecho cuando:** hay *baseline* y 3 modelos clásicos y 1 neuronal en el registro con la misma partición, y cada persona tiene al menos una fila.

<!--nav-->
---

[← Paso 1](Reto_Sprint_15_paso_1.md) · [Ficha del reto](Reto_Sprint_15.md) · [Paso 3 →](Reto_Sprint_15_paso_3.md)
<!--/nav-->
