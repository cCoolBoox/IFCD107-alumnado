# Sprint 7 · ML supervisado: regresión y clasificación

**Pregunta guía:** ¿podemos predecir el precio o la cancelación?

**Fechas:** 5–9 de noviembre · **Horas:** 12 h (4 h teoría · 5 h práctica guiada · 3 h PBL)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_07.pdf`](Guia_Sprint_07.pdf)
- 🖥️ **S07.1 · Regresion lineal polinomica y regularizacion:** [`S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf`](presentaciones/S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf)
- 🖥️ **S07.2 · Regresion logistica y clasificacion:** [`S07.2_Regresion_logistica_y_clasificacion.pdf`](presentaciones/S07.2_Regresion_logistica_y_clasificacion.pdf)
- 🖥️ **S07.3 · k NN y Naive Bayes:** [`S07.3_k_NN_y_Naive_Bayes.pdf`](presentaciones/S07.3_k_NN_y_Naive_Bayes.pdf)

**Contenidos:** M3 UD 3.3 (regresión lineal, polinómica, Ridge y Lasso), UD 3.4 (regresión logística y clasificación) y UD 3.5 (k-NN y Naive Bayes).

## Qué aprenderás
1. Ajustar una regresión lineal y polinómica e **interpretar los coeficientes** en euros.
2. Usar **Ridge y Lasso** para controlar el sobreajuste y seleccionar variables.
3. Entrenar una regresión logística, leer *odds ratios*, la **matriz de confusión** y elegir un **umbral**.
4. Evaluar con **ROC, precisión–recall** y tratar clases desbalanceadas.
5. Comparar k-NN y Naive Bayes con la logística y **traducir las métricas a euros** para el cliente.

## Requisitos previos
- Sprint 6: pipelines (`ColumnTransformer` + `Pipeline`), baseline, validación cruzada y fuga de datos.
- Datos: `datos/reservas_turisdata.csv` (6000 reservas; objetivos `precio_noche` y `cancelada`). Los notebooks lo descargan solos si no lo encuentran.

## Prácticas

| Notebook | Tema | Tiempo | Colab |
|---|---|---|---|
| `S07_01_regresion_lineal_polinomica` | Regresión lineal, coeficientes, residuos, interacciones y polinomios | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/S07_01_regresion_lineal_polinomica.ipynb) |
| `S07_02_ridge_lasso` | Regularización: Ridge, Lasso y elección de `alpha` | 50 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/S07_02_ridge_lasso.ipynb) |
| `S07_03_regresion_logistica` | Regresión logística, *odds ratios*, umbral, matriz de confusión y coste | 70 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/S07_03_regresion_logistica.ipynb) |
| `S07_04_roc_pr_desbalance` | ROC, precisión–recall y clases desbalanceadas | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/S07_04_roc_pr_desbalance.ipynb) |
| `S07_05_knn_naive_bayes` | k-NN y Naive Bayes; comparativa de modelos | 55 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/S07_05_knn_naive_bayes.ipynb) |

Los ejercicios se autocorrigen con `assert`. Si terminas antes, dedica tiempo a las preguntas de reflexión del final de cada notebook.

---

## Reto PBL · «Precio y cancelación» (3 h, en equipo)

**Contexto del cliente.** TurisData Canarias quiere dos cosas: (1) una **tarifa de referencia** que le diga cuánto debería costar una noche según el tipo de habitación y la época, y (2) un **aviso de riesgo de cancelación** para decidir cuándo vender por encima de su capacidad (*overbooking*). El gerente no quiere oír hablar de "AUC": quiere saber **cuánto dinero se juega** si el modelo se equivoca en un sentido o en otro.

**Qué se entrega.**
1. `informe_modelado.md` (o PDF), 2–3 páginas. Plantilla: `guias/S07/informe_modelado_plantilla.md`. Debe incluir la comparativa de métricas de los dos modelos y una **recomendación de negocio** (con euros).
2. `reto_S07.ipynb`: un modelo de **regresión** para `precio_noche` y otro de **clasificación** para `cancelada`, cada uno con su *baseline*, validación y métricas.
3. `README.md` para reproducirlo (semilla, versiones).

**La pregunta clave del informe.** *¿Qué cuesta más: una cancelación no prevista (habitación vacía) o una falsa alarma (cliente que llega y no hay sitio)?* Debéis **proponer una hipótesis de coste razonada** para cada error (por ejemplo, «solo se revende la mitad de las noches» o «una noche de compensación»), elegir el **umbral** que minimiza el coste y mostrar **qué pasa si esos costes cambian** (análisis de sensibilidad).

**Restricciones.**
- Solo variables **conocidas en el momento de reservar** (¡sin fuga!). `cancelada` no puede usarse para predecir el precio.
- El umbral se elige con validación cruzada sobre train; el test se usa una sola vez.
- Solo librerías del curso; semilla fija (`SEMILLA = 42`).
- Máximo 3 modelos por problema (baseline incluido).

**Criterios de evaluación** (0–4 cada uno; misma rúbrica de todos los retos):

| Criterio | 1 · Insuficiente | 2 · Suficiente | 3 · Bueno | 4 · Excelente |
|---|---|---|---|---|
| Corrección técnica | Errores que invalidan el resultado | Correcto con fallos menores | Correcto y bien justificado | Correcto, justificado y con alternativas comparadas |
| Reproducibilidad | No se puede volver a ejecutar | Se ejecuta con ayuda | Se ejecuta desde el README | Además incluye datos o script y versiones fijas |
| Análisis y comunicación al cliente | Solo código o cifras sin interpretar | Interpretación básica | Conclusiones claras para el cliente | Recomendación accionable con límites explicados |
| IA responsable | No se considera | Menciones genéricas | Riesgos específicos identificados | Medidas aplicadas y evaluadas |

*Pista de IA responsable:* ¿quién sufre los falsos positivos (un cliente reubicado)? ¿Se penaliza a algún país o canal? ¿Qué pasa si el modelo se usa para pedir depósitos solo a ciertos clientes?

**Pasos sugeridos.**
- **Día 1 (5–6/11):** *planning* (30 min); acordar las hipótesis de coste; regresión: baseline, lineal y una mejora (interacciones o Lasso); métricas en euros.
- **Día 2 (7–8/11):** clasificación: baseline y logística (más un segundo modelo si queréis); curva ROC/PR, elección del umbral con validación cruzada; coste total en test.
- **Día 3 (9/11):** análisis de sensibilidad, informe con la recomendación, README, autoevaluación y coevaluación; **review + retrospectiva** (última hora).

**Qué se enseña en la review** (5 min por equipo): la tabla comparativa de métricas, el umbral elegido y su coste en euros frente a «no hacer nada», y una frase de recomendación para el gerente.

**Preguntas de la retrospectiva:** ¿qué hipótesis de coste discutimos más? ¿Cómo cambia la decisión si cambia el coste? ¿Qué habríamos necesitado saber del hotel para afinar?

## Definition of Done
- [ ] Modelo de regresión con baseline y métricas en euros (MAE, RMSE) y R².
- [ ] Modelo de clasificación con baseline, matriz de confusión, AUC/AP y umbral justificado.
- [ ] Costes de FN y FP explicitados como hipótesis y análisis de sensibilidad.
- [ ] Recomendación de negocio con cifras y límites.
- [ ] Sin fuga de datos; test usado una sola vez.
- [ ] Notebook ejecutable de principio a fin y README con versiones.
- [ ] Subido a Git; autoevaluación y coevaluación rellenadas.

## Recursos
- Documentación de scikit-learn: *Linear Models* (Ridge, Lasso, regresión logística).
- Documentación de scikit-learn: *Model evaluation: quantifying the quality of predictions* (ROC, PR, matriz de confusión).
- Guía de scikit-learn: *Tuning the decision threshold for class prediction*.
- Notebook `S07_03` (umbral y coste): reutiliza `coste_total` como punto de partida.
- Tu tabla de defectos y el pipeline del reto del Sprint 6.
