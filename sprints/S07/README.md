# README Sprint S07 · ML supervisado: regresión y clasificación

**Pregunta guía:** ¿podemos predecir el precio o la cancelación?  
**Fechas:** 10–11 de noviembre · **Horas:** 9 h (2 h teoría · 4 h práctica · 3 h PBL)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_07.pdf) · [ecofriendly](pdf/README_Sprint_07_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

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
| ☐ | 📖 Teoría · Regresión lineal, polinómica y regularización (Ridge y Lasso) | [Presentación S07.1](1_Teoria/S07.1_Regresion_lineal_polinomica_y_regularizacion.pdf) | 25 |
| ☐ | 💻 Práctica · Regresión lineal y polinómica (los ejercicios marcados «en clase») | [Cuaderno S07_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_01_regresion_lineal_polinomica.ipynb) | 40 |
| ☐ | 💻 Práctica · Ridge y Lasso (los ejercicios marcados «en clase») | [Cuaderno S07_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_02_ridge_lasso.ipynb) | 35 |
| ☐ | 📖 Teoría · Regresión logística y clasificación | [Presentación S07.2](1_Teoria/S07.2_Regresion_logistica_y_clasificacion.pdf) | 20 |
| ☐ | 💻 Práctica · Regresión logística (los ejercicios marcados «en clase») | [Cuaderno S07_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_03_regresion_logistica.ipynb) | 45 |
| ☐ | 🎯 Reto · Acordar las hipótesis de coste y hacer la regresión del precio (pasos 1–2) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_07_una_pagina.md) | 25 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé entrenar una regresión y una regresión logística con scikit-learn.
- [ ] Sé leer un coeficiente.

## Día 2 · Miércoles 11/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 💻 Práctica · ROC, PR y datos desbalanceados (los ejercicios marcados «en clase») | [Cuaderno S07_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_04_roc_pr_desbalance.ipynb) | 25 |
| ☐ | 📖 Teoría · k-NN y Naive Bayes | [Presentación S07.3](1_Teoria/S07.3_k_NN_y_Naive_Bayes.pdf) | 10 |
| ☐ | 🎯 Reto · Clasificación de la cancelación, análisis de sensibilidad, informe y README (pasos 3–5) | [Reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_07_una_pagina.md) | 30 |
| ☐ | 📝 Test · **Test de M3 (parte 1)**, solo se abre hoy | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S07/tests/test_M3_parte1.html) | 25 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-07/` y autoevaluación y coevaluación del Sprint 7 (la review y la retro se hacen junto con las del Sprint 8) | — | 15 |

**En clase: 1 h 45 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** El gerente de TurisData quiere **dos herramientas**:

**Qué vais a entregar:** `informe_modelado.md` (o PDF), el cuaderno `reto_S07.ipynb` y un `README.md`.

**Núcleo y extra.** Núcleo: regresión del precio y clasificación de la cancelación con las hipótesis de coste. Extra: análisis de sensibilidad completo.

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_07_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_07.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-07/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `reto_S07.ipynb` · lo creáis
- [ ] `informe_modelado.md` · lo creáis a partir de una plantilla
- [ ] `README.md` · lo modificáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-07/`: 3 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 6). Aparte: reservas_turisdata.csv en `data/` si aún no está; Segundo modelo de clasificación (extra); los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el mié 11/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Regresión (MAE, RMSE, R²) y clasificación (matriz de confusión, AUC/AP) con *baseline*
- [ ] Costes de error explicitados, umbral justificado y recomendación con cifras
- [ ] Sin fuga de datos; test usado una sola vez
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_07.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_regresion_y_clasificacion.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_07.md).
2. Mira el [código explicado](2_Practica/codigo_explicado/README.md) del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`; sus PDF (color y ecofriendly) están en la subcarpeta `pdf/`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Reto_en_una_pagina` · `2_Ficha_completa` · `3_Laminas` · `4_Plantillas_y_entrega` |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| UD 3.3 | Regresión lineal y polinómica; regularización Ridge/Lasso |
| UD 3.4 | Regresión logística y clasificación |
| UD 3.5 | k-NN y Naive Bayes |

**Y ahora:** Sprint 8 · Árboles, ensembles y SVM (miércoles 11/11).

*9 h (2 h teoría · 4 h práctica · 3 h PBL).*
