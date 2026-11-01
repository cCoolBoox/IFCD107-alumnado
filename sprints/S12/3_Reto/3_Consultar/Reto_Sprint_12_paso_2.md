# Paso 2 · Datos y modelos (día 2, 50 minutos, y día 3, 30 minutos)

<!--nav-->
> Sprint 12 · Reto «Escuchar al cliente» · paso 2 de 4 · [Ficha del reto](Reto_Sprint_12.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_12_una_pagina.md) · [Paso 3 →](Reto_Sprint_12_paso_3.md)
<!--/nav-->

1. Día 2, en paralelo: la parte A (reseñas) y la parte C (asistente), unos 25 minutos cada una.
2. Día 3: la parte B (ocupación), 30 minutos.
3. Cada parte se hace en un cuaderno propio, copia del de la práctica, y acaba con un resultado que se pueda contar.
4. Las cifras de los informes salen siempre del código, nunca de la memoria.

**Cómo se hace.** En Colab, abrid el cuaderno de la práctica (enlaces en el apartado 2), pulsad *Archivo → Guardar una copia en Drive*, cambiadle el nombre (`resenas`, `ocupacion` o `asistente_rag`) y quedaos con lo que necesitáis. Subid al panel izquierdo el fichero de datos que usa la parte. Aquí tenéis, para cada parte, el orden de trabajo y en qué sección del cuaderno está la pista. **No es el código**: lo escribís vosotros.

## 2.1 · Parte A · Reseñas (día 2, unos 25 minutos)

**Recibe y devuelve.** `resenas.csv` (columnas `id_resena`, `texto`, `nota`, `sentimiento` y `temas`) → un reparto del sentimiento, la exactitud de un clasificador en prueba, los temas más mencionados, un gráfico (`grafico_resenas.png`) y citas reales.

| Orden | Qué hacéis | Pista | Se comprueba con |
|---|---|---|---|
| 1 | Cargar el fichero y limpiar el texto (minúsculas, sin signos y **sin quitar «no»**) | `pd.read_csv`; sección 2 de `S12_03` | Un `print` de 3 reseñas limpias |
| 2 | Calcular el porcentaje de reseñas positivas, neutras y negativas y dibujarlo | `value_counts(normalize=True)` y `plt.savefig("grafico_resenas.png")` | El gráfico y los porcentajes suman 100 % |
| 3 | Entrenar un clasificador de sentimiento: partir **antes** de vectorizar y ajustar el vectorizador solo con el entrenamiento | `make_pipeline(TfidfVectorizer(...), LogisticRegression(...))`; sección 4 de `S12_03` | La exactitud en prueba |
| 4 | Ver dónde se equivoca: matriz de confusión | `ConfusionMatrixDisplay`, `classification_report` | La matriz de confusión |
| 5 | Contar cuántas reseñas negativas y cuántas positivas mencionan cada tema | Secciones 6 y 8 de `S12_03` (palabras clave y panel de quejas) | Una tabla tema × número de reseñas |
| 6 | Elegir las citas reales (3 como mínimo, 5 en el estándar) con su `id_resena` | Filtrar con `resenas[resenas["temas"].str.contains("ruido")]` | Las citas aparecen tal cual en `resenas.csv` |

**Ejemplo de lo que cuenta el informe.** «El 31 % de las críticas mencionan el ruido; el 22 % de los elogios, el desayuno» (cifras de ejemplo: las vuestras salen de vuestro código).

## 2.2 · Parte C · Asistente con RAG (día 2, unos 25 minutos)

**Recibe y devuelve.** Una pregunta → una respuesta que **cita el fragmento de la política** del que sale, o la frase «No consta en la política del alojamiento.» si el parecido es demasiado bajo.

| Orden | Qué hacéis | Pista | Se comprueba con |
|---|---|---|---|
| 1 | Trocear `politica_alojamiento.md` en fragmentos, cada uno con el título de su sección | `trocear(politica)`; sección 2 de `S12_06` | Contar los fragmentos |
| 2 | Convertir fragmentos y pregunta en vectores y recuperar el más parecido | `TfidfVectorizer` y similitud coseno: `recuperar(pregunta, k=3)`; sección 3 | «¿Hasta cuándo puedo cancelar gratis?» devuelve la sección de cancelaciones |
| 3 | Responder citando la fuente | `construir_prompt` y `generar`; sección 5 (el simulador sin internet vale) | La respuesta lleva un número de fragmento, por ejemplo `[1]` |
| 4 | Fijar un **umbral**: si la mejor puntuación es menor, responder «No consta…» | `responder(pregunta, umbral=0.15)`; sección 6 | «¿Tienen gimnasio?» responde «No consta…» |

**Qué deberíais ver al terminar el paso.** Tres cuadernos con resultados: el de reseñas con su gráfico y su exactitud, el del asistente que cita y sabe callar, y el de ocupación (parte B, de abajo) con su tabla de MAE.

## 2.3 · Parte B · Ocupación (día 3, 30 minutos)

**Recibe y devuelve.** `ocupacion_diaria.csv` (columnas `fecha`, `ocupacion_pct`, `temperatura_c`, `festivo` y `precio_medio`) → una tabla de MAE con el *baseline* y el modelo, un gráfico de la previsión a 7 días y una frase para el cliente.

| Orden | Qué hacéis | Pista | Se comprueba con |
|---|---|---|---|
| 1 | Cargar la serie y dibujarla | `pd.read_csv(..., parse_dates=["fecha"])`; sección 1 de `S12_01` | El gráfico se parece a la ocupación real del alojamiento |
| 2 | Partir **por fecha**: lo antiguo para entrenar y las últimas semanas para evaluar | Sección 2 de `S12_01`: reserva los últimos 91 días | Las fechas de entrenamiento terminan **antes** que las de prueba |
| 3 | Calcular el *baseline* («igual que la misma semana anterior») y su MAE | Sección 3 de `S12_01` | Un MAE en puntos de ocupación |
| 4 | Entrenar un modelo y calcular su MAE: SARIMAX o una red GRU | `SARIMAX(...)`, sección 5 de `S12_01`; o `GRU`, secciones 6 y 7 de `S12_02` (con escalado ajustado solo con el entrenamiento) | Otro MAE |
| 5 | Meter ambos MAE en **una tabla** y decir si el modelo gana de verdad | `100 * (baseline - modelo) / baseline`; sección 7 de `S12_01` | Un porcentaje de mejora (puede ser pequeño o negativo) |
| 6 | Dibujar la previsión a 7 días y escribir una frase para el cliente | Sección 6 de `S12_01` | Un gráfico con la previsión y una frase sin jerga |

**Ejemplo de frase para el cliente.** «El método simple se equivoca de media en 6,2 puntos de ocupación; nuestro modelo, en 4,7» (cifras de ejemplo: si el vuestro no mejora al simple, decidlo con claridad, es un resultado válido).

**Qué deberíais ver.** Los tres cuadernos ejecutados de arriba abajo, cada uno con su resultado final visible.

**Hecho cuando:** hay un gráfico y un porcentaje de sentimiento, un asistente que cita y dice «No consta…» a la pregunta del gimnasio, y una tabla de MAE con *baseline* y modelo.

<!--nav-->
---

[← Paso 1](Reto_Sprint_12_paso_1.md) · [Ficha del reto](Reto_Sprint_12.md) · [Paso 3 →](Reto_Sprint_12_paso_3.md)
<!--/nav-->
