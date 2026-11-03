# Paso 3 · Evaluación y análisis de errores (día 2, 20 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 4 →](Reto_Sprint_11_paso_4.md)
<!--/nav-->

1. Evaluar en la prueba (**una sola vez**) y sacar las métricas por clase.
2. Mirar la matriz de confusión y hacer los ejercicios 3 y 4.
3. Elegir las fotos mal clasificadas (3 como mínimo, 6 como estándar) y rellenar la tabla de errores.
4. Buscar patrones entre los errores.

**En sencillo.** Hasta ahora solo habéis mirado la nota de la **validación**, el ensayo. Ahora llega el **examen final**: las 60 fotos de la prueba que el modelo no ha visto nunca. Pero una sola cifra («acierta el 90 %») es como la nota media de una clase: no dice **quién** suspende. Por eso miramos tres cosas: la nota de cada tipo de alojamiento, la **matriz de confusión** (una tabla que cruza «lo que era» con «lo que dijo el modelo») y, sobre todo, **las fotos concretas en las que se equivoca**, con los ojos. Los fallos más peligrosos son aquellos en los que el modelo estaba muy seguro y se equivocó. A veces, además, el que se equivoca no es el modelo, sino la etiqueta de la foto: por eso apuntasteis las dudosas en el paso 1. No hace falta saber matemáticas: dos divisiones y una ordenación.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Prueba** (*test*) | Las 60 fotos reservadas desde el paso 1. Se usan **una sola vez**, para esta nota final; después no se decide nada con ellas. |
| **Exactitud global** (*accuracy*) | De todas las fotos de la prueba, qué fracción acierta el modelo. El cuaderno la llama «Exactitud en prueba». |
| **Precisión de una clase** | De las fotos que el modelo dijo «hotel», cuántas eran de verdad hotel. Baja si el modelo llama «hotel» a cosas que no lo son. |
| ***Recall*** (o exhaustividad) | De las fotos que de verdad eran hotel, cuántas encontró el modelo. Baja si deja hoteles sin reconocer. |
| **F1 macro** | Una nota que mezcla precisión y *recall* de cada clase y hace la media de las clases, de modo que todas pesan igual. |
| **Matriz de confusión** | Una tabla donde cada **fila** es la clase **real** y cada **columna** la clase **predicha**. La diagonal son los aciertos; lo que queda fuera son los errores. |
| **Confianza** | La probabilidad más alta que da el modelo a una foto. Un error con confianza alta es un error «seguro de sí mismo». |
| **Hipótesis de causa** | Una explicación de por qué falló que se **puede ver en la foto** («la piscina es muy pequeña»), no una frase vaga como «faltan datos». |
| **Índice** | La posición de una foto en la lista (la primera es la 0). Con los índices se sacan las fotos concretas. |

**Cómo se hace**

1. **Evaluar en la prueba.** Ejecutad la celda de la sección 3 («Rendimiento en el conjunto de prueba»). Ya está escrita y **no hay que modificarla**. Estas son sus primeras líneas:

    ```python
    prob_pru = modelo.predict(X_pru, verbose=0)
    pred_pru = prob_pru.argmax(axis=1)
    pred_cero = desde_cero.predict(X_pru, verbose=0).argmax(axis=1)
    print(f"Exactitud en prueba → transfer + fine-tuning: {accuracy_score(y_pru, pred_pru):.3f} · desde cero: {accuracy_score(y_pru, pred_cero):.3f}")
    print(f"F1 macro → transfer: {f1_score(y_pru, pred_pru, average='macro'):.3f} · desde cero: {f1_score(y_pru, pred_cero, average='macro'):.3f}")
    print(classification_report(y_pru, pred_pru, target_names=NOMBRES, zero_division=0))

    cm = confusion_matrix(y_pru, pred_pru, labels=range(N_CLASES))
    ```

    Qué hace cada línea:

    - `prob_pru = modelo.predict(X_pru, verbose=0)`: el modelo mira cada foto de la prueba y devuelve 5 probabilidades por foto, una por clase. Es una tabla de 60 filas y 5 columnas.
    - `pred_pru = prob_pru.argmax(axis=1)`: de cada fila, la **posición** de la probabilidad más alta. Es la clase que el modelo elige (un número del 0 al 4).
    - `pred_cero = desde_cero.predict(…).argmax(axis=1)`: lo mismo con el modelo de referencia, para compararlos.
    - Los dos `print(f"…")`: escriben la exactitud global y el F1 macro de los dos modelos, con tres decimales. `y_pru` son las clases reales; `pred_pru`, las predichas.
    - `print(classification_report(…))`: una tabla con una fila por clase y las columnas `precision`, `recall`, `f1-score` y `support` (cuántas fotos de prueba hay de esa clase). Debajo, las filas `accuracy`, `macro avg` y `weighted avg`.
    - `cm = confusion_matrix(…)`: la matriz de confusión, de 5 × 5. Cada fila es una clase real; cada columna, una predicha.

    El resto de la celda dibuja la matriz como cuadrados azules con el número dentro (más oscuro = más fotos). No hace falta tocarlo. **Esta es la única celda que evalúa en la prueba: no la ejecutéis otra vez para retocar el modelo.**

2. **Ejercicio 3: precisión y *recall* de cada clase.** Bajad al enunciado «Ejercicio 3». En su celda hay un `# TODO`, tres puntos `...` y varias líneas con `assert`. Borrad **solo los tres puntos** y escribid:

    ```python
    diag = np.diag(cm).astype(float)
    recall_clase = np.divide(diag, cm.sum(axis=1), out=np.zeros(N_CLASES), where=cm.sum(axis=1) > 0)
    precision_clase = np.divide(diag, cm.sum(axis=0), out=np.zeros(N_CLASES), where=cm.sum(axis=0) > 0)
    clase_mas_dificil = NOMBRES[int(np.argmin(recall_clase))]
    ```

    Qué hace cada línea:

    - `diag = np.diag(cm).astype(float)`: saca la diagonal de la matriz (los aciertos de cada clase, uno por clase) y los pasa a números con decimales.
    - `cm.sum(axis=1)`: la suma de cada **fila**, es decir, cuántas fotos reales hay de cada clase. `cm.sum(axis=0)`: la suma de cada **columna**, es decir, cuántas fotos ha llamado el modelo de cada clase.
    - `recall_clase = np.divide(diag, cm.sum(axis=1), …)`: aciertos entre fotos reales de la clase. Es el *recall*.
    - `precision_clase = np.divide(diag, cm.sum(axis=0), …)`: aciertos entre fotos que el modelo llamó de esa clase. Es la precisión de la clase.
    - `out=np.zeros(N_CLASES), where=… > 0`: es la forma de «si una suma es 0, deja 0» que pide el enunciado. `np.divide` solo divide donde la suma es mayor que 0; en el resto deja el 0 de `out`, y así no hay divisiones entre cero.
    - `clase_mas_dificil = NOMBRES[int(np.argmin(recall_clase))]`: `np.argmin` da la posición del *recall* más bajo, y `NOMBRES[…]` la convierte en el **nombre** de la clase (hay que guardar el nombre, no el número).

    Pulsad ▶. La celda imprime una tabla con una fila por clase y las columnas `recall` y `precisión`, y la línea `Clase más difícil (menor recall): …`. Las cifras de la tabla deben **coincidir** (redondeadas) con las columnas `recall` y `precision` del informe de arriba: es una buena forma de comprobar que lo habéis hecho bien.

3. **Ejercicio 4: ordenar los errores de más a menos confianza.** Bajad al enunciado «Ejercicio 4», borrad los `...` y escribid:

    ```python
    def indices_errores(y_real, prob):
        pred = prob.argmax(axis=1)
        errores = np.where(pred != y_real)[0]
        return errores[np.argsort(-prob.max(axis=1)[errores])]
    ```

    Qué hace cada línea:

    - `def indices_errores(y_real, prob):`: define la función. Recibe las clases reales y la tabla de probabilidades. No olvidéis los dos puntos.
    - `pred = prob.argmax(axis=1)`: la clase elegida para cada foto, como antes.
    - `errores = np.where(pred != y_real)[0]`: `pred != y_real` marca con `True` las fotos donde lo predicho no coincide con lo real; `np.where` da las **posiciones** de esos `True`. Son los índices de las fotos mal clasificadas.
    - `prob.max(axis=1)[errores]`: la confianza (la probabilidad más alta) de cada foto mal clasificada.
    - `np.argsort(-…)`: da el orden que pondría las confianzas de **mayor a menor**. El signo menos delante es lo que invierte el orden (sin él saldrían de menor a mayor).
    - `return errores[…]`: devuelve los índices de los errores en ese orden: primero los más seguros de sí mismos.

    Pulsad ▶. Las comprobaciones de debajo usan números de juguete (por eso no hace falta haber entrenado nada para probarlas).

4. **Ver los errores.** Ejecutad las dos celdas siguientes (ya escritas). La primera escribe `N imágenes mal clasificadas de 60` y dibuja hasta **10** fotos: encima de cada una pone la clase real (`real:`), la predicha (`predicho:`) y entre paréntesis la confianza, y junto a ella, en letra pequeña, el **nombre del archivo**. Las primeras son las de más confianza, las más preocupantes. La segunda, con `value_counts`, cuenta los **pares** más repetidos con el formato `clase real → clase predicha`.

    Para cada foto de la figura mirad con calma y preguntaos: ¿está mal etiquetada y el modelo tiene razón? ¿Tiene mucho grano? ¿Se parece a otra clase (un edificio alto y uno bajo, por ejemplo)? ¿El objeto es muy pequeño? Si la foto aparece en vuestra lista de «etiquetas dudosas» del paso 1, probablemente **no** se ha equivocado el modelo, sino quien etiquetó, y eso también hay que contarlo.

5. **Rellenar la tabla de errores.** Copiad esta tabla en `analisis_errores.md` (lo escribiréis en el paso 5) y añadid **una fila por foto**: 3 como mínimo, 6 para el nivel estándar. *(Si el modelo acierta casi todo y hay menos errores de los que se piden, completad la tabla con las fotos que acertó con **menos confianza**: es un «casi error», se analiza igual y lo ponéis en el informe. Si no hay ningún error, decidlo y analizad las 3 de menos confianza.)* En «Foto» poned la carpeta de la clase real y el nombre del archivo, por ejemplo `camping/img_031.png`:

    | Foto | Verdadera | Predicha | Confianza | Hipótesis de causa | Mejora propuesta |
    |---|---|---|---|---|---|
    | `piscina/img_012.png` (ejemplo inventado) | Piscina | Hotel | 81 % | El edificio ocupa media imagen y la piscina es muy pequeña | Más ejemplos con la piscina en primer plano |

    Una hipótesis vale cuando **se ve en la foto**: «por falta de datos» no basta. Mejoras posibles: más fotos de esa clase, revisar la etiqueta, añadir variaciones de las fotos que ya hay (girarlas, recortarlas), o más ajuste fino. La fila de ejemplo es inventada: no la copiéis.

6. **Interpretar la matriz en una frase.** Mirad qué números hay fuera de la diagonal y escribid, con vuestras cifras: *«La clase [X] es la más difícil (*recall* [..]): [n] de sus fotos se predicen como [Y], posiblemente porque [se parecen / la etiqueta es dudosa]»*. Comprobad también si el modelo con *transfer learning* y el de «desde cero» quedan cerca o lejos en las dos líneas de precisión y F1 macro, y anotadlo.

**Qué deberíais ver.**
- **Dos líneas** con la exactitud y el F1 macro de los dos modelos, y el informe `classification_report` con cinco filas de clases (`apartamentos`, `camping`, `casa_rural`, `hotel`, `piscina`) más las filas `accuracy`, `macro avg` y `weighted avg`.
- **La matriz de confusión:** una cuadrícula de 5 × 5 con números, con la diagonal más oscura. Los dibujos de hotel y apartamentos se parecen (los dos son edificios), así que sería razonable que se mezclen entre sí, pero lo que cuenta es lo que salga en **vuestra** matriz.
- **El ejercicio 3:** una tabla de cinco filas con `recall` y `precisión`, y la clase más difícil.
- **Los errores:** `N imágenes mal clasificadas de 60`, hasta diez fotos con su clase real, predicha y confianza, y la lista de los pares más confundidos. Si N es menor que 3, es una buena noticia, no un fallo: apuntadlo y avisad al docente de que no tenéis fotos suficientes para la tabla.

**Hecho cuando:** tenéis las métricas por clase y la matriz interpretada en una frase, y la tabla con al menos 3 errores (6 si vais al estándar), cada uno con hipótesis y mejora. **A partir de aquí la prueba no se vuelve a usar para decidir nada.**

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'cm' is not defined` (o `'prob_pru'`, `'pred_pru'`) | No se ha ejecutado la celda de la sección 3 que evalúa. | Ejecutadla (y las anteriores, por orden) y repetid el ejercicio. |
| `NameError: name 'recall_clase' is not defined` o `name 'indices_errores' is not defined` | La celda del ejercicio todavía tiene los `...` o no se ha ejecutado. | Borrad los tres puntos, escribid el código y pulsad ▶. |
| `AssertionError: El recall se divide entre la suma de la FILA` | Se ha dividido entre la suma de columnas (`axis=0`) en lugar de la de filas. | El *recall* usa `cm.sum(axis=1)`; la precisión, `cm.sum(axis=0)`. |
| `AssertionError: clase_mas_dificil debe ser el nombre de una clase` | Se ha guardado un número (el resultado de `np.argmin`) y no el nombre. | Envolvedlo con `NOMBRES[int(np.argmin(recall_clase))]`. |
| `AssertionError: Deben ser vectores de una posición por clase` | `recall_clase` o `precision_clase` no tiene 5 valores. | Comprobad que usáis `np.diag(cm)` y las sumas con `axis`, no una suma de toda la matriz. |
| `AssertionError: Los errores son las filas 0 (confianza 0.9) y 2 (0.8); deben salir en ese orden: [0, 2]` | Los errores salen desordenados o de menor a mayor confianza. | Poned el signo menos dentro de `np.argsort(-…)`. |
| `IndentationError: expected an indented block after function definition on line …` | Las líneas de dentro de `indices_errores` no tienen sangría. | Poned 4 espacios delante de cada línea de la función, incluido el `return`. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_11_paso_2.md) · [Ficha del reto](Reto_Sprint_11.md) · [Paso 4 →](Reto_Sprint_11_paso_4.md)
<!--/nav-->
