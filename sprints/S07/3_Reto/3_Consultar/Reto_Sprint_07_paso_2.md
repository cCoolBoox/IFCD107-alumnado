# Paso 2 · Regresión del precio (día 1, 20 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md) · [Paso 3 →](Reto_Sprint_07_paso_3.md)
<!--/nav-->

1. Elegir las variables que **se conocen al reservar**; `cancelada` queda fuera.
2. Separar train y test, y medir el modelo de referencia (precio medio).
3. Ajustar la regresión lineal y comparar.
4. Probar una mejora y decidir si compensa. Contar el resultado en euros.

**Cómo se hace**
- **Variables sin fuga.** Haced una lista de las columnas del CSV y marcad cuáles se conocen **en el momento de reservar** (por ejemplo, tipo de habitación, mes de llegada, antelación, canal). **`cancelada` no se puede usar para predecir el precio**: es fuga, porque no se sabe hasta después. Apuntad la lista de usadas y excluidas: va en el informe.
- **Separar y medir la referencia.** Como en `S07_01`: `train_test_split` con 20 % de test y `random_state=SEMILLA`. El modelo de referencia (*baseline*) predice siempre la media del precio de entrenamiento (`DummyRegressor`). Medid MAE y RMSE sobre test.
- **Regresión lineal.** La de `S07_01` (`LinearRegression`), con las variables elegidas. Medid MAE, RMSE y R². ¿Mejora a la referencia?
- **Una mejora.** Interacciones o polinomio (`S07_01`) o regularización Ridge o Lasso (`S07_02`). Si apenas mejora, quedaos con el modelo sencillo y decidlo en el informe.
- **En euros.** Escribid una frase del tipo «nos equivocamos de media en X € por noche».

**Qué deberíais ver.** Una tabla con una fila por modelo (referencia, lineal y mejora) y las columnas MAE, RMSE y R². La lineal mejora a la referencia. Como orientación: en `S07_01`, con tipo de habitación y temporada, el cuaderno espera un R² por encima de 0,85 y un MAE de entre 5 y 15 €. Si el vuestro está muy lejos, mirad la «Ayuda 2».

**Hecho cuando:** la tabla de precio está en el cuaderno, sin `cancelada` entre las variables, y tenéis la frase del error medio en euros.

<!--nav-->
---

[← Paso 1](Reto_Sprint_07_paso_1.md) · [Ficha del reto](Reto_Sprint_07.md) · [Paso 3 →](Reto_Sprint_07_paso_3.md)
<!--/nav-->
