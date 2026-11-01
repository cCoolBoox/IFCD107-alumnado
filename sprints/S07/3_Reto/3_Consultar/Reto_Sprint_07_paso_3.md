# Paso 3 · Clasificación de la cancelación y elección del umbral (día 2, 15 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md) · [Paso 4 →](Reto_Sprint_07_paso_4.md)
<!--/nav-->

1. Separar train y test, y **no tocar el test** hasta el final.
2. Medir la referencia (siempre «no cancela») y la regresión logística; dibujar la matriz de confusión y las curvas ROC y PR.
3. Elegir el umbral que minimiza el coste con validación cruzada sobre train.
4. Usar el test **una sola vez**, al final, para dar el coste esperado.

**Cómo se hace**
- **Partir y modelos.** Como en `S07_03`: partición train/test y regresión logística. La referencia es un `DummyClassifier` que siempre dice «no cancela». Máximo 3 modelos por problema, referencia incluida.
- **Matriz y curvas.** Matriz de confusión en test (`S07_03`), y curvas ROC y PR con AUC y AP (`S07_04`: `roc_auc_score`, `average_precision_score`). Para el nivel mínimo basta la matriz.
- **El umbral.** El umbral es la probabilidad a partir de la cual decimos «se cancelará». Con `cross_val_predict` sobre train (como en `S07_03`) obtenéis las probabilidades; probad muchos umbrales (`np.arange(0.05, 0.96, 0.05)`) y calculad el coste de cada uno: `coste = FN × COSTE_FN + FP × COSTE_FP`. **Cuidado:** `coste_total` de `S07_03` trae por defecto FN = 3 y FP = 1; pasadle **vuestros** costes. El mejor umbral es el que **minimiza el coste**; no se lo dejéis elegir a la IA.
- **El test, una vez.** Con el umbral ya elegido, calculad el coste en test de tres formas: **sin modelo** (la referencia, que nunca avisa), con el umbral 0,5 y con el umbral elegido.

**Qué deberíais ver.** La matriz de confusión, una tabla o curva de coste por umbral con un mínimo claro y tres cifras de coste en test (sin modelo, umbral 0,5 y umbral elegido). El umbral elegido cuesta menos que el 0,5.

**Hecho cuando:** hay umbral elegido con vuestros costes, el coste en test está calculado una sola vez y nadie ha mirado el test para elegir el umbral.

<!--nav-->
---

[← Paso 2](Reto_Sprint_07_paso_2.md) · [Ficha del reto](Reto_Sprint_07.md) · [Paso 4 →](Reto_Sprint_07_paso_4.md)
<!--/nav-->
