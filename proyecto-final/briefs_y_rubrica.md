# IFCD107 · Proyecto final (M9)
## Briefs, requisitos, entregables y rúbrica

**Acción 25-38/012242 · Sprints 14–17 · 25/11 – 14/12/2026 · 60 h + 3 h de Storytelling**

---

## 1. Reglas comunes del proyecto

**Equipos:** 3–4 personas, formados en el Sprint 0 (pueden reajustarse una vez, hasta el 26/11).
**Elección:** cada equipo elige **uno de los 4 briefs** o presenta un **brief libre** (sección 4). Dos equipos pueden elegir el mismo brief, pero con enfoques distintos (cada equipo define su propia pregunta y métrica).
**Rol del docente:** cliente y Product Owner. Los briefs son abiertos a propósito: el equipo decide alcance, datos concretos y técnicas dentro de los mínimos.

### Requisitos mínimos (obligatorios en todos los proyectos)

| # | Requisito | Módulo relacionado |
|---|---|---|
| R1 | Problema definido con **métrica de éxito de negocio y métrica técnica** | M9, Design Thinking |
| R2 | Datos reales con **fuente y licencia documentadas**; EDA y informe de calidad del dato | M2 |
| R3 | **Baseline** simple + **al menos 3 modelos** comparados con validación correcta (sin fuga de datos; partición temporal si hay series) | M3, M4 |
| R4 | **Al menos un modelo de redes neuronales** (o un LLM/RAG en el brief 3) | M4 |
| R5 | Evaluación con **visualizaciones** (curvas, matriz de confusión, importancia de variables, SHAP o Grad-CAM según el caso) | M5 |
| R6 | **IA responsable:** checklist ético del Sprint 1 actualizado, análisis de sesgos y limitaciones, clasificación de riesgo (RGPD / AI Act) | M8 |
| R7 | **Demostrador ejecutable** (app Streamlit/Gradio, notebook interactivo o endpoint) | M7, M9 |
| R8 | **Repositorio Git** reproducible (README, requisitos, datos o script de descarga) con commits de todos los integrantes | M1b |
| R9 | **Evidencia Scrum:** tablero, backlog, planning/review/retro de cada sprint | Softskills |
| R10 | **Memoria técnica** (10–15 páginas) | M9 |
| R11 | **Defensa** en la que **todos los integrantes** presentan y responden preguntas | M9, Storytelling |

### Hitos y entregables por sprint

| Sprint | Fechas | Entregable | Hito |
|---|---|---|---|
| 14 · Reto, equipo y datos | 25–30/11 | Ficha de proyecto (1 pág., anexo A) + datos + EDA + baseline + backlog + plan ético | **26/11:** elección de brief. **27/11:** ficha aprobada por el docente (go / no-go) |
| 15 · Modelado y experimentos | 1–3/12 | ≥ 3 modelos comparados + registro de experimentos | 3/12: modelo candidato elegido |
| 16 · Evaluación, IA responsable y entrega | 4–10/12 | Demostrador + evaluación + análisis de sesgos + **memoria** | **10/12, 14:30:** congelación de repositorio y memoria |
| 17 · Storytelling, ensayos y defensa | 11 y 14/12 | Presentación (máx. 12 diapositivas) | **11/12:** ensayo general. **14/12:** defensa |

Los cambios de alcance después del 27/11 se negocian en la review del sprint con el docente.

---

## 2. Briefs

### Brief 1 · Demanda turística y presión sobre el territorio
**Cliente:** consejería o cabildo que quiere anticipar la llegada de visitantes por isla y mes para planificar servicios (transporte, residuos, alojamiento).
**Pregunta guía:** ¿podemos predecir la llegada de turistas con 3–6 meses de antelación y qué factores la explican?

- **Datos candidatos (a validar antes del 16/10):** estadísticas de turismo del ISTAC y Frontur-Canarias, datos abiertos de datos.gob.es, meteorología de AEMET OpenData, calendario de festivos y eventos.
- **Tipo de problema:** previsión de series temporales + segmentación de mercados emisores.
- **Técnicas esperadas:** baseline estacional; regresión regularizada; Random Forest/XGBoost con variables de calendario; **LSTM/GRU**; clustering de mercados emisores; PCA.
- **Entregable específico:** panel con la previsión, su intervalo de incertidumbre y las variables más influyentes; nota de recomendaciones para el cliente.
- **Métrica orientativa:** MAPE/MAE frente al baseline estacional en un periodo de test posterior al entrenamiento (partición temporal obligatoria).
- **Nivel avanzado:** predicción por isla y mercado; incorporar reseñas o búsquedas web como variable externa.
- **Riesgos éticos/RGPD:** datos agregados (riesgo bajo); explicar que las predicciones no deben usarse para restringir el acceso o discriminar mercados; cuidado con la eventualidad de sucesos atípicos (p. ej. crisis) que rompen la serie.

### Brief 2 · Salud de cultivos con visión por computador
**Cliente:** cooperativa agraria que quiere una herramienta para que el agricultor fotografíe una hoja y reciba un primer diagnóstico orientativo.
**Pregunta guía:** ¿con qué fiabilidad se distingue una hoja sana de una enferma, y cuándo no debemos fiarnos del modelo?

- **Datos candidatos (a validar):** PlantVillage (Kaggle o TensorFlow Datasets) para los cultivos disponibles (p. ej. tomate, vid); fotos propias del equipo como **conjunto de prueba en condiciones reales**.
- **Tipo de problema:** clasificación de imágenes (opcionalmente detección o segmentación).
- **Técnicas esperadas:** CNN desde cero como baseline; ***transfer learning*** (ResNet/MobileNet/EfficientNet); *data augmentation*; **Grad-CAM**; análisis de errores por clase.
- **Entregable específico:** app donde se sube una foto y se devuelve la clase con **nivel de confianza y aviso de incertidumbre**.
- **Métrica orientativa:** F1 macro; y sobre todo **caída de rendimiento entre las imágenes del dataset y las fotos reales del equipo** (análisis de generalización).
- **Nivel avanzado:** detección de fuera de distribución (rechazar imágenes que no son hojas); modelo ligero para móvil.
- **Riesgos éticos:** sesgo del dataset (fotos de laboratorio con fondo uniforme); riesgo de sobreconfianza del usuario; el diagnóstico es orientativo, no sustituye a un técnico agrícola.
- **Recursos:** requiere GPU (Colab); planificar el tiempo de entrenamiento.

### Brief 3 · Asistente de orientación sobre Formación Profesional
**Cliente:** centro de FP o asociación de formación que quiere un asistente que responda dudas sobre ciclos, requisitos de acceso y salidas laborales.
**Pregunta guía:** ¿puede un asistente basado en LLM responder con datos fiables sin inventar, y cómo lo medimos?

- **Datos candidatos (a validar licencia y uso):** catálogo oficial de títulos de FP y normativa publicados por organismos oficiales; preguntas frecuentes del propio centro (proporcionadas por el docente).
- **Tipo de problema:** NLP con **recuperación aumentada (RAG)**: chunking, *embeddings*, búsqueda semántica y generación con LLM (API o modelo abierto de Hugging Face).
- **Técnicas esperadas:** baseline por palabras clave (TF-IDF/BM25); *embeddings* + búsqueda vectorial; LLM con RAG; comparativa de configuraciones (tamaño de chunk, número de fragmentos, modelo).
- **Entregable específico:** chat funcional con **citas a la fuente** de cada respuesta.
- **Evaluación obligatoria:** conjunto de al menos **40 preguntas de referencia** creado por el equipo; medir aciertos, respuestas sin fuente y **alucinaciones** (respuestas no respaldadas por los documentos).
- **Nivel avanzado:** reformulación de consultas; evaluación automática con un LLM como juez, contrastada con evaluación manual.
- **Riesgos éticos:** alucinaciones y desinformación al alumnado; privacidad (no se procesan datos personales del alumnado); transparencia de que es un asistente automático; **no debe tomar decisiones sobre personas**. Clasificar el riesgo según el AI Act.
- **Recursos:** claves de API o modelos abiertos ligeros; controlar coste y límites de uso.

### Brief 4 · Previsión de demanda eléctrica e integración de renovables
**Cliente:** empresa energética insular que quiere anticipar la demanda diaria para ajustar la generación y aprovechar mejor las renovables.
**Pregunta guía:** ¿podemos predecir la demanda de las próximas 24 h mejor que un modelo de referencia, y cuánto ayuda la meteorología?

- **Datos candidatos (a validar):** datos abiertos de demanda y generación por sistema insular de Red Eléctrica (REData); meteorología de AEMET OpenData; calendario laboral y festivos.
- **Tipo de problema:** previsión de series temporales con variables exógenas.
- **Técnicas esperadas:** baseline de persistencia estacional (mismo día y hora de la semana anterior); regresión con variables de calendario; Gradient Boosting/XGBoost; **LSTM/GRU**; comparativa con y sin variables meteorológicas.
- **Entregable específico:** demostrador que muestra la demanda real frente a la prevista y el error por franja horaria.
- **Métrica orientativa:** MAE y MAPE frente al baseline en un periodo de test posterior; error en horas punta.
- **Nivel avanzado:** predicción de generación renovable (solar o eólica); escenarios de mayor penetración renovable.
- **Riesgos éticos:** datos agregados (riesgo bajo); impacto de errores en decisiones de red (coste de infra o de sobrepredicción); explicar límites en eventos extraordinarios.

---

## 3. Comparativa rápida de briefs

| Brief | Núcleo técnico | Tipo de dato | Dificultad de datos | Carga de cómputo |
|---|---|---|---|---|
| 1 Turismo | Series temporales + clustering | Tabular / serie | Media | Baja |
| 2 Cultivos | CNN y transfer learning | Imágenes | Baja (datasets grandes) | Alta (GPU) |
| 3 Asistente FP | RAG y evaluación de LLM | Texto | Media (preparar corpus) | Media |
| 4 Energía | Series temporales + LSTM | Tabular / serie | Media | Media |

---

## 4. Brief libre

Un equipo puede proponer su propio proyecto si presenta la **ficha de proyecto (anexo A)** antes del **26/11** y cumple:

1. Pregunta de negocio clara con métrica de éxito.
2. Datos **reales, accesibles y con licencia** ya identificados (no se aceptan proyectos "a la espera de datos").
3. Cumple **todos los requisitos mínimos R1–R11**.
4. Dificultad comparable a los briefs anteriores (se descartan problemas triviales o irrealizables en 55 h).
5. No usa datos personales sensibles ni de terceros sin autorización (RGPD).

El docente responde go / no-go el **27/11**.

---

## 5. Rúbrica de evaluación del proyecto (100 puntos)

**Niveles:** Insuficiente (< 50 % del criterio) · Suficiente (50–69 %) · Bueno (70–89 %) · Excelente (≥ 90 %).

| Criterio | Peso | Insuficiente | Suficiente | Bueno | Excelente |
|---|---|---|---|---|---|
| **A. Problema y valor de negocio** | 10 | Problema vago o sin métrica | Problema definido, métrica poco justificada | Métricas de negocio y técnica coherentes | Además vincula el resultado con una decisión concreta del cliente y cuantifica el valor |
| **B. Datos y EDA** | 10 | Sin documentar fuente o con datos no válidos | EDA básico, limpieza sin justificar | EDA completo, defectos y causas documentados | Además valida la calidad, trata sesgos de muestreo y documenta el linaje del dato |
| **C. Modelado y experimentación** | 20 | Menos de 3 modelos o sin baseline | Baseline y 3 modelos, validación con fallos menores | Comparación rigurosa, ajuste de hiperparámetros, registro de experimentos | Además controla fuga de datos, justifica la elección con coste/beneficio y explica el porqué de los resultados |
| **D. Evaluación y visualización** | 10 | Solo una métrica global | Métricas adecuadas y gráficos básicos | Análisis de errores y gráficos claros | Además interpreta el modelo (SHAP/Grad-CAM/curvas) y comunica la incertidumbre |
| **E. IA responsable** | 10 | Sin análisis ético | Checklist rellenado sin aplicarlo | Sesgos, limitaciones y riesgo RGPD/AI Act identificados | Además propone y aplica medidas de mitigación y las evalúa |
| **F. Demostrador y reproducibilidad** | 10 | No funciona o no se puede reproducir | Funciona en el entorno del equipo | Reproducible desde el README | Además incluye pruebas, versiones fijas y manejo de errores del usuario |
| **G. Trabajo en equipo y metodología** | 10 | Sin evidencia Scrum ni reparto | Tablero y ceremonias parciales | Sprints completos, roles rotados, commits repartidos | Además muestra mejora entre retrospectivas y coevaluación equilibrada |
| **H. Memoria técnica** | 5 | Incompleta o copiada | Estructura completa, redacción irregular | Clara, con figuras y referencias | Además autocontenida, concisa y con conclusiones accionables |
| **I. Defensa (Storytelling, demo y preguntas)** | 15 | No presenta todo el equipo o no responde | Discurso correcto, demo con fallos | Relato claro, demo estable, respuestas sólidas | Además relato memorable para público no técnico, gestiona el tiempo y responde con datos |

### Criterios de "Apto" (el programa exige Apto / No Apto)

Para obtener **Apto** en el módulo M9 se deben cumplir **todos**:

1. Nota del proyecto **≥ 50 / 100**.
2. **Criterio C** al menos en "Suficiente" (sin modelado no hay proyecto).
3. **Criterio E** al menos en "Suficiente" (la IA responsable es un mínimo, no una opción).
4. **Presentar en la defensa** y responder a al menos una pregunta individual.
5. Contribución individual verificable (commits y coevaluación).

### Nota individual

La nota del equipo se ajusta con un **factor individual (0,8 – 1,1)** a partir de la coevaluación (anexo B) y la contribución en el repositorio. Un integrante sin aportación verificable puede quedar **No Apto** aunque el equipo apruebe.

---

## 6. Defensa (14/12)

Tiempo total: 2 h. Se reservan 10 min para cambios de equipo; el resto se reparte.

| Nº de equipos | Tiempo por equipo |
|---|---|
| 5 | 22 min |
| 6 | 18 min |
| 7 | 15 min |
| 8 | 13 min |

**Reparto sugerido en cada turno:** 60 % presentación · 20 % demostración · 20 % preguntas del tribunal.
**Estructura recomendada (Storytelling):** contexto y problema → qué hicimos → qué aprendimos (resultados) → demo → límites y riesgos → qué proponemos al cliente.
**Reglas:** todos los integrantes hablan; la demo se prueba antes (plan B grabado en vídeo); las preguntas de ampliación pueden dirigirse a cualquier integrante.
**Si hay más de 7 equipos:** valorar adelantar parte de las defensas a la tarde del 11/12 en lugar de los ensayos, sin perder el ensayo general.

---

## 7. Rúbrica de los retos PBL (Sprints 1–13)

Cada entregable se evalúa de 0 a 4 en estos cuatro criterios (los pesos son iguales); su media alimenta el bloque de "ejercicios y entregas".

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| **Corrección técnica** | Errores que invalidan el resultado | Correcto con fallos menores | Correcto y bien justificado | Correcto, justificado y con alternativas comparadas |
| **Reproducibilidad** | No se puede volver a ejecutar | Se ejecuta con ayuda | Se ejecuta desde el README | Además incluye datos o script y versiones fijas |
| **Análisis y comunicación al cliente** | Solo código o cifras sin interpretar | Interpretación básica | Conclusiones claras para el cliente | Recomendación accionable con límites explicados |
| **IA responsable** | No se considera | Menciones genéricas | Riesgos específicos identificados | Medidas aplicadas y evaluadas |

---

## Anexo A · Ficha de proyecto (1 página, entrega antes del 27/11)

1. **Equipo** y roles iniciales (Scrum Master, responsable técnico, responsable de datos, responsable de IA responsable).
2. **Brief elegido** (o propuesta libre) y **pregunta de negocio** en una frase.
3. **Cliente y decisión** que se apoyará con el resultado.
4. **Datos:** fuente, licencia, tamaño, variables clave y limitaciones previstas.
5. **Métrica de éxito** (negocio y técnica) y **baseline** previsto.
6. **Modelos previstos** (≥ 3, incluyendo redes neuronales/LLM según el brief).
7. **Demostrador previsto** y tecnología.
8. **Riesgos** (datos, cómputo, ética) y mitigación.
9. **Backlog inicial** (10–15 historias) y objetivo de cada sprint.

## Anexo B · Coevaluación (por integrante, al cierre del Sprint 16)

Cada persona valora a las demás y a sí misma de 1 a 4 en: **contribución técnica**, **cumplimiento de tareas**, **comunicación**, **colaboración** y **fiabilidad**. Se añade un comentario obligatorio para puntuaciones de 1 o de 4. El docente contrasta la coevaluación con el historial de commits y el tablero.
