# Paso 1 · Elegir el modelo, cargarlo y fijar los costes (día 1, 4 minutos)

<!--nav-->
> Sprint 13 · Reto «Informe visual para dirección» · paso 1 de 4 · [Ficha del reto](Reto_Sprint_13.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md) · [Paso 2 →](Reto_Sprint_13_paso_2.md)
<!--/nav-->

1. Elegir el mejor modelo del curso y abrir el cuaderno plantilla en Colab.
2. Comprobar que el modelo se carga y que el cuaderno llega hasta el final sin errores.
3. Escribir el coste de cada error y el umbral.
4. Repartir el trabajo del paso 2.

**Cómo se hace**
- **Abrir la plantilla.** Pulsad el botón de Colab del apartado 2 y guardad una copia (*Archivo → Guardar una copia en Drive*), para no perder los cambios.
- **Cambiar el modelo.** Buscad la línea marcada `# >>> EDITA` en la celda «1. Datos y modelo» y poned vuestro modelo. Tiene que ser un objeto que sepa dar probabilidades (`predict_proba`) y que reciba `X_test`. Mantened las **semillas** y la separación entre entrenamiento y prueba, y usad **el mismo preprocesado con el que se entrenó**. Si el modelo no carga a tiempo, dejad el de ejemplo (regresión logística), que sí funciona, y decidlo en el pie del informe.
- **Fijar los costes.** En la celda «Parámetros del informe» cambiad `COSTE_FN` (lo que perdéis por cada cancelación que el modelo no detecta, es decir, una habitación vacía) y `COSTE_FP` (lo que cuesta avisar a quien sí iba a venir). Los valores de la plantilla (50 y 30) son de ejemplo. Preguntadle al docente, que hace de cliente; si no lo sabe, **proponed una hipótesis y escribidla**.
- **Elegir el umbral.** `UMBRAL` es la probabilidad a partir de la cual avisáis. Elegidlo con el gráfico de costes del cuaderno [`S13_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_01_visualizacion_resultados.ipynb), no por costumbre.

| Persona | Parte | Minutos |
|---|---|---|
| A | Modelo, costes y cuaderno (paso 1) | 4 |
| B | Los gráficos y sus títulos (paso 2) | 8 |
| C | Titular, viñetas y pie (paso 3) | 8 |
| D (si hay 4) | Prueba de los 30 segundos y revisión (paso 4) | 5 |

**Qué deberíais ver.** Una línea como `AUC en prueba: … · reservas de prueba: …` al final de la celda de datos y modelo, y ningún mensaje de error rojo.

**Hecho cuando:** el modelo se carga, `COSTE_FN`, `COSTE_FP` y `UMBRAL` están escritos, y cada persona sabe qué parte le toca.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_13.md) · [Paso 2 →](Reto_Sprint_13_paso_2.md)
<!--/nav-->
