# Paso 1 · Elegir el problema y reproducir la referencia (día 2, 15 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 1 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md) · [Paso 2 →](Reto_Sprint_10_paso_2.md)
<!--/nav-->

1. Elegir **un problema**: cancelaciones (`cancelada`) o precio (`precio_noche`).
2. Abrir `S10_04` en Colab, hacer una copia y ejecutarlo celda a celda hasta la partición.
3. Hacer el ejercicio 1 (`evaluar`) y reproducir el modelo de referencia, anotando su métrica y su tiempo.
4. Fijar la partición entrenamiento / validación / prueba y no cambiarla nunca más.

**En sencillo.** TurisData pregunta si una red neuronal es mejor que lo que ya tiene. Para contestar con justicia hay que comparar los dos modelos **con las mismas reglas**, igual que dos candidatos que hacen el mismo examen. En este paso preparáis ese examen: repartís las 6000 reservas en tres montones (uno para estudiar, otro para ensayar y otro para el examen final), escribís la función que pone la nota (`evaluar`) y entrenáis al candidato veterano, un modelo de árboles llamado *boosting*, para tener una nota con la que comparar. La red llegará en el paso siguiente. No hace falta saber programar: casi todo el código ya está escrito y lo único que escribís es una función corta, que tenéis aquí línea a línea. Tampoco hace falta entender cómo funciona por dentro el boosting.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Celda** | Cada caja del cuaderno. Las de texto se leen; las de código se **ejecutan** con el botón ▶ (o con `Mayús + Intro`). |
| **Variable** | Un nombre al que se guarda un valor: `y = …` guarda lo que haya a la derecha con el nombre `y`. |
| **Función** | Una receta con nombre: se escribe una vez con `def` y se usa las veces que haga falta. `evaluar(…)` será la receta que pone la nota a un modelo. |
| **Diccionario** | Una lista de parejas «nombre: valor» entre llaves, por ejemplo `{"AUC": 0.75, "F1": 0.5}`. |
| **Partición** | El reparto de las reservas en tres montones: con el de **entrenamiento** aprende el modelo; con el de **validación** se ensaya y se decide; el de **prueba** es el examen final y se mira **una sola vez**. |
| **Semilla** | Un número que fija el azar para que, al repetir el reparto, salga siempre lo mismo. Aquí, `SEMILLA = 42`. |
| **AUC** | Una nota de 0,5 a 1 que mide si el modelo pone las probabilidades más altas a las reservas que de verdad se cancelan. 0,5 es como tirar una moneda; 1 sería perfecto. |
| **Boosting** | Un modelo de «árboles» de decisión que se corrigen unos a otros. Aquí es la **referencia**: lo que ya funciona y contra lo que se compara la red. |
| **`assert`** | Una línea que comprueba algo y, si no se cumple, para con un `AssertionError` y un mensaje. Es el **punto de control** de cada ejercicio. |

**Cómo se hace**

1. **Elegir el problema.** Elegid **cancelaciones**: es el que el cuaderno trae montado (¿la reserva termina con `cancelada` = 1 o con 0?) y los ejercicios 1 a 4 están pensados para él. El **precio** (`precio_noche`) es otro problema, predecir un número en euros, y queda como ampliación opcional para el final, con la sección 7 del cuaderno. Apuntad en el documento del equipo: «Problema: cancelaciones».
2. **Abrir vuestra copia del cuaderno.** Entrad en el [cuaderno `S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_04_reto_vale_la_pena.ipynb) (se abre en Colab). Arriba, *Archivo → Guardar una copia en Drive*: así trabajáis en una copia vuestra y el original no se toca. Pulsad *Compartir* (arriba a la derecha) y añadid los correos del equipo con permiso de **Editor**. Una persona escribe y las demás miran y opinan; cambiad de turno cada pocos minutos.
3. **Ejecutar las celdas por orden, hasta la partición.** Pulsad ▶ en la celda «Preparación» (**siempre la primera**: crea la función `dato(…)`, que descarga el archivo de datos), después en la de importaciones y semilla (tarda unos segundos porque trae las librerías de redes neuronales) y después en «1. Datos y partición». Sabréis que han terminado porque aparece un ✓ y un número entre corchetes. **Ejecutad celda a celda, sin «Ejecutar todo»**: el cuaderno tiene huecos (`...`) que dan error hasta que los rellenéis, y más adelante hay una celda que usa la prueba y no debe ejecutarse antes de tiempo.

    La celda de la partición ya está escrita. No la modifiquéis; lo importante son estas tres líneas:

    ```python
    X, y = df[num + cat], df["cancelada"].to_numpy()
    X_res, X_pru, y_res, y_pru = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
    X_ent, X_val, y_ent, y_val = train_test_split(X_res, y_res, test_size=0.2, random_state=SEMILLA, stratify=y_res)
    ```

    Qué hace cada línea:

    - `X, y = df[num + cat], df["cancelada"].to_numpy()`: `X` guarda las columnas con los datos de cada reserva (las de las listas `num` y `cat`) e `y`, la respuesta que se quiere adivinar: `cancelada` (1 = se canceló, 0 = no).
    - `X_res, X_pru, y_res, y_pru = train_test_split(…, test_size=0.2, …)`: aparta el 20 % de las reservas como **prueba** (`X_pru`, `y_pru`). Lo que queda se llama `_res` («resto»).
    - `X_ent, X_val, y_ent, y_val = train_test_split(X_res, …, test_size=0.2, …)`: del resto, el 20 % pasa a **validación** y el 80 % a **entrenamiento**. Salen un 64 % (0,8 × 0,8), un 16 % y un 20 %.
    - `random_state=SEMILLA`: hace que el reparto sea siempre el mismo. **No lo cambiéis**: si cambia la partición, los modelos ya no se pueden comparar entre sí.
    - `stratify=y`: reparte de forma que en cada montón quede la misma proporción de reservas canceladas (aproximadamente un 46 % en los tres).

    Las líneas siguientes de la celda (las de `pre`, `A_ent`, `A_val` y `A_pru`) convierten los datos en números listos para la red; las veréis en el paso 2.

4. **Ejercicio 1: la función `evaluar`.** Bajad hasta «2 · Una función para evaluar a todos por igual». La celda tiene una línea `# TODO` (una pista; Python la ignora), tres puntos `...` y varias líneas con `assert`. Borrad **solo los tres puntos** y escribid esto, respetando mayúsculas, comillas, paréntesis y la sangría de 4 espacios:

    ```python
    def evaluar(y_real, prob, umbral=0.5):
        clases = (np.asarray(prob) >= umbral).astype(int)
        return {"AUC": roc_auc_score(y_real, prob),
                "AP": average_precision_score(y_real, prob),
                "F1": f1_score(y_real, clases),
                "precisión": accuracy_score(y_real, clases)}
    ```

    Qué hace cada línea:

    - `def evaluar(y_real, prob, umbral=0.5):`: define la función. Recibe `y_real` (lo que pasó de verdad, 0 o 1), `prob` (la probabilidad de cancelar que da el modelo) y `umbral` (el corte; si no se dice nada, 0,5). **Los dos puntos del final y la sangría de las líneas de debajo son obligatorios.**
    - `clases = (np.asarray(prob) >= umbral).astype(int)`: convierte probabilidades en decisiones: 1 («cancelará») si la probabilidad llega al umbral y 0 si no. `np.asarray` se asegura de que `prob` sea una tabla de NumPy y `.astype(int)` cambia `True`/`False` por 1/0.
    - `return {…}`: devuelve un diccionario con las cuatro notas. **Los nombres de las claves no se pueden cambiar** (`"AUC"`, `"AP"`, `"F1"` y `"precisión"`, con tilde): el `assert` los comprueba.
    - `roc_auc_score(y_real, prob)` y `average_precision_score(y_real, prob)`: el AUC y el AP (otra nota basada en probabilidades). Se calculan con **`prob`**, no con las clases.
    - `f1_score(y_real, clases)` y `accuracy_score(y_real, clases)`: el F1 (equilibra no dejar escapar cancelaciones y no dar falsas alarmas) y la precisión (aciertos entre total). Se calculan con **`clases`**, las decisiones.

    Pulsad ▶. Si no aparece nada, está bien: los `assert` solo hablan cuando algo falla.

5. **Entrenar la referencia (boosting).** Ejecutad la celda «3 · La referencia: boosting de árboles», que ya está escrita. Estas son sus líneas:

    ```python
    t0 = time.time()
    boost = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_depth=4, random_state=SEMILLA)
    boost.fit(A_ent, y_ent)
    t_boost = time.time() - t0
    prob_boost_val, prob_boost_pru = boost.predict_proba(A_val)[:, 1], boost.predict_proba(A_pru)[:, 1]
    print(f"Boosting entrenado en {t_boost:.1f} s · AUC validación = {roc_auc_score(y_val, prob_boost_val):.3f}")
    ```

    Qué hace cada línea:

    - `t0 = time.time()` y `t_boost = time.time() - t0`: miden cuántos segundos tarda en entrenar. **El tiempo forma parte del coste** que le contaréis al cliente.
    - `boost = HistGradientBoostingClassifier(…)`: crea el modelo (200 rondas de árboles, de profundidad máxima 4). `random_state=SEMILLA` fija su azar.
    - `boost.fit(A_ent, y_ent)`: **entrena**: aprende con las reservas de entrenamiento y sus respuestas.
    - `boost.predict_proba(A_val)[:, 1]`: pide la probabilidad de cancelar de cada reserva (`[:, 1]` es la columna del «sí cancela»). Se hace para validación y para prueba, pero **ahora solo se mira la de validación**: la de prueba se guarda para el veredicto del paso 5.
    - `print(f"…")`: escribe el tiempo y el AUC de validación con tres decimales.

6. **Anotar la referencia.** En el documento del equipo, apuntad el AUC de validación y el tiempo del boosting. **No se cambia la referencia para que la red gane.** Si vuestro equipo tiene un campeón del Sprint 8 (XGBoost, LightGBM, Random Forest…) y sabéis ponerlo en lugar del boosting, podéis usarlo; si no, vale el del cuaderno.

**Qué deberíais ver.**
- **La partición:** `(3840, 35) (960, 35) (1200, 35)`. Suman 6000 reservas y cada una son 35 números (9 de las columnas numéricas y 26 de las categorías convertidas en 0 y 1).
- **El ejercicio 1:** la celda no escribe nada. Si algo falla, aparece un `AssertionError` con un mensaje.
- **El boosting:** una línea como `Boosting entrenado en 0.3 s · AUC validación = 0.734`. El tiempo cambia según el ordenador (serán décimas de segundo); el AUC debe salir ≈ 0,73. Un AUC de 0,5 sería lo mismo que tirar una moneda; uno cercano a 1,0 haría sospechar de una fuga de datos (que el modelo hubiera visto la respuesta).

**Hecho cuando:** el cuaderno llega hasta el boosting sin errores, el ejercicio 1 pasa su comprobación y tenéis anotadas la métrica y el tiempo de la referencia.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'dato' is not defined` (o `'np'`, `'train_test_split'`, `'keras'`) | No se ha ejecutado una celda anterior, o Colab se desconectó y se olvidó de todo. | Ejecutad desde la primera celda hacia abajo, una a una, hasta la que falla. |
| `NameError: name 'evaluar' is not defined` | La celda del ejercicio 1 todavía tiene los `...` y no define la función. | Borrad los tres puntos, escribid la función y volved a pulsar ▶. |
| `TypeError: 'NoneType' object is not iterable` | La función no devuelve nada: falta el `return`. | Poned `return {…}` como última línea de la función, con la misma sangría. |
| `IndentationError: expected an indented block…` | Las líneas de dentro de la función no tienen sangría. | Dejad 4 espacios delante de las tres líneas de debajo de `def`. |
| `AssertionError: El diccionario debe tener las claves AUC, AP, F1 y precisión` | Falta una clave o está mal escrita (por ejemplo, `precision` sin tilde). | Copiad los cuatro nombres tal cual: `"AUC"`, `"AP"`, `"F1"`, `"precisión"`. |
| `AssertionError: Revisa: AUC esperado 0.75 y precisión 0.5 en la prueba mínima` | El AUC se ha calculado con las clases (0 y 1) en vez de con las probabilidades, o el umbral no se aplica bien. | AUC y AP con `prob`; F1 y precisión con `clases`. |
| `ValueError: Classification metrics can't handle a mix of binary and continuous targets` | Se ha pasado `prob` (números decimales) a `f1_score` o a `accuracy_score`. | Pasadles `clases`. |
| El AUC de validación sale casi 1,000 | Sospecha de fuga: el modelo ha visto la respuesta. | Comprobad que no habéis tocado las listas `num` y `cat` (la respuesta, `cancelada`, no puede ser una entrada). |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_10.md) · [Paso 2 →](Reto_Sprint_10_paso_2.md)
<!--/nav-->
