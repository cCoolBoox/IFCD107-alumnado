# Sprint 8 · Reto «Duelo de modelos»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_08_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** TurisData ya sabe que se pueden predecir las cancelaciones de reservas (lo visteis en el Sprint 7). Ahora el gerente pregunta: **¿qué modelo ponemos en producción?** Duda entre tres cosas: *«¿el más preciso? ¿el que yo pueda entender? ¿el más barato de mantener?»*. Vuestro equipo tiene que **enfrentar varios modelos** (árboles, bosques, *boosting* y SVM), medirlos todos con las mismas reglas en una tabla de resultados (el *leaderboard*) y **elegir un campeón con argumentos**. La idea clave: en la vida real **el modelo más preciso no siempre es el mejor**; uno un poco peor, pero que se entiende y se mantiene fácilmente, puede ser la mejor decisión. Por eso se decide con **tres criterios**: rendimiento, explicabilidad y coste.

**Cómo se trabaja.** No hace falta experiencia previa: el cuaderno `S08_06` ya trae las herramientas para medir todos los modelos igual, y vosotros rellenáis los huecos paso a paso. Hay una regla de oro: **el test se usa una sola vez, solo con el campeón**; probar varios modelos en el test y quedarse con el mejor es hacer trampa. El trabajo completo son unos **150 minutos de equipo** (cinco pasos): en clase tenéis 10 minutos de planning (día 1), **75 minutos de reto + 35 de entrega, review y retro** (día 2); lo que no quepa va a casa o a la 6.ª hora. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra.

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **Google Colab** (el navegador, sin instalar nada) con las librerías `scikit-learn`, `xgboost` y `lightgbm` | Ejecutar el cuaderno del reto | Ya instaladas en Colab |
| **El cuaderno del reto** [`S08_06_leaderboard_plantilla`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_06_leaderboard_plantilla.ipynb) | Medir todos los modelos igual, guardar `leaderboard_S08.csv`, calcular la puntuación global y evaluar el campeón en el test | Colab. Su [código explicado](../../2_Practica/codigo_explicado/S08_06_leaderboard_plantilla.md) |
| **Cuadernos de modelos**: [`S08_01` árboles](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_01_arboles_decision.ipynb), [`S08_02` bosques](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_02_random_forest.ipynb), [`S08_03` *boosting*](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_03_boosting_xgboost_lightgbm.ipynb) y [`S08_04` SVM](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_04_svm.ipynb) | Las pistas para cada familia de modelos | Colab; su [código explicado](../../2_Practica/codigo_explicado/README.md) |
| **Cuaderno de búsqueda de hiperparámetros** [`S08_05`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S08/2_Practica/S08_05_busqueda_hiperparametros.ipynb) | La guía para el paso 3 (`GridSearchCV` y `RandomizedSearchCV`). Es el cuaderno **del reto** que se hace **en casa la tarde del 11/11** (≈ 40 min; para el paso 3 os bastan las secciones 2 y 3): venid con él hecho al paso 3 | Colab; su [código explicado](../../2_Practica/codigo_explicado/S08_05_busqueda_hiperparametros.md) |
| **Presentaciones y apuntes** | Repasar cómo funciona cada modelo: [árboles](../../1_Teoria/S08.1_Arboles_de_decision.pdf), [ensembles](../../1_Teoria/S08.2_Ensembles_Random_Forest_y_Boosting.pdf), [SVM](../../1_Teoria/S08.3_Maquinas_de_vectores_de_soporte.pdf) y [apuntes](../../1_Teoria/apuntes/apuntes_arboles_ensembles_y_svm.md) | Carpeta `1_Teoria` |
| **Plantilla de la *model card*** [`model_card_plantilla.md`](../1_Trabajar/plantillas/model_card_plantilla.md) | La «ficha técnica» del campeón, con sus apartados | En GitHub: *Raw* y copiar el texto |
| **Plantilla del *leaderboard*** [`leaderboard_plantilla.csv`](../1_Trabajar/plantillas/leaderboard_plantilla.csv) | Ver qué columnas tiene la tabla (el cuaderno ya crea la vuestra) | Solo para consultar |
| **Los datos** [`reservas_turisdata.csv`](../../../../datos/reservas_turisdata.csv) | El problema: predecir la columna `cancelada`. Son reservas **sintéticas** | El cuaderno los descarga solo si no los encuentra |
| **Cómo entregar en GitHub** | Subir los ficheros a la carpeta `sprint-08/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender modelos y errores, y preparar la defensa | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son cinco pasos, de **150 minutos en total**. Cada uno dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. El calendario da menos tiempo de reto del que suman los pasos: el día 1 solo hay 10 minutos (el planning, donde se acuerdan los pesos; los otros 10 son para escribirlos justificados al empezar el día 2) y el día 2 hay 75 minutos de reto (los pasos 4 y 5), más la entrega, la review y la retro. **Los pasos 2 y 3 (55 minutos) se hacen dentro de las prácticas** `S08_02` y `S08_03` del día 2 (30 y 25 minutos), con los modelos que ahí estudiáis: en el cuaderno del reto solo los registráis. Los 10 minutos que faltan se hacen al final del día 2, en la **consolidación** (13:00–13:30) y en la **6.ª hora** (hasta las 14:30); la subida puede hacerse hasta esa hora. Si el tiempo aprieta, completad el nivel mínimo y dejad lo demás para casa.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Planning y pesos de los criterios (día 1, 20 minutos)](Reto_Sprint_08_paso_1.md)
- [Paso 2 · Primeros modelos en el leaderboard (día 2, 30 minutos)](Reto_Sprint_08_paso_2.md)
- [Paso 3 · *Boosting*, SVM y búsqueda de hiperparámetros (día 2, 25 minutos)](Reto_Sprint_08_paso_3.md)
- [Paso 4 · Elegir el campeón (día 2, 45 minutos)](Reto_Sprint_08_paso_4.md)
- [Paso 5 · *Model card*, README y entrega (día 2, 30 minutos)](Reto_Sprint_08_paso_5.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede ahorrar tiempo, pero **da respuestas que parecen correctas y no lo son**. Reglas:
- **La IA no decide el campeón:** lo decide el cálculo con vuestros pesos.
- **Todo lo que dé, lo ejecutáis y lo entendéis.** Si el docente pregunta por una línea o por un número de la *model card*, tenéis que saber explicarlo.
- **Declaradlo** en el README: qué pedisteis y qué revisasteis.
- **Nada de datos personales ni claves** en una IA.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender un modelo | «Explícame cómo funciona un bosque aleatorio con una analogía de votación de expertos, sin fórmulas» | Que podéis explicárselo al gerente |
| Entender un hiperparámetro | «¿Qué hace `max_depth` en un árbol? ¿Qué pasa si es muy grande?» | Que probáis valores y veis lo que ocurre (sobreajuste) |
| Redactar la *model card* | «Ayúdame a redactar la sección de limitaciones. Estos son los datos: *[resumen]*» | Que **todo** lo que escriba coincide con vuestros resultados |
| Preparar la defensa | «Hazme 5 preguntas difíciles que un gerente podría hacer sobre mi elección de campeón» | Que preparáis la respuesta con **vuestros** datos |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Comparar modelos con particiones distintas | Cada persona prueba «por su lado» | Usad el cuaderno plantilla y no cambiéis la celda de herramientas: mismos folds para todos |
| Ajustar hiperparámetros mirando el test | «Para ver si mejora» | Buscad solo con `X_train` y validación cruzada; `X_test` solo aparece en el paso 4 |
| Evaluar varios modelos en el test y quedarse con el mejor | Curiosidad o prisa | El test se usa **una vez**, con el campeón ya elegido; `auc_test` en una sola fila |
| Elegir por el AUC más alto sin mirar la desviación | «0,81 es más que 0,80» | Si las desviaciones se solapan, la diferencia puede ser ruido: elegid el más simple |
| `model_card` genérica | Se copian los ejemplos de la plantilla | Cada apartado con **vuestros** datos y riesgos |
| Olvidar la explicabilidad y el coste | Solo se mira la precisión | Puntuadlos y ponderadlos con `puntuacion_global` |
| Búsquedas que duran horas | «Más combinaciones» | Máximo 5 minutos por búsqueda: menos combinaciones o `RandomizedSearchCV` con pocas iteraciones |
| Se pierde el leaderboard | Colab borra los ficheros al cerrar y `REINICIAR = True` vuelve a empezar de cero | Descargad `leaderboard_S08.csv` antes de cerrar y no editéis el CSV a mano |
| El campeón no está en `catalogo` | Se registró un modelo ajustado y no se añadió al diccionario | Añadid cada modelo ajustado a `catalogo` con el mismo nombre del leaderboard |

#### Ayuda 3 · Si os atascáis

1. **No sabéis qué peso poner:** pensad en lo que diría el gerente. Si prioriza entender, sube la explicabilidad.
2. **La búsqueda tarda demasiado:** reducid el número de combinaciones o usad búsqueda aleatoria con pocas iteraciones.
3. **Dos modelos empatan:** es un resultado válido. Elegid el más simple y explicadlo.
4. **Falla una comprobación (`assert`) del cuaderno:** leed el mensaje, que dice qué esperaba, y repasad el ejercicio de esa celda y su [código explicado](../../2_Practica/codigo_explicado/S08_06_leaderboard_plantilla.md). Preguntad al equipo y, después, al docente.
