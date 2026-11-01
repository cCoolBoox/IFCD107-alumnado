# Paso 5 · Medir la seguridad del resultado (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 5 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 6 →](Reto_Sprint_05_paso_6.md)
<!--/nav-->

1. Obtener el p-valor, el intervalo de confianza y el R².
2. Calcular el tamaño del efecto.
3. Explicar cada cifra con palabras.

**Cómo se hace**
- **Cuatro variables** del cuaderno: `p_temp_control = ols_control.pvalues["temperatura_c"]`; `ic_festivo = tuple(ols_control.conf_int().loc["festivo"])`; `p_festivo_ttest = stats.ttest_ind(festivos, no_festivos, equal_var=False).pvalue` (el t de Welch compara la ocupación de los días festivos con la de los demás; separad antes las dos series); `r2_control = ols_control.rsquared`.
- **El tamaño del efecto** es cuántos puntos de ocupación cambia el resultado: con un grado más, o con un festivo. Ya lo tenéis en los coeficientes.
- **Explicar con palabras.** Una frase por cifra, como en esta plantilla: *«Con un festivo, la ocupación sube X puntos (intervalo de confianza entre A y B)»*. El p-valor, en una frase: *«¿sería raro ver esto si no hubiera efecto?»*; si es muy pequeño, sí lo sería. Escribid las frases en una celda de texto, porque son la base de la respuesta.

**Qué deberíais ver.** `Punto de control 4 superado`, con estos valores aproximados: `p_temp_control` ≈ 0,48 (la temperatura **no** es significativa una vez controlado el mes), `ic_festivo` ≈ (7,35 ; 10,87), `p_festivo_ttest` minúsculo y `r2_control` ≈ 0,58.

**Hecho cuando:** el punto de control 4 está superado y cada cifra tiene su frase explicada con palabras.

<!--nav-->
---

[← Paso 4](Reto_Sprint_05_paso_4.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 6 →](Reto_Sprint_05_paso_6.md)
<!--/nav-->
