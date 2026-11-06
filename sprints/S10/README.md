# README Sprint S10 · Redes neuronales bien entrenadas

**Pregunta guía:** ¿una red neuronal mejora al aprendizaje automático clásico y a qué precio?  
**Fechas:** 17–18 de noviembre · **Horas:** 12 h (3 h teoría · 5 h práctica · 4 h PBL)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Los cuadernos **«en clase»** (carpeta `2_Practica/en_clase/`) son la parte que se hace en el aula; los completos (carpeta `2_Practica/para_casa/`) son para casa.

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
| ☐ | 📖 Teoría · Una red neuronal desde cero: neurona, activación, error y gradiente | [Presentación S10_01](1_Teoria/S10_01_presentacion_Red_neuronal_desde_cero.pdf) | 20 |
| ☐ | 💻 Práctica · Una red neuronal con solo NumPy (cuaderno «en clase») | [Cuaderno S10_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/en_clase/S10_01_red_desde_cero_en_clase.ipynb) | 40 |
| ☐ | 📖 Teoría · Redes densas con Keras: preparar los datos, Sequential, Dense y fit | [Presentación S10_02](1_Teoria/S10_02_presentacion_Redes_densas_con_Keras.pdf) | 25 |
| ☐ | 💻 Práctica · MLP en Keras: clasificación y regresión (cuaderno «en clase») | [Cuaderno S10_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/en_clase/S10_02_mlp_keras_en_clase.ipynb) | 60 |
| ☐ | 📖 Teoría · Entrenamiento y regularización: sobreajuste, L2, *dropout* y *callbacks* (diapositivas 2 a 5; la 11 es del reto) | [Presentación S10_03](1_Teoria/S10_03_presentacion_Entrenamiento_y_regularizacion.pdf) | 25 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 20 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé entrenar un MLP en Keras.
- [ ] Sé qué es una época y para qué sirve la validación.

## Día 2 · Miércoles 18/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 💻 Práctica · Sobreajuste, L2, *dropout*, parada temprana y *callbacks* (cuaderno «en clase») | [Cuaderno S10_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/en_clase/S10_03_regularizacion_en_clase.ipynb) · [Presentación S10_03](1_Teoria/S10_03_presentacion_Entrenamiento_y_regularizacion.pdf) | 55 |
| ☐ | 🎯 Reto · Esqueleto `S10_04`: elegir el problema y reproducir la referencia (paso 1) → primera red (2) → variantes (3) → diagnosticar el sobreajuste (4) → comparación justa (5) → informe y entrega (6); lo que falte, en la consolidación y la 6.ª hora | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_10_una_pagina.md) | 90 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 15 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-10/`, autoevaluación y coevaluación, review y retrospectiva | — | 40 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé entrenar una red con Keras y reconocer el sobreajuste en las curvas de aprendizaje.
- [ ] Sé decidir con datos si una red neuronal vale la pena frente a un modelo de ML clásico.

## El reto en pocas palabras

**Qué os pide el cliente.** La dirección de TurisData oye hablar de **redes neuronales** en todas partes y pregunta si debe **sustituir su modelo de cancelaciones por una red**. No quiere una opinión: quiere **evidencias, con el coste incluido**, para decidir si merece la pena el cambio.

**Qué vais a entregar:** un cuaderno ejecutable (basado en `S10_04`) y un informe comparativo *ML clásico frente a MLP*.

**Núcleo y extra.** Núcleo: un único problema: reproducir la referencia y una mejora con la red, bien medida. Extra: más experimentos y las prácticas «en casa».

Antes de empezar, probad la [demo interactiva](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S10/3_Reto/1_Trabajar/S10_demo_reto.html) (muestra lo que tendréis al final). Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_10_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_10.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-10/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `reto_vale_la_pena.ipynb` · lo modificáis
- [ ] `informe_comparativo.md` · lo creáis a partir de una plantilla
- [ ] `README.md` · lo modificáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-10/`: 3 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 6). Aparte: reservas_turisdata.csv en `data/` si aún no está; curvas_aprendizaje.png; mlp_final.keras; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Notebook de arriba abajo con semillas fijas; test usado una sola vez
- [ ] MLP y modelo de árboles/boosting comparados con incertidumbre
- [ ] Curvas de aprendizaje y recomendación concreta con coste y límites
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los **cuadernos completos** (🏠 para casa) de los que hiciste en clase la parte «en clase». Traen **todos** los ejercicios y el mini-reto, se autocorrigen y llevan una «Solución de referencia» plegada por si te quedas atascado: [`S10_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/para_casa/S10_01_red_desde_cero.ipynb) · [`S10_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/para_casa/S10_02_mlp_keras.ipynb) · [`S10_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/2_Practica/para_casa/S10_03_regularizacion.ipynb).
- **Solucionarios** (para contrastar después de intentarlo): [cuadernos «en clase»](2_Practica/en_clase/Solucionario_en_clase.md) y [cuadernos completos](2_Practica/para_casa/Solucionario_para_casa.md).
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_redes_neuronales.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_10.md).
2. Mira el [código explicado](2_Practica/codigo_explicado/README.md) del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
| [`4_Referencia/`](4_Referencia/) | Resultados de los cuadernos (presentación y documento) e infografías |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| UD 4.1 | Fundamentos: neurona, perceptrón, activaciones, pérdida, backpropagation y optimizadores (implementación en NumPy) |
| UD 4.2 | Redes densas (MLP) con Keras: clasificación y regresión |
| UD 4.3 | Entrenamiento y regularización: dropout, L2, early stopping, batch norm, callbacks, TensorBoard |

**Y ahora:** Sprint 11 · Visión por computador (jueves 19/11).

*12 h (3 h teoría · 5 h práctica · 4 h PBL).*
