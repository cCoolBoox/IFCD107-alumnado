# Paso 2 · Primeros modelos en el leaderboard (día 2, 30 minutos)

<!--nav-->
> Sprint 8 · Reto «Duelo de modelos» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_08.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md) · [Paso 3 →](Reto_Sprint_08_paso_3.md)
<!--/nav-->

1. Abrir `S08_06_leaderboard_plantilla` en Colab, guardar una copia y llamarla `reto_S08.ipynb`.
2. Ejecutar las celdas de preparación y de herramientas **sin cambiarlas**.
3. Registrar el modelo de referencia (*baseline*), la regresión logística, un árbol podado y un bosque.
4. Comprobar que la tabla tiene una fila por modelo.

**Cómo se hace**
- **Abrir y guardar una copia.** Abrid el [cuaderno](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_06_leaderboard_plantilla.ipynb), pulsad *Archivo → Guardar una copia en Drive* y luego *Archivo → Cambiar nombre* para llamarla `reto_S08.ipynb`. Trabajad siempre en **vuestra copia**.
- **Ejecutar en orden.** Ejecutad las celdas de arriba abajo; la primera (*Preparación*) siempre antes que las demás. La celda **«Herramientas del leaderboard»** no se toca: es la que garantiza **mismos datos, mismos folds y misma métrica** para todos los modelos.
- **Rellenar los huecos.** Donde hay `# TODO` y `...`, escribid vosotros el código. Cada modelo se registra con el patrón `registrar(evaluar_modelo(nombre, familia, hacer_pipe(...), explicabilidad, notas))`. Las pistas de los cuatro de este paso:

| Modelo (nombre) | Familia | Qué le pasáis a `hacer_pipe` | Explicabilidad |
|---|---|---|---|
| `baseline` | `referencia` | `DummyClassifier(strategy="prior")` (siempre predice lo más habitual) | 5 |
| `logistica` | `lineal` | `LogisticRegression(max_iter=1000)` con `escalar=True` | 4 |
| `arbol_podado` | `arbol` | `DecisionTreeClassifier(min_samples_leaf=80, random_state=SEMILLA)` | 5 |
| `random_forest` | `ensemble_bagging` | `RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2)` | 2 |

- **Dos tandas.** Los ejercicios 1 y 2 del cuaderno traen una comprobación (`assert`). La del ejercicio 2 pide 6 modelos, así que dará error hasta que estén también *boosting* y SVM (paso 3): es normal. Pistas de cuaderno: [`S08_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_01_arboles_decision.ipynb) (árbol) y [`S08_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_02_random_forest.ipynb) (bosque).

**Qué deberíais ver.** Una tabla ordenada por AUC con cuatro filas. El *baseline* sale con AUC cerca de 0,5 (el cuaderno lo comprueba) y el resto, por encima. Cada fila trae AUC medio, desviación, tiempos, tamaño y explicabilidad. En el panel de archivos de Colab (icono de la carpeta, a la izquierda) aparece `leaderboard_S08.csv`.

**Hecho cuando:** el leaderboard tiene `baseline`, `logistica`, `arbol_podado` y `random_forest`, y cada persona sabe explicar qué mide cada columna.

<!--nav-->
---

[← Paso 1](Reto_Sprint_08_paso_1.md) · [Ficha del reto](Reto_Sprint_08.md) · [Paso 3 →](Reto_Sprint_08_paso_3.md)
<!--/nav-->
