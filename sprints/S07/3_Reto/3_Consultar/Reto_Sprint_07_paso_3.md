# Paso 3 · Clasificación de la cancelación y elección del umbral (día 2, 25 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md) · [Paso 4 →](Reto_Sprint_07_paso_4.md)
<!--/nav-->

1. Separar train y test, y **no tocar el test** hasta el final.
2. Medir la referencia (siempre «no cancela») y la regresión logística; dibujar la matriz de confusión y las curvas ROC y PR.
3. Elegir el umbral que minimiza el coste con validación cruzada sobre train.
4. Usar el test **una sola vez**, al final, para dar el coste esperado.

**En sencillo.** El modelo no dice «se cancela» o «no se cancela»: da una **probabilidad** para cada reserva (por ejemplo, 0,62). Vosotros decidís a partir de qué probabilidad hacéis saltar la alarma: ese corte es el **umbral**. Un umbral bajo avisa mucho (más falsas alarmas, menos habitaciones vacías); uno alto avisa poco. El mejor umbral no es «0,5 porque sí»: es el que **cuesta menos euros** con los costes que acordasteis en el paso 1. Se busca probando muchos umbrales con datos de entrenamiento, y el test, que es como el examen final, se abre **una sola vez** para contar cuánto ahorraríais. No hace falta entender cómo calcula la regresión logística: se usa tal cual.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Probabilidad (`predict_proba`)** | Para cada reserva, un número entre 0 y 1: cuánto cree el modelo que se cancelará. |
| **Umbral** | El corte: si la probabilidad es igual o mayor, el modelo avisa de que se cancelará. |
| **Matriz de confusión** | Una tabla 2×2 que cuenta aciertos y errores: VN (no cancela y acierta), FP (falsa alarma), FN (cancelación no prevista) y VP (cancela y acierta). |
| **Precisión y recall** | Precisión: de los avisos que da el modelo, cuántos son ciertos. Recall: de las cancelaciones reales, cuántas detecta. |
| **Coste total** | FN × `COSTE_FN` + FP × `COSTE_FP`: lo que cuestan en euros los errores. |
| **`cross_val_predict`** | Da una probabilidad a cada reserva de *train* con un modelo que **no la ha visto** (se divide *train* en 5 trozos). |
| **Curva ROC y AUC** | Muestran cómo se comporta el modelo con todos los umbrales a la vez. AUC va de 0,5 (azar) a 1 (perfecto). |
| **Curva PR y AP** | Lo mismo, pero fijándose en las cancelaciones: precisión frente a recall. AP es el resumen. |
| **Modelo de referencia (`tonto`)** | `DummyClassifier(strategy="most_frequent")`: dice siempre «no cancela». Es el «no hacer nada». |

**Cómo se hace**

1. **Separar train y test y montar los modelos.** Primera celda de este paso. Como en [`S07_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_03_regresion_logistica.ipynb). Son 2 modelos (la referencia y la logística); el máximo es 3 por problema.

    ```python
    from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedKFold
    from sklearn.linear_model import LogisticRegression
    from sklearn.dummy import DummyClassifier
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.base import clone
    from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay, roc_curve, roc_auc_score,
                                 precision_recall_curve, average_precision_score)
    import matplotlib.pyplot as plt

    columnas_num = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche",
                    "peticiones_especiales", "cliente_repetidor", "cancelaciones_previas", "temporada_alta"]
    columnas_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
    X, y = df[columnas_num + columnas_cat], df["cancelada"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)

    prep = ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), columnas_num),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore", drop="if_binary"))]), columnas_cat),
    ])
    logit = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))])
    tonto = Pipeline([("prep", clone(prep)), ("clf", DummyClassifier(strategy="most_frequent"))])
    print(X_train.shape, X_test.shape, round(y_train.mean(), 3), round(y_test.mean(), 3))
    ```

    Qué hace cada línea:

    - `from … import …`: trae las piezas que se usan en todo el paso. `matplotlib.pyplot as plt` es para dibujar.
    - `columnas_num` y `columnas_cat`: las columnas de números y de texto que se conocen al reservar. Quedan fuera `cancelada` (es `y`), `id_reserva` y las fechas.
    - `X, y = …` y `train_test_split(…, stratify=y)`: apartan el 20 % para test y mantienen la misma proporción de canceladas en las dos partes.
    - `prep = ColumnTransformer([…])`: la preparación (rellenar huecos, igualar escalas, pasar texto a 0 y 1), ajustada solo con lo que le llegue a `fit`.
    - `logit` y `tonto`: la misma preparación con distinto modelo al final. `clone(prep)` hace una copia independiente.

2. **Escribir las funciones de las métricas y del coste.** Celda nueva. Ojo: aquí **no hay costes por defecto**, así que Python os obliga a pasar los vuestros (`coste_total` de `S07_03` trae FN = 3 y FP = 1).

    ```python
    def metricas_umbral(y_real, proba, umbral):
        pred = (proba >= umbral).astype(int)
        vn, fp, fn, vp = confusion_matrix(y_real, pred).ravel()
        return {"umbral": umbral, "VN": int(vn), "FP": int(fp), "FN": int(fn), "VP": int(vp),
                "precision": float(vp / (vp + fp)) if (vp + fp) else np.nan,
                "recall": float(vp / (vp + fn))}

    def coste_total(y_real, proba, umbral, coste_fn, coste_fp):
        m = metricas_umbral(y_real, proba, umbral)
        return m["FN"] * coste_fn + m["FP"] * coste_fp
    ```

    Qué hace cada línea:

    - `pred = (proba >= umbral).astype(int)`: convierte cada probabilidad en un aviso (1) o no (0) según el umbral.
    - `confusion_matrix(y_real, pred).ravel()`: cuenta VN, FP, FN y VP, en ese orden.
    - `return {…}`: devuelve un diccionario con los cuatro conteos, la precisión y el recall.
    - `coste_total(…)`: multiplica los FN por `coste_fn` y los FP por `coste_fp`, y suma.

3. **Elegir el umbral con validación cruzada sobre train.** Celda nueva. Aquí **no se usa el test**:

    ```python
    cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)
    proba_cv = cross_val_predict(logit, X_train, y_train, cv=cv, method="predict_proba")[:, 1]
    umbrales = np.arange(0.05, 0.96, 0.05)

    def buscar_umbral(coste_fn, coste_fp):
        """Prueba todos los umbrales con las probabilidades de train y devuelve el de menor coste."""
        costes = []
        for u in umbrales:
            costes.append(coste_total(y_train, proba_cv, u, coste_fn, coste_fp))
        mejor = round(float(umbrales[np.argmin(costes)]), 2)
        return mejor, costes

    mejor_umbral, costes = buscar_umbral(COSTE_FN, COSTE_FP)
    plt.plot(umbrales, costes, marker="o")
    plt.axvline(mejor_umbral, color="red", linestyle="--", label=f"Mejor umbral: {mejor_umbral}")
    plt.xlabel("Umbral"); plt.ylabel("Coste total en train (€)"); plt.legend(); plt.show()
    print("Umbral elegido:", mejor_umbral)
    ```

    Qué hace cada línea:

    - `cross_val_predict(…, method="predict_proba")[:, 1]`: la probabilidad de cancelar de cada reserva de *train*, calculada con un modelo que no la vio. El `[:, 1]` se queda con la columna de «cancela».
    - `np.arange(0.05, 0.96, 0.05)`: los umbrales a probar, de 0,05 a 0,95 de 0,05 en 0,05.
    - `def buscar_umbral(…)`: calcula el coste de cada umbral con `for` y se queda con el menor (`np.argmin`). **Se reutiliza en el paso 4.**
    - `buscar_umbral(COSTE_FN, COSTE_FP)`: usa vuestros costes del paso 1. Guarda el umbral en `mejor_umbral` y la lista en `costes`.
    - `plt.plot(…)` y `plt.axvline(…)`: dibujan la curva y una línea roja en el mejor umbral.

4. **Abrir el test, una vez.** Celda nueva. Con el umbral ya elegido, calcula el coste de tres formas y dibuja la matriz:

    ```python
    logit.fit(X_train, y_train)
    tonto.fit(X_train, y_train)
    proba_test = logit.predict_proba(X_test)[:, 1]

    coste_sin_modelo = y_test.sum() * COSTE_FN
    coste_05 = coste_total(y_test, proba_test, 0.5, COSTE_FN, COSTE_FP)
    coste_elegido = coste_total(y_test, proba_test, mejor_umbral, COSTE_FN, COSTE_FP)
    print("Coste en test sin modelo: {:,.0f} €".format(coste_sin_modelo))
    print("Coste en test con umbral 0.5: {:,.0f} €".format(coste_05))
    print("Coste en test con umbral {}: {:,.0f} €".format(mejor_umbral, coste_elegido))
    ahorro = coste_sin_modelo - coste_elegido
    print("Ahorro frente a no hacer nada: {:,.0f} € ({:.0%})".format(ahorro, ahorro / coste_sin_modelo))

    m = metricas_umbral(y_test, proba_test, mejor_umbral)
    print("VN {VN} · FP {FP} · FN {FN} · VP {VP}".format(**m))
    print("Precisión {:.0%} · Recall {:.0%}".format(m["precision"], m["recall"]))
    ConfusionMatrixDisplay.from_predictions(y_test, (proba_test >= mejor_umbral).astype(int),
                                            display_labels=["Se mantiene", "Cancela"], cmap="Blues", colorbar=False)
    plt.title(f"Matriz de confusión en test (umbral {mejor_umbral})")
    plt.xlabel("Lo que dice el modelo"); plt.ylabel("Lo que pasó")
    plt.show()
    ```

    Qué hace cada línea:

    - `logit.fit(X_train, y_train)`: el modelo aprende con *train*. `predict_proba(X_test)` da la probabilidad de cada reserva de test.
    - `coste_sin_modelo`: sin modelo nunca se avisa, así que todas las cancelaciones reales (`y_test.sum()`) son falsos negativos.
    - `coste_05` y `coste_elegido`: el coste con el umbral 0,5 y con el que elegisteis.
    - `"{:,.0f}".format(x)`: escribe el número sin decimales y con separador de miles (Colab usa la coma: `156,484`).
    - `ConfusionMatrixDisplay.from_predictions(…)`: dibuja la matriz; el resto de líneas le ponen título y nombres.

5. **Dibujar las curvas ROC y PR** (nivel estándar; para el mínimo basta la matriz). Celda nueva, con las funciones de [`S07_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_04_roc_pr_desbalance.ipynb):

    ```python
    proba_tonto = tonto.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, proba_test)
    prec, rec, _ = precision_recall_curve(y_test, proba_test)
    auc, ap = roc_auc_score(y_test, proba_test), average_precision_score(y_test, proba_test)

    fig, ejes = plt.subplots(1, 2, figsize=(10, 4))
    ejes[0].plot(fpr, tpr, label=f"Regresión logística (AUC {auc:.2f})")
    ejes[0].plot([0, 1], [0, 1], "--", color="gray", label="Azar")
    ejes[0].set(title="Curva ROC", xlabel="Falsas alarmas (tasa)", ylabel="Cancelaciones detectadas (tasa)")
    ejes[1].plot(rec, prec, label=f"Regresión logística (AP {ap:.2f})")
    ejes[1].axhline(y_test.mean(), linestyle="--", color="gray", label="Referencia")
    ejes[1].set(title="Curva PR", xlabel="Recall", ylabel="Precisión")
    ejes[0].legend(); ejes[1].legend()
    plt.tight_layout(); plt.show()
    print(f"AUC {auc:.3f} · AP {ap:.3f} · referencia: AUC {roc_auc_score(y_test, proba_tonto):.3f}, AP {average_precision_score(y_test, proba_tonto):.3f}")
    ```

    - `roc_curve(…)` y `precision_recall_curve(…)`: calculan los puntos de cada curva con todos los umbrales. El `_` guarda lo que no se usa.
    - `plt.subplots(1, 2, …)`: dos gráficos lado a lado; `ejes[0].plot(…)` dibuja en el primero y `ejes[1]` en el segundo.
    - La línea gris es la referencia: el azar en la ROC y la proporción de canceladas en la PR.

**Qué deberíais ver.** Con los costes del ejemplo del paso 1 (284 y 103), aproximadamente:

- `(4800, 15) (1200, 15) 0.459 0.459`: casi un 46 % de canceladas en las dos partes.
- Una curva de coste en U, con un mínimo claro, y `Umbral elegido: 0.25`.
- Coste en test: `156,484 €` sin modelo, `78,439 €` con el umbral 0.5 y `58,331 €` con el elegido, y `Ahorro frente a no hacer nada: 98,153 € (63%)`. El umbral elegido cuesta menos que el 0,5.
- `VN 204 · FP 445 · FN 44 · VP 507` y `Precisión 53% · Recall 92%`: se avisa mucho, con muchas falsas alarmas, porque un FN cuesta casi tres veces más que un FP.
- `AUC 0.746 · AP 0.729 · referencia: AUC 0.500, AP 0.459`.

Con vuestros costes saldrán otras cifras: lo que no cambia es que el mínimo es claro y que el elegido cuesta menos que el 0,5.

**Hecho cuando:** hay umbral elegido con vuestros costes, el coste en test está calculado una sola vez y nadie ha mirado el test para elegir el umbral.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'COSTE_FN' is not defined` | La celda del paso 1 no se ha ejecutado. | Ejecutad desde arriba. |
| `TypeError: coste_total() missing 2 required positional arguments: 'coste_fn' and 'coste_fp'` | Se llamó a `coste_total` sin los costes. | Pasad `COSTE_FN` y `COSTE_FP` al final de la llamada. |
| `ValueError: Found input variables with inconsistent numbers of samples: [1200, 4800, 1200]` | Se mezclaron probabilidades de *train* con la `y` de *test* (o al revés). | Con `proba_cv` va `y_train`; con `proba_test`, `y_test`. |
| `IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed` | Falta `method="predict_proba"` en `cross_val_predict`. | Añadidlo: sin él devuelve 0 y 1, no probabilidades. |
| `NotFittedError: This Pipeline instance is not fitted yet…` | Se usó `predict_proba` antes de `fit`. | Ejecutad primero `logit.fit(X_train, y_train)` (y `tonto.fit(…)`). |
| El umbral elegido es alto (por ejemplo 0,65) y el ahorro es pequeño | `COSTE_FN` es bajo frente a `COSTE_FP`: avisar sale caro y el modelo apenas avisa. | Revisad las razones de los costes del paso 1. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_07_paso_2.md) · [Ficha del reto](Reto_Sprint_07.md) · [Paso 4 →](Reto_Sprint_07_paso_4.md)
<!--/nav-->
