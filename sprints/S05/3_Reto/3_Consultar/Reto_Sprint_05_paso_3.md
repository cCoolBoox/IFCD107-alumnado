# Paso 3 · Regresión lineal desde cero (día 2, 35 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 3 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 4 →](Reto_Sprint_05_paso_4.md)
<!--/nav-->

1. Escribir `gradiente_mse` y `entrenar` (el descenso del gradiente).
2. Ajustar el modelo simple (solo temperatura) y dibujar la curva de aprendizaje.
3. Ajustar el modelo con control (temperatura, festivo y mes).

**Cómo se hace**
- **La idea.** Si la ocupación fuera `a + b × temperatura`, queremos las `a` y `b` que dan la mejor recta. El **error** (MSE) mide lo mal que se ajusta; el **gradiente** indica en qué dirección cambiar `a` y `b` para que el error baje. El descenso del gradiente repite: calcular el gradiente, dar un pasito en la dirección contraria y volver a empezar. Si lo necesitáis, repasad [`S05_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_03_gradiente_regresion.ipynb): el ejemplo de una sola variable es el mismo.
- **`gradiente_mse(X, y, w)`** devuelve `(2/n) · Xᵀ(Xw − y)`. Con NumPy: `2 / len(y) * X.T @ (X @ w - y)`.
- **`entrenar(X, y, tasa, epocas)`** empieza con `w` a ceros y repite `epocas` veces: `w = w - tasa * gradiente_mse(X, y, w)`, guardando el MSE de cada vuelta en una lista `historial`. Devuelve `(w, historial)`. **Sin `scikit-learn`.**
- **Modelo simple.** Estandarizad la temperatura (restar la media y dividir entre la desviación) y añadid una columna de unos para la constante. Entrenad (probad con tasa 0,1 y unas 2000 épocas). Para dar la pendiente en **puntos por °C**, deshaced la estandarización: dividid el coeficiente entre la desviación de la temperatura. Guardadla en `pendiente_simple`.
- **Curva de aprendizaje.** `plt.plot(historial)` con título y ejes en español, y una línea de texto debajo: ¿baja y se estabiliza? Si sube sin parar o sale `NaN`, la tasa es demasiado grande: reducidla.
- **Modelo con control.** Las variables son la temperatura, `festivo` y los indicadores de mes: `pd.get_dummies(diaria["mes"], drop_first=True)` da las 11 columnas. Estandarizad todas, entrenad (unas 2000 épocas, tasa 0,1) y dividid cada coeficiente entre la desviación de su variable para volver a las unidades originales. Guardad `efecto_temp_control` y `efecto_festivo_control`.

**Qué deberíais ver.** Una curva que baja rápido y se aplana, y el mensaje `Punto de control 2 superado: simple -1.86 · con control: temp -0.09, festivo +9.11`. Fijaos en que **la temperatura casi deja de importar** cuando se controla el mes. En el nivel mínimo, el punto de control dará error en las líneas del modelo con control hasta que lo hagáis.

**Hecho cuando:** `pendiente_simple` sale ≈ −1,86, la curva de aprendizaje está dibujada y comentada y (en el estándar) el punto de control 2 está superado.

<!--nav-->
---

[← Paso 2](Reto_Sprint_05_paso_2.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 4 →](Reto_Sprint_05_paso_4.md)
<!--/nav-->
