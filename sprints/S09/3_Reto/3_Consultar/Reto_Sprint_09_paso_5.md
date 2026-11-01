# Paso 5 · Ficha, IA responsable, revisión y entrega (día 2, 30 minutos)

<!--nav-->
> Sprint 9 · Reto «Conocer al huésped» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_09.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_09_una_pagina.md)
<!--/nav-->

1. Rellenar la ficha de segmentos y la nota de IA responsable.
2. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado en la ficha.
3. Dejar el cuaderno ejecutable y subir los ficheros a `sprint-09/`.
4. Ensayar 3 minutos de review.

**En sencillo.** Lucía no va a abrir vuestro cuaderno: lo que lee es la **ficha**, una página que le cuenta quiénes son sus clientes y qué hacer con ellos, como el prospecto de un medicamento. Casi no hay código: se escribe **texto** con las cifras que ya tenéis. Además hay que contar con honestidad qué riesgos tiene usar estos grupos y estas recomendaciones, y dejar el cuaderno de modo que otra persona lo repita. Después, alguien del equipo que no escribió esa parte lo revisa con la rúbrica, con ojos frescos, y entre todos subís el trabajo a GitHub. No hace falta saber Markdown: la plantilla trae las tablas ya montadas.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Ficha de segmentos** | La página para el cliente: método y `k`, mapa, una fila por segmento, recomendador, riesgos y límites. Es el fichero `ficha_segmentos.md`. |
| **Markdown (`.md`)** | Texto normal con marcas sencillas: `#` para los títulos y barras verticales para separar las columnas de una tabla. |
| **Experiencia estrella** | La experiencia que mejor encaja con un segmento y que recomendaríais a ese grupo. |
| **Supuesto** | Algo que damos por cierto sin poder comprobarlo con los datos. Se escribe como tal. |
| **Sesgo de popularidad** | Que se recomienden siempre las mismas experiencias (las más conocidas) y las demás casi nunca salgan. |
| **Discriminación** | Tratar peor a alguien por su edad, por viajar con niños, etc. (por ejemplo, subiéndole el precio). |
| **Rúbrica** | La tabla con que se evalúa el reto: cuatro criterios, cada uno de 1 a 4. |
| ***Commit*** | Guardar en GitHub un cambio con un mensaje corto y vuestro nombre. Sin pulsar **Commit changes** no se guarda nada. |

**Cómo se hace**

1. **Crear `ficha_segmentos.md` con la plantilla.** Abrid la [plantilla](../1_Trabajar/plantillas/plantilla_ficha_segmentos.md) y pulsad **Raw**, `Ctrl + A`, `Ctrl + C`. Después, en el repositorio del equipo, entrad en la carpeta `sprint-09`, **Add file → Create new file**, nombre `ficha_segmentos.md`, y pegad. Rellenad cada sección **con vuestras cifras**, sin dejar los `______`:

    | Sección | Qué escribís |
    |---|---|
    | Cabecera | Equipo, método (k-means; tachad lo demás), `k`, silueta (aquí, 0,431 con `k` = 4) y la frase de las dos razones del paso 2 |
    | Mapa de segmentos | La imagen `mapa_pca.png` (se baja del panel de archivos de Colab y se sube a `sprint-09`) con una línea como «Mapa: ver el fichero `mapa_pca.png`», o decid dónde está en el cuaderno |
    | Segmentos | Una fila por segmento: nombre, tamaño (n y %), perfil con cifras, acción y experiencia estrella. La tabla `perfil` y la de nombres del paso 3 ya traen casi todo |
    | Recomendador | Los dos métodos con RMSE y precision@3, el elegido y por qué, un ejemplo con un usuario (aquí, el usuario 1 → Parque Timanfaya, 4,73) y qué haría el sistema con un huésped nuevo (popularidad) |
    | IA responsable | Cinco líneas, con **al menos 2 riesgos específicos** de este caso y su medida (apartado 3) |
    | Limitaciones | Datos sintéticos, comportamiento de un año, 4 a 11 valoraciones por persona, el mapa solo conserva el 69 % y la prueba del recomendador tiene 115 usuarios. Añadid las vuestras |

2. **Elegir la experiencia estrella de cada segmento.** Ojo: los datos son sintéticos y las 300 personas de las valoraciones **no son** las de `huespedes.csv`, así que **no hay un cruce real** entre los dos ficheros. Elegid la experiencia razonando con el perfil del segmento, apoyadla en lo que recomienda vuestro prototipo y **anotadla como supuesto**. Ejemplos con los datos de esta ejecución (la cuarta es para vosotros):

    | Segmento | Experiencia estrella | Por qué (y nota media en el prototipo) |
    |---|---|---|
    | Familias de larga estancia | Parque acuático (familia) | 9 de cada 10 viajan con niños (3,68) |
    | Jóvenes aventureros | Parapente (aventura) | El 75 % de su gasto es en actividades (3,82) |
    | Mayores de alto gasto | Visita a Garachico (cultura) | Gastan 211 € al día y casi nada en actividades: plan tranquilo (4,21) |
    | Escapadas frecuentes | … | … |

    Mirad la nota media de la experiencia: no pongáis de estrella una que el prototipo valora mal (el Spa y termas tiene un 1,70). Escribid: «Supuesto: los usuarios que valoraron no son los huéspedes de este segmento».

3. **La nota de IA responsable (5 líneas).** Elegid los riesgos que valen para **vuestro** caso, cada uno con una medida. Ejemplos:

    ```text
    - Riesgo 1 (segmentar): discriminar, si se usa la edad o «viaja con niños» para cobrar precios distintos. Medida: usar los segmentos para decidir qué comunicar, no para variar precios.
    - Riesgo 2 (recomendar): sesgo de popularidad. Medida: reservar un hueco de cada lista a una experiencia menos conocida.
    - Datos personales implicados y base legal: …
    ```

    Si queréis **comprobar** el riesgo 2 con datos (es un extra), añadid esta celda al cuaderno, después de `recomendar`:

    ```python
    todas = [i for u in range(1, 301) for i in recomendar(u, 3).index]
    print(len(set(todas)), "experiencias distintas recomendadas, de 25")
    print(pd.Series(todas).value_counts().head(3))
    ```

    Qué hace cada línea:

    - La primera recorre los 300 usuarios, pide a `recomendar` tres experiencias para cada uno y las junta en una lista (`todas`, con 900 números).
    - `len(set(todas))`: `set` elimina los repetidos y `len` cuenta los que quedan: cuántas experiencias **distintas** se han recomendado.
    - `pd.Series(todas).value_counts().head(3)`: las tres que más se repiten y cuántas veces.

    Con item-item sale `18 experiencias distintas recomendadas, de 25`, y la 11 (Parque Timanfaya) se repite 160 veces, la 22 (Garachico), 144 y la 24 (Parapente), 106. Con la popularidad (`P=P_pop`) solo saldrían 8. Es una cifra honesta para la ficha: el sesgo existe, aunque item-item lo reduce.

4. **Declarar la IA en el cuaderno.** En una celda de texto, con este molde: «Usamos la IA para …; comprobamos …; cambiamos …». Si no la usasteis, decidlo. **Nada de datos personales ni claves** en una IA.
5. **La revisión con la rúbrica (10 minutos).** La hace **una persona que no escribió esa parte**. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md): ejecutar el cuaderno con *Reiniciar y ejecutar todo*, leer la ficha como si fuera Lucía (¿se entiende qué hacer con cada segmento? ¿los tamaños suman 1200?), mirar el cuaderno (¿se escala antes de agrupar?, ¿`recomendar` no devuelve nada ya valorado?), **comprobar que cada nombre sigue encajando con su fila de `perfil`** y poner un nivel de 1 a 4 por criterio con **una frase de prueba**, por ejemplo: «3 · el cuaderno se ejecuta entero y salen k = 4 y los mismos tamaños, pero falta probar `recomendar` con un tercer usuario». Sin prueba escrita, el nivel no vale. Se apunta en la sección «Revisión con la rúbrica» del final de `ficha_segmentos.md` (borrad el texto entre `<…>`). Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos».
6. **Dejar el cuaderno y subir los ficheros (la vía del curso, desde el navegador).** En Colab: *Entorno de ejecución → Reiniciar y ejecutar todo* (ninguna celda debe dar error) y *Archivo → Descargar → Descargar .ipynb*; bajad también `mapa_pca.png` desde el panel de archivos (clic derecho → *Descargar*). Después, seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-09`**; (2) *Add file → Upload files* y arrastrad los ficheros; (3) escribid un mensaje corto («Añado segmentación y recomendador») y pulsad **Commit changes**. Un reparto posible: la persona A sube el cuaderno, la B la ficha y el mapa («Añado ficha de segmentos»), y cada persona sube su autoevaluación. Nombres de archivo **sin espacios ni tildes**.
7. **Ensayar la review (3 minutos).** Preparad qué enseñaréis: **vuestros segmentos (nombre y acción)** y **una recomendación concreta para un usuario**. Decidid quién cuenta qué.

**Qué deberíais ver.** En la carpeta `sprint-09` del repositorio, el cuaderno y la ficha del equipo (y el mapa, si lo habéis puesto) y una hoja de autoevaluación por persona (**2 + N**); y en el historial (el icono del reloj), *commits* de todas las personas del equipo.

**Hecho cuando:** otra persona podría repetir el cuaderno de arriba abajo, la sección «Revisión con la rúbrica» está rellena y cada persona ha subido algo con su cuenta.

**Después, 40 minutos de entrega, review y retrospectiva:** cada persona rellena y sube su [autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md) a `sprint-09/`, y el equipo presenta en 3 minutos **sus segmentos (nombre y acción)** y **una recomendación concreta para un usuario**. Se comparan los `k` elegidos y se discute: *¿es el mismo cliente aunque le pongamos otro nombre?*

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Los tamaños de la ficha no suman 1200 | Alguna cifra está mal copiada. | Copiadlas de la tabla `perfil` y comprobad con `perfil["n_huespedes"].sum()`. |
| No encontráis el mapa al leer la ficha | El fichero `mapa_pca.png` no está en `sprint-09` o la ficha no dice dónde está. | Subidlo a la misma carpeta (nombre exacto, en minúsculas) y escribid en la ficha «Mapa: ver el fichero `mapa_pca.png`». |
| Las tablas de la ficha se ven como líneas de texto con barras verticales | Se ha borrado alguna de las barras de la tabla o la línea de guiones que hay bajo la cabecera. | Pulsad **Preview** en GitHub, comparad con la plantilla y reponed lo que falte. |
| Tras *Reiniciar y ejecutar todo*, los nombres no encajan con los perfiles | Los números de grupo pueden salir en otro orden con otra versión de las bibliotecas, y el diccionario `nombres_segmentos` va por número. | Mirad el `perfil` y corregid el diccionario según vuestras cifras. Dejad escrita la versión en el cuaderno. |
| Al *Reiniciar y ejecutar todo*, una celda da error en rojo | Una celda depende de otra que está debajo o que falla. | Leed el error de la **primera** celda en rojo, corregidla y repetid. |
| Subisteis un fichero a la raíz del repositorio y no a `sprint-09` | No entrasteis primero en la carpeta. | Abrid el fichero → icono del lápiz → delante del nombre escribid `sprint-09/` → **Commit changes**. |
| No sabéis qué nivel poner en la rúbrica | Los niveles están descritos en [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). | Poned el nivel cuyo texto **se cumple entero** (si algo se cumple a medias, es el de abajo) y escribid la prueba. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_09_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_09.md)
<!--/nav-->
