# Paso 2 · Datos y modelos (día 2, 50 minutos, y día 3, 30 minutos)

<!--nav-->
> Sprint 12 · Reto «Escuchar al cliente» · paso 2 de 4 · [Ficha del reto](Reto_Sprint_12.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_12_una_pagina.md) · [Paso 3 →](Reto_Sprint_12_paso_3.md)
<!--/nav-->

1. Día 2, en paralelo: la parte A (reseñas) y la parte C (asistente), unos 25 minutos cada una.
2. Día 3: la parte B (ocupación), 30 minutos.
3. Cada parte se hace en un cuaderno propio, copia del de la práctica, y acaba con un resultado que se pueda contar.
4. Las cifras de los informes salen siempre del código, nunca de la memoria.

**En sencillo.** Un cuaderno de Colab es una hoja con cajas: unas de texto (se leen) y otras de código (se ejecutan una a una). Aquí hacéis tres cuadernos, uno por parte: A cuenta **qué opinan** los huéspedes (el ordenador lee 1.500 reseñas y las clasifica en positivas, neutras y negativas), C construye un **asistente que busca la respuesta en la política del alojamiento** y cita de dónde la saca, y B **prevé la ocupación** de la semana siguiente y comprueba si el modelo gana a un método muy simple. No hace falta saber programar ni entender las matemáticas de los modelos: casi todo el código ya está en los cuadernos de la práctica y aquí tenéis, línea a línea, las pocas piezas que hay que escribir. Es como una receta: los ingredientes (los datos) están en la despensa y vosotros seguís el orden y probáis el plato (comprobáis que la cifra sale) antes de servirlo.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Celda** | Cada caja del cuaderno. Las de código se ejecutan con el botón ▶ (o con `Mayús + Intro`). |
| **Variable** | Un nombre al que se guarda un valor para usarlo después. `acc_lr = …` guarda lo que haya a la derecha con el nombre `acc_lr`. |
| **DataFrame** | La tabla de `pandas` dentro de Python: filas, columnas con nombre y valores. Aquí, `resenas`. |
| **Función** (`def`) | Una receta con nombre: se escribe una vez (`def limpiar(texto):`) y se usa las veces que haga falta (`limpiar("¡Qué BUENO!")`). |
| **Entrenamiento y prueba** | Se reparten los datos en dos montones: con uno el modelo aprende (entrenamiento) y con el otro se le examina (prueba), sin que lo haya visto antes. |
| **Exactitud** | El porcentaje de aciertos en prueba. Un 0,99 son 99 aciertos de cada 100 reseñas. |
| ***Baseline*** | El método más simple que se puede usar. Es el rival a batir: un modelo complicado solo vale la pena si lo mejora. |
| **MAE** | Error absoluto medio: cuántos puntos de ocupación se equivoca de media la previsión. Cuanto más bajo, mejor. |
| **Umbral** | La puntuación mínima para que el asistente se atreva a responder. Si no llega, dice «No consta…». |

**Cómo se hace**

1. **Abrir una copia del cuaderno de cada parte.** Parte A: [`S12_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_03_nlp_clasico.ipynb). Parte C: [`S12_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_06_mini_rag.ipynb). Parte B: [`S12_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_01_series_temporales.ipynb) (o [`S12_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_02_redes_recurrentes.ipynb) si usáis una red). Mejor, la versión que ya hicisteis en clase. En cada uno: *Archivo → Guardar una copia en Drive* y cambiad el nombre (pulsad el título, arriba a la izquierda) a `resenas`, `asistente_rag` u `ocupacion`.
2. **Ejecutar las dos primeras celdas de código, por orden.** La primera («Preparación») crea la función `dato(…)`, que localiza y **descarga sola** el fichero de datos: no hace falta subir nada al panel izquierdo (solo si trabajáis sin internet: subidlo a una carpeta llamada `datos`). La segunda trae las librerías y carga los datos.
3. **Trabajar de arriba abajo, celda a celda.** Pulsad ▶ en cada una, **por orden**. Si Colab se reinicia, se olvida de todo: ejecutad otra vez desde la primera. Las celdas con `# TODO` y `...` son los ejercicios: **borrad solo los `...`** y escribid el código. No toquéis las líneas `assert`: son el punto de control y su mensaje de error dice qué falta.
4. **Dejar el cuaderno limpio.** En el paso 4 lo ejecutaréis entero con *Reiniciar sesión y ejecutar todo*, que se detiene en la primera celda que da error. Los ejercicios que el reto no usa (se dice en cada parte) o los completáis o los borráis con la papelera que aparece al pasar el ratón por la celda.

## 2.1 · Parte A · Reseñas (día 2, unos 25 minutos)

**Recibe y devuelve.** `resenas.csv` (1.500 reseñas; columnas `id_resena`, `texto`, `nota`, `sentimiento` y `temas`) → el reparto del sentimiento, la exactitud de un clasificador en prueba, los temas más mencionados, `grafico_resenas.png` y citas reales. Cuaderno: copia de `S12_03`, guardada como `resenas`. Los ejercicios 2, 4 y 5 y el mini-reto del cuaderno no hacen falta.

**Cómo se hace**

1. **Limpiar el texto.** Para el ordenador «Bueno», «bueno!» y «BUENO» son tres palabras distintas. La función `limpiar` las unifica. En la celda del Ejercicio 1 (sección 2) borrad los `...` y escribid:

    ```python
    def limpiar(texto):
        texto = texto.lower()
        texto = re.sub(r"[^a-záéíóúüñ\s]", " ", texto)
        return " ".join(texto.split())
    ```

    Qué hace cada línea:

    - `def limpiar(texto):` crea la función. `texto` es lo que le damos para limpiar. **El nombre `limpiar` no se puede cambiar**: lo usan las celdas siguientes.
    - `texto.lower()`: pasa todo a minúsculas.
    - `re.sub(patrón, " ", texto)`: cambia por un espacio todo lo que cumple el patrón. `[^a-záéíóúüñ\s]` significa «cualquier carácter que **no** sea una letra (con tildes y `ñ`) o un espacio»: así desaparecen signos, números y símbolos. `re` ya está importada.
    - `" ".join(texto.split())`: `split()` rompe el texto en palabras y `join` las pega con un solo espacio, así que se acaban los espacios dobles.
    - `return`: lo que la función devuelve. Fijaos en que **no quita la palabra «no»**: cambia el sentido de la frase.

    La celda siguiente del cuaderno ya aplica la función a todas las reseñas (`resenas["limpio"] = resenas["texto"].apply(limpiar)`). Para verlo, en una celda nueva: `for t in resenas["limpio"].head(3): print("-", t)`. Deberíais ver tres líneas en minúsculas y sin signos, la primera: `- escapada de fin de semana la música del bar no nos dejó dormir vistas al mar increíbles estancia normal sin más`.

2. **Calcular el reparto del sentimiento y dibujarlo.** En una celda nueva:

    ```python
    porcentajes = (resenas["sentimiento"].value_counts(normalize=True) * 100).round(1)
    porcentajes = porcentajes.reindex(["positivo", "neutro", "negativo"])
    print(porcentajes)
    print("Suma:", porcentajes.sum())

    fig, ax = plt.subplots(figsize=(6, 3.5))
    porcentajes.plot.bar(ax=ax, color=["tab:green", "tab:gray", "tab:red"], rot=0)
    ax.bar_label(ax.containers[0], fmt="%.1f %%", padding=3)
    ax.set_ylim(0, 60)
    ax.set_title(f"El {porcentajes['positivo']:.0f} % de las reseñas es positivo y el {porcentajes['negativo']:.0f} % negativo")
    ax.set_xlabel("Sentimiento de la reseña")
    ax.set_ylabel("Reseñas (%)")
    plt.tight_layout()
    plt.savefig("grafico_resenas.png", dpi=150)
    plt.show()
    ```

    Qué hace cada línea:

    - `value_counts(normalize=True)`: cuenta cuántas reseñas hay de cada sentimiento y lo da como proporción (de 0 a 1). `* 100` lo pasa a porcentaje y `.round(1)` deja un decimal.
    - `.reindex([...])`: pone las filas en el orden que queremos (positivo, neutro, negativo).
    - `plt.subplots(figsize=(6, 3.5))`: crea el lienzo (`fig`) y el gráfico (`ax`); `figsize` es el tamaño.
    - `porcentajes.plot.bar(...)`: dibuja una barra por sentimiento; `color` elige el color de cada una y `rot=0` deja las etiquetas rectas.
    - `ax.bar_label(...)`: escribe el valor encima de cada barra.
    - `ax.set_ylim(0, 60)`: el eje vertical **empieza en 0**, para que las barras sean honestas.
    - `ax.set_title(f"…")`: la `f` delante de las comillas permite meter números calculados entre llaves `{…}`; `:.0f` los redondea a 0 decimales. El título dice una conclusión con cifras que salen del código.
    - `set_xlabel` y `set_ylabel`: nombres de los ejes.
    - `plt.savefig("grafico_resenas.png", dpi=150)`: guarda el gráfico como imagen. Va **antes** de `plt.show()`, para que el archivo se guarde con el gráfico dibujado. El nombre tiene que ser ese: lo enlaza el informe.

    Deberíais ver: `positivo 46.9`, `neutro 21.2`, `negativo 31.9`, `Suma: 100.0` y un gráfico de tres barras (verde, gris y roja) titulado «El 47 % de las reseñas es positivo y el 32 % negativo». En el panel de archivos de Colab (icono de la carpeta 📁; si no aparece, pulsad el icono de refrescar) está ya `grafico_resenas.png`.

3. **Entrenar el clasificador y medirlo en prueba.** Ejecutad la celda que reparte las reseñas (sección 4: debe decir `1125 para entrenar, 375 para probar`). En la celda del Ejercicio 3 borrad los `...` y escribid:

    ```python
    modelo_lr = make_pipeline(TfidfVectorizer(preprocessor=limpiar), LogisticRegression(max_iter=1000)).fit(X_ent, y_ent)
    acc_lr = accuracy_score(y_test, modelo_lr.predict(X_test))
    modelo_nb = make_pipeline(CountVectorizer(preprocessor=limpiar), MultinomialNB()).fit(X_ent, y_ent)
    acc_nb = accuracy_score(y_test, modelo_nb.predict(X_test))
    ```

    Qué hace cada línea:

    - La celda anterior ya partió los datos con `train_test_split`: `X_ent` y `y_ent` (el 75 %, para entrenar) y `X_test` y `y_test` (el 25 %, para probar). `X` es el texto de la reseña e `y` la respuesta correcta (el sentimiento). El reparto es **antes** de vectorizar: la prueba no se toca hasta medir.
    - `make_pipeline(A, B)`: encadena dos pasos. `TfidfVectorizer(preprocessor=limpiar)` convierte cada texto en números (las palabras que distinguen una reseña pesan más) usando vuestra `limpiar`; `LogisticRegression(max_iter=1000)` es el clasificador que aprende qué palabras llevan a cada sentimiento.
    - `.fit(X_ent, y_ent)`: entrena **solo con el entrenamiento**. Así el vectorizador tampoco ve la prueba (esto evita la «fuga de datos»).
    - `modelo_lr.predict(X_test)`: las predicciones sobre reseñas que el modelo no ha visto. `accuracy_score(real, predicho)` calcula la exactitud.
    - Las dos últimas líneas hacen lo mismo con otro método (Naive Bayes). Los nombres `modelo_lr`, `acc_lr`, `modelo_nb` y `acc_nb` **no se pueden cambiar**: el `assert` y las celdas siguientes los usan.

    Deberíais ver `Regresión logística + TF-IDF : 0.992`, `Naive Bayes + bolsa de palabras: 0.989` y, debajo, que un clasificador que siempre dijera la clase más frecuente acertaría `0.469`. Contra ese 0,469 hay que leer el 0,992.

4. **Ver dónde se equivoca.** Ejecutad la celda siguiente (`classification_report` y matriz de confusión) y la de la sección 5 («Los límites: negaciones»). Sin escribir nada, deberíais ver: una tabla con `accuracy 0.99` sobre 375 reseñas y una matriz de 3 × 3 cuyas filas son `[120, 0, 0]`, `[3, 76, 0]` y `[0, 0, 176]` (en el orden negativo, neutro, positivo). Es decir, **3 errores**: reseñas neutras que el modelo toma por negativas. En la sección 5, `La limpieza no es impecable` sale como `positivo`: **el modelo no entiende la negación**. Guardad esa frase: es un límite para el informe.
5. **Contar los temas.** Ejecutad la celda de la sección 6 («Temas por palabras clave»): crea `resenas["temas_reales"]` (la lista de temas de cada reseña, sacada de la columna `temas`) y `temas_detectados` (los que encuentra un buscador de palabras clave). En una celda nueva:

    ```python
    negativas = resenas[resenas["sentimiento"] == "negativo"]
    positivas = resenas[resenas["sentimiento"] == "positivo"]
    tabla_temas = pd.DataFrame({
        "negativas": negativas["temas_reales"].explode().value_counts(),
        "positivas": positivas["temas_reales"].explode().value_counts(),
    }).sort_values("negativas", ascending=False)
    print(len(negativas), "críticas y", len(positivas), "elogios")
    print(tabla_temas)
    print((tabla_temas / [len(negativas), len(positivas)] * 100).round(0))
    ```

    Qué hace cada línea:

    - `resenas[resenas["sentimiento"] == "negativo"]`: se queda solo con las filas cuyo sentimiento es negativo. `==` compara; no confundir con `=`, que guarda.
    - `["temas_reales"].explode()`: cada reseña trae una lista de temas (por ejemplo `["ruido", "precio"]`); `explode` la separa en una fila por tema. `.value_counts()` cuenta cuántas veces sale cada uno.
    - `pd.DataFrame({...})`: junta las dos cuentas en una tabla con dos columnas. `.sort_values("negativas", ascending=False)` ordena de más a menos críticas.
    - La última línea divide cada columna entre el total de su sentimiento (478 y 704) para tener porcentajes.

    Deberíais ver `478 críticas y 704 elogios` y esta tabla: limpieza 171 · 249, precio 165 · 243, desayuno 162 · 237, ubicacion 160 · 244, ruido 155 · 244 y personal 147 · 218. En porcentajes, los seis temas salen entre el 31 % y el 36 % **tanto en críticas como en elogios**: ninguno destaca claramente. Decidlo así en el informe (el que más se menciona en las críticas es la limpieza, pero solo por 6 reseñas sobre el precio) y no inventéis una diferencia que no hay. Si en el mini-reto del cuaderno os salió «ruido» como queja principal (201 críticas), es el buscador de palabras clave: marca «ruido» en 46 críticas en las que la etiqueta del corpus no lo marca (155). Para el informe usad las etiquetas y contad esa diferencia como límite.

6. **Elegir las citas reales.** En una celda nueva (el tema, `limpieza`, el más mencionado en las críticas):

    ```python
    citas = resenas[(resenas["sentimiento"] == "negativo") & resenas["temas"].str.contains("limpieza", na=False)]
    print(len(citas), "críticas mencionan limpieza")
    for _, fila in citas.head(3).iterrows():
        print(fila["id_resena"], "·", fila["texto"])
    ```

    Qué hace cada línea:

    - `&` significa «y a la vez»: crítica **y** con el tema limpieza. Cada condición va entre paréntesis.
    - `.str.contains("limpieza", na=False)`: busca la palabra dentro del texto de la columna `temas`. **`na=False` es imprescindible**: 92 reseñas no tienen ningún tema (la celda está vacía) y sin él da error.
    - `citas.head(3).iterrows()`: recorre las tres primeras filas; `_` es el número de fila, que no usamos, y `fila` la reseña.

    Deberíais ver `171 críticas mencionan limpieza` y tres reseñas: la 13 («Viajamos en familia. La limpieza deja mucho que desear...»), la 17 y la 20. Copiad las citas **tal cual** y con su `id_resena`.

**Hecho cuando (parte A):** existe `grafico_resenas.png`, tenéis los porcentajes, la exactitud en prueba (0,992) y su matriz, la tabla de temas y 3 citas con su `id_resena`.

## 2.2 · Parte C · Asistente con RAG (día 2, unos 25 minutos)

**Recibe y devuelve.** Una pregunta → una respuesta que **cita el fragmento de la política** del que sale, o la frase «No consta en la política del alojamiento.» si el parecido es demasiado bajo. Cuaderno: copia de `S12_06`, guardada como `asistente_rag`. RAG significa buscar primero y responder después: como un bibliotecario que localiza la página antes de contestar y te dice de qué página la sacó. Un **fragmento** es una frase de la política con el título de su sección. Con el simulador que trae el cuaderno no hace falta internet ni ninguna clave.

**Cómo se hace**

1. **Cargar la política.** Ejecutad las dos primeras celdas. Deberíais ver `352 palabras en la política | 20 preguntas de referencia` y el principio del documento.
2. **Trocear la política.** En la celda del Ejercicio 1 (sección 2) borrad los `...` y escribid:

    ```python
    def trocear(texto):
        fragmentos, seccion = [], None
        for linea in texto.splitlines():
            linea = linea.strip().replace("**", "")
            if not linea or linea.startswith("# "):
                continue
            if linea.startswith("## "):
                seccion = linea[3:]
                continue
            for frase in re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ])", linea):
                if frase.strip():
                    fragmentos.append({"seccion": seccion, "texto": frase.strip()})
        return fragmentos
    ```

    Qué hace cada línea:

    - `fragmentos, seccion = [], None`: empieza con una lista vacía (`[]`, donde se irán guardando los fragmentos) y sin sección (`None` es «todavía nada»).
    - `for linea in texto.splitlines():` repite lo de dentro **para cada línea** del documento. Lo que queda sangrado (con espacios a la izquierda) es lo que se repite.
    - `linea.strip().replace("**", "")`: quita espacios sobrantes y los asteriscos del formato en negrita.
    - `if not linea or linea.startswith("# "): continue`: si la línea está vacía o es el título del documento, salta a la siguiente.
    - `if linea.startswith("## "): seccion = linea[3:]`: las líneas que empiezan por `## ` son títulos de sección; guarda el título (sin esos tres primeros caracteres) y sigue.
    - `re.split(...)`: parte la línea en frases cortando en cada punto seguido de mayúscula. `fragmentos.append({...})` añade a la lista un diccionario con dos datos: `"seccion"` y `"texto"`. **Esas dos claves no se pueden cambiar**: el `assert` las comprueba.
    - `return fragmentos`: devuelve la lista entera.

    Deberíais ver `25 fragmentos. Ejemplo: {'seccion': '1. Reservas y cancelaciones', 'texto': 'Si el cliente ha pagado un depósito parcial, se devuelve íntegro en las cancelaciones gratuitas.'}`.

3. **Recuperar el fragmento más parecido.** Ejecutad la celda de la sección 3 (convierte cada fragmento en números con TF-IDF y dice `Matriz TF-IDF: (25, 136)`: 25 fragmentos y 136 «raíces» de palabras). Después, en la celda del Ejercicio 2, borrad los `...` y escribid:

    ```python
    def recuperar(pregunta, k=3):
        sim = cosine_similarity(vectorizador.transform([pregunta]), matriz)[0]
        orden = np.argsort(sim)[::-1][:k]
        return [(float(sim[i]), fragmentos[i]) for i in orden]
    ```

    Qué hace cada línea:

    - `vectorizador.transform([pregunta])`: convierte la pregunta en números con el mismo método que los fragmentos. `cosine_similarity(…, matriz)` da una puntuación de parecido de 0 (nada) a 1 (idéntico) con cada fragmento.
    - `np.argsort(sim)[::-1][:k]`: `argsort` da las posiciones ordenadas de menor a mayor; `[::-1]` le da la vuelta (mayor primero) y `[:k]` se queda con las `k` primeras (3 por defecto).
    - `return [...]`: devuelve una lista de pares `(puntuación, fragmento)`.

    Para probarla, escribid en una celda `for p, f in recuperar("¿Hasta cuándo puedo cancelar gratis?", 3): print(f"{p:.2f} | {f['seccion']} | {f['texto']}")`. Primera línea: `0.51 | 1. Reservas y cancelaciones | Las reservas con tarifa flexible se pueden cancelar gratis hasta 48 horas antes de la llegada.` Después ejecutad la celda de la sección 4: `Fragmento correcto en 1.ª posición: 84% | entre los 3 primeros: 89%`, y la lista de tres preguntas que fallan por vocabulario («dejar la habitación» frente a «salida», «bebés» frente a «niños», y «el desayuno», que se confunde con la media pensión).

4. **Arreglar el vocabulario con sinónimos (Ejercicio 3).** En su celda borrad los `...` de `expandir` y escribid:

    ```python
    def expandir(pregunta):
        base = quitar_tildes(pregunta)
        extras = [v for k, v in SINONIMOS.items() if k in base]
        return pregunta + " " + " ".join(extras) if extras else pregunta
    ```

    Qué hace cada línea:

    - `base = quitar_tildes(pregunta)`: la pregunta en minúsculas y sin tildes, para poder compararla con las claves.
    - `SINONIMOS` (ya escrito en la celda) es un diccionario «lo que dice el cliente → lo que dice la política». `extras = [...]` recoge el valor de cada clave que aparece en la pregunta.
    - `return pregunta + " " + " ".join(extras) if extras else pregunta`: si hay sinónimos, los añade al final de la pregunta; si no, la devuelve igual.

    Deberíais ver `Con expansión → 1.ª posición: 95% (antes 84%) | entre los 3 primeros: 100%`. Los números del paso 3 suponen este ejercicio hecho.

5. **Montar el prompt y el generador.** Ejecutad las celdas de la sección 5 (`PLANTILLA`, `construir_prompt` y `generar_simulado`). Deberíais ver el *prompt* de «¿Admiten perros?»: las reglas, el contexto con los fragmentos numerados `[1]`, `[2]` y la pregunta. El **simulador** no es un modelo de lenguaje: devuelve el primer fragmento recuperado, con su cita. Sirve para probar todo el sistema sin internet. Las dos celdas «OPCIONAL» (Ollama y API) podéis saltarlas: el docente no las ha verificado y nunca se escribe una clave en el cuaderno.
6. **Responder, o callar.** En la celda del Ejercicio 4 (sección 6) borrad los `...` y escribid:

    ```python
    def responder(pregunta, umbral=0.15, k=3):
        recuperados = recuperar(pregunta, k)
        mejor = recuperados[0][0]
        if mejor < umbral:
            return {"respuesta": FRASE_NO_CONSTA, "fragmentos": [], "puntuacion": mejor}
        respuesta = generar(construir_prompt(pregunta, recuperados))
        return {"respuesta": respuesta, "fragmentos": [f for _, f in recuperados], "puntuacion": mejor}
    ```

    Qué hace cada línea:

    - `recuperados[0][0]` es la puntuación del primer fragmento, el más parecido: `mejor`.
    - `if mejor < umbral:` si no llega al **umbral** (0,15 por defecto), no se llama al generador: la respuesta es `FRASE_NO_CONSTA`. Así el asistente no inventa.
    - Si llega, `construir_prompt` monta el texto con los fragmentos y `generar` lo contesta, citando `[1]`.
    - Devuelve un diccionario con las tres claves `respuesta`, `fragmentos` y `puntuacion`, que **no se pueden cambiar** (los `assert` y la evaluación del paso 3 las leen).

    Deberíais ver, para «¿Hasta cuándo puedo cancelar gratis?», `Las reservas con tarifa flexible se pueden cancelar gratis hasta 48 horas antes de la llegada. [1] (Fuente: 1. Reservas y cancelaciones)` con puntuación 0.51, y para «¿Tienen gimnasio?» (que la política no menciona), `No consta en la política del alojamiento.` con puntuación 0.0.

**Hecho cuando (parte C):** `responder` cita la fuente con un número (`[1]`) y la pregunta del gimnasio devuelve «No consta en la política del alojamiento.».

## 2.3 · Parte B · Ocupación (día 3, 30 minutos)

**Recibe y devuelve.** `ocupacion_diaria.csv` (1.096 días, de 2023 a 2025; columnas `fecha`, `ocupacion_pct`, `temperatura_c`, `festivo` y `precio_medio`) → una tabla de MAE con el *baseline* y el modelo, un gráfico de la previsión a 7 días y una frase para el cliente. Cuaderno: copia de `S12_01`, guardada como `ocupacion`. El modelo es **SARIMAX**: una receta estadística que mira lo que pasó los días y semanas anteriores y los festivos para prever los siguientes siete días. Los ejercicios 1, 3 y 4 del cuaderno y su mini-reto no hacen falta; sí el Ejercicio 2.

**Cómo se hace**

1. **Cargar y mirar la serie.** Ejecutad las celdas de preparación y carga (debe salir `(1096, 4)`) y la de la sección 1, que dibuja la ocupación diaria y la media por día de la semana y por mes. Deberíais ver una serie con subidas y bajadas regulares, con el fin de semana más ocupado y septiembre como el mes más bajo.
2. **Partir por fecha, nunca al azar.** Ejecutad la celda de la sección 2. Una serie temporal no se baraja: el modelo no puede ver el futuro. Deberíais ver `Entrenamiento: 2023-01-01 → 2025-10-01 1005` y `Prueba       : 2025-10-02 → 2025-12-31 91`. El entrenamiento termina **antes** de que empiece la prueba: son las últimas 13 semanas.
3. **Calcular el *baseline*.** Ejecutad la celda de la sección 3: prevé cada semana de prueba con los 7 días anteriores («igual que la semana anterior») y mide el MAE en las 13 semanas. Deberíais ver `MAE ingenuo    : 5.95 puntos` y `MAE estacional : 4.46 puntos`: el segundo es vuestro *baseline*. Después, en la celda del Ejercicio 2, borrad los `...` y escribid (la celda del modelo imprime este dato):

    ```python
    def pred_media4(historia, o):
        ultimas = historia.iloc[-28:].values.reshape(4, 7)
        return ultimas.mean(axis=0)
    ```

    Qué hace cada línea: `historia.iloc[-28:]` son las últimas 28 observaciones (4 semanas); `.values.reshape(4, 7)` las coloca en una tabla de 4 filas (semanas) y 7 columnas (días de la semana); `.mean(axis=0)` hace la media de cada columna: la ocupación media de un lunes, de un martes… Devuelve 7 valores, uno por día. Debería salir `MAE media 4 semanas: 4.45`.

4. **Entrenar el modelo.** Ejecutad las dos celdas de la sección 5: la primera ajusta SARIMAX y escribe una tabla larga de coeficientes (no hace falta entenderla); la segunda lo evalúa semana a semana, tarda unos segundos y escribe `MAE SARIMAX: 3.18   (estacional ingenuo: 4.46, media 4 sem.: 4.45)`. No usa la temperatura: no se conoce con antelación y sería **fuga de datos**.
5. **Meter los dos MAE en una tabla y decir si el modelo gana.** En una celda nueva:

    ```python
    tabla_mae = pd.DataFrame({
        "MAE (puntos de ocupación)": {
            "Ingenuo: igual que ayer": mae_ing,
            "Baseline: igual que la semana anterior": mae_est,
            "SARIMAX": mae_sar,
        }
    }).round(2)
    print(tabla_mae)
    mejora_pct = 100 * (mae_est - mae_sar) / mae_est
    print(f"Mejora del modelo sobre el baseline: {mejora_pct:.1f} %")
    ```

    Qué hace cada línea: el diccionario de dentro tiene una entrada por método (nombre → MAE), `pd.DataFrame` lo convierte en tabla y `.round(2)` deja dos decimales. `100 * (baseline - modelo) / baseline` es el porcentaje en que el error baja: **positivo, el modelo gana; negativo, pierde**. Los nombres `mae_ing`, `mae_est` y `mae_sar` los crearon las celdas anteriores: no los cambiéis. Deberíais ver 5.95, 4.46 y 3.18, y `Mejora del modelo sobre el baseline: 28.7 %`. Si en vuestro caso saliera negativo, decidlo con claridad: es un resultado válido y significa que el método simple es la mejor respuesta para el cliente.

6. **Dibujar la previsión y escribir la frase para el cliente.** Dos celdas nuevas. La primera guarda la previsión del *baseline* para los **próximos 7 días** (repite la última semana conocida):

    ```python
    fechas = pd.date_range(serie.index[-1] + pd.Timedelta(days=1), periods=7)
    proxima_semana = pd.Series(serie.iloc[-7:].values, index=fechas, name="ocupacion_pct")
    print(proxima_semana.round(1))
    ```

    La segunda dibuja la previsión a 7 días en las 13 semanas de prueba y escribe la frase:

    ```python
    fig, ax = plt.subplots()
    ax.plot(prueba.index, prueba.values, label="Real", color="black", lw=1.2)
    ax.plot(prueba.index, p_est, label="Baseline: igual que la semana anterior", alpha=0.8)
    ax.plot(prueba.index, p_sar, label="SARIMAX", alpha=0.9)
    ax.set_title(f"SARIMAX se equivoca {mae_sar:.1f} puntos de ocupación; el baseline, {mae_est:.1f}")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Ocupación (%)")
    ax.legend()
    plt.show()
    print(f"El método simple se equivoca de media {mae_est:.1f} puntos de ocupación a 7 días; nuestro modelo, {mae_sar:.1f} ({mejora_pct:.0f} % menos).")
    ```

    Qué hace cada línea: `pd.date_range(…, periods=7)` crea las 7 fechas siguientes a la última de la serie; `serie.iloc[-7:]` son los últimos 7 valores. `p_est` y `p_sar` son las previsiones del baseline y de SARIMAX que dejó la evaluación semanal; `prueba.index` son las 91 fechas de la prueba. `label` es el nombre de cada línea en la leyenda (`ax.legend()`). El título y la última frase meten las cifras con `{…}` para que salgan del código. Deberíais ver siete días, del `2026-01-01` (85.7) al `2026-01-07` (80.6); un gráfico con la línea real en negro y las dos previsiones, y la frase «El método simple se equivoca de media 4.5 puntos de ocupación a 7 días; nuestro modelo, 3.2 (29 % menos).».

    Si la celda `comparativa` de la sección 6 del cuaderno da `NameError: name 'mae_sin_exog' is not defined`, falta el Ejercicio 4: borrad esa celda, la vuestra ya hace su trabajo.

    **Si preferís una red GRU en lugar de SARIMAX.** Copiad `S12_02` en vez de `S12_01`: los pasos 1 a 3 son los mismos (la misma partición por fecha y el mismo *baseline* de 4.46, que ahí se llama `mae_base`). Ejecutad las secciones 4 a 7; la del Ejercicio 3 entrena SimpleRNN, LSTM y GRU, y la 7 escribe la comparación y dibuja la mejor. Deberíais ver más o menos `SimpleRNN 3.79`, `LSTM 3.51`, `GRU 3.28` y `Baseline estacional 4.46` (cambian unas décimas de una ejecución a otra). Para vuestra tabla del paso 5 usad `resultados["GRU"]` donde pone `mae_sar` y `mae_base` donde pone `mae_est`; el gráfico y la frase del paso 6 funcionan igual con esos nombres. Una red no tiene por qué ganar: aquí queda casi empatada con SARIMAX (3.28 frente a 3.18), y la entrega pide que digáis cuál elegís y por qué (precisión, tiempo de ejecución y facilidad para explicarla al cliente).

**Hecho cuando (parte B):** hay una tabla con el MAE del *baseline* y del modelo, el porcentaje de mejora, la previsión de los próximos 7 días del *baseline*, un gráfico y una frase para el cliente.

**Qué deberíais ver.** Los tres cuadernos, cada uno con su resultado final visible:

- Reseñas: el gráfico `grafico_resenas.png`, los porcentajes 46.9 / 21.2 / 31.9, la exactitud 0.992 con su matriz, la tabla de temas y 3 citas.
- Asistente: una respuesta con su fuente `[1]` y la frase «No consta…» para el gimnasio.
- Ocupación: la tabla de MAE (5.95, 4.46 y 3.18), la mejora del 28.7 % y el gráfico de la previsión.

**Hecho cuando:** hay un gráfico y un porcentaje de sentimiento, un asistente que cita y dice «No consta…» a la pregunta del gimnasio, y una tabla de MAE con *baseline* y modelo.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'pd' is not defined` (o `'limpiar'`, `'dato'`, `'fragmentos'`…) | Se saltó una celda o Colab se reinició y olvidó todo. | Ejecutad otra vez desde la primera celda, por orden. |
| `ValueError: Cannot mask with non-boolean array containing NA / NaN values` | `.str.contains(…)` sobre `temas`: 92 reseñas no tienen tema. | Añadid `na=False`: `.str.contains("limpieza", na=False)`. |
| `TypeError: object of type 'NoneType' has no len()` (o `'NoneType' object is not iterable`, `is not subscriptable`) | Dejasteis los `...` en `trocear`, `recuperar` o `responder`: la función no devuelve nada. | Borrad los `...`, escribid el cuerpo y acabad con `return`. |
| `AssertionError: Deberías obtener entre 20 y 40 fragmentos (una frase cada uno).` | `trocear` no parte bien: no separa frases o cuenta los títulos. | Comparad con el código de arriba: `startswith("## ")` y el `re.split`. |
| `NameError: name 'mae_media4' is not defined` en la celda de SARIMAX | No se ha hecho el Ejercicio 2 de `S12_01`. | Escribid `pred_media4` y su cálculo (paso 3 de la parte B) y volved a ejecutar. |
| `NameError: name 'dia_max' is not defined` (o `'amplitud_semanal'`, `'mae_sin_exog'`…) | Una celda de ejercicio sin completar que el reto no usa. | Borradla con la papelera o completadla. *Reiniciar sesión y ejecutar todo* se para en ella. |
| `grafico_resenas.png` no aparece, o sale en blanco | `savefig` va después de `plt.show()` o el panel no se ha refrescado. | Poned `plt.savefig(…)` antes de `plt.show()` y pulsad el icono de refrescar del panel 📁. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_12_paso_1.md) · [Ficha del reto](Reto_Sprint_12.md) · [Paso 3 →](Reto_Sprint_12_paso_3.md)
<!--/nav-->
