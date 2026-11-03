# README Sprint S08 · Árboles, ensembles y SVM

**Pregunta guía:** ¿cuál es el mejor modelo y cuánto nos cuesta mantenerlo?  
**Fechas:** 11–12 de noviembre · **Horas:** 9 h (2 h teoría · 3 h práctica · 4 h PBL)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

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
| ☐ | 📖 Teoría · Árboles de decisión: reglas, sobreajuste y poda | [Presentación S08_01](1_Teoria/S08_01_presentacion_Arboles_de_decision.pdf) | 25 |
| ☐ | 💻 Práctica · Árbol de decisión: reglas, poda e importancia (los ejercicios marcados «en clase») | [Cuaderno S08_01](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_01_arboles_decision.ipynb) | 35 |
| ☐ | 📖 Teoría · Random Forest: muchos árboles votan | [Presentación S08_02](1_Teoria/S08_02_presentacion_Random_Forest.pdf) | 15 |
| ☐ | 📖 Teoría · *Boosting*: corregir los errores paso a paso | [Presentación S08_03](1_Teoria/S08_03_presentacion_Boosting.pdf) | 10 |
| ☐ | 🏠 **En casa** · Buscar hiperparámetros con `GridSearchCV` y `RandomizedSearchCV`: **esta tarde**, para el paso 3 del reto de mañana (bastan sus secciones 2 y 3) | [Cuaderno S08_05](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_05_busqueda_hiperparametros.ipynb) · [Presentación S08_05](1_Teoria/S08_05_presentacion_Busqueda_de_hiperparametros.pdf) | 40 (casa) |

**En clase: 1 h 35 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Mi equipo ha acordado los pesos de rendimiento, explicabilidad y coste.
- [ ] Sé cómo decide un árbol y para qué sirve un ensemble.
- [ ] En casa, esta tarde: la práctica `S08_05` (≈ 40 min), la guía del paso 3 del reto de mañana.

## Día 2 · Jueves 12/11

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · Máquinas de vectores de soporte (SVM), versión corta | [Presentación S08_04](1_Teoria/S08_04_presentacion_Maquinas_de_vectores_de_soporte_SVM.pdf) | 10 |
| ☐ | 💻 Práctica · Random Forest: bagging, OOB e importancia por permutación (los ejercicios marcados «en clase») | [Cuaderno S08_02](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_02_random_forest.ipynb) · [Presentación S08_02](1_Teoria/S08_02_presentacion_Random_Forest.pdf) | 30 |
| ☐ | 💻 Práctica · Gradient Boosting, XGBoost y LightGBM (los ejercicios marcados «en clase») | [Cuaderno S08_03](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_03_boosting_xgboost_lightgbm.ipynb) · [Presentación S08_03](1_Teoria/S08_03_presentacion_Boosting.pdf) | 25 |
| ☐ | 🎯 Reto · *Leaderboard* (*baseline*, logística, árbol y bosque), búsqueda de hiperparámetros en dos familias, sensibilidad de los pesos, campeón, test **una sola vez**, ficha del modelo y README (pasos 4–5; los pasos 2–3 van dentro de las prácticas; lo que falte, en la consolidación y la 6.ª hora) | [Cuaderno S08_06](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_06_leaderboard_plantilla.ipynb) | 75 |
| ☐ | 📝 Test · **Test de M3 (parte 2)** | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/tests/test_M3_parte2.html) | 25 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-08/`, autoevaluación y coevaluación, y review y retrospectiva de los Sprints 7 y 8 | — | 35 |
| ☐ | 🏠 **En casa** · Máquinas de vectores de soporte, SVM (cuaderno completo) | [Cuaderno S08_04](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_04_svm.ipynb) · [Presentación S08_04](1_Teoria/S08_04_presentacion_Maquinas_de_vectores_de_soporte_SVM.pdf) | 40 (casa) |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé buscar hiperparámetros sin engañarme con la nota de validación.
- [ ] Sé elegir un modelo campeón justificando rendimiento, explicabilidad y coste.
- [ ] Sé usar el test una sola vez y documentar el modelo en una ficha (*model card*).

## El reto en pocas palabras

**Qué os pide el cliente.** TurisData ya sabe que se pueden predecir las cancelaciones (lo visteis en el Sprint 7). Ahora la pregunta es: **¿qué modelo ponemos en producción?** El gerente duda: *«¿el más preciso? ¿el que yo pueda entender? ¿el más barato de mantener?»*. Vuestro equipo tiene que **enfrentar varios modelos** (árboles, bosques, boosting y SVM), compararlos con las mismas reglas y **elegir un campeón con argumentos**.

**Qué vais a entregar:** `leaderboard_S08.csv` (plantilla), `model_card.md` (plantilla), el cuaderno `reto_S08.ipynb` y `README.md`.

**Núcleo y extra.** Núcleo: *leaderboard* con 6 modelos de al menos 4 familias, pesos de los criterios, test una sola vez y ficha del modelo. Estándar: búsqueda de hiperparámetros en dos familias y análisis de sensibilidad de los pesos. Extra: más familias y búsqueda en varias.

Antes de empezar, probad la [demo interactiva](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S08/3_Reto/1_Trabajar/S08_demo_reto.html) (muestra lo que tendréis al final). Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_08_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_08.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-08/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `leaderboard_S08.csv` · lo genera
- [ ] `reto_S08.ipynb` · lo modificáis
- [ ] `model_card.md` · lo creáis a partir de una plantilla
- [ ] `README.md` · lo modificáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-08/`: 4 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 7). Los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el jue 12/11
- [ ] Notebook ejecutable de principio a fin (`Restart & Run all`)
- [ ] Leaderboard con ≥ 6 modelos de al menos 4 familias
- [ ] Hiperparámetros buscados con validación cruzada en train para dos familias
- [ ] AUC de test calculado una sola vez y `model_card.md` completa
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_arboles_ensembles_y_svm.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_08.md).
2. Mira el [código explicado](2_Practica/codigo_explicado/README.md) del cuaderno en el que estás.
3. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Los cuadernos (Colab) y su explicación línea a línea en `codigo_explicado/` |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
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
