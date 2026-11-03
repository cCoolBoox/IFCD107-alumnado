# README Sprint S03 · Del dato al modelo en la nube

**Pregunta guía:** ¿podemos tener un primer modelo funcionando, sin programar?  
**Fechas:** 26–30/10 · **Horas:** 30 h (16 h teoría · 7 h práctica · 7 h proyecto)

📄 **Para imprimir:** todos los documentos del sprint en PDF, a color y ecofriendly, están juntos en la carpeta [`pdf/`](pdf/) (descárgalos para que funcionen los enlaces).

> **Sigue el orden de arriba abajo y abre solo lo que pone en cada fila.** Los demás documentos del sprint son para consultar si te atascas (apartado «Si te atascas»). Si el tiempo aprieta, haz solo lo que pone en las filas de cada día: lo demás es para casa.

## Qué aprenderás

1. A **consultar y modificar** una base de datos relacional con SQL (`SELECT`, `JOIN`, `GROUP BY`, subconsultas, `INSERT`/`UPDATE`/`DELETE`).
2. A **modelar** datos con claves, restricciones e índices, y a explicar por qué importan.
3. A guardar el mismo dato como **documentos** en MongoDB y a decidir cuándo conviene SQL o NoSQL.
4. A lanzar un **experimento de AutoML**, leer sus métricas y elegir un umbral con criterio de negocio.
5. A **servir un modelo por API** y a controlar y cerrar los recursos que usas.

## Día 1 · Lunes 26/10

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 🔔 Ceremonia · Planning del reto «Primer modelo en producción»: leed la ficha y repartid roles | — | 10 |
| ☐ | 📖 Teoría · Modelo relacional, SQL, CRUD y nociones de administración | [Presentación S03_01](1_Teoria/S03_01_presentacion_Bases_de_datos_relacionales_y_SQL.pdf) | 40 |
| ☐ | 💻 Práctica · Scripts SQL 01–06 en DB Browser, en este orden: `SELECT`, `JOIN`, `GROUP BY` y subconsultas; después, CRUD sobre una copia y modelado e índices | [`SELECT`](2_Practica/sql/01_select_where.sql) | 105 |
| ☐ | 📖 Teoría · Bases de datos NoSQL (demostración corta) | [Presentación S03_02](1_Teoria/S03_02_presentacion_Bases_de_datos_NoSQL.pdf) | 15 |
| ☐ | 💻 Práctica · NoSQL con documentos (o, si usáis MongoDB Compass, la guía de MongoDB) | [NoSQL con documentos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/2_Practica/S03_01_nosql_mongomock.ipynb) | 30 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Sé escribir un `SELECT` con `JOIN` y `GROUP BY`.
- [ ] Sé cuándo elegir una base relacional y cuándo una NoSQL.

## Día 2 · Martes 27/10

| ☐ | Qué haces | Abre | Min |
|---|---|---|---|
| ☐ | 📖 Teoría · Introducción a AutoML y MLOps | [Presentación S03_03](1_Teoria/S03_03_presentacion_AutoML_y_MLOps.pdf) | 20 |
| ☐ | 💻 Práctica · Carga, exploración y primer experimento de AutoML: cuaderno en Colab con la guía en parejas y el listado de pasos (pasos 0 a 5) | [cuaderno en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/2_Practica/laboratorio_automl/S3.5_lab_autogluon.ipynb) | 35 |
| ☐ | 🎯 Reto · Reto «Primer modelo en producción»: entender el problema → comparar modelos → elegir el umbral → publicar el servicio → **cerrar y borrar los recursos** → informe (pasos 1–6) | [Reto en una página](3_Reto/1_Trabajar/Reto_Sprint_03_una_pagina.md) | 80 |
| ☐ | 📝 Test · **Test del bloque M6–M8** (bases de datos, AutoML y responsabilidad) | [Abrir](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/tests/test_M6-M8.html) | 25 |
| ☐ | 🔔 Ceremonia · Entrega en `sprint-03/`, autoevaluación y coevaluación, review y retrospectiva | — | 40 |

**En clase: 3 h 20 min.**

**Al acabar el día, deberías poder decir:**

- [ ] Informe del mejor modelo, evidencia de la llamada al servicio e informe de recursos en `sprint-03/`.
- [ ] Recursos cerrados y borrados (0 €).
- [ ] Test M6–M8 hecho y autoevaluación/coevaluación rellenadas.

## El reto en pocas palabras

**Qué os pide el cliente.** TurisData ha perdido dinero porque algunas reservas se cancelan a última hora y la habitación se queda vacía. Os envía su histórico de reservas y os pide: *«¿Se puede construir algo que avise de qué reservas tienen más riesgo de cancelarse, y que mi equipo de reservas lo consulte desde otra aplicación?»* Es decir: **un modelo de IA funcionando como un servicio**, no solo un experimento.

**Qué vais a entregar:** un único informe de máximo 4 páginas con tres partes: el mejor modelo (con su umbral y sus costes), la evidencia de la llamada a la API y el informe de recursos y costes, con la prueba de que habéis cerrado todo.

**Núcleo y extra.** Núcleo: el mejor modelo con su umbral (con vuestros costes), la llamada al servicio, el cierre y borrado de recursos (0 €) y el informe con riesgos y recomendación. Extra: comparar más modelos o ajustes, probar la API con datos imposibles, estimar el beneficio en euros o comprobar un posible sesgo con los datos.

Para trabajar: [reto en una página](3_Reto/1_Trabajar/Reto_Sprint_03_una_pagina.md). Para entregar: [qué se sube y rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md). Para consultar: [ficha del reto](3_Reto/3_Consultar/Reto_Sprint_03.md) (qué pide el cliente, ayudas y errores frecuentes) y [cada paso explicado](3_Reto/3_Consultar/).

## ✅ Antes de cerrar el sprint (Definition of Done)

**Archivos subidos en el repositorio del equipo, carpeta `sprint-03/`** (marca cada uno cuando lo veas en GitHub):
- [ ] `informe_modelo.md` · lo creáis a partir de una plantilla
- [ ] `captura_cierre.png` · lo creáis
- [ ] `autoevaluacion_nombre.md` · **uno por persona** (la coevaluación va dentro del mismo fichero): [plantilla](3_Reto/2_Entregar/autoevaluacion_y_coevaluacion.md)

**Total en `sprint-03/`: 2 ficheros del equipo + 1 hoja por persona** (un equipo de 3 sube 5). Aparte: S3.5_lab_autogluon.ipynb; los extras solo si los hacéis. La *review* y la *retro* no se suben.

**Comprobaciones antes de dar el sprint por cerrado:**
- [ ] Test de conocimientos hecho el mar 27/10
- [ ] Informe con las tres partes, en 4 páginas o menos
- [ ] Métrica y umbral justificados en lenguaje de negocio, y variables excluidas por fuga explicadas
- [ ] Llamada a la API probada, sin credenciales
- [ ] Recursos cerrados o eliminados, con prueba
- [ ] Alguien que **no escribió esa parte** ha revisado el entregable con la [rúbrica](3_Reto/2_Entregar/entrega_y_rubrica.md) y lo ha anotado en el propio entregable

## En casa (cuando puedas)

- Los ejercicios de cada cuaderno que **no** se hacen en clase. Se autocorrigen, y debajo llevan una «Solución de referencia» plegada por si te quedas atascado.
- Si quieres repasar la teoría con calma: [apuntes del sprint](1_Teoria/apuntes/apuntes_sql_nosql_y_automl.md).

## Si te atascas

1. Lee primero la parte «Si os atascáis» de la [ficha completa del reto](3_Reto/3_Consultar/Reto_Sprint_03.md).
2. Pregunta a tu equipo y, después, al docente. Si usas IA, cuenta en el README qué te dijo y qué comprobaste.

## Todo el material, por carpetas

Las carpetas están **numeradas en el orden en que las usas**. Cada documento está en `.md`.

| Carpeta | Qué hay |
|---|---|
| [`1_Teoria/`](1_Teoria/) | Las presentaciones del sprint y los apuntes para repasar |
| [`2_Practica/`](2_Practica/) | Las actividades del sprint: dinámicas, hojas de ejercicios, guías y scripts |
| [`3_Reto/`](3_Reto/) | `1_Trabajar` (reto en una página, plantillas y datos) · `2_Entregar` (qué se sube, rúbrica y autoevaluación) · `3_Consultar` (ficha del reto y cada paso explicado) |
| [`4_Referencia/`](4_Referencia/) | Infografías del sprint |

Cómo se trabaja un reto, en todos los sprints: [método de trabajo](../../material/4.%20Como_se_trabaja_un_reto.md).

## Temario oficial de este sprint

| Unidad | Conceptos que entran |
|---|---|
| M6a · Bases de datos SQL y NoSQL (UD 6a.1 a 6a.3) | Tablas, claves, relaciones, normalización básica · DDL/DML y CRUD: CREATE, INSERT, SELECT, UPDATE, DELETE; WHERE, ORDER BY, JOIN, GROUP BY · Índices, transacciones (ACID), copias de seguridad, usuarios y permisos · Buenas prácticas: nombrado, integridad, evitar SELECT , consultas parametrizadas · Tipos: documental, clave-valor, columnar, grafos; comparativa con SQL · CRUD en MongoDB (Compass/Atlas); cuándo elegir cada tipo |
| M7 · AutoML y MLOps (UD 7.1 a 7.4) | Qué es AutoML; beneficios y límites frente al ML tradicional · Plataformas: SageMaker (Canvas/Autopilot), Vertex AI, Azure AutoML, H2O · Principios de MLOps: ciclo, versionado, despliegue, monitorización, deriva de datos · Cuenta, IAM, costes y buenas prácticas de seguridad; almacenamiento en S3 · Carga y tratamiento del dataset; visualización y calidad de datos · Tipo de problema y métrica objetivo; lanzamiento del experimento · Revisión de modelos candidatos, explicabilidad, validación y evaluación · Despliegue de un endpoint; invocación por API · Seguridad de acceso (IAM, API Gateway/Lambda), monitorización, control de costes |

**Y ahora:** Sprint 4 · Python para IA (martes 3/11).

*12 h (4 h teoría · 4 h práctica · 4 h PBL).*
