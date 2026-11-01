# Paso 2 · Regresión del precio (día 1, 20 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md) · [Paso 3 →](Reto_Sprint_07_paso_3.md)
<!--/nav-->

1. Elegir las variables que **se conocen al reservar**; `cancelada` queda fuera.
2. Separar train y test, y medir el modelo de referencia (precio medio).
3. Ajustar la regresión lineal y comparar.
4. Probar una mejora y decidir si compensa. Contar el resultado en euros.

**En sencillo.** Vais a enseñar al ordenador a **estimar el precio de una noche** a partir de dos datos: el tipo de habitación y la época del año. Un modelo de regresión lineal es como una tarifa con suplementos: un precio base más un extra por cada característica (por ejemplo, «suite: +101 €; temporada alta: +22 €»). Para saber si vale algo, lo comparáis con un modelo de referencia que siempre dice «el precio medio». Después medís en euros cuánto se equivoca. No hace falta saber de álgebra: pandas y scikit-learn hacen las cuentas y vosotros leéis los números. Lo importante es la decisión: **qué variables se pueden usar** sin hacer trampa.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Variable objetivo** | Lo que se quiere predecir. Aquí, `precio_noche`. |
| **Variables predictoras** | Las columnas con las que se predice. Aquí, el tipo de habitación y la temporada. |
| **Fuga** | Usar para predecir un dato que no se conoce al reservar, como `cancelada`. Da buenos resultados falsos. |
| **Coeficiente** | Cuánto suma o resta al precio cada característica: en una regresión lineal se lee directamente en euros. |
| **Variable ficticia (`get_dummies`)** | Convierte una columna de texto en columnas de 0 y 1. `drop_first=True` quita una (la que queda como base). |
| **Modelo de referencia (*baseline*)** | Un modelo muy simple que sirve de suelo. Aquí, predecir siempre el precio medio de *train* (`DummyRegressor`). |
| **Interacción** | Que el efecto de una variable dependa de otra: la temporada alta puede subir más el precio de una suite que el de una estándar. |
| **MAE y RMSE** | El error en euros. MAE es el error medio; RMSE castiga más los errores grandes. Menos es mejor. |
| **R²** | Qué parte de la variación del precio explica el modelo: 0 es nada y 1 es todo. |

**Cómo se hace**

1. **Elegir las variables.** Para cada columna del CSV, una pregunta: «¿se conoce **al reservar**?». Escribid `df.columns.tolist()` en una celda para ver todas. La lista de usadas y excluidas va en el apartado 2 del informe. Una propuesta:

    | Columna | Decisión | Por qué |
    |---|---|---|
    | `precio_noche` | Es la variable objetivo | Es lo que se predice. |
    | `cancelada` | **Fuera** | No se sabe hasta después de reservar: es fuga. |
    | `id_reserva` | Fuera | Es un identificador; no explica el precio. |
    | `fecha_reserva`, `fecha_llegada` | Resumidas en `temporada_alta` | Las fechas sueltas no sirven; la temporada sí. |
    | `tipo_habitacion`, `temporada_alta` | **Dentro** | Se conocen al reservar y explican casi todo el precio. |
    | El resto (`noches`, `canal`, `pais_origen`…) | Fuera de este modelo | Se conocen al reservar, pero apenas mejoran: con todas, el error baja de 7,24 € a unos 7,23 €. |

2. **Preparar X e y y separar train y test.** Celda nueva. Los nombres llevan una `p` de precio para no pisar los del paso 3:

    ```python
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.dummy import DummyRegressor
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.pipeline import make_pipeline
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    Xp = pd.get_dummies(df[["tipo_habitacion"]], drop_first=True).astype(int)
    Xp["temporada_alta"] = df["temporada_alta"]
    yp = df["precio_noche"]
    Xp_train, Xp_test, yp_train, yp_test = train_test_split(Xp, yp, test_size=0.2, random_state=SEMILLA)
    print(Xp.shape, Xp_train.shape, Xp_test.shape)
    ```

    Qué hace cada línea:

    - `from … import …`: trae las piezas de scikit-learn que se usan en este paso.
    - `pd.get_dummies(df[["tipo_habitacion"]], drop_first=True)`: convierte el tipo de habitación en tres columnas de 0 y 1 (familiar, suite, superior); la estándar queda como base. `.astype(int)` asegura que son números.
    - `Xp["temporada_alta"] = …`: añade la temporada como cuarta columna.
    - `yp = df["precio_noche"]`: lo que se predice.
    - `train_test_split(…, test_size=0.2, random_state=SEMILLA)`: aparta el 20 % de las reservas como test (las que el modelo no ve al aprender). Devuelve cuatro cosas, en este orden.

3. **Medir los tres modelos.** Celda nueva. Es el máximo permitido: referencia, lineal y una mejora.

    ```python
    modelos = {
        "Referencia (media)": DummyRegressor(strategy="mean"),
        "Regresión lineal": LinearRegression(),
        "Lineal con interacciones": make_pipeline(PolynomialFeatures(degree=2, interaction_only=True, include_bias=False), LinearRegression()),
    }
    filas = {}
    for nombre, modelo in modelos.items():
        modelo.fit(Xp_train, yp_train)
        pred = modelo.predict(Xp_test)
        filas[nombre] = {"MAE (€)": mean_absolute_error(yp_test, pred),
                         "RMSE (€)": mean_squared_error(yp_test, pred) ** 0.5,
                         "R²": r2_score(yp_test, pred)}
    resultados_precio = pd.DataFrame(filas).T.round(3)
    resultados_precio
    ```

    Qué hace cada línea:

    - `modelos = {…}`: un diccionario con tres modelos, cada uno con un nombre. `PolynomialFeatures(…, interaction_only=True)` añade los cruces entre variables, por ejemplo suite × temporada alta.
    - `for nombre, modelo in modelos.items():`: repite lo de debajo (con la sangría) una vez por modelo. Las líneas de dentro **llevan 4 espacios**.
    - `modelo.fit(Xp_train, yp_train)`: el modelo aprende con *train*.
    - `pred = modelo.predict(Xp_test)`: predice el precio de las reservas de *test*.
    - `mean_absolute_error(yp_test, pred)`, `mean_squared_error(…) ** 0.5` y `r2_score(…)`: comparan lo predicho con el precio real y dan MAE, RMSE y R².
    - `pd.DataFrame(filas).T.round(3)`: junta los resultados en una tabla con una fila por modelo (`.T` la gira) y 3 decimales.

4. **Leer los coeficientes en euros.** Celda nueva:

    ```python
    lineal = modelos["Regresión lineal"]
    print(pd.Series(lineal.coef_, index=Xp.columns).round(1))
    print("Precio base (estándar en temporada baja):", round(lineal.intercept_, 1), "€")
    ```

    Qué hace cada línea:

    - `modelos["Regresión lineal"]`: recupera el modelo lineal ya ajustado.
    - `lineal.coef_`: el extra en euros de cada columna; `pd.Series(…, index=Xp.columns)` les pone nombre.
    - `lineal.intercept_`: el precio base, cuando todo vale 0 (habitación estándar y temporada baja).

5. **Decidir y escribir la frase.** Mirad la tabla: ¿la lineal gana a la referencia? ¿Compensa la mejora con interacciones? Si apenas mejora, quedaos con el modelo sencillo y decidlo en el informe. Otra mejora posible es la regularización Ridge o Lasso de [`S07_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_02_ridge_lasso.ipynb). Escribid la frase en euros con vuestras cifras: «nos equivocamos de media en X € por noche».

**Qué deberíais ver.** Aproximadamente, con el CSV del curso:

- `(6000, 4) (4800, 4) (1200, 4)`: 4 columnas; 4800 reservas para entrenar y 1200 para test.
- Una tabla con una fila por modelo: **Referencia (media)** con MAE 25,564 € y R² -0,002; **Regresión lineal** con MAE 7,239 €, RMSE 9,704 € y R² 0,915; **Lineal con interacciones** con MAE 6,758 €, RMSE 8,936 € y R² 0,928.
- Coeficientes: familiar 45,0 · suite 101,2 · superior 28,4 · temporada alta 22,4, y `Precio base … 67.3 €`.
- La lineal mejora mucho a la referencia; las interacciones mejoran solo unos 0,5 € de MAE. Es lo esperado en `S07_01`: R² por encima de 0,85 y MAE de entre 5 y 15 €. Si el vuestro está muy lejos, mirad la «Ayuda 2» de la [ficha del reto](Reto_Sprint_07.md).

**Hecho cuando:** la tabla de precio está en el cuaderno, sin `cancelada` entre las variables, y tenéis la frase del error medio en euros.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'df' is not defined` | La celda del paso 1 no se ha ejecutado. | Ejecutad el cuaderno de arriba abajo. |
| `KeyError: 'tipo_habitacio'` (o el nombre que sea) | El nombre de la columna no es exacto. | Copiadlo de `df.columns`. |
| `ValueError: could not convert string to float: 'estandar'` | Se pasó la columna de texto sin convertirla a 0 y 1. | Usad `pd.get_dummies(…)` como en el punto 2. |
| `ValueError: Found input variables with inconsistent numbers of samples: [4800, 6000]` | `X` e `y` no tienen las mismas filas (por ejemplo, una es de *train* y la otra de todo el CSV). | Usad `Xp_train` con `yp_train`, y `Xp_test` con `yp_test`. |
| Las tres filas de la tabla salen casi iguales | `cancelada` o `precio_noche` se han colado en `Xp`. | `Xp.columns` debe tener solo los 3 tipos de habitación y `temporada_alta`. |
| Los números no coinciden con los de esta página | Otro `random_state` o otra versión de las librerías. | Mirad que `SEMILLA = 42` y esperad cifras parecidas, no idénticas. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_07_paso_1.md) · [Ficha del reto](Reto_Sprint_07.md) · [Paso 3 →](Reto_Sprint_07_paso_3.md)
<!--/nav-->
