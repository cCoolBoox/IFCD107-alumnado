# Paso 3 · Escribir titular, viñetas y pie (día 1, 8 minutos)

<!--nav-->
> Sprint 13 · Reto «Informe visual para dirección» · paso 3 de 4 · [Ficha del reto](Reto_Sprint_13.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md) · [Paso 4 →](Reto_Sprint_13_paso_4.md)
<!--/nav-->

1. Copiar `plantilla_informe_visual.md` como `informe_visual.md`.
2. Escribir el titular-decisión y las tres viñetas, sin jerga.
3. Rellenar la sección de IA responsable y el pie.
4. Comprobar que las cifras del texto son las mismas que las del gráfico.

**En sencillo.** Ya tenéis los gráficos. Falta lo que Marcos lee primero: **una frase** que le diga qué hacer, **tres líneas** que le cuenten qué habéis hecho, qué recomendáis y qué límites hay, y **un pie** que diga de dónde salen los datos. Funciona como un parte médico: lo importante va arriba, en una frase, y el detalle queda debajo. Se escribe en un archivo de texto (`.md`) a partir de una plantilla con huecos entre corchetes: sustituís cada hueco por vuestro texto y respetáis los símbolos que ya vienen (`|`, `**`, `#`, `-`). No hace falta programar. Las cifras no se inventan: se copian del cuaderno y alguien las comprueba una por una.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Markdown (`.md`)** | Texto normal con marcas sencillas: `#` para un título, `**negrita**`, `-` para una viñeta y barras verticales para separar las columnas de una tabla. GitHub lo muestra ya con formato. |
| **Raw** | Botón de GitHub que abre un archivo como texto sin formato, para poder copiarlo entero. |
| **Preview** | Pestaña del editor de GitHub que enseña cómo se verá el texto antes de guardarlo. **Edit** vuelve a la escritura. |
| **Commit changes** | El botón verde que guarda el archivo en GitHub con un mensaje corto. Sin pulsarlo no se guarda nada. |
| **Titular-decisión** | Una frase que dice **qué hacer, a quién y con qué efecto**. No describe el modelo ni cuenta un resultado. |
| **Viñeta** | Una línea de una lista, la que empieza con `-`. Aquí son tres, de una o dos frases cada una. |
| **Jerga** | Palabras de la técnica que dirección no usa: AUC, F1, SHAP, umbral, nombres de columnas como `antelacion_dias`. |
| **Hueco entre corchetes** | Lo que la plantilla marca como `[…]` para que lo sustituyáis. Al final no puede quedar ninguno. |

**Cómo se hace**

1. **Crear `informe_visual.md` con el texto de la plantilla.** Escribe una persona (la C del reparto del paso 1); las demás dictan y vigilan las cifras. Los pasos, como en la [guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md):

    - Abrid la [plantilla del informe](../1_Trabajar/plantillas/plantilla_informe_visual.md), pulsad **Raw** (arriba a la derecha) y copiad todo con `Ctrl + A` y `Ctrl + C`.
    - En el repositorio del equipo **entrad primero en la carpeta `sprint-13`** y pulsad **Add file → Create new file**. En el cuadro del nombre escribid `informe_visual.md` (minúsculas, sin espacios) y pegad el texto con `Ctrl + V`.
    - Usad **Preview** para ver el resultado y **Edit** para seguir escribiendo. Cuando tengáis un primer texto, pulsad **Commit changes…**, escribid «Subo el borrador del informe visual» y confirmad. Para seguir editando después: abrid el archivo, icono del lápiz, cambiad y **Commit changes**.
    - **No borréis** la lista de comprobación, las reglas de oro ni «Revisión con la rúbrica» del final: se usan en el paso 4.

2. **Rellenar la cabecera.** Son las dos primeras líneas de la plantilla:

    | Hueco | Qué poner | Ejemplo |
    |---|---|---|
    | `[Nombre del modelo]` | El modelo que usa vuestro panel | `Regresión logística` |
    | **Equipo:** `______` | El nombre del equipo y de las personas | `Equipo 3 (Ana, Luis, Marta)` |
    | **Fecha:** `______` | La fecha de hoy | La del día en que escribís |
    | **Versión:** `1` | Dejadlo como está | `1` |

3. **Escribir el titular: una decisión, no un resultado.** Una línea con **qué hacer, a quién y con qué efecto**. Comparad:

    | Tipo | Ejemplo | ¿Vale? |
    |---|---|---|
    | Describe | «Modelo de regresión logística con AUC 0.74» | No: no dice qué hacer |
    | Cuenta un resultado | «El modelo detecta el 83% de las cancelaciones» | No: dice qué pasa, no qué decidir |
    | Es una decisión | «Avisar a las reservas de mayor riesgo evitaría unos 16 600 € de pérdidas por cada 1 500 reservas» | Sí: acción, a quién y efecto en euros |

    Reglas del titular:

    - Sustituid lo que va entre corchetes en `## TITULAR: […]` y **borrad la línea en cursiva del ejemplo** de la plantilla.
    - La cifra sale del gráfico del coste. Si la redondeáis, escribid «unos» (aquí 16.590 € se redondea a «unos 16 600 €») y dejad la cifra exacta en la frase de ese gráfico.
    - Una sola línea: **unos 100 caracteres como máximo**; si es más larga, se corta por la derecha en el PNG.
    - **Copiadlo también en el cuaderno.** En la celda «Parámetros del informe» sustituid el texto entre comillas de `TITULAR = "…"` y ejecutad otra vez la celda del panel: el titular es el título general de la imagen. Así texto e imagen dicen lo mismo.

4. **Rellenar «Los cuatro gráficos».** La plantilla tiene una tabla con cuatro casillas. Cada una lleva un título entre corchetes y, debajo, una frase en cursiva: sustituid las dos cosas. En la plantilla la curva ROC está arriba a la izquierda y la matriz arriba a la derecha; en el panel del cuaderno es al revés. Da igual: **colocad cada título en la casilla del gráfico del mismo nombre**, copiándolo tal cual sale en el PNG. Así se rellena con el modelo de ejemplo:

    | Casilla | Título (el mismo que en el PNG) | Frase de debajo |
    |---|---|---|
    | Curva ROC · ¿Podemos fiarnos del modelo? | Acierta mejor que el azar (AUC = 0.74), pero no es perfecto | El modelo detecta más cancelaciones que tirar una moneda con la misma proporción de falsas alarmas. El AUC es una nota de 0,5 (moneda) a 1 (perfecto) y aquí sale 0,74. |
    | Matriz · ¿Qué falla y cuánto? | Detectamos el 83% de las cancelaciones, avisando por error al 49% de quien no cancela | El error más caro es no detectar una cancelación (50 €) frente a avisar por error (30 €); por eso preferimos avisar de más. |
    | Importancia · ¿Qué mueve el resultado? | La antelación de la reserva pesa más del doble que cualquier otra variable | Lo que más pesa es cuántos días antes de la llegada se reserva; le siguen el depósito y el canal de venta. |
    | Coste · ¿Cuánto vale? | Con el modelo perdemos 16.590 € menos en 1500 reservas | Supuestos: cada cancelación no detectada cuesta 50 € (FN = 50 €) y cada falsa alarma 30 € (FP = 30 €). Sin modelo se pierden 34.400 € y con modelo 17.810 €. |

    Después, **sustituid la línea** `(Panel generado por el notebook: informe_visual_panel.png.)` **por esta**, que enseña la imagen en la página:

    ```text
    ![Panel del informe](informe_visual_panel.png )
    ```

    Qué hace esa línea:

    - Una imagen se pide en Markdown con un `!`, seguido del texto alternativo entre corchetes y del nombre del archivo entre paréntesis.
    - El nombre tiene que ser **exactamente** `informe_visual_panel.png`. La imagen se verá cuando esté subida a `sprint-13` (paso 4); en Preview, hasta entonces, saldrá rota.
    - El espacio antes del último paréntesis es opcional. Si ya lo tenéis escrito así, dejadlo.

5. **Sacar del cuaderno las cifras que faltan.** Para las viñetas vais a necesitar datos que el panel no escribe: cuántos avisos, dónde falla más el modelo, con cuántos datos se entrenó. En el cuaderno, **debajo de la celda del panel**, añadid una celda de código (botón **+ Código**), pegad esto y ejecutadla con ▶:

    ```python
    print(f"Entrenamiento: {len(X_ent)} · prueba: {len(X_test)} · reservas hechas entre {reservas['fecha_reserva'].min().date()} y {reservas['fecha_reserva'].max().date()}")
    print(f"Avisos: {int(pred.sum())} de {len(pred)} · falsas alarmas: {fp}")
    por_canal = pd.DataFrame({"canal": X_test["canal"].values, "cancelo": y_test.values, "avisado": pred})
    print(por_canal[por_canal["cancelo"] == 1].groupby("canal")["avisado"].mean().round(2))
    print(reservas.groupby(reservas["antelacion_dias"] > 90)["cancelada"].mean().round(2))
    ```

    Qué hace cada línea:

    - La primera cuenta las reservas de entrenamiento y de prueba y busca la primera y la última fecha de reserva (`.min()` y `.max()`).
    - La segunda cuenta los avisos (`pred.sum()` suma los 1, que son «avisamos») y recupera las falsas alarmas `fp` que ya calculó el cuaderno.
    - La tercera arma una tabla con tres columnas: el canal de cada reserva de prueba, si canceló de verdad y si el modelo avisó. `.values` evita problemas de numeración entre tablas.
    - La cuarta se queda con quienes **sí cancelaron** (`cancelo == 1`), los agrupa por canal y calcula qué proporción detectó el modelo (la media de `avisado`).
    - La quinta mira la tasa de cancelación de todas las reservas según tengan **más de 90 días** de antelación (`True`) o no (`False`).
    - **No cambiéis** los nombres `X_ent`, `X_test`, `y_test`, `pred`, `fp` ni `reservas`: vienen de las celdas anteriores, que tienen que estar ejecutadas.

    Con el modelo de ejemplo y el umbral 0.35 deberíais ver `Entrenamiento: 4500 · prueba: 1500 · reservas hechas entre 2024-01-01 y 2025-12-30` y `Avisos: 967 de 1500 · falsas alarmas: 397`. Por canal, el modelo detecta `agencia 0.81`, `directo 0.62`, `empresa 0.74` y `web_intermediaria 0.91`; y se cancelan `0.37` de las reservas con 90 días o menos de antelación y `0.60` de las de más de 90. Si cambiasteis de modelo o de umbral, saldrán otras cifras: las vuestras son las que valen.

6. **Escribir las tres viñetas.** Sustituid las tres líneas con corchetes. Frases cortas, cifras concretas y nada de jerga. Cada viñeta tiene su trabajo:

    - **Qué hemos hecho:** cuántos datos y qué se predice.
    - **Qué recomendamos:** la acción, para quién, con qué umbral, el ahorro esperado y cuándo empezar.
    - **Qué límites tiene:** de qué datos sale, dónde falla más, qué **no** debe usarse para decidir y cuándo se revisa.

    Así quedan con las cifras del modelo de ejemplo (el equipo y la fecha de inicio son vuestros: es un ejemplo):

    ```text
    - **Qué hemos hecho:** Un modelo que calcula la probabilidad de que cada reserva se cancele. Lo hemos entrenado con 4 500 reservas de TurisData hechas en 2024 y 2025 y lo hemos probado con otras 1 500 que no había visto.
    - **Qué recomendamos:** Que Ingresos avise a toda reserva con un 35 % o más de probabilidad de cancelar, empezando el lunes por las de esa semana. Con las 1 500 reservas de prueba habría supuesto 967 avisos y un ahorro de 16.590 € (de 34.400 € a 17.810 €), contando 50 € por cada cancelación no detectada y 30 € por cada falsa alarma.
    - **Qué límites tiene:** Los datos son sintéticos. De cada 10 avisos, unos 4 son falsas alarmas (397 de 967). Detecta peor las cancelaciones de las reservas directas (62 %) que las de intermediarios web (91 %). El ahorro supone que avisar siempre evita la cancelación. No debe usarse para negar reservas a nadie. Se revisará cada trimestre.
    ```

    Entre el titular, los gráficos y estas viñetas tienen que quedar contestadas las tres preguntas de Marcos: **¿puedo fiarme del modelo, qué mueve las cancelaciones y qué hago el lunes?**

7. **Rellenar «IA responsable» y el pie.** «IA responsable» son **dos líneas**: un riesgo concreto, una medida y qué se pidió a la IA y qué se revisó. Si no usasteis ninguna IA, escribidlo así: «No hemos usado IA». El pie es una línea con los datos, el modelo, el umbral, la semilla, el cuaderno y quién es responsable. Con el ejemplo:

    ```text
    Riesgo: usar la puntuación del modelo para negar o encarecer reservas, cuando además falla más con las reservas directas. Medida: solo se usa para decidir a quién avisar, nunca para negar una reserva, y se revisará por canal cada trimestre. Los datos son sintéticos. Hemos usado una IA para quitar jerga de las viñetas y hemos comprobado a mano que ninguna cifra cambiaba.
    ```

    ```text
    Datos: reservas sintéticas de TurisData (n = 6 000, reservas hechas en 2024 y 2025; prueba con 1 500) · Modelo: regresión logística · Umbral: 0.35 · Semilla: 42 · Notebook: `informe_visual.ipynb` (copia de S13_02) · Responsable: Marta
    ```

    En el pie, `Semilla: 42` es la del cuaderno (`SEMILLA = 42`). Si cambiasteis el modelo o el umbral, cambiad también esas dos casillas. «Responsable» es la persona que responde del informe.

8. **Traducir la jerga.** Buscad en la pestaña Preview (con `Ctrl + F`) cada palabra de esta tabla. Si aparece, sustituidla por la frase o dejad la sigla y poned la frase al lado:

    | Palabra | Cómo decirlo |
    |---|---|
    | AUC | «nota de 0,5 a 1 de lo bien que el modelo separa a quien cancela de quien no» |
    | F1 | «número que combina cuántos avisos acierta y cuántas cancelaciones detecta» |
    | SHAP | «forma de ver qué datos empujan más la decisión del modelo» |
    | Falso negativo / falso positivo | «cancelación que no detectamos» / «falsa alarma» |
    | Umbral | «a partir de qué probabilidad avisamos: con 0,35, avisamos si el modelo da un 35 % o más de probabilidad de cancelar» |
    | Nombre de una columna | `antelacion_dias` → «días entre la reserva y la llegada»; `web_intermediaria` → «intermediarios web» |

9. **Comprobar las cifras una por una.** Una persona lee el texto en voz alta y otra señala dónde sale cada cifra. Confirmad también que **no queda ningún corchete** `[` ni la línea del ejemplo en cursiva:

    | Cifra del texto | Dónde sale |
    |---|---|
    | 83% y 49% | Matriz de confusión del panel (casillas Cancela/Cancela y No cancela/Cancela) |
    | 0.74 | Leyenda de la curva ROC y salida `AUC en prueba: 0.744` |
    | 34.400 €, 17.810 € y 16.590 € | Barras del gráfico del coste y la línea `Coste sin modelo: 34.400 € · con modelo: 17.810 € · ahorro: 16.590 €` |
    | 50 € y 30 € | `COSTE_FN` y `COSTE_FP` de la celda de parámetros |
    | 0.35 y 35 % | `UMBRAL` |
    | 1 500, 4 500, 967, 62 %, 91 % | La celda nueva del punto 5 |

    Fijaos en que **49% y 4 de cada 10 (41 %) no se contradicen**: el 49% es la parte de quienes **no** cancelan a los que se avisó por error (397 de 812); el 41 % es la parte de los **avisos** que son falsas alarmas (397 de 967). Decid siempre qué se está contando. Si el tiempo aprieta, para el nivel mínimo bastan el titular y las tres viñetas; la IA responsable y el pie se rematan después.

**Qué deberíais ver.** Un `informe_visual.md` guardado en `sprint-13` que, en la pestaña Preview, se lee en un minuto: titular-decisión arriba, la tabla de los cuatro gráficos con sus títulos y frases, las tres viñetas, «IA responsable» y el pie, sin ningún corchete. El panel aparecerá cuando subáis el PNG en el paso 4. Todas las cifras del texto son las mismas que las del cuaderno y las del gráfico.

**Hecho cuando:** no queda ningún corchete de la plantilla, no hay jerga sin explicar y alguien ha comparado una por una las cifras del texto con las del gráfico.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'pred' is not defined` (o `'fp'`, `'X_ent'`) | Se saltó una celda anterior o Colab se reinició. | Ejecutad otra vez las celdas desde la primera, por orden, y después la nueva. |
| `KeyError: 'Canal'` | Escribisteis el nombre de la columna con mayúscula. | Las columnas van en minúsculas: `"canal"`. |
| En Preview, la tabla sale como líneas de texto con barras verticales | Falta una barra o la línea en blanco anterior a la tabla. | Comparad cada fila con la plantilla: mismo número de barras verticales en todas. |
| En Preview, el panel sale como una imagen rota o solo con su texto alternativo | El PNG aún no está en `sprint-13`, o el nombre no coincide. | Se arregla en el paso 4; comprobad que el nombre es `informe_visual_panel.png`, en minúsculas. |
| El titular aparece cortado por la derecha en el PNG | Pasa de unos 100 caracteres. | Acortadlo en el cuaderno y en `informe_visual.md`, y ejecutad otra vez la celda del panel. |
| El texto dice 4 de cada 10 y el gráfico 49% (o al revés) | Son dos porcentajes distintos: falsas alarmas entre los avisos, y entre quienes no cancelan. | Escribid junto a cada cifra qué cuenta, como en las viñetas del ejemplo. |
| Al guardar, GitHub avisa de un conflicto, o al volver no está el texto | Dos personas editaron a la vez, o no se pulsó **Commit changes**. | Recargad la página y repetid vuestro cambio sobre la versión actual. Escribe una sola persona. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_13_paso_2.md) · [Ficha del reto](Reto_Sprint_13.md) · [Paso 4 →](Reto_Sprint_13_paso_4.md)
<!--/nav-->
