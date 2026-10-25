# README Sprint S03 · Del dato al modelo en la nube

**Pregunta guía:** ¿podemos tener un primer modelo funcionando, sin programar?
**Fechas:** 26–27/10 · **Horas:** 12 h (4 h teoría · 4 h práctica · 4 h proyecto)

📄 **Este README en PDF:** [a color](README_Sprint_03.pdf) · [ecofriendly, para imprimir](README_Sprint_03_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## Qué aprenderás
1. A **consultar y modificar** una base de datos relacional con SQL (`SELECT`, `JOIN`, `GROUP BY`, subconsultas, `INSERT`/`UPDATE`/`DELETE`).
2. A **modelar** datos con claves, restricciones e índices, y a explicar por qué importan.
3. A guardar el mismo dato como **documentos** en MongoDB y a decidir cuándo conviene SQL o NoSQL.
4. A lanzar un **experimento de AutoML**, leer sus métricas y elegir un umbral con criterio de negocio.
5. A **servir un modelo por API** y a controlar y cerrar los recursos que usas.

## Requisitos previos
- Haber terminado el Sprint 2 (cuentas y herramientas preparadas).
- Un navegador actual. Para SQL: **DB Browser for SQLite** instalado, o un cliente SQLite en línea (consulta con tu docente cuál).
- No hace falta saber programar en este sprint. Los ejercicios de SQL y AutoML no usan Python; solo el laboratorio opcional de NoSQL (y el laboratorio de AutoML basado en cuadernos, si se usa).
- Datos: `turisdata.db` (SQLite con las tablas `alojamientos`, `clientes` y `reservas`). Son datos **sintéticos**: sirven para practicar, no son estadísticas reales del turismo en Canarias.

## 📎 Materiales del sprint

**Documentos del curso** (PDF y .md; las actividades van en la tabla siguiente)

| Material | Tema | Tiempo | Cuándo |
|---|---|---|---|
| [Guía del sprint (PDF)](guia/Guia_Sprint_03.pdf) · [ecofriendly](guia/Guia_Sprint_03_ecofriendly.pdf) | Resumen del sprint: qué aprenderás, temario, material, reto y conclusión | 2 páginas | Antes de empezar |
| [Reto completo, paso a paso (.md)](guia/Reto_Sprint_03.md) · [PDF](guia/Reto_Sprint_03.pdf) · [ecofriendly](guia/Reto_Sprint_03_ecofriendly.pdf) | Qué pide el cliente, pasos, rúbrica, ayudas y errores frecuentes | — | Antes del planning y durante el reto |
| [Resumen del sprint en una página](infografias/S03_00_resumen_del_sprint.png) | Lámina con la pregunta guía, qué aprenderás, cómo se reparte el sprint (teoría, práctica y reto) y dónde estás en el curso | — | Antes del planning |
| [Esquema del contenido y su relación con el reto](infografias/S03_07_esquema_contenido_y_reto.png) | Qué presentación prepara cada pieza del entregable, con el material que se reutiliza después | — | Antes del planning y como guía durante el reto |
| [Infografías del reto](infografias/) | 3 láminas ilustradas del reto | — | Reto |
| [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md) | El método de trabajo de todos los retos | — | Antes del primer reto |
| [`S03.1_Bases_de_datos_relacionales_y_SQL.pdf`](presentaciones/S03.1_Bases_de_datos_relacionales_y_SQL.pdf) | Modelo relacional, SQL, CRUD y nociones de administración | 40 min | Teoría · día 1 del S03 |
| [`S03.2_Bases_de_datos_NoSQL.pdf`](presentaciones/S03.2_Bases_de_datos_NoSQL.pdf) | Bases de datos NoSQL (demostración corta) | 15 min | Teoría · día 1 del S03 |
| [`S03.3_AutoML_y_MLOps.pdf`](presentaciones/S03.3_AutoML_y_MLOps.pdf) | Introducción a AutoML y MLOps | 20 min | Teoría · día 2 del S03 |
| [`Guia_AutoML_AutoGluon.pdf`](guia/Guia_AutoML_AutoGluon.pdf) | Guía de laboratorio de AutoML con AutoGluon | — | AutoML (Bloque B) |
| [Test de conocimientos](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/tests/test_M6-M8.html) | Test del bloque M6–M8 · SQL, AutoML e IA responsable · 10 preguntas · individual, en el navegador, sin penalización por fallo. | 15 min | Solo se abre el mar 27/10 (hora de Canarias) |

**Material de las actividades**

**Bloque A · SQL.** Abre `turisdata.db` (datos sintéticos) en DB Browser for SQLite, pestaña *Ejecutar SQL*, y sigue los scripts en orden:

| Script | Tema |
|---|---|
| [`sql/01_select_where.sql`](recursos/sql/01_select_where.sql) | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `NULL` |
| [`sql/02_join.sql`](recursos/sql/02_join.sql) | `JOIN` y `LEFT JOIN` |
| [`sql/03_group_by.sql`](recursos/sql/03_group_by.sql) | Agregaciones, `GROUP BY`, `HAVING` |
| [`sql/04_subconsultas.sql`](recursos/sql/04_subconsultas.sql) | Subconsultas y `WITH` |
| [`sql/05_crud.sql`](recursos/sql/05_crud.sql) | `INSERT`, `UPDATE`, `DELETE`, transacciones |
| [`sql/06_modelado_indices.sql`](recursos/sql/06_modelado_indices.sql) | Claves, normalización e índices |

| Guía / cuaderno | Tema | Colab |
|---|---|---|
| [`NoSQL_MongoDB.md`](guia/NoSQL_MongoDB.md) + `S03_01_nosql_mongomock` (opcional) | Reservas como documentos en MongoDB | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/notebooks/S03_01_nosql_mongomock.ipynb) |

**Bloque B · AutoML.** Sigue la **[guía de laboratorio AutoML con AutoGluon](guia/Guia_AutoML_AutoGluon.pdf)** (en Colab, sin coste, sin crear más cuentas). Tu docente además hará una **demostración con Amazon SageMaker** como referencia profesional.

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

**Día 1 del S03**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 1 | 🔔 Ceremonia | Planning del reto «Primer modelo en producción»: leed la ficha y repartid roles | 10 min |
| 2 | 📖 Teoría | [Modelo relacional, SQL, CRUD y nociones de administración](presentaciones/S03.1_Bases_de_datos_relacionales_y_SQL.pdf) | 40 min |
| 3 | 💻 Práctica | Scripts SQL 01–06 en DB Browser, en este orden: [`SELECT`](recursos/sql/01_select_where.sql), [`JOIN`](recursos/sql/02_join.sql), [`GROUP BY`](recursos/sql/03_group_by.sql) y [subconsultas](recursos/sql/04_subconsultas.sql); después, [CRUD sobre una copia](recursos/sql/05_crud.sql) y [modelado e índices](recursos/sql/06_modelado_indices.sql) | 1 h 40 min |
| 4 | 📖 Teoría | [Bases de datos NoSQL (demostración corta)](presentaciones/S03.2_Bases_de_datos_NoSQL.pdf) | 15 min |
| 5 | 💻 Práctica | [NoSQL con documentos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/notebooks/S03_01_nosql_mongomock.ipynb) (o, si usáis MongoDB Compass, la [guía de MongoDB](guia/NoSQL_MongoDB.md)) | 35 min |

**Día 2 del S03**

| Nº | Tipo | Qué se hace | Tiempo |
|---|---|---|---|
| 6 | 📖 Teoría | [Introducción a AutoML y MLOps](presentaciones/S03.3_AutoML_y_MLOps.pdf) | 20 min |
| 7 | 💻 Práctica | [Carga y exploración de datos y primer experimento de AutoML (guía de laboratorio)](guia/Guia_AutoML_AutoGluon.pdf) | 35 min |
| 8 | 🎯 Reto | [Reto «Primer modelo en producción»: entender el problema → comparar modelos → elegir el umbral → publicar el servicio → **cerrar y borrar los recursos** → informe (pasos 1–6)](guia/Reto_Sprint_03.md) | 1 h 20 min |
| 9 | 📝 Test | [**Test del bloque M6–M8** (bases de datos, AutoML y responsabilidad), solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/tests/test_M6-M8.html) | 25 min |
| 10 | 🔔 Ceremonia | Entrega en `sprint-03/`, autoevaluación y coevaluación, review y retrospectiva | 40 min |

<!--orden:fin-->

## Reto · «Primer modelo en producción»

📄 [Reto en PDF](guia/Reto_Sprint_03.pdf) · [ecofriendly](guia/Reto_Sprint_03_ecofriendly.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

👉 **[Ver el reto completo, explicado paso a paso](guia/Reto_Sprint_03.md)** (qué se pide, cómo hacerlo, cómo usar la IA, errores frecuentes y autoevaluación).


**Contexto:** TurisData Canarias quiere avisar de las reservas con más riesgo de cancelarse y consultarlo desde otra aplicación. Vosotros lo ponéis en marcha, del dato al servicio.

**Entregáis** (un documento `.md` o PDF de máx. 4 páginas, en la carpeta `sprint-03/` del repositorio del equipo):
- Informe del mejor modelo: modelos comparados, métrica, resultados en datos no vistos, umbral justificado y variables influyentes.
- Evidencia de una llamada real a la API, con su respuesta y sin claves visibles.
- Informe de recursos y costes, con prueba de que todo se ha cerrado o eliminado.

**Reglas:**
- Unas 3 h 30 min de proyecto; solo datos sintéticos de TurisData y el límite de uso que indique el docente.
- Nunca claves, contraseñas ni cadenas de conexión en el informe ni en el repositorio.
- Evitad la fuga de datos: solo información disponible al hacer la reserva.

**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente (qué hacer con una alerta) e IA responsable (falsas alertas, sesgos por país o canal), más umbral y fuga de datos bien justificados.

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mar 27/10
- [ ] Informe con las tres partes, en 4 páginas o menos
- [ ] Métrica y umbral justificados en lenguaje de negocio, y variables excluidas por fuga explicadas
- [ ] Llamada a la API probada, sin credenciales
- [ ] Recursos cerrados o eliminados, con prueba
- [ ] Entregable subido a la carpeta `sprint-03/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
