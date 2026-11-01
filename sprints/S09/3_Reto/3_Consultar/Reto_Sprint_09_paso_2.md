# Paso 2 · Segmentar y elegir k (día 1, 20 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 3 →](Reto_Sprint_09_paso_3.md)
<!--/nav-->

1. Probar k-means con `k` de 2 a 8.
2. Calcular la silueta de cada `k` y dibujar la curva.
3. Elegir `k` con una razón técnica **y** una de negocio.
4. Escribir esa razón en una frase.

**En sencillo.** Imaginad una cena con 1200 invitados y que hay que sentarlos en mesas según lo parecidos que sean. Antes de empezar tenéis que decidir **cuántas mesas** (`k`). K-means coloca un «centro» en cada mesa y manda a cada persona al centro más cercano; después recoloca los centros y repite. Pero ¿cuántas mesas son las buenas? Aquí **no hay respuesta correcta en los datos**: probáis de 2 a 8 mesas y medís con la **silueta** qué tan compactas y separadas quedan (cuanto más alta, mejor). El número más alto no decide solo: también hay que preguntarse si Lucía puede **hacer algo distinto** para cada grupo. No hace falta saber cómo funciona k-means por dentro: basta con saber qué se le pide y qué devuelve.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **k-means** | Un algoritmo que reparte los datos en `k` grupos de elementos parecidos, sin que nadie le diga de antemano a qué grupo pertenece cada uno. |
| **`k`** | El número de grupos. Lo decidís vosotros. |
| **Etiqueta** | El número de grupo que el algoritmo asigna a cada huésped (0, 1, 2…). Aquí, `etiquetas` tiene 1200 números. |
| **Silueta** | Una nota de −1 a 1 para cada `k`: cuanto más alta, grupos más compactos y más separados entre sí. Por encima de 0,5 es una estructura buena; entre 0,25 y 0,5, aceptable. |
| **Diccionario** (`{}`) | Una agenda de parejas `clave: valor`. Aquí, `siluetas` guarda `k: silueta`. |
| **Bucle `for`** | Repite unas líneas para cada valor de una lista: `for k in range(2, 9)` las repite para k = 2, 3… 8. |
| **`range(2, 9)`** | Los números del 2 al 8: el último (el 9) **no entra**. |
| **`n_init=10`** | Hace que k-means se ejecute 10 veces desde puntos de partida distintos y se quede con la mejor. Resultado más estable. |
| **`max(…, key=…)`** | Devuelve la clave del diccionario cuyo valor es el mayor. |

**Cómo se hace**

1. **Probar cada `k` y guardar su silueta.** En una celda nueva (pulsad **+ Código**):

    ```python
    siluetas = {}
    for k in range(2, 9):
        etiquetas = KMeans(n_clusters=k, n_init=10, random_state=SEMILLA).fit_predict(X)
        siluetas[k] = silhouette_score(X, etiquetas)
    k_mejor = max(siluetas, key=siluetas.get)
    print({k: round(v, 3) for k, v in siluetas.items()})
    print("k con mejor silueta:", k_mejor)
    ```

    Qué hace cada línea:

    - `siluetas = {}`: crea un diccionario vacío, la agenda donde se anotará cada resultado.
    - `for k in range(2, 9):`: repite las líneas de debajo (las que están **con sangría**, empujadas a la derecha) para cada `k`. Los dos puntos del final son obligatorios.
    - `KMeans(n_clusters=k, n_init=10, random_state=SEMILLA).fit_predict(X)`: prepara k-means con `k` grupos, lo ejecuta sobre `X` y devuelve las `etiquetas`. `random_state=SEMILLA` fija el azar.
    - `siluetas[k] = silhouette_score(X, etiquetas)`: calcula la silueta media y la anota en la agenda con la clave `k`.
    - `k_mejor = max(siluetas, key=siluetas.get)`: guarda el `k` de silueta más alta.
    - Las dos líneas `print` escriben la agenda (redondeada a 3 decimales) y el mejor `k`.

    Pulsad ▶ (tarda unos segundos). Sale `{2: 0.367, 3: 0.415, 4: 0.431, 5: 0.414, 6: 0.326, 7: 0.317, 8: 0.257}` y `k con mejor silueta: 4`.

2. **Dibujar la curva.** Otra celda:

    ```python
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(list(siluetas), list(siluetas.values()), marker="o")
    ax.axvline(k_mejor, color="tab:red", linestyle="--", label=f"mejor k = {k_mejor}")
    ax.set_xlabel("Número de grupos (k)")
    ax.set_ylabel("Silueta media")
    ax.set_title(f"La silueta es más alta con k = {k_mejor}")
    ax.legend()
    plt.show()
    ```

    Qué hace cada línea:

    - `fig, ax = plt.subplots(figsize=(6, 3.5))`: crea el lienzo del gráfico (6 × 3,5 pulgadas). `ax` es el dibujo dentro del lienzo.
    - `ax.plot(…, marker="o")`: dibuja la línea con un punto en cada `k` (eje horizontal) y su silueta (eje vertical).
    - `ax.axvline(k_mejor, …)`: añade una línea vertical roja y discontinua en el mejor `k`.
    - `set_xlabel`, `set_ylabel`, `set_title`: ponen los nombres de los ejes y el título. El título dice una **conclusión**, no solo «silueta».
    - `ax.legend()` y `plt.show()`: muestran la leyenda y el gráfico.

    Veréis una curva que sube hasta k = 4 y baja después, con la línea roja en 4.

3. **Mirar cuántos huéspedes hay en cada grupo.** La silueta de 3, 4 y 5 casi empata (0,415, 0,431 y 0,414), así que hay que mirar el negocio. Otra celda:

    ```python
    for k in (3, 4, 5):
        etiquetas = KMeans(n_clusters=k, n_init=10, random_state=SEMILLA).fit_predict(X)
        print(k, "grupos · tamaños:", np.bincount(etiquetas))
    ```

    Qué hace cada línea:

    - `for k in (3, 4, 5):`: repite para esos tres valores, escritos entre paréntesis.
    - `np.bincount(etiquetas)`: cuenta cuántos huéspedes hay con la etiqueta 0, con la 1, con la 2…

    Sale: `3 grupos · tamaños: [317 480 403]`, `4 grupos · tamaños: [194 402 317 287]` y `5 grupos · tamaños: [ 72 402 317 126 283]`. Con 5 grupos, uno tiene solo 72 huéspedes (el 6 %): cuesta justificar una campaña para tan pocos. Con 4, el más pequeño tiene 194 (el 16 %) y los cuatro son lo bastante grandes para actuar.

4. **Elegir `k` y escribir la frase con las dos razones.** En una celda de texto (**+ Texto**) con este molde:

    ```text
    Elegimos k = … porque la silueta es … y, para el negocio, … grupos se pueden gestionar (el más pequeño tiene el … % de los huéspedes).
    ```

    Por ejemplo, con los números de esta ejecución: *«Elegimos k = 4 porque su silueta es la más alta (0,431), aunque 3 y 5 casi empatan, y, para el negocio, 4 grupos se pueden gestionar: el más pequeño tiene el 16 % de los huéspedes.»* Los vuestros pueden ser otros. Vale elegir 3 o 5 si lo razonáis. **No vale** elegir solo porque «salía el número más alto» ni «porque lo dijo la IA». Esta frase irá también a la cabecera de la ficha del paso 5.

**Qué deberíais ver.** Una agenda con siluetas para `k` = 2 a 8 (la mayor, en torno a 0,43 con `k` = 4), una curva con la línea roja en `k_mejor`, los tamaños de los grupos para 3, 4 y 5, y un `k` elegido entre 3 y 5 con su frase. Si usáis otra versión de scikit-learn, las siluetas pueden cambiar en las milésimas.

**Hecho cuando:** hay curva de silueta, un `k` elegido y la frase con las dos razones.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'X' is not defined` (o `'KMeans'`) | No se han ejecutado las celdas del paso 1, o Colab se reinició. | Pulsad ▶ en las celdas de arriba, en orden (*Entorno de ejecución → Ejecutar todo*). |
| `ValueError: Number of labels is 1. Valid values are 2 to n_samples - 1 (inclusive)` | Habéis probado `k = 1` (`range(1, 9)`): con un solo grupo no hay silueta. | Escribid `range(2, 9)`. |
| La curva acaba en 7 | Habéis escrito `range(2, 8)`: el último número no entra. | Escribid `range(2, 9)` para llegar al 8. |
| `IndentationError: expected an indented block after 'for' statement on line 2` o `SyntaxError: expected ':'` | Falta la sangría en las líneas de dentro del bucle, o los dos puntos del final. | Dejad 4 espacios delante de las líneas de dentro y poned `:` al final de la línea del `for`. |
| La silueta sale más alta (por ejemplo, 0,52 con `k` = 2) | Habéis agrupado sin escalar (`huespedes[variables]` en vez de `X`). Engaña: mandan las columnas de números grandes, como el gasto. | Usad `X`, la matriz escalada del paso 1. |
| `k_mejor` es 3 o 5, o las cifras no coinciden con las de aquí | Con otra versión de scikit-learn cambian unas milésimas; con 3, 4 y 5 casi empatados, puede ganar otro. | Es válido. Usad **vuestras** cifras en la frase y la razón de negocio. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_09_paso_1.md) · [Ficha del reto](Reto_Sprint_09.md) · [Paso 3 →](Reto_Sprint_09_paso_3.md)
<!--/nav-->
