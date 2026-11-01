# Paso 1 · Preparar el terreno y repetir el baseline (día 1, 130 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 2 →](Reto_Sprint_15_paso_2.md)
<!--/nav-->

1. Fijar la semilla, anotar las versiones y crear el registro con la plantilla.
2. Definir la partición común y escribir qué modelos se van a probar y por qué.
3. Repetir el *baseline* y anotarlo como primera fila del registro.
4. Entrenar el primer modelo clásico y anotarlo.

**Cómo se hace**
- **Semilla y versiones (25 minutos).** Del cuaderno `S15_01` copiad a un fichero común (`utilidades.py`) las funciones `fijar_semillas`, `registrar` y `experimento`, y que **todo el equipo use la misma**. Fijad una semilla, por ejemplo `SEMILLA = 42`, y anotad las versiones (`python --version` y `pandas.__version__`, `sklearn.__version__`) en la primera celda de `03_modelos.ipynb`. **No se cambia la semilla hasta que salga un resultado bonito.**
- **El registro.** Copiad la plantilla como `registro.csv`. Cada columna tiene su función:

| Columna | Qué se anota |
|---|---|
| `id` | Un número que sube con cada prueba (1, 2, 3…) |
| `fecha`, `responsable` | Cuándo y **quién** hizo la prueba (clave para demostrar que participa todo el equipo) |
| `modelo`, `hiperparametros` | Qué modelo y con qué ajustes |
| `datos_hash`, `semilla` | Una huella corta de los datos y la semilla usada, para saber con qué se hizo |
| `metrica`, `valor_cv`, `desv_cv` | La métrica que fijasteis en el Sprint 14, su media y su desviación en validación cruzada |
| `tiempo_s`, `notas` | Cuánto tardó y lo que habéis aprendido; aquí se marca también si el código lo generó una IA |

- **Partición común y plan (20 minutos).** Definid **una** partición para todo el equipo (temporal si hay series; por grupos si hay fotos del mismo objeto), guardadla y **no la cambiéis**. Reservad el test: no se toca hasta el paso 5. Escribid en la primera celda de texto qué vais a probar y por qué (por ejemplo, regresión logística, bosque, boosting y una red). **No vale «probar 200 combinaciones y quedarse con la mejor».**
- **Baseline (30 minutos).** Repetid el modelo del Sprint 14 con la misma partición y anotadlo con `experimento(...)`: será la fila 1.
- **Primer modelo (55 minutos).** Una persona entrena el primer modelo clásico mientras las demás preparan el siguiente. Anotad la fila con el nombre de quien lo ha hecho.

**Qué deberíais ver.** Un `registro.csv` con al menos 3 filas (*baseline*, primer modelo y alguna prueba más) y las columnas rellenas, y el cuaderno ejecutándose de arriba abajo con las mismas cifras en dos ejecuciones seguidas (señal de que la semilla funciona). El *baseline* tiene la métrica más baja o similar a la de un modelo que no sabe nada.

**Hecho cuando:** hay semilla, versiones, partición común, plan escrito y el registro tiene el *baseline* y al menos un modelo más.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_15.md) · [Paso 2 →](Reto_Sprint_15_paso_2.md)
<!--/nav-->
