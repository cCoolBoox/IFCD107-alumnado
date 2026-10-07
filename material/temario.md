# IFCD107 · Especialista en Inteligencia Artificial
## Temario detallado del curso (230 h)

🔗 Calendario interactivo online: <https://ccoolboox.github.io/IFCD107-alumnado/material/calendario_sprints.html>

**Acción 25-38/012242 · 16/10/2026 – 14/12/2026 · 08:30–14:30**
Este temario sigue el orden de impartición de `distribucion_historico.md`: Bloque A (sin Python) → Bloque B (Python) → Bloque C (proyecto y cierre).

---

## Índice y horas

| Bloque | Código | Módulo / unidad | Horas | Fechas |
|---|---|---|---|---|
| A | M1a | Fundamentos de IA (conceptual) | 20 | 16–21/10 |
| A | M6a | Bases de datos SQL/NoSQL | 4 | 21/10 |
| A | M7 | Auto Machine Learning | 10 | 22–23/10 |
| A | M8 | Responsible AI | 5 | 23–26/10 |
| A | SS1 | Softskills: Scrum | 4 | 26–27/10 |
| A | SS2 | Softskills: Design Thinking | 3 | 27/10 |
| B | M1b | Python + mates/estadística aplicadas | 22 | 27/10–3/11 |
| B | M6b | CRUD desde Python | 1 | 3/11 |
| B | M2 | Exploración del conjunto de datos | 5 | 3–4/11 |
| B | M3 | Algoritmos de Machine Learning | 40 | 4–12/11 |
| B | M4 | Redes Neuronales | 50 | 13–25/11 |
| B | M5 | Visualización de resultados | 3 | 25/11 |
| C | M9 | Caso práctico en IA (proyecto) | 60 | 25/11–14/12 |
| C | SS3 | Softskills: Storytelling | 3 | 11/12 |
| | | **Total** (M9 60 h incluidas; SS3 dentro de las 230 h) | **230** | |

> Nota de cómputo: M9 son 60 h de proyecto + 3 h de Storytelling (SS3) = 63 h del bloque C, ya contadas en el calendario.
> El total de teoría (Bloques A y B, más SS3) es 170 h.

**Convención de cada unidad:** contenidos → práctica (P) → producto evaluable (E).
**Entorno común:** Google Colab / Jupyter, Python 3.11+, VS Code, Git y GitHub. Datasets abiertos (Kaggle, UCI, datos.gob.es, Open Data Canarias).

---

# BLOQUE A · SIN PYTHON (46 h)

## M1a · Fundamentos de Inteligencia Artificial (20 h)
**Objetivo:** adquirir los conceptos, modalidades y bases matemático-estadísticas de la IA.

### UD 1a.1 · Introducción a la IA (4 h)
- Historia y definiciones: IA simbólica, ML, DL, IA generativa. IA débil, general y superinteligencia.
- Modalidades: visión por computador, NLP, voz, sistemas de recomendación, robótica, IA generativa.
- Casos de uso reales por sector (educación, salud, turismo, industria, administración).
- Mitos y límites: qué puede y qué no puede hacer la IA hoy.
- **P:** mapa de casos de uso de IA en la empresa del alumno. **E:** ficha de caso de uso.

### UD 1a.2 · Panorama de algoritmos y ciclo de un proyecto (3 h)
- Familias: reglas, regresión, clasificación, clustering, árboles, ensembles, redes neuronales.
- Ciclo de vida: CRISP-DM (negocio → datos → modelado → evaluación → despliegue).
- Datos, características y etiquetas; qué hace falta para entrenar un modelo.
- **P:** elegir la familia de algoritmos adecuada para 6 problemas dados.

### UD 1a.3 · Tipos de aprendizaje (3 h)
- Supervisado, no supervisado, semisupervisado, autosupervisado y por refuerzo.
- Entrenamiento, validación y test; overfitting y underfitting; sesgo y varianza (intuición).
- Introducción a métricas: exactitud, error, matriz de confusión.
- **P:** dinámica de clasificación "a mano" (tarjetas) para entender el sobreajuste.

### UD 1a.4 · Fundamentos matemáticos (5 h)
- Álgebra lineal: vectores, matrices, producto escalar y matricial, transpuesta, inversa; idea de autovalores.
- Cálculo: función, derivada, derivada parcial, gradiente, regla de la cadena.
- Optimización: función de coste y descenso del gradiente (intuición geométrica).
- **P:** ejercicios en papel y con Desmos/GeoGebra. **E:** hoja de ejercicios.

### UD 1a.5 · Fundamentos estadísticos (4 h)
- Estadística descriptiva: media, mediana, varianza, desviación típica, cuartiles.
- Probabilidad, probabilidad condicionada y teorema de Bayes.
- Distribuciones (normal, binomial, uniforme), muestreo y sesgo de muestreo.
- Correlación frente a causalidad; nociones de inferencia (intervalos, contraste de hipótesis).
- **P:** casos de interpretación de estadísticas engañosas.

### UD 1a.6 · Ecosistema de software para IA (1 h)
- Python, Jupyter, Colab; librerías (NumPy, pandas, scikit-learn), frameworks (TensorFlow/Keras, PyTorch), Hugging Face.
- Hardware: CPU, GPU, TPU; local vs nube; costes.
- **P:** alta en Colab (antes del 22/10).

---

## M6a · Bases de datos en IA: SQL y NoSQL (4 h)
**Objetivo:** aplicar los modelos de bases de datos y su integración con la IA.

### UD 6a.1 · Modelo relacional y SQL (2 h)
- Tablas, claves, relaciones, normalización básica.
- DDL/DML y CRUD: `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`; `WHERE`, `ORDER BY`, `JOIN`, `GROUP BY`.
- **P:** base de datos de práctica (SQLite o PostgreSQL) con consultas guiadas.

### UD 6a.2 · Nociones de DBA y buenas prácticas SQL (1 h)
- Índices, transacciones (ACID), copias de seguridad, usuarios y permisos.
- Buenas prácticas: nombrado, integridad, evitar `SELECT *`, consultas parametrizadas.

### UD 6a.3 · Bases de datos NoSQL (1 h)
- Tipos: documental, clave-valor, columnar, grafos; comparativa con SQL.
- CRUD en MongoDB (Compass/Atlas); cuándo elegir cada tipo.
- **P:** misma información modelada en SQL y en NoSQL. **E:** breve informe comparativo.

---

## M7 · Auto Machine Learning (10 h)
**Objetivo:** generar, entrenar y probar modelos con herramientas AutoML; conocer los principios de MLOps.
**Requisito:** Colab operativo antes del 22/10. AutoML con AutoGluon en Colab; Amazon SageMaker se muestra en demostración docente (sin cuenta AWS del alumnado).

### UD 7.1 · Introducción a AutoML y MLOps (2 h)
- Qué es AutoML; beneficios y límites frente al ML tradicional.
- Plataformas: SageMaker (Canvas/Autopilot), Vertex AI, Azure AutoML, H2O.
- Principios de MLOps: ciclo, versionado, despliegue, monitorización, deriva de datos.

### UD 7.2 · Datos en SageMaker (2 h)
- Cuenta, IAM, costes y buenas prácticas de seguridad; almacenamiento en S3.
- Carga y tratamiento del dataset; visualización y calidad de datos.
- **P:** cargar y explorar un dataset tabular.

### UD 7.3 · Entrenamiento con AutoML (3 h)
- Tipo de problema y métrica objetivo; lanzamiento del experimento.
- Revisión de modelos candidatos, explicabilidad, validación y evaluación.
- **P:** entrenar y comparar modelos. **E:** informe del mejor modelo.

### UD 7.4 · Servicios web ML seguros (3 h)
- Despliegue de un endpoint; invocación por API.
- Seguridad de acceso (IAM, API Gateway/Lambda), monitorización, control de costes.
- **P:** consumir el modelo por API y **eliminar los recursos** al terminar.

---

## M8 · Responsible AI (5 h)
**Objetivo:** aplicar una IA responsable.

### UD 8.1 · Ética, moral y derechos digitales (1 h)
- Ética, responsabilidad, gobernanza de datos, investigación e innovación responsables.

### UD 8.2 · Sesgo, equidad y explicabilidad (1 h)
- Fuentes de sesgo en datos y modelos; equidad; transparencia y explicabilidad.

### UD 8.3 · Marco normativo (1 h)
- RGPD y LOPDGDD; Reglamento Europeo de IA (AI Act): niveles de riesgo y obligaciones.
- *Verificar antes de impartir el calendario de aplicación vigente del AI Act.*

### UD 8.4 · Casos reales (1 h)
- Análisis de casos con dilemas éticos (selección de personal, reconocimiento facial, scoring, IA en educación).
- **P:** debate guiado con roles.

### UD 8.5 · Evaluación ética de un proyecto (1 h)
- Checklist de IA responsable aplicado a un caso propio.
- **E:** checklist completado (se reutilizará en el proyecto final).

---

## SS1 · Softskills: Metodología Scrum (4 h)
- **Agile vs tradicional; Manifiesto Ágil** (1 h).
- **Roles y artefactos:** Product Owner, Scrum Master, equipo; backlog, sprint backlog, incremento (1 h).
- **Ceremonias:** planning, daily, review, retrospectiva (1 h).
- **P:** simulación de un sprint corto (1 h).

## SS2 · Softskills: Design Thinking (3 h)
- Fases: empatizar, definir, idear, prototipar, testear.
- Técnicas: mapa de empatía, entrevistas, "How might we", brainstorming, prototipado rápido.
- **P:** mini-reto de diseño de una solución de IA. Se retoma en el arranque del proyecto.

---

# BLOQUE B · PYTHON (121 h)

## M1b · Python + matemáticas y estadística aplicadas (22 h)
**Objetivo:** dominar Python como herramienta para implementar conceptos de IA. El alumnado viene de Java: se apoyará en comparaciones Java ↔ Python.

### UD 1b.1 · Puesta en marcha del entorno (2 h)
- Instalación de Python, entornos virtuales, `pip`, Jupyter, VS Code; Git básico.

### UD 1b.2 · Fundamentos del lenguaje (3 h)
- Sintaxis, tipos, operadores, `input/print`, condicionales, bucles.

### UD 1b.3 · Estructuras de datos y funciones (3 h)
- Listas, tuplas, diccionarios, conjuntos, comprensiones.
- Funciones, parámetros, `lambda`, `*args/**kwargs`.

### UD 1b.4 · Módulos, ficheros, excepciones y POO (2 h)
- Importación de módulos, lectura y escritura de ficheros (CSV, JSON).
- Excepciones; clases y objetos (comparativa con Java).

### UD 1b.5 · NumPy (3 h)
- Arrays, indexación, vectorización, *broadcasting*; álgebra lineal (`dot`, `matmul`, inversa, autovalores).

### UD 1b.6 · Implementación de conceptos matemáticos (4 h)
- Derivadas numéricas, función de coste, descenso del gradiente y regresión lineal **desde cero**.
- **E:** notebook con el descenso del gradiente implementado.

### UD 1b.7 · Estadística con Python (5 h)
- Estadística descriptiva con pandas; distribuciones con SciPy; simulación Monte Carlo.
- Bayes en código, correlación, contraste de hipótesis (t-test), intervalos de confianza.
- **E:** notebook de análisis estadístico de un dataset.

---

## M6b · CRUD desde Python (1 h)
- `sqlite3`/SQLAlchemy y `pandas.to_sql` para cargar un dataset y consultarlo; `pymongo` (demostración).
- **P:** cargar en base de datos el dataset que se usará en M2.

---

## M2 · Exploración del conjunto de datos (5 h)
**Objetivo:** tratar y preparar conjuntos de datos para entrenar modelos.

### UD 2.1 · Rol del Data Scientist y tipos de dato (1 h)
- Funciones del Data Scientist; datos estructurados, no estructurados y series temporales.

### UD 2.2 · pandas: carga e inspección (1 h)
- `read_csv`, `info`, `describe`, filtrado, agrupación, uniones.

### UD 2.3 · Visualización exploratoria (1 h)
- matplotlib, seaborn, plotly; elección del gráfico según el tipo de dato.

### UD 2.4 · Limpieza de datos (1 h)
- Nulos, duplicados, *outliers*, tipos incorrectos; detección de defectos y de sus causas.

### UD 2.5 · Preprocesado (1 h)
- Escalado, codificación de categóricas, reducción de dimensionalidad, separación train/test.
- **E:** EDA completo con conclusiones (dataset sugerido: California Housing o Palmer Penguins).

---

## M3 · Algoritmos de Machine Learning (40 h)
**Objetivo:** aplicar algoritmos de ML a problemas de distinta índole.
Cada unidad cierra con un caso práctico en Python con scikit-learn.

| UD | Contenido | Horas |
|---|---|---|
| 3.1 | Flujo de trabajo con scikit-learn: estimadores, *pipelines*, validación cruzada | 3 |
| 3.2 | Métricas y evaluación: MAE/RMSE/R², precisión/recall/F1, ROC-AUC, sesgo-varianza, `GridSearchCV` | 3 |
| 3.3 | Regresión lineal y polinómica; regularización Ridge/Lasso | 5 |
| 3.4 | Regresión logística y clasificación | 4 |
| 3.5 | k-NN y Naive Bayes | 3 |
| 3.6 | Árboles de decisión | 3 |
| 3.7 | Ensembles: Random Forest, Gradient Boosting, XGBoost | 5 |
| 3.8 | Máquinas de vectores de soporte (SVM) | 3 |
| 3.9 | Clustering: k-means, jerárquico, DBSCAN | 4 |
| 3.10 | Reducción de dimensionalidad: PCA (mención de t-SNE) | 2 |
| 3.11 | Sistemas de recomendación (contenido, colaborativo, factorización) | 3 |
| 3.12 | Introducción al aprendizaje por refuerzo (Q-learning con Gymnasium) | 2 |
| | **Total** | **40** |

- Selección del algoritmo según tipología y aplicabilidad (criterio transversal).
- **E:** 3 entregas: regresión (UD 3.3), clasificación con comparativa de modelos (UD 3.7) y clustering/recomendación (UD 3.9–3.11).

---

## M4 · Redes Neuronales (50 h)
**Objetivo:** aplicar redes neuronales a visión por computador, NLP y otros campos.
**Framework principal:** Keras/TensorFlow; comparativa breve con PyTorch.

| UD | Contenido | Horas |
|---|---|---|
| 4.1 | Fundamentos: neurona, perceptrón, activaciones, pérdida, *backpropagation* y optimizadores (implementación en NumPy) | 4 |
| 4.2 | Redes densas (MLP) con Keras: clasificación y regresión | 6 |
| 4.3 | Entrenamiento y regularización: dropout, L2, *early stopping*, batch norm, callbacks, TensorBoard | 5 |
| 4.4 | CNN y visión por computador: convolución, pooling, arquitecturas (LeNet, VGG, ResNet), *data augmentation* | 9 |
| 4.5 | *Transfer learning* y *fine-tuning* | 5 |
| 4.6 | Detección de objetos y segmentación (introducción, YOLO) | 3 |
| 4.7 | RNN, LSTM, GRU y series temporales | 6 |
| 4.8 | NLP clásico y *embeddings*: tokenización, TF-IDF, word2vec; procesamiento léxico, sintáctico y semántico | 4 |
| 4.9 | Transformers y LLM: atención, BERT/GPT, Hugging Face, *fine-tuning* ligero, introducción a RAG y APIs | 6 |
| 4.10 | Autoencoders y modelos generativos (GAN, difusión: introducción) | 2 |
| | **Total** | **50** |

- **E:** entrega de clasificación de imágenes con *transfer learning* (UD 4.5) y entrega de NLP (UD 4.8–4.9).

---

## M5 · Visualización de resultados (3 h)
**Objetivo:** interpretar los resultados de los modelos mediante visualización.

- **UD 5.1 · Seguimiento del entrenamiento (1 h):** curvas de pérdida y precisión, TensorBoard; *vanishing/exploding gradient*, detección de overfitting.
- **UD 5.2 · Evaluación visual (1 h):** matriz de confusión, ROC/PR, importancia de variables, SHAP y Grad-CAM; detección de sesgos.
- **UD 5.3 · Comunicación de resultados (1 h):** informes y cuadros de mando para la toma de decisiones basada en datos.
- **E:** informe visual del mejor modelo de M3 o M4 (semilla del informe final).

---

# BLOQUE C · CIERRE (63 h)

## M9 · Caso práctico en IA · Proyecto final (60 h)
**Objetivo:** proyecto completo por equipos que integre lo aprendido, con defensa final.
**Metodología:** PBL con Scrum (sprints), retrospectiva y reparto de roles.

Estructura provisional (el diseño detallado del proyecto está pendiente):

| Fase | Contenido | Horas aprox. |
|---|---|---|
| 0 | Arranque: equipos, roles, elección del reto (Design Thinking), backlog | 3 |
| 1 | Sprint 1: definición del problema, datos y EDA | 12 |
| 2 | Sprint 2: modelado y experimentos | 15 |
| 3 | Sprint 3: evaluación, visualización y componente de IA responsable | 12 |
| 4 | Sprint 4: despliegue/demostrador, documentación y memoria | 12 |
| 5 | Ensayos de defensa | 4 |
| 6 | **Defensa (14/12)** | 2 |
| | **Total** | **60** |

## SS3 · Softskills: Storytelling (3 h)
- Estructura, elementos, ejemplos y práctica; pitch de 3 minutos para la defensa.
- Impartido el **11/12**, junto a los ensayos de defensa.

---

# EVALUACIÓN (Apto / No Apto)

| Instrumento | Cuándo | Peso orientativo |
|---|---|---|
| Evaluación inicial diagnóstica (Python y mates) | Sesión 1 | Sin nota |
| Tests de conocimientos | Fin de M1a, M3 (en dos partes), M4 y bloque M6–M8 | 30 % |
| Ejercicios y entregas prácticas por módulo | Continua | 30 % |
| Participación y trabajo en equipo (retrospectivas, coevaluación) | Continua y en el proyecto | 10 % |
| Proyecto final: entrega + **defensa** (rúbrica) | 11–14/12 | 30 % |

**Los 5 tests (cada uno se abre solo su día; el enlace está también en el README del sprint):**

| Test | Día | Sprint | Enlace |
|---|---|---|---|
| M1a · Fundamentos de IA | vie 23/10 | S02 | [abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S02/test_M1a.html) |
| Bloque M6–M8 · SQL, AutoML e IA responsable | mar 27/10 | S03 | [abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/test_M6-M8.html) |
| M3 · parte 1 (UD 3.1–3.4) | lun 9/11 | S07 | [abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/test_M3_parte1.html) |
| M3 · parte 2 (UD 3.5–3.8) | mié 11/11 | S08 | [abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/test_M3_parte2.html) |
| M4 · Redes neuronales | mié 25/11 | S12 | [abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S12/test_M4.html) |


Criterio de "Apto": superar cada instrumento con un mínimo del 50 % y asistir al mínimo exigido por la normativa de la acción.
Pesos y umbrales **orientativos**; confirmar con los requisitos de la entidad y del SEPE.
