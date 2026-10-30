# Sprint 9 · Reto «Conocer al huésped»

> **Ficha completa del reto, para consultar.** Para trabajar con ella abierta, usad [el reto en una página](../1_Reto_en_una_pagina/Reto_Sprint_09_una_pagina.md).
>
> - Volver al [README del sprint](../../README.md) · [README del sprint en PDF](../../pdf/README_Sprint_09.pdf) · [ecofriendly](../../pdf/README_Sprint_09_ecofriendly.pdf)
> - **Esta ficha en PDF:** [a color](pdf/Reto_Sprint_09.pdf) · [ecofriendly, para imprimir](pdf/Reto_Sprint_09_ecofriendly.pdf)
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** Lucía, la directora comercial de TurisData Canarias, envía **la misma newsletter a sus 1.200 huéspedes** y vende sus **25 experiencias** con los mismos banners. Sospecha que hay «tipos» de cliente muy distintos y que cada uno querría cosas diferentes. Os pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno.»* Ninguna columna dice a qué tipo pertenece cada huésped: vosotros tenéis que **descubrir los grupos** con *clustering* (agrupar datos parecidos sin respuestas previas), **dibujarlos** en un mapa 2D, **ponerles nombre** y proponer **una acción comercial por grupo**. Además, construiréis un **recomendador** sencillo: dado un huésped, sugerirle experiencias que probablemente le gusten.

**Cómo se trabaja.** No hace falta experiencia previa: los cuadernos del sprint (`S09_01`, `S09_02` y `S09_03`) ya os hacen practicar cada pieza, y el reto consiste en **reutilizarlas con vuestras propias decisiones** y, sobre todo, en **explicar** qué habéis encontrado. No hay pruebas automáticas ni solución del docente: los grupos se validan con **sentido de negocio** y con **métricas internas** (silueta, RMSE). En clase tenéis 10 minutos de planning y 45 de reto el día 1, y 50 de reto más 40 de entrega, review y retrospectiva el día 2; lo que no quepa va a casa. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Python con `numpy`, `pandas`, `matplotlib`/`seaborn` y `scikit-learn`** (solo esas bibliotecas: nada de librerías de recomendación especializadas) | Escribir el cuaderno del reto | Ya instaladas en Google Colab |
| **Google Colab** | Crear y ejecutar `reto_S09_conocer_al_huesped.ipynb` | En colab.research.google.com: *Archivo → Cuaderno nuevo* |
| **Los datos de huéspedes** [`huespedes.csv`](../../../../datos/huespedes.csv) | 1.200 huéspedes con 7 variables (`edad`, `gasto_medio_dia`, `noches_medias`, `reservas_anio`, `antelacion_media`, `pct_gasto_actividades`, `viaja_con_ninos`). Son **sintéticos** | No hace falta descargarlos: la celda «Preparación» de los cuadernos `S09_01`–`S09_03` los baja sola |
| **Las valoraciones** [`valoraciones_experiencias.csv`](../../../../datos/valoraciones_experiencias.csv) y [`experiencias.csv`](../../../../datos/experiencias.csv) | Unas 2.200 valoraciones (de 1 a 5 estrellas) de 300 usuarios sobre 25 experiencias, y el catálogo con nombre, categoría e isla | Igual: los baja la celda «Preparación» |
| **Cuadernos del sprint**: [`S09_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_01_clustering.ipynb), [`S09_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_02_pca.ipynb) y [`S09_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_03_recomendadores.ipynb) | El código de cada paso: escalar, k-means y silueta, PCA, recomendadores, RMSE y precision@3 | Colab; su [código explicado](../../2_Practica/codigo_explicado/README.md) |
| **Presentaciones** [Clustering y PCA](../../1_Teoria/S09.1_Clustering_y_PCA.pdf) y [Sistemas de recomendación](../../1_Teoria/S09.2_Sistemas_de_recomendacion.pdf) | Repasar los conceptos | En el repositorio del curso |
| **La plantilla de la ficha** [`plantilla_ficha_segmentos.md`](../4_Plantillas_y_entrega/plantilla_ficha_segmentos.md) | Ficha de segmentos con huecos, nota de IA responsable y sección «Revisión con la rúbrica» | En GitHub: abrid el archivo y copiad el texto con el botón *Raw* |
| **Cómo entregar en GitHub** | Subir el cuaderno y la ficha a `sprint-09/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender conceptos, pedir nombres y pensar riesgos | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 📦 Qué entregar

Este apartado responde a **dos preguntas distintas**, una tabla para cada una:

**Tabla A · Los ficheros:** qué ficheros hay, de dónde sale cada uno (ya hecho, lo modificáis, lo creáis o lo genera el cuaderno) y **cuáles se suben y adónde**.

**Tabla B · Los requisitos:** qué tiene que cumplir lo que entregáis y hasta dónde llegar (🟢 mínimo, 🟡 estándar, 🔴 extra). **Es lo que se evalúa.**

**En total, al final del sprint se suben a `sprint-09/`:** **2 ficheros del equipo** (`reto_S09_conocer_al_huesped.ipynb`, `ficha_segmentos.md`) **+ 1 autoevaluación y coevaluación por persona**, es decir, **2 + tantos ficheros como personas haya en el equipo** (un equipo de 3 sube 5). «El reto» no es un fichero aparte: son esos dos ficheros. La **nota de IA responsable** (5 líneas) y la **revisión con la rúbrica** van **dentro de la ficha**, no en ficheros distintos. Los datos no se suben: ya están en el repositorio del curso y el cuaderno los descarga solo. La imagen del mapa solo se sube si la ponéis en la ficha. La *review* y la *retro* se hacen de palabra: no se suben.

#### Tabla A · Los ficheros: de dónde sale cada uno y cuáles se suben

Todo lo que se sube va al repositorio privado del equipo (`ifcd107-equipo-…`), en la carpeta **`sprint-09/`**.

| Fichero | Origen | Qué hacéis vosotros | ¿Se sube? |
|---|---|---|---|
| `reto_S09_conocer_al_huesped.ipynb` | **Lo creáis.** Cuaderno nuevo en Colab; podéis reutilizar el código de `S09_01`, `S09_02` y `S09_03` | Segmentación, mapa PCA y recomendador, con semillas fijas y el uso de IA declarado | **Sí** · `sprint-09/` |
| `ficha_segmentos.md` | **Lo creáis a partir de una plantilla.** Os damos `plantilla_ficha_segmentos.md` con huecos | Copiarla como `ficha_segmentos.md` y rellenarla: segmentos, recomendador, nota de IA responsable y revisión con la rúbrica | **Sí** · `sprint-09/` |
| `mapa_pca.png` | **Lo genera el cuaderno** al guardar la figura del mapa (por ejemplo con `plt.savefig("mapa_pca.png")`) | Descargarla del panel de archivos de Colab y enlazarla desde la ficha | Solo si ponéis el mapa en la ficha · `sprint-09/` |
| Autoevaluación y coevaluación (`autoevaluacion_nombre.md`) | **Ya hecha, en blanco** | Cada persona copia la plantilla con su nombre y la rellena; la coevaluación va **dentro del mismo fichero** | **Sí**, **una por persona** (no una por equipo) · `sprint-09/` |
| `huespedes.csv` | **Ya hecho.** Los datos de 1.200 huéspedes (sintéticos) | Nada: el cuaderno los descarga con la celda «Preparación» | **No**: ya están en `datos/` del repositorio del curso |
| `valoraciones_experiencias.csv` y `experiencias.csv` | **Ya hechos.** Valoraciones y catálogo de 25 experiencias | Nada: los descarga la misma celda | **No**: ya están en `datos/` del repositorio del curso |

#### Tabla B · Los requisitos: qué tiene que cumplir y hasta dónde llegar

| Requisito | Qué se pide exactamente | Nivel | Dónde se comprueba |
|---|---|---|---|
| **Escalar antes de agrupar** | Las 7 variables numéricas de `huespedes.csv` (sin `id_huesped`) se escalan antes de aplicar el clustering | 🟢 Mínimo | Cuaderno |
| **Elegir k** | k-means con varios `k` (de 2 a 8), curva de la silueta y **una frase con las dos razones** del `k` elegido: la técnica (silueta) y la de negocio (¿puede Lucía actuar con ese número de grupos?) | 🟢 Mínimo | Cuaderno y cabecera de la ficha |
| **Mapa 2D con PCA** | Los huéspedes en 2 componentes, coloreados por segmento, con el **% de varianza** en cada eje y un título que enuncia una conclusión | 🟢 Mínimo | Cuaderno y ficha |
| **Ficha de segmentos** | Por segmento: nombre comercial, tamaño (n y %), perfil en una frase **con cifras** y **una acción comercial**. Los tamaños suman 1.200 | 🟢 Mínimo | `ficha_segmentos.md` |
| **Nota de IA responsable** | 5 líneas dentro de la ficha sobre los riesgos de segmentar y recomendar | 🟢 Mínimo | `ficha_segmentos.md` |
| **Declarar el uso de la IA** | En el cuaderno, dónde la habéis usado y qué habéis comprobado a mano | 🟢 Mínimo | Cuaderno |
| **Recomendador comparado** | Al menos **dos métodos** (la popularidad y otro), evaluados con valoraciones **escondidas** (división de prueba) con **RMSE** y **precision@3**, y una frase que explica cuál elegís | 🟡 Estándar | Cuaderno y apartado «Recomendador» de la ficha |
| **Función `recomendar(id_usuario, n)`** | Devuelve las `n` mejores experiencias que el usuario **aún no ha valorado**; probada con 3 usuarios distintos | 🟡 Estándar | Cuaderno |
| **Experiencia estrella** | Por segmento, la experiencia que recomienda vuestro prototipo | 🟡 Estándar | `ficha_segmentos.md` |
| **IA responsable con riesgos concretos** | Al menos **2 riesgos específicos** de este caso (por ejemplo, sesgo de popularidad, discriminación por edad o niños, privacidad), cada uno con su medida | 🟡 Estándar | `ficha_segmentos.md` |
| **Cuaderno reproducible** | «Reiniciar y ejecutar todo» funciona sin errores y con semillas fijas | 🟡 Estándar | Cuaderno |
| **Git** | Cada persona del equipo sube su parte, con un mensaje claro, sin claves ni datos personales | 🟡 Estándar | Historial del repositorio del equipo |
| **Revisión y autoevaluación** | Alguien que **no escribió esa parte** revisa cuaderno y ficha con la rúbrica (justo debajo de estas tablas) y anota nivel y prueba en la ficha; cada persona sube su hoja de autoevaluación y coevaluación | 🟡 Estándar | `ficha_segmentos.md` (sección «Revisión con la rúbrica») y `sprint-09/` |
| **Extras** | Comparar k-means con clustering jerárquico o DBSCAN y explicar la diferencia · interpretar los ejes del PCA con las cargas · recomendar a un huésped nuevo sin historial | 🔴 Extra | Cuaderno y ficha |

#### Rúbrica del reto · cómo se puntúa y cómo se revisa

La usan **dos veces**: el equipo, para revisar su propio trabajo antes de entregar (es lo que dice la *Definition of Done*), y el docente, para puntuar. Se mira **cada criterio por separado** y se pone el nivel de la columna cuyo texto **se cumple entero**: si lo de un nivel se cumple a medias, es el nivel de abajo. **0** significa que no se ha entregado nada de ese criterio.

Orientación: lo que pide el nivel 🟢 mínimo sale en un **2**, el 🟡 estándar en un **3** y los 🔴 extras en un **4**.

| Criterio | 1 · Empezado | 2 · Mínimo | 3 · Estándar | 4 · Extra |
|---|---|---|---|---|
| **Corrección técnica** (¿funciona?) | Hay código, pero se agrupa sin escalar, el `k` se elige sin mirar la silueta o el cuaderno da errores | Las variables están escaladas, hay curva de silueta para varios `k` y un mapa PCA con los segmentos coloreados | Además, el recomendador se evalúa con valoraciones escondidas (RMSE y precision@3) frente a la popularidad, y `recomendar` no propone nada ya valorado en 3 usuarios de prueba | Además, compara k-means con jerárquico o DBSCAN con resultados razonados, o recomienda a un huésped nuevo sin historial |
| **Reproducibilidad** (¿lo puede repetir otra persona?) | Solo funciona en la sesión de Colab de quien lo escribió, con celdas ejecutadas en desorden | Se ejecuta de arriba abajo, pero con ayuda del equipo o sin semillas fijas | Otra persona hace *Reiniciar y ejecutar todo* y obtiene **el mismo `k`, los mismos tamaños y la misma tabla de RMSE y precision@3**; cada persona ha subido su parte, sin claves ni datos personales | Además, el cuaderno empieza con una celda de texto que explica cómo ejecutarlo y con las versiones de Python y de las bibliotecas |
| **Análisis y comunicación al cliente** (¿lo entiende quien no programa?) | Solo hay cifras o gráficos, sin interpretar y sin nombres de segmento | La ficha tiene nombre, tamaño, perfil y **una acción comercial** por segmento | Además, cada nombre se apoya en **dos cifras** del perfil, los tamaños suman 1.200, hay una experiencia estrella por segmento y la frase del `k` da la razón técnica y la de negocio | Además, prioriza los segmentos por valor, explica los límites (datos sintéticos, lo que el 2D no recoge) y dice qué haría con un huésped nuevo |
| **IA responsable** (¿se sabe qué hizo la IA y qué comprobasteis?) | No hay nota, o no dice si se ha usado IA | Hay nota de 5 líneas con riesgos genéricos y se dice que se ha usado IA | Al menos **2 riesgos específicos** de este caso, cada uno con su medida, y se dice **qué se pidió a la IA y qué se comprobó** | Además, comprueba una medida con los datos (por ejemplo, que el recomendador no repite siempre las mismas experiencias) y explica el arranque en frío |

**Cómo se revisa** (unos 10 minutos, antes de subir; lo hace **una persona que no escribió esa parte**):

1. **Ejecutar** el cuaderno en Colab con *Entorno de ejecución → Reiniciar y ejecutar todo*. Anotar si algo falla y si salen los mismos `k`, tamaños y tabla de RMSE y precision@3 que cuenta la ficha.
2. **Leer la ficha como si fuera Lucía**: ¿se entiende qué es cada segmento y qué hacer con él? ¿Los tamaños suman 1.200? Subrayar lo que no se entienda.
3. **Mirar el cuaderno**: ¿se escala antes de agrupar? ¿Se evalúa el recomendador con valoraciones escondidas? ¿`recomendar` no devuelve nada ya valorado? ¿Está dicho dónde se ha usado la IA? Que quien lo escribió explique cualquier celda.
4. **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba** (por ejemplo: «3 · el cuaderno se ejecuta entero y salen k = 4 y los mismos tamaños, pero falta probar `recomendar` con un tercer usuario»). Sin prueba escrita, el nivel no vale.
5. **Apuntar el resultado** en la sección «Revisión con la rúbrica» del final de `ficha_segmentos.md` y corregir lo más fácil de arreglar. Lo demás se anota como mejora.

Cada persona, además, se puntúa a sí misma en su hoja de [autoevaluación y coevaluación](../4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md) con **esta misma rúbrica**.

---

### 4 · 🪜 Guía paso a paso

Son cinco pasos, de **105 minutos en total** (unos 45 el día 1 y unos 60 el día 2; el aula da 45 y 50, así que lo que no quepa va a casa). Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa.

#### Paso 1 · Preparar el cuaderno y los datos (día 1, 10 minutos)
1. Crear en Colab el cuaderno `reto_S09_conocer_al_huesped.ipynb`.
2. Cargar `huespedes.csv` y mirar sus columnas.
3. Escalar las variables numéricas.
4. Repartir el trabajo de los pasos 2 y 3.

**Cómo se hace**
- **Crear el cuaderno.** En Colab: *Archivo → Cuaderno nuevo* y cambiadle el nombre a `reto_S09_conocer_al_huesped`. Trabajad en una sola pantalla compartida o compartid el cuaderno con el botón *Compartir* de Colab.
- **Cargar los datos.** Copiad al principio la celda «Preparación» de `S09_01` (la que define `dato(...)` y descarga los datos) y las importaciones. Fijad una semilla una sola vez, `SEMILLA = 42`, y usadla siempre que pidan `random_state`.
- **Mirar las columnas.** Con `head()` y `describe()`: `id_huesped` es solo un identificador y las otras 7 son números (`viaja_con_ninos` solo vale 0 o 1). Fijaos en las escalas: la edad va de 18 a 75 y el gasto diario, de 35 a 340.
- **Escalar.** Quitad `id_huesped` y pasad las 7 columnas por `StandardScaler().fit_transform(...)`: así todas pesan lo mismo. Guardad el resultado como `X`. Sin escalar, el gasto en euros mandaría sobre las demás.

**Qué deberíais ver.** Una tabla de 1200 filas y 8 columnas (el identificador y las 7 variables) y una matriz `X` de 1200 filas y 7 columnas, con la media de cada columna cerca de 0.

**Hecho cuando:** `X` existe y está escalada, y cada persona sabe qué parte del paso 2 o del 3 le toca.

#### Paso 2 · Segmentar y elegir k (día 1, 20 minutos)
1. Probar k-means con `k` de 2 a 8.
2. Calcular la silueta de cada `k` y dibujar la curva.
3. Elegir `k` con una razón técnica **y** una de negocio.
4. Escribir esa razón en una frase.

**Cómo se hace.** Es el mismo trabajo del ejercicio 2 de `S09_01`: podéis copiar de ahí la idea y adaptarla a vuestro cuaderno.

| Orden | Qué hacéis | Pista |
|---|---|---|
| 1 | Para cada `k` de 2 a 8, entrenar k-means sobre `X` | `KMeans(n_clusters=k, n_init=10, random_state=SEMILLA)` |
| 2 | Guardar la silueta media de cada `k` en un diccionario | `silhouette_score(X, etiquetas)`; va de −1 a 1 y **más alto es mejor** |
| 3 | Dibujar la curva: `k` en el eje horizontal y silueta en el vertical | Título y nombres de ejes, como en `S09_01` |
| 4 | Preguntaos si Lucía puede actuar con ese número de grupos | Entre 3 y 5 segmentos suele ser manejable; 12 no lo serían |
| 5 | Escribir **una frase con las dos razones** y ponerla en el cuaderno y en la cabecera de la ficha | «Elegimos k = … porque la silueta es … y, para el negocio, … grupos se pueden gestionar» |

**Qué deberíais ver.** Una curva con siluetas para `k` = 2, 3, …, 8 y un `k` elegido entre 3 y 5 (en `S09_01` el de mejor silueta cae en ese rango). No elijáis `k` **solo** por el número más alto de la silueta.

**Hecho cuando:** hay curva de silueta, un `k` elegido y la frase con las dos razones.

#### Paso 3 · Mapa PCA e interpretación de los segmentos (día 1, 15 minutos)
1. Dibujar el mapa 2D con PCA, con los segmentos coloreados.
2. Calcular el perfil medio de cada segmento y su tamaño.
3. Ponerle nombre a cada segmento, con cifras.
4. Proponer una acción comercial por segmento.

**Cómo se hace**
- **El mapa.** Entrenad `k-means` con el `k` elegido y guardad el grupo de cada huésped. Aplicad `PCA(n_components=2)` sobre `X` y dibujad un diagrama de dispersión coloreado por grupo (es el ejercicio 2 de `S09_02`). Los ejes llevan el **% de varianza** de cada componente (`explained_variance_ratio_`) y el título dice una **conclusión** («Cuatro tipos de huésped bastante separados»). Con 2 componentes se conserva solo una parte de la información (en `S09_02` salía cerca del 69 %): si el mapa sale mezclado, decidlo en la ficha.
- **El perfil.** Con `groupby` calculad la media de cada variable por grupo y el número de huéspedes. Comparad cada media con la media general; el mapa de calor de `S09_01` ayuda.
- **El nombre.** Cada nombre se apoya en **dos cifras** del perfil. Ejemplo de la plantilla: «Familias de larga estancia · 410 (34 %) · 9 de cada 10 viajan con niños, reservan con 110 días de antelación y gastan poco en actividades». Los tamaños de todos los segmentos suman 1.200.
- **La acción comercial.** Una por segmento: qué enseñar, cuándo y por qué canal. La IA puede sugerir nombres, pero el nombre tiene que reflejar vuestras cifras.

**Qué deberíais ver.** Un mapa con un color por segmento y el % de varianza en los ejes, y una tabla con el perfil medio de cada segmento: nombre, tamaño, dos o tres cifras y una acción.

**Hecho cuando:** el mapa está dibujado y cada segmento tiene nombre, tamaño, perfil con cifras y una acción.

#### Paso 4 · Recomendador de experiencias (día 2, 30 minutos)
1. Separar valoraciones de entrenamiento y de prueba.
2. Montar al menos dos métodos y evaluarlos con RMSE y precision@3.
3. Programar `recomendar(id_usuario, n)`.
4. Probarla con 3 usuarios.

**Cómo se hace.** Es el trabajo de `S09_03`: reutilizad su código y comprobad que lo entendéis.

| Orden | Qué hacéis | Pista |
|---|---|---|
| 1 | Esconder el 20 % de las valoraciones como prueba y construir la matriz usuario × experiencia solo con el 80 % restante | `valoraciones.sample(frac=0.2, random_state=SEMILLA)`; las casillas vacías son `NaN` |
| 2 | Primer método: **popularidad** (la nota media de cada experiencia, igual para todos) | Es la referencia que hay que batir y la única opción para un huésped nuevo (*arranque en frío*) |
| 3 | Segundo método: **contenido** (se hace en clase en `S09_03`) o, si lo habéis hecho en casa, filtrado colaborativo o factorización | Cualquiera sirve, pero tiene que ser distinto de la popularidad |
| 4 | Medir los dos con **RMSE** (error de la nota, menos es mejor) y **precision@3** (de las 3 recomendadas, cuántas le gustaban, más es mejor) | Con pocos usuarios evaluables, una diferencia de 0,01 es ruido: no la vendáis como mejora |
| 5 | Una tabla *método · RMSE · precision@3* y una frase que explica cuál elegís | «Elegimos … porque su precision@3 es …» |
| 6 | Programar `recomendar(id_usuario, n)`: las `n` mejores experiencias **que el usuario no ha valorado**, con nombre, categoría, isla y nota prevista | Poned `-inf` en lo ya valorado antes de ordenar; es el mini-reto de `S09_03` |

Probad `recomendar` con **3 usuarios distintos** y comprobad dos cosas: que ninguna experiencia recomendada estaba ya valorada y que las recomendaciones cambian de una persona a otra. Solo los usuarios 1 a 300 tienen valoraciones.

**Qué deberíais ver.** La tabla comparativa de los dos métodos, la frase de elección y tres listas de `n` experiencias, distintas entre sí.

**Hecho cuando:** el recomendador está evaluado con valoraciones escondidas, `recomendar` funciona con 3 usuarios y no propone nada ya valorado.

#### Paso 5 · Ficha, IA responsable, revisión y entrega (día 2, 30 minutos)
1. Rellenar la ficha de segmentos y la nota de IA responsable.
2. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado en la ficha.
3. Dejar el cuaderno ejecutable y subir los ficheros a `sprint-09/`.
4. Ensayar 3 minutos de review.

**Cómo se hace**
- **La ficha.** Copiad el texto de `plantilla_ficha_segmentos.md` en un archivo nuevo `ficha_segmentos.md` y rellenad cada sección:

| Sección de la plantilla | Qué escribís |
|---|---|
| Cabecera | Equipo, método, `k`, silueta y la frase de las dos razones del paso 2 |
| Mapa de segmentos | La imagen del mapa (`mapa_pca.png`, subida junto a la ficha) o dónde está en el cuaderno |
| Segmentos | Una fila por segmento: nombre, tamaño, perfil con cifras, acción y **experiencia estrella** (la que recomienda vuestro prototipo a huéspedes de ese grupo; probad con huéspedes con `id_huesped` entre 1 y 300, que son los que tienen valoraciones) |
| Recomendador | Los dos métodos con su RMSE y precision@3, el elegido y un ejemplo con un usuario; qué haría el sistema con un huésped nuevo sin valoraciones |
| IA responsable | Cinco líneas con **al menos 2 riesgos específicos** de este caso, cada uno con su medida (ejemplos justo debajo de la tabla) |
| Limitaciones | Datos sintéticos, comportamiento de un año, pocas valoraciones por persona, y las vuestras |

- **Nota de IA responsable.** Ejemplos, para que elijáis los que valen para **vuestro** caso: *discriminar* (si se usan la edad o «viaja con niños» para fijar precios; medida: usar la segmentación para comunicar, no para variar precios); *sesgo de popularidad* (las experiencias poco conocidas casi no se recomiendan; medida: reservar un hueco a opciones menos populares); *privacidad* (se combinan datos de reserva y valoraciones; medida: usar identificadores y no mostrar datos personales).
- **Declarar la IA.** En el cuaderno, una celda de texto que diga dónde la habéis usado y qué habéis comprobado a mano.
- **La revisión con la rúbrica (10 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» (apartado 3) y rellena la sección «Revisión con la rúbrica» del final de `ficha_segmentos.md`: un nivel de 1 a 4 por criterio y **una frase de prueba**. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos». Si sobran minutos, empezad algún extra.
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). (1) En Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y después *Archivo → Descargar → Descargar .ipynb*. (2) Abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-09`**. (3) *Add file → Upload files*, arrastrad los ficheros, escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace. Un reparto posible: la persona A sube el cuaderno («Añado segmentación y recomendador»), la B sube la ficha y el mapa («Añado ficha de segmentos»), y cada persona sube su autoevaluación. Nombres de archivo **sin espacios ni tildes**.

**Qué deberíais ver.** En la carpeta `sprint-09` del repositorio, el cuaderno y la ficha del equipo (y el mapa, si lo habéis puesto) y una hoja de autoevaluación por persona (**2 + N**); y en el historial (el icono del reloj), *commits* de todas las personas del equipo.

**Hecho cuando:** otra persona podría repetir el cuaderno de arriba abajo, la sección «Revisión con la rúbrica» está rellena y cada persona ha subido algo con su cuenta.

**Después, 40 minutos de entrega, review y retrospectiva:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-09/`, y el equipo presenta en 3 minutos **sus segmentos (nombre y acción)** y **una recomendación concreta para un usuario**. Se comparan los `k` elegidos y se discute: *¿es el mismo cliente aunque le pongamos otro nombre?*

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **inventa con mucha seguridad**: un nombre de segmento que suena bien pero no refleja las cifras es un error. Reglas:
- **Todo lo que dé, lo comprobáis y lo entendéis.** Si el docente pregunta por una celda, tenéis que saber explicarla; en la review puede preguntar a cualquiera.
- **Los datos mandan:** si un nombre o una conclusión de la IA no cuadra con vuestras cifras, no vale.
- **Declaradlo** en el cuaderno: dónde la habéis usado y qué habéis comprobado.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender un concepto | «Explícame k-means y la silueta con una analogía de personas en una fiesta» | Que podéis explicarlo con vuestras palabras |
| Entender PCA | «¿Qué significa que PCA conserve el 60 % de la varianza? Dame un ejemplo sin fórmulas» | Que vuestro gráfico dice lo mismo |
| Poner nombres a los segmentos | «Dado este perfil medio: *[tabla]*, dame 5 nombres comerciales cortos y evocadores» | Que el nombre refleja las **cifras** del segmento, no una invención |
| Pensar en riesgos | «¿Qué riesgos tiene recomendar experiencias según la edad?» | Elegid los que aplican a **vuestro** caso y dad una medida real |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Agrupar sin escalar | Se olvida | Escalad **antes** del clustering |
| Elegir `k` solo con la silueta | «Es lo que dice el número» | Añadid el criterio de negocio |
| Poner nombres sin mirar los datos | Suena bien | Cada nombre debe justificarse con **dos cifras** del perfil |
| Recomendar lo que el usuario ya ha valorado | No se filtra | La función debe excluirlas |
| Evaluar el recomendador con los mismos datos que usó | «Es lo más fácil» | Probad con valoraciones **escondidas** |
| Nota de IA responsable genérica | Prisa | Dos riesgos **concretos** de este caso, con medida |
| El cuaderno falla al ejecutarlo de nuevo | Celdas ejecutadas en desorden o semillas sin fijar | *Reiniciar y ejecutar todo* antes de subirlo y usar siempre la misma `SEMILLA` |

#### Ayuda 3 · Si os atascáis

1. **Todos los segmentos se parecen:** revisad que habéis escalado y probad otras columnas; quizá algunas no aportan.
2. **El mapa PCA sale con todo mezclado:** es posible; decidlo en la ficha. Los grupos pueden estar separados en dimensiones que el 2D no recoge.
3. **El recomendador recomienda siempre lo mismo:** probablemente es un sesgo de popularidad; comentadlo como riesgo.
4. Repasad el cuaderno de ese paso y su código explicado; preguntad al equipo y, después, al docente. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
