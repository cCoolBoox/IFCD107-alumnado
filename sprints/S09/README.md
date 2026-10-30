# README Sprint S09 · Segmentar, recomendar y aprender por refuerzo

**Pregunta guía:** ¿qué tipos de cliente tenemos y qué les ofrecemos?  
**Fechas:** 13 y 16 de noviembre · **Horas:** 12 h (2 h teoría · 6 h práctica · 4 h PBL)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_09.pdf) · [ecofriendly](pdf/README_Sprint_09_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. Agrupar clientes sin etiquetas con **k-means, clustering jerárquico y DBSCAN**, y elegir cuántos grupos con el **coeficiente de silueta**.
2. Reducir dimensiones con **PCA** para ver los datos en 2D e interpretar qué variables pesan.
3. Construir recomendadores por **popularidad, contenido y filtrado colaborativo** (incluida la factorización de matrices) y evaluarlos con **RMSE** y **precision@k**.
4. Entender el **aprendizaje por refuerzo** implementando **Q-learning** en un entorno pequeño con numpy.
5. **Interpretar** un resultado no supervisado para el negocio: poner nombre, tamaño y una acción comercial a cada segmento.

## Día 1 · Viernes 13/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «Conocer al huésped» y reparto de roles | — | 10 |
| ☐ | 📖 Teoría · Clustering y PCA | [Presentación S09.1](1_Teoria/S09.1_Clustering_y_PCA.pdf) | 30 |
| ☐ | 💻 Práctica · Segmentar huéspedes: k-means, silueta, jerárquico y DBSCAN (los ejercicios marcados «en clase») | [Cuaderno S09_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_01_clustering.ipynb) | 45 |
| ☐ | 💻 Práctica · PCA: varianza explicada y mapa en 2D (los ejercicios marcados «en clase») | [Cuaderno S09_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_02_pca.ipynb) | 30 |
| ☐ | 🎯 Reto · Arrancar el reto: preparar datos, segmentar y elegir `k`, mapa PCA (pasos 1–3) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_09_una_pagina.md) | 45 |
| ☐ | 📖 Teoría · Sistemas de recomendación | [Presentación S09.2](1_Teoria/S09.2_Sistemas_de_recomendacion.pdf) | 25 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 15 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Mi equipo tiene los segmentos en borrador y ha elegido `k`.
- [ ] Sé qué indica la silueta y la varianza explicada.

## Día 2 · Lunes 16/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 💻 Práctica · Recomendadores: popularidad, contenido, colaborativo y factorización (los ejercicios marcados «en clase») | [Cuaderno S09_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_03_recomendadores.ipynb) | 50 |
| ☐ | 📖 Teoría · Aprendizaje por refuerzo (visión conceptual) | [Presentación S09.3](1_Teoria/S09.3_Aprendizaje_por_refuerzo.pdf) | 15 |
| ☐ | 💻 Práctica · Q-learning en el hotel (demostración guiada) | [Cuaderno S09_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/2_Practica/S09_04_q_learning.ipynb) | 25 |
| ☐ | 🎯 Reto · Recomendador, ficha de segmentos, IA responsable y ensayo (pasos 4–5) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_09_una_pagina.md) | 50 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 20 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-09/`, autoevaluación y coevaluación, review (3 min por equipo) y retrospectiva | — | 40 |

**En clase: 3 h 20 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** Lucía, la directora comercial de TurisData, envía **la misma newsletter a sus 1.200 huéspedes** y vende las **25 experiencias** con los mismos banners. Sospecha que hay «tipos» de cliente muy distintos y que cada uno querría cosas diferentes. Os pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno.»*

**Qué vais a entregar:** un cuaderno, una ficha de segmentos de 1 página y una nota de IA responsable (dentro de la ficha).

**Núcleo y extra.** Núcleo: segmentos con `k` justificado y su ficha, y un recomendador sencillo. Extra: otros algoritmos de agrupación y el aprendizaje por refuerzo (que se ve en demostración).

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_09_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_09.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-09/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `reto_S09_conocer_al_huesped.ipynb` · lo creáis
- [ ] `ficha_segmentos.md` · lo creáis a partir de una plantilla
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-09/`: 2 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 5). Aparte: mapa_pca.png; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Variables escaladas antes de agrupar; mapa PCA con % de varianza en los ejes
- [ ] Recomendador evaluado con RMSE y precision@3 frente a la popularidad
- [ ] Cada persona del equipo ha hecho *commit* de su parte
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_09.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_clustering_recomendadores_y_refuerzo.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_09.md).
2. Mira el [código explicado](2_Practica/codigo_explicado/README.md) del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`; sus PDF (color y ecofriendly) están en la subcarpeta `pdf/`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Reto_en_una_pagina` · `2_Ficha_completa` · `3_Laminas` · `4_Plantillas_y_entrega` |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| UD 3.9 | Clustering: k-means, jerárquico, DBSCAN |
| UD 3.10 | Reducción de dimensionalidad: PCA (mención de t-SNE) |
| UD 3.11 | Sistemas de recomendación (contenido, colaborativo, factorización) |
| UD 3.12 | Introducción al aprendizaje por refuerzo (Q-learning con Gymnasium) |

**Y ahora:** Sprint 10 · Redes neuronales bien entrenadas (martes 17/11).

*12 h (2 h teoría · 6 h práctica · 4 h PBL).*
