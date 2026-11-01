# Paso 1 · Acordar las hipótesis de coste y abrir el cuaderno (día 1, 5 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md) · [Paso 2 →](Reto_Sprint_07_paso_2.md)
<!--/nav-->

1. Abrir un cuaderno nuevo en Colab con el nombre `reto_S07`.
2. Responder la pregunta central: ¿qué cuesta más, una cancelación no prevista o una falsa alarma?
3. Escribir una hipótesis de coste para cada error, con una frase de razón.

**Cómo se hace**
- **Abrir el cuaderno.** En [Colab](https://colab.research.google.com), *Nuevo cuaderno*, y ponedle `reto_S07`. En la primera celda copiad la celda «Preparación» de `S07_01` (la función `dato()` que descarga el CSV) y escribid `SEMILLA = 42`.
- **La pregunta central del informe.** Una **cancelación no prevista** es un falso negativo (FN): el modelo dice «no se cancelará», sí se cancela y la habitación queda vacía. Una **falsa alarma** es un falso positivo (FP): el modelo dice «se cancelará», no se cancela y el cliente llega y no hay sitio.
- **Hipótesis de coste.** Proponed una cifra en euros para cada error y **una frase de razón**. Ejemplos del enunciado: una cancelación no prevista cuesta **la mitad de una noche**, porque solo se revende la mitad de esas noches; una falsa alarma cuesta **una noche de compensación** (alojamiento en otro hotel y una disculpa). Para pasar «una noche» a euros, mirad el precio medio de `precio_noche` en los datos.
- **Escribidlas como variables**, con su razón en un comentario, para poder cambiarlas luego: `COSTE_FN = …  # razón` y `COSTE_FP = …  # razón`.

**Qué deberíais ver.** Una celda con `SEMILLA`, `COSTE_FN` y `COSTE_FP`, cada coste con su razón al lado, y el CSV cargado en un `DataFrame`.

**Hecho cuando:** el cuaderno abre y carga los datos, y las dos hipótesis de coste están escritas con su razón.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_07.md) · [Paso 2 →](Reto_Sprint_07_paso_2.md)
<!--/nav-->
