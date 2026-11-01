# Paso 5 · Informe y README (día 2, 10 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md)
<!--/nav-->

1. Copiar la plantilla como `informe_modelado.md` y rellenarla con las cifras del cuaderno.
2. Escribir el README: semilla, versiones, cómo ejecutar y uso de la IA.
3. Preparar la entrega: revisión con la rúbrica, subida y autoevaluación (los 15 minutos siguientes).

**En sencillo.** El trabajo técnico ya está hecho; falta **contárselo al gerente del hotel**, que no sabe qué es un AUC y quiere saber qué hacer, cuánto cuesta equivocarse y cuánto ahorra el modelo. El informe traduce vuestras cifras a euros y a una recomendación. El README es el manual para que otra persona abra el cuaderno y obtenga lo mismo. Casi todo es copiar números que ya salieron en los pasos 2 a 4 a una plantilla de texto; solo hay una celda de código nueva y es opcional. Una persona que no escribió esa parte lo revisa con la rúbrica antes de subirlo.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Informe** | El documento (`informe_modelado.md`) que cuenta el trabajo a quien no programa. |
| **README** | La «portada» de la carpeta: cómo ejecutar, versiones y quién hizo qué. |
| **Markdown (`.md`)** | Texto con símbolos sencillos: `##` hace un título y `\|` separa las columnas de una tabla. |
| **Versión** | El número de edición de Python o de una librería. Con otra versión, algunas cifras pueden cambiar un poco. |
| **Reiniciar y ejecutar todo** | Borra la memoria del cuaderno y lo ejecuta de arriba abajo: prueba de que no depende de nada escondido. |
| **Rúbrica** | La tabla con la que se evalúa: cuatro criterios, cada uno de 1 a 4. |
| ***Commit*** | Guardar cambios en GitHub con un mensaje corto y vuestro nombre. Sin pulsar **Commit changes**, no se guarda nada. |

**Cómo se hace**

1. **Crear y rellenar el informe.** Abrid [`informe_modelado_plantilla.md`](../1_Trabajar/plantillas/informe_modelado_plantilla.md), pulsad *Raw*, copiad el texto y, en la carpeta `sprint-07` del repositorio, usad *Add file → Create new file* con el nombre `informe_modelado.md` y pegadlo. Cada hueco sale de una celda del cuaderno:

    | Apartado de la plantilla | Qué escribís | De dónde sale |
    |---|---|---|
    | 1 · Resumen para el gerente | Seis líneas con euros: qué recomendáis, qué cuesta cada error y cuánto ahorráis frente a no hacer nada | Pasos 3 y 4 |
    | 3 · Regresión | La tabla de MAE, RMSE y R² y la frase del error medio en euros | Paso 2 (`resultados_precio`) |
    | 4 · Clasificación | La tabla de métricas y la matriz de confusión con el umbral elegido | Paso 3 |
    | 5 · De las métricas a los euros | `COSTE_FN` y `COSTE_FP` con su razón, el umbral y los tres costes en test | Pasos 1 y 3 |

    Esos cuatro son el **nivel mínimo**, en pocas líneas. Para el **estándar**, completad también el 2 (variables usadas y excluidas, del paso 2), la sensibilidad del 5 (la tabla del paso 4), el 6 (recomendación con cifras y límites) y el 7 (riesgos de IA responsable). Un molde para el resumen, con vuestras cifras: «Recomendamos avisar de las reservas con una probabilidad de cancelar igual o mayor que [0,25]. Con un coste de [284] € por cancelación no prevista y [103] € por falsa alarma, el modelo cuesta [58.331] € en test frente a [156.484] € sin modelo: un ahorro de [98.153] € ([63] %)». Un molde para la tabla del apartado 4:

    ```text
    | Modelo | AUC | AP | Recall (umbral) | Precisión (umbral) |
    |---|---|---|---|---|
    | Baseline | 0.500 | 0.459 | 0 % | — |
    | Logística (umbral 0,25) | 0.746 | 0.729 | 92 % | 53 % |
    ```

    Pulsad *Preview* para ver cómo queda la tabla antes de guardar.

2. **IA responsable, con datos (apartado 7).** La pregunta del enunciado: ¿quién sufre los falsos positivos y se penaliza a algún canal? Para contestar con números, celda nueva (necesita `proba_test` y `mejor_umbral` del paso 3):

    ```python
    resultado = X_test.copy()
    resultado["real"] = y_test
    resultado["aviso"] = (proba_test >= mejor_umbral).astype(int)
    no_canceladas = resultado[resultado["real"] == 0]
    print(no_canceladas.groupby("canal")["aviso"].mean().round(2))
    ```

    Qué hace cada línea:

    - `X_test.copy()`: una copia de las reservas de test; así no se toca la original. Las dos líneas siguientes le añaden dos columnas: lo que pasó (`real`) y si el modelo avisó (`aviso`: 1 si la probabilidad llega al umbral).
    - `resultado[resultado["real"] == 0]`: se queda con las reservas que **no** se cancelaron. `==` significa «es igual a».
    - `.groupby("canal")["aviso"].mean()`: por cada canal, la proporción de esas reservas que recibió un aviso. Cada una es una falsa alarma. Cambiad `"canal"` por `"pais_origen"` o `"deposito"` para mirar otras.

    Con los costes de ejemplo, salen aproximadamente: `agencia 0.65`, `directo 0.49`, `empresa 0.74` y `web_intermediaria 0.85`. Es decir, un cliente que reserva por una web intermediaria y no cancela tiene mucha más probabilidad de recibir una falsa alarma que uno que reserva directo. Contadlo en el informe y proponed una medida.

3. **Escribir el README.** En `sprint-07/`, abrid `README.md` y pulsad el icono del lápiz. Cuatro cosas: `SEMILLA = 42`; las versiones; cómo ejecutar (*abrir en Colab y ejecutar de arriba abajo*); y el uso de la IA (qué pedisteis y qué revisasteis). Añadid quién hizo qué. Las versiones salen de una celda del cuaderno:

    ```python
    !python --version
    import sklearn
    print(sklearn.__version__)
    ```

    Qué hace cada línea:

    - `!python --version`: el `!` pide a Colab que ejecute esa orden del sistema y escriba la versión de Python. Solo funciona en Colab o Jupyter.
    - `import sklearn` y `print(sklearn.__version__)`: escriben la versión de scikit-learn. Copiad las dos al README; en cada ordenador salen otras y es normal.

4. **Reiniciar y ejecutar todo.** En Colab, *Entorno de ejecución → Reiniciar y ejecutar todo*, y esperad al final: ninguna celda debe mostrar un error en rojo. Si falla, corregid la primera celda en rojo y repetid.

5. **Revisión con la rúbrica (5 minutos, al empezar la entrega).** La hace una persona que **no escribió** esa parte. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y rellena la sección «Revisión con la rúbrica» del final de `informe_modelado.md`: un nivel de 1 a 4 por criterio y **una frase de prueba** (lo que ha comprobado), más «Lo primero que mejoraríamos».

**Qué deberíais ver.** `informe_modelado.md` con los apartados del nivel elegido rellenos y cifras en euros, un `README.md` con semilla, versiones y cómo ejecutar, y el cuaderno entero ejecutado sin errores. La celda del punto 2 escribe cuatro líneas de canal y la del punto 3 escribe una versión de Python y otra de scikit-learn.

**Hecho cuando:** otra persona podría ejecutar el cuaderno siguiendo solo el README, la sección «Revisión con la rúbrica» del informe está rellena y todo está subido a `sprint-07/`.

**Después, 15 minutos de entrega:**

- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y después *Archivo → Descargar → Descargar .ipynb*; (2) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-07`**; (3) *Add file → Upload files* y arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube `reto_S07.ipynb` («Añado cuaderno del reto»), la B sube `informe_modelado.md` («Añado informe»), la C edita `README.md` («Completo README»). Los nombres, **en minúsculas y sin espacios**. El CSV va a `data/` del repositorio solo si aún no está.
- **La autoevaluación.** Cada persona copia [la plantilla](../2_Entregar/autoevaluacion_y_coevaluacion.md), la rellena y la sube a `sprint-07/` como `autoevaluacion_nombre.md`. La parte de coevaluación se completa en la *review* del jueves 12/11, en el mismo fichero.
- **La review (5 minutos por equipo).** Enseñaréis la tabla comparativa de métricas, el umbral elegido y su coste en euros frente a «no hacer nada», y una frase de recomendación para el gerente.
- **La retro.** Pensad: ¿qué hipótesis de coste discutimos más? ¿Cómo cambia la decisión si cambia el coste? ¿Qué habríamos necesitado saber del hotel para afinar?

**Qué deberíais ver.** En la carpeta `sprint-07` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), *commits* de personas distintas.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'proba_test' is not defined` | La celda del paso 3 no se ha ejecutado antes de esta. | Ejecutad el cuaderno desde arriba con *Reiniciar y ejecutar todo*. |
| `SyntaxError: invalid syntax` al ejecutar la celda de las versiones | La línea `!python --version` se ejecutó fuera de Colab. | Quitad esa línea y escribid la versión de Python a mano desde `import sys; print(sys.version)`. |
| `KeyError: 'canal '` | El nombre de la columna lleva un espacio o una errata. | Copiadlo de `X_test.columns`. |
| La tabla del informe se ve rota en *Preview* | Falta una `\|` en una fila o hay un salto de línea dentro de una celda. | Cada fila, en una sola línea y con las mismas `\|` que la cabecera. |
| El archivo aparece fuera de `sprint-07/` | Se subió desde la raíz del repositorio. | Entrad primero en `sprint-07` y repetid la subida. |
| No sabéis qué nivel poner en la rúbrica | Los niveles están en [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). | Elegid el nivel cuyo texto se cumple **entero** y escribid la prueba. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_07_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_07.md)
<!--/nav-->
