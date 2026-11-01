# Paso 1 · Elegir el modelo, cargarlo y fijar los costes (día 1, 4 minutos)

<!--nav-->
> Sprint 13 · Reto «Informe visual para dirección» · paso 1 de 4 · [Ficha del reto](Reto_Sprint_13.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md) · [Paso 2 →](Reto_Sprint_13_paso_2.md)
<!--/nav-->

1. Elegir el mejor modelo del curso y abrir el cuaderno plantilla en Colab.
2. Comprobar que el modelo se carga y que el cuaderno llega hasta el final sin errores.
3. Escribir el coste de cada error y el umbral.
4. Repartir el trabajo del paso 2.

**En sencillo.** Marcos, el director de TurisData, tiene 10 minutos y no sabe qué es un AUC: quiere **una página** que le diga si puede fiarse del modelo, qué mueve las cancelaciones y qué hacer el lunes. El cuaderno plantilla ya funciona: al ejecutarlo dibuja un panel de cuatro gráficos con un modelo de ejemplo. Es como el cuadro de mandos de un coche, que ya viene montado; vosotros le ponéis el motor (el modelo) y los precios (cuánto cuesta cada error). En este paso casi no se escribe: se abre, se ejecuta, se cambian unos números y se comprueba que no hay errores. No hace falta saber programar.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Celda** | Cada caja del cuaderno. Las de código se ejecutan con el botón ▶ (o con `Mayús + Intro`), por orden. |
| **Modelo** | Lo que, dada una reserva, calcula la **probabilidad** (de 0 a 1) de que se cancele. Se pide con `predict_proba`. |
| **AUC** | Una nota de 0,5 (como tirar una moneda) a 1 (perfecto) de lo bien que el modelo separa a quien cancela de quien no. |
| **Datos de prueba** | El 25 % de las reservas, que el modelo no ha visto al aprender. Todas las cifras del informe salen de ahí. |
| **Semilla** (`SEMILLA = 42`) | Un número que fija el azar para que a otra persona le salgan exactamente las mismas cifras. |
| **FN y FP** | Falso negativo (**FN**): una cancelación que el modelo no detecta, es decir, una habitación vacía. Falso positivo (**FP**): una falsa alarma, avisar a quien sí iba a venir. |
| **Umbral** | La probabilidad a partir de la cual avisáis. Con `UMBRAL = 0.35`, avisáis si el modelo da un 35 % o más de probabilidad de cancelación. |
| **`# >>> EDITA`** | La marca que lleva la plantilla en las líneas que os toca cambiar. Lo demás, no se toca. |

**Cómo se hace**

1. **Abrir la plantilla y guardar vuestra copia.** Entrad en el [cuaderno `S13_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) y pulsad *Archivo → Guardar una copia en Drive*: así el original no se toca. Cambiad el nombre (pulsad el título, arriba a la izquierda) a `informe_visual`. Compartid la copia con el equipo como **Editor**. Una persona escribe y las demás miran.
2. **Ejecutar la plantilla entera, sin cambiar nada.** Pulsad ▶ en cada celda, de arriba abajo. Las dos primeras no escriben nada (preparación e importaciones). Deberíais ver `AUC en prueba: 0.744 · reservas de prueba: 1500`, después `Coste sin modelo: 34,400 € · con modelo: 17,810 € · ahorro: 16,590 € (en 1500 reservas de prueba)` y, al final, el panel de cuatro gráficos. En el panel de archivos de Colab (icono de la carpeta 📁; si no aparece, pulsad el icono de refrescar) está ya `informe_visual_panel.png`.
3. **Elegir el modelo.** El de la plantilla es una regresión logística y funciona: en el cuaderno [`S13_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_01_visualizacion_resultados.ipynb) sale con AUC 0.744 frente a 0.733 del bosque aleatorio. Si tenéis otro mejor, o queréis cambiar, buscad en la celda «1. Datos y modelo» la línea marcada `# >>> EDITA` y cambiadla. Por ejemplo, para el bosque aleatorio, añadid la primera línea arriba de la celda y sustituid la línea marcada `# >>> EDITA` por la segunda:

    ```python
    from sklearn.ensemble import RandomForestClassifier

    modelo = Pipeline([("prep", prep), ("m", RandomForestClassifier(300, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2))]).fit(X_ent, y_ent)   # >>> EDITA
    ```

    Qué hace cada línea:

    - `from sklearn.ensemble import RandomForestClassifier`: trae el bosque aleatorio. Si falta, da `NameError`.
    - `Pipeline([("prep", prep), ("m", …)])`: una cadena de dos pasos: primero el preprocesado (`prep`: escala los números y convierte las categorías en columnas) y después el modelo. **Mantened `prep`**: es «el mismo preprocesado con el que se entrenó».
    - `.fit(X_ent, y_ent)`: el modelo aprende con el entrenamiento (el 75 %). **No cambiéis `X_ent`, `y_ent` ni `SEMILLA`**: así la prueba sigue siendo la misma.
    - La celda sigue con `prob = modelo.predict_proba(X_test)[:, 1]`: la probabilidad de cancelar de cada reserva de prueba. Vuestro modelo tiene que saber darla.

    Con el bosque debería salir `AUC en prueba: 0.733`. Si vuestro modelo no carga a tiempo, dejad el de ejemplo y decidlo en el pie del informe. **Si cambiáis de modelo, cambiad también el texto `modelo: regresión logística`** de la última línea de la celda del panel.

4. **Escribir los costes.** En la celda «Parámetros del informe» están estas líneas (todas con `# >>> EDITA`). Cambiad lo que os toque:

    ```python
    TITULAR = "Recomendamos pedir depósito y avisar a las reservas de riesgo alto"
    CLIENTE = "TurisData Canarias · Dirección de Ingresos"
    AUTORES = "Equipo X (nombres)"
    COSTE_FN = 50   # € que perdemos por cada cancelación que el modelo no detecta
    COSTE_FP = 30   # € que cuesta tratar como "en riesgo" a quien sí viene
    UMBRAL = 0.35   # a partir de qué probabilidad avisamos
    ```

    Qué hace cada línea:

    - `AUTORES`: poned vuestros nombres entre comillas. Salen en el pie del panel. El `TITULAR` lo pulís en el paso 3.
    - `COSTE_FN`: lo que perdéis por cada cancelación que no detecta el modelo (una habitación que se queda vacía). `COSTE_FP`: lo que cuesta avisar a quien sí iba a venir. Los 50 y 30 son de ejemplo: **preguntadle al docente, que hace de cliente**. Si no lo sabe, proponed una hipótesis y escribidla en el informe.
    - `UMBRAL`: se decide en el punto siguiente. Los números van **sin comillas**; los textos, entre comillas.

5. **Elegir el umbral con los costes, no por costumbre.** En una celda nueva, justo debajo de la celda «1. Datos y modelo», escribid:

    ```python
    umbrales = np.round(np.arange(0.05, 0.96, 0.01), 2)
    costes = []
    for u in umbrales:
        pred_u = (prob >= u).astype(int)
        fn_u = int(((pred_u == 0) & (y_test == 1)).sum())
        fp_u = int(((pred_u == 1) & (y_test == 0)).sum())
        costes.append(COSTE_FN * fn_u + COSTE_FP * fp_u)
    umbral_optimo = umbrales[int(np.argmin(costes))]
    print(f"Umbral óptimo con vuestros costes: {umbral_optimo:.2f} · coste mínimo: {min(costes):,.0f} €")
    ```

    Qué hace cada línea:

    - `np.arange(0.05, 0.96, 0.01)` genera los umbrales de 0,05 a 0,95 de uno en uno (centésimas).
    - El `for` prueba cada umbral `u`: `pred_u` es 1 («avisamos») si la probabilidad llega a `u`. `fn_u` cuenta las cancelaciones que no avisamos y `fp_u`, las falsas alarmas; `&` significa «y a la vez».
    - `costes.append(…)` apunta el coste total de ese umbral: `COSTE_FN × fn_u + COSTE_FP × fp_u`.
    - `np.argmin(costes)` da la posición del coste más bajo; `umbrales[…]` dice a qué umbral corresponde.

    Con 50 y 30 y la regresión logística debería salir `Umbral óptimo con vuestros costes: 0.35 · coste mínimo: 17,810 €` (con el bosque, 0.38 y 18,930 €). Escribid ese número en `UMBRAL` y **volved a ejecutar desde la celda de parámetros hacia abajo**. El cálculo es el Ejercicio 4 de `S13_01`.

6. **Repartir el paso 2 y los siguientes.** Una persona no necesita saber de todo, pero todas deben entender el panel:

    | Persona | Parte | Minutos |
    |---|---|---|
    | A | Modelo, costes y cuaderno (paso 1) | 4 |
    | B | Los gráficos y sus títulos (paso 2) | 8 |
    | C | Titular, viñetas y pie (paso 3) | 8 |
    | D (si hay 4) | Prueba de los 30 segundos y revisión (paso 4) | 5 |

**Qué deberíais ver.** Al final de la celda de datos y modelo, la línea `AUC en prueba: … · reservas de prueba: 1500` (0.744 con el modelo de ejemplo), la del umbral óptimo, y ningún mensaje de error en rojo hasta el panel.

**Hecho cuando:** el modelo se carga, `COSTE_FN`, `COSTE_FP` y `UMBRAL` están escritos, y cada persona sabe qué parte le toca.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'RandomForestClassifier' is not defined` | Cambiasteis de modelo y falta la línea `from … import …`. | Añadid el import arriba de la celda del modelo. |
| `AttributeError: This 'Pipeline' has no attribute 'predict_proba'` | El modelo elegido no sabe dar probabilidades. | Elegid otro que dé probabilidades o dejad la regresión logística de ejemplo. |
| `ValueError: columns are missing: {'canal'}` (o `The feature names should match those that were passed during fit`) | El modelo se entrenó en otro cuaderno con otras columnas o sin el mismo preprocesado. | Entrenadlo aquí, con `X_ent`, `y_ent` y el mismo `prep`, o dejad el de ejemplo. |
| `NameError: name 'prob' is not defined` (o `'UMBRAL'`, `'cm'`) | Se saltó una celda anterior o Colab se reinició. | Ejecutad otra vez las celdas desde la primera, por orden. |
| `AUC en prueba` no es 0.744 | Habéis cambiado de modelo, que es lo normal. | Apuntad el nuevo AUC: es el que va en el informe. |
| Cambiasteis `UMBRAL` y el panel sigue igual | El panel se calculó con el valor anterior. | Volved a ejecutar desde la celda de parámetros hacia abajo. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_13.md) · [Paso 2 →](Reto_Sprint_13_paso_2.md)
<!--/nav-->
