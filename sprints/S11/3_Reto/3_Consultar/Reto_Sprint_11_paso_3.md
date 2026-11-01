# Paso 3 · Evaluación y análisis de errores (día 2, 20 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 4 →](Reto_Sprint_11_paso_4.md)
<!--/nav-->

1. Evaluar en la prueba (una sola vez) y sacar las métricas por clase.
2. Mirar la matriz de confusión y completar los ejercicios 3 y 4.
3. Elegir las fotos mal clasificadas (3 como mínimo, 6 como estándar) y rellenar la tabla de errores.
4. Buscar patrones entre los errores.

**Cómo se hace**
- **Evaluar.** Ejecutad las celdas de la sección 3: precisión de los dos modelos, `classification_report` y la **matriz de confusión** (filas = clase real, columnas = clase predicha; lo que queda fuera de la diagonal son los errores).- **Ejercicio 3.** Con la matriz `cm`, calculad `recall_clase` (la diagonal entre la suma de cada fila), `precision_clase` (entre la suma de cada columna) y `clase_mas_dificil`. Con ello sabréis qué clase falla más.
- **Ejercicio 4.** Completad `indices_errores(y_real, prob)`: devuelve los índices de las fotos mal clasificadas, **de más a menos confianza**. Los primeros son los más preocupantes: el modelo estaba seguro y se equivocó. La celda siguiente os enseña hasta diez, con la clase real, la predicha y la confianza.
- **Rellenar la tabla de errores.** Elegid las fotos y copiad la tabla en `analisis_errores.md`. En «Foto» poned la carpeta de la clase real y el nombre del fichero, por ejemplo `camping/img_031.png`:

| Foto | Verdadera | Predicha | Confianza | Hipótesis de causa | Mejora propuesta |
|---|---|---|---|---|---|
| `piscina/img_012.png` (ejemplo inventado) | Piscina | Hotel | 81 % | El edificio ocupa media imagen y la piscina es muy pequeña | Más ejemplos con la piscina en primer plano |

- **Buscar patrones.** ¿Los errores se juntan en un par de clases? ¿Son fotos oscuras o con ruido? ¿Hay etiquetas dudosas? ¿Fondos parecidos? La celda de los pares (`value_counts`) os dice cuáles se confunden más. Una hipótesis vale cuando **se ve en la foto**: «por falta de datos» no basta.

**Qué deberíais ver.** La precisión en la prueba de los dos modelos, el informe por clase, la matriz de confusión, entre cero y diez fotos mal clasificadas con su clase real y predicha, y la lista de pares más confundidos.

**Hecho cuando:** tenéis las métricas por clase y la matriz interpretada en una frase, y la tabla con al menos 3 errores (6 si vais al estándar), cada uno con hipótesis y mejora. **A partir de aquí la prueba no se vuelve a usar para decidir nada.**

<!--nav-->
---

[← Paso 2](Reto_Sprint_11_paso_2.md) · [Ficha del reto](Reto_Sprint_11.md) · [Paso 4 →](Reto_Sprint_11_paso_4.md)
<!--/nav-->
