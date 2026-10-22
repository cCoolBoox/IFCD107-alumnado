# README Sprint S09 · Segmentar, recomendar y aprender por refuerzo

**Pregunta guía:** ¿qué tipos de cliente tenemos y qué les ofrecemos?
**Fechas:** 12 y 13 de noviembre · **Horas:** 12 h (3 h teoría · 5 h práctica · 4 h PBL)
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
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_09.md) · [PDF](guia/Reto_Sprint_09.pdf) · [ecofriendly](guia/Reto_Sprint_09_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Infografías del reto](infografias/) | 2 láminas ilustradas del reto | — | Reto |
| [Atlas de algoritmos](infografias/S09_03_atlas_no_supervisado_y_refuerzo.png) | Atlas de algoritmos del sprint: k-means, jerárquico, DBSCAN, PCA, recomendadores y Q-learning | — | Teoría y práctica; consulta cuando elijas modelo |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S09.1_Clustering_y_PCA.pdf`](presentaciones/S09.1_Clustering_y_PCA.pdf) | Clustering y PCA | 30 min | Teoría · jueves 12/11 |
| [`S09.2_Sistemas_de_recomendacion.pdf`](presentaciones/S09.2_Sistemas_de_recomendacion.pdf) | Sistemas de recomendación | 10 min | Teoría · viernes 13/11 |
| [`S09.3_Aprendizaje_por_refuerzo.pdf`](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf) | Aprendizaje por refuerzo (visión conceptual) | 10 min | Teoría · viernes 13/11 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S09_01_clustering` | Segmentar huéspedes: escalado, k-means, silueta, jerárquico, DBSCAN | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_01_clustering.ipynb) |
| `S09_02_pca` | PCA: varianza explicada, mapa 2D, cargas, mención a t-SNE | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_02_pca.ipynb) |
| `S09_03_recomendadores` | Popularidad, contenido, colaborativo, factorización; RMSE y precision@k | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_03_recomendadores.ipynb) |
| `S09_04_q_learning` | Q-learning en el hotel (numpy): recompensas, epsilon-greedy, política | 30 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_04_q_learning.ipynb) |

Cada notebook tiene comprobaciones automáticas (✔). Trabaja en orden: no pases al siguiente hasta que los `assert` pasen. Los datos se descargan solos.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Jueves 12/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Conocer al huésped» y reparto de roles | 10 min |
| 2 | 📖 Teoría | [Clustering y PCA](presentaciones/S09.1_Clustering_y_PCA.pdf) | 30 min |
| 3 | 💻 Práctica | [Segmentar huéspedes: k-means, silueta, jerárquico y DBSCAN](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_01_clustering.ipynb) | 55 min |
| 4 | 💻 Práctica | [PCA: varianza explicada y mapa en 2D](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_02_pca.ipynb) | 40 min |
| 5 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 15 min |
| 6 | 🎯 Reto | [Arrancar el reto: preparar datos, segmentar y elegir `k`, mapa PCA (pasos 1–3)](guia/Reto_Sprint_09.md) | 50 min |

**Viernes 13/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 7 | 📖 Teoría | [Sistemas de recomendación](presentaciones/S09.2_Sistemas_de_recomendacion.pdf) | 10 min |
| 8 | 📖 Teoría | [Aprendizaje por refuerzo (visión conceptual)](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf) | 10 min |
| 9 | 💻 Práctica | [Recomendadores: popularidad, contenido, colaborativo y factorización](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_03_recomendadores.ipynb) | 1 h |
| 10 | 💻 Práctica | [Q-learning en el hotel (demostración guiada)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_04_q_learning.ipynb) | 30 min |
| 11 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 10 min |
| 12 | 🎯 Reto | [Recomendador, ficha de segmentos, IA responsable y ensayo (pasos 4–5)](guia/Reto_Sprint_09.md) | 40 min |
| 13 | 🔔 Ceremonia | Entrega en `sprint-09/`, autoevaluación y coevaluación, review (3 min por equipo) y retrospectiva | 40 min |

<!--orden:fin-->

## Reto · «Conocer al huésped»

📄 [Reto en PDF](guia/Reto_Sprint_09.pdf) · [ecofriendly](guia/Reto_Sprint_09_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_09.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** Lucía, directora comercial de TurisData Canarias, envía la misma newsletter a sus 1 200 huéspedes y vende 25 experiencias con los mismos banners. Pide: «Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno».


**Entregáis** (carpeta `sprint-09/` del repositorio del equipo):
- `reto_S09_conocer_al_huesped.ipynb`: segmentación de `huespedes.csv` (`k` con silueta y criterio de negocio), mapa 2D con PCA y `recomendar(id_usuario, n)`.
- Ficha de segmentos (1 página): nombre, tamaño, perfil, una acción y una experiencia estrella por segmento. Plantilla: [`plantilla_ficha_segmentos.md`](plantillas/plantilla_ficha_segmentos.md).
- Nota de IA responsable (5 líneas) dentro de la ficha.


**Reglas:**
- Unas 3 h 20 min en equipos de 3-4; solo numpy, pandas, matplotlib/seaborn y scikit-learn. Todas las personas deben poder explicar cualquier parte.
- Mínimo dos recomendadores comparados con RMSE y precision@3; `recomendar` no propone lo ya valorado.
- Nunca claves ni datos personales. Review: 3 min por equipo.


**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (sesgo de popularidad, discriminación por edad o niños, privacidad), más segmentos con sentido de negocio.

## ✅ Antes de cerrar el sprint
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Variables escaladas antes de agrupar; mapa PCA con % de varianza en los ejes
- [ ] Recomendador evaluado con RMSE y precision@3 frente a la popularidad
- [ ] Cada persona del equipo ha hecho *commit* de su parte
- [ ] Entregable subido a la carpeta `sprint-09/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
