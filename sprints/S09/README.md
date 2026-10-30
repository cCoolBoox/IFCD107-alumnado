# README Sprint S09 · Segmentar, recomendar y aprender por refuerzo

**Pregunta guía:** ¿qué tipos de cliente tenemos y qué les ofrecemos?
**Fechas:** 13 y 16 de noviembre · **Horas:** 12 h (2 h teoría · 6 h práctica · 4 h PBL)
**Módulo:** M3, unidades 3.9 a 3.12 · **Evaluación:** test de M3 (segunda parte)

📄 **Este README en PDF:** [a color](README_Sprint_09.pdf) · [ecofriendly, para imprimir](README_Sprint_09_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. Agrupar clientes sin etiquetas con **k-means, clustering jerárquico y DBSCAN**, y elegir cuántos grupos con el **coeficiente de silueta**.
2. Reducir dimensiones con **PCA** para ver los datos en 2D e interpretar qué variables pesan.
3. Construir recomendadores por **popularidad, contenido y filtrado colaborativo** (incluida la factorización de matrices) y evaluarlos con **RMSE** y **precision@k**.
4. Entender el **aprendizaje por refuerzo** implementando **Q-learning** en un entorno pequeño con numpy.
5. **Interpretar** un resultado no supervisado para el negocio: poner nombre, tamaño y una acción comercial a cada segmento.

## Requisitos previos
- Pipelines y validación de scikit-learn (Sprints 7 y 8), y numpy/pandas (Sprints 4-5).
- Saber leer un mapa de calor y un diagrama de dispersión.
- Datos: `huespedes.csv`, `valoraciones_experiencias.csv` y `experiencias.csv` (los notebooks los descargan solos).

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_09.pdf) · [ecofriendly](guia/Guia_Sprint_09_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [**Carpeta del reto: `Reto_S09/`**](Reto_S09/) | Todo el material del reto junto: ficha (.md y PDF), plantillas y material de apoyo, hoja de autoevaluación y coevaluación y láminas del reto | — | Antes del planning y durante el reto |
| [Reto completo, paso a paso (.md)](Reto_S09/Reto_Sprint_09.md) · [PDF](Reto_S09/Reto_Sprint_09.pdf) · [ecofriendly](Reto_S09/Reto_Sprint_09_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S09_00_resumen_del_sprint.png) | Lámina con la pregunta guía, qué aprenderás, cómo se reparte el sprint (teoría, práctica y reto) y dónde estás en el curso | — | Antes del planning |
| [El reto paso a paso](Reto_S09/S09_03_reto_paso_a_paso.png) · [PDF con enlaces](Reto_S09/S09_03_reto_paso_a_paso.pdf) | Los pasos del reto con su día y minutos, el material de cada paso, los errores frecuentes y el uso de la IA | — | Durante el reto |
| [Esquema del contenido y su relación con el reto](infografias/S09_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del sprint](infografias/) | 3 láminas ilustradas | — | Antes del planning y durante el reto |
| [Atlas de algoritmos](infografias/S09_03_atlas_no_supervisado_y_refuerzo.png) | Atlas de algoritmos del sprint: k-means, jerárquico, DBSCAN, PCA, recomendadores y Q-learning | — | Teoría y práctica; consulta cuando elijas modelo |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S09.1_Clustering_y_PCA.pdf`](presentaciones/S09.1_Clustering_y_PCA.pdf) | Clustering y PCA | 30 min | Teoría · día 1 del S09 |
| [`S09.2_Sistemas_de_recomendacion.pdf`](presentaciones/S09.2_Sistemas_de_recomendacion.pdf) | Sistemas de recomendación | 10 min | Teoría · día 2 del S09 |
| [`S09.3_Aprendizaje_por_refuerzo.pdf`](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf) | Aprendizaje por refuerzo (visión conceptual) | 10 min | Teoría · día 2 del S09 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| [`apuntes_clustering_recomendadores_y_refuerzo.md`](actividades/apuntes_clustering_recomendadores_y_refuerzo.md) · [PDF](actividades/apuntes_clustering_recomendadores_y_refuerzo.pdf) · [ecofriendly](actividades/apuntes_clustering_recomendadores_y_refuerzo_ecofriendly.pdf) | **Apuntes que complementan las diapositivas**: k-means, silueta, DBSCAN, PCA, recomendadores (popularidad, contenido, colaborativo) y Q-learning explicados con ejemplos que puedes calcular a mano | — | Antes del sprint y cuando tengas dudas |
| `S09_01_clustering` | Segmentar huéspedes: escalado, k-means, silueta, jerárquico, DBSCAN | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_01_clustering.ipynb) |
| `S09_02_pca` | PCA: varianza explicada, mapa 2D, cargas, mención a t-SNE | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_02_pca.ipynb) |
| `S09_03_recomendadores` | Popularidad, contenido, colaborativo, factorización; RMSE y precision@k | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_03_recomendadores.ipynb) |
| `S09_04_q_learning` | Q-learning en el hotel (numpy): recompensas, epsilon-greedy, política | 30 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_04_q_learning.ipynb) |

Cada notebook tiene comprobaciones automáticas (✔). Trabaja en orden: no pases al siguiente hasta que los `assert` pasen. Los datos se descargan solos.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Día 1 del S09**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Conocer al huésped» y reparto de roles | 10 min |
| 2 | 📖 Teoría | [Clustering y PCA](presentaciones/S09.1_Clustering_y_PCA.pdf) | 30 min |
| 3 | 💻 Práctica | [Segmentar huéspedes: k-means, silueta, jerárquico y DBSCAN (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_01_clustering.ipynb) | 40 min |
| 4 | 💻 Práctica | [PCA: varianza explicada y mapa en 2D (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_02_pca.ipynb) | 30 min |
| 5 | 🎯 Reto | [Arrancar el reto: preparar datos, segmentar y elegir `k`, mapa PCA (pasos 1–3)](Reto_S09/Reto_Sprint_09.md) | 45 min |
| 6 | 📖 Teoría | [Sistemas de recomendación](presentaciones/S09.2_Sistemas_de_recomendacion.pdf) | 25 min |
| 7 | 💻 Práctica | Terminad los cuadernos pendientes y poneos al día | 20 min |

**Día 2 del S09**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 8 | 💻 Práctica | [Recomendadores: popularidad, contenido, colaborativo y factorización (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_03_recomendadores.ipynb) | 40 min |
| 9 | 📖 Teoría | [Aprendizaje por refuerzo (visión conceptual)](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf) | 15 min |
| 10 | 💻 Práctica | [Q-learning en el hotel (demostración guiada)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_04_q_learning.ipynb) | 20 min |
| 11 | 🎯 Reto | [Recomendador, ficha de segmentos, IA responsable y ensayo (pasos 4–5)](Reto_S09/Reto_Sprint_09.md) | 50 min |
| 12 | 💻 Práctica | Terminad los cuadernos pendientes y poneos al día | 35 min |
| 13 | 🔔 Ceremonia | Entrega en `sprint-09/`, autoevaluación y coevaluación, review (3 min por equipo) y retrospectiva | 40 min |

<!--orden:fin-->

## Reto · «Conocer al huésped»

📄 [Reto en PDF](Reto_S09/Reto_Sprint_09.pdf) · [ecofriendly](Reto_S09/Reto_Sprint_09_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](Reto_S09/Reto_Sprint_09.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** Lucía, directora comercial de TurisData Canarias, envía la misma newsletter a sus 1 200 huéspedes y vende 25 experiencias con los mismos banners. Pide: «Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno».


**Entregáis** (carpeta `sprint-09/` del repositorio del equipo):
- `reto_S09_conocer_al_huesped.ipynb`: segmentación de `huespedes.csv` (`k` con silueta y criterio de negocio), mapa 2D con PCA y `recomendar(id_usuario, n)`.
- Ficha de segmentos (1 página): nombre, tamaño, perfil, una acción y una experiencia estrella por segmento. Plantilla: [`plantilla_ficha_segmentos.md`](Reto_S09/plantilla_ficha_segmentos.md).
- Nota de IA responsable (5 líneas) dentro de la ficha.


**Reglas:**
- Unas 2 h 20 min en equipos de 3-4; solo numpy, pandas, matplotlib/seaborn y scikit-learn. Todas las personas deben poder explicar cualquier parte.
- Mínimo dos recomendadores comparados con RMSE y precision@3; `recomendar` no propone lo ya valorado.
- Nunca claves ni datos personales. Review: 3 min por equipo.


**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (sesgo de popularidad, discriminación por edad o niños, privacidad), más segmentos con sentido de negocio.

## ✅ Antes de cerrar el sprint
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Variables escaladas antes de agrupar; mapa PCA con % de varianza en los ejes
- [ ] Recomendador evaluado con RMSE y precision@3 frente a la popularidad
- [ ] Cada persona del equipo ha hecho *commit* de su parte
- [ ] Entregable subido a la carpeta `sprint-09/` del repositorio del equipo
- [ ] [Autoevaluación y coevaluación](Reto_S09/autoevaluacion_y_coevaluacion.md) rellenadas
