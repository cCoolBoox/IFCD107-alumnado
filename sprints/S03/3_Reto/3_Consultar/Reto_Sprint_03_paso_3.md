# Paso 3 · Elegir el umbral con vuestros costes (día 2, 25 minutos)

<!--nav-->
> Sprint 3 · Reto «Primer modelo en producción» · paso 3 de 6 · [Ficha del reto](Reto_Sprint_03.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md) · [Paso 4 →](Reto_Sprint_03_paso_4.md)
<!--/nav-->

1. Evaluar el modelo con dos umbrales (0,5 y 0,3) y leer la matriz de confusión.
2. Poner **vuestros importes** en euros a las dos formas de equivocarse.
3. Elegir el umbral más barato y compararlo con «avisar a todos» y «no avisar nunca».

**En sencillo.** El modelo no contesta «sí» o «no»: contesta un riesgo, por ejemplo 0,79. El **umbral** es el punto de corte a partir del cual el equipo de reservas recibe una alerta. Es como un detector de humo: si es muy sensible, suena por una tostada (muchas falsas alarmas); si no lo es, se quema la cocina sin avisar. Dónde poner el punto de corte **no es una cuestión de matemáticas, sino de dinero**: depende de cuánto cuesta cada tipo de error. Eso lo ponéis vosotros. El cuaderno hace los cálculos; vosotros cambiáis dos números, leéis una tabla y elegís.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Probabilidad** | El riesgo que da el modelo para una reserva, de 0 a 1 (0,79 = 79 % de riesgo). |
| **Umbral** | El punto de corte: si el riesgo lo supera, damos la alerta. |
| **Alerta falsa** | Avisamos, pero la reserva no se iba a cancelar. Cuesta una llamada, un descuento o molestar a un cliente. |
| **Cancelación no prevista** | No avisamos y la reserva se cancela. Cuesta una habitación vacía. |
| **Precisión** | De las alertas que damos, cuántas acertaban. |
| **Recall** (exhaustividad) | De las cancelaciones que hay, cuántas detectamos. |
| **Matriz de confusión** | Una tabla de 2 × 2 que cuenta los aciertos y los dos tipos de error. |

**Cómo se hace**

1. **Evaluar con dos umbrales.** Ejecutad el apartado «6. Evaluar en el periodo de prueba» del cuaderno. Imprime la precisión, el recall y el F1 con umbral 0,5 y con umbral 0,3, el `ROC-AUC` y la matriz de confusión del umbral 0,5. La matriz se lee así: las filas son lo que **pasó de verdad** y las columnas lo que **dijo el modelo**.

    | | El modelo dijo «no cancela» | El modelo dijo «cancela» |
    |---|---|---|
    | **Realmente no canceló** | acierto | **alerta falsa** |
    | **Realmente canceló** | **cancelación no prevista** | acierto |

    Anotad la precisión y el recall de los dos umbrales y contestad: ¿qué se gana y qué se pierde al bajar el umbral de 0,5 a 0,3?

2. **Pensar vuestros importes, antes de tocar el cuaderno.** Sois una consultora: ponéis una cifra a cada error y explicáis de dónde sale. Rellenad esta tabla en la hoja del equipo:

    ```text
    | Error                    | Qué pasa                              | Cuánto cuesta (€) | Por qué esa cifra |
    |--------------------------|---------------------------------------|-------------------|-------------------|
    | Cancelación no prevista  | La habitación se queda vacía          |                   |                   |
    | Alerta falsa             | Actuamos sin que hiciera falta        |                   |                   |
    ```

    Para tener una referencia de cuánto vale una reserva, podéis calcular en DB Browser el ingreso medio de una reserva:

    ```sql
    SELECT ROUND(AVG(noches * precio_noche), 1) AS ingreso_medio
    FROM reservas;
    ```

    Qué hace: multiplica las noches por el precio de cada noche y saca la media de todas las reservas. A partir de ahí razonad: ¿qué parte de ese ingreso se pierde si no avisamos?, ¿cuánto cuesta una llamada o un descuento? Los 100 € y 40 € del cuaderno son **solo un ejemplo**. Qué no vale: dejar los del cuaderno sin pensarlos, poner una cifra sin frase que la explique, o presentarla como un dato del cliente. Son **vuestras hipótesis**: en el informe se dice que TurisData debería validarlas.

3. **Cambiar los dos importes en el cuaderno.** Id al apartado «6b. Elegir el umbral con costes» (la celda de debajo del 6) y cambiad **solo los números** de estas dos líneas:

    ```python
    COSTE_NO_PREVISTA = 100    # euros que cuesta una cancelación que no avisamos (noche vacía)
    COSTE_ALERTA_FALSA = 40    # euros que cuesta una alerta que no hacía falta (p. ej. un descuento regalado)
    ```

    Qué hace cada línea:

    - `COSTE_NO_PREVISTA = 100`: los euros que cuesta cada cancelación que no avisamos. Poned el vuestro.
    - `COSTE_ALERTA_FALSA = 40`: los euros que cuesta cada alerta que no hacía falta. Poned el vuestro.
    - Los nombres **no se pueden cambiar**: el resto de la celda los usa.
    - El texto detrás de `#` es un comentario: Python lo ignora.

    Ejecutad la celda (`Mayús + Intro`).

4. **Leer la tabla de costes.** La celda saca una fila por umbral (de 0,1 a 0,7) con las alertas, las cancelaciones no previstas, las alertas falsas y el coste en euros. Debajo escribe el umbral con menos coste de los probados, el **umbral teórico** y la comparación con las dos referencias:

    - **«No avisar nunca»**: pagáis todas las cancelaciones.
    - **«Avisar a todos»**: pagáis todas las alertas falsas.

    El umbral teórico sale de una regla: conviene dar la alerta cuando **riesgo > coste de la alerta falsa ÷ (coste de la alerta falsa + coste de la no prevista)**. Con 40 € y 100 €: 40 ÷ 140 = 0,29. Si queréis probar otro umbral (por ejemplo el teórico redondeado), añadidlo a la lista de umbrales que va dentro del paréntesis de la línea `for u in` (la primera lista es 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7) y volved a ejecutar.

5. **Elegir y escribir la frase para un directivo.** Elegid el umbral con menos coste o uno muy parecido; si dos cuestan casi lo mismo, quedaos con el que da menos alertas, porque el equipo tiene que poder atenderlas. Comparad su coste con «avisar a todos» y con «no avisar nunca»: si el modelo no los mejora, no compensa, y hay que decirlo con honestidad. Para la frase necesitáis dos cuentas con la fila de vuestro umbral:

    - Cancelaciones detectadas: **aciertos = alertas − alertas falsas**; el total de canceladas es **aciertos + no previstas**; el recall es aciertos ÷ canceladas.
    - Alertas falsas: **alertas falsas ÷ alertas**.

    Ejemplo con la fila 0,3 de la tabla de la [guía en parejas](../../2_Practica/automl/guia_automl_en_parejas.md) (importes de ejemplo 100 € y 40 €: 897 alertas, 388 falsas, 68 no previstas): aciertos 897 − 388 = 509; canceladas 509 + 68 = 577; recall 509 ÷ 577 ≈ 0,88; falsas 388 ÷ 897 ≈ 0,43. La frase queda así (con vuestras cifras, no con estas): «Recomendamos alertar cuando el riesgo supere el 30 %: así detectamos casi 9 de cada 10 cancelaciones, aunque 4 de cada 10 alertas serán falsas. Con una no prevista valorada en ___ € y una falsa en ___ €, el coste baja a ___ €, frente a ___ € si avisamos a todos y ___ € si no avisamos nunca».

**Qué deberíais ver.** Un bloque con la precisión, el recall y el F1 de los dos umbrales, el `ROC-AUC` (la guía da ~0,72) y la matriz de confusión con cuatro números. Después, una tabla de siete filas (si no habéis añadido umbrales) cuyo coste **baja al principio y vuelve a subir**: con los importes de ejemplo el mínimo cae en los umbrales bajos (0,2–0,3), no en 0,5; con los vuestros puede cambiar. Debajo, tres líneas: el umbral con menos coste, el umbral teórico (0,29 con 100 € y 40 €) y la comparación con «no avisar nunca» y «avisar a todos».

**Hecho cuando:** tenéis los dos importes con su razón, la tabla ejecutada con ellos, el umbral elegido, su coste comparado con las dos referencias y la frase para el directivo escrita.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'prob' is not defined` (o `'y_real'`) | Ejecutasteis el apartado 6b sin ejecutar antes el 6. | Ejecutad el apartado 6 y después el 6b. |
| `NameError: name 'COSTE_NO_PREVISTA' is not defined` | Borrasteis una línea de importes o no ejecutasteis la celda. | Volved a poner las dos líneas con sus nombres exactos y ejecutadla. |
| El umbral con menos coste sale 0,1 o 0,7 | Vuestros importes son muy desiguales. | Es lógico: si una no prevista cuesta mucho más que una falsa, conviene avisar casi siempre. Explicadlo en el informe. |
| El modelo no gana a «avisar a todos» | Pasa cuando la alerta falsa cuesta muy poco. | Es un resultado válido. Decidlo tal cual: el modelo solo compensa si actuar cuesta o hay poca gente para hacerlo. |
| Vuestro umbral teórico no aparece en la tabla | La tabla solo prueba de 0,1 a 0,7 de 0,1 en 0,1. | Añadid el umbral a la lista que va en la línea `for u in` y ejecutad otra vez. |
| Habéis dejado 100 € y 40 € | Son los de ejemplo. | Cambiadlos por los vuestros y escribid la frase que los justifica. |
| El recall o la precisión de la guía no coinciden con los vuestros | AutoGluon varía algo entre equipos. | Es normal. En el informe van **vuestras** cifras. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_03_paso_2.md) · [Ficha del reto](Reto_Sprint_03.md) · [Paso 4 →](Reto_Sprint_03_paso_4.md)
<!--/nav-->
