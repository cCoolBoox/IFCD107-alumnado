# Paso 4 · Demostrador y umbral de confianza (día 2, 15 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 5 →](Reto_Sprint_11_paso_5.md)
<!--/nav-->

1. Probar `clasificar_foto` con 2 o 3 fotos de la prueba.
2. Medir cobertura y acierto para varios umbrales con el ejercicio 5.
3. Elegir el umbral y apuntar la recomendación.

**Cómo se hace**
- **El demostrador.** Está en la sección 6 del cuaderno (queda bajo la línea «en casa» de la práctica, pero en el reto sí se hace). `clasificar_foto(ruta_imagen, umbral=0.7)` carga una foto y devuelve la **clase**, la **confianza** (lo seguro que está el modelo, de 0 a 1) y las probabilidades; si la confianza es menor que el **umbral**, en vez de la clase dice «revisar a mano». Probadla con 2 o 3 rutas de fotos de la prueba (`rutas_pru[0]`, `rutas_pru[1]`…) y ved qué responde.
- **Ejercicio 5.** Completad `cobertura_y_precision(prob, y_real, umbral)`: devuelve la **cobertura** (qué parte de las fotos decide el modelo solo) y la **precisión de las aceptadas** (qué parte de esas acierta). Un umbral alto da menos fotos automáticas, pero más fiables.
- **Elegir el umbral.** Para el estándar basta con el umbral que trae el cuaderno y explicar qué hace. Para el extra 🔴, calculad la tabla con varios umbrales **sobre validación** (`modelo.predict(X_val, verbose=0)`), porque la tabla del cuaderno usa las probabilidades de la prueba. Elegid el que equilibre fotos revisadas y errores evitados.
- **Una frase para el cliente.** Escribidla ya, con números: «Con un umbral de …, el modelo decide solo el … % de las fotos y acierta el … % de ellas; el resto lo revisa una persona».

**Qué deberíais ver.** La respuesta de `clasificar_foto` para cada foto, con su confianza (a veces «revisar a mano»), y una tabla con la cobertura y la precisión de las aceptadas para cada umbral probado.

**Hecho cuando:** `clasificar_foto` funciona con 2 o 3 fotos delante del equipo, `cobertura_y_precision` pasa sus comprobaciones y tenéis anotado el umbral elegido con su frase.

<!--nav-->
---

[← Paso 3](Reto_Sprint_11_paso_3.md) · [Ficha del reto](Reto_Sprint_11.md) · [Paso 5 →](Reto_Sprint_11_paso_5.md)
<!--/nav-->
