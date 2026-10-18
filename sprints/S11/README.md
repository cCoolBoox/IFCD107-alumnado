# Sprint 11 · Visión por computador

**Pregunta guía:** ¿podemos aprovechar las imágenes del cliente?
**Fechas:** 17–20 de noviembre · **Horas:** 17 h (5 h teoría · 7 h práctica · 5 h PBL) · **Módulo 4, UD 4.4–4.6**

> 🎯 **Reto de este sprint: «Visión artificial para el cliente».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_11.md) · [Reto en PDF](guia/Reto_Sprint_11.pdf) ([ecofriendly](guia/Reto_Sprint_11_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_11.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_11.pdf`](guia/Guia_Sprint_11.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_11_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_11.md`](guia/Reto_Sprint_11.md)
- 🖥️ **S11.1 · Redes convolucionales CNN:** [`S11.1_Redes_convolucionales_CNN.pdf`](presentaciones/S11.1_Redes_convolucionales_CNN.pdf)
- 🖥️ **S11.2 · Transfer learning y fine tuning:** [`S11.2_Transfer_learning_y_fine_tuning.pdf`](presentaciones/S11.2_Transfer_learning_y_fine_tuning.pdf)
- 🖥️ **S11.3 · Deteccion de objetos y segmentacion:** [`S11.3_Deteccion_de_objetos_y_segmentacion.pdf`](presentaciones/S11.3_Deteccion_de_objetos_y_segmentacion.pdf)

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`recursos/`](recursos/) scripts y ficheros de apoyo

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Prácticas, en este orden**

1. 📖 **Teoría**: [Redes convolucionales (CNN)](presentaciones/S11.1_Redes_convolucionales_CNN.pdf) · _1 h 30 min_
2. 💻 **Práctica**: [Convolución, pooling, CNN y *data augmentation*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_01_cnn.ipynb) · _1 h 45 min_
3. 📖 **Teoría**: [Transfer learning y fine-tuning](presentaciones/S11.2_Transfer_learning_y_fine_tuning.pdf) · _1 h 30 min_
4. 💻 **Práctica**: [Transfer learning y fine-tuning](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_02_transfer_learning.ipynb) · _1 h 45 min_
5. 📖 **Teoría**: [Detección de objetos y segmentación](presentaciones/S11.3_Deteccion_de_objetos_y_segmentacion.pdf) · _1 h 30 min_
6. 💻 **Práctica**: [IoU, NMS, mAP, detector con OpenCV y segmentación](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_03_deteccion_segmentacion.ipynb) · _1 h 45 min_
7. 💻 **Práctica**: [Esqueleto del reto: dataset por carpetas y análisis de errores (arranque del reto)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_04_reto_vision_cliente.ipynb) · _1 h 45 min_

**Reto «Visión artificial para el cliente»**

8. 🎯 **Reto**: [Preparar los datos (paso 1) → transfer learning y referencia (2) → evaluación y análisis de errores (3) → demostrador y umbral de confianza (4) → informe y presentación (5)](guia/Reto_Sprint_11.md) · _5 h_

<!--orden:fin-->

## Qué aprenderás
- Cómo «ve» una red: convolución, *pooling* y CNN; *data augmentation*.
- Reutilizar redes preentrenadas: *transfer learning* y *fine-tuning*.
- Detección y segmentación (IoU, NMS, mAP) y análisis de errores por clase.
- Hace falta el Sprint 10. Funciona sin internet con imágenes sintéticas; las celdas «requiere internet» son opcionales.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S11_01_cnn` | Convolución, pooling y CNN en Keras (dígitos 8×8); *data augmentation* | 1 h 45 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_01_cnn.ipynb) |
| `S11_02_transfer_learning` | Transfer learning y fine-tuning (con preentrenamiento propio y MobileNetV2 en Colab) | 1 h 45 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_02_transfer_learning.ipynb) |
| `S11_03_deteccion_segmentacion` | IoU, NMS, mAP, detector con OpenCV, segmentación (y YOLO opcional) | 1 h 45 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_03_deteccion_segmentacion.ipynb) |
| `S11_04_reto_vision_cliente` | Esqueleto del reto: dataset por carpetas, transfer learning, análisis de errores | 1 h 45 (+ trabajo PBL) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_04_reto_vision_cliente.ipynb) |

Extra: `generar_dataset_sintetico.py` crea el mini dataset de alojamientos (una carpeta por clase): `python generar_dataset_sintetico.py`.

## Reto · «Visión artificial para el cliente»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_11.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** TurisData Canarias recibe cientos de fotos de alojamientos cada semana y las clasifica una persona a mano. Quiere saber si un modelo puede pre-clasificarlas y, sobre todo, en qué se equivoca, para decidir qué fotos revisar a mano.

**Entregáis** (carpeta `sprint-11/` del repositorio del equipo):
- Modelo con *transfer learning* (`.keras` o notebook que lo reproduce), con una referencia desde cero.
- Demostrador: función que recibe una foto y devuelve clase, confianza y «revisar a mano» si es baja.
- Análisis de errores (1–2 páginas): métricas por clase, matriz de confusión y ≥ 6 ejemplos mal clasificados con su causa probable.
- Origen y licencia de los datos.

**Reglas:**
- 5 h en equipo; dataset sintético o propio con licencia clara, sin personas reconocibles, una carpeta por clase (≥ 30 imágenes).
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
