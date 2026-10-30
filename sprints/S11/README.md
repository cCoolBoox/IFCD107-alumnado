# README Sprint S11 · Visión por computador

**Pregunta guía:** ¿podemos aprovechar las imágenes del cliente?  
**Fechas:** 19–20 de noviembre · **Horas:** 12 h (2 h teoría · 4 h práctica · 6 h PBL)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_11.pdf) · [ecofriendly](pdf/README_Sprint_11_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. Cómo "ve" una red: imágenes como matrices, convolución, *pooling* y arquitectura de una CNN.
2. Entrenar una CNN pequeña y mejorar su generalización con *data augmentation*.
3. Reutilizar redes preentrenadas: *transfer learning* y *fine-tuning*.
4. Detección de objetos y segmentación: IoU, NMS, AP/mAP y un detector clásico con OpenCV.
5. Evaluar un clasificador de imágenes con métricas por clase y **análisis de errores**.

## Día 1 · Jueves 19/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «Visión artificial para el cliente» y reparto de roles | — | 10 |
| ☐ | 📖 Teoría · Redes convolucionales (CNN) | [Presentación S11.1](1_Teoria/S11.1_Redes_convolucionales_CNN.pdf) | 25 |
| ☐ | 💻 Práctica · Convolución, pooling, CNN y *data augmentation* (los ejercicios marcados «en clase») | [Cuaderno S11_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_01_cnn.ipynb) | 40 |
| ☐ | 📖 Teoría · Transfer learning y fine-tuning | [Presentación S11.2](1_Teoria/S11.2_Transfer_learning_y_fine_tuning.pdf) | 25 |
| ☐ | 💻 Práctica · Transfer learning y fine-tuning (los ejercicios marcados «en clase») | [Cuaderno S11_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_02_transfer_learning.ipynb) | 75 |
| ☐ | 🎯 Reto · Preparar los datos (paso 1) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_11_una_pagina.md) | 25 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé qué hace una capa convolucional.
- [ ] Sé qué es el transfer learning.
- [ ] El dataset de mi equipo está preparado.

## Día 2 · Viernes 20/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · Detección de objetos y segmentación (versión corta) | [Presentación S11.3](1_Teoria/S11.3_Deteccion_de_objetos_y_segmentacion.pdf) | 15 |
| ☐ | 💻 Práctica · IoU y NMS con números pequeños (los ejercicios marcados «en clase»); el detector con OpenCV y la segmentación son para casa | [Cuaderno S11_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_03_deteccion_segmentacion.ipynb) | 35 |
| ☐ | 💻 Práctica · Esqueleto del reto: dataset por carpetas y análisis de errores | [Cuaderno S11_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_04_reto_vision_cliente.ipynb) | 40 |
| ☐ | 🎯 Reto · Transfer learning y referencia (2) → evaluación y análisis de errores (3) → demostrador y umbral de confianza (4) → informe y presentación (5) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_11_una_pagina.md) | 80 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-11/`, autoevaluación y coevaluación, review y retrospectiva | — | 30 |

**En clase: 3 h 20 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** TurisData recibe **cientos de fotos** de alojamientos y zonas cada semana, y una persona las clasifica a mano (hotel, apartamentos, casa rural, camping, piscina). Quiere saber si un modelo puede **pre-clasificarlas** y, sobre todo, **en qué se equivoca**, para decidir cuánto puede fiarse y **qué fotos debe revisar una persona**.

**Qué vais a entregar:** el modelo (`.keras` o cuaderno que lo reproduce), el demostrador y el análisis de errores.

**Núcleo y extra.** Núcleo: un modelo de *transfer learning* bien evaluado, con análisis de errores y demostrador. Extra: *fine-tuning* y comparar más modelos.

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_11_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_11.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-11/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `reto_vision_cliente.ipynb` · lo modificáis
- [ ] `analisis_errores.md` · lo creáis
- [ ] `README.md` · lo creáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-11/`: 3 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 6). Aparte: clasificador_alojamientos.keras; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Dataset por carpetas comprobado por clase; test usado una sola vez
- [ ] Métricas por clase, matriz de confusión y ≥ 6 errores analizados
- [ ] Demostrador con umbral de confianza y opción «revisar a mano»
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_11.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_vision_por_computador.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_11.md).
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
| UD 4.4 | CNN y visión por computador: convolución, pooling, arquitecturas (LeNet, VGG, ResNet), data augmentation |
| UD 4.5 | Transfer learning y fine-tuning |
| UD 4.6 | Detección de objetos y segmentación (introducción, YOLO) |

**Y ahora:** Sprint 12 · Lenguaje, secuencias y modelos generativos (+ informe visual) (lunes 23/11).

*12 h (2 h teoría · 4 h práctica · 6 h PBL).*
