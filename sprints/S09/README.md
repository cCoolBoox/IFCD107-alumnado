# Sprint 9 · Segmentar, recomendar y aprender por refuerzo

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_09.pdf`](Guia_Sprint_09.pdf)
- 🖥️ **S09.1 · Clustering y PCA:** [`S09.1_Clustering_y_PCA.pdf`](presentaciones/S09.1_Clustering_y_PCA.pdf)
- 🖥️ **S09.2 · Sistemas de recomendacion:** [`S09.2_Sistemas_de_recomendacion.pdf`](presentaciones/S09.2_Sistemas_de_recomendacion.pdf)
- 🖥️ **S09.3 · Aprendizaje por refuerzo:** [`S09.3_Aprendizaje_por_refuerzo.pdf`](presentaciones/S09.3_Aprendizaje_por_refuerzo.pdf)

> **Pregunta guía:** ¿qué tipos de cliente tenemos y qué les ofrecemos?
> **Fechas:** 11 y 12 de noviembre · **Horas:** 11 h (3 h teoría · 5 h práctica · 3 h PBL)
> **Módulo:** M3, unidades 3.9 a 3.12 · **Evaluación:** test de M3 (segunda parte)

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

## Prácticas

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S09_01_clustering` | Segmentar huéspedes: escalado, k-means, silueta, jerárquico, DBSCAN | 1 h 30 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_01_clustering.ipynb) |
| `S09_02_pca` | PCA: varianza explicada, mapa 2D, cargas, mención a t-SNE | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_02_pca.ipynb) |
| `S09_03_recomendadores` | Popularidad, contenido, colaborativo, factorización; RMSE y precision@k | 1 h 30 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_03_recomendadores.ipynb) |
| `S09_04_q_learning` | Q-learning en el hotel (numpy): recompensas, epsilon-greedy, política | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S09/S09_04_q_learning.ipynb) |

Cada notebook tiene ejercicios con comprobaciones automáticas (✔ cuando salen bien). Trabaja en orden y no pases al siguiente hasta que los `assert` pasen.

---

## Reto PBL · «Conocer al huésped»  (3 h)

### El cliente
Lucía, directora comercial de **TurisData Canarias**, envía la misma newsletter a los 1 200 huéspedes de su base y vende las 25 experiencias con los mismos banners. Sospecha que hay «tipos» de cliente muy distintos y que cada uno querría cosas diferentes. Nos pide: *«Decidme quiénes son mis clientes, cómo los llamo y qué le enseño a cada uno»*.

### Qué se entrega y en qué formato
1. **Notebook** `reto_S09_conocer_al_huesped.ipynb` (versión ejecutable de arriba abajo, con semillas fijas) con:
   - Segmentación de `huespedes.csv` (método justificado, `k` elegido con silueta y con criterio de negocio) y un **mapa 2D con PCA**.
   - Prototipo de **recomendador de experiencias** (mínimo dos métodos comparados con RMSE y precision@3) y la función `recomendar(id_usuario, n)`.
2. **Ficha de segmentos (1 página, Markdown o PDF)** usando `plantilla_ficha_segmentos.md`: por cada segmento, nombre, tamaño, perfil en una frase, **una acción comercial** y **una experiencia estrella** de las que recomienda tu prototipo.
3. **Nota de IA responsable (5 líneas)** dentro de la ficha: qué riesgos tiene segmentar y recomendar (discriminación, sesgo de popularidad, privacidad).

### Restricciones
- Solo numpy, pandas, matplotlib/seaborn y scikit-learn (sin librerías de recomendación especializadas).
- Trabajo en equipos de 3-4; **todas las personas** deben poder explicar cualquier parte.
- Los ficheros de solución del docente no están disponibles: los segmentos se validan con **sentido de negocio** y con métricas internas.

### Criterios de evaluación (rúbrica de retos, de 1 a 4)

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Datos sin escalar o `k` al azar; métricas mal calculadas | Segmenta y recomienda con fallos menores | Escalado, `k` justificado y recomendador evaluado con una división de prueba | Además compara varios métodos de clustering y de recomendación con resultados razonados |
| **Reproducibilidad** | No se puede volver a ejecutar | Se ejecuta con ayuda del equipo | Se ejecuta de arriba abajo con semillas fijas | Además incluye README corto, datos o script de descarga y versiones |
| **Análisis y comunicación al cliente** | Solo cifras o gráficos sin interpretar | Nombres de segmentos sin acciones | Segmentos con nombre, tamaño y una acción cada uno | Además recomendación accionable, priorizada por valor y con límites explicados |
| **IA responsable** | No se considera | Menciones genéricas («hay que cuidar la privacidad») | Riesgos específicos: sesgo de popularidad, discriminación por edad o niños | Además propone medidas (p. ej. no segmentar por edad para precios) y comprueba alguna |

### Pasos sugeridos
| Día | Qué hacer |
|---|---|
| **11/11 (1 h de PBL tras las prácticas 01 y 02)** | Ya tenéis los segmentos en borrador: elegid método y `k` con silueta **y** con criterio de negocio; haced el mapa PCA. |
| **12/11 mañana** | Prácticas 03 y 04. Con lo aprendido, arrancad el prototipo de `recomendar` y comparad al menos dos métodos. |
| **12/11 (2 h de PBL)** | 1) Interpretad segmentos y rellenad la ficha (50 min). 2) Comparad recomendadores y probad `recomendar` con 3 usuarios (40 min). 3) Nota de IA responsable, repaso de la Definition of Done y ensayo de la review (30 min). |

### Qué se enseña en la review
Cada equipo presenta en 3 minutos: **sus segmentos (nombre + acción)** y **una recomendación concreta para un usuario**. Se comparan los `k` elegidos y se discute *¿es el mismo cliente aunque le pongamos otro nombre?*

### Definition of Done
- [ ] El notebook se ejecuta de arriba abajo sin errores y con semillas fijas.
- [ ] Variables escaladas antes de agrupar; `k` justificado con silueta **y** con criterio de negocio.
- [ ] Mapa 2D (PCA) con los segmentos coloreados y ejes con el % de varianza.
- [ ] Ficha de segmentos con nombre, tamaño, perfil y acción por segmento.
- [ ] Recomendador evaluado con RMSE y precision@3, comparado con la popularidad.
- [ ] `recomendar(id_usuario, n)` no propone experiencias ya valoradas.
- [ ] Nota de IA responsable con al menos dos riesgos específicos.
- [ ] Cada persona del equipo ha hecho *commit* de su parte.

## Recursos
- Documentación de scikit-learn: *Clustering* y *Decomposition* (guía de usuario, en inglés).
- Vídeo o artículo introductorio sobre el **coeficiente de silueta** y el método del codo (busca material propio del centro o de tu elección).
- Explicación visual de la **factorización de matrices** para recomendación.
- «Sutton y Barto: *Reinforcement Learning: An Introduction*» (capítulo 1, gratuito online) para ir más allá de Q-learning.
- Ampliación: Gymnasium (`pip install gymnasium`), la librería estándar que replica la interfaz `reset`/`step` del notebook 04.
