# Sprint 11 · Visión por computador

**Pregunta guía:** ¿podemos aprovechar las imágenes del cliente?
**Fechas:** 17–20 de noviembre · **Horas:** 17 h (5 h teoría · 7 h práctica · 5 h PBL) · **Módulo 4, UD 4.4–4.6**

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_11.pdf`](Guia_Sprint_11.pdf)
- 🖥️ **S11.1 · Redes convolucionales CNN:** [`S11.1_Redes_convolucionales_CNN.pdf`](presentaciones/S11.1_Redes_convolucionales_CNN.pdf)
- 🖥️ **S11.2 · Transfer learning y fine tuning:** [`S11.2_Transfer_learning_y_fine_tuning.pdf`](presentaciones/S11.2_Transfer_learning_y_fine_tuning.pdf)
- 🖥️ **S11.3 · Deteccion de objetos y segmentacion:** [`S11.3_Deteccion_de_objetos_y_segmentacion.pdf`](presentaciones/S11.3_Deteccion_de_objetos_y_segmentacion.pdf)

## Qué aprenderás
- Cómo «ve» una red: convolución, *pooling* y CNN; *data augmentation*.
- Reutilizar redes preentrenadas: *transfer learning* y *fine-tuning*.
- Detección y segmentación (IoU, NMS, mAP) y análisis de errores por clase.
- Hace falta el Sprint 10. Funciona sin internet con imágenes sintéticas; las celdas «requiere internet» son opcionales.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S11_01_cnn` | Convolución, pooling y CNN en Keras (dígitos 8×8); *data augmentation* | 1 h 45 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/S11_01_cnn.ipynb) |
| `S11_02_transfer_learning` | Transfer learning y fine-tuning (con preentrenamiento propio y MobileNetV2 en Colab) | 1 h 45 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/S11_02_transfer_learning.ipynb) |
| `S11_03_deteccion_segmentacion` | IoU, NMS, mAP, detector con OpenCV, segmentación (y YOLO opcional) | 1 h 45 | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/S11_03_deteccion_segmentacion.ipynb) |
| `S11_04_reto_vision_cliente` | Esqueleto del reto: dataset por carpetas, transfer learning, análisis de errores | 1 h 45 (+ trabajo PBL) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/S11_04_reto_vision_cliente.ipynb) |

Extra: `generar_dataset_sintetico.py` crea el mini dataset de alojamientos (una carpeta por clase): `python generar_dataset_sintetico.py`.

## Reto · «Visión artificial para el cliente»
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
