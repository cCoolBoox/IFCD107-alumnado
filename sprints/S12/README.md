# README Sprint S12 · Lenguaje, secuencias y modelos generativos (+ informe visual)

**Pregunta guía:** ¿qué dicen los clientes y qué pasará mañana?  
**Fechas:** 23–25/11 · **Horas:** 18 h (3 h teoría · 8 h práctica · 7 h PBL, con el Sprint 13 integrado en el último día)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_12.pdf) · [ecofriendly](pdf/README_Sprint_12_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. A **predecir una serie temporal** (la ocupación) y a comprobar si tu modelo gana de verdad a un método simple (*baseline*).
2. A **leer reseñas con Python**: limpiar texto, medir el sentimiento y descubrir de qué se queja o qué alaba la gente.
3. A representar texto con **vectores (embeddings)** y a entender, con números pequeños, cómo funciona la **atención** de un Transformer.
4. A montar un **mini asistente con RAG** que responde con la política del alojamiento, cita su fuente y sabe decir "no consta".
5. A **evaluar** un asistente (aciertos, alucinaciones) y a reconocer un ataque de *prompt injection*; y a entender la idea de autoencoders, GAN y difusión.

## Día 1 · Lunes 23/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «Escuchar al cliente» y reparto de las cinco áreas | — | 10 |
| ☐ | 📖 Teoría · RNN, LSTM, GRU y series temporales | [Presentación S12.1](1_Teoria/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf) | 20 |
| ☐ | 💻 Práctica · Series temporales: *baselines*, descomposición y SARIMAX (los ejercicios marcados «en clase») | [Cuaderno S12_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/S12_01_series_temporales.ipynb) | 45 |
| ☐ | 💻 Práctica · RNN, LSTM y GRU frente al *baseline* (los ejercicios marcados «en clase») | [Cuaderno S12_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/S12_02_redes_recurrentes.ipynb) | 45 |
| ☐ | 📖 Teoría · NLP clásico y embeddings | [Presentación S12.2](1_Teoria/S12.2_NLP_clasico_y_embeddings.pdf) | 25 |
| ☐ | 💻 Práctica · Reseñas: limpieza, TF-IDF, sentimiento, temas y n-gramas (los ejercicios marcados «en clase») | [Cuaderno S12_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/S12_03_nlp_clasico.ipynb) | 55 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé partir una serie temporal por fecha y calcular un *baseline*.
- [ ] Sé calcular el sentimiento de una reseña.

## Día 2 · Martes 24/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · Transformers y LLM | [Presentación S12.3](1_Teoria/S12.3_Transformers_y_LLM.pdf) | 30 |
| ☐ | 💻 Práctica · Tokens, atención paso a paso y temperatura (los ejercicios marcados «en clase») | [Cuaderno S12_05](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/S12_05_transformers_atencion.ipynb) | 40 |
| ☐ | 💻 Práctica · Mini RAG con la política, evaluación y seguridad (los ejercicios marcados «en clase») | [Cuaderno S12_06](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/2_Practica/S12_06_mini_rag.ipynb) | 45 |
| ☐ | 📖 Teoría · Autoencoders y modelos generativos | [Presentación S12.4](1_Teoria/S12.4_Autoencoders_y_modelos_generativos.pdf) | 10 |
| ☐ | 🎯 Reto · Reparto y plan (paso 1) y datos y modelos de las partes A (reseñas) y C (asistente) (paso 2) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_12_una_pagina.md) | 65 |
| ☐ | 💻 Práctica · Terminad los cuadernos pendientes y poneos al día | — | 10 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Mi equipo tiene una tarjeta por entregable con responsable.
- [ ] Sé qué es RAG y por qué hace falta un umbral.

## Día 3 · Miércoles 25/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🎯 Reto · Parte B (ocupación), evaluación y seguridad del asistente y cierre (pasos 2–4) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_12_una_pagina.md) | 65 |
| ☐ | 📝 Test · **Test de M4** (redes neuronales), solo se abre hoy | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/tests/test_M4.html) | 30 |
| ☐ | 📖 Teoría · Visualizar y comunicar resultados (Sprint 13, integrado; versión rápida) | [Presentación S13.1](../S13/1_Teoria/S13.1_Visualizar_y_comunicar_resultados.pdf) | 10 |
| ☐ | 💻 Práctica · Matriz de confusión, ROC/PR, importancia, umbral y coste | [Cuaderno S13_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/2_Practica/S13_01_visualizacion_resultados.ipynb) | 35 |
| ☐ | 🎯 Reto · Reto del Sprint 13: elegir el modelo y los costes → tres o cuatro gráficos → titular y viñetas. Usad el cuaderno plantilla y la plantilla del informe | [Reto del Sprint 13](../S13/3_Reto/1_Reto_en_una_pagina/Reto_Sprint_13_una_pagina.md) | 25 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-12/` (y el informe visual en `sprint-13/`), autoevaluación y coevaluación, review y retrospectiva | — | 35 |

**En clase: 3 h 20 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** TurisData recibe cada semana **decenas de reseñas** y **decenas de mensajes** de huéspedes con las mismas preguntas («¿hasta cuándo puedo cancelar?», «¿admiten perros?»). La dirección no puede leerlo todo ni contestar a mano. Quiere **tres cosas**:

**Qué vais a entregar:** una carpeta (o zip) por equipo con (1) el informe de reseñas, (2) el cuaderno del modelo de ocupación, (3) el cuaderno de la demo del asistente con su tabla de evaluación y (4) la nota de IA responsable, más un `LEEME.md` de 5 líneas.

**Núcleo y extra.** Núcleo: dos de las tres partes técnicas (a elegir entre reseñas, ocupación y asistente) con su informe. Extra: la tercera parte y las prácticas de ampliación.

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_12_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_12.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

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
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-12/`: 8 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 11). Aparte: resenas.csv en `data/` si aún no está; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el mié 25/11
- [ ] Serie partida **por fecha** y con **baseline** en la tabla.
- [ ] Escalado y vectorización ajustados solo con entrenamiento.
- [ ] El asistente cita la fuente y responde «No consta…» cuando no sabe.
- [ ] Probados 3 ataques de prompt injection.
- [ ] Ninguna clave en el código ni en el repositorio.
- [ ] Todo se ejecuta de arriba abajo, sin errores y sin internet.
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_12.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_series_lenguaje_y_generativa.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_12.md).
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
| UD 4.7 | RNN, LSTM, GRU y series temporales |
| UD 4.8 | NLP clásico y embeddings: tokenización, TF-IDF, word2vec; procesamiento léxico, sintáctico y semántico |
| UD 4.9 | Transformers y LLM: atención, BERT/GPT, Hugging Face, fine-tuning ligero, introducción a RAG y APIs |
| UD 4.10 | Autoencoders y modelos generativos (GAN, difusión: introducción) |

**Y ahora:** Sprint 13 · Contar lo que hace el modelo, dentro de esta misma última jornada (miércoles 25/11).

*18 h (3 h teoría · 8 h práctica · 7 h PBL).*
