# Paso 2 · Comparar los modelos y ver qué pesa (día 2, 10 minutos)

<!--nav-->
> Sprint 3 · Reto «Primer modelo en producción» · paso 2 de 6 · [Ficha del reto](Reto_Sprint_03.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md) · [Paso 3 →](Reto_Sprint_03_paso_3.md)
<!--/nav-->

1. Leer la tabla de modelos (el *leaderboard*) y apuntar cuál gana y por cuánto.
2. Escribir qué métrica miráis y por qué.
3. Ver qué variables pesan más (apartado 7 del cuaderno) y decir si tienen sentido.
4. Anotar los ajustes, para que otra persona pueda repetir el experimento.

**En sencillo.** AutoML es como un cocinero que prueba diez recetas con los mismos ingredientes y os enseña una clasificación. Vosotros no elegís la receta: elegís **con qué nota se compara** y **si tiene sentido lo que ha salido**. Ya entrenasteis el modelo en la práctica de AutoML (apartados 0 a 5 del cuaderno), así que aquí solo **leéis y anotáis**. Lo único delicado es qué nota mirar: hay una «de examen con preguntas nuevas» y otra «de ejercicios parecidos a los que ha estudiado», y solo la primera es honesta. No hace falta saber cómo funciona cada algoritmo.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **AutoML** | Herramienta que entrena y compara varios modelos por vosotros. |
| **Leaderboard** | La tabla de modelos candidatos, del mejor al peor. |
| **Ensamblado** | Un modelo que **combina varios** y reparte el voto entre ellos (`WeightedEnsemble_L2`). |
| **`score_test` y `score_val`** | La nota con reservas que el modelo **no ha visto** (las más recientes) y la nota con una parte de las reservas con las que entrenó. La que vale es `score_test`. |
| **ROC-AUC** | Una nota de 0,5 (como el azar) a 1 (perfecto): ¿ordena bien las reservas de más a menos riesgo? |
| **Importancia de variables** | Cuánto empeora el modelo si se desordena una columna: cuanto más empeora, más pesa. |
| **Semilla y preset** | La semilla (`SEMILLA = 42`) hace que el azar sea repetible. El preset (`medium_quality`) es el equilibrio entre rapidez y calidad. |

**Cómo se hace**

1. **Ir al apartado «5. Revisar los modelos candidatos (leaderboard)» del [cuaderno](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/2_Practica/laboratorio_automl/S3.5_lab_autogluon.ipynb)** que abristeis en la práctica y mirar su salida. Si Colab se ha reiniciado o la celda no tiene salida, ejecutad las celdas **de arriba abajo, de una en una** (`Mayús + Intro`), desde la instalación hasta él; la instalación tarda 2 o 3 minutos y, si Colab pide reiniciar, aceptad y seguid desde «0. Configuración». La celda saca estas cuatro columnas:

    - `model`: el nombre del modelo.
    - `score_test`: la nota con las reservas que no ha visto. **Es la que vale.**
    - `score_val`: la nota con parte de las reservas de entrenamiento. Sale más alta, y es lo esperado.
    - `fit_time`: segundos que tardó en entrenarse.

2. **Apuntar tres cosas de la tabla** y contestar a las preguntas que deja la celda (¿el mejor es un ensamblado?, ¿cuánto tarda cada uno?, ¿merece la pena?):

    - el mejor modelo y su `score_test`;
    - el segundo y la diferencia con el primero;
    - el `fit_time` de los dos.

    Una respuesta que vale: «Gana X con 0,7__; el segundo queda a 0,00__, una diferencia muy pequeña, y X tarda __ s frente a __ s; elegimos ______ porque ______». Una respuesta que no vale: «gana el primero porque tiene el número más alto».

3. **Escribir la métrica y por qué.** El cuaderno entrena con `eval_metric="roc_auc"`. Con casi la mitad de las reservas canceladas, el porcentaje de aciertos engaña: un modelo que dijera «nadie cancela» acertaría más de la mitad de las veces sin haber aprendido nada. Completad con vuestras palabras: «Miramos el AUC porque mide ______ y no depende de ______».

4. **Ejecutar el apartado «7. Explicabilidad: importancia de variables».** Saca una tabla con `importance` y `stddev` para cada columna. Apuntad las tres primeras y contestad: ¿tienen sentido para el negocio?, ¿alguna parece una fuga de datos? Recordad que «importante» significa que **ayuda a predecir**, no que **provoque** la cancelación.

5. **Anotar los ajustes.** Los necesita quien quiera repetir vuestro experimento. Para la versión, añadid una celda nueva (botón **+ Código**), escribid esta línea y ejecutadla:

    ```python
    !pip show autogluon.tabular
    ```

    Qué hace: pregunta a Python qué versión de AutoGluon tenéis; buscad la línea que empieza por `Version:`. El resto de los ajustes ya están en el cuaderno:

    | Ajuste | Dónde se ve |
    |---|---|
    | Versión de AutoGluon | La celda nueva (la línea que empieza por `Version:`) |
    | Preset | `presets="medium_quality"`, en el apartado «4. Entrenar con AutoML» |
    | Límite de tiempo | `LIMITE_TIEMPO`, en el apartado «0. Configuración» (120, o lo que hayáis puesto) |
    | Semilla | `SEMILLA = 42`, en ese mismo apartado |
    | Partición | 80 % más antiguo para entrenar y 20 % más reciente para probar, por `fecha_reserva`; las filas y las fechas las imprime el apartado «3. Partición TEMPORAL» |

**Qué deberíais ver.** Una tabla de unos diez modelos (en Colab pueden salir más, con redes neuronales), ordenada de mejor a peor `score_test`. El mejor ronda el 0,7 (la guía de AutoML da ~0,72) y su `score_val` es claramente mayor. Los primeros están casi empatados, con diferencias de milésimas. En la importancia de variables, unas pocas columnas se despegan del resto, que queda cerca de 0. Las cifras exactas cambian de un equipo a otro: lo que cuenta es que sean **las vuestras**.

**Hecho cuando:** tenéis anotados el mejor modelo y el segundo con su `score_test`, la métrica con su porqué, las variables que más pesan y los cinco ajustes.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'autogluon'` | Colab se reinició o no se ejecutó la instalación. | Ejecutad otra vez la celda de instalación (2–3 minutos) y después las demás, de arriba abajo. |
| `NameError: name 'prueba' is not defined` (o `'predictor'`, `'datos'`) | Os saltasteis alguna celda anterior, o la sesión se reinició. | Ejecutad desde «0. Configuración» hasta la celda que falla, **una a una**. |
| La celda del entrenamiento «no acaba» | AutoGluon tarda de medio minuto a dos minutos. | Esperad. Para un ensayo, poned `LIMITE_TIEMPO = 15` en «0. Configuración». No interrumpáis la celda. |
| Salen avisos (`Warning`, `Failed to import torch`) | No son errores: AutoGluon se salta ese modelo y sigue. | Seguid. |
| El `score_val` es más alto que el `score_test` | Es lo esperado: la nota «de ejercicios» es optimista. | Usad `score_test` en el informe y explicad por qué. |
| Vuestras cifras no coinciden con las de la guía | AutoGluon varía algo entre equipos y entre ejecuciones. | Es normal si el orden y la forma se parecen. Anotad **las vuestras**. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_03_paso_1.md) · [Ficha del reto](Reto_Sprint_03.md) · [Paso 3 →](Reto_Sprint_03_paso_3.md)
<!--/nav-->
