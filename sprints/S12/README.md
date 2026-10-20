# Sprint 12 · Lenguaje, secuencias y modelos generativos
**Pregunta guía:** ¿qué dicen los clientes y qué pasará mañana?
**Fechas:** 23–25/11 · **Horas:** 18 h (5 h teoría · 6 h práctica · 7 h PBL, con el Sprint 13 integrado en el último día)

> 🎯 **Reto de este sprint: «Escuchar al cliente».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_12.md) · [Reto en PDF](guia/Reto_Sprint_12.pdf) ([ecofriendly](guia/Reto_Sprint_12_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_12.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_12.pdf) · [ecofriendly, para imprimir](README_Sprint_12_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_12.pdf`](guia/Guia_Sprint_12.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_12_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_12.md`](guia/Reto_Sprint_12.md)
- 🖼️ **Infografías del reto (2 láminas: el reto de un vistazo y cómo se trabaja y se evalúa):** [`infografias/`](infografias/)
- 🖥️ **S12.1 · RNN LSTM GRU y series temporales:** [`S12.1_RNN_LSTM_GRU_y_series_temporales.pdf`](presentaciones/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf)
- 🖥️ **S12.2 · NLP clasico y embeddings:** [`S12.2_NLP_clasico_y_embeddings.pdf`](presentaciones/S12.2_NLP_clasico_y_embeddings.pdf)
- 🖥️ **S12.3 · Transformers y LLM:** [`S12.3_Transformers_y_LLM.pdf`](presentaciones/S12.3_Transformers_y_LLM.pdf)
- 🖥️ **S12.4 · Autoencoders y modelos generativos:** [`S12.4_Autoencoders_y_modelos_generativos.pdf`](presentaciones/S12.4_Autoencoders_y_modelos_generativos.pdf)
- 🤖 **¿Tu proyecto usará un modelo de lenguaje por internet?** Guía de acceso gratuito: [`Acceso_modelos_de_lenguaje.md`](../../material/Acceso_modelos_de_lenguaje.md)

**📁 En esta carpeta:** [`infografias/`](infografias/) láminas ilustradas del reto · [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto · [`tests/`](tests/) test de conocimientos

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Lunes 23/11**

1. 🔔 **Ceremonia**: Planning del reto «Escuchar al cliente» y reparto de las cinco áreas · _10 min_
2. 📖 **Teoría**: [RNN, LSTM, GRU y series temporales](presentaciones/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf) · _25 min_
3. 💻 **Práctica**: [Series temporales: *baselines*, descomposición y SARIMAX](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_01_series_temporales.ipynb) · _45 min_
4. 💻 **Práctica**: [RNN, LSTM y GRU frente al *baseline*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_02_redes_recurrentes.ipynb) · _45 min_
5. 📖 **Teoría**: [NLP clásico y embeddings](presentaciones/S12.2_NLP_clasico_y_embeddings.pdf) · _20 min_
6. 💻 **Práctica**: [Reseñas: limpieza, TF-IDF, sentimiento, temas y n-gramas](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_03_nlp_clasico.ipynb) · _55 min_

**Martes 24/11**

7. 📖 **Teoría**: [Transformers y LLM](presentaciones/S12.3_Transformers_y_LLM.pdf) · _35 min_
8. 💻 **Práctica**: [Tokens, atención paso a paso y temperatura](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_05_transformers_atencion.ipynb) · _40 min_
9. 💻 **Práctica**: [Mini RAG con la política, evaluación y seguridad](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_06_mini_rag.ipynb) · _45 min_
10. 📖 **Teoría**: [Autoencoders y modelos generativos](presentaciones/S12.4_Autoencoders_y_modelos_generativos.pdf) · _15 min_
11. 🎯 **Reto**: [Reparto y plan (paso 1) y datos y modelos de las partes A (reseñas) y C (asistente) (paso 2)](guia/Reto_Sprint_12.md) · _1 h 5 min_

**Miércoles 25/11**

12. 🎯 **Reto**: [Parte B (ocupación), evaluación y seguridad del asistente y cierre (pasos 2–4)](guia/Reto_Sprint_12.md) · _1 h 5 min_
13. 📝 **Test**: [**Test de M4** (redes neuronales), solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/tests/test_M4.html) · _30 min_
14. 📖 **Teoría**: [Visualizar y comunicar resultados (Sprint 13, integrado; versión rápida)](../S13/presentaciones/S13.1_Visualizar_y_comunicar_resultados.pdf) · _10 min_
15. 💻 **Práctica**: [Matriz de confusión, ROC/PR, importancia, umbral y coste](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_01_visualizacion_resultados.ipynb) · _35 min_
16. 🎯 **Reto**: [Reto del Sprint 13](../S13/guia/Reto_Sprint_13.md): elegir el modelo y los costes → tres o cuatro gráficos → titular y viñetas. Usad el [cuaderno plantilla](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_02_plantilla_informe_visual.ipynb) y la [plantilla del informe](../S13/plantillas/plantilla_informe_visual.md) · _25 min_
17. 🔔 **Ceremonia**: Entrega en `sprint-12/` (y el informe visual en `sprint-13/`), autoevaluación y coevaluación, review y retrospectiva · _35 min_

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
| `S12_01_series_temporales` | Serie temporal: baselines, descomposición, ARIMA/SARIMAX | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_01_series_temporales.ipynb) |
| `S12_02_redes_recurrentes` | RNN, LSTM y GRU en Keras vs. baseline | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_02_redes_recurrentes.ipynb) |
| `S12_03_nlp_clasico` | Reseñas: limpieza, TF-IDF, sentimiento, temas y n-gramas | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_03_nlp_clasico.ipynb) |
| `S12_04_embeddings_lsa` | Embeddings con LSA y buscador de reseñas parecidas | 50 min (opcional, en casa) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_04_embeddings_lsa.ipynb) |
| `S12_05_transformers_atencion` | Tokens, atención paso a paso, temperatura (+ Hugging Face opcional) | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_05_transformers_atencion.ipynb) |
| `S12_06_mini_rag` | Mini RAG con la política, evaluación y seguridad | 45 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_06_mini_rag.ipynb) |
| `S12_07_autoencoder_generativos` | Autoencoder para anomalías; idea de GAN y difusión | 50 min (opcional, en casa) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_07_autoencoder_generativos.ipynb) |

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
