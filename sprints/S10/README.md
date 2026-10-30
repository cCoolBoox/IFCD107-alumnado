# README Sprint S10 · Redes neuronales bien entrenadas

**Pregunta guía:** ¿una red neuronal mejora al aprendizaje automático clásico y a qué precio?
**Fechas:** 17–18 de noviembre · **Horas:** 12 h (3 h teoría · 5 h práctica · 4 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_10.pdf) · [ecofriendly, para imprimir](README_Sprint_10_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás

1. Cómo funciona por dentro una red neuronal: neurona, capas, activación, propagación hacia delante y hacia atrás.
2. Construir y entrenar un MLP con Keras para clasificar cancelaciones y predecir el precio por noche.
3. Reconocer el **sobreajuste** en las curvas de aprendizaje y combatirlo (L2, *dropout*, parada temprana, *batch norm*).
4. Ajustar tasa de aprendizaje y tamaño de lote, usar *callbacks* y guardar/cargar modelos.
5. Decidir con datos si una red "vale la pena" frente a un modelo de boosting.

## Requisitos previos

- Sprints 7 y 8: partición entrenamiento/validación/prueba, métricas (AUC, F1, MAE) y modelos de árboles/boosting.
- Python y pandas del Bloque B. No hace falta saber matemáticas avanzadas: se explican con ejemplos.
- Datos: `reservas_turisdata.csv` (se descarga solo desde el notebook). Todo funciona **sin internet** y en Colab.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_10.pdf) · [ecofriendly](guia/Guia_Sprint_10_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [**Carpeta del reto: `Reto_S10/`**](Reto_S10/) | Todo el material del reto junto: ficha (.md y PDF), hoja de autoevaluación y coevaluación y láminas del reto | — | Antes del planning y durante el reto |
| [Reto completo, paso a paso (.md)](Reto_S10/Reto_Sprint_10.md) · [PDF](Reto_S10/Reto_Sprint_10.pdf) · [ecofriendly](Reto_S10/Reto_Sprint_10_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S10_00_resumen_del_sprint.png) | Lámina con la pregunta guía, qué aprenderás, cómo se reparte el sprint (teoría, práctica y reto) y dónde estás en el curso | — | Antes del planning |
| [El reto paso a paso](Reto_S10/S10_03_reto_paso_a_paso.png) · [PDF con enlaces](Reto_S10/S10_03_reto_paso_a_paso.pdf) | Los pasos del reto con su día y minutos, el material de cada paso, los errores frecuentes y el uso de la IA | — | Durante el reto |
| [Esquema del contenido y su relación con el reto](infografias/S10_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del sprint](infografias/) | 3 láminas ilustradas | — | Antes del planning y durante el reto |
| [Atlas de algoritmos](infografias/S10_03_atlas_redes_neuronales_y_vision.png) | Atlas de algoritmos (S10–S11): MLP, regularización, CNN, transfer learning y detección | — | Teoría y práctica; consulta cuando elijas modelo |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S10.1_Fundamentos_de_redes_neuronales.pdf`](presentaciones/S10.1_Fundamentos_de_redes_neuronales.pdf) | Fundamentos de redes neuronales | 20 min | Teoría · día 1 del S10 |
| [`S10.2_Redes_densas_con_Keras.pdf`](presentaciones/S10.2_Redes_densas_con_Keras.pdf) | Redes densas con Keras | 20 min | Teoría · día 1 del S10 |
| [`S10.3_Entrenamiento_y_regularizacion.pdf`](presentaciones/S10.3_Entrenamiento_y_regularizacion.pdf) | Entrenamiento y regularización (primera parte) | 35 min | Teoría · día 1 del S10 y día 2 del S10 |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| [`apuntes_redes_neuronales.md`](actividades/apuntes_redes_neuronales.md) · [PDF](actividades/apuntes_redes_neuronales.pdf) · [ecofriendly](actividades/apuntes_redes_neuronales_ecofriendly.pdf) | **Apuntes que complementan las diapositivas**: la neurona, las capas, el entrenamiento, Keras, el sobreajuste y la regularización (L2, dropout, parada temprana) explicados con cuentas que puedes hacer a mano | — | Antes del sprint y cuando tengas dudas |
| `S10_01_red_desde_cero` | Una red neuronal con solo NumPy: neurona, activación, *backprop*, entrenamiento | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_01_red_desde_cero.ipynb) |
| `S10_02_mlp_keras` | MLP en Keras: cancelaciones (clasificación) y `precio_noche` (regresión) | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_02_mlp_keras.ipynb) |
| `S10_03_regularizacion` | Curvas, sobreajuste, L2, *dropout*, parada temprana, lote, tasa, *callbacks*, guardar modelo | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_03_regularizacion.ipynb) |
| `S10_04_reto_vale_la_pena` | Esqueleto del reto: MLP frente a boosting con incertidumbre y diagnóstico | 1 h 30 (+ trabajo PBL) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb) |

Cada notebook tiene ejercicios con `assert`: si saltan, el mensaje te dice qué revisar.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Día 1 del S10**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «¿Vale la pena la red?» y reparto de roles | 10 min |
| 2 | 📖 Teoría | [Fundamentos de redes neuronales](presentaciones/S10.1_Fundamentos_de_redes_neuronales.pdf) | 25 min |
| 3 | 💻 Práctica | [Una red neuronal con solo NumPy (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_01_red_desde_cero.ipynb) | 40 min |
| 4 | 📖 Teoría | [Redes densas con Keras](presentaciones/S10.2_Redes_densas_con_Keras.pdf) | 25 min |
| 5 | 💻 Práctica | [MLP en Keras: clasificación y regresión (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_02_mlp_keras.ipynb) | 1 h |
| 6 | 📖 Teoría | [Entrenamiento y regularización (diapositivas 1–5; las 6–7 son del reto)](presentaciones/S10.3_Entrenamiento_y_regularizacion.pdf) | 30 min |
| 7 | 💻 Práctica | Terminad los cuadernos pendientes y poneos al día | 10 min |

**Día 2 del S10**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 8 | 💻 Práctica | [Sobreajuste, L2, *dropout*, parada temprana y *callbacks* (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_03_regularizacion.ipynb) | 55 min |
| 9 | 🎯 Reto | Esqueleto [`S10_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S10/notebooks/S10_04_reto_vale_la_pena.ipynb): elegir el problema y reproducir la referencia (paso 1) → primera red (2) → diagnosticar el sobreajuste (3) → comparación justa (4) → informe y presentación (5) | 1 h 30 min |
| 10 | 💻 Práctica | Terminad los cuadernos pendientes y poneos al día | 15 min |
| 11 | 🔔 Ceremonia | Entrega en `sprint-10/`, autoevaluación y coevaluación, review y retrospectiva | 40 min |

<!--orden:fin-->

## Reto · «¿Vale la pena la red?»

📄 [Reto en PDF](Reto_S10/Reto_Sprint_10.pdf) · [ecofriendly](Reto_S10/Reto_Sprint_10_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](Reto_S10/Reto_Sprint_10.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** la dirección de TurisData Canarias oye hablar de redes neuronales y pregunta si debe sustituir su modelo de cancelaciones. No quiere una opinión: quiere evidencias, coste incluido.


**Entregáis** (carpeta `sprint-10/` del repositorio del equipo):
- Notebook ejecutable de principio a fin, basado en `S10_04`, con semillas fijas.
- Informe comparativo de 1–2 páginas (PDF o Markdown) «ML clásico frente a MLP»: tabla de resultados, curvas de aprendizaje y recomendación.


**Reglas:**
- Unas 2 h 20 min en equipo (planning, reto y entrega); un solo problema (`cancelada` **o** `precio_noche`), misma partición para todos y prueba usada una sola vez.
- Referencia: tu campeón del Sprint 8; máx. 40 épocas; el escalador se ajusta solo con entrenamiento.
- Nunca claves ni datos personales.


**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (datos sintéticos, coste de errores, sesgos por país o canal), más comparación con incertidumbre (varias semillas).

## ✅ Antes de cerrar el sprint
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Notebook de arriba abajo con semillas fijas; test usado una sola vez
- [ ] MLP y modelo de árboles/boosting comparados con incertidumbre
- [ ] Curvas de aprendizaje y recomendación concreta con coste y límites
- [ ] Entregable subido a la carpeta `sprint-10/` del repositorio del equipo
- [ ] [Autoevaluación y coevaluación](Reto_S10/autoevaluacion_y_coevaluacion.md) rellenadas
