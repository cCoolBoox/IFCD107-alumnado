# Sprint 12 · Lenguaje, secuencias y modelos generativos
**Pregunta guía:** ¿qué dicen los clientes y qué pasará mañana?
**Fechas:** 20–25/11 · **Horas:** 18 h (5 T · 8 P · 5 reto PBL)

> 🎯 **Reto de este sprint: «Escuchar al cliente».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_12.md) · [Reto en PDF](guia/Reto_Sprint_12.pdf) ([ecofriendly](guia/Reto_Sprint_12_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_12.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_12.pdf`](guia/Guia_Sprint_12.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_12_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_12.md`](guia/Reto_Sprint_12.md)
- 🖥️ **S12.1 · RNN LSTM GRU y series temporales:** [`S12.1_RNN_LSTM_GRU_y_series_temporales.pdf`](presentaciones/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf)
- 🖥️ **S12.2 · NLP clasico y embeddings:** [`S12.2_NLP_clasico_y_embeddings.pdf`](presentaciones/S12.2_NLP_clasico_y_embeddings.pdf)
- 🖥️ **S12.3 · Transformers y LLM:** [`S12.3_Transformers_y_LLM.pdf`](presentaciones/S12.3_Transformers_y_LLM.pdf)
- 🖥️ **S12.4 · Autoencoders y modelos generativos:** [`S12.4_Autoencoders_y_modelos_generativos.pdf`](presentaciones/S12.4_Autoencoders_y_modelos_generativos.pdf)
- 🤖 **¿Tu proyecto usará un modelo de lenguaje por internet?** Guía de acceso gratuito: [`Acceso_modelos_de_lenguaje.md`](../../material/Acceso_modelos_de_lenguaje.md)

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto · [`tests/`](tests/) test de conocimientos

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Bloque 1 · Series temporales**

1. 📖 **Teoría**: [RNN, LSTM, GRU y series temporales](presentaciones/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf) · _1 h 30 min_
2. 💻 **Práctica**: [Series temporales: *baselines*, descomposición y SARIMAX](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_01_series_temporales.ipynb) · _1 h_
3. 💻 **Práctica**: [RNN, LSTM y GRU frente al *baseline*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_02_redes_recurrentes.ipynb) · _1 h_

**Bloque 2 · Texto**

4. 📖 **Teoría**: [NLP clásico y embeddings](presentaciones/S12.2_NLP_clasico_y_embeddings.pdf) · _1 h_
5. 💻 **Práctica**: [Reseñas: limpieza, TF-IDF, sentimiento, temas y n-gramas](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_03_nlp_clasico.ipynb) · _1 h 10 min_
6. 💻 **Práctica**: [Embeddings con LSA y buscador de reseñas parecidas](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_04_embeddings_lsa.ipynb) · _50 min_

**Bloque 3 · Transformers y LLM**

7. 📖 **Teoría**: [Transformers y LLM](presentaciones/S12.3_Transformers_y_LLM.pdf) · _1 h 30 min_
8. 💻 **Práctica**: [Tokens, atención paso a paso y temperatura](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_05_transformers_atencion.ipynb) · _1 h 10 min_
9. 💻 **Práctica**: [Mini RAG con la política, evaluación y seguridad](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_06_mini_rag.ipynb) · _1 h 30 min_

**Bloque 4 · Generativos y reto**

10. 📖 **Teoría**: [Autoencoders y modelos generativos](presentaciones/S12.4_Autoencoders_y_modelos_generativos.pdf) · _1 h_
11. 💻 **Práctica**: [Autoencoder para anomalías; idea de GAN y difusión](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_07_autoencoder_generativos.ipynb) · _50 min_
12. 🎯 **Reto**: [Reparto y plan (hora 1) → datos y modelos (horas 2–3) → evaluación y seguridad del asistente (hora 4) → cierre (hora 5)](guia/Reto_Sprint_12.md) · _5 h_

<!--orden:fin-->

## Qué aprenderás
- A **predecir una serie temporal** (la ocupación) y comprobar si gana a un método simple (*baseline*).
- A **leer reseñas con Python**: sentimiento y temas de queja o elogio.
- Qué son los **embeddings** y la **atención** de un Transformer.
- A montar un **mini asistente RAG** que cita su fuente y sabe decir «no consta», y a reconocer un *prompt injection*.

## Prácticas
Todo se ejecuta sin internet (las partes **OPCIONAL / NO VERIFICADO** se pueden saltar). Nunca escribas claves de API en el código.

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S12_01_series_temporales` | Serie temporal: baselines, descomposición, ARIMA/SARIMAX | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_01_series_temporales.ipynb) |
| `S12_02_redes_recurrentes` | RNN, LSTM y GRU en Keras vs. baseline | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_02_redes_recurrentes.ipynb) |
| `S12_03_nlp_clasico` | Reseñas: limpieza, TF-IDF, sentimiento, temas y n-gramas | 1 h 10 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_03_nlp_clasico.ipynb) |
| `S12_04_embeddings_lsa` | Embeddings con LSA y buscador de reseñas parecidas | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_04_embeddings_lsa.ipynb) |
| `S12_05_transformers_atencion` | Tokens, atención paso a paso, temperatura (+ Hugging Face opcional) | 1 h 10 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_05_transformers_atencion.ipynb) |
| `S12_06_mini_rag` | Mini RAG con la política, evaluación y seguridad | 1 h 30 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_06_mini_rag.ipynb) |
| `S12_07_autoencoder_generativos` | Autoencoder para anomalías; idea de GAN y difusión | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_07_autoencoder_generativos.ipynb) |

Plantilla en esta carpeta: [`plantilla_informe_cliente.md`](plantillas/plantilla_informe_cliente.md) (informe de reseñas).

## Entrega / Reto · «Escuchar al cliente»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_12.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** TurisData Canarias recibe decenas de reseñas y mensajes de huéspedes cada semana. Quiere saber qué opinan, prever la ocupación de la próxima semana y probar un asistente que responda con su política sin inventar nada. Los datos son sintéticos: dilo en el informe.
**Entregáis** (carpeta `sprint-12/` del repositorio del equipo):
- `informe_resenas.md` (o PDF), 2 páginas: sentimiento, 3 temas criticados y 3 valorados, 5 citas, 3 recomendaciones y límites.
- Notebook de ocupación: partición temporal, baseline, modelo, tabla de MAE y previsión a 7 días.
- Notebook del asistente RAG con tabla de evaluación: 20 preguntas de referencia + 5 propias + 3 ataques.
- Nota de IA responsable (1 página `.md`): riesgos y medidas medidas.
- `LEEME.md` de 5 líneas para ejecutarlo todo.
**Reglas:**
- Prohibido partir la serie al azar, o escalar/vectorizar antes de partir.
- Todo debe ejecutarse sin internet y sin claves; las cifras salen del código.
- Se presenta en la *review* (5 min por equipo).
**Se valora:** corrección técnica, reproducibilidad (`SEMILLA = 42`), comunicación al cliente e IA responsable (0–4 cada uno).

## 📝 Test de conocimientos · mié 25/11
**Test de M4 · Redes neuronales** · 12 preguntas · unos 20 min · individual, en el navegador, sin penalización por fallo. Cubre M4 (redes densas, CNN, series, lenguaje y Transformers).

👉 **[Abrir el test](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/tests/test_M4.html)** (`https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/tests/test_M4.html`)

**Solo se abre el día mié 25/11** (hora de Canarias). Al terminar, copia tu resultado y envíaselo al docente. Cuenta para el 30 % de «tests de conocimientos».

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mié 25/11
- [ ] Serie partida **por fecha** y con **baseline** en la tabla.
- [ ] Escalado y vectorización ajustados solo con entrenamiento.
- [ ] El asistente cita la fuente y responde «No consta…» cuando no sabe.
- [ ] Probados 3 ataques de prompt injection.
- [ ] Ninguna clave en el código ni en el repositorio.
- [ ] Todo se ejecuta de arriba abajo, sin errores y sin internet.
- [ ] Entregable subido a la carpeta `sprint-12/` del repositorio del equipo.
