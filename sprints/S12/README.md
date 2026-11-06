# README Sprint S12 · Lenguaje, secuencias y modelos generativos (+ informe visual)

**Pregunta guía:** ¿qué dicen los clientes y qué pasará mañana?  
**Fechas:** 23–25/11 · **Horas:** 18 h (3 h teoría · 8 h práctica · 7 h PBL, con el Sprint 13 integrado en el último día)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Los cuadernos **«en clase»** (carpeta `2_Practica/en_clase/`) son la parte que se hace en el aula; los completos (carpeta `2_Practica/para_casa/`) son para casa.

## Qué aprenderás

1. A **predecir una serie temporal** (la ocupación) y a comprobar si tu modelo gana de verdad a un método simple (*baseline*).
2. A **leer reseñas con Python**: limpiar texto, medir el sentimiento y descubrir de qué se queja o qué alaba la gente.
3. A representar texto con **vectores (embeddings)** y a entender, con números pequeños, cómo funciona la **atención** de un Transformer.
4. A montar un **mini asistente con RAG** que responde con la política del alojamiento, cita su fuente y sabe decir "no consta".
5. A **evaluar** un asistente (aciertos, alucinaciones) y a reconocer un ataque de *prompt injection*; y a entender la idea de autoencoders, GAN y difusión.

## Día 1 · Lunes 23/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «Escuchar al cliente» y reparto de las cinco áreas | — | 15 |
| ☐ | 📖 Teoría · Series temporales: *baseline*, descomposición y SARIMAX | [Presentación S12_01](1_Teoria/S12_01_presentacion_Series_temporales.pdf) | 10 |
| ☐ | 💻 Práctica · Series temporales: *baselines*, descomposición y SARIMAX (cuaderno «en clase») | [Cuaderno S12_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/en_clase/S12_01_series_temporales_en_clase.ipynb) | 45 |
| ☐ | 📖 Teoría · RNN, LSTM y GRU: redes con memoria | [Presentación S12_02](1_Teoria/S12_02_presentacion_RNN_LSTM_y_GRU.pdf) | 10 |
| ☐ | 💻 Práctica · RNN, LSTM y GRU frente al *baseline* (cuaderno «en clase») | [Cuaderno S12_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/en_clase/S12_02_redes_recurrentes_en_clase.ipynb) | 45 |
| ☐ | 📖 Teoría · NLP clásico: limpiar, vectorizar y clasificar texto | [Presentación S12_03](1_Teoria/S12_03_presentacion_NLP_clasico.pdf) | 20 |
| ☐ | 💻 Práctica · Reseñas: limpieza, TF-IDF, sentimiento y temas (cuaderno «en clase») | [Cuaderno S12_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/en_clase/S12_03_nlp_clasico_en_clase.ipynb) | 55 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé partir una serie temporal por fecha y calcular un *baseline*.
- [ ] Sé calcular el sentimiento de una reseña.

## Día 2 · Martes 24/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · Transformers, atención y LLM | [Presentación S12_05](1_Teoria/S12_05_presentacion_Transformers_y_atencion.pdf) | 15 |
| ☐ | 💻 Práctica · Softmax, atención paso a paso y máscara causal (cuaderno «en clase») | [Cuaderno S12_05](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/en_clase/S12_05_transformers_atencion_en_clase.ipynb) | 40 |
| ☐ | 📖 Teoría · RAG: un asistente que cita su fuente | [Presentación S12_06](1_Teoria/S12_06_presentacion_Mini_RAG.pdf) | 10 |
| ☐ | 💻 Práctica · Mini RAG: trocear la política, recuperar fragmentos y responder con umbral (cuaderno «en clase») | [Cuaderno S12_06](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/en_clase/S12_06_mini_rag_en_clase.ipynb) | 45 |
| ☐ | 📖 Teoría · Autoencoders y modelos generativos (versión corta) | [Presentación S12_07](1_Teoria/S12_07_presentacion_Autoencoders_y_modelos_generativos.pdf) | 10 |
| ☐ | 🎯 Reto · Reparto y plan (paso 1) y datos y modelos de las partes A (reseñas) y C (asistente) (paso 2) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_12_una_pagina.md) | 65 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 15 |
| ☐ | 🏠 **En casa** · Embeddings: representar el significado con vectores, LSA (ampliación) | [Cuaderno S12_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_04_embeddings_lsa.ipynb) · [Presentación S12_04](1_Teoria/S12_04_presentacion_Embeddings_y_LSA.pdf) | 50 (casa) |
| ☐ | 🏠 **En casa** · Autoencoders y modelos generativos, GAN y difusión (ampliación) | [Cuaderno S12_07](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_07_autoencoder_generativos.ipynb) · [Presentación S12_07](1_Teoria/S12_07_presentacion_Autoencoders_y_modelos_generativos.pdf) | 50 (casa) |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Mi equipo tiene una tarjeta por entregable con responsable.
- [ ] Sé qué es RAG y por qué hace falta un umbral.

## Día 3 · Miércoles 25/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · Parte B (ocupación), evaluación y seguridad del asistente y cierre (pasos 2–4) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_12_una_pagina.md) | 65 |
| ☐ | 📝 Test · **Test de M4** (redes neuronales) | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/tests/test_M4.html) | 30 |
| ☐ | 📖 Teoría · Visualizar y comunicar resultados (Sprint 13, integrado; versión rápida) | [Presentación S13_01](../S13/1_Teoria/S13_01_presentacion_Visualizar_y_comunicar_resultados.pdf) | 10 |
| ☐ | 💻 Práctica · Matriz de confusión, ROC/PR, importancia, umbral y coste | [Cuaderno S13_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/en_clase/S13_01_visualizacion_resultados_en_clase.ipynb) | 35 |
| ☐ | 🎯 Reto · Reto del Sprint 13: elegir el modelo y los costes → tres o cuatro gráficos → titular y viñetas. Usad el cuaderno plantilla y la plantilla del informe | [Reto del Sprint 13](../S13/3_Reto/1_Trabajar/Reto_Sprint_13_una_pagina.md) | 35 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-12/` (y el informe visual en `sprint-13/`), autoevaluación y coevaluación, review y retrospectiva | — | 25 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé comprobar si un modelo de series temporales gana de verdad a un *baseline*.
- [ ] Sé montar un mini asistente con RAG que cita su fuente y sabe decir «no consta».
- [ ] Sé explicar un resultado a un cliente con tres o cuatro gráficos y un titular.

## El reto en pocas palabras

**Qué os pide el cliente.** TurisData recibe cada semana **decenas de reseñas** y **decenas de mensajes** de huéspedes con las mismas preguntas («¿hasta cuándo puedo cancelar?», «¿admiten perros?»). La dirección no puede leerlo todo ni contestar a mano. Quiere **tres cosas**:

1. **Saber qué opinan y de qué se quejan** sus clientes (reseñas).
2. **Prever la ocupación de la próxima semana** para organizar personal y compras (serie temporal).
3. **Probar un asistente** que responda con la política del alojamiento **sin inventar nada** (RAG).

**Qué vais a entregar:** una carpeta (o zip) por equipo con (1) el informe de reseñas, (2) el cuaderno del modelo de ocupación, (3) el cuaderno de la demo del asistente con su tabla de evaluación y (4) la nota de IA responsable, más un `LEEME.md` de 5 líneas.

**Núcleo y extra.** Núcleo: dos de las tres partes técnicas (a elegir entre reseñas, ocupación y asistente) con su informe. Extra: la tercera parte y las prácticas de ampliación.

Antes de empezar, probad la [demo interactiva](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/3_Reto/1_Trabajar/S12_demo_reto.html) (muestra lo que tendréis al final). Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_12_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_12.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-12/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `informe_resenas.md` · lo creáis a partir de una plantilla
- [ ] `grafico_resenas.png` · lo genera
- [ ] `resenas.ipynb` · lo creáis
- [ ] `ocupacion.ipynb` · lo creáis
- [ ] `asistente_rag.ipynb` · lo creáis
- [ ] `evaluacion_asistente.csv` · lo genera
- [ ] `nota_ia_responsable.md` · lo creáis
- [ ] `LEEME.md` · lo creáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-12/`: 8 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 11). Aparte: resenas.csv en `data/` si aún no está; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el mié 25/11
- [ ] Serie partida **por fecha** y con **baseline** en la tabla.
- [ ] Escalado y vectorización ajustados solo con entrenamiento.
- [ ] El asistente cita la fuente y responde «No consta…» cuando no sabe.
- [ ] Probados 3 ataques de prompt injection.
- [ ] Ninguna clave en el código ni en el repositorio.
- [ ] Todo se ejecuta de arriba abajo, sin errores y sin internet.
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los **cuadernos completos** (🏠 para casa) de los que hiciste en clase la parte «en clase». Traen **todos** los ejercicios y el mini-reto, se autocorrigen y llevan una «Solución de referencia» plegada por si te quedas atascado: [`S12_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_01_series_temporales.ipynb) · [`S12_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_02_redes_recurrentes.ipynb) · [`S12_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_03_nlp_clasico.ipynb) · [`S12_05`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_05_transformers_atencion.ipynb) · [`S12_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/para_casa/S12_06_mini_rag.ipynb).
- **Solucionarios** (para contrastar después de intentarlo): [cuadernos «en clase»](2_Practica/en_clase/Solucionario_en_clase.md) y [cuadernos completos](2_Practica/para_casa/Solucionario_para_casa.md).
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_series_lenguaje_y_generativa.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_12.md).
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
| UD 4.7 | RNN, LSTM, GRU y series temporales |
| UD 4.8 | NLP clásico y embeddings: tokenización, TF-IDF, word2vec; procesamiento léxico, sintáctico y semántico |
| UD 4.9 | Transformers y LLM: atención, BERT/GPT, Hugging Face, fine-tuning ligero, introducción a RAG y APIs |
| UD 4.10 | Autoencoders y modelos generativos (GAN, difusión: introducción) |

**Y ahora:** Sprint 13 · Contar lo que hace el modelo, dentro de esta misma última jornada (miércoles 25/11).

*18 h (3 h teoría · 8 h práctica · 7 h PBL).*
