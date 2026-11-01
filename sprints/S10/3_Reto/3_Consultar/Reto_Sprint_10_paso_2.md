# Paso 2 · Primera red (día 2, 25 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 2 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 3 →](Reto_Sprint_10_paso_3.md)
<!--/nav-->

1. Comprobar que los datos están escalados **ajustando el escalador solo con el entrenamiento**.
2. Entrenar un MLP pequeño en CPU, con un máximo de 40 épocas.
3. Dibujar la curva de aprendizaje: error en entrenamiento y en validación.
4. Hacer el ejercicio 2 (el AUC de cada semilla).

**Cómo se hace**
- **Escalar sin fugas.** Escalar es poner todas las columnas en una escala parecida para que la red aprenda bien. El cuaderno ya lo hace en la sección 1 con `pre.fit_transform(X_ent)` (solo entrenamiento) y `pre.transform(...)` para validación y prueba. Mirad por qué: si el escalador viera la prueba, la red «se enteraría» de ella (eso es una **fuga**).
- **El MLP.** La sección 4 define `construir_mlp`: dos capas ocultas (64 y 32 neuronas), L2, *dropout*, parada temprana y un máximo de 40 épocas. Si preferís algo todavía más pequeño (por ejemplo, 2 capas de 32 neuronas y unas 30 épocas), cambiad los argumentos `capas` y `epochs`. Se entrena con **3 semillas**, y en CPU tarda pocos minutos.
- **Las curvas.** La sección 5 dibuja, para cada semilla, el error en entrenamiento y en validación a lo largo de las épocas. Mirad también cuántas épocas hizo cada una antes de parar.
- **Ejercicio 2.** Calculad en `aucs_mlp_val` el AUC de cada modelo sobre la **validación** y en `auc_mlp_medio` su media.

**Qué deberíais ver.** Tres líneas, una por semilla, del estilo `semilla 1: 17 épocas, AUC validación = 0.7… (máx.)`, tres gráficas con dos curvas cada una y, tras el ejercicio 2, `AUC de validación por semilla: …` con la media. La comprobación del cuaderno espera una media entre 0,6 y 0,85.

**Hecho cuando:** hay un MLP entrenado con su curva de aprendizaje, el ejercicio 2 pasa su comprobación y sabéis decir en una frase qué hace una época.

<!--nav-->
---

[← Paso 1](Reto_Sprint_10_paso_1.md) · [Ficha del reto](Reto_Sprint_10.md) · [Paso 3 →](Reto_Sprint_10_paso_3.md)
<!--/nav-->
