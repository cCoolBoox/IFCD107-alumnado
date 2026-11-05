# Paso 3 · Mitigar el sesgo y volver a medir (día 2, 80 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 3 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 4 →](Reto_Sprint_16_paso_4.md)
<!--/nav-->

1. Elegir una medida de mitigación para el sesgo que detectasteis.
2. Aplicarla y volver a medir, por subgrupo, antes y después.
3. Anotar los resultados en el cuaderno y en el registro de experimentos.

**En sencillo.** Imaginad una báscula que pesa bien casi todo, pero se queda corta con los objetos pequeños. No basta con darse cuenta: hay que ajustarla y **volver a pesar** para comprobar dos cosas: que ahora pesa bien lo pequeño y que no ha empezado a fallar con lo demás. Con el modelo es igual. Una **mitigación** es una medida que toca algo (la decisión, los datos, el entrenamiento) para que al grupo que va peor le vaya mejor. Después se vuelve a medir, grupo a grupo, y se apunta lo que mejoró, lo que empeoró y lo que costó. **No existe una mitigación gratis**, y a veces la que probáis no funciona: eso también es un resultado válido y se anota. Una regla de oro: el número que ajustáis (un umbral, un peso) lo elegís con los datos de **entrenamiento**, nunca mirando el test; el test solo se usa para medir el «después» con la medida ya fijada.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Mitigación** | Medida para reducir un sesgo. Hay que medirla, no solo aplicarla. |
| **Antes y después** | La misma tabla por subgrupo calculada sin la medida y con ella, para compararlas fila a fila. |
| **Umbral por grupo** | Decir «cancelará» a partir de una probabilidad distinta en cada grupo. Un umbral más bajo avisa más y detecta más, pero también da más falsas alarmas. |
| **Reponderar** | Dar más peso, al entrenar, a los ejemplos del grupo que va peor. |
| **Validación cruzada** (`cross_val_predict`) | Predice cada dato de entrenamiento con un modelo que no lo ha visto. Sirve para decidir **sin tocar el test** (como en `S07_04`). |
| **`.map`** | Cambia cada valor de una columna según un diccionario: `{"directo": 0.25}` convierte «directo» en 0,25. |
| **Registro de experimentos** | El `registro.csv` del Sprint 15: una fila por prueba. |

**Cómo se hace**

1. **Elegir una medida (5 minutos).** Mirad la tabla por subgrupos del paso 1 y escoged **una** (la que mejor encaje con vuestro sesgo):

    | Medida | En qué consiste |
    |---|---|
    | Reponderar | Dar más peso al entrenar a los ejemplos del subgrupo que va peor |
    | Ajustar el umbral por grupo | Decidir «cancelará» con una probabilidad mínima distinta para cada grupo |
    | Añadir datos | Conseguir más ejemplos del subgrupo que falta |
    | Limitar el uso | Decir en el aviso del demostrador: «no usar el modelo para el grupo X» |

    Aquí tenéis código para las dos primeras (con TurisData y su peor subgrupo, el canal `directo`). Para la tercera y la cuarta, mirad el apartado 7; si vuestro proyecto no es una tabla, el apartado 6.

2. **Guardar el «antes» (5 minutos).** En `04_evaluacion.ipynb`, con las celdas del paso 1 ya ejecutadas (necesitáis la función `medir_subgrupos` y las variables `real`, `pred`):

    ```python
    grupo = X_test["canal"].fillna("sin dato").to_numpy()
    antes = medir_subgrupos(real, pred, grupo)
    avisos_antes = int(pred.sum())
    falsas_antes = int(((pred == 1) & (real == 0)).sum())
    ```

    `antes` es la tabla por canal de siempre y las otras dos variables guardan cuántos avisos y cuántas falsas alarmas hubo. **No cambiéis `pred`**: la medida creará una `pred_nueva` aparte, para poder comparar. Poned vuestra columna donde pone `canal`.

3. **Medida A · umbral por grupo (20 minutos).** Primero, con los datos de entrenamiento, ver qué umbral conviene al grupo:

    ```python
    from sklearn.base import clone
    from sklearn.model_selection import cross_val_predict, StratifiedKFold

    cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)
    prob_cv = cross_val_predict(clone(modelo), X_ent, y_ent, cv=cv, method="predict_proba")[:, 1]
    real_ent = y_ent.to_numpy()
    print("Recall global en validación cruzada:", round(recall_score(real_ent, prob_cv >= UMBRAL), 3))
    en_directo = (X_ent["canal"] == "directo").to_numpy()
    for umbral in [0.35, 0.30, 0.25, 0.20, 0.15]:
        avisa = prob_cv[en_directo] >= umbral
        print(f"umbral {umbral:.2f} → recall {recall_score(real_ent[en_directo], avisa):.3f} · precisión {precision_score(real_ent[en_directo], avisa):.3f}")
    ```

    Qué hace cada parte:

    - `clone(modelo)`: una copia **sin entrenar** del modelo, con los mismos ajustes. `cross_val_predict(…, cv=cv, method="predict_proba")[:, 1]` entrena 5 veces con 4/5 de los datos de entrenamiento y predice el 1/5 restante, así que `prob_cv` es una probabilidad «honesta» para cada reserva de entrenamiento.
    - `en_directo`: `True` donde la reserva es del canal `directo`. Cambiad `"directo"` por vuestro peor subgrupo.
    - El bucle prueba cinco umbrales y escribe, para ese grupo, el recall y la precisión. **Elegid el umbral con el que el recall del grupo se acerca al global sin disparar las falsas alarmas.** Esa es una decisión del equipo y se justifica en la memoria.

    Con el umbral elegido, se aplica al test y se mide el «después»:

    ```python
    UMBRALES = {"agencia": UMBRAL, "directo": 0.25, "empresa": UMBRAL, "web_intermediaria": UMBRAL}
    umbral_fila = X_test["canal"].map(UMBRALES).to_numpy()
    pred_nueva = (prob >= umbral_fila).astype(int)
    despues = medir_subgrupos(real, pred_nueva, grupo)
    ```

    `UMBRALES` dice qué umbral usa cada grupo (todos igual que antes, salvo el que queréis mejorar). `.map(UMBRALES)` pone a cada reserva el umbral de su canal, y `pred_nueva` avisa cuando su probabilidad lo alcanza. **Los nombres de las claves deben coincidir letra por letra con los valores de la columna.**

4. **Medida B · reponderar (15 minutos, opcional).** Probad si dar más peso al grupo ayuda; la prueba se hace también con el entrenamiento, no con el test:

    ```python
    for peso in [1, 2, 3, 5]:
        pesos = np.where(X_ent["canal"] == "directo", float(peso), 1.0)
        prob_peso = cross_val_predict(clone(modelo), X_ent, y_ent, cv=cv, method="predict_proba", params={"m__sample_weight": pesos})[:, 1]
        avisa = prob_peso[en_directo] >= UMBRAL
        print(f"peso {peso} → recall en directo {recall_score(real_ent[en_directo], avisa):.3f} · precisión {precision_score(real_ent[en_directo], avisa):.3f}")
    ```

    `np.where(condición, a, b)` pone el peso `a` a las reservas de `directo` y 1 a las demás. `m__sample_weight` es la forma de decirle al modelo (`Pipeline`) «pasa estos pesos a la pieza `m`» (las dos piezas se llaman `prep` y `m`, como en `S13_02`). Si el recall del grupo no sube, la medida **no funciona**: descartadla, anotadlo y probad otra. Comparar dos medidas cuenta como nivel extra.

5. **Medir antes y después y escribir la lectura (20 minutos).**

    ```python
    tabla = antes[["subgrupo", "reservas", "recall", "precisión"]].merge(
        despues[["subgrupo", "recall", "precisión"]], on="subgrupo", suffixes=(" antes", " después"))
    tabla["cambio en recall (puntos)"] = ((tabla["recall después"] - tabla["recall antes"]) * 100).round(1)
    print(tabla.to_string(index=False))
    print(f"Recall global: {recall_score(real, pred):.1%} → {recall_score(real, pred_nueva):.1%}")
    print(f"Avisos: {avisos_antes} → {int(pred_nueva.sum())} · falsas alarmas: {falsas_antes} → {int(((pred_nueva == 1) & (real == 0)).sum())}")
    ```

    `.merge(…, on="subgrupo")` junta las dos tablas fila a fila por el nombre del subgrupo y `suffixes` añade «antes» y «después» a las columnas repetidas. Debajo, **una frase de lectura honesta** con vuestras cifras: «El recall de [grupo] sube del [X] % al [Y] % y el de [resto] [cambia/no cambia]; a cambio hay [N] falsas alarmas más». Copiad la tabla a una celda de texto.

6. **Si vuestro proyecto no es una tabla (series, imágenes o asistente con documentos).** La idea es la misma (medir por subgrupos, cambiar **una** cosa, medir otra vez), pero los subgrupos y la medida cambian. Elegid la fila de vuestro tipo:

    | Tipo | Subgrupos que medir | Una línea para medirlos | Medida posible |
    |---|---|---|---|
    | **Serie temporal** | Día de la semana, mes o temporada, festivos | `error.groupby(error.index.dayofweek).mean()` (con `error = (real - prediccion).abs()`) | Añadir al modelo una columna del grupo que falla (por ejemplo, «es festivo») y repetir |
    | **Imágenes** | Cada clase, y una condición de la foto (luz, fondo, tamaño) si la apuntasteis | `classification_report(y_test, pred)` para el recall por clase | Más fotos (o giros y recortes) de la clase que va peor; umbral de confianza distinto por clase |
    | **Asistente con documentos** | Tipo de pregunta (directa, de varias fuentes, sin respuesta, intento de engaño) y documento | `resultados.groupby("tipo")["correcta"].mean()` (con una columna `correcta` de 0 o 1 por pregunta) | Subir el umbral de recuperación, o añadir la regla «si no consta, decirlo» y repetir las preguntas |

    El resto de pasos no cambia: guardad el «antes», aplicad una sola medida, medid el «después» con la misma tabla y escribid la frase de lectura. Para el demostrador de estos tres tipos, mirad «Qué adaptar en vuestro proyecto» en `README_demostrador.md` (paso 4).

7. **Si el sesgo no se puede arreglar (en el mismo tiempo).** Para **añadir datos**, decid cuántos casos del grupo faltan y cómo se conseguirían; si no hay forma, es una limitación. Para **limitar el uso**, escribidlo en el campo `limitaciones` del demostrador (paso 4) y en la model card. Esconderlo no es una opción.
8. **Registro de experimentos (15 minutos).** Una fila nueva en `registro.csv` con la medida, el antes y después y la decisión. Si copiasteis `registrar` a `utilidades.py` en el Sprint 15 ([`S15_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/2_Practica/para_casa/S15_01_seguimiento_experimentos.ipynb)), usadla; si no, añadid la fila a mano con las mismas 12 columnas:

    ```python
    registrar("Ana", "RegresionLogistica+umbral_directo", UMBRALES, DATOS_HASH, SEMILLA, "recall_directo", 0.800, 0, 0,
              "Mitigación del canal directo. Test: recall 61,6 % → 79,2 %; +52 falsas alarmas; resto de canales igual")
    ```

    Los argumentos van en este orden: quién la hace (vuestro nombre), modelo, ajustes (`UMBRALES`), huella de los datos (`DATOS_HASH`, de `03_modelos.ipynb`), semilla, nombre de la métrica, su valor en validación cruzada (0,800 es el recall de `directo` con umbral 0,25 de la tabla del apartado 3), su desviación (0 si no la calculasteis: decidlo en `notas`), el tiempo y las notas.

**Qué deberíais ver.** Con el ejemplo de TurisData:
- `Recall global en validación cruzada: 0.834` y, para `directo`, recall 0.597 con umbral 0.35 que sube a 0.800 con 0.25 (precisión de 0.521 a 0.464).
- Con el peso (opcional): recall de `directo` en 0.597, 0.600, 0.600 y 0.591 para los pesos 1, 2, 3 y 5. **No mejora**: reponderar aquí no sirve.
- La tabla de antes y después: `directo` pasa de recall 0.616 a 0.792 (**+17.6 puntos**, precisión de 0.500 a 0.434) y los otros tres canales no cambian (0.0).
- `Recall global: 82.8% → 86.0%` y `Avisos: 967 → 1041 · falsas alarmas: 397 → 449`: la mejora cuesta 52 falsas alarmas más. Con los costes de `S13_02` (50 € por cancelación no detectada, 30 € por falsa alarma) la medida sale unos 460 € más cara en las 1500 reservas de prueba: la equidad tiene precio.

**Hecho cuando:** hay una mitigación aplicada, medida por subgrupo antes y después (con su coste) y anotada en el cuaderno y en el registro de experimentos.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'medir_subgrupos' is not defined` (o `real`, `pred`, `prob`) | Colab se reinició o no se ejecutaron las celdas del paso 1. | Pulsad ▶ por orden desde la primera celda del cuaderno. |
| `ValueError: Pipeline.fit does not accept the sample_weight parameter` | Habéis escrito `sample_weight` en vez de `m__sample_weight`. | Usad el nombre de la pieza del `Pipeline` con dos guiones bajos. |
| El recall de un grupo cae a 0.000 después de aplicar los umbrales | Una clave de `UMBRALES` no coincide con el valor de la columna (por ejemplo `"Directo"` en vez de `"directo"`): `.map` deja un hueco (NaN) y un hueco nunca alcanza el umbral, así que esa reserva no avisa nunca. | Comprobad `X_test["canal"].map(UMBRALES).isna().sum()`: debe dar 0. |
| `TypeError: cross_val_predict() got an unexpected keyword argument 'params'` | Una versión de scikit-learn anterior a la 1.4, donde el argumento se llama `fit_params`. | Cambiad `params=` por `fit_params=` o preguntad al docente. |
| El recall del grupo casi no se mueve (0.597 → 0.600) | La medida no funciona con este modelo. | Anotadlo como resultado, descartadla y probad otra. |
| Sube el recall del grupo pero bajan la precisión y el número de falsas alarmas se dispara | Es el precio de la medida, no un fallo. | Cuantificadlo (avisos y falsas alarmas) y explicadlo en la lectura. |
| Las cifras del «antes» no coinciden con las del paso 1 | Habéis cambiado `UMBRAL`, la partición o el modelo entre medias. | Volved a ejecutar el cuaderno desde la primera celda sin tocar esos tres. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_16_paso_2.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 4 →](Reto_Sprint_16_paso_4.md)
<!--/nav-->
