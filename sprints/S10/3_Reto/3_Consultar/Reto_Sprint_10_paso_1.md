# Paso 1 · Elegir el problema y reproducir la referencia (día 2, 15 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 1 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 2 →](Reto_Sprint_10_paso_2.md)
<!--/nav-->

1. Elegir **un problema**: cancelaciones (`cancelada`) o precio (`precio_noche`).
2. Abrir `S10_04` en Colab y ejecutarlo bloque a bloque, entendiendo cada uno.
3. Reproducir el modelo de referencia y anotar su métrica y su tiempo.
4. Fijar la partición entrenamiento / validación / prueba y no cambiarla nunca más.

**Cómo se hace**
- **Elegir el problema.** El cuaderno trae montado el de cancelaciones, así que es el camino más corto. Si elegís precio, seguid la sección 7 del cuaderno (hay que **quitar `precio_noche` de las entradas**). El otro problema es opcional.
- **Abrir el cuaderno.** Pulsad el [enlace de Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_04_reto_vale_la_pena.ipynb) y haced una copia (*Archivo → Guardar una copia en Drive*). **Ejecutad siempre primero la celda «Preparación»**, que descarga los datos.
- **Ir bloque a bloque.** Pulsad ▶ en cada celda y leed lo que pone antes. Los ejercicios 1 a 4 tienen un hueco (`...`) y dan error hasta que lo rellenéis: es lo normal. En este paso, haced el **ejercicio 1** (`evaluar`), la función que mide a todos los modelos por igual. Si no entendéis un bloque, preguntad antes de seguir.
- **La partición.** La sección 1 reparte 64 % entrenamiento, 16 % validación y 20 % prueba, con semilla fija. No toquéis ni la semilla ni los `random_state`. La validación sirve para **decidir**; la prueba, para el veredicto final y **una sola vez**.
- **La referencia.** La sección 3 entrena el boosting (`HistGradientBoostingClassifier`). Si vuestro equipo tiene un campeón del Sprint 8 (XGBoost, LightGBM, Random Forest…), usadlo en su lugar y compararéis con él. **No se cambia la referencia para que la red gane.**

**Qué deberíais ver.** Al ejecutar la partición, tres tamaños: `(3840, 35) (960, 35) (1200, 35)`. Al entrenar el boosting, una línea como `Boosting entrenado en 0.3 s · AUC validación = 0.73`. Un AUC de 0,5 sería lo mismo que tirar una moneda; uno cercano a 1,0 haría sospechar de una fuga de datos.

**Hecho cuando:** el cuaderno llega hasta el boosting sin errores, el ejercicio 1 pasa su comprobación y tenéis anotadas la métrica y el tiempo de la referencia.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_10.md) · [Paso 2 →](Reto_Sprint_10_paso_2.md)
<!--/nav-->
