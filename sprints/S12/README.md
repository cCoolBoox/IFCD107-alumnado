# Sprint 12 · Lenguaje, secuencias y modelos generativos

**Pregunta guía:** ¿qué dicen los clientes y qué pasará mañana?

**Fechas:** 20–25/11 · **18 horas:** 5 h de teoría (T) · 8 h de práctica (P) · 5 h de reto PBL

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_12.pdf`](Guia_Sprint_12.pdf)
- 🖥️ **S12.1 · RNN LSTM GRU y series temporales:** [`S12.1_RNN_LSTM_GRU_y_series_temporales.pdf`](presentaciones/S12.1_RNN_LSTM_GRU_y_series_temporales.pdf)
- 🖥️ **S12.2 · NLP clasico y embeddings:** [`S12.2_NLP_clasico_y_embeddings.pdf`](presentaciones/S12.2_NLP_clasico_y_embeddings.pdf)
- 🖥️ **S12.3 · Transformers y LLM:** [`S12.3_Transformers_y_LLM.pdf`](presentaciones/S12.3_Transformers_y_LLM.pdf)
- 🖥️ **S12.4 · Autoencoders y modelos generativos:** [`S12.4_Autoencoders_y_modelos_generativos.pdf`](presentaciones/S12.4_Autoencoders_y_modelos_generativos.pdf)

**Contenidos (Módulo 4):** UD 4.7 redes recurrentes y series temporales · UD 4.8 NLP clásico y embeddings · UD 4.9 Transformers, LLM y RAG · UD 4.10 autoencoders y modelos generativos.
**Evaluación:** test de M4 + entrega del reto con la rúbrica de 4 criterios.

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

## Prácticas (≈ 7 h 10 min + tiempo de repaso)
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S12_01_series_temporales` | Serie temporal: baselines, descomposición, ARIMA/SARIMAX | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/S12_01_series_temporales.ipynb) |
| `S12_02_redes_recurrentes` | RNN, LSTM y GRU en Keras vs. baseline | 1 h | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/S12_02_redes_recurrentes.ipynb) |
| `S12_03_nlp_clasico` | Reseñas: limpieza, TF-IDF, sentimiento, temas y n-gramas | 1 h 10 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/S12_03_nlp_clasico.ipynb) |
| `S12_04_embeddings_lsa` | Embeddings con LSA y buscador de reseñas parecidas | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/S12_04_embeddings_lsa.ipynb) |
| `S12_05_transformers_atencion` | Tokens, atención paso a paso, temperatura (+ Hugging Face opcional) | 1 h 10 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/S12_05_transformers_atencion.ipynb) |
| `S12_06_mini_rag` | Mini RAG con la política, evaluación y seguridad | 1 h 30 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/S12_06_mini_rag.ipynb) |
| `S12_07_autoencoder_generativos` | Autoencoder para anomalías; idea de GAN y difusión | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S12/S12_07_autoencoder_generativos.ipynb) |

**Cómo trabajar:** ejecuta las celdas en orden. Cada ejercicio tiene una pista y, justo debajo, una comprobación automática (`assert`): si falla, te dice qué revisar. Las celdas marcadas **OPCIONAL / NO VERIFICADO** usan internet o programas externos: puedes saltártelas sin perder nada.

**Regla de oro del sprint:** nunca escribas claves de API en el código. Si usas un servicio externo, la clave se lee de una variable de entorno o con `getpass`.

---

# Reto PBL: «Escuchar al cliente»

## Escena del cliente
TurisData Canarias recibe cada semana decenas de reseñas y decenas de mensajes de huéspedes con las mismas preguntas ("¿hasta cuándo puedo cancelar?", "¿admiten perros?"). La dirección no puede leerlo todo ni contestar a mano.
Quiere tres cosas: **saber qué opinan y de qué se quejan** sus clientes, **prever la ocupación de la próxima semana** para organizar personal y compras, y **probar un asistente** que responda con la política del alojamiento sin inventar nada.
Tenéis que demostrar que se puede hacer con datos, con sentido común y con cuidado.

## Qué se entrega y en qué formato
Una **carpeta (o zip) por equipo** con estos cuatro elementos:

| Nº | Entregable | Formato | Contenido mínimo |
|---|---|---|---|
| 1 | **Informe de reseñas** | `informe_resenas.md` o PDF, **2 páginas máx.** (plantilla en `plantilla_informe_cliente.md`) | Sentimiento global, 3 temas más criticados y 3 más valorados (con cifras y 1 gráfico), 5 citas reales, **3 recomendaciones accionables**, límites del análisis |
| 2 | **Modelo de ocupación** | Notebook `.ipynb` que se ejecute de arriba abajo | Partición temporal, **baseline**, un modelo estadístico o una red, tabla de MAE, gráfico de previsión a 7 días, y una frase para el cliente |
| 3 | **Demo del asistente RAG** | Notebook con la demo **+ tabla de evaluación** (`.csv` o tabla en el informe) | Las 20 preguntas de referencia + **5 preguntas propias** (una sin respuesta en la política) + **3 intentos de ataque** y su resultado |
| 4 | **Nota de IA responsable** | 1 página en `.md` | Riesgos concretos (alucinación, datos personales, prompt injection, sesgos) y **qué medidas habéis aplicado y cómo las habéis medido** |

Un `LEEME.md` de 5 líneas explica cómo ejecutar todo (versiones de librerías incluidas).

## Datos y recursos
`datos/resenas.csv` · `datos/ocupacion_diaria.csv` · `datos/politica_alojamiento.md` · `datos/preguntas_referencia.csv` · tus notebooks S12_01 a S12_07. **Los datos son sintéticos**: dilo en el informe.

## Restricciones
- **Tiempo:** 5 h de reto (más lo que avances en las prácticas). Se presenta en la *review* (5 min por equipo).
- **Herramientas:** Python y las librerías del curso. Todo debe poder ejecutarse **sin internet**. El LLM real (Ollama o API) es **opcional**: si lo usáis, indicad que no se ha podido verificar por el docente y **no incluyáis claves**.
- **Presupuesto:** 0 €. Cuotas gratuitas solo si vuestro equipo lo decide y sin datos personales.
- **Prohibido:** partir la serie al azar, escalar o vectorizar con todos los datos antes de partir, y dar cifras del informe que no salgan del código.

## Criterios de evaluación (rúbrica de retos del curso, 0–4 en cada uno)
| Criterio | Qué miraremos en este reto |
|---|---|
| **Corrección técnica** | Partición temporal y sin fuga; baseline comparado con el modelo; clasificador de sentimiento evaluado en prueba; RAG que recupera y cita fuente; métricas bien calculadas. Para un 4: alternativas comparadas (p. ej. SARIMAX vs. GRU, umbrales del asistente) y justificadas |
| **Reproducibilidad** | El notebook se ejecuta de arriba abajo con `SEMILLA = 42`; `LEEME.md` claro. Para un 4: versiones fijadas y datos o script incluidos |
| **Análisis y comunicación al cliente** | El informe se entiende sin saber programar: cifras interpretadas, recomendaciones que el cliente puede ejecutar el lunes, y **límites** explicados (datos sintéticos, error medio de la previsión) |
| **IA responsable** | Riesgos específicos (no genéricos): qué pasa con la pregunta sin respuesta, con datos personales en reseñas, con un texto que intenta manipular al asistente. Para un 4: medidas aplicadas y **medidas evaluadas** (p. ej. «el filtro bloqueó 3 de 3 ataques y ninguna frase legítima») |

## Pasos sugeridos
- **Hora 1 · Reparto y plan.** Roles (una persona por parte: reseñas, ocupación, asistente, IA responsable y coordinación). Repasad la rúbrica y decidid la pregunta de negocio de cada parte.
- **Horas 2–3 · Datos y modelos.** Reseñas: sentimiento y temas, gráficos y citas. Ocupación: baseline y modelo, MAE por semana. Asistente: troceado, recuperación y umbral.
- **Hora 4 · Evaluación y seguridad.** Evaluad el asistente con las 20 preguntas y vuestras 5; probad 3 ataques; anotad qué falla y qué arreglasteis.
- **Hora 5 · Cierre.** Redactad el informe, la nota de IA responsable y el `LEEME.md`; ejecutad todo desde cero y ensayad los 5 minutos de presentación.

## Qué se enseña en la review
Cada equipo presenta **una cifra, un gráfico y una demo** (5 min): (1) cuánto se equivoca la previsión frente al método simple; (2) el tema más criticado y qué haría el cliente; (3) una pregunta que el asistente responde bien, **la que no sabe** y un ataque frenado. Después, 3 min de preguntas del docente y de otros equipos.

## Checklist Definition of Done
- [ ] La serie se parte **por fecha** y hay un **baseline** en la tabla de resultados.
- [ ] Escalado y vectorización se ajustan **solo con entrenamiento**.
- [ ] Sentimiento evaluado en prueba (exactitud y matriz de confusión) y temas con ejemplos reales.
- [ ] El asistente **cita la fuente** y responde «No consta…» a la pregunta sin respuesta.
- [ ] Evaluación con **aciertos, sin fuente y alucinaciones** sobre 20 + 5 preguntas.
- [ ] Probados **3 ataques** de prompt injection y descrito el resultado.
- [ ] **Ninguna clave** en el código ni en el repositorio.
- [ ] Informe de 2 páginas con 3 recomendaciones y los límites del análisis.
- [ ] Todo se ejecuta de arriba abajo, sin errores y **sin internet**.
- [ ] Nota de IA responsable entregada.

## Recursos
1. Documentación de `statsmodels` sobre SARIMAX y de Keras sobre RNN/LSTM/GRU (guías oficiales).
2. Documentación de `scikit-learn`: *Working with text data* (TF-IDF y clasificación de texto).
3. Guía de Hugging Face *Transformers*: pipelines de sentimiento y *zero-shot* (para la parte opcional en Colab).
4. OWASP *Top 10 for LLM Applications*: riesgos de seguridad (prompt injection).
5. Documentación de Ollama (LLM en local) para probar el asistente con un modelo real (opcional).
