# README Sprint S12 · Lenguaje, secuencias y modelos generativos

**Pregunta guía:** ¿qué dicen los clientes y qué pasará mañana?
**Fechas:** 23–25/11 · **Horas:** 18 h (5 h teoría · 6 h práctica · 7 h PBL, con el Sprint 13 integrado en el último día)

📄 **Este README en PDF:** [a color](README_Sprint_12.pdf) · [ecofriendly, para imprimir](README_Sprint_12_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. A **predecir una serie temporal** (la ocupación) y a comprobar si tu modelo gana de verdad a un método simple (*baseline*).
2. A **leer reseñas con Python**: limpiar texto, medir el sentimiento y descubrir de qué se queja o qué alaba la gente.
3. A representar texto con **vectores (embeddings)** y a entender, con números pequeños, cómo funciona la **atención** de un Transformer.
4. A montar un **mini asistente con RAG** que responde con la política del alojamiento, cita su fuente y sabe decir "no consta".
5. A **evaluar** un asistente (aciertos, alucinaciones) y a reconocer un ataque de *prompt injection*; y a entender la idea de autoencoders, GAN y difusión.

## Requisitos previos
- Sprints 9–11: aprendizaje automático con scikit-learn, redes neuronales y Keras básico (capas, `fit`, épocas).
- Saber cargar datos con pandas y hacer gráficos sencillos.
- No necesitas cuenta en ningún servicio de IA: **todo se ejecuta sin internet**. Hay partes opcionales (marcadas **NO VERIFICADO**) para Colab o para un LLM instalado en tu equipo.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_12.pdf) · [ecofriendly](guia/Guia_Sprint_12_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_12.md) · [PDF](guia/Reto_Sprint_12.pdf) · [ecofriendly](guia/Reto_Sprint_12_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Infografías del reto](infografias/) | 2 láminas ilustradas del reto | — | Reto |
| [Atlas de algoritmos](infografias/S12_03_atlas_series_lenguaje_y_generativa.png) | Atlas de algoritmos del sprint: series, RNN/LSTM/GRU, NLP, Transformers/LLM y autoencoders | — | Teoría y práctica; consulta cuando elijas modelo |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S12.1_RNN_LSTM_GRU_y_series_temporales.pdf`](presentaciones/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf) | RNN, LSTM, GRU y series temporales | 20 min | Teoría · lunes 23/11 |
| [`S12.2_NLP_clasico_y_embeddings.pdf`](presentaciones/S12.2_NLP_clasico_y_embeddings.pdf) | NLP clásico y embeddings | 15 min | Teoría · lunes 23/11 |
| [`S12.3_Transformers_y_LLM.pdf`](presentaciones/S12.3_Transformers_y_LLM.pdf) | Transformers y LLM | 30 min | Teoría · martes 24/11 |
| [`S12.4_Autoencoders_y_modelos_generativos.pdf`](presentaciones/S12.4_Autoencoders_y_modelos_generativos.pdf) | Autoencoders y modelos generativos | 10 min | Teoría · martes 24/11 |
| [`S13.1_Visualizar_y_comunicar_resultados.pdf`](../S13/presentaciones/S13.1_Visualizar_y_comunicar_resultados.pdf) | Visualizar y comunicar resultados (Sprint 13, integrado; versión rápida) | 10 min | Teoría · miércoles 25/11 |
| [`Acceso_modelos_de_lenguaje.md`](../../material/Acceso_modelos_de_lenguaje.md) | ¿Tu proyecto usará un modelo de lenguaje por internet? Guía de acceso gratuito | — | Si tu proyecto usa un modelo de lenguaje |
| [Test de conocimientos](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/tests/test_M4.html) | Test de M4 · Redes neuronales · 12 preguntas · individual, en el navegador, sin penalización por fallo. | 20 min | Solo se abre el mié 25/11 (hora de Canarias) |

**Material de las actividades**

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

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Lunes 23/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Escuchar al cliente» y reparto de las cinco áreas | 10 min |
| 2 | 📖 Teoría | [RNN, LSTM, GRU y series temporales](presentaciones/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf) | 20 min |
| 3 | 💻 Práctica | [Series temporales: *baselines*, descomposición y SARIMAX](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_01_series_temporales.ipynb) | 45 min |
| 4 | 💻 Práctica | [RNN, LSTM y GRU frente al *baseline*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_02_redes_recurrentes.ipynb) | 45 min |
| 5 | 📖 Teoría | [NLP clásico y embeddings](presentaciones/S12.2_NLP_clasico_y_embeddings.pdf) | 15 min |
| 6 | 💻 Práctica | [Reseñas: limpieza, TF-IDF, sentimiento, temas y n-gramas](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_03_nlp_clasico.ipynb) | 55 min |
| 7 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 10 min |

**Martes 24/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 8 | 📖 Teoría | [Transformers y LLM](presentaciones/S12.3_Transformers_y_LLM.pdf) | 30 min |
| 9 | 💻 Práctica | [Tokens, atención paso a paso y temperatura](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_05_transformers_atencion.ipynb) | 40 min |
| 10 | 💻 Práctica | [Mini RAG con la política, evaluación y seguridad](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/notebooks/S12_06_mini_rag.ipynb) | 45 min |
| 11 | 💻 Práctica | Terminad los cuadernos pendientes, incluido el apartado «en casa», y poneos al día | 10 min |
| 12 | 📖 Teoría | [Autoencoders y modelos generativos](presentaciones/S12.4_Autoencoders_y_modelos_generativos.pdf) | 10 min |
| 13 | 🎯 Reto | [Reparto y plan (paso 1) y datos y modelos de las partes A (reseñas) y C (asistente) (paso 2)](guia/Reto_Sprint_12.md) | 1 h 5 min |

**Miércoles 25/11**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 14 | 🎯 Reto | [Parte B (ocupación), evaluación y seguridad del asistente y cierre (pasos 2–4)](guia/Reto_Sprint_12.md) | 1 h 5 min |
| 15 | 📝 Test | [**Test de M4** (redes neuronales), solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/tests/test_M4.html) | 30 min |
| 16 | 📖 Teoría | [Visualizar y comunicar resultados (Sprint 13, integrado; versión rápida)](../S13/presentaciones/S13.1_Visualizar_y_comunicar_resultados.pdf) | 10 min |
| 17 | 💻 Práctica | [Matriz de confusión, ROC/PR, importancia, umbral y coste](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_01_visualizacion_resultados.ipynb) | 35 min |
| 18 | 🎯 Reto | [Reto del Sprint 13](../S13/guia/Reto_Sprint_13.md): elegir el modelo y los costes → tres o cuatro gráficos → titular y viñetas. Usad el [cuaderno plantilla](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S13/notebooks/S13_02_plantilla_informe_visual.ipynb) y la [plantilla del informe](../S13/plantillas/plantilla_informe_visual.md) | 25 min |
| 19 | 🔔 Ceremonia | Entrega en `sprint-12/` (y el informe visual en `sprint-13/`), autoevaluación y coevaluación, review y retrospectiva | 35 min |

<!--orden:fin-->

## Entrega / Reto · «Escuchar al cliente»

📄 [Reto en PDF](guia/Reto_Sprint_12.pdf) · [ecofriendly](guia/Reto_Sprint_12_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

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

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mié 25/11
- [ ] Serie partida **por fecha** y con **baseline** en la tabla.
- [ ] Escalado y vectorización ajustados solo con entrenamiento.
- [ ] El asistente cita la fuente y responde «No consta…» cuando no sabe.
- [ ] Probados 3 ataques de prompt injection.
- [ ] Ninguna clave en el código ni en el repositorio.
- [ ] Todo se ejecuta de arriba abajo, sin errores y sin internet.
- [ ] Entregable subido a la carpeta `sprint-12/` del repositorio del equipo.
