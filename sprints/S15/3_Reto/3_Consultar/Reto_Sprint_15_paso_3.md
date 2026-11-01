# Paso 3 · Comprobar que no hay fugas y tutoría (día 2, 60 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 4 →](Reto_Sprint_15_paso_4.md)
<!--/nav-->

1. Contestar la lista de fugas en una celda de texto de `03_modelos.ipynb`.
2. Corregir lo que falle y repetir las pruebas afectadas.
3. Ir a la tutoría técnica de 20 minutos con el docente.

**En sencillo.** Una **fuga de datos** es una trampa involuntaria: el modelo ve una pista que, en la vida real, todavía no existiría. Es como un examen en el que la respuesta está escrita en el enunciado: sacas un 10, pero no has aprendido nada. Por eso, si un resultado parece **demasiado bueno para ser verdad**, hay que sospechar. Hoy contestáis cinco preguntas por escrito, limpiáis el registro y habláis con el docente. No hay que programar mucho: una demostración opcional y tres líneas para revisar el registro.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Fuga de datos** | Usar, sin querer, información del futuro o de la propia respuesta para predecir. |
| **«En el momento de decidir»** | El instante en que se usaría el modelo. Solo vale lo que ya se conoce entonces. |
| **Variable de fuga** | Una columna que solo existe después del suceso (por ejemplo, `reembolso_emitido`, que solo hay si la reserva se canceló). |
| **Duplicados** | Filas que son la misma prueba repetida. |
| **Tutoría técnica** | Una conversación de 20 minutos con el docente para revisar vuestro trabajo. |

**Cómo se hace**

1. **La lista de fugas (20 minutos).** En `03_modelos.ipynb`, añadid una celda de texto (botón **+ Texto**) titulada «Comprobación de fugas» y copiad estas cinco preguntas. Contestad **Sí / No con una frase** a cada una:

    1. ¿Las variables se conocerían **en el momento de decidir**?
    2. ¿El escalado, la imputación y la codificación se aprenden **solo con el entrenamiento** (dentro de un `Pipeline`)?
    3. ¿La partición respeta el **tiempo** o los **grupos**?
    4. ¿Se ha ajustado algo mirando el test? Si sí, hay que rehacer la evaluación.
    5. ¿La métrica es **demasiado buena para ser verdad**? Sospechad.

    Ejemplo de respuestas con los datos de práctica (las vuestras dependen de vuestros datos): «1 · Sí: antelación, noches, canal, depósito… se conocen al reservar; quitamos el identificador y las fechas en bruto. 2 · Sí: usamos `crear_pipeline`, que aprende dentro de cada trozo de la validación cruzada. 3 · No hay series ni fotos del mismo objeto: reparto aleatorio estratificado. 4 · No: `X_test` no se ha usado. 5 · No: un AUC de 0,75 es creíble en este problema».

2. **Ver cómo suena una fuga (5 minutos, recomendable).** Para reconocer una, provocad una a propósito en vuestra sección, con la columna inventada `reembolso_emitido`, que «sabe» la respuesta:

    ```python
    X_fuga = X_ent.copy()
    X_fuga["reembolso_emitido"] = ((y_ent == 1) & (rng.random(len(y_ent)) < 0.9)).astype(int)
    media, desv = experimento("LogisticaConFuga", LogisticRegression(max_iter=2000), {"C": 1.0}, responsable="Ana",
                              notas="ALARMA: AUC sospechosamente alto (fuga: reembolso_emitido)", Xd=X_fuga)
    print(f"AUC con la variable con fuga: {media:.3f}")
    ```

    Qué hace cada línea:

    - `X_fuga` es una copia de las pistas a la que se añade una columna que vale 1 casi siempre que la reserva se canceló: es la respuesta disfrazada de pista.
    - `Xd=X_fuga` le dice a `experimento` que use esa tabla en lugar de `X_ent`. La fila queda en el registro con el nombre `LogisticaConFuga` y la nota `ALARMA`.

    Con los datos de práctica sale aproximadamente `AUC con la variable con fuga: 0.975`, frente a ≈ 0,75 sin ella: **demasiado bueno**. Este modelo **no se puede elegir** (en el paso 4 se excluye por llevar «Fuga» en el nombre); sirve para contar en la *review* **una fuga que detectasteis**.

3. **Si una respuesta falla, corregid y repetid.** Si descubrís una variable que no se conocería al decidir, quitadla de `X` y repetid las pruebas afectadas. **No borréis la celda antigua**: dejadla y añadid en su `notas=` que tenía una fuga (por ejemplo, `notas="tenía fuga: variable X; repetida sin ella"`). Así el registro cuenta lo que pasó, y sirve para la rúbrica.

4. **Tutoría técnica (20 minutos).** El docente indica la franja de cada equipo. Llevad la tabla del registro, que se muestra con:

    ```python
    registro = pd.read_csv(RUTA_REGISTRO)
    registro[["id", "responsable", "modelo", "valor_cv", "desv_cv", "tiempo_s", "notas"]]
    ```

    Contad **qué comparación estáis haciendo** y **qué fuga podría haber**. Anotad las respuestas del docente en una celda de texto («Tutoría»).

5. **Limpiar el registro (15 minutos).** Revisad columnas vacías, filas repetidas y nombres distintos para el mismo modelo:

    ```python
    print(registro.isna().sum())
    print(registro["modelo"].value_counts())
    print("Repetidas:", registro.duplicated(subset=["modelo", "hiperparametros"]).sum())
    ```

    - `isna().sum()` cuenta las casillas vacías por columna: solo `notas` puede tener algunas; las demás deben estar a 0.
    - `value_counts()` cuenta cuántas filas tiene cada nombre de modelo: si veis `RandomForest` y `randomforest`, son el mismo modelo con dos nombres; corregid el nombre en la celda donde lo escribisteis.
    - La última línea cuenta pruebas con el mismo modelo y los mismos ajustes. Con las pruebas de ejemplo sale `Repetidas: 0`; las repeticiones hechas a propósito (persona D) llevan una nota que lo dice y no cuentan como error.

**Qué deberíais ver.** La celda «Comprobación de fugas» con cinco respuestas, un registro sin columnas vacías (salvo `notas`) ni filas repetidas por error y, si ha habido una fuga, una fila anotada que lo explica. Ninguna prueba con un resultado casi perfecto sin explicación.

**Hecho cuando:** la lista está contestada, el registro está limpio y la tutoría ha quedado anotada.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Un modelo da un AUC de 0,97 o más a la primera | Casi seguro, hay una fuga. | Mirad la lista de columnas: ¿alguna solo existe después de la respuesta? Quitadla y repetid. |
| `NameError: name 'rng' is not defined` | No se ejecutó la celda de `fijar_semillas`. | Ejecutad desde la primera celda hacia abajo. |
| El registro tiene dos o tres filas `LogisticaConFuga` | Se ejecutó la celda de la demostración varias veces. | *Reiniciar y ejecutar todo* rehace el registro y deja una sola fila. |
| `value_counts()` muestra `RandomForest` y `randomforest` como dos modelos | El mismo modelo se anotó con dos nombres distintos. | Corregid el nombre en la celda donde lo escribisteis y volved a ejecutar todo. |
| `FileNotFoundError: [Errno 2] No such file or directory: 'registro.csv'` | Se reinició Colab y el archivo no se ha vuelto a crear. | *Reiniciar y ejecutar todo*, que rehace el registro desde cero. |
| No sabéis si una variable es una fuga | Cuesta decidir qué se conoce «al decidir». | Preguntaos: «¿La tendría ya en la mano el día que uso el modelo?». Si no, es fuga: preguntadlo en la tutoría. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_15_paso_2.md) · [Ficha del reto](Reto_Sprint_15.md) · [Paso 4 →](Reto_Sprint_15_paso_4.md)
<!--/nav-->
