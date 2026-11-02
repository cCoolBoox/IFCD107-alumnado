# Paso 1 · Evaluar el modelo en el test y buscar dónde falla (día 1, 40 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 1 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 2 →](Reto_Sprint_16_paso_2.md)
<!--/nav-->

1. Evaluar el modelo candidato del Sprint 15 en el test, **una sola vez**, y anotar las métricas con su incertidumbre.
2. Adaptar los gráficos de `S13_02` y guardar todo en `notebooks/04_evaluacion.ipynb`.
3. Calcular la métrica por subgrupos y sacar la lista de los errores más frecuentes.

**En sencillo.** El **test** es el examen final del modelo: datos que apartasteis al principio y que nunca ha visto. Es como el examen de conducir: si lo repetís hasta aprobar, la nota ya no mide nada. Por eso se hace **una vez** y se apunta el resultado, sea el que sea. Pero una nota global no basta: un modelo puede acertar «el 83 %» y fallar mucho más con un grupo (un canal de venta, un país). Ese fallo desigual se llama **sesgo**, y este paso sirve para encontrarlo y para mirar ejemplos reales de errores. No hay que programar de cero: partís de una plantilla que ya funciona (`S13_02`) y cambiáis lo marcado como `# >>> EDITA`. Los códigos de abajo funcionan tal cual con los datos de TurisData: ejecutadlos primero así, para ver qué sale, y después ponedlos con los datos de **vuestro** proyecto.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Test** | Datos apartados desde el principio para el examen final. Se usan una sola vez. |
| **Métrica** | Un número que resume cómo lo hace el modelo. **AUC**: 0,5 es azar y 1 es perfecto. **Recall**: de las cancelaciones reales, cuántas detecta. **Precisión**: de las que avisa, cuántas ocurren de verdad. |
| **Umbral** (`UMBRAL`) | La probabilidad a partir de la cual el modelo «avisa». En `S13_02` vale 0,35. |
| **Falsa alarma / no detectada** | Aviso de cancelación que luego no ocurrió / cancelación que el modelo no vio venir. |
| **Intervalo del 95 %** | El tramo (de A a B) donde probablemente está la cifra real. Se calcula barajando el test 300 veces (*remuestreo* o *bootstrap*). |
| **Subgrupo** | Parte de los datos que se mide por separado: un canal, un país, un tipo de foto… |
| **Sesgo** | Que el modelo funcione peor para un grupo que para otros. |
| **Título-conclusión** | Título de gráfico que dice lo que se ve («En el canal directo detectamos solo el 62 %»), no lo que es («Recall por canal»). |

**Cómo se hace**

1. **Crear el cuaderno (5 minutos).** Abrid [`S13_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_02_plantilla_informe_visual.ipynb) en Colab, *Archivo → Guardar una copia en Drive* y llamadla `04_evaluacion`. Pulsad *Compartir* y añadid al equipo como **Editor**. Una persona escribe y las demás miran; cambiad de turno. Pulsad ▶ **por orden** en las celdas hasta «2. Cálculos que alimentan el panel». Con TurisData sale `AUC en prueba: 0.744 · reservas de prueba: 1500`: así sabéis que funciona.
2. **Poner vuestro modelo (10 minutos).** En «1. Datos y modelo» cambiad solo lo marcado `# >>> EDITA`: leed **vuestros** datos y repetid la **misma partición** del Sprint 15 (copiad la línea `train_test_split` de `03_modelos.ipynb`: misma `random_state`, mismo `test_size`). En vez de entrenar, cargad el modelo guardado:

    ```python
    import joblib
    modelo = joblib.load("modelo_candidato.joblib")
    prob = modelo.predict_proba(X_test)[:, 1]
    ```

    Qué hace cada línea:

    - `joblib.load("modelo_candidato.joblib")`: lee el modelo ya entrenado (con su preprocesado). Poned el nombre de **vuestro** fichero y arrastradlo al panel de archivos de Colab (icono 📁, a la izquierda) desde `sprint-15/` de vuestro repositorio. Si Colab se reinicia, hay que subirlo otra vez.
    - `modelo.predict_proba(X_test)[:, 1]`: la probabilidad de «cancela» de cada reserva del test. **Se llama `prob`**: las celdas siguientes usan ese nombre, y también `X_test`, `y_test`, `pred`, `auc` y `UMBRAL`. No los renombréis.

    Si vuestro proyecto no es una tabla (imágenes, series, asistente), la métrica cambia (F1, MAE, aciertos…), pero la estructura es la misma: una cifra general y la misma cifra por grupo. Consultadlo en la tutoría.

3. **Evaluar en el test, una vez (8 minutos).** En una celda nueva (**+ Código**):

    ```python
    from sklearn.metrics import recall_score, precision_score

    print("Reservas de prueba:", len(y_test))
    print(f"AUC {auc:.3f} · recall {recall_score(y_test, pred):.3f} · precisión {precision_score(y_test, pred):.3f} (umbral {UMBRAL})")

    rng = np.random.default_rng(SEMILLA)
    real = y_test.to_numpy()
    aucs, recalls = [], []
    for _ in range(300):
        idx = rng.integers(0, len(real), len(real))
        if len(np.unique(real[idx])) < 2:
            continue
        aucs.append(roc_auc_score(real[idx], prob[idx]))
        recalls.append(recall_score(real[idx], pred[idx]))
    for nombre, valores in (("AUC", aucs), ("Recall", recalls)):
        inf, sup = np.percentile(valores, [2.5, 97.5])
        print(f"{nombre}: intervalo 95 % entre {inf:.3f} y {sup:.3f}")
    ```

    Qué hace cada parte:

    - Las dos primeras líneas con `print` escriben las tres métricas. `auc` y `pred` (1 si `prob` ≥ `UMBRAL`, 0 si no) ya los calculó la celda «2. Cálculos». La `f` antes de las comillas deja poner variables entre llaves, y `:.3f` las escribe con 3 decimales.
    - El bucle `for` es el remuestreo de `S10_04`: 300 veces elige al azar `len(real)` reservas del test (pueden repetirse) y recalcula la métrica. **No vuelve a pasar el modelo por el test**: usa las mismas predicciones, así que sigue siendo «una sola vez».
    - `if len(np.unique(real[idx])) < 2: continue` salta los barajados con una sola clase, donde el AUC no se puede calcular.
    - `np.percentile(valores, [2.5, 97.5])` se queda con el 95 % central de las 300 cifras: es el intervalo.

    Copiad las cifras a una celda de texto («AUC 0,744, entre 0,719 y 0,767»). No cambiéis el modelo ni `UMBRAL` para mejorarlas.

4. **Gráficos con título-conclusión (7 minutos).** Pulsad ▶ en la celda «3. El panel de una página» (dibuja 4 gráficos) y cambiad los títulos marcados `# >>> EDITA` para que digan lo que muestran **vuestras** cifras. En TurisData: «Detectamos el 83 % de las cancelaciones; avisamos por error al 49 % de quien no cancela»; «Lo que más pesa en una cancelación es la antelación» (la variable líder sale de `importancias.head(6)`); y el del dinero, «Con el modelo perdemos 16,590 € menos en 1500 reservas».
5. **Métrica por subgrupos (8 minutos).** Pegad esta función (se queda en el cuaderno: la usaréis también en el paso 3) y usadla con la columna que queráis. *(Si vuestro proyecto es una serie, imágenes o un asistente con documentos, no uséis esta función: la tabla del apartado 6 del paso 3 dice qué subgrupos medir y cómo.)*

    ```python
    def medir_subgrupos(real, pred, grupo):
        filas = []
        for valor in sorted(set(grupo)):
            quien = grupo == valor
            r, p = real[quien], pred[quien]
            cancelan = int((r == 1).sum())
            detectadas = int(((r == 1) & (p == 1)).sum())
            avisadas = int((p == 1).sum())
            recall = detectadas / cancelan
            precision = detectadas / avisadas if avisadas else float("nan")
            margen = 1.96 * np.sqrt(recall * (1 - recall) / cancelan)
            filas.append({"subgrupo": valor, "reservas": int(quien.sum()), "cancelan": cancelan, "detectadas": detectadas,
                          "recall": round(recall, 3), "±": round(margen, 3), "precisión": round(precision, 3)})
        return pd.DataFrame(filas)

    grupo = X_test["canal"].fillna("sin dato").to_numpy()
    por_canal = medir_subgrupos(real, pred, grupo)
    print(por_canal.to_string(index=False))

    for columna in categoricas:
        tabla = medir_subgrupos(real, pred, X_test[columna].fillna("sin dato").to_numpy())
        peor = tabla.sort_values("recall").iloc[0]
        print(f"{columna}: el peor subgrupo es {peor['subgrupo']} (recall {peor['recall']:.3f}, {peor['cancelan']} cancelaciones)")
    ```

    Qué hace cada parte:

    - `def medir_subgrupos(real, pred, grupo)`: una receta que recibe lo ocurrido (`real`), lo avisado (`pred`) y a qué grupo pertenece cada reserva (`grupo`). Por cada valor del grupo cuenta cuántas reservas cancelan, cuántas detecta y calcula el recall y la precisión.
    - `margen = 1.96 * np.sqrt(…)`: la columna `±`. Es el margen del intervalo del 95 % de una proporción (el de los intervalos de confianza de `S05`): con pocos casos sale grande y avisa de que la cifra es poco fiable.
    - `X_test["canal"].fillna("sin dato")`: elige la columna `canal` y rellena los huecos con «sin dato» (un hueco hace fallar el orden; y **los datos que faltan también son un subgrupo**).
    - `for columna in categoricas`: repite lo mismo con todas las columnas de categorías (`categoricas` la creó `S13_02`) y escribe el peor subgrupo de cada una. Elegid el que tenga **un recall bajo y bastantes casos**.

6. **Gráfico de subgrupos (4 minutos).** Una barra por grupo, con su `±`:

    ```python
    t = por_canal.sort_values("recall")
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.barh(t["subgrupo"], t["recall"], xerr=t["±"], color="tab:blue", capsize=4)
    ax.axvline(recall_score(real, pred), color="gray", linestyle="--", label="Global")
    ax.set_xlabel("Recall: cancelaciones detectadas (± margen)")
    ax.set_title("En el canal directo detectamos solo el 62 % de las cancelaciones")
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.show()
    ```

    `barh` dibuja barras horizontales y `xerr` les pone el `±`; `axvline` traza la línea del recall global. **El título lo escribís vosotros** con vuestro peor subgrupo y sus cifras.

7. **Lista de errores (8 minutos).** Las cancelaciones que el modelo no detectó, de la más segura a la menos:

    ```python
    resultados = X_test.copy()
    resultados["real"] = real
    resultados["pred"] = pred
    resultados["prob"] = prob.round(3)
    no_detectadas = resultados[(resultados["real"] == 1) & (resultados["pred"] == 0)].sort_values("prob")
    print(len(no_detectadas), "cancelaciones no detectadas de", int(real.sum()))
    no_detectadas.head(20)
    ```

    Mirad esas 20 filas una a una y buscad qué tienen en común. Para comprobarlo con números, comparad las no detectadas con **todas** las canceladas (cambiad `canal` y `antelacion_dias` por columnas vuestras):

    ```python
    canceladas = resultados[resultados["real"] == 1]
    comparacion = pd.DataFrame({"no detectadas": no_detectadas["canal"].value_counts(normalize=True),
                                "todas las canceladas": canceladas["canal"].value_counts(normalize=True)}).round(2)
    print(comparacion)
    print("Antelación media (días):", round(no_detectadas["antelacion_dias"].mean(), 1), "frente a", round(canceladas["antelacion_dias"].mean(), 1))
    ```

    `value_counts(normalize=True)` cuenta qué parte de las filas es de cada canal. En una celda de texto, escribid 2–3 frases («fallamos más con…»). De ahí salen las **limitaciones** de la model card y de la memoria.

8. **Tutoría de sesgos y visualización.** En estos 40 minutos cada equipo tiene su franja: llevad el cuaderno abierto, con la tabla por subgrupos y el gráfico.

**Qué deberíais ver.** Con el ejemplo de TurisData:
- `Reservas de prueba: 1500` y `AUC 0.744 · recall 0.828 · precisión 0.589 (umbral 0.35)`.
- Intervalos aproximados: AUC entre 0.719 y 0.767; recall entre 0.799 y 0.854.
- La tabla por canal: `directo`, 125 cancelaciones y solo 77 detectadas (**recall 0.616, ± 0.085**); `web_intermediaria`, 397 y 361 (0.909). El global (0.828) esconde esa diferencia de 21 puntos.
- En el bucle, el peor subgrupo de `pais_origen` es `sin dato` (recall 0.533 con 15 cancelaciones: el `±` sale de 0.252, poca evidencia).
- `118 cancelaciones no detectadas de 688`. Entre ellas pesa el canal `directo` (41 % de las no detectadas frente al 18 % del total de canceladas), y se hicieron con menos antelación (57 días de media frente a 111 en el total de canceladas).

Con vuestros datos, las mismas formas con vuestras cifras: una tabla de métricas con intervalo, 2–4 gráficos con título-conclusión, una tabla por subgrupo y 2–3 frases sobre los errores. Aunque no haya diferencias entre subgrupos, la tabla se entrega.

**Hecho cuando:** `04_evaluacion.ipynb` tiene la evaluación en test (una vez) con su intervalo, los gráficos, la métrica por subgrupos y la lista de errores, y todo el equipo sabe qué subgrupo va peor.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'prob' is not defined` (o `pred`, `auc`, `X_test`, `UMBRAL`) | No se ejecutó alguna celda de `S13_02`, o Colab se reinició. | Pulsad ▶ por orden desde la primera celda hasta «2. Cálculos». |
| `NameError: name 'recall_score' is not defined` | Falta la línea `from sklearn.metrics import recall_score, precision_score`. | Ejecutad la celda del apartado 3 entera, empezando por esa línea. |
| `FileNotFoundError: [Errno 2] No such file or directory: 'modelo_candidato.joblib'` | El fichero del modelo no está en Colab. | Arrastradlo al panel 📁 y escribid su nombre exacto. |
| `KeyError: 'canal'` (con otro nombre) | La columna no se llama así en vuestros datos. | Mirad los nombres con `X_test.columns`. |
| `TypeError: '<' not supported between instances of 'float' and 'str'` | La columna tiene huecos y Python no sabe ordenarlos. | Usad `.fillna("sin dato")`, como en el ejemplo. |
| `ZeroDivisionError: division by zero` | Un subgrupo no tiene ninguna cancelación (ningún caso positivo) y no se puede calcular su recall. | Juntadlo con otro subgrupo parecido, o dejadlo fuera y anotad por qué. |
| Las cifras cambian cada vez que ejecutáis | La partición o el remuestreo no usan semilla fija. | Usad la misma `random_state` que en el Sprint 15 y `np.random.default_rng(SEMILLA)`. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_16.md) · [Paso 2 →](Reto_Sprint_16_paso_2.md)
<!--/nav-->
