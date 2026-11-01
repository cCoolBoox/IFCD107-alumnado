# Paso 2 · Entrenar con *transfer learning* y una referencia (día 2, 25 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 3 →](Reto_Sprint_11_paso_3.md)
<!--/nav-->

1. Completar `modelo_transfer` (ejercicio 2): copia congelada de la base preentrenada más una cabeza nueva.
2. Entrenar el modelo y hacer el ajuste fino del último bloque.
3. Entrenar una referencia «desde cero» con la misma arquitectura.
4. Anotar la precisión de validación de las tres versiones.

**Cómo se hace**
- **La idea.** Una red que ya ha aprendido a ver formas y texturas se **reutiliza**: se **congelan** sus capas (no cambian) y solo se entrena la **cabeza** (las capas nuevas que dan una respuesta por clase). Después, el **ajuste fino** (*fine-tuning*) descongela el último bloque y lo ajusta con una tasa de aprendizaje muy baja. Pista: [`S11_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_02_transfer_learning.ipynb).
- **Ejercicio 2.** Escribid `modelo_transfer(base_preentrenada, n_clases)`: haced una copia de la base con `keras.models.clone_model`, pasadle los pesos con `set_weights(...get_weights())`, ponedle `trainable = False` y añadid la cabeza con `con_cabeza`. **La base original no debe quedar congelada**: el `assert` de la celda os lo dirá.
- **Entrenar.** Ejecutad las celdas de la sección 2: se crea la base preentrenada con una tarea auxiliar (unos 15 segundos), se entrena con la base congelada y luego con el último bloque descongelado.
- **La referencia.** La celda siguiente entrena `desde_cero`, la misma red sin preentrenar. Anotad su precisión de validación con `desde_cero.evaluate(X_val, y_val, verbose=0)[1]`.
- **Solo validación.** Aquí se mide **únicamente en validación**. La prueba no se toca todavía.
- **Extra 🔴.** Con fotos reales en Colab podéis usar la rama de MobileNetV2 (sección 7: `USAR_INTERNET = True`, `TAM` de 96 a 160 y `construir_mobilenet(N_CLASES, pesos="imagenet")`). Es opcional y necesita internet.

**Qué deberíais ver.** Tres cifras de precisión de validación: base congelada, tras el ajuste fino y desde cero. Lo esperable es que el *transfer learning* sea igual o mejor que la referencia y aprenda con menos fotos; si no lo es, no es un error: anotadlo y pensad por qué.

**Hecho cuando:** `modelo_transfer` pasa sus comprobaciones y tenéis anotadas las tres cifras de validación.

<!--nav-->
---

[← Paso 1](Reto_Sprint_11_paso_1.md) · [Ficha del reto](Reto_Sprint_11.md) · [Paso 3 →](Reto_Sprint_11_paso_3.md)
<!--/nav-->
