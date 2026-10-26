# Material por sprint

Cada carpeta `Sxx/` tiene **un `README.md`** (la guía del sprint con la ficha del reto), que también está en PDF (`README_Sprint_XX.pdf`, a color, y `README_Sprint_XX_ecofriendly.pdf`, para imprimir) y **subcarpetas** con el resto:

| Subcarpeta | Qué contiene |
|---|---|
| `Reto_SXX/` | **Todo el material del reto junto**: la ficha del reto explicada paso a paso (`Reto_Sprint_XX.md` y PDF), las plantillas, la hoja de `autoevaluacion_y_coevaluacion.md` y las láminas del reto (`SXX_02_…`, `SXX_03_reto_paso_a_paso`) |
| `guia/` | La guía del sprint en PDF (`Guia_Sprint_XX.pdf`) y su versión `_ecofriendly` para imprimir con poca tinta |
| `presentaciones/` | Diapositivas de cada sesión |
| `notebooks/` | Prácticas para abrir en Google Colab |
| `actividades/` | Material de las actividades y ejercicios, con sus scripts y ficheros de apoyo |
| `tests/` | Test de conocimientos (solo se abre el día indicado) |

Un sprint solo tiene las subcarpetas que necesita. Empieza siempre por el `README.md` del sprint: tiene la sección *📎 Material del sprint* con todos los enlaces.
Los notebooks se abren en **Google Colab** con la insignia de la primera celda de cada uno; los datos se descargan solos desde la carpeta [`../datos`](../datos).

| Sprint | Tema | Fechas | Notebooks | Guía |
|---|---|---|---|---|
| 0 | Arranque ágil | 16–19/10 | – | [S00](S00) |
| 1 | Qué es la IA y cómo usarla bien | 20–21/10 | – | [S01](S01) |
| 2 | Matemáticas y estadística | 22–23/10 | – | [S02](S02) |
| 3 | Del dato al modelo | 26–27/10 | NoSQL | [S03](S03) |
| 4 | Python para IA | 28–29/10 | 5 | [S04](S04) |
| 5 | Matemáticas y estadística en código | 30/10 y 3/11 | 7 | [S05](S05) |
| 6 | Datos listos para modelar | 4–5/11 | 4 | [S06](S06) |
| 7 | ML supervisado | 6 y 9/11 | 5 | [S07](S07) |
| 8 | Árboles, ensembles y SVM | 10–11/11 | 6 | [S08](S08) |
| 9 | Segmentar, recomendar y refuerzo | 12–13/11 | 4 | [S09](S09) |
| 10 | Redes neuronales | 16–17/11 | 4 | [S10](S10) |
| 11 | Visión por computador | 18–20/11 | 4 | [S11](S11) |
| 12 | Lenguaje, series y generativos | 23–25/11 | 7 | [S12](S12) |
| 13 | Contar lo que hace el modelo | 25/11 (dentro del 12) | 2 | [S13](S13) |
| 14–17 | Proyecto final | 26/11–14/12 | 2 | [S14](S14) · [S15](S15) · [S16](S16) · [S17](S17) |

**Cómo trabajar un notebook:** ábrelo en Colab, ejecuta la primera celda, completa los huecos marcados con `# TODO` (sustituye `...`) y ejecuta las celdas de comprobación (`assert`): si fallan, te dicen qué revisar. Las soluciones no se publican.

> 💡 **Los PDF, descargados:** la vista previa de GitHub no abre los enlaces de un PDF. Descárgalo (**Download**) y ábrelo con tu lector de PDF para que funcionen.
