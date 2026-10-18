# Sprint 7 · ML supervisado: regresión y clasificación

**Pregunta guía:** ¿podemos predecir el precio o la cancelación?
**Fechas:** 5–9 de noviembre · **Horas:** 12 h (4 h teoría · 5 h práctica guiada · 3 h PBL)

> 🎯 **Reto de este sprint: «Precio y cancelación».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_07.md) · [Reto en PDF](guia/Reto_Sprint_07.pdf) ([ecofriendly](guia/Reto_Sprint_07_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_07.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_07.pdf`](guia/Guia_Sprint_07.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_07_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_07.md`](guia/Reto_Sprint_07.md)
- 🖥️ **S07.1 · Regresion lineal polinomica y regularizacion:** [`S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf`](presentaciones/S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf)
- 🖥️ **S07.2 · Regresion logistica y clasificacion:** [`S07.2_Regresion_logistica_y_clasificacion.pdf`](presentaciones/S07.2_Regresion_logistica_y_clasificacion.pdf)
- 🖥️ **S07.3 · k NN y Naive Bayes:** [`S07.3_k_NN_y_Naive_Bayes.pdf`](presentaciones/S07.3_k_NN_y_Naive_Bayes.pdf)

**Contenidos:** M3 UD 3.3 (regresión lineal, polinómica, Ridge y Lasso), UD 3.4 (regresión logística y clasificación) y UD 3.5 (k-NN y Naive Bayes).

**📁 En esta carpeta:** [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`plantillas/`](plantillas/) plantillas para el reto · [`tests/`](tests/) test de conocimientos

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Sesión 1**

1. 🔔 **Ceremonia**: Planning del reto y reparto de roles · _30 min_
2. 📖 **Teoría**: [Regresión lineal, polinómica y regularización (Ridge y Lasso)](presentaciones/S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf) · _2 h_
3. 💻 **Práctica**: [Regresión lineal y polinómica](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_01_regresion_lineal_polinomica.ipynb) · _60 min_
4. 💻 **Práctica**: [Ridge y Lasso](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_02_ridge_lasso.ipynb) · _50 min_

**Sesión 2**

5. 📖 **Teoría**: [Regresión logística y clasificación](presentaciones/S07.2_Regresion_logistica_y_clasificacion.pdf) · _1 h_
6. 💻 **Práctica**: [Regresión logística](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_03_regresion_logistica.ipynb) · _70 min_
7. 💻 **Práctica**: [ROC, PR y datos desbalanceados](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_04_roc_pr_desbalance.ipynb) · _60 min_
8. 🎯 **Reto**: [Acordar las hipótesis de coste y hacer la regresión del precio (pasos 1–2)](guia/Reto_Sprint_07.md) · _1 h_

**Sesión 3 (última)**

9. 📖 **Teoría**: [k-NN y Naive Bayes](presentaciones/S07.3_k_NN_y_Naive_Bayes.pdf) · _1 h_
10. 💻 **Práctica**: [k-NN y Naive Bayes](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_05_knn_naive_bayes.ipynb) · _55 min_
11. 🎯 **Reto**: [Clasificación de la cancelación, análisis de sensibilidad, informe y README (pasos 3–5)](guia/Reto_Sprint_07.md) · _2 h_
12. 🔔 **Ceremonia**: Review y retrospectiva · _última hora_

<!--orden:fin-->

## Qué aprenderás
- Ajustar regresiones lineales y polinómicas e **interpretar los coeficientes** en euros.
- Usar **Ridge y Lasso** contra el sobreajuste y entrenar una regresión logística (umbral, matriz de confusión).
- Evaluar con **ROC y precisión–recall** y comparar con k-NN y Naive Bayes.
- Hace falta lo del Sprint 6: *pipelines*, *baseline* y validación cruzada.

## Prácticas
| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S07_01_regresion_lineal_polinomica` | Regresión lineal, coeficientes, residuos, interacciones y polinomios | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_01_regresion_lineal_polinomica.ipynb) |
| `S07_02_ridge_lasso` | Regularización: Ridge, Lasso y elección de `alpha` | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_02_ridge_lasso.ipynb) |
| `S07_03_regresion_logistica` | Regresión logística, *odds ratios*, umbral, matriz de confusión y coste | 70 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_03_regresion_logistica.ipynb) |
| `S07_04_roc_pr_desbalance` | ROC, precisión–recall y clases desbalanceadas | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_04_roc_pr_desbalance.ipynb) |
| `S07_05_knn_naive_bayes` | k-NN y Naive Bayes; comparativa de modelos | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/notebooks/S07_05_knn_naive_bayes.ipynb) |

Los ejercicios se autocorrigen con `assert`. Los datos (`reservas_turisdata.csv`) se descargan solos.

## Reto · «Precio y cancelación»

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_07.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).

**Contexto:** TurisData Canarias quiere una tarifa de referencia por noche y un aviso de riesgo de cancelación para decidir el *overbooking*. El gerente no quiere oír hablar de «AUC»: quiere saber cuánto dinero se juega si el modelo falla.

**Entregáis** (carpeta `sprint-07/` del repositorio del equipo):
- `informe_modelado.md` (2–3 páginas) con comparativa de métricas y recomendación de negocio en euros. Plantilla: [`informe_modelado_plantilla.md`](plantillas/informe_modelado_plantilla.md).
- `reto_S07.ipynb`: regresión para `precio_noche` y clasificación para `cancelada`, cada una con *baseline*.
- Hipótesis de coste de cada error, umbral elegido y análisis de sensibilidad.
- `README.md` para reproducirlo (semilla, versiones).

**Reglas:**
- 3 h en equipo; máx. 3 modelos por problema (*baseline* incluido); `SEMILLA = 42`.
- Solo variables conocidas al reservar (sin fuga). El umbral se elige con validación cruzada y el test se usa una sola vez.
- Nunca claves ni datos personales.

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente e IA responsable (¿se penaliza a algún país o canal?), más costes razonados y sensibilidad.

## 📝 Test de conocimientos · lun 9/11
**Test de M3 · parte 1** · 10 preguntas · unos 20 min · individual, en el navegador, sin penalización por fallo. Cubre M3, UD 3.1 a 3.4 (preprocesado, métricas, regresión y clasificación).

👉 **[Abrir el test](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/tests/test_M3_parte1.html)** (`https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/tests/test_M3_parte1.html`)

**Solo se abre el día lun 9/11** (hora de Canarias). Al terminar, copia tu resultado y envíaselo al docente. Cuenta para el 30 % de «tests de conocimientos».

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el lun 9/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Regresión (MAE, RMSE, R²) y clasificación (matriz de confusión, AUC/AP) con *baseline*
- [ ] Costes de error explicitados, umbral justificado y recomendación con cifras
- [ ] Sin fuga de datos; test usado una sola vez
- [ ] Entregable subido a la carpeta `sprint-07/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
