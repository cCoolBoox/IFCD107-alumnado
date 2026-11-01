# Paso 4 · Recomendador de experiencias (día 2, 30 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 5 →](Reto_Sprint_09_paso_5.md)
<!--/nav-->

1. Separar valoraciones de entrenamiento y de prueba.
2. Montar al menos dos métodos y evaluarlos con RMSE y precision@3.
3. Programar `recomendar(id_usuario, n)`.
4. Probarla con 3 usuarios.

**En sencillo.** TurisData vende 25 experiencias (excursiones, talleres, deportes) y 300 clientes han puntuado algunas de 1 a 5 estrellas. Recomendar es como un librero que sugiere lecturas. Para saber si es bueno, le **escondéis** una parte de las opiniones (el 20 %) y miráis si las adivina, igual que un examen con preguntas que no ha visto. Probaréis dos libreros: uno que recomienda **lo más valorado por todos** (la estantería de los más vendidos) y otro que mira **qué experiencias gustan a la misma gente** («a quien le gustó el Teide, también le gustó…»). Y los mediréis de dos formas: cuánto se equivocan en la nota y si acierta la lista corta de tres. No hace falta entender las fórmulas: están escritas, y lo importante es saber qué mide cada cosa.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Matriz usuario × experiencia** | Una tabla con un usuario por fila y una experiencia por columna; en cada casilla, la nota que dio. |
| **`NaN`** | Una casilla vacía: ese usuario no ha valorado esa experiencia. Aquí, el 76 % de las casillas están vacías. |
| **Entrenamiento y prueba** | El 80 % de las valoraciones, que usa el recomendador, y el 20 % escondido, con el que se le examina. |
| **Popularidad** | Recomendar a todos lo mejor valorado de media. Es la referencia que hay que batir, y la única opción con un huésped nuevo. |
| **Item-item** | Recomendar mirando qué experiencias son «parecidas» (las puntúa por encima o por debajo de lo normal la misma gente). |
| **RMSE** | «De media, ¿en cuántas estrellas se equivoca?». Cuanto **más bajo**, mejor. |
| **precision@3** | De las 3 experiencias recomendadas, qué fracción le gustó de verdad (4 estrellas o más en la prueba). Cuanto **más alta**, mejor. |
| **Arranque en frío** | Cuando no hay datos de un usuario nuevo y no se puede personalizar. |
| **`-inf`** | «Menos infinito»: un valor tan bajo que esa experiencia nunca saldrá entre las mejores. Sirve para ocultar lo ya valorado. |

**Cómo se hace**

1. **Cargar los datos, esconder el 20 % y montar la matriz.** Nueva celda:

    ```python
    from sklearn.metrics.pairwise import cosine_similarity

    valoraciones = pd.read_csv(dato("valoraciones_experiencias.csv"))
    experiencias = pd.read_csv(dato("experiencias.csv"))

    prueba = valoraciones.sample(frac=0.2, random_state=SEMILLA)
    entrenamiento = valoraciones.drop(prueba.index)

    R = entrenamiento.pivot(index="id_usuario", columns="id_experiencia", values="valoracion")
    R = R.reindex(index=range(1, 301), columns=range(1, 26))
    M = R.notna().values
    media_global = entrenamiento["valoracion"].mean()
    print(valoraciones.shape, experiencias.shape, len(entrenamiento), len(prueba))
    print("Matriz:", R.shape, "· casillas con dato:", f"{M.mean():.0%}")
    ```

    Qué hace cada línea:

    - `from sklearn.metrics.pairwise import cosine_similarity`: trae la herramienta que mide «lo parecidas que son» dos columnas (la usaréis en el método 2).
    - `valoraciones = …` y `experiencias = …`: leen las valoraciones (usuario, experiencia, nota) y el catálogo (nombre, categoría, isla).
    - `prueba = valoraciones.sample(frac=0.2, random_state=SEMILLA)`: **esconde** el 20 % de las valoraciones, elegidas al azar (con la semilla, siempre las mismas). `entrenamiento = valoraciones.drop(prueba.index)` se queda con el resto.
    - `R = entrenamiento.pivot(…)`: construye la matriz usuario × experiencia con **solo** el entrenamiento. `reindex(…)` asegura 300 usuarios (1 a 300) y 25 experiencias (1 a 25).
    - `M = R.notna().values`: una matriz de «sí/no» que marca dónde hay valoración. `media_global` es la nota media de todo el entrenamiento.

    Sale `(2232, 3) (25, 4) 1786 446` y `Matriz: (300, 25) · casillas con dato: 24%`.

2. **Las dos reglas para medir.** Nueva celda:

    ```python
    fila_p = prueba["id_usuario"].values - 1
    col_p = prueba["id_experiencia"].values - 1
    real_p = prueba["valoracion"].values

    def evaluar_rmse(P):
        pred = np.clip(P[fila_p, col_p], 1, 5)
        return float(np.sqrt(np.mean((pred - real_p) ** 2)))

    relevantes = prueba[prueba["valoracion"] >= 4]

    def precision_k(P, k=3):
        aciertos = []
        for u, g in relevantes.groupby("id_usuario"):
            puntuacion = P[u - 1].astype(float).copy()
            puntuacion[M[u - 1]] = -np.inf
            recomendadas = np.argsort(-puntuacion)[:k] + 1
            aciertos.append(len(set(recomendadas) & set(g["id_experiencia"])) / k)
        return float(np.mean(aciertos))

    print("Usuarios evaluables:", relevantes["id_usuario"].nunique())
    ```

    Qué hace cada línea:

    - `fila_p`, `col_p`, `real_p`: dónde están las valoraciones escondidas y qué nota tienen. Se resta 1 porque Python cuenta desde 0.
    - `def evaluar_rmse(P):`: recibe una matriz de notas previstas `P` y devuelve el **RMSE** en las valoraciones escondidas (`np.clip` mantiene la nota entre 1 y 5).
    - `relevantes = …`: las valoraciones escondidas de 4 estrellas o más: «lo que le gusta» a cada usuario.
    - `def precision_k(P, k=3):`: para cada usuario toma su fila de `P`, **oculta lo que ya valoró** con `-np.inf`, se queda con las `k` mejores (`np.argsort` ordena; `+ 1` pasa de posición a número de experiencia) y cuenta qué fracción estaba en lo que le gusta.

    Sale `Usuarios evaluables: 115`. **Copiadlas sin cambiar nada**: son las reglas del examen.

3. **Método 1: popularidad.** Nueva celda:

    ```python
    media_item = R.mean()
    P_pop = np.tile(media_item.values, (300, 1))
    print(f"Popularidad · RMSE = {evaluar_rmse(P_pop):.3f} · precision@3 = {precision_k(P_pop):.3f}")
    top = media_item.sort_values(ascending=False).head(5)
    print(experiencias.set_index("id_experiencia").loc[top.index, "nombre"].to_frame().assign(nota=top.round(2)))
    ```

    Qué hace cada línea:

    - `media_item = R.mean()`: la nota media de cada una de las 25 experiencias, con el entrenamiento.
    - `P_pop = np.tile(media_item.values, (300, 1))`: repite esa lista en 300 filas: **todos los usuarios reciben la misma predicción**.
    - Las dos últimas líneas escriben las 5 experiencias mejor valoradas con su nombre.

    Sale `Popularidad · RMSE = 1.029 · precision@3 = 0.125` y las cinco más valoradas: Parque Timanfaya (4,43), Visita a Garachico (4,21), Observación de cetáceos (3,93), Parapente (3,82) y Astronomía en el Roque (3,77).

4. **Método 2: item-item, y la tabla comparativa.** Nueva celda:

    ```python
    media_item_v = media_item.fillna(media_global).values
    C = np.where(M, R.values - media_item_v[None, :], 0.0)
    S = cosine_similarity(C.T)
    np.fill_diagonal(S, 0)
    P_item = media_item_v[None, :] + (C @ S.T) / (M.astype(float) @ np.abs(S).T + 1e-9)

    metodos = {"Popularidad": P_pop, "Item-item": P_item}
    tabla = pd.DataFrame({
        "RMSE": {n: evaluar_rmse(P) for n, P in metodos.items()},
        "precision@3": {n: precision_k(P) for n, P in metodos.items()},
    }).round(3)
    tabla
    ```

    Qué hace cada línea:

    - `C = …`: para cada casilla con dato, cuánto puntuó el usuario **por encima o por debajo** de la nota media de esa experiencia (0 si no la valoró).
    - `S = cosine_similarity(C.T)`: una tabla 25 × 25 con el parecido entre experiencias (1, van a la par; 0, nada que ver; −1, opuestas). `np.fill_diagonal(S, 0)` evita que una experiencia se ayude a sí misma.
    - `P_item = …`: la nota prevista de cada usuario para cada experiencia: su nota media más lo que ese usuario puntuó en las experiencias parecidas. No hace falta entender la fórmula: es la de `S09_03`.
    - `metodos` y `tabla`: juntan los dos métodos en una tabla con su RMSE y su precision@3.

    Sale esta tabla:

    | | RMSE | precision@3 |
    |---|---|---|
    | Popularidad | 1.029 | 0.125 |
    | Item-item | 0.895 | 0.171 |

    Si en clase hicisteis el método por contenido (`S09_03`, apartado 4), podéis añadir `"Contenido": P_cont` a `metodos`: sale con RMSE 1.066 y precision@3 0.130, **sin mejorar** a la popularidad. Los nombres de las variables son los mismos que en `S09_03`, así que podéis copiar de ahí.

5. **Elegir el método con una frase.** Comparad con prudencia: con solo 115 usuarios evaluables, una diferencia de 0,01 es ruido y no se vende como mejora. Aquí, 0,171 frente a 0,125 en precision@3 y 0,895 frente a 1,029 en RMSE son diferencias claras, aunque la prueba sea pequeña. Escribid en una celda de texto una frase como esta, con **vuestras** cifras: *«Elegimos item-item porque su precision@3 es 0,171 frente a 0,125 de la popularidad y su RMSE es 0,895 frente a 1,029.»*
6. **Programar `recomendar` y probarla.** Nueva celda:

    ```python
    def recomendar(id_usuario, n=3, P=P_item):
        puntuacion = P[id_usuario - 1].astype(float).copy()
        puntuacion[M[id_usuario - 1]] = -np.inf
        ids = np.argsort(-puntuacion)[:n] + 1
        res = experiencias.set_index("id_experiencia").loc[ids, ["nombre", "categoria", "isla"]].copy()
        res["nota_prevista"] = np.clip(P[id_usuario - 1][ids - 1], 1, 5).round(2)
        return res

    for u in (1, 2, 3):
        print("Usuario", u)
        print(recomendar(u))
        vistas = set(np.where(M[u - 1])[0] + 1)
        print("Recomendadas que ya había valorado:", set(recomendar(u).index) & vistas)
    ```

    Qué hace cada línea:

    - `def recomendar(id_usuario, n=3, P=P_item):`: una función con tres entradas: el usuario, cuántas experiencias (3 si no se dice) y la matriz de notas previstas (item-item si no se dice).
    - `puntuacion = P[id_usuario - 1]…` y `puntuacion[M[id_usuario - 1]] = -np.inf`: toma la fila del usuario y pone `-inf` en lo que **ya valoró**, para que no se recomiende.
    - `ids = np.argsort(-puntuacion)[:n] + 1`: ordena de mayor a menor nota prevista y se queda con las `n` primeras.
    - `res = …loc[ids, …]` y `res["nota_prevista"] = …`: busca nombre, categoría e isla en el catálogo y añade la nota prevista.
    - El bucle `for u in (1, 2, 3)` la prueba con tres usuarios y comprueba que ninguna recomendada estaba ya valorada: tiene que salir `set()`, que significa «ninguna».

    Para el usuario 1 sale Parque Timanfaya (4,73), Ruta por Anaga (4,14) y Zoo y jardines (3,87); para el 2, Observación de cetáceos (4,55), Astronomía en el Roque (4,51) y Parapente (3,90); y para el 3, Visita a Garachico (5,00), Ruta del queso majorero (4,17) y Ruta por Anaga (3,99). Son distintas entre sí. Solo existen los usuarios **1 a 300**.

7. **Pensar en el huésped nuevo.** Un huésped que no ha valorado nada no tiene fila en la matriz: es el **arranque en frío**. Aquí lo único posible es la popularidad: enseñarle las mejores de `top` (Parque Timanfaya, Visita a Garachico, Observación de cetáceos). Dejadlo escrito en una celda de texto: irá a la ficha.

**Qué deberíais ver.** La tabla comparativa de los dos métodos (item-item mejor que la popularidad en las dos medidas), la frase de elección y tres listas de tres experiencias, distintas entre sí y sin nada ya valorado. Las cifras pueden variar un poco con otras versiones de las bibliotecas.

**Hecho cuando:** el recomendador está evaluado con valoraciones escondidas, `recomendar` funciona con 3 usuarios y no propone nada ya valorado.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'M' is not defined` (o `'R'`, `'P_pop'`, `'cosine_similarity'`) | Las celdas se han ejecutado en desorden o Colab se reinició. | Ejecutad las celdas de este paso de arriba abajo, empezando por la primera (la del `import`). |
| `KeyError: 'valoraciones'` | En `pivot` habéis escrito `values="valoraciones"`; la columna es `valoracion`. | Escribid `values="valoracion"`, en singular. |
| `IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed` | `P_pop` no se ha repetido con `np.tile`: es una sola fila. | Usad `np.tile(media_item.values, (300, 1))`. |
| `IndexError: index 300 is out of bounds for axis 0 with size 300` | Habéis pedido `recomendar(301)`: solo hay usuarios 1 a 300. | Probad con un número entre 1 y 300. Un huésped nuevo se resuelve con la popularidad. |
| `recomendar(0)` no da error, pero devuelve recomendaciones | El usuario 0 no existe; Python cuenta `0 - 1 = -1` desde el final y devuelve las del usuario 300. | Los usuarios empiezan en 1. |
| `recomendar` propone algo que el usuario ya valoró | Falta `puntuacion[M[id_usuario - 1]] = -np.inf`. | Añadid esa línea antes de ordenar. |
| Todos los usuarios reciben casi las mismas experiencias | La función usa `P_pop` (la popularidad), no `P_item`. | Llamadla sin `P=` (usa item-item) o con `P=P_item`. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_09_paso_3.md) · [Ficha del reto](Reto_Sprint_09.md) · [Paso 5 →](Reto_Sprint_09_paso_5.md)
<!--/nav-->
