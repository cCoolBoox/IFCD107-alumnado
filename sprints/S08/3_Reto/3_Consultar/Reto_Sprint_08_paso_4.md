# Paso 4 · Elegir el campeón (día 2, 45 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 5 →](Reto_Sprint_08_paso_5.md)
<!--/nav-->

1. Calcular la puntuación global de cada modelo con vuestros pesos y ver quién gana.
2. Probar otros pesos (análisis de sensibilidad) y anotar si el campeón cambia.
3. Evaluar al campeón en el test, **una sola vez**, y guardar el resultado.
4. Escribir tres o cuatro líneas: por qué ganó, por qué no ganó otro y qué cambiaría la elección.

**Cómo se hace**
- **Puntuación global.** Definid el diccionario `pesos` con las claves `"rendimiento"`, `"explicabilidad"` y `"coste"` (en decimales que sumen 1, por ejemplo 0.5, 0.3 y 0.2) y calculad `lb_pond = puntuacion_global(lb, pesos)`. El campeón es la **primera fila** (`campeon`, el nombre del modelo). Pistas: [código explicado del cuaderno](../../2_Practica/codigo_explicado/S08_06_leaderboard_plantilla.md).
- **Mirad la incertidumbre.** Un AUC de 0,81 no es mejor que uno de 0,80 si sus desviaciones son parecidas: la diferencia puede ser ruido. Si dos modelos empatan, es un resultado válido: elegid el más simple y explicadlo.
- **Sensibilidad.** Probad al menos otros dos conjuntos de pesos (el cuaderno trae `escenarios`: solo rendimiento, equilibrado y explicabilidad primero) y apuntad en una tabla qué campeón sale con cada uno. Si cambia fácilmente, decidlo: la recomendación depende de lo que valore el cliente.
- **El examen final.** Antes de seguir, comprobad en equipo que el campeón es el definitivo. Luego, en el cuaderno: reconstruid el campeón con `catalogo[campeon]()`, ajustadlo con **todo `X_train`**, calculad `auc_test_campeon` (su AUC sobre `X_test` con `roc_auc_score`) y guardadlo con `actualizar_test(campeon, auc_test_campeon)`. **No se evalúa ningún otro modelo en el test**, y el campeón no se cambia después de ver ese número.
- **Las líneas de la decisión.** Con el ejemplo de este modelo: «Campeón: … (AUC … ± …). No ganó … porque …. Si el cliente valorara solo …, elegiríamos …». Esas líneas van a la *model card*.

**Qué deberíais ver.** Una línea como `Campeón: … · AUC en validación cruzada 0.… · AUC en test 0.…` (el AUC de test está entre 0,65 y 0,85, y cerca del de validación; si está mucho más abajo, hay sobreajuste). En `leaderboard_S08.csv`, la columna `auc_test` tiene valor en **una sola fila**. Y una tabla de sensibilidad con el campeón de cada escenario.

**Hecho cuando:** hay un campeón elegido con vuestros pesos, la sensibilidad está probada y apuntada, y `auc_test` aparece en una única fila.

<!--nav-->
---

[← Paso 3](Reto_Sprint_08_paso_3.md) · [Ficha del reto](Reto_Sprint_08.md) · [Paso 5 →](Reto_Sprint_08_paso_5.md)
<!--/nav-->
