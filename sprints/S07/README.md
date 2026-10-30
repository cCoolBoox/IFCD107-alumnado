# README Sprint S07 · ML supervisado: regresión y clasificación

**Pregunta guía:** ¿podemos predecir el precio o la cancelación?
**Fechas:** 10–11 de noviembre · **Horas:** 9 h (2 h teoría · 4 h práctica · 3 h PBL)

📄 **Este README en PDF:** [a color](README_Sprint_07.pdf) · [ecofriendly, para imprimir](README_Sprint_07_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. Ajustar una regresión lineal y polinómica e **interpretar los coeficientes** en euros.
2. Usar **Ridge y Lasso** para controlar el sobreajuste y seleccionar variables.
3. Entrenar una regresión logística, leer *odds ratios*, la **matriz de confusión** y elegir un **umbral**.
4. Evaluar con **ROC, precisión–recall** y tratar clases desbalanceadas.
5. Comparar k-NN y Naive Bayes con la logística y **traducir las métricas a euros** para el cliente.

## Requisitos previos
- Sprint 6: pipelines (`ColumnTransformer` + `Pipeline`), baseline, validación cruzada y fuga de datos.
- Datos: `datos/reservas_turisdata.csv` (6000 reservas; objetivos `precio_noche` y `cancelada`). Los notebooks lo descargan solos si no lo encuentran.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_07.pdf) · [ecofriendly](guia/Guia_Sprint_07_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [**Código explicado de los cuadernos**](codigo_explicado/) | Cada cuaderno explicado por escrito: recorrido de 10 minutos con el docente, glosario de sus palabras de código y qué hace cada celda y cada línea (para leerlo con calma, mientras o después de ejecutar) | A tu ritmo | Con cada cuaderno |
| [**Carpeta del reto: `Reto_S07/`**](Reto_S07/) | Todo el material del reto junto: ficha (.md y PDF), plantillas y material de apoyo, hoja de autoevaluación y coevaluación y láminas del reto | — | Antes del planning y durante el reto |
| [**Reto en una página** (.md)](Reto_S07/Reto_Sprint_07_una_pagina.md) · [PDF](Reto_S07/Reto_Sprint_07_una_pagina.pdf) · [ecofriendly](Reto_S07/Reto_Sprint_07_una_pagina_ecofriendly.pdf) | Lo esencial para trabajar con la ficha abierta: tres niveles (mínimo, estándar, extra), reparto del tiempo y frases para el informe | 1 página | Durante el reto |
| [Reto completo, paso a paso (.md)](Reto_S07/Reto_Sprint_07.md) · [PDF](Reto_S07/Reto_Sprint_07.pdf) · [ecofriendly](Reto_S07/Reto_Sprint_07_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S07_00_resumen_del_sprint.png) | Lámina con la pregunta guía, qué aprenderás, cómo se reparte el sprint (teoría, práctica y reto) y dónde estás en el curso | — | Antes del planning |
| [El reto paso a paso](Reto_S07/S07_03_reto_paso_a_paso.png) · [PDF con enlaces](Reto_S07/S07_03_reto_paso_a_paso.pdf) | Los pasos del reto con su día y minutos, el material de cada paso, los errores frecuentes y el uso de la IA | — | Durante el reto |
| [Esquema del contenido y su relación con el reto](infografias/S07_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del sprint](infografias/) | 4 láminas ilustradas | — | Antes del planning y durante el reto |
| [Atlas de algoritmos](infografias/S07_03_atlas_regresion_y_clasificacion.png) | Atlas de algoritmos del sprint: regresión lineal, Ridge/Lasso, logística, k-NN y Naive Bayes | — | Teoría y práctica; consulta cuando elijas modelo |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf`](presentaciones/S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf) | Regresión lineal, polinómica y regularización (Ridge y Lasso) | 25 min | Teoría · día 1 del S07 |
| [`S07.2_Regresion_logistica_y_clasificacion.pdf`](presentaciones/S07.2_Regresion_logistica_y_clasificacion.pdf) | Regresión logística y clasificación | 15 min | Teoría · día 1 del S07 |
| [Explicación sencilla: matriz de confusión (VN, FP, FN, VP)](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/actividades/S07_matriz_de_confusion_en_sencillo.html) · [`.html`](actividades/S07_matriz_de_confusion_en_sencillo.html) | Las cuatro casillas, cómo leer las siglas, por qué los errores no cuestan igual y mini-test | 10 min | Antes del ejercicio interactivo |
| [Lámina: la matriz de confusión](infografias/S07_04_matriz_de_confusion.png) | Una página con las cuatro casillas, las métricas y el efecto del umbral (para tener a mano) | — | Consulta (junto al ejercicio) |
| [Ejercicio interactivo: matriz de confusión](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/actividades/S07_ejercicio_matriz_de_confusion.html) · [`.html`](actividades/S07_ejercicio_matriz_de_confusion.html) | Construye la matriz a mano, calcula métricas, mueve el umbral y elige con el coste (datos ficticios) | 25–30 min | Antes del cuaderno S07_03 (refuerzo) |
| [`S07.3_k_NN_y_Naive_Bayes.pdf`](presentaciones/S07.3_k_NN_y_Naive_Bayes.pdf) | k-NN y Naive Bayes | 10 min | Teoría · día 2 del S07 |
| [Test de conocimientos](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/tests/test_M3_parte1.html) | Test de M3 · parte 1 · 10 preguntas · individual, en el navegador, sin penalización por fallo.1 a 3.4 (preprocesado, métricas, regresión y clasificación). | 20 min | Solo se abre el lun 9/11 (hora de Canarias) |

**Material de las actividades**

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| [`apuntes_regresion_y_clasificacion.md`](actividades/apuntes_regresion_y_clasificacion.md) · [PDF](actividades/apuntes_regresion_y_clasificacion.pdf) · [ecofriendly](actividades/apuntes_regresion_y_clasificacion_ecofriendly.pdf) | **Apuntes que complementan las diapositivas**: regresión lineal y polinómica, Ridge y Lasso, regresión logística, umbral por coste, ROC y PR, k-NN y Naive Bayes explicados con ejemplos que puedes comprobar a mano | — | Antes del sprint y cuando tengas dudas |
| `S07_01_regresion_lineal_polinomica` | Regresión lineal, coeficientes, residuos, interacciones y polinomios | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_01_regresion_lineal_polinomica.ipynb) |
| `S07_02_ridge_lasso` | Regularización: Ridge, Lasso y elección de `alpha` | 35 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_02_ridge_lasso.ipynb) |
| `S07_03_regresion_logistica` | Regresión logística, *odds ratios*, umbral, matriz de confusión y coste | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_03_regresion_logistica.ipynb) |
| `S07_04_roc_pr_desbalance` | ROC, precisión–recall y clases desbalanceadas | 40 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_04_roc_pr_desbalance.ipynb) |
| `S07_05_knn_naive_bayes` | k-NN y Naive Bayes; comparativa de modelos | 25 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_05_knn_naive_bayes.ipynb) |

Los ejercicios se autocorrigen con `assert`. Los datos (`reservas_turisdata.csv`) se descargan solos.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Día 1 del S07**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Precio y cancelación» y reparto de roles | 10 min |
| 2 | 📖 Teoría | [Regresión lineal, polinómica y regularización (Ridge y Lasso)](presentaciones/S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf) | 25 min |
| 3 | 💻 Práctica | [Regresión lineal y polinómica (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_01_regresion_lineal_polinomica.ipynb) | 40 min |
| 4 | 💻 Práctica | [Ridge y Lasso (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_02_ridge_lasso.ipynb) | 35 min |
| 5 | 📖 Teoría | [Regresión logística y clasificación](presentaciones/S07.2_Regresion_logistica_y_clasificacion.pdf) | 20 min |
| 6 | 💻 Práctica | [Regresión logística (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_03_regresion_logistica.ipynb) | 45 min |
| 7 | 🎯 Reto | [Acordar las hipótesis de coste y hacer la regresión del precio (pasos 1–2)](Reto_S07/Reto_Sprint_07.md) | 25 min |

**Día 2 del S07**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 8 | 💻 Práctica | [ROC, PR y datos desbalanceados (los ejercicios marcados «en clase»)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_04_roc_pr_desbalance.ipynb) | 25 min |
| 9 | 📖 Teoría | [k-NN y Naive Bayes](presentaciones/S07.3_k_NN_y_Naive_Bayes.pdf) | 10 min |
| 10 | 🎯 Reto | [Clasificación de la cancelación, análisis de sensibilidad, informe y README (pasos 3–5)](Reto_S07/Reto_Sprint_07.md) | 30 min |
| 11 | 📝 Test | [**Test de M3 (parte 1)**, solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/tests/test_M3_parte1.html) | 25 min |
| 12 | 🔔 Ceremonia | Entrega en `sprint-07/` y autoevaluación y coevaluación del Sprint 7 (la review y la retro se hacen junto con las del Sprint 8) | 15 min |

<!--orden:fin-->

## Reto · «Precio y cancelación»

📄 [Reto en PDF](Reto_S07/Reto_Sprint_07.pdf) · [ecofriendly](Reto_S07/Reto_Sprint_07_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](Reto_S07/Reto_Sprint_07.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** TurisData Canarias quiere una tarifa de referencia por noche y un aviso de riesgo de cancelación para decidir el *overbooking*. El gerente no quiere oír hablar de «AUC»: quiere saber cuánto dinero se juega si el modelo falla.


**Entregáis** (carpeta `sprint-07/` del repositorio del equipo):
- `informe_modelado.md` (2–3 páginas) con comparativa de métricas y recomendación de negocio en euros. Plantilla: [`informe_modelado_plantilla.md`](Reto_S07/informe_modelado_plantilla.md).
- `reto_S07.ipynb`: regresión para `precio_noche` y clasificación para `cancelada`, cada una con *baseline*.
- Hipótesis de coste de cada error, umbral elegido y análisis de sensibilidad.
- `README.md` para reproducirlo (semilla, versiones).


**Reglas:**
- Unas 1 h 40 min en equipo (planning, reto y entrega); máx. 3 modelos por problema (*baseline* incluido); `SEMILLA = 42`.
- Solo variables conocidas al reservar (sin fuga). El umbral se elige con validación cruzada y el test se usa una sola vez.
- Nunca claves ni datos personales.


**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (¿se penaliza a algún país o canal?), más costes razonados y sensibilidad.

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mié 11/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Regresión (MAE, RMSE, R²) y clasificación (matriz de confusión, AUC/AP) con *baseline*
- [ ] Costes de error explicitados, umbral justificado y recomendación con cifras
- [ ] Sin fuga de datos; test usado una sola vez
- [ ] Entregable subido a la carpeta `sprint-07/` del repositorio del equipo
- [ ] [Autoevaluación y coevaluación](Reto_S07/autoevaluacion_y_coevaluacion.md) rellenadas
