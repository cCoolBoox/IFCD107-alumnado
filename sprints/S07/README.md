# README Sprint S07 · ML supervisado: regresión y clasificación

**Pregunta guía:** ¿podemos predecir el precio o la cancelación?  
**Fechas:** 10–11 de noviembre · **Horas:** 9 h (2 h teoría · 4 h práctica · 3 h PBL)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Los cuadernos **«en clase»** (carpeta `2_Practica/en_clase/`) son la parte que se hace en el aula; los completos (carpeta `2_Practica/para_casa/`) son para casa.

## Qué aprenderás

1. Ajustar una regresión lineal y polinómica e **interpretar los coeficientes** en euros.
2. Usar **Ridge y Lasso** para controlar el sobreajuste y seleccionar variables.
3. Entrenar una regresión logística, leer *odds ratios*, la **matriz de confusión** y elegir un **umbral**.
4. Evaluar con **ROC, precisión–recall** y tratar clases desbalanceadas.
5. Comparar k-NN y Naive Bayes con la logística y **traducir las métricas a euros** para el cliente.

## Día 1 · Martes 10/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «Precio y cancelación» y reparto de roles | — | 10 |
| ☐ | 📖 Teoría · Regresión lineal y polinómica: coeficientes, residuos e interacciones | [Presentación S07_01](1_Teoria/S07_01_presentacion_Regresion_lineal_y_polinomica.pdf) | 15 |
| ☐ | 💻 Práctica · Regresión lineal y polinómica (cuaderno «en clase») | [Cuaderno S07_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_01_regresion_lineal_polinomica_en_clase.ipynb) | 40 |
| ☐ | 📖 Teoría · Regularización: Ridge y Lasso | [Presentación S07_02](1_Teoria/S07_02_presentacion_Regularizacion_Ridge_y_Lasso.pdf) | 10 |
| ☐ | 💻 Práctica · Ridge y Lasso (cuaderno «en clase») | [Cuaderno S07_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_02_ridge_lasso_en_clase.ipynb) | 35 |
| ☐ | 📖 Teoría · Regresión logística: probabilidades, odds y umbral | [Presentación S07_03](1_Teoria/S07_03_presentacion_Regresion_logistica.pdf) | 20 |
| ☐ | 💻 Práctica · Regresión logística (cuaderno «en clase») | [Cuaderno S07_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_03_regresion_logistica_en_clase.ipynb) | 45 |
| ☐ | 🎯 Reto · Acordar las hipótesis de coste y hacer la regresión del precio (pasos 1–2) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_07_una_pagina.md) | 25 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé entrenar una regresión y una regresión logística con scikit-learn.
- [ ] Sé leer un coeficiente.

## Día 2 · Miércoles 11/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 💻 Práctica · ROC, PR y datos desbalanceados (cuaderno «en clase») | [Cuaderno S07_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/en_clase/S07_04_roc_pr_desbalance_en_clase.ipynb) · [Presentación S07_04](1_Teoria/S07_04_presentacion_Curvas_ROC_y_PR_y_clases_desbalanceadas.pdf) | 15 |
| ☐ | 📖 Teoría · k-NN y Naive Bayes: dos algoritmos más | [Presentación S07_05](1_Teoria/S07_05_presentacion_k-NN_y_Naive_Bayes.pdf) | 10 |
| ☐ | 🎯 Reto · Clasificación de la cancelación, análisis de sensibilidad, informe y README (pasos 3–5) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_07_una_pagina.md) | 40 |
| ☐ | 📝 Test · **Test de M3 (parte 1)** | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/tests/test_M3_parte1.html) | 25 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-07/` y autoevaluación del Sprint 7 (la coevaluación, la review y la retro se hacen el jueves, junto con las del Sprint 8) | — | 15 |
| ☐ | 🏠 **En casa** · k vecinos (k-NN) y Naive Bayes (cuaderno completo) | [Cuaderno S07_05](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_05_knn_naive_bayes.ipynb) · [Presentación S07_05](1_Teoria/S07_05_presentacion_k-NN_y_Naive_Bayes.pdf) | 40 (casa) |

**En clase: 1 h 45 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé interpretar en euros los coeficientes de una regresión.
- [ ] Sé leer una matriz de confusión y elegir un umbral según lo que cuesta equivocarse.
- [ ] Sé traducir las métricas de mis modelos a euros para el cliente.

## El reto en pocas palabras

**Qué os pide el cliente.** El gerente de TurisData quiere **dos herramientas**:

1. Una **tarifa de referencia**: cuánto debería costar una noche según el tipo de habitación y la época (predecir un **número**: `precio_noche`).
2. Un **aviso de riesgo de cancelación**, para decidir cuándo vender por encima de su capacidad (*overbooking*: aceptar más reservas que habitaciones, apostando a que algunas se cancelarán) (predecir una **categoría**: `cancelada`, sí o no).

**Qué vais a entregar:** `informe_modelado.md` (o PDF), el cuaderno `reto_S07.ipynb` y un `README.md`.

**Núcleo y extra.** Núcleo: regresión del precio y clasificación de la cancelación con las hipótesis de coste. Extra: análisis de sensibilidad completo.

Antes de empezar, probad la [demo interactiva](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/3_Reto/1_Trabajar/S07_demo_reto.html) (muestra lo que tendréis al final). Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_07_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_07.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-07/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `reto_S07.ipynb` · lo creáis
- [ ] `informe_modelado.md` · lo creáis a partir de una plantilla
- [ ] `README.md` · lo modificáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-07/`: 3 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 6). Aparte: reservas_turisdata.csv en `data/` si aún no está; Segundo modelo de clasificación (extra); los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el mié 11/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Regresión (MAE, RMSE, R²) y clasificación (matriz de confusión, AUC/AP) con *baseline*
- [ ] Costes de error explicitados, umbral justificado y recomendación con cifras
- [ ] Sin fuga de datos; test usado una sola vez
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los **cuadernos completos** (🏠 para casa) de los que hiciste en clase la parte «en clase». Traen **todos** los ejercicios y el mini-reto, se autocorrigen y llevan una «Solución de referencia» plegada por si te quedas atascado: [`S07_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_01_regresion_lineal_polinomica.ipynb) · [`S07_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_02_ridge_lasso.ipynb) · [`S07_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_03_regresion_logistica.ipynb) · [`S07_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/para_casa/S07_04_roc_pr_desbalance.ipynb).
- **Solucionarios** (para contrastar después de intentarlo): [cuadernos «en clase»](2_Practica/en_clase/Solucionario_en_clase.md) y [cuadernos completos](2_Practica/para_casa/Solucionario_para_casa.md).
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_regresion_y_clasificacion.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_07.md).
2. Mira el [código explicado](2_Practica/codigo_explicado/README.md) del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
| [`4_Referencia/`](4_Referencia/) | Resultados de los cuadernos (presentación y documento) e infografías |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| UD 3.3 | Regresión lineal y polinómica; regularización Ridge/Lasso |
| UD 3.4 | Regresión logística y clasificación |
| UD 3.5 | k-NN y Naive Bayes |

**Y ahora:** Sprint 8 · Árboles, ensembles y SVM (miércoles 11/11).

*9 h (2 h teoría · 4 h práctica · 3 h PBL).*
