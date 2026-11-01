# Paso 1 · Preparar el cuaderno y los datos (día 1, 10 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 2 →](Reto_Sprint_09_paso_2.md)
<!--/nav-->

1. Crear en Colab el cuaderno `reto_S09_conocer_al_huesped.ipynb`.
2. Cargar `huespedes.csv` y mirar sus columnas.
3. Escalar las variables numéricas.
4. Repartir el trabajo de los pasos 2 y 3.

**Cómo se hace**
- **Crear el cuaderno.** En Colab: *Archivo → Cuaderno nuevo* y cambiadle el nombre a `reto_S09_conocer_al_huesped`. Trabajad en una sola pantalla compartida o compartid el cuaderno con el botón *Compartir* de Colab.
- **Cargar los datos.** Copiad al principio la celda «Preparación» de `S09_01` (la que define `dato(...)` y descarga los datos) y las importaciones. Fijad una semilla una sola vez, `SEMILLA = 42`, y usadla siempre que pidan `random_state`.
- **Mirar las columnas.** Con `head()` y `describe()`: `id_huesped` es solo un identificador y las otras 7 son números (`viaja_con_ninos` solo vale 0 o 1). Fijaos en las escalas: la edad va de 18 a 75 y el gasto diario, de 35 a 340.
- **Escalar.** Quitad `id_huesped` y pasad las 7 columnas por `StandardScaler().fit_transform(...)`: así todas pesan lo mismo. Guardad el resultado como `X`. Sin escalar, el gasto en euros mandaría sobre las demás.

**Qué deberíais ver.** Una tabla de 1200 filas y 8 columnas (el identificador y las 7 variables) y una matriz `X` de 1200 filas y 7 columnas, con la media de cada columna cerca de 0.

**Hecho cuando:** `X` existe y está escalada, y cada persona sabe qué parte del paso 2 o del 3 le toca.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_09.md) · [Paso 2 →](Reto_Sprint_09_paso_2.md)
<!--/nav-->
