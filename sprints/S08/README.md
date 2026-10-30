# README Sprint S08 · Árboles, ensembles y SVM

**Pregunta guía:** ¿cuál es el mejor modelo y cuánto nos cuesta mantenerlo?  
**Fechas:** 11–12 de noviembre · **Horas:** 9 h (2 h teoría · 3 h práctica · 4 h PBL)

📄 **Este README en PDF** (para imprimir; descárgalo para que funcionen los enlaces): [a color](pdf/README_Sprint_08.pdf) · [ecofriendly](pdf/README_Sprint_08_ecofriendly.pdf)

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo los ejercicios marcados «en clase»: el resto es para casa.

## Qué aprenderás

1. Entrenar un **árbol de decisión**, detectar su sobreajuste, podarlo y leer sus reglas y su importancia de variables.
2. Explicar la diferencia entre **bosque aleatorio** (promediar árboles) y **boosting** (corregir errores en cadena), y usar XGBoost y LightGBM con parada temprana.
3. Ajustar una **SVM** (`C`, `gamma`, kernel) y saber cuándo su coste la descarta.
4. Buscar hiperparámetros con **`GridSearchCV`** y **`RandomizedSearchCV`** sin engañarte con la nota de validación.
5. **Elegir un modelo campeón** justificando rendimiento, explicabilidad y coste, y documentarlo en una *model card*.

## Día 1 · Miércoles 11/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «Duelo de modelos» y pesos de los criterios (la «voz del cliente») | — | 10 |
| ☐ | 📖 Teoría · Árboles de decisión | [Presentación S08.1](1_Teoria/S08.1_Arboles_de_decision.pdf) | 25 |
| ☐ | 💻 Práctica · Árbol de decisión: reglas, poda e importancia (los ejercicios marcados «en clase») | [Cuaderno S08_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_01_arboles_decision.ipynb) | 35 |
| ☐ | 📖 Teoría · Ensembles: Random Forest y *boosting* | [Presentación S08.2](1_Teoria/S08.2_Ensembles_Random_Forest_y_Boosting.pdf) | 25 |

**En clase: 1 h 35 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Mi equipo ha acordado los pesos de rendimiento, explicabilidad y coste.
- [ ] Sé cómo decide un árbol y para qué sirve un ensemble.

## Día 2 · Jueves 12/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · Máquinas de vectores de soporte (SVM), versión corta | [Presentación S08.3](1_Teoria/S08.3_Maquinas_de_vectores_de_soporte.pdf) | 10 |
| ☐ | 💻 Práctica · Random Forest: bagging, OOB e importancia por permutación (los ejercicios marcados «en clase») | [Cuaderno S08_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_02_random_forest.ipynb) | 30 |
| ☐ | 💻 Práctica · Gradient Boosting, XGBoost y LightGBM (los ejercicios marcados «en clase») | [Cuaderno S08_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_03_boosting_xgboost_lightgbm.ipynb) | 25 |
| ☐ | 🎯 Reto · *Leaderboard* (*baseline*, logística, árbol y bosque), búsqueda de hiperparámetros para una familia, sensibilidad de los pesos, campeón, test **una sola vez**, ficha del modelo y README (pasos 1–5) | [Cuaderno S08_06](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_06_leaderboard_plantilla.ipynb) | 75 |
| ☐ | 📝 Test · **Test de M3 (parte 2)**, solo se abre hoy | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/tests/test_M3_parte2.html) | 25 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-08/`, autoevaluación y coevaluación, y review y retrospectiva de los Sprints 7 y 8 | — | 35 |

**En clase: 3 h 20 min.**

## El reto en pocas palabras

**Qué os pide el cliente.** TurisData ya sabe que se pueden predecir las cancelaciones (lo visteis en el Sprint 7). Ahora la pregunta es: **¿qué modelo ponemos en producción?** El gerente duda: *«¿el más preciso? ¿el que yo pueda entender? ¿el más barato de mantener?»*. Vuestro equipo tiene que **enfrentar varios modelos** (árboles, bosques, boosting y SVM), compararlos con las mismas reglas y **elegir un campeón con argumentos**.

**Qué vais a entregar:** `leaderboard_S08.csv` (plantilla), `model_card.md` (plantilla), el cuaderno `reto_S08.ipynb` y `README.md`.

**Núcleo y extra.** Núcleo: *leaderboard* con tres familias de modelos, pesos de los criterios, test una sola vez y ficha del modelo. Extra: más familias y búsqueda de hiperparámetros en varias.

Para trabajar: [reto en una página](3_Reto/1_Reto_en_una_pagina/Reto_Sprint_08_una_pagina.md). Para consultar: [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_08.md) (pasos, rúbrica, ayudas y errores frecuentes). Plantillas, datos y autoevaluación: [`3_Reto/4_Plantillas_y_entrega/`](3_Reto/4_Plantillas_y_entrega/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-08/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `leaderboard_S08.csv` · lo genera
- [ ] `reto_S08.ipynb` · lo modificáis
- [ ] `model_card.md` · lo creáis a partir de una plantilla
- [ ] `README.md` · lo creáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/4_Plantillas_y_entrega/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-08/`: 4 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 7). Los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el jue 12/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Leaderboard con ≥ 6 modelos de al menos 4 familias
- [ ] Hiperparámetros buscados con validación cruzada en train para dos familias
- [ ] AUC de test calculado una sola vez y `model_card.md` completa
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Ficha_completa/Reto_Sprint_08.md#rúbrica-del-reto--cómo-se-puntúa-y-cómo-se-revisa) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_arboles_ensembles_y_svm.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/2_Ficha_completa/Reto_Sprint_08.md).
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
| UD 3.6 | Árboles de decisión |
| UD 3.7 | Ensembles: Random Forest, Gradient Boosting, XGBoost |
| UD 3.8 | Máquinas de vectores de soporte (SVM) |

**Y ahora:** Sprint 9 · Segmentar, recomendar y aprender por refuerzo (viernes 13/11).

*9 h (2 h teoría · 3 h práctica · 4 h PBL).*
