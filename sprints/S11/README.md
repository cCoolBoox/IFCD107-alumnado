# README Sprint S11 · Visión por computador

**Pregunta guía:** ¿podemos aprovechar las imágenes del cliente?
**Fechas:** 18–20 de noviembre · **Horas:** 18 h (4 h teoría · 7 h práctica · 7 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_11.pdf) · [ecofriendly, para imprimir](README_Sprint_11_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás

1. Cómo "ve" una red: imágenes como matrices, convolución, *pooling* y arquitectura de una CNN.
2. Entrenar una CNN pequeña y mejorar su generalización con *data augmentation*.
3. Reutilizar redes preentrenadas: *transfer learning* y *fine-tuning*.
4. Detección de objetos y segmentación: IoU, NMS, AP/mAP y un detector clásico con OpenCV.
5. Evaluar un clasificador de imágenes con métricas por clase y **análisis de errores**.

## Requisitos previos

- Sprint 10 (redes neuronales, Keras, curvas de aprendizaje, regularización).
- Todo funciona **sin internet** con imágenes sintéticas (dibujos generados por código, no fotos reales).
- Algunas celdas opcionales para Colab (descarga de `tf_flowers`, pesos de MobileNetV2 con ImageNet, YOLO) están marcadas
  como **«requiere internet»**: en el taller no se ejecutan (llevan un interruptor `USAR_INTERNET = False`).

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_11.pdf) · [ecofriendly](guia/Guia_Sprint_11_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_11.md) · [PDF](guia/Reto_Sprint_11.pdf) · [ecofriendly](guia/Reto_Sprint_11_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S11_00_resumen_del_sprint.png) | Lámina con la pregunta del cliente, los pasos, lo que se entrega y lo que se aprende | — | Antes del planning |
| [Esquema del contenido y su relación con el reto](infografias/S11_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del reto](infografias/) | 4 láminas ilustradas del reto | — | Reto |
| [Atlas de algoritmos](infografias/../S10/infografias/S10_03_atlas_redes_neuronales_y_vision.png) | Atlas de algoritmos (S10–S11): CNN, transfer learning y detección, junto al MLP | — | Teoría y práctica; consulta cuando elijas modelo |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S11.1_Redes_convolucionales_CNN.pdf`](presentaciones/S11.1_Redes_convolucionales_CNN.pdf) | Redes convolucionales (CNN) | 25 min | Teoría · miércoles 18/11 |
| [`S11.2_Transfer_learning_y_fine_tuning.pdf`](presentaciones/S11.2_Transfer_learning_y_fine_tuning.pdf) | Transfer learning y fine-tuning | 20 min | Teoría · miércoles 18/11 |
| [`S11.3_Deteccion_de_objetos_y_segmentacion.pdf`](presentaciones/S11.3_Deteccion_de_objetos_y_segmentacion.pdf) | Detección de objetos y segmentación | 20 min | Teoría · jueves 19/11 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S11_01_cnn` | Convolución, pooling y CNN en Keras (dígitos 8×8); *data augmentation* | 65 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_01_cnn.ipynb) |
| `S11_02_transfer_learning` | Transfer learning y fine-tuning (con preentrenamiento propio y MobileNetV2 en Colab) | 80 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_02_transfer_learning.ipynb) |
| `S11_03_deteccion_segmentacion` | IoU, NMS, mAP, detector con OpenCV, segmentación (y YOLO opcional) | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_03_deteccion_segmentacion.ipynb) |
| `S11_04_reto_vision_cliente` | Esqueleto del reto: dataset por carpetas, transfer learning, análisis de errores | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_04_reto_vision_cliente.ipynb) |

Extra: `generar_dataset_sintetico.py` crea el mini dataset de alojamientos (una carpeta por clase): `python generar_dataset_sintetico.py`.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Miércoles 18/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Visión artificial para el cliente» y reparto de roles | 10 min |
| 2 | 📖 Teoría | [Redes convolucionales (CNN)](presentaciones/S11.1_Redes_convolucionales_CNN.pdf) | 25 min |
| 3 | 💻 Práctica | [Convolución, pooling, CNN y *data augmentation*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_01_cnn.ipynb) | 1 h 5 min |
| 4 | 📖 Teoría | [Transfer learning y fine-tuning](presentaciones/S11.2_Transfer_learning_y_fine_tuning.pdf) | 20 min |
| 5 | 💻 Práctica | [Transfer learning y fine-tuning (primera parte)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_02_transfer_learning.ipynb) | 1 h |
| 6 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 20 min |

**Jueves 19/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 7 | 💻 Práctica | [Transfer learning y fine-tuning (final)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_02_transfer_learning.ipynb) | 20 min |
| 8 | 📖 Teoría | [Detección de objetos y segmentación](presentaciones/S11.3_Deteccion_de_objetos_y_segmentacion.pdf) | 20 min |
| 9 | 💻 Práctica | [IoU, NMS, mAP, detector con OpenCV y segmentación](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_03_deteccion_segmentacion.ipynb) | 45 min |
| 10 | 💻 Práctica | [Esqueleto del reto: dataset por carpetas y análisis de errores (arranque del reto)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_04_reto_vision_cliente.ipynb) | 1 h |
| 11 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 10 min |
| 12 | 🎯 Reto | [Preparar los datos (paso 1)](guia/Reto_Sprint_11.md) | 45 min |

**Viernes 20/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 13 | 🎯 Reto | [Transfer learning y referencia (2) → evaluación y análisis de errores (3) → demostrador y umbral de confianza (4) → informe y presentación (5)](guia/Reto_Sprint_11.md) | 2 h 20 min |
| 14 | 🔔 Ceremonia | Entrega en `sprint-11/`, autoevaluación y coevaluación, review y retrospectiva | 1 h |

<!--orden:fin-->

## Reto · «Visión artificial para el cliente»

📄 [Reto en PDF](guia/Reto_Sprint_11.pdf) · [ecofriendly](guia/Reto_Sprint_11_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_11.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** TurisData Canarias recibe cientos de fotos de alojamientos cada semana y las clasifica una persona a mano. Quiere saber si un modelo puede pre-clasificarlas y, sobre todo, en qué se equivoca, para decidir qué fotos revisar a mano.


**Entregáis** (carpeta `sprint-11/` del repositorio del equipo):
- Modelo con *transfer learning* (`.keras` o notebook que lo reproduce), con una referencia desde cero.
- Demostrador: función que recibe una foto y devuelve clase, confianza y «revisar a mano» si es baja.
- Análisis de errores (1–2 páginas): métricas por clase, matriz de confusión y ≥ 6 ejemplos mal clasificados con su causa probable.
- Origen y licencia de los datos.


**Reglas:**
- Unas 4 h 10 min de reto en equipo; dataset sintético o propio con licencia clara, sin personas reconocibles, una carpeta por clase (≥ 30 imágenes).
- Partición fija; prueba usada una sola vez; debe ejecutarse en CPU en pocos minutos.
- Nunca claves ni datos personales.


**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (representatividad, clases raras, licencias y privacidad), más umbral de confianza justificado.

## ✅ Antes de cerrar el sprint
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Dataset por carpetas comprobado por clase; test usado una sola vez
- [ ] Métricas por clase, matriz de confusión y ≥ 6 errores analizados
- [ ] Demostrador con umbral de confianza y opción «revisar a mano»
- [ ] Entregable subido a la carpeta `sprint-11/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
