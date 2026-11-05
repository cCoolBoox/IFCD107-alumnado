# Paso 4 · Pipeline y baseline (día 2, 15 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md) · [Paso 5 →](Reto_Sprint_06_paso_5.md)
<!--/nav-->

1. Construir un `Pipeline` que impute, escale y codifique.
2. Añadir un modelo de referencia y un `DummyClassifier`.
3. Compararlos con validación cruzada y escribir la frase del resultado.

**En sencillo.** Tras la limpieza todavía quedan huecos, números en escalas muy distintas (una antelación de 300 días y un 1 de «cliente repetidor») y texto que el ordenador no sabe usar. Un *pipeline* es una **cadena de montaje**: la tabla entra por un lado, pasa por varias máquinas (rellenar huecos, igualar escalas, convertir texto en números) y sale al modelo, y la cadena entera se monta una vez y se reutiliza igual. Para saber si vuestro modelo vale algo, lo comparáis con un «modelo tonto» que no mira los datos y apunta siempre a lo más frecuente, y lo hacéis con *validación cruzada*: repetir la prueba cinco veces con trozos distintos. No hace falta entender por dentro la regresión logística: basta con que sepáis leer si gana al modelo tonto.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| ***Pipeline*** | Una cadena de pasos (preparar datos y modelo) que se ejecuta siempre en el mismo orden. |
| **`ColumnTransformer`** | La parte de la cadena que prepara cada grupo de columnas de forma distinta: números por un lado, texto por otro. |
| **Imputar (`SimpleImputer`)** | Rellenar huecos: con la mediana en las columnas numéricas y con el valor más frecuente en las de texto. |
| **Escalar (`StandardScaler`)** | Poner las columnas numéricas en una escala parecida, para que una no pese más solo por tener números más grandes. |
| **Codificar (`OneHotEncoder`)** | Convertir una columna de texto en varias columnas de 0 y 1, una por cada valor posible. |
| ***Baseline* o modelo tonto** | El modelo de referencia, que no aprende nada y sirve de suelo: si el vuestro no lo supera, no aporta. |
| **Validación cruzada** | Trocear *train* en 5 partes y repetir 5 veces «entrenar con 4 y puntuar con la que sobra». |
| ***Fold*** | Cada una de esas 5 repeticiones; salen 5 puntuaciones. |
| **AUC (`roc_auc`)** | Una nota de 0,5 a 1: 0,5 es azar y 1 es perfecto. Mide si el modelo pone delante las reservas que se cancelan. |
| **Fuga** | Que el *test* (o información de fuera de lo que se está entrenando) influya en lo que el modelo aprende. |

**Cómo se hace**

1. **Montar el preprocesado.** Celda nueva. Usa `columnas_num` y `columnas_cat` del paso 3:

    ```python
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder

    preprocesado = ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                          ("esc", StandardScaler())]), columnas_num),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore"))]), columnas_cat),
    ])
    ```

    Qué hace cada línea:

    - `from … import …`: trae las piezas de scikit-learn que se van a usar.
    - `ColumnTransformer([…])`: abre la lista de «ventanillas». Cada una tiene un nombre (`"num"`, `"cat"`), qué hace y a qué columnas se aplica.
    - `("num", Pipeline([…]), columnas_num)`: las columnas numéricas pasan primero por `SimpleImputer(strategy="median")` (huecos con la mediana) y luego por `StandardScaler()` (misma escala).
    - `("cat", Pipeline([…]), columnas_cat)`: las de texto pasan por `SimpleImputer(strategy="most_frequent")` (huecos con el valor más frecuente, también en `regimen`) y por `OneHotEncoder(handle_unknown="ignore")`, que no da error si en *test* aparece un valor nuevo.
    - Los nombres `"imp"`, `"esc"`, `"oh"`, `"num"` y `"cat"` los podéis cambiar, pero conviene dejarlos.

2. **Montar el modelo y el modelo tonto.** Celda nueva, con la **misma** cadena de preparación:

    ```python
    from sklearn.linear_model import LogisticRegression
    from sklearn.dummy import DummyClassifier

    modelo = Pipeline([("prep", preprocesado), ("clf", LogisticRegression(max_iter=1000))])
    tonto = Pipeline([("prep", preprocesado), ("clf", DummyClassifier(strategy="prior"))])

    matriz = preprocesado.fit_transform(X_train)
    print(X_train.shape, "→", matriz.shape)
    ```

    Qué hace cada línea:

    - `modelo = Pipeline([("prep", …), ("clf", …)])`: la cadena completa: primero el preprocesado y al final la regresión logística, que predice si una reserva se cancela. `max_iter=1000` le da margen para ajustarse.
    - `tonto = …`: la misma cadena, pero el último paso es `DummyClassifier(strategy="prior")`, que solo mira la proporción de canceladas.
    - `preprocesado.fit_transform(X_train)`: aplica la preparación solo a *train* (es solo para mirar el resultado).
    - `print(X_train.shape, "→", matriz.shape)`: tamaño antes y después. Las columnas de texto se han abierto en muchas de 0 y 1.

3. **Validación cruzada.** Celda nueva:

    ```python
    from sklearn.model_selection import StratifiedKFold, cross_val_score

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMILLA)
    auc_tonto = cross_val_score(tonto, X_train, y_train, cv=cv, scoring="roc_auc")
    auc_modelo = cross_val_score(modelo, X_train, y_train, cv=cv, scoring="roc_auc")

    resultados = pd.DataFrame({
        "media": [auc_tonto.mean(), auc_modelo.mean()],
        "desviación": [auc_tonto.std(), auc_modelo.std()],
    }, index=["modelo tonto", "regresión logística"]).round(3)
    resultados
    ```

    Qué hace cada línea:

    - `StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMILLA)`: define los 5 trozos, mezclados con una semilla y con la misma proporción de canceladas en cada uno.
    - `cross_val_score(modelo, X_train, y_train, cv=cv, scoring="roc_auc")`: en cada vuelta entrena con 4 trozos y puntúa con el que sobra. Devuelve 5 notas.
    - Se usa `X_train`, nunca `X_test`. Como el imputador y el escalador están **dentro** de la cadena, en cada vuelta aprenden solo de los 4 trozos de entrenamiento: eso evita la fuga.
    - `.mean()` y `.std()`: la media de las 5 notas y cuánto varían (desviación).
    - `scoring="roc_auc"` es la métrica del paso. Si preferís `"f1"` (equilibra aciertos y falsas alarmas entre las canceladas), cambiad solo esa palabra y decid cuál elegís y por qué.

4. **Escribir la frase.** Va en el apartado 4 del informe, con vuestras cifras. Ejemplo con las de este fichero: «Nuestro modelo obtiene un AUC medio de 0,758 ± 0,025 frente a 0,500 del modelo tonto. Eso significa que ordena las reservas mucho mejor que el azar». Con `"f1"`: «Un F1 medio de 0,660 ± 0,029 frente a 0,000 del modelo tonto». Para el nivel extra, mirad la partición temporal en [`S06_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/para_casa/S06_04_metricas_validacion.ipynb) y la fuga en [`S06_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/para_casa/S06_03_preprocesado_pipeline.ipynb).

**Qué deberíais ver.** Aproximadamente estas cifras con el CSV del curso:

- `(1200, 15) → (1200, 34)`: las 15 columnas pasan a 34.
- Una tabla de dos filas: modelo tonto con media `0.500` y desviación `0.000`; regresión logística con media `0.758` y desviación `0.025`.
- Las cinco notas de `auc_modelo` van de 0,73 a 0,81, y las del tonto valen 0,5 las cinco veces. Si lo cambiáis a `"f1"`, el tonto da 0,0 y vuestro modelo unos 0,66.
- Vuestro modelo **por encima del tonto**. Si no, algo falla: mirad la «Ayuda 2» de la [ficha del reto](Reto_Sprint_06.md).

**Hecho cuando:** el cuaderno tiene el *pipeline*, la tabla de resultados y la frase con media ± desviación, y sabéis explicar por qué el escalado y la imputación no usan el *test*.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'X_train' is not defined` | No se ejecutó la celda del paso 3 con la partición. | Ejecutad desde arriba o al menos hasta el paso 3. |
| `ValueError: Input X contains NaN.` y `LogisticRegression does not accept missing values encoded as NaN natively` | Falta un `SimpleImputer` en alguna de las ramas, o el modelo recibe columnas que no pasaron por el preprocesado. | Comprobad que `columnas_num` y `columnas_cat` están completas y que cada rama lleva su imputador. |
| `ValueError: Some column names are not columns of the dataframe: {'precio'}` | Un nombre de `columnas_num` o `columnas_cat` no existe en `X`. | Comparad con `X_train.columns` y corregid la errata. |
| `ValueError: Cannot use median strategy with non-numeric data` y `could not convert string to float: 'desayuno'` | Una columna de texto (por ejemplo `regimen`) está en la rama numérica. | Pasadla a `columnas_cat`. |
| `NameError: name 'preprocesado' is not defined` | La celda 1 no se ejecutó. | Ejecutadla antes de la celda del modelo. |
| El modelo tonto da exactamente 0,500 con desviación 0,000 | Es lo esperado: siempre apunta a lo mismo. | No es un error; es el suelo con el que se compara. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_06_paso_3.md) · [Ficha del reto](Reto_Sprint_06.md) · [Paso 5 →](Reto_Sprint_06_paso_5.md)
<!--/nav-->
