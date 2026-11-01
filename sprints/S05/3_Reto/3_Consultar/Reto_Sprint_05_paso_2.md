# Paso 2 · Mirar los datos (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 2 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 3 →](Reto_Sprint_05_paso_3.md)
<!--/nav-->

1. Describir la serie y calcular la media de ocupación por mes.
2. Hacer al menos dos gráficos: ocupación por mes y ocupación frente a temperatura.
3. Escribir 2–3 observaciones con vuestras palabras.

**Cómo se hace**
- **Describir.** `diaria.describe()` muestra la media, la dispersión, el mínimo y el máximo. La media por mes sale con `diaria.groupby("mes")["ocupacion_pct"].mean()`.
- **Dos gráficos** con `matplotlib`: un diagrama de caja por mes (`boxplot`) y una nube de puntos de temperatura contra ocupación (`scatter`). Todos con **título y ejes en español** y con las unidades (`°C`, `%`).
- **Observaciones.** En la celda de texto «Mis observaciones» escribid 2–3 frases: ¿en qué meses hay más y menos ocupación? ¿Se ve una relación con la temperatura? ¿Coincide el calor con unos meses concretos? Es la base de vuestra respuesta al cliente.

**Qué deberíais ver.** Una ocupación alta en invierno (en torno al 78–79 % de media en enero, febrero y diciembre) y más baja de mayo a octubre (en torno al 60–63 %), y una nube de puntos que **baja de izquierda a derecha**: a más temperatura, menos ocupación. No hay `assert` en este paso: lo revisa el equipo.

**Hecho cuando:** hay dos gráficos con título y ejes en español y 2–3 observaciones escritas.

<!--nav-->
---

[← Paso 1](Reto_Sprint_05_paso_1.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 3 →](Reto_Sprint_05_paso_3.md)
<!--/nav-->
