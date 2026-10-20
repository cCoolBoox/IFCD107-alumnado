# Sprint 9 · Segmentar, recomendar y aprender por refuerzo

**Pregunta guía:** ¿qué tipos de cliente tenemos y qué les ofrecemos?
**Fechas:** 12 y 13 de noviembre · **Horas:** 12 h (3 h teoría · 5 h práctica · 4 h PBL)
**Módulo:** M3, unidades 3.9 a 3.12 · **Evaluación:** test de M3 (segunda parte)

> 🎯 **Reto de este sprint: «Conocer al huésped».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_09.md) · [Reto en PDF](guia/Reto_Sprint_09.pdf) ([ecofriendly](guia/Reto_Sprint_09_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_09.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_09.pdf) · [ecofriendly, para imprimir](README_Sprint_09_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_09.pdf`](guia/Guia_Sprint_09.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_09_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_09.md`](guia/Reto_Sprint_09.md)
- 🖥️ **S09.1 · Clustering y PCA:** [`S09.1_Clustering_y_PCA.pdf`](presentaciones/S09.1_Clustering_y_PCA.pdf)
- 🖥️ **S09.2 · Sistemas de recomendacion:** [`S09.2_Sistemas_de_recomendacion.pdf`](presentaciones/S09.2_Sistemas_de_recomendacion.pdf)
- 🖥️ **S09.3 · Aprendizaje por refuerzo:** [`S09.3_Aprendizaje_por_refuerzo.pdf`](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf)

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Jueves 12/11**

1. 🔔 **Ceremonia**: Planning del reto «Conocer al huésped» y reparto de roles · _10 min_
2. 📖 **Teoría**: [Clustering y PCA](presentaciones/S09.1_Clustering_y_PCA.pdf) · _1 h 15 min_
3. 💻 **Práctica**: [Segmentar huéspedes: k-means, silueta, jerárquico y DBSCAN](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_01_clustering.ipynb) · _1 h_
4. 💻 **Práctica**: [PCA: varianza explicada y mapa en 2D](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_02_pca.ipynb) · _40 min_
5. 🎯 **Reto**: [Arrancar el reto: preparar datos, segmentar y elegir `k`, mapa PCA (pasos 1–3)](guia/Reto_Sprint_09.md) · _1 h 5 min_

**Viernes 13/11**

6. 📖 **Teoría**: [Sistemas de recomendación](presentaciones/S09.2_Sistemas_de_recomendacion.pdf) · _20 min_
7. 📖 **Teoría**: [Aprendizaje por refuerzo (visión conceptual)](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf) · _25 min_
8. 💻 **Práctica**: [Recomendadores: popularidad, contenido, colaborativo y factorización](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_03_recomendadores.ipynb) · _1 h_
9. 💻 **Práctica**: [Q-learning en el hotel (demostración guiada)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_04_q_learning.ipynb) · _25 min_
10. 🎯 **Reto**: [Recomendador, ficha de segmentos, IA responsable y ensayo (pasos 4–5)](guia/Reto_Sprint_09.md) · _1 h 20 min_
11. 🔔 **Ceremonia**: Entrega en `sprint-09/`, autoevaluación y coevaluación, review (3 min por equipo) y retrospectiva · _40 min_

<!--orden:fin-->

## Qué aprenderás
- Agrupar clientes con **k-means, jerárquico y DBSCAN** y elegir `k` con la silueta.
- Reducir dimensiones con **PCA** y construir recomendadores (popularidad, contenido, colaborativo).
- Entender el **aprendizaje por refuerzo** con un Q-learning pequeño en numpy.
- Interpretar cada segmento para el negocio: nombre, tamaño y una acción comercial.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S09_01_clustering` | Segmentar huéspedes: escalado, k-means, silueta, jerárquico, DBSCAN | 80 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_01_clustering.ipynb) |
| `S09_02_pca` | PCA: varianza explicada, mapa 2D, cargas, mención a t-SNE | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_02_pca.ipynb) |
| `S09_03_recomendadores` | Popularidad, contenido, colaborativo, factorización; RMSE y precision@k | 80 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_03_recomendadores.ipynb) |
| `S09_04_q_learning` | Q-learning en el hotel (numpy): recompensas, epsilon-greedy, política | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/notebooks/S09_04_q_learning.ipynb) |

Cada notebook tiene comprobaciones automáticas (✔). Trabaja en orden: no pases al siguiente hasta que los `assert` pasen. Los datos se descargan solos.

## Reto · «Conocer al huésped»

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
