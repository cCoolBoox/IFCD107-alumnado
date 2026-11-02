# Sprint 3 · Reto «Primer modelo en producción»

> **Ficha completa del reto, para consultar.** Para trabajar, [el reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md). Qué se sube y cómo se evalúa: [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md).
>
> - Volver al [README del sprint](../../README.md).
> - Si es vuestro primer reto: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).

## Ficha del reto

### 1 · 🎯 Qué os pide el cliente

**Qué os pide el cliente.** TurisData ha perdido dinero porque algunas reservas se cancelan a última hora y la habitación se queda vacía. Os envía su histórico de reservas (6.000, sintéticas) y os pregunta: *«¿Se puede construir algo que avise de qué reservas tienen más riesgo de cancelarse, y que mi equipo de reservas lo consulte desde otra aplicación?»* Es decir: **un modelo de IA funcionando como un servicio**, no solo un experimento. Vuestra respuesta es **un único informe de 4 páginas como máximo** con tres partes: el mejor modelo (con su umbral y sus costes), la evidencia de una llamada real a la API y el informe de recursos y costes, con la prueba de que habéis cerrado todo lo que creasteis.

**Cómo se trabaja.** Es vuestro primer modelo y no hace falta programar: usaréis **AutoML** (una herramienta que prueba varios modelos por vosotros) en un cuaderno de Colab que ya está escrito. El **laboratorio** del día 2 (35 minutos) hace la parte técnica; lo que **añade el reto**, y es lo que se evalúa, es lo que el cuaderno no hace: mirar los datos con SQL, razonar cada columna, poner **vuestros** importes, elegir el umbral con ellos, hacer la llamada a la API, cerrar y borrar, y contárselo a un directivo con sus riesgos y su recomendación. En clase tenéis 10 minutos de planning (día 1) y, el día 2, **80 minutos de reto en seis pasos** más 40 de entrega, review y retro; lo que no quepa se remata en casa esa tarde. El equipo decide hasta dónde llega: 🟢 mínimo, 🟡 estándar o 🔴 extra. **Reglas:** solo datos sintéticos de TurisData (nada de datos personales reales); nunca claves, contraseñas ni cadenas de conexión en el informe, en el repositorio ni en una IA; todo recurso que creéis se cierra o se elimina al terminar, y se demuestra; y el modelo solo puede usar información que se conoce **al hacer la reserva** (si usa otra, hace trampa: se llama *fuga de datos*).

---

### 2 · 🧰 Recursos del reto

| Recurso | Para qué lo usaréis | Dónde está |
|---|---|---|
| **El cuaderno del laboratorio** [`S3.5_lab_autogluon`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/2_Practica/laboratorio_automl/S3.5_lab_autogluon.ipynb) | Entrenar y comparar modelos, elegir el umbral con costes, publicar la API y medir los recursos. El reto lee sus salidas y añade lo que él no hace | Colab. Usad *Archivo → Guardar una copia en Drive* y compartidla con el equipo (permiso de edición) |
| **La guía en parejas** [`guia_automl_en_parejas.md`](../../2_Practica/automl/guia_automl_en_parejas.md) y el [listado de pasos](../../2_Practica/automl/listado_pasos_automl.md) | Saber qué debe salir en cada apartado del cuaderno y qué hacer si falla | Se abren en GitHub |
| **Los datos**: [`turisdata.db`](../../../../datos/turisdata.db) y `reservas_turisdata.csv` | La base de datos para SQL y el CSV (6.000 reservas, 18 columnas, sintéticas) que usa el cuaderno | `turisdata.db` se abre en DB Browser for SQLite; el cuaderno descarga el CSV solo |
| **Script SQL** [`03_group_by.sql`](../../2_Practica/sql/03_group_by.sql) y [esquema de la base](../../2_Practica/esquema_turisdata/esquema_turisdata.md) | Paso 1: porcentaje de cancelaciones por canal y qué significa cada columna | DB Browser for SQLite |
| **Presentación S03_03** [AutoML y MLOps](../../1_Teoria/S03_03_presentacion_AutoML_y_MLOps.pdf) y los [apuntes](../../1_Teoria/apuntes/apuntes_sql_nosql_y_automl.md) | Qué es AutoML, qué pesa en un modelo y qué cuesta dejar un servicio encendido | El docente la explica el día 2 (20 minutos) |
| **Plantilla del informe** [`plantilla_informe_modelo.md`](../1_Trabajar/plantillas/plantilla_informe_modelo.md) | Los siete apartados del informe y la revisión con la rúbrica | Copiadla como `informe_modelo.md` |
| **Cómo entregar en GitHub** | Subir el informe y la captura a `sprint-03/` | [Guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md) |
| **Autoevaluación y coevaluación** | Cada persona rellena su hoja | [Hoja del sprint](../2_Entregar/autoevaluacion_y_coevaluacion.md) |
| **Un asistente de IA** (opcional) | Entender una consulta o una métrica y pulir la redacción | Con las reglas de la «Ayuda 1» del paso a paso |

---

### 3 · 🪜 Guía paso a paso

Son seis pasos, de **80 minutos en total**, el día 2 y después del laboratorio, que ya ha entrenado el modelo (apartados 0 a 5 del cuaderno): aquí **lo leéis, lo cuestionáis y lo ponéis en marcha**, sin volver a entrenar. Cada paso dice **qué hacéis** (la lista corta), **cómo se hace** con el detalle, **qué deberíais ver** y **cuándo está hecho**. Las ayudas (IA, errores, atascos) están al final. Si el tiempo aprieta, completad el nivel mínimo y dejad el informe para el bloque de entrega y para casa. Todo número del informe sale de **vuestro** cuaderno, no de la guía.

**Cada paso tiene su propia página.** Abrid la que toque y volved aquí cuando acabéis:

- [Paso 1 · Entender el problema y los datos (día 2, 10 minutos)](Reto_Sprint_03_paso_1.md)
- [Paso 2 · Comparar los modelos y ver qué pesa (día 2, 10 minutos)](Reto_Sprint_03_paso_2.md)
- [Paso 3 · Elegir el umbral con vuestros costes (día 2, 25 minutos)](Reto_Sprint_03_paso_3.md)
- [Paso 4 · Publicar el servicio y hacer una llamada (día 2, 10 minutos)](Reto_Sprint_03_paso_4.md)
- [Paso 5 · Cerrar y borrar (día 2, 10 minutos)](Reto_Sprint_03_paso_5.md)
- [Paso 6 · Redactar el informe (día 2, 15 minutos)](Reto_Sprint_03_paso_6.md)

#### Ayuda 1 · Cómo usar la IA en este reto

La IA puede explicar una consulta o una métrica, pero **puede inventar resultados**. Reglas:
- **Todo número del informe sale de vuestro cuaderno**, no de la IA.
- **Nunca peguéis claves, contraseñas ni cadenas de conexión** en una IA, en el informe ni en el repositorio. Si ocurre por error, avisad al docente y cambiad la clave.
- **Comprobad lo que os diga**: ejecutad la consulta y mirad que hace lo que dice.

| Para qué | Ejemplo de petición | Qué comprobáis |
|---|---|---|
| Entender el SQL | «Explícame esta consulta SQL línea por línea: *[pega tu consulta]*» | Ejecutadla y comprobad que hace lo que dice |
| Interpretar una métrica | «Explícame qué es el AUC con un ejemplo de hotel, sin fórmulas» | Que podáis explicarlo vosotros |
| Redactar para un directivo | «Reescribe este párrafo para alguien que no sabe estadística: *[párrafo]*. No cambies las cifras» | Que las cifras sean idénticas |

#### Ayuda 2 · Errores frecuentes (y cómo evitarlos)

| Error | Por qué ocurre | Cómo evitarlo |
|---|---|---|
| Resultados «demasiado buenos» (casi 100 %) | Fuga de datos: una columna delata la respuesta | Revisad cada columna: ¿se conocería al reservar? |
| Elegir el modelo solo por la métrica más alta | Es lo más visible | Explicad por qué esa métrica y qué significa en euros |
| Barajar las filas al azar antes de partir | Es lo que se hace «de normal» | Entrenad con lo antiguo y evaluad con lo reciente |
| Dejar los 100 € y 40 € del cuaderno | Se ejecuta sin pensar | Poned vuestros importes y la razón de cada uno |
| Llamar a la API con el umbral 0,5 | Se olvida la celda que fija el umbral | Ejecutad la celda de `UMBRAL` y repetid la llamada |
| Cerrar Colab antes de apuntar las cifras | La sesión borra todo al cerrarse | Apuntad primero, guardad una copia en Drive y cerrad después |
| Capturas con claves o datos personales visibles | Prisa | Revisad la captura antes de subirla |
| Informe que solo habla de técnica | Se escribe para el docente | Releedlo como si fuerais el director de TurisData |

#### Ayuda 3 · Si os atascáis

1. **El cuaderno falla o tarda mucho:** leed el mensaje completo, buscadlo en «Si algo falla» del paso y en la sección 7 de la [guía en parejas](../../2_Practica/automl/guia_automl_en_parejas.md); para un ensayo, poned `LIMITE_TIEMPO = 15`.
2. **No sabemos qué columna es una trampa:** hacedlas todas en una tabla con «¿se conoce al reservar?» y discutidla en equipo (en este CSV lo normal es que solo sobre `id_reserva`).
3. **No sabemos qué importes poner:** calculad el ingreso medio de una reserva con SQL (paso 3), razonad qué parte se pierde y decid que son hipótesis.
4. **Se ha cerrado Colab sin apuntar algo:** abrid la copia guardada en Drive; si no la hay, volved a entrenar con `LIMITE_TIEMPO = 15`.
5. Más ayuda: [Cómo se trabaja un reto](../../../../material/4.%20Como_se_trabaja_un_reto.md).
