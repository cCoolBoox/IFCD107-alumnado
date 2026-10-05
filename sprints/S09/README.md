# Sprint 9 · Segmentar, recomendar y aprender por refuerzo

**Pregunta guía:** ¿qué tipos de cliente tenemos y qué les ofrecemos?
**Fechas:** 11 y 12 de noviembre · **Horas:** 11 h (3 h teoría · 5 h práctica · 3 h PBL)
**Módulo:** M3, unidades 3.9 a 3.12 · **Evaluación:** test de M3 (segunda parte)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_09.pdf`](Guia_Sprint_09.pdf)
- 🖥️ **S09.1 · Clustering y PCA:** [`S09.1_Clustering_y_PCA.pdf`](presentaciones/S09.1_Clustering_y_PCA.pdf)
- 🖥️ **S09.2 · Sistemas de recomendacion:** [`S09.2_Sistemas_de_recomendacion.pdf`](presentaciones/S09.2_Sistemas_de_recomendacion.pdf)
- 🖥️ **S09.3 · Aprendizaje por refuerzo:** [`S09.3_Aprendizaje_por_refuerzo.pdf`](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf)

## Qué aprenderás
- Agrupar clientes con **k-means, jerárquico y DBSCAN** y elegir `k` con la silueta.
- Reducir dimensiones con **PCA** y construir recomendadores (popularidad, contenido, colaborativo).
- Entender el **aprendizaje por refuerzo** con un Q-learning pequeño en numpy.
- Interpretar cada segmento para el negocio: nombre, tamaño y una acción comercial.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S09_01_clustering` | Segmentar huéspedes: escalado, k-means, silueta, jerárquico, DBSCAN | 1 h 30 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_01_clustering.ipynb) |
| `S09_02_pca` | PCA: varianza explicada, mapa 2D, cargas, mención a t-SNE | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_02_pca.ipynb) |
| `S09_03_recomendadores` | Popularidad, contenido, colaborativo, factorización; RMSE y precision@k | 1 h 30 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_03_recomendadores.ipynb) |
| `S09_04_q_learning` | Q-learning en el hotel (numpy): recompensas, epsilon-greedy, política | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_04_q_learning.ipynb) |

Cada notebook tiene comprobaciones automáticas (✔). Trabaja en orden: no pases al siguiente hasta que los `assert` pasen. Los datos se descargan solos.

## Reto · «Conocer al huésped»
**Contexto:** Lucía, directora comercial de TurisData Canarias, envía la misma newsletter a sus 1 200 huéspedes y vende 25 experiencias con los mismos banners. Pide: «Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno».

**Entregáis** (carpeta `sprint-09/` del repositorio del equipo):
- `reto_S09_conocer_al_huesped.ipynb`: segmentación de `huespedes.csv` (`k` con silueta y criterio de negocio), mapa 2D con PCA y `recomendar(id_usuario, n)`.
- Ficha de segmentos (1 página): nombre, tamaño, perfil, una acción y una experiencia estrella por segmento. Plantilla: [`plantilla_ficha_segmentos.md`](plantilla_ficha_segmentos.md).
- Nota de IA responsable (5 líneas) dentro de la ficha.

**Reglas:**
- 3 h en equipos de 3-4; solo numpy, pandas, matplotlib/seaborn y scikit-learn. Todas las personas deben poder explicar cualquier parte.
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
