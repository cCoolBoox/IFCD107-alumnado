# Sprint 3 · Del dato al modelo en la nube
**Pregunta guía:** ¿podemos tener un primer modelo funcionando, sin programar?
**Fechas:** 23–27/10 · **Horas:** 14 h (5 h teoría · 5 h práctica · 4 h proyecto)

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_03.pdf`](Guia_Sprint_03.pdf)
- 🧪 **Guía de laboratorio AutoML (AutoGluon):** [`Guia_AutoML_AutoGluon.pdf`](Guia_AutoML_AutoGluon.pdf)
- 🖥️ **S03.1 · Bases de datos relacionales y SQL:** [`S03.1_Bases_de_datos_relacionales_y_SQL.pdf`](presentaciones/S03.1_Bases_de_datos_relacionales_y_SQL.pdf)
- 🖥️ **S03.2 · Bases de datos NoSQL:** [`S03.2_Bases_de_datos_NoSQL.pdf`](presentaciones/S03.2_Bases_de_datos_NoSQL.pdf)
- 🖥️ **S03.3 · AutoML y MLOps:** [`S03.3_AutoML_y_MLOps.pdf`](presentaciones/S03.3_AutoML_y_MLOps.pdf)

## Qué aprenderás
- Consultar y modificar una base de datos con SQL, y modelarla con claves e índices.
- Guardar datos como documentos en MongoDB y decidir cuándo usar SQL o NoSQL.
- Lanzar un experimento de AutoML, leer sus métricas y elegir un umbral con criterio de negocio.
- Servir un modelo por API y cerrar los recursos. Requisito: Sprint 2 y DB Browser for SQLite; no hace falta programar.

## Prácticas
**Bloque A · SQL.** Abre `turisdata.db` (datos sintéticos) en DB Browser for SQLite, pestaña *Ejecutar SQL*, y sigue los scripts en orden:

| Script | Tema |
|---|---|
| [`sql/01_select_where.sql`](sql/01_select_where.sql) | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `NULL` |
| [`sql/02_join.sql`](sql/02_join.sql) | `JOIN` y `LEFT JOIN` |
| [`sql/03_group_by.sql`](sql/03_group_by.sql) | Agregaciones, `GROUP BY`, `HAVING` |
| [`sql/04_subconsultas.sql`](sql/04_subconsultas.sql) | Subconsultas y `WITH` |
| [`sql/05_crud.sql`](sql/05_crud.sql) | `INSERT`, `UPDATE`, `DELETE`, transacciones |
| [`sql/06_modelado_indices.sql`](sql/06_modelado_indices.sql) | Claves, normalización e índices |

| Guía / cuaderno | Tema | Colab |
|---|---|---|
| [`NoSQL_MongoDB.md`](NoSQL_MongoDB.md) + `S03_01_nosql_mongomock` (opcional) | Reservas como documentos en MongoDB | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/S03_01_nosql_mongomock.ipynb) |

**Bloque B · AutoML.** Sigue la **[guía de laboratorio AutoML con AutoGluon](Guia_AutoML_AutoGluon.pdf)** (en Colab, sin coste, sin crear más cuentas). Tu docente además hará una **demostración con Amazon SageMaker** como referencia profesional.

## Reto · «Primer modelo en producción»
**Contexto:** TurisData Canarias quiere avisar de las reservas con más riesgo de cancelarse y consultarlo desde otra aplicación. Vosotros lo ponéis en marcha, del dato al servicio.
**Entregáis** (un documento `.md` o PDF de máx. 4 páginas, en la carpeta `sprint-03/` del repositorio del equipo):
- Informe del mejor modelo: modelos comparados, métrica, resultados en datos no vistos, umbral justificado y variables influyentes.
- Evidencia de una llamada real a la API, con su respuesta y sin claves visibles.
- Informe de recursos y costes, con prueba de que todo se ha cerrado o eliminado.
**Reglas:**
- 4 h de proyecto; solo datos sintéticos de TurisData y el límite de uso que indique el docente.
- Nunca claves, contraseñas ni cadenas de conexión en el informe ni en el repositorio.
- Evitad la fuga de datos: solo información disponible al hacer la reserva.
**Se valora:** corrección técnica, reproducibilidad, comunicación al cliente (qué hacer con una alerta) e IA responsable (falsas alertas, sesgos por país o canal), más umbral y fuga de datos bien justificados.

## 📝 Test de conocimientos · mar 27/10
**Test del bloque M6–M8 · SQL, AutoML e IA responsable** · 10 preguntas · unos 15 min · individual, en el navegador, sin penalización por fallo. Cubre M6–M8 (SQL/NoSQL, AutoML e IA responsable).

👉 **[Abrir el test](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/test_M6-M8.html)** (`https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/test_M6-M8.html`)

**Solo se abre el día mar 27/10** (hora de Canarias). Al terminar, copia tu resultado y envíaselo al docente. Cuenta para el 30 % de «tests de conocimientos».

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mar 27/10
- [ ] Informe con las tres partes, en 4 páginas o menos
- [ ] Métrica y umbral justificados en lenguaje de negocio, y variables excluidas por fuga explicadas
- [ ] Llamada a la API probada, sin credenciales
- [ ] Recursos cerrados o eliminados, con prueba
- [ ] Entregable subido a la carpeta `sprint-03/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
