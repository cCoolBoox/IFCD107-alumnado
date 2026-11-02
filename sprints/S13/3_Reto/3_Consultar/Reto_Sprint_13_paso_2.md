# Paso 2 · Ajustar los gráficos con título-conclusión (día 1, 8 minutos)

<!--nav-->
> Sprint 13 · Reto «Informe visual para dirección» · paso 2 de 4 · [Ficha del reto](Reto_Sprint_13.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md) · [Paso 3 →](Reto_Sprint_13_paso_3.md)
<!--/nav-->

1. Ejecutar las celdas de cálculos y del panel.
2. Cambiar el título de cada gráfico para que **diga una conclusión** con su cifra.
3. Comprobar que cada gráfico tiene ejes con nombre, barras desde 0 y pocos colores.
4. Volver a ejecutar para guardar el PNG con los cambios.

**En sencillo.** Marcos no va a leer un manual: mira los gráficos y sus títulos. Un título que **describe** («Matriz de confusión») no le dice nada; uno que **concluye** («Detectamos el 83 % de las cancelaciones») le dice qué pensar antes de mirar el dibujo. La plantilla ya calcula los números y escribe sola dos títulos con esas cifras; vosotros reescribís los otros dos y comprobáis que lo que dice cada título **se ve de verdad** en su gráfico. Cambiar un título es cambiar una frase entre comillas: no hace falta saber programar y no se toca nada más.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Título-conclusión** | Un título que dice lo que hay que concluir del gráfico, con una cifra: «Con el modelo perdemos 16.590 € menos». |
| **Matriz de confusión** | Una tabla que cruza lo que ocurrió con lo que dijo el modelo. Aquí, en porcentaje de cada fila real: «de cada 100 cancelaciones, a cuántas avisó». |
| **Curva ROC** | Muestra, para todos los umbrales, cuántas cancelaciones se detectan (vertical) frente a cuántas falsas alarmas se dan (horizontal). La diagonal es el azar. |
| **Importancia de variables** | Se desordena una variable al azar y se mide cuánto empeora el modelo (cuánto cae el AUC). Si empeora mucho, esa variable pesa. |
| **Cadena con `f`** (`f"…{x}…"`) | Un texto en el que lo que va entre llaves `{}` se sustituye por un valor calculado. `{auc:.2f}` es el `auc` con dos decimales; `{cm[1, 1]:.0%}`, un tanto por ciento. |
| **`ax[fila, columna]`** | Cada gráfico del panel. `ax[0, 1]` es el de la primera fila y la segunda columna (arriba a la derecha). |
| **PNG** | Una imagen. `plt.savefig("informe_visual_panel.png")` guarda el panel como imagen cada vez que se ejecuta la celda. |

**Cómo se hace**

1. **Ejecutar los cálculos y el panel.** Ejecutad con ▶ la celda «2. Cálculos que alimentan el panel» y la celda «3. El panel de una página» (las anteriores ya deberían estar ejecutadas, del paso 1). Deberíais ver `Coste sin modelo: 34.400 € · con modelo: 17.810 € · ahorro: 16.590 € (en 1500 reservas de prueba)` y el panel de 2 × 2.
2. **Leer qué dice cada gráfico antes de escribir su título.** Cada uno contesta a una pregunta de Marcos. Con el modelo de ejemplo y el umbral 0.35, esto es lo que se ve:

    | Gráfico | Contesta a | Línea de la celda del panel | Qué se ve |
    |---|---|---|---|
    | 1. Matriz de confusión (en %) | ¿Puedo fiarme? | `ax[0, 0].set_title(f"…")`: cambia sola con los números | Detecta el 83 % de las cancelaciones y avisa al 49 % de quienes no cancelan |
    | 2. Curva ROC | ¿Puedo fiarme? | `ax[0, 1].set_title("…")`: fijo, hay que cambiarlo | AUC = 0.74, por encima de la diagonal del azar |
    | 3. Importancia de variables | ¿Qué mueve las cancelaciones? | `ax[1, 0].set_title("…")`: fijo, hay que cambiarlo | `antelacion_dias` (0.10), `deposito` (0.05), `canal` (0.04), `tarifa` (0.03) |
    | 4. Coste con y sin modelo | ¿Qué hago el lunes? | `ax[1, 1].set_title(f"…")`: cambia sola con los números | 34.400 € sin modelo y 17.810 € con modelo: 16.590 € menos en 1500 reservas |

3. **Reescribir los títulos que son fijos.** En la celda del panel, buscad las dos líneas marcadas `# >>> EDITA` (gráficos 2 y 3) y sustituidlas por estas:

    ```python
    ax[0, 1].set_title(f"Acierta mejor que el azar (AUC = {auc:.2f}), pero no es perfecto")
    ax[1, 0].set_title("La antelación de la reserva pesa más del doble que cualquier otra variable")
    ```

    Qué hace cada línea:

    - `ax[0, 1]` es el gráfico de arriba a la derecha (la curva ROC) y `ax[1, 0]` el de abajo a la izquierda (importancia). **No cambiéis esos números**: eligen el gráfico.
    - `.set_title(…)` pone el título. Lo que va entre comillas es vuestra frase; si empieza por `f` puede llevar números entre llaves.
    - `{auc:.2f}` mete el AUC calculado (0.74) con dos decimales. Así, si cambiáis de modelo, el título sigue siendo cierto.
    - En el gráfico 3 la frase es fija: **mirad las barras antes de escribirla**. Con la regresión logística la primera (`antelacion_dias`, 0.10) es más del doble que la segunda (`deposito`, 0.05). Con otro modelo puede no serlo: nombrad la variable líder y ajustad la frase.
    - Dejad las comillas y los paréntesis como están: si falta uno, la celda da `SyntaxError`.

    Los dos títulos que cambian solos (gráficos 1 y 4) pueden quedarse. Si queréis que el 1 sea más claro, cambiad su segunda parte: `…\navisando por error al {cm[0, 1]:.0%} de quien no cancela`. El `\n` es un salto de línea. Fijaos en que «falsas alarmas» es un porcentaje de las reservas que **no** se cancelan, no de los avisos.

4. **Comprobar cada gráfico con la lista corta.** Pasad por los cuatro:

    - **El título concluye y se ve.** Lo que dice el título está en el gráfico: el 83 % y el 49 % salen en la matriz; el AUC, en la leyenda de la curva.
    - **Ejes con nombre y barras desde 0.** El gráfico 4 ya lleva `set_ylim(0, …)`; los cuatro tienen nombre en los ejes. Nada de 3D, y pocos colores con sentido (azul, gris y verde).
    - **Es del test, no del entrenamiento.** Todo sale de `X_test` e `y_test`: no lo cambiéis.
    - **El pie dice la verdad.** La última línea de la celda (`fig.text(…)`) pone «modelo: regresión logística» y el umbral. Si cambiasteis de modelo, cambiad ese texto.

5. **Volver a ejecutar para guardar el PNG.** Pulsad otra vez ▶ en la celda del panel: su última línea, `plt.savefig("informe_visual_panel.png", dpi=150)`, escribe la imagen **con vuestros títulos**. Se puede abrir con doble clic en el panel de archivos de Colab (icono de la carpeta 📁; si no aparece, pulsad el icono de refrescar).

**Qué deberíais ver.** Un panel de 2 × 2 con vuestros cuatro títulos y, en el panel de archivos, `informe_visual_panel.png`. Con el modelo de ejemplo: «Detectamos el 83% de las cancelaciones; avisamos por error al 49% de quien no cancela», «Acierta mejor que el azar (AUC = 0.74), pero no es perfecto», «La antelación de la reserva pesa más del doble que cualquier otra variable» y «Con el modelo perdemos 16.590 € menos en 1500 reservas».

**Hecho cuando:** cada gráfico tiene un título-conclusión y ejes con nombre, y el PNG se ha generado **después** del último cambio.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `SyntaxError: unterminated string literal (detected at line N)` | Al editar un título se borró una comilla. | Mirad la línea N: el texto debe empezar y acabar con `"`. |
| `SyntaxError: '(' was never closed` | Se borró un paréntesis al final de la línea. | Comprobad que `set_title(` acaba en `)`. |
| `NameError: name 'auc' is not defined` (o `'cm'`, `'ahorro'`) | Las cifras de los títulos salen de la celda «2. Cálculos» y no se ejecutó. | Ejecutad esa celda antes que la del panel. |
| `IndexError: index 2 is out of bounds for axis 0 with size 2` | Escribisteis `ax[2, 0]`: el panel solo tiene filas 0 y 1. | Usad `ax[0, 0]`, `ax[0, 1]`, `ax[1, 0]` o `ax[1, 1]`. |
| El título aparece cortado por los lados | Es demasiado largo. | Acortadlo o partidlo en dos líneas con `\n` dentro de las comillas. |
| El panel o el PNG enseñan el título antiguo | Se editó, pero no se volvió a ejecutar la celda del panel. | Pulsad ▶ en la celda del panel y refrescad el panel de archivos. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_13_paso_1.md) · [Ficha del reto](Reto_Sprint_13.md) · [Paso 3 →](Reto_Sprint_13_paso_3.md)
<!--/nav-->
