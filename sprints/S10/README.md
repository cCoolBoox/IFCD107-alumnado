# README Sprint S10 · Redes neuronales bien entrenadas

**Pregunta guía:** ¿una red neuronal mejora al aprendizaje automático clásico y a qué precio?  
**Fechas:** 17–18 de noviembre · **Horas:** 12 h (3 h teoría · 5 h práctica · 4 h PBL)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_10.pdf) · [ecofriendly](pdf/README_Sprint_10_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. Cómo funciona por dentro una red neuronal: neurona, capas, activación, propagación hacia delante y hacia atrás.
2. Construir y entrenar un MLP con Keras para clasificar cancelaciones y predecir el precio por noche.
3. Reconocer el **sobreajuste** en las curvas de aprendizaje y combatirlo (L2, *dropout*, parada temprana, *batch norm*).
4. Ajustar tasa de aprendizaje y tamaño de lote, usar *callbacks* y guardar/cargar modelos.
5. Decidir con datos si una red "vale la pena" frente a un modelo de boosting.

## Día 1 · Martes 17/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «¿Vale la pena la red?» y reparto de roles | — | 10 |
| ☐ | 📖 Teoría · Fundamentos de redes neuronales | [Presentación S10.1](1_Teoria/S10.1_Fundamentos_de_redes_neuronales.pdf) | 25 |
| ☐ | 💻 Práctica · Una red neuronal con solo NumPy (los ejercicios marcados «en clase») | [Cuaderno S10_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_01_red_desde_cero.ipynb) | 40 |
| ☐ | 📖 Teoría · Redes densas con Keras | [Presentación S10.2](1_Teoria/S10.2_Redes_densas_con_Keras.pdf) | 25 |
| ☐ | 💻 Práctica · MLP en Keras: clasificación y regresión (los ejercicios marcados «en clase») | [Cuaderno S10_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_02_mlp_keras.ipynb) | 60 |
| ☐ | 📖 Teoría · Entrenamiento y regularización (diapositivas 1–5; las 6–7 son del reto) | [Presentación S10.3](1_Teoria/S10.3_Entrenamiento_y_regularizacion.pdf) | 30 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 10 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé entrenar un MLP en Keras.
- [ ] Sé qué es una época y para qué sirve la validación.

## Día 2 · Miércoles 18/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 💻 Práctica · Sobreajuste, L2, *dropout*, parada temprana y *callbacks* (los ejercicios marcados «en clase») | [Cuaderno S10_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/S10_03_regularizacion.ipynb) | 55 |
| ☐ | 🎯 Reto · Esqueleto `S10_04`: elegir el problema y reproducir la referencia (paso 1) → primera red (2) → diagnosticar el sobreajuste (3) → comparación justa (4) → informe y presentación (5) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_10_una_pagina.md) | 90 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 15 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-10/`, autoevaluación y coevaluación, review y retrospectiva | — | 40 |

**En clase: 3 h 20 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** La dirección de TurisData oye hablar de **redes neuronales** en todas partes y pregunta si debe **sustituir su modelo de cancelaciones por una red**. No quiere una opinión: quiere **evidencias, con el coste incluido**, para decidir si merece la pena el cambio.

**Qué vais a entregar:** un cuaderno ejecutable (basado en `S10_04`) y un informe comparativo *ML clásico frente a MLP*.

**Núcleo y extra.** Núcleo: un único problema: reproducir la referencia y una mejora con la red, bien medida. Extra: más experimentos y las prácticas «en casa».

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_10_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_10.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-10/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `reto_vale_la_pena.ipynb` · lo modificáis
- [ ] `informe_comparativo.md` · lo creáis
- [ ] `README.md` · lo modificáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-10/`: 3 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 6). Aparte: reservas_turisdata.csv en `data/` si aún no está; curvas_aprendizaje.png; mlp_final.keras; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Notebook de arriba abajo con semillas fijas; test usado una sola vez
- [ ] MLP y modelo de árboles/boosting comparados con incertidumbre
- [ ] Curvas de aprendizaje y recomendación concreta con coste y límites
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_10.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_redes_neuronales.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_10.md).
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
| UD 4.1 | Fundamentos: neurona, perceptrón, activaciones, pérdida, backpropagation y optimizadores (implementación en NumPy) |
| UD 4.2 | Redes densas (MLP) con Keras: clasificación y regresión |
| UD 4.3 | Entrenamiento y regularización: dropout, L2, early stopping, batch norm, callbacks, TensorBoard |

**Y ahora:** Sprint 11 · Visión por computador (jueves 19/11).

*12 h (3 h teoría · 5 h práctica · 4 h PBL).*
