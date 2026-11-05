# Paso 1 · Preparar el terreno y repetir el baseline (día 1, 130 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 2 →](Reto_Sprint_15_paso_2.md)
<!--/nav-->

1. Fijar la semilla, anotar las versiones y crear el registro con la plantilla.
2. Definir la partición común y escribir qué modelos se van a probar y por qué.
3. Repetir el *baseline* y anotarlo como primera fila del registro.
4. Entrenar el primer modelo clásico y anotarlo.

**En sencillo.** Este sprint se parece a un laboratorio: vais a probar varios modelos y hay que **apuntar cada prueba**, porque al tercer día nadie recuerda si aquel 0,75 era con la semilla 1 o la 42. Hoy preparáis el terreno: un cuaderno común, una forma de dejar el azar fijo (la **semilla**), un **cuaderno de notas** en forma de tabla (el **registro**) y un reparto de los datos que no se cambia nunca. Con eso hecho, repetís el modelo más simple (el *baseline*) y entrenáis el primero de verdad. No hace falta entender cómo funciona cada modelo: el código viene de la práctica `S15_01` y solo cambiáis las líneas marcadas.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Semilla** | Un número fijo (42) que hace que el azar dé siempre lo mismo. Con ella, otra persona obtiene exactamente vuestras cifras. |
| **Registro de experimentos** | Una tabla (`registro.csv`) con una fila por prueba: quién, qué modelo, con qué ajustes y qué resultado. |
| **Hiperparámetro** | Un ajuste que elegís vosotros antes de entrenar (por ejemplo, la profundidad de un árbol). |
| **Validación cruzada** | Partir el entrenamiento en 5 trozos y entrenar 5 veces, probando cada vez en el trozo que no se ha visto. Da una **media** y una **desviación**. |
| **Test** | Datos apartados que no se miran hasta el final. Se usan **una sola vez**. |
| **Pipeline** | Una cadena de pasos (escalar, codificar, modelo) que se aprende solo con el entrenamiento. |
| **Huella (hash)** | Un código corto que cambia si cambian los datos. |
| **AUC** | Una métrica de 0 a 1 para clasificar: 0,5 es azar y 1 es perfecto. |

**Cómo se hace**

1. **Crear el cuaderno común (5 minutos).** Una persona (la responsable técnica) abre Colab, *Archivo → Cuaderno nuevo*, lo llama `03_modelos.ipynb` y pulsa **Compartir** (arriba a la derecha) para dar acceso de **editor** al resto. Subid también vuestro archivo de datos (panel 📁 de la izquierda). Todo el equipo trabaja en **este mismo cuaderno**: lo común arriba, y debajo una sección por persona con su nombre. **No editéis las celdas de otra persona.**

2. **Semilla y versiones (10 minutos).** Si ya hicisteis [`S15_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S15/2_Practica/para_casa/S15_01_seguimiento_experimentos.ipynb), copiad de allí estas celdas. En la primera celda de `03_modelos.ipynb` van las importaciones:

    ```python
    import os, sys, time, json, random, hashlib
    from datetime import datetime
    import numpy as np
    import pandas as pd
    import sklearn
    from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.dummy import DummyClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
    from sklearn.metrics import roc_auc_score
    ```

    En la segunda, la semilla y las versiones:

    ```python
    def fijar_semillas(semilla):
        random.seed(semilla)
        np.random.seed(semilla)
        os.environ["PYTHONHASHSEED"] = str(semilla)
        return np.random.default_rng(semilla)

    SEMILLA = 42
    rng = fijar_semillas(SEMILLA)

    ENTORNO = {"python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__, "scikit-learn": sklearn.__version__}
    print(json.dumps(ENTORNO, indent=2))
    ```

    Qué hace cada línea:

    - `import` carga las herramientas que se usarán; **no se cambian**.
    - `fijar_semillas` fija el azar de `random` y de `numpy`; `SEMILLA = 42` es el número. **No lo cambiéis hasta que salga un resultado bonito: nunca.** Es trampa.
    - `ENTORNO` junta las versiones y `print(json.dumps(...))` las escribe. Salen cuatro líneas: `python`, `numpy`, `pandas` y `scikit-learn` con su versión (con las vuestras, que dependen de Colab). Copiadlas en una celda de texto y más tarde en el README.

3. **Crear el registro (10 minutos).** El registro tiene doce columnas, las mismas que la plantilla [`registro_experimentos_plantilla.csv`](../1_Trabajar/plantillas/registro_experimentos_plantilla.csv) (que solo trae esa cabecera). No hace falta subir la plantilla: este código crea `registro.csv` con esas columnas.

    | Columna | Qué se anota |
    |---|---|
    | `id` | Un número que sube con cada prueba (1, 2, 3…) |
    | `fecha`, `responsable` | Cuándo y **quién** hizo la prueba (demuestra que participa todo el equipo) |
    | `modelo`, `hiperparametros` | Qué modelo y con qué ajustes |
    | `datos_hash`, `semilla` | Una huella corta de los datos y la semilla usada |
    | `metrica`, `valor_cv`, `desv_cv` | La métrica que fijasteis en el sprint 14, su media y su desviación en validación cruzada |
    | `tiempo_s`, `notas` | Cuánto tardó y lo que habéis aprendido; aquí se marca también si el código lo generó una IA |

    ```python
    RUTA_REGISTRO = "registro.csv"
    COLUMNAS = ["id", "fecha", "responsable", "modelo", "hiperparametros", "datos_hash", "semilla",
                "metrica", "valor_cv", "desv_cv", "tiempo_s", "notas"]
    if os.path.exists(RUTA_REGISTRO):
        os.remove(RUTA_REGISTRO)

    def registrar(responsable, modelo, hiperparametros, datos_hash, semilla, metrica, valor_cv, desv_cv, tiempo_s, notas=""):
        existe = os.path.exists(RUTA_REGISTRO)
        n = len(pd.read_csv(RUTA_REGISTRO)) if existe else 0
        fila = pd.DataFrame([{
            "id": n + 1, "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"), "responsable": responsable, "modelo": modelo,
            "hiperparametros": json.dumps(hiperparametros, sort_keys=True), "datos_hash": datos_hash, "semilla": semilla,
            "metrica": metrica, "valor_cv": round(float(valor_cv), 4), "desv_cv": round(float(desv_cv), 4),
            "tiempo_s": round(float(tiempo_s), 2), "notas": notas}], columns=COLUMNAS)
        fila.to_csv(RUTA_REGISTRO, mode="a", header=not existe, index=False)
        return n + 1
    ```

    - `registrar(...)` añade **una fila** al final de `registro.csv`: si el archivo no existe lo crea con la cabecera, y el `id` es el número de filas + 1. **No cambiéis los nombres de las columnas.**
    - Las líneas con `os.remove` borran el registro al empezar para que cada ejecución completa del cuaderno lo **rehaga desde cero** (sin filas repetidas). El `registro.csv` final es, por tanto, el resultado de ejecutar el cuaderno entero.

4. **Datos y partición común (20 minutos).** Una sola partición para todo el equipo, que no se cambia. Es la primera del sprint 14: con la misma semilla sale **el mismo test**. El test se aparta ahora y **no se toca hasta el paso 5**.

    ```python
    RUTA = "mis_datos.csv"
    OBJETIVO = "cancelada"
    QUITAR = ["id_reserva", "fecha_reserva", "fecha_llegada"]

    df = pd.read_csv(RUTA, parse_dates=["fecha_reserva", "fecha_llegada"])
    df["mes_llegada"] = df["fecha_llegada"].dt.month
    X = df.drop(columns=QUITAR + [OBJETIVO])
    y = df[OBJETIVO]
    X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEMILLA)

    DATOS_HASH = hashlib.md5(pd.util.hash_pandas_object(df, index=True).values.tobytes()).hexdigest()[:8]
    print("Huella de los datos:", DATOS_HASH, "· entrenamiento:", X_ent.shape, "· test (sin tocar):", X_test.shape)
    ```

    - **Cambiad** `RUTA`, `OBJETIVO` (la columna a predecir) y `QUITAR` (identificadores y fechas en bruto: no son pistas válidas). Las dos líneas de `parse_dates` y `mes_llegada` son del ejemplo con fechas: adaptadlas o borradlas.
    - `X` son las pistas y `y` la respuesta. `X_ent` es el entrenamiento (con validación cruzada dentro) y `X_test` se guarda.
    - `DATOS_HASH` es la huella. Con `reservas_turisdata.csv` sale `Huella de los datos: 800f40b2 · entrenamiento: (4800, 15) · test (sin tocar): (1200, 15)`. Con vuestros datos saldrán otros números.

5. **Escribir el plan (en una celda de texto).** Debajo de lo anterior, una celda de texto con **qué vais a probar y por qué**. Ejemplo: «Regresión logística (simple y explicable), bosque aleatorio y *gradient boosting* (capturan relaciones que no son líneas rectas) y una red neuronal pequeña. Ajustaremos solo en validación: la profundidad del bosque». **No vale «probar 200 combinaciones y quedarse con la mejor».**

6. **El baseline como fila 1 (30 minutos).** Las funciones de comparación (la cadena de pasos, el reparto de la validación cruzada y `experimento`) y el *baseline* del sprint 14:

    ```python
    categoricas = X.select_dtypes("object").columns.tolist()
    METRICA = "AUC"
    SCORING = "roc_auc"

    def crear_pipeline(estimador, columnas):
        numericas = [c for c in columnas if c not in categoricas]
        prep = ColumnTransformer([("num", StandardScaler(), numericas), ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas)])
        return Pipeline([("prep", prep), ("m", estimador)])

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMILLA)

    def experimento(nombre, estimador, hiperparametros, responsable="equipo", notas="", Xd=None):
        Xd = X_ent if Xd is None else Xd
        t0 = time.time()
        puntuaciones = cross_val_score(crear_pipeline(estimador, Xd.columns), Xd, y_ent, cv=cv, scoring=SCORING)
        registrar(responsable, nombre, hiperparametros, DATOS_HASH, SEMILLA, METRICA, puntuaciones.mean(), puntuaciones.std(), time.time() - t0, notas)
        return puntuaciones.mean(), puntuaciones.std()

    media, desv = experimento("Baseline", DummyClassifier(strategy="prior"), {"strategy": "prior"}, responsable="Ana", notas="referencia mínima")
    print(f"Baseline: {media:.3f} ± {desv:.3f}")
    ```

    - `METRICA` es el nombre que se escribe en el registro y `SCORING` el mismo concepto con el nombre de scikit-learn. **Poned la métrica que fijasteis en el sprint 14**: F1 es `"f1"` y exactitud es `"accuracy"`.
    - `crear_pipeline` convierte los números a una misma escala y los textos en columnas de 0 y 1, **dentro** de la cadena, para que solo se aprenda con el entrenamiento. `cv` define los 5 trozos.
    - `experimento` entrena y evalúa con validación cruzada, mide el tiempo y **registra la fila**. **Cambiad `"Ana"` por vuestro nombre** en el parámetro `responsable`.
    - El `Baseline` con `DummyClassifier(strategy="prior")` no mira las pistas y sale con `Baseline: 0.500 ± 0.000`: eso es el azar. Debe ser la **fila 1**.

7. **El primer modelo (55 minutos).** Una persona entrena el primero mientras las demás preparan el siguiente en su sección. En una celda nueva, con vuestro nombre:

    ```python
    media, desv = experimento("RegresionLogistica", LogisticRegression(max_iter=2000), {"C": 1.0}, responsable="Ana")
    print(f"Regresión logística: {media:.3f} ± {desv:.3f}")
    ```

    Con los datos de práctica sale `Regresión logística: 0.755 ± 0.012`. Las cifras de los vuestros serán otras: lo que importa es que **supere al baseline**. Comprobad el registro con `pd.read_csv(RUTA_REGISTRO)`: debe tener las filas 1 (*baseline*) y 2.

8. **Comprobar la semilla.** Elegid *Entorno de ejecución → Reiniciar y ejecutar todo* y mirad que las cifras salen **iguales** que antes. Si cambian, algo usa azar sin semilla.

9. **Si vuestros datos son una serie temporal** (brief 1 o 4), sustituid los apartados 4 y 6 por esto. El reparto es por fechas (los últimos 91 días van al test) y se valida con `TimeSeriesSplit`, que respeta el orden del tiempo:

    ```python
    from sklearn.model_selection import TimeSeriesSplit
    from sklearn.dummy import DummyRegressor
    from sklearn.linear_model import Ridge
    from sklearn.ensemble import HistGradientBoostingRegressor
    from sklearn.metrics import mean_absolute_error

    df = pd.read_csv("mis_datos.csv", parse_dates=["fecha"]).sort_values("fecha")
    df["mes"] = df["fecha"].dt.month
    df["dia_semana"] = df["fecha"].dt.dayofweek
    X = df[["mes", "dia_semana", "festivo"]]
    y = df["ocupacion_pct"]
    DIAS = 91
    X_ent, X_test = X.iloc[:-DIAS], X.iloc[-DIAS:]
    y_ent, y_test = y.iloc[:-DIAS], y.iloc[-DIAS:]
    print(X_ent.shape, X_test.shape)
    DATOS_HASH = hashlib.md5(pd.util.hash_pandas_object(df, index=True).values.tobytes()).hexdigest()[:8]

    def crear_pipeline(estimador, columnas):
        return Pipeline([("prep", StandardScaler()), ("m", estimador)])

    cv = TimeSeriesSplit(n_splits=5)

    def experimento(nombre, estimador, hiperparametros, responsable="equipo", notas="", Xd=None):
        Xd = X_ent if Xd is None else Xd
        t0 = time.time()
        errores = -cross_val_score(crear_pipeline(estimador, Xd.columns), Xd, y_ent, cv=cv, scoring="neg_mean_absolute_error")
        registrar(responsable, nombre, hiperparametros, DATOS_HASH, SEMILLA, "MAE", errores.mean(), errores.std(), time.time() - t0, notas)
        return errores.mean(), errores.std()

    errores = []
    for ent, val in cv.split(X_ent):
        errores.append(mean_absolute_error(y_ent.iloc[val], y_ent.shift(7).iloc[val]))
    registrar("Ana", "Baseline_semana_pasada", {"desfase_dias": 7}, DATOS_HASH, SEMILLA, "MAE", np.mean(errores), np.std(errores), 0, "igual que la semana pasada")
    media, desv = experimento("Ridge", Ridge(), {"alpha": 1.0}, responsable="Ana")
    print(f"MAE de la semana pasada: {np.mean(errores):.2f} ± {np.std(errores):.2f} · Ridge: {media:.2f} ± {desv:.2f}")
    ```

    Cambiad el nombre del archivo, `ocupacion_pct` (lo que predecís) y las pistas de `X`. En series la métrica es un **error** (MAE), y cuanto **menor**, mejor; el signo menos pasa a positivo lo que `scikit-learn` devuelve como negativo. Con `ocupacion_diaria.csv` salen `(1005, 3) (91, 3)` y `MAE de la semana pasada: 4.77 ± 0.36 · Ridge: 8.26 ± 3.88` (dos filas nuevas en el registro, la 1 y la 2).

**Qué deberíais ver.** Un `registro.csv` con al menos 3 filas (*baseline*, primer modelo y alguna prueba más) y las doce columnas rellenas; el cuaderno ejecutándose de arriba abajo con **las mismas cifras en dos ejecuciones seguidas** (señal de que la semilla funciona); y el *baseline* con la métrica más baja o igual al azar (AUC 0,5 en clasificación).

**Hecho cuando:** hay semilla, versiones, partición común, plan escrito y el registro tiene el *baseline* y al menos un modelo más.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'experimento' is not defined` | La celda donde se define no se ha ejecutado, o Colab se reinició. | Ejecutad desde la primera celda hacia abajo (*Entorno de ejecución → Ejecutar todo*). |
| `FileNotFoundError: [Errno 2] No such file or directory: 'mis_datos.csv'` | El archivo no está subido en esta sesión de Colab, o `RUTA` no coincide. | Subidlo otra vez con el panel 📁 y copiad el nombre exacto. Los archivos subidos se pierden cuando Colab se reinicia. |
| `KeyError: "['cancelado'] not found in axis"` (con otros nombres) | Un nombre de `OBJETIVO` o de `QUITAR` no es exacto. | Escribid `df.columns` y copiad los nombres tal cual. |
| `ValueError: All the 5 fits failed.` y, más abajo, `Input X contains NaN` | Hay casillas vacías en columnas numéricas y el modelo no las admite. | Rellenadlas o quitad esas filas dentro de la cadena de pasos (un imputador en el `Pipeline`) o probad `HistGradientBoostingClassifier`, que las acepta. |
| `ValueError: The least populated classes in y have only 1 member, which is too few` | Una clase tiene una sola fila y `stratify` no puede repartirla. | Quitad `stratify=y` o agrupad esa clase con otra, y apuntadlo en las notas. |
| El registro tiene filas repetidas o empieza en un `id` raro | Se ejecutó una celda de `experimento` varias veces sin reiniciar. | *Reiniciar y ejecutar todo*: el registro se rehace desde cero. |
| Cada vez que ejecutáis salen cifras distintas | Falta fijar la semilla en algún paso. | Comprobad que `SEMILLA` se usa en `train_test_split`, `cv` y los modelos (`random_state=SEMILLA`). |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_15.md) · [Paso 2 →](Reto_Sprint_15_paso_2.md)
<!--/nav-->
