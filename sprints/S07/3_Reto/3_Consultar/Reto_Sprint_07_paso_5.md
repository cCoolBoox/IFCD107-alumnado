# Paso 5 · Informe y README (día 2, 10 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md)
<!--/nav-->

1. Copiar la plantilla como `informe_modelado.md` y rellenarla con las cifras del cuaderno.
2. Escribir el README: semilla, versiones, cómo ejecutar y uso de la IA.
3. Preparar la entrega: revisión con la rúbrica, subida y autoevaluación (los 15 minutos siguientes).

**Cómo se hace**
- **El informe.** Abrid [`informe_modelado_plantilla.md`](../1_Trabajar/plantillas/informe_modelado_plantilla.md), pulsad *Raw*, copiad el texto y pegadlo en un archivo nuevo `informe_modelado.md`. Para el **nivel mínimo** bastan estas, en pocas líneas:

| Apartado de la plantilla | Qué escribís |
|---|---|
| 1 · Resumen para el gerente | Cinco líneas con euros: qué recomendáis, qué cuesta cada error y cuánto ahorráis frente a no hacer nada |
| 3 · Regresión | La tabla de MAE, RMSE y R² y la frase del error medio en euros |
| 4 · Clasificación | La tabla de métricas y la matriz de confusión con el umbral elegido |
| 5 · De las métricas a los euros | `COSTE_FN` y `COSTE_FP` con su razón, el umbral y el coste en test |

  Para el **nivel estándar**, completad también el 2 (variables usadas y excluidas), la sensibilidad del 5, el 6 (recomendación con cifras y límites) y el 7 (riesgos de IA responsable).
- **El README.** Cuatro cosas: `SEMILLA = 42`; las versiones (`!python --version` y `import sklearn; print(sklearn.__version__)` en una celda); cómo ejecutar (*abrir en Colab y ejecutar de arriba abajo*); y el uso de la IA (qué pedisteis y qué revisasteis). Añadid quién hizo qué.
- **La revisión con la rúbrica (5 minutos, al empezar la entrega).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y rellena la sección «Revisión con la rúbrica» del final de `informe_modelado.md`: un nivel de 1 a 4 por criterio y **una frase de prueba**.
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y después *Archivo → Descargar → Descargar .ipynb*; (2) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-07`**; (3) *Add file → Upload files* y arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube `reto_S07.ipynb` («Añado cuaderno del reto»), la B sube `informe_modelado.md` («Añado informe»), la C edita `README.md` («Completo README»). Los nombres de archivo, **en minúsculas y sin espacios**. El CSV va a `data/` del repositorio solo si aún no está.

**Qué deberíais ver.** En la carpeta `sprint-07` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), commits de personas distintas.

**Hecho cuando:** otra persona podría ejecutar el cuaderno siguiendo solo el README, la sección «Revisión con la rúbrica» del informe está rellena y todo está subido a `sprint-07/`.

**Después, 15 minutos de entrega:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-07/` (la parte de coevaluación se completa en la *review* del jueves 12/11, en el mismo fichero). En la *review* (5 minutos por equipo) enseñaréis la tabla comparativa de métricas, el umbral elegido y su coste en euros frente a «no hacer nada», y una frase de recomendación para el gerente. En la retrospectiva, pensad: ¿qué hipótesis de coste discutimos más? ¿Cómo cambia la decisión si cambia el coste? ¿Qué habríamos necesitado saber del hotel para afinar?

<!--nav-->
---

[← Paso 4](Reto_Sprint_07_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_07.md)
<!--/nav-->
