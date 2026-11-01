# Paso 3 · Mapa PCA e interpretación de los segmentos (día 1, 15 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md) · [Paso 4 →](Reto_Sprint_09_paso_4.md)
<!--/nav-->

1. Dibujar el mapa 2D con PCA, con los segmentos coloreados.
2. Calcular el perfil medio de cada segmento y su tamaño.
3. Ponerle nombre a cada segmento, con cifras.
4. Proponer una acción comercial por segmento.

**En sencillo.** Cada huésped tiene siete datos, y un dibujo solo tiene dos ejes. **PCA** es como hacer una foto a una escultura desde el mejor ángulo: se pierde algo (la profundidad), pero se ve la forma. Así pintaréis los 1200 huéspedes en un mapa y comprobaréis a simple vista si los grupos están separados. Después, para cada grupo calcularéis su **perfil**: la media de cada dato, como el retrato robot de un cliente típico. Con ese retrato, el grupo recibe un **nombre** que Lucía entienda y una **acción comercial**. El nombre tiene que salir de **vuestras cifras**, no del ingenio. No hace falta saber cómo calcula PCA las componentes: lo hace una línea de código.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **PCA** | Una técnica que resume muchas columnas en pocas «columnas nuevas» (componentes) para poder dibujar los datos. |
| **Componente** | Cada eje nuevo del mapa. La componente 1 recoge la mayor parte de la variación; la 2, la siguiente. |
| **% de varianza** | Cuánta información del conjunto conserva cada componente. Es lo que va en los ejes del mapa. |
| **Segmento** | Un grupo de huéspedes parecidos entre sí. Aquí, cada número de `grupo`. |
| **Perfil** | La media de cada variable dentro de un segmento: el retrato del cliente típico de ese grupo. |
| **`groupby`** | Reparte las filas de una tabla por grupos y calcula algo (la media, por ejemplo) en cada uno. |
| **Mapa de calor** | Una tabla pintada: rojo si el grupo está por encima de la media, azul si está por debajo. |
| **Acción comercial** | Qué enseñarle a ese segmento, cuándo y por qué canal. |

**Cómo se hace**

1. **Entrenar k-means con el `k` elegido y guardar el grupo de cada huésped.** Nueva celda (cambiad el 4 por el `k` que elegisteis):

    ```python
    k_elegido = 4
    km = KMeans(n_clusters=k_elegido, n_init=10, random_state=SEMILLA).fit(X)
    huespedes["grupo"] = km.labels_
    print(huespedes["grupo"].value_counts().sort_index())
    ```

    Qué hace cada línea:

    - `km = KMeans(…).fit(X)`: entrena k-means y guarda el modelo en `km`. Es lo mismo del paso 2, pero ahora con un solo `k`.
    - `huespedes["grupo"] = km.labels_`: añade a la tabla una columna `grupo` con el número de grupo de cada huésped.
    - `value_counts().sort_index()`: cuenta cuántos huéspedes hay en cada grupo y los ordena por número.

    Pulsad ▶. Con `k` = 4 salen los grupos 0, 1, 2 y 3 con 194, 402, 317 y 287 huéspedes.

2. **El mapa PCA.** Nueva celda:

    ```python
    pca = PCA(n_components=2, random_state=SEMILLA)
    Z2 = pca.fit_transform(X)
    var1, var2 = pca.explained_variance_ratio_ * 100

    fig, ax = plt.subplots(figsize=(7, 5))
    dibujo = ax.scatter(Z2[:, 0], Z2[:, 1], c=huespedes["grupo"], cmap="tab10", s=10, alpha=0.7)
    ax.set_title("Cuatro tipos de huésped bastante separados")
    ax.set_xlabel(f"Componente 1 ({var1:.0f} % de la varianza)")
    ax.set_ylabel(f"Componente 2 ({var2:.0f} % de la varianza)")
    ax.legend(*dibujo.legend_elements(), title="Segmento")
    fig.savefig("mapa_pca.png", dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Información conservada con 2 componentes: {var1 + var2:.1f} %")
    ```

    Qué hace cada línea:

    - `PCA(n_components=2, …).fit_transform(X)`: resume las 7 columnas de `X` en 2 y guarda un par de coordenadas por huésped en `Z2`.
    - `var1, var2 = pca.explained_variance_ratio_ * 100`: el % de varianza de cada componente, en dos variables.
    - `ax.scatter(Z2[:, 0], Z2[:, 1], c=huespedes["grupo"], …)`: dibuja un punto por huésped. `Z2[:, 0]` es la primera columna (eje horizontal) y `Z2[:, 1]`, la segunda (eje vertical). `c=` colorea por grupo.
    - `set_title(…)`: el título debe ser una **conclusión** («Cuatro tipos de huésped bastante separados»). **Cambiadlo** si en vuestro mapa no es verdad.
    - `set_xlabel`, `set_ylabel`: nombres de los ejes, con el % de varianza escrito automáticamente. `ax.legend(…)` muestra los segmentos.
    - `fig.savefig("mapa_pca.png", …)`: guarda el mapa como imagen, para la ficha del paso 5.

    Se ve un punto por huésped en cuatro nubes de colores. Los ejes dicen 43 % y 26 % de la varianza y la última línea escribe `Información conservada con 2 componentes: 68.7 %`. Es una «foto» que conserva cerca del 69 %: si vuestro mapa sale mezclado, decidlo en la ficha. Aquí, dos de las nubes se tocan un poco.

3. **El perfil de cada segmento.** Nueva celda:

    ```python
    perfil = huespedes.groupby("grupo")[variables].mean().round(1)
    perfil["n_huespedes"] = huespedes["grupo"].value_counts().sort_index()
    perfil["pct"] = (perfil["n_huespedes"] / len(huespedes) * 100).round(0)
    perfil
    ```

    Qué hace cada línea:

    - `huespedes.groupby("grupo")[variables].mean().round(1)`: agrupa por `grupo` y calcula la media de cada variable con un decimal.
    - `perfil["n_huespedes"] = …` y `perfil["pct"] = …`: añaden el tamaño de cada grupo y su porcentaje sobre los 1200.

    Pulsad ▶. Con `k` = 4 sale esta tabla (aquí, una fila por variable y una columna por grupo; el grupo puede salir con otro número en vuestro ordenador):

    | | grupo 0 | grupo 1 | grupo 2 | grupo 3 |
    |---|---|---|---|---|
    | `edad` | 34,6 | 40,3 | 57,2 | 29,3 |
    | `gasto_medio_dia` | 120,4 | 95,2 | 211,4 | 71,2 |
    | `noches_medias` | 2,6 | 7,4 | 8,1 | 6,1 |
    | `reservas_anio` | 4,0 | 1,3 | 1,6 | 2,1 |
    | `antelacion_media` | 22,2 | 110,3 | 90,3 | 59,7 |
    | `pct_gasto_actividades` | 41,2 | 26,0 | 20,0 | 74,6 |
    | `viaja_con_ninos` | 0,1 | 0,9 | 0,0 | 0,0 |
    | `n_huespedes` | 194 | 402 | 317 | 287 |
    | `pct` | 16 | 34 | 26 | 24 |

4. **Comparar con la media: el mapa de calor.** Nueva celda:

    ```python
    perfil_z = pd.DataFrame(km.cluster_centers_, columns=variables)
    fig, ax = plt.subplots(figsize=(9, 3.5))
    sns.heatmap(perfil_z, annot=True, fmt=".1f", cmap="RdBu_r", center=0, ax=ax)
    ax.set_title("Perfil de cada grupo (en desviaciones típicas respecto a la media)")
    ax.set_ylabel("Grupo")
    plt.show()
    ```

    Qué hace cada línea:

    - `km.cluster_centers_`: el centro de cada grupo, con los datos ya escalados; `pd.DataFrame(…, columns=variables)` los pone en una tabla con nombres.
    - `sns.heatmap(…)`: la pinta. `annot=True` escribe el número en cada casilla y `center=0` pone el blanco en la media.

    Un **0** es «en la media»; un **1,2**, «bastante por encima»; un **−1,7**, «muy por debajo». Los números grandes (en rojo o azul fuerte) son los que definen al grupo. Por ejemplo, el grupo de 402 tiene un 1,2 en `viaja_con_ninos` y el de 287, un 1,5 en `pct_gasto_actividades`.

5. **Poner nombre a cada segmento.** Cada nombre se apoya en **dos cifras** de su perfil. Con los datos de esta ejecución:

    | Grupo | Nombre | Tamaño | Las dos cifras que lo justifican | Acción comercial (ejemplo) |
    |---|---|---|---|---|
    | 1 | Familias de larga estancia | 402 (34 %) | 9 de cada 10 viajan con niños y reservan con 110 días de antelación | Pack «Niños gratis en el parque acuático» en la reserva |
    | 2 | Mayores de alto gasto | 317 (26 %) | 57 años de media y 211 € de gasto al día | Mejora de habitación y experiencias tranquilas, con reserva anticipada |
    | 3 | Jóvenes aventureros | 287 (24 %) | 29 años de media y el 75 % de su gasto en actividades | Newsletter solo con excursiones y deportes, con precio de grupo |
    | 0 | Escapadas frecuentes | 194 (16 %) | 4 reservas al año y estancias de 2,6 noches | Oferta de última hora: reservan con unos 22 días de antelación |

    **Los números de grupo los pone el algoritmo y pueden salir permutados en otro ordenador.** Mirad vuestro `perfil` y poned cada nombre donde corresponda: **no copiéis los nombres de aquí sin comprobarlos con vuestras cifras**. La IA puede sugerir nombres, pero un nombre que no cuadra con vuestras cifras no vale. Cada **acción** dice qué enseñar, cuándo y por qué canal, y tiene que servir a Lucía de verdad.

6. **Guardar los nombres y comprobar los tamaños.** Nueva celda, con **vuestros** nombres (la clave es el número de grupo, sin comillas):

    ```python
    nombres_segmentos = {0: "Escapadas frecuentes", 1: "Familias de larga estancia",
                         2: "Mayores de alto gasto", 3: "Jóvenes aventureros"}
    perfil["nombre"] = pd.Series(nombres_segmentos)
    print(perfil[["nombre", "n_huespedes", "pct"]])
    print("Suma de tamaños:", perfil["n_huespedes"].sum())
    ```

    Qué hace cada línea:

    - `nombres_segmentos = {0: "…", …}`: un diccionario `número de grupo: nombre`. Las comillas rodean cada nombre; los dos puntos separan la clave y el nombre.
    - `perfil["nombre"] = pd.Series(nombres_segmentos)`: añade a la tabla una columna con el nombre de cada grupo.
    - La última línea suma los tamaños: tiene que salir **1200**.

    Después, en una celda de texto, apuntad una fila por segmento: nombre, tamaño, perfil con dos cifras y acción. Es lo que pasaréis a la ficha en el paso 5.

**Qué deberíais ver.** Un mapa con un color por segmento y el % de varianza en los ejes (aquí, 43 % y 26 %, y 68,7 % entre los dos), una tabla `perfil` con la media de cada variable, el tamaño y el porcentaje de cada grupo, el mapa de calor y, por segmento, un nombre, dos cifras y una acción. La suma de tamaños es 1200.

**Hecho cuando:** el mapa está dibujado y cada segmento tiene nombre, tamaño, perfil con cifras y una acción.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'PCA' is not defined` (o `'sns'`, `'X'`) | No se han ejecutado las celdas del paso 1. | Ejecutad desde arriba, en orden. |
| `KeyError: 'grupo'` | Aún no se ha ejecutado la celda del apartado 1 de este paso. | Ejecutadla antes del perfil y del mapa. |
| Aparece una columna `grupo` en `perfil` o en el mapa de calor | Se ha vuelto a ejecutar la celda `variables = …` **después** de crear `grupo`, y `grupo` se ha colado como variable. | *Entorno de ejecución → Reiniciar y ejecutar todo*: así `variables` se crea antes que `grupo`. |
| Los grupos del mapa se mezclan | Es posible: con 2 componentes solo se ve el 69 % de la información. | Decidlo en la ficha. No cambiéis los grupos para que «se vean mejor». |
| La columna `nombre` sale con `NaN` en algún grupo | Falta ese número en el diccionario o las claves llevan comillas (`"0"`). | Las claves son números sin comillas: `{0: "…", 1: "…"}`. |
| Vuestros grupos y tamaños no son los de aquí | El algoritmo numera los grupos a su manera y, con otra versión de scikit-learn, los números varían un poco. | Es normal. Seguid **vuestro** `perfil` y poned los nombres según vuestras cifras. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_09_paso_2.md) · [Ficha del reto](Reto_Sprint_09.md) · [Paso 4 →](Reto_Sprint_09_paso_4.md)
<!--/nav-->
