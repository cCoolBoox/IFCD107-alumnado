# Paso 1 · Evaluar el modelo en el test y buscar dónde falla (día 1, 40 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 1 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 2 →](Reto_Sprint_16_paso_2.md)
<!--/nav-->

1. Evaluar el modelo candidato del Sprint 15 en el test, **una sola vez**, y anotar las métricas con su incertidumbre.
2. Adaptar los gráficos de `S13_02` y guardar todo en `notebooks/04_evaluacion.ipynb`.
3. Calcular la métrica por subgrupos y sacar la lista de los errores más frecuentes.

**Cómo se hace**
- **Evaluar.** Cargad el modelo ya elegido y pasadle el test. **Una vez.** Si el resultado no os gusta, no se vuelve a elegir mirando el test: se anota y se explica. Guardad la métrica con su intervalo o su variación.
- **Gráficos.** Abrid [`S13_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) y copiad lo que os sirva: matriz de confusión, curvas, importancia de variables, SHAP o Grad-CAM. Cada gráfico con un **título que diga la conclusión** («Las reservas por móvil se cancelan más»), no una descripción.
- **Subgrupos.** Elegid las columnas con categorías (país, canal, tipo de imagen…) y calculad la métrica para cada valor. Ejemplo con cifras inventadas: el *recall* es del 74,8 % en total, pero del 80 % en web y del 58 % en móvil. Eso es un sesgo que el número global esconde. Si el subgrupo tiene pocos casos, decid cuánta incertidumbre hay.
- **Errores.** Sacad la lista de los casos donde más falla (por ejemplo, las 20 cancelaciones que el modelo no detectó), mirad ejemplos reales uno a uno y anotad qué tienen en común. De ahí salen las limitaciones honestas de la memoria.
- **Tutoría.** En estos 40 minutos cada equipo tiene su franja de tutoría de sesgos y visualización: llevad el cuaderno abierto con la métrica por subgrupos.

**Qué deberíais ver.** Una tabla con las métricas del test y su incertidumbre, dos o tres gráficos con título-conclusión, una tabla con la métrica de cada subgrupo (aunque no haya diferencias, se anota) y una lista corta de errores típicos.

**Hecho cuando:** el cuaderno `04_evaluacion.ipynb` tiene la evaluación en test, los gráficos, los subgrupos y la lista de errores, y todo el equipo sabe qué subgrupo va peor.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_16.md) · [Paso 2 →](Reto_Sprint_16_paso_2.md)
<!--/nav-->
