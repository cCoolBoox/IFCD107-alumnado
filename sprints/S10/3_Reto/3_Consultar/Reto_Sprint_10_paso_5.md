# Paso 5 · Comparación justa (día 2, 25 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 5 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 6 →](Reto_Sprint_10_paso_6.md)
<!--/nav-->

1. Repetir el entrenamiento con varias semillas y calcular media ± desviación.
2. Medir el veredicto en la prueba **una sola vez**, con el MLP elegido y con la referencia.
3. Hacer el ejercicio 4 (¿la diferencia es real o es ruido?).
4. Añadir el coste: tiempo, complejidad y explicabilidad.

**Cómo se hace**
- **Varias semillas.** El bucle de la sección 4 ya entrena con tres semillas (1, 2 y 3). Si el MLP elegido es una variante, **cambiad en ese bucle los argumentos de `construir_mlp`** y volved a ejecutar antes de seguir. Calculad la media y la desviación del AUC; si el modelo clásico da siempre exactamente la misma cifra, el intervalo *bootstrap* del cuaderno es vuestra medida de incertidumbre.
- **El veredicto.** La sección 6 usa la prueba **una sola vez**: media de las 3 semillas para el MLP y el boosting, con la función `evaluar` del ejercicio 1. Apuntad los resultados y no la volváis a mirar para cambiar nada.
- **¿Real o ruido?** El *bootstrap* remuestrea la prueba 300 veces y da un intervalo para la diferencia de AUC. **Si el intervalo incluye el 0, no podéis decir que uno sea mejor.** Eso es el **ejercicio 4**: `hay_diferencia` (verdadero si el intervalo no contiene el 0) y `mejor_modelo` (`"MLP"`, `"Boosting"` o `"Empate"`).
- **El coste.** La tabla del cuaderno ya trae el tiempo de entrenamiento y el número de parámetros. Añadid la **explicabilidad** (explicar por qué un boosting dice «cancelará» es más fácil que explicar una red). Una red puede mejorar un 1 % y tardar 20 veces más.

**Qué deberíais ver.** Una tabla con dos filas (`Boosting de árboles` y `MLP (media de 3 semillas)`) y las columnas AUC, AP, F1, precisión, tiempo y parámetros; una línea `Diferencia de AUC (MLP − boosting): … · intervalo 95 %: […]`, un histograma con una línea roja en el 0 y `Veredicto estadístico: …`. Con estos datos lo esperable es que los dos queden muy cerca, y un «Empate» es un resultado perfectamente válido.

**Hecho cuando:** el ejercicio 4 pasa su comprobación, tenéis media ± desviación (o intervalo) de ambos enfoques y los números del coste apuntados.

<!--nav-->
---

[← Paso 4](Reto_Sprint_10_paso_4.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 6 →](Reto_Sprint_10_paso_6.md)
<!--/nav-->
