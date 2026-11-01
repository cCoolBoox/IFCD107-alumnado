# Paso 4 · Comparar con una librería (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 4 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 5 →](Reto_Sprint_05_paso_5.md)
<!--/nav-->

1. Ajustar los mismos dos modelos con `statsmodels`.
2. Reunir los tres coeficientes en la tabla `comparacion`.
3. Comprobar que coinciden con los vuestros.

**Cómo se hace**
- **Ajustar.** `ols_simple = smf.ols("ocupacion_pct ~ temperatura_c", data=diaria).fit()` y `ols_control = smf.ols("ocupacion_pct ~ temperatura_c + festivo + C(mes)", data=diaria).fit()`. `C(mes)` le dice a la librería que `mes` son categorías.
- **La tabla.** Un DataFrame `comparacion` de **3 filas × 2 columnas**: las filas son `pendiente_simple`, `efecto_temp_control` y `efecto_festivo_control`; las columnas, `desde_cero` (vuestros valores) y `statsmodels` (los de `ols_simple.params["temperatura_c"]`, `ols_control.params["temperatura_c"]` y `ols_control.params["festivo"]`).
- **Si no coinciden**, la causa más común es una tasa de aprendizaje inadecuada o pocas épocas. Probad con más vueltas antes de buscar un fallo en el código.

**Qué deberíais ver.** `Punto de control 3 superado` y la tabla con dos columnas casi idénticas (se admite una diferencia de 0,02).

**Hecho cuando:** `comparacion` tiene 3 × 2 valores que coinciden y el punto de control 3 está superado.

<!--nav-->
---

[← Paso 3](Reto_Sprint_05_paso_3.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 5 →](Reto_Sprint_05_paso_5.md)
<!--/nav-->
