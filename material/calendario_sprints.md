# IFCD107 · Especialista en Inteligencia Artificial
## Plan por sprints: teoría + práctica + PBL

**Acción 25-38/012242 · 16/10/2026 – 14/12/2026 · 08:30–14:30 (6 h/día) · 230 h**


---

## 1. Modelo de trabajo

**Escenario común (hilo conductor).** Cada equipo (3–4 personas) es una **consultora de IA**. El docente hace de **cliente y Product Owner**: *TurisData Canarias*, empresa ficticia de alojamiento y experiencias turísticas que quiere incorporar IA. Cada sprint cierra con un **reto PBL** sobre ese cliente, que reutiliza los datos y el trabajo del sprint anterior. Datos: candidatos a validar antes del curso (ISTAC/Frontur, datos.gob.es, Kaggle, Inside Airbnb si hay región canaria disponible). El proyecto final (Sprints 14–17) lo eligen los equipos entre 3–4 briefs sectoriales.

**Cada sprint tiene tres tipos de hora:**

| Tipo | Qué es |
|---|---|
| **T · Teoría** | Exposición con presentación, demostraciones, ejemplos |
| **P · Práctica guiada** | Ejercicios y laboratorios con el docente, individual o en parejas |
| **PBL** | Reto del cliente en equipo: planificación, trabajo, entrega, review y retrospectiva |

**Ceremonias (dentro de las horas del sprint, no suman aparte):**
- *Planning:* primeros 30 min del sprint. Se toma del backlog el reto.
- *Daily:* 10 min al inicio de cada sesión.
- *Review + retrospectiva:* última hora del sprint. Cada equipo enseña su entregable (5 min) y se cierra con retro breve.
- *Roles rotativos:* Scrum Master y responsable técnico cambian cada sprint.
- **Definition of Done común:** entregable reproducible (notebook o documento), README, subido a Git, autoevaluación y coevaluación rellenadas.

---

## 2. Vista general

| Sprint | Título | Módulos / UD | Horas | T | P | PBL | Fechas |
|---|---|---|---|---|---|---|---|
| **BLOQUE A · Sin Python (46 h)** | | | | | | | |
| 0 | Arranque ágil | Scrum + Design Thinking | 7 | 3 | 2 | 2 | 16–19/10 |
| 1 | Qué es la IA, cómo aprende y cómo usarla bien | M1a (UD 1–3) + M8 | 15 | 8 | 4 | 3 | 19–21/10 |
| 2 | Las matemáticas y la estadística detrás | M1a (UD 4–6) | 10 | 5 | 3 | 2 | 21–23/10 |
| 3 | Del dato al modelo en la nube | M6a + M7 | 14 | 5 | 5 | 4 | 23–27/10 |
| **BLOQUE B · Python (121 h, bloque continuo)** | | | | | | | |
| 4 | Python para IA | M1b (UD 1–4) | 10 | 3 | 5 | 2 | 27–29/10 |
| 5 | Matemáticas y estadística en código | M1b (UD 5–7) + M6b | 13 | 4 | 6 | 3 | 29/10–3/11 |
| 6 | Datos listos para modelar | M2 + M3 (UD 3.1–3.2) | 11 | 4 | 4 | 3 | 3–5/11 |
| 7 | ML supervisado: regresión y clasificación | M3 (UD 3.3–3.5) | 12 | 4 | 5 | 3 | 5–9/11 |
| 8 | Árboles, ensembles y SVM | M3 (UD 3.6–3.8) | 11 | 3 | 5 | 3 | 9–11/11 |
| 9 | Segmentar, recomendar y aprender por refuerzo | M3 (UD 3.9–3.12) | 11 | 3 | 5 | 3 | 11–12/11 |
| 10 | Redes neuronales bien entrenadas | M4 (UD 4.1–4.3) | 15 | 5 | 6 | 4 | 13–17/11 |
| 11 | Visión por computador | M4 (UD 4.4–4.6) | 17 | 5 | 7 | 5 | 17–20/11 |
| 12 | Lenguaje, secuencias y modelos generativos | M4 (UD 4.7–4.10) | 18 | 5 | 8 | 5 | 20–25/11 |
| 13 | Contar lo que hace el modelo | M5 | 3 | 1 | 1 | 1 | 25/11 |
| **BLOQUE C · Proyecto de cierre (63 h)** | | | | | | | |
| 14 | Proyecto · Reto, equipo y datos | M9 | 19 | 1 | 3 | 15 | 25–30/11 |
| 15 | Proyecto · Modelado y experimentos | M9 | 18 | 1 | 3 | 14 | 1–3/12 |
| 16 | Proyecto · Evaluación, IA responsable y entrega | M9 | 18 | 1 | 3 | 14 | 4–10/12 |
| 17 | Proyecto · Storytelling, ensayos y defensa | M9 + Storytelling | 8 | 1 | 2 | 5 | 11 y 14/12 |
| | **Total** | | **230** | **62** | **77** | **91** | |

Comprobaciones: Python continuo del 27/10 al 25/11 (Sprints 4–13) = 121 h. M9 = 55 h (Sprints 14–16) + 3 h de ensayos + 2 h de defensa = **60 h**. Storytelling = **3 h** (1 T + 2 P del Sprint 17). Softskills = 4 + 3 + 3 = 10 h.

---

# BLOQUE A · SIN PYTHON

## Sprint 0 · Arranque ágil (7 h · 16–19/10)
**Pregunta guía:** ¿cómo vamos a trabajar y con quién?

- **Teoría (3 h):** Agile frente al enfoque tradicional y Manifiesto Ágil (1 h); roles, artefactos y ceremonias de Scrum (1 h); fases del Design Thinking (1 h).
- **Práctica (2 h):** simulación de un sprint corto (1 h); mapa de empatía y "How might we" sobre un usuario ficticio (1 h).
- **PBL (2 h) · Reto: "Constituir la consultora".** Formar equipos, nombre, acuerdo de trabajo, tablero (Trello o similar), Definition of Done y backlog del curso. Entrevista de descubrimiento al cliente (el docente) y primer mapa de empatía de *TurisData*.
- **Entregable:** tablero + acuerdo de equipo + mapa de empatía.
- **Evaluación:** rúbrica de equipo (roles, tablero, acuerdo).

## Sprint 1 · Qué es la IA, cómo aprende y cómo usarla bien (15 h · 19–21/10)
**Pregunta guía:** ¿dónde puede ayudar la IA al cliente y qué riesgos tiene?

- **Teoría (8 h):** M1a UD 1a.1 introducción, modalidades y casos de uso (2 h); UD 1a.2 panorama de algoritmos y CRISP-DM (2 h); UD 1a.3 tipos de aprendizaje, overfitting y evaluación (2 h); M8 ética, sesgo y AI Act (2 h, repartidas entre las sesiones del sprint).
- **Práctica (4 h):** clasificación "a mano" con tarjetas para entender el sobreajuste; elegir familia de algoritmos en 6 problemas; debate guiado de casos éticos con roles (M8 UD 8.4).
- **PBL (3 h) · Reto: "Auditoría de oportunidades de IA".** Proponer 5 casos de uso para *TurisData*, clasificados por modalidad, tipo de aprendizaje y datos necesarios, con **checklist ético** (M8 UD 8.5) y priorización.
- **Entregable:** informe de oportunidades (2–3 páginas) + checklist ético.
- **Notas:** el checklist se reutiliza en el proyecto final. Verificar el calendario vigente del AI Act antes de impartir.

## Sprint 2 · Las matemáticas y la estadística detrás (10 h · 21–23/10)
**Pregunta guía:** ¿en qué se apoyan los modelos y cuándo no debemos fiarnos de un dato?

- **Teoría (5 h):** UD 1a.4 álgebra lineal, derivadas y gradiente (2,5 h); UD 1a.5 estadística descriptiva, probabilidad, Bayes, muestreo y sesgo (2 h); UD 1a.6 ecosistema de software (0,5 h).
- **Práctica (3 h):** ejercicios en papel y con Desmos/GeoGebra; interpretación de estadísticas engañosas; alta en Colab, GitHub y cuentas AWS (antes del 22/10).
- **PBL (2 h) · Reto: "¿Nos fiamos de este informe?".** Auditar un informe del cliente con errores estadísticos (correlación frente a causalidad, paradoja de Simpson, muestreo sesgado) y rehacer los cálculos.
- **Entregable:** dictamen de auditoría + hoja de ejercicios.
- **Evaluación:** test corto de M1a (conceptos, mates, estadística).

## Sprint 3 · Del dato al modelo en la nube (14 h · 23–27/10)
**Pregunta guía:** ¿podemos tener un primer modelo funcionando, sin programar?

- **Teoría (5 h):** M6a modelo relacional, SQL y CRUD (2 h); nociones de DBA y buenas prácticas (1 h); NoSQL (1 h); M7 introducción a AutoML y MLOps (1 h, T de UD 7.1).
- **Práctica (5 h):** consultas SQL y CRUD en SQLite/PostgreSQL; mismo dato en MongoDB; carga y exploración de datos en SageMaker (UD 7.2); lanzar un experimento AutoML (UD 7.3).
- **PBL (4 h) · Reto: "Primer modelo en producción".** El cliente entrega un dataset de reservas y cancelaciones. Modelarlo en una BD, entrenar un modelo AutoML de **predicción de cancelaciones**, desplegar un endpoint, consumirlo por API y **apagar los recursos**.
- **Entregable:** informe del mejor modelo + evidencia de la llamada al endpoint + informe de costes.
- **Requisito:** cuentas AWS con SageMaker operativas antes del 22/10 y presupuesto de costes controlado.

---

# BLOQUE B · PYTHON (121 h continuas)

## Sprint 4 · Python para IA (10 h · 27–29/10)
**Pregunta guía:** ¿cómo automatizamos lo que hemos hecho a mano?

- **Teoría (3 h):** UD 1b.1 entorno (venv, pip, Jupyter, VS Code, Git); fundamentos del lenguaje, estructuras de datos, funciones, módulos, ficheros, excepciones y POO (comparativa con Java).
- **Práctica (5 h):** ejercicios progresivos de sintaxis, estructuras y funciones; lectura y escritura de CSV/JSON; primeras clases.
- **PBL (2 h) · Reto: "Herramientas internas".** Un script que lee el CSV de reservas del cliente, calcula KPIs (ocupación, ingreso medio, cancelaciones), gestiona errores y exporta un JSON.
- **Entregable:** repositorio con README y pruebas sencillas.
- **Evaluación:** ejercicios de Python (autocorregidos con asserts).

## Sprint 5 · Matemáticas y estadística en código (13 h · 29/10–3/11)
**Pregunta guía:** ¿podemos demostrar con código lo que vimos en teoría?

- **Teoría (4 h):** UD 1b.5 NumPy y álgebra lineal (vectorización, *broadcasting*); UD 1b.6 derivadas y descenso del gradiente; UD 1b.7 estadística con pandas y SciPy.
- **Práctica (6 h):** regresión lineal **desde cero** con descenso del gradiente; simulación Monte Carlo; Bayes en código; contrastes de hipótesis; **M6b CRUD desde Python** (1 h): cargar y consultar un dataset en base de datos.
- **PBL (3 h) · Reto: "¿La ocupación depende de esto?".** Implementar la regresión desde cero, contrastarla con una librería y responder con estadística a una pregunta del cliente (p. ej. efecto de la temporada o del precio en la ocupación). Cargar los datos en BD y consultarlos desde Python.
- **Entregable:** notebook con gradiente implementado + análisis estadístico + BD poblada.

## Sprint 6 · Datos listos para modelar (11 h · 3–5/11)
**Pregunta guía:** ¿están los datos en condiciones de entrenar algo fiable?

- **Teoría (4 h):** M2 rol del Data Scientist, pandas, visualización exploratoria, limpieza y preprocesado; M3 UD 3.1 (flujo con scikit-learn, *pipelines*) y UD 3.2 (métricas, sesgo-varianza, `GridSearchCV`).
- **Práctica (4 h):** EDA guiado (California Housing o Palmer Penguins); escalado, codificación, separación train/test; validación cruzada y métricas.
- **PBL (3 h) · Reto: "Datos sucios, cliente impaciente".** Recibir un dataset con nulos, duplicados, *outliers* y tipos incorrectos; documentar los defectos y sus causas y construir un **pipeline de preprocesado reproducible** con un modelo *baseline*.
- **Entregable:** notebook de EDA + pipeline + informe de defectos de datos.

## Sprint 7 · ML supervisado: regresión y clasificación (12 h · 5–9/11)
**Pregunta guía:** ¿podemos predecir el precio o la cancelación?

- **Teoría (4 h):** UD 3.3 regresión lineal, polinómica, Ridge y Lasso; UD 3.4 regresión logística; UD 3.5 k-NN y Naive Bayes.
- **Práctica (5 h):** un laboratorio por algoritmo con scikit-learn; interpretación de coeficientes; matriz de confusión y curvas ROC.
- **PBL (3 h) · Reto: "Precio y cancelación".** Construir un modelo de **regresión** (precio por noche u ocupación) y otro de **clasificación** (cancelación), comparar métricas y traducir el resultado a una recomendación de negocio.
- **Entregable:** informe de modelado con recomendación.

## Sprint 8 · Árboles, ensembles y SVM (11 h · 9–11/11)
**Pregunta guía:** ¿cuál es el mejor modelo y cuánto nos cuesta mantenerlo?

- **Teoría (3 h):** UD 3.6 árboles de decisión; UD 3.7 Random Forest, Gradient Boosting y XGBoost; UD 3.8 SVM.
- **Práctica (5 h):** laboratorios con ajuste de hiperparámetros; importancia de variables; comparación en el mismo dataset.
- **PBL (3 h) · Reto: "Duelo de modelos".** Comparar árboles, RF, boosting y SVM con `GridSearchCV`; elegir un **modelo campeón** justificando rendimiento, explicabilidad y coste.
- **Entregable:** *leaderboard* interno + ficha del modelo (*model card*).
- **Evaluación:** test de M3 (primera parte).

## Sprint 9 · Segmentar, recomendar y aprender por refuerzo (11 h · 11–12/11)
**Pregunta guía:** ¿qué tipos de cliente tenemos y qué les ofrecemos?

- **Teoría (3 h):** UD 3.9 clustering (k-means, jerárquico, DBSCAN); UD 3.10 PCA; UD 3.11 sistemas de recomendación; UD 3.12 introducción al aprendizaje por refuerzo.
- **Práctica (5 h):** segmentación de un dataset de clientes; reducción de dimensionalidad; recomendador basado en contenido y colaborativo; Q-learning con Gymnasium.
- **PBL (3 h) · Reto: "Conocer al huésped".** Segmentar a los huéspedes, interpretar los segmentos y prototipar un **recomendador de experiencias**.
- **Entregable:** segmentos interpretados + prototipo de recomendador.
- **Evaluación:** test de M3 (segunda parte).

## Sprint 10 · Redes neuronales bien entrenadas (15 h · 13–17/11)
**Pregunta guía:** ¿una red neuronal mejora al ML clásico y a qué precio?

- **Teoría (5 h):** UD 4.1 neurona, activaciones, *backpropagation* y optimizadores; UD 4.2 MLP con Keras; UD 4.3 regularización, *early stopping*, batch norm, TensorBoard.
- **Práctica (6 h):** red implementada en NumPy; MLP de clasificación y regresión; diagnóstico de overfitting con curvas de aprendizaje.
- **PBL (4 h) · Reto: "¿Vale la pena la red?".** Entrenar un MLP sobre el problema de cancelaciones o precios, compararlo con el modelo campeón del Sprint 8 y diagnosticar sobreajuste con curvas.
- **Entregable:** notebook + informe comparativo ML clásico frente a MLP.

## Sprint 11 · Visión por computador (17 h · 17–20/11)
**Pregunta guía:** ¿podemos aprovechar las imágenes del cliente?

- **Teoría (5 h):** UD 4.4 CNN (convolución, pooling, arquitecturas LeNet, VGG, ResNet, *data augmentation*); UD 4.5 *transfer learning* y *fine-tuning*; UD 4.6 detección y segmentación (YOLO, introducción).
- **Práctica (7 h):** CNN desde cero; *transfer learning* con un modelo preentrenado; detección de objetos con un modelo listo.
- **PBL (5 h) · Reto: "Visión artificial para el cliente".** Clasificar fotos (p. ej. tipo de alojamiento o de zona) con *transfer learning*, medir el rendimiento y hacer **análisis de errores** con ejemplos mal clasificados. Dataset público a validar.
- **Entregable:** modelo + demostrador + análisis de errores.

## Sprint 12 · Lenguaje, secuencias y modelos generativos (18 h · 20–25/11)
**Pregunta guía:** ¿qué dicen los clientes y qué pasará mañana?

- **Teoría (5 h):** UD 4.7 RNN, LSTM, GRU y series temporales; UD 4.8 NLP clásico y *embeddings*; UD 4.9 Transformers y LLM (Hugging Face, *fine-tuning* ligero, introducción a RAG); UD 4.10 autoencoders y modelos generativos.
- **Práctica (8 h):** predicción de una serie temporal; análisis de sentimiento y temas en reseñas; uso de LLM por API; mini RAG.
- **PBL (5 h) · Reto: "Escuchar al cliente".** Análisis de reseñas (sentimiento y temas), predicción de ocupación con una serie temporal y prototipo de **asistente con RAG** sobre la política del alojamiento.
- **Entregable:** informe de reseñas + modelo de serie temporal + demo del asistente.
- **Evaluación:** test de M4.

## Sprint 13 · Contar lo que hace el modelo (3 h · 25/11)
**Pregunta guía:** ¿cómo enseñamos y defendemos los resultados de un modelo?

- **Teoría (1 h):** curvas de entrenamiento, matriz de confusión, ROC/PR, importancia de variables, SHAP y Grad-CAM, detección de sesgos.
- **Práctica (1 h):** generar las visualizaciones del mejor modelo del curso.
- **PBL (1 h) · Reto: "Informe visual para dirección".** Un informe de una página del mejor modelo, con gráficos y conclusiones para decidir.
- **Entregable:** informe visual (semilla de la memoria del proyecto final).

---

# BLOQUE C · PROYECTO DE CIERRE

*En los Sprints 14–16 la teoría se reduce a una píldora de apoyo de 1 h por sprint; el trabajo es de equipo con tutoría del docente. El proyecto final lo eligen los equipos entre 3–4 briefs sectoriales (diseño pendiente).*

## Sprint 14 · Proyecto · Reto, equipo y datos (19 h · 25–30/11)
- **Teoría (1 h):** píldora sobre cómo formular un proyecto de IA (canvas, criterios de éxito).
- **Práctica (3 h):** talleres de Design Thinking aplicados al brief elegido y de definición del backlog.
- **PBL (15 h):** elegir brief, definir el problema, obtener datos, EDA, *baseline*, backlog y **plan ético** con el checklist del Sprint 1.
- **Entregable:** documento de definición + EDA + backlog + modelo *baseline*.

## Sprint 15 · Proyecto · Modelado y experimentos (18 h · 1–3/12)
- **Teoría (1 h):** píldora de seguimiento de experimentos y buenas prácticas (versionado de datos y modelos).
- **Práctica (3 h):** sesiones de tutoría técnica por equipo.
- **PBL (14 h):** iteraciones de modelado, registro de experimentos, comparativa y selección del modelo.
- **Entregable:** modelo candidato + registro de experimentos.

## Sprint 16 · Proyecto · Evaluación, IA responsable y entrega (18 h · 4–10/12)
- **Teoría (1 h):** píldora de despliegue de un demostrador y de documentación técnica.
- **Práctica (3 h):** tutorías de evaluación de sesgos y visualización de resultados.
- **PBL (14 h):** evaluación final, análisis de sesgos y riesgos, demostrador o endpoint, memoria técnica.
- **Entregable:** demostrador + memoria del proyecto.

## Sprint 17 · Proyecto · Storytelling, ensayos y defensa (8 h · 11 y 14/12)
- **Teoría (1 h):** Storytelling: estructura y elementos (11/12).
- **Práctica (2 h):** construcción del relato y práctica del pitch de 3 min (11/12).
- **PBL (5 h):** ensayos de defensa (3 h, 11/12) y **defensa final** de los equipos (2 h, 14/12).
- **Entregable:** presentación + defensa. Con 2 h el tiempo por equipo es de unos 15 min si hay 7 equipos; ajustar según el número de alumnos.

---

## 3. Cobertura de módulos

| Módulo | Horas | Sprints |
|---|---|---|
| M1 Fundamentos de IA | 42 | 1, 2 (M1a: 20 h) · 4, 5 (M1b: 22 h) |
| M2 Exploración de datos | 5 | 6 |
| M3 Machine Learning | 40 | 6, 7, 8, 9 |
| M4 Redes Neuronales | 50 | 10, 11, 12 |
| M5 Visualización de resultados | 3 | 13 |
| M6 Bases de datos en IA | 5 | 3 (M6a: 4 h) · 5 (M6b: 1 h) |
| M7 Auto Machine Learning | 10 | 3 |
| M8 Responsible AI | 5 | 1 |
| M9 Caso práctico | 60 | 14, 15, 16, 17 |
| Softskills | 10 | 0 (Scrum 4 h, DT 3 h) · 17 (Storytelling 3 h) |

## 4. Evaluación por sprint (Apto / No Apto)

- **Entregables PBL de los Sprints 1–13:** evaluados con la misma rúbrica de 4 criterios (corrección técnica, reproducibilidad, análisis y comunicación al cliente, IA responsable). Su media alimenta el bloque de "ejercicios y entregas".
- **Tests:** Sprint 2 (M1a), Sprint 8 y 9 (M3), Sprint 12 (M4) y un test breve de M6–M8 en el Sprint 3.
- **Trabajo en equipo:** coevaluación y retrospectiva de cada sprint.
- **Proyecto final (Sprints 14–17):** rúbrica de entregables, memoria y defensa.
- Pesos y umbrales orientativos, a validar con los requisitos de la entidad y del SEPE.

## 5. Pendiente

1. Redactar los 3–4 **briefs** del proyecto final y la rúbrica de defensa.
2. Preparar y validar los **datasets** del cliente ancla (reservas, cancelaciones, reseñas, imágenes, series).
3. Presentaciones, sprint a sprint, empezando por el Sprint 0 y el Sprint 1.
4. Sincronizar `distribucion_historico.md` con este calendario si se quiere mantener como documento aparte.
