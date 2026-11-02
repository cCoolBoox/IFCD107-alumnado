# Paso 5 · Test una sola vez, explicación, revisión y entrega (día 3, 70 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md)
<!--/nav-->

1. Evaluar el candidato en el test, una sola vez.
2. Guardar el modelo con `metadatos.json` y hacer la primera explicación.
3. Revisar con la rúbrica y anotar el resultado.
4. Subir los ficheros a `sprint-15/`.

**En sencillo.** Es el día de la verdad. Hasta ahora el test estaba guardado en un cajón; hoy lo abrís **una sola vez** para ver cómo se portaría el modelo elegido con datos que nunca ha visto. Es como el examen final: no se puede repetir para sacar mejor nota. Después guardáis el modelo en un archivo (para que otra persona lo use sin reentrenarlo), hacéis un primer gráfico de **qué pistas pesan más** en sus decisiones, os revisáis entre vosotros y subís todo. Hay código, pero cada bloque es corto y viene probado.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Test, una sola vez** | Se evalúa el candidato en el test después de elegirlo. Si el resultado no gusta, **no se vuelve a elegir con él**. |
| **`joblib`** | Una herramienta para guardar un modelo entrenado en un archivo (`.joblib`) y volver a abrirlo después. |
| **Metadatos (`metadatos.json`)** | Un archivo de texto con los datos del modelo: qué modelo es, cuándo se entrenó, versiones, resultados y variables. |
| **Importancia por permutación** | Se desordena una variable y se mira cuánto empeora el modelo: cuanto más empeora, más pesa esa variable. |
| **Explicabilidad** | Poder contar qué pistas usa el modelo y por qué decide lo que decide. |
| **Commit** | Cada subida a GitHub con su mensaje y su autor. |

**Cómo se hace**

1. **Test, una vez (10 minutos).** En una celda nueva, con el candidato que elegisteis en el paso 4 (aquí la regresión logística):

    ```python
    candidato = LogisticRegression(max_iter=2000)
    final = crear_pipeline(candidato, X_ent.columns).fit(X_ent, y_ent)
    auc_test = roc_auc_score(y_test, final.predict_proba(X_test)[:, 1])
    print(f"AUC en test: {auc_test:.3f}")
    ```

    Qué hace cada línea:

    - `candidato` es el modelo que elegisteis (**cambiadlo** por el vuestro, con los mismos ajustes que anotasteis en el registro). `crear_pipeline(...).fit(X_ent, y_ent)` lo entrena con **todo** el entrenamiento.
    - `roc_auc_score(y_test, final.predict_proba(X_test)[:, 1])` calcula el AUC en el test (con series, `mean_absolute_error(y_test, final.predict(X_test))`).

    Con los datos de práctica sale `AUC en test: 0.745`, muy cerca del 0,755 de la validación cruzada: es lo esperable. Si el test saliera muy por debajo (más de unas seis centésimas), sospechad sobreajuste o fuga. Copiad el resultado a la justificación. **No cambiéis de candidato después de verlo**: si no os gusta, anotadlo y explicadlo.

2. **Guardar el modelo y los metadatos (10 minutos).**

    ```python
    import joblib
    from datetime import date

    joblib.dump(final, "modelo_candidato.joblib")
    metadatos = {
        "modelo": "RegresionLogistica",
        "entrenado": str(date.today()),
        "semilla": SEMILLA,
        "datos_hash": DATOS_HASH,
        "metrica": METRICA,
        "valor_validacion": round(float(tabla.loc[tabla["modelo"] == "RegresionLogistica", "valor_cv"].iloc[0]), 3),
        "valor_test": round(float(auc_test), 3),
        "variables": list(X_ent.columns),
        "versiones": ENTORNO,
    }
    with open("metadatos.json", "w", encoding="utf8") as f:
        json.dump(metadatos, f, ensure_ascii=False, indent=2)
    print(open("metadatos.json").read())
    ```

    Qué hace cada línea:

    - `joblib.dump(final, ...)` guarda el modelo **entero** (con su escalado y su codificación) en `modelo_candidato.joblib`; con los datos de práctica pesa unos 5 KB.
    - El diccionario `metadatos` recoge versión de las bibliotecas (`ENTORNO`), fecha, semilla, huella de los datos, métrica en validación y en test, y los nombres de las variables. **Cambiad `"RegresionLogistica"` (dos veces) por el nombre de vuestro candidato en el registro.**
    - `json.dump(...)` lo escribe en `metadatos.json` y el último `print` lo enseña.

    Salen las líneas del archivo, con `"valor_validacion": 0.755` y `"valor_test": 0.745` en el ejemplo. En el brief 3, guardad el asistente tal como lo ejecutáis y apuntad en `metadatos.json` el modelo de lenguaje, los parámetros y el modo de recuperar los textos. Si el modelo es una red de Keras, se guarda con el formato de la red (`.keras`).

3. **Primera explicación (20 minutos).** Importancia de variables por permutación, calculada sobre el **entrenamiento** (para no usar el test una segunda vez):

    ```python
    from sklearn.inspection import permutation_importance
    import matplotlib.pyplot as plt

    resultado = permutation_importance(final, X_ent, y_ent, scoring="roc_auc", n_repeats=5, random_state=SEMILLA)
    importancias = pd.Series(resultado.importances_mean, index=X_ent.columns).sort_values(ascending=False)
    print(importancias.head(8).round(3))

    fig, ax = plt.subplots(figsize=(7, 4))
    importancias.head(8)[::-1].plot.barh(ax=ax, color="tab:blue")
    ax.set_xlabel("Caída del AUC al desordenar la variable")
    ax.set_title("Variables que más pesan en el modelo candidato")
    plt.tight_layout()
    plt.savefig("explicacion_modelo.png", dpi=150)
    plt.show()
    ```

    Qué hace cada línea:

    - `permutation_importance` desordena cada variable 5 veces (`n_repeats=5`) y mide cuánto cae el AUC. Con series, `scoring="neg_mean_absolute_error"`.
    - `pd.Series(...).sort_values(...)` ordena las variables de más a menos importante; `head(8)` se queda con las ocho primeras.
    - `plt.savefig("explicacion_modelo.png", dpi=150)` guarda el gráfico (**antes** de `plt.show()`).

    Con los datos de práctica salen, aproximadamente, `antelacion_dias` 0,103, `deposito` 0,059, `canal` 0,042 y `tarifa` 0,037. Escribid **2–3 frases de lectura** en la justificación: «La variable más importante es la antelación, lo que tiene sentido porque, en los datos, se cancela cerca del 28 % de las reservas con 30 días o menos de antelación y el 67 % de las de más de 120 días». El gráfico solo dice qué pistas usa el modelo, **no** que sean la causa. Si los datos son tabulares y queréis ir más allá, se puede usar SHAP, y con imágenes, Grad-CAM; se profundiza en el sprint 16.

4. **La revisión con la rúbrica (10 minutos).** Quien revisa **no escribió** esa parte y sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md): ejecutar `03_modelos.ipynb` de arriba abajo y comparar las cifras con la tabla de la justificación; mirar el registro (*baseline* en la fila 1, columnas rellenas, una fila de cada persona); buscar fugas y trampas; leer la justificación como el cliente y poner un nivel de 1 a 4 en cada criterio **con una frase de prueba**; y anotar el resultado. Añadid al final de `justificacion_candidato.md` una sección como esta:

```
## Revisión con la rúbrica
**Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | | |
| Reproducibilidad | | |
| Análisis y comunicación al cliente | | |
| IA responsable | | |

**Lo primero que mejoraríamos:** <una cosa concreta>
```

5. **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). Descargad del panel 📁 de Colab (clic derecho sobre cada archivo → *Descargar*) `registro.csv`, `modelo_candidato.joblib`, `metadatos.json` y `explicacion_modelo.png`; y el cuaderno con *Archivo → Descargar → Descargar .ipynb*. Después: (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-15`**; (2) *Add file → Upload files*; (3) arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube `03_modelos.ipynb` («Añado cuaderno de modelos»), la B sube `registro.csv` y `explicacion_modelo.png`, la C sube `justificacion_candidato.md`, `modelo_candidato.joblib` y `metadatos.json`. Los nombres de archivo, **en minúsculas y sin espacios**. Cada persona sube además su `autoevaluacion_nombre.md`.

**Qué deberíais ver.** En la carpeta `sprint-15` del repositorio, los seis ficheros del equipo y una hoja de autoevaluación por persona (**6 + N**); y en el historial (el icono del reloj), al menos tres *commits* con nombres distintos.

**Hecho cuando:** el test se ha evaluado una vez, el modelo y su explicación están guardados, la sección «Revisión con la rúbrica» está rellena y todo está en `sprint-15/`.

**Después, 60 minutos de review y retro.** Cada persona sube su autoevaluación y coevaluación a `sprint-15/` (en el tiempo de entrega). En la *review*, cada equipo enseña en 5 minutos: (1) la tabla de modelos con media ± desviación, (2) el candidato elegido y **por qué** (no solo la métrica), (3) una fuga que evitó o detectó, (4) una hipótesis sobre por qué gana ese modelo y (5) su registro de experimentos. El resto de equipos pregunta: *«¿cómo sabéis que la diferencia no es ruido?»*

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'final' is not defined` | La celda del test no se ejecutó antes de guardar o explicar. | Ejecutad desde la primera celda: *Entorno de ejecución → Ejecutar todo*. |
| `TypeError: Object of type int64 is not JSON serializable` (o `float32`) | Hay un número de NumPy dentro de `metadatos` y JSON no sabe escribirlo. | Convertidlo con `float(...)` o `int(...)`, como en el código de arriba. |
| `FileNotFoundError: [Errno 2] No such file or directory: 'modelo_candidato.joblib'` | Se reinició Colab y el archivo guardado se perdió, o el nombre no coincide. | Volved a ejecutar la celda que guarda el modelo y descargad los archivos antes de cerrar. |
| El test sale mucho peor que la validación | Sobreajuste o fuga. | No cambiéis de candidato por verlo: anotad la diferencia en la justificación y explicad la causa probable. |
| `ModuleNotFoundError: No module named 'shap'` | SHAP no está instalado en la sesión. | Usad la importancia por permutación de este paso, que no necesita instalar nada. |
| El navegador no deja subir el modelo | Pesa más de 25 MB. | No lo subáis por el navegador: avisad al docente y dejad escrito en `metadatos.json` cómo volver a generarlo con vuestro cuaderno. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_15_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_15.md)
<!--/nav-->
