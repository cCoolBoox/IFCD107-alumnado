# Sprint 3 · Del dato al modelo en la nube
**Pregunta guía:** ¿podemos tener un primer modelo funcionando, sin programar?
**Fechas:** 26–27/10 · **Horas:** 12 h (4 h teoría · 4 h práctica · 4 h proyecto)

> 🎯 **Reto de este sprint: «Primer modelo en producción».** 👉 [**Ver el reto completo, explicado paso a paso**](guia/Reto_Sprint_03.md) · [Reto en PDF](guia/Reto_Sprint_03.pdf) ([ecofriendly](guia/Reto_Sprint_03_ecofriendly.pdf)) · [PDF de la guía](guia/Guia_Sprint_03.pdf) · [Cómo se trabaja un reto](../../material/4.%20Como_se_trabaja_un_reto.md)

📄 **Este README en PDF:** [a color](README_Sprint_03.pdf) · [ecofriendly, para imprimir](README_Sprint_03_ecofriendly.pdf) (descárgalo para que funcionen los enlaces; la vista previa de GitHub no los abre).

## 📎 Material del sprint

- 📘 **Guía del sprint (PDF):** [`Guia_Sprint_03.pdf`](guia/Guia_Sprint_03.pdf) · [versión ecofriendly para imprimir](guia/Guia_Sprint_03_ecofriendly.pdf)
- 🎯 **Reto completo, paso a paso:** [`Reto_Sprint_03.md`](guia/Reto_Sprint_03.md)
- 🖼️ **Infografías del reto (2 láminas: el reto de un vistazo y cómo se trabaja y se evalúa):** [`infografias/`](infografias/)
- 🧪 **Guía de laboratorio AutoML (AutoGluon):** [`Guia_AutoML_AutoGluon.pdf`](guia/Guia_AutoML_AutoGluon.pdf)
- 🖥️ **S03.1 · Bases de datos relacionales y SQL:** [`S03.1_Bases_de_datos_relacionales_y_SQL.pdf`](presentaciones/S03.1_Bases_de_datos_relacionales_y_SQL.pdf)
- 🖥️ **S03.2 · Bases de datos NoSQL:** [`S03.2_Bases_de_datos_NoSQL.pdf`](presentaciones/S03.2_Bases_de_datos_NoSQL.pdf)
- 🖥️ **S03.3 · AutoML y MLOps:** [`S03.3_AutoML_y_MLOps.pdf`](presentaciones/S03.3_AutoML_y_MLOps.pdf)

**📁 En esta carpeta:** [`infografias/`](infografias/) láminas ilustradas del reto · [`guia/`](guia/) PDF de la guía (normal y para imprimir) y el reto explicado paso a paso · [`presentaciones/`](presentaciones/) diapositivas de cada sesión · [`notebooks/`](notebooks/) prácticas para abrir en Colab · [`recursos/`](recursos/) scripts y ficheros de apoyo · [`tests/`](tests/) test de conocimientos

<!--orden:ini-->
## 🧭 Orden de trabajo del sprint

Sigue los pasos **en este orden**: primero la teoría, después la práctica que la aplica y, por último, el reto. Los tiempos son orientativos; si el docente cambia el ritmo, mantén el orden.

📖 teoría (diapositivas) · 💻 práctica (cuaderno de Colab o actividad) · 🎯 reto en equipo · 🔔 ceremonia de Scrum

**Lunes 26/10**

1. 🔔 **Ceremonia**: Planning del reto «Primer modelo en producción»: leed la ficha y repartid roles · _10 min_
2. 📖 **Teoría**: [Modelo relacional, SQL, CRUD y nociones de administración](presentaciones/S03.1_Bases_de_datos_relacionales_y_SQL.pdf) · _1 h 30 min_
3. 💻 **Práctica**: Scripts SQL 01–04 en DB Browser, en este orden: [`SELECT`](recursos/sql/01_select_where.sql), [`JOIN`](recursos/sql/02_join.sql), [`GROUP BY`](recursos/sql/03_group_by.sql) y [subconsultas](recursos/sql/04_subconsultas.sql). **Para casa:** [CRUD sobre una copia](recursos/sql/05_crud.sql) y [modelado e índices](recursos/sql/06_modelado_indices.sql) · _1 h 30 min_
4. 📖 **Teoría**: [Bases de datos NoSQL (demostración corta)](presentaciones/S03.2_Bases_de_datos_NoSQL.pdf) · _30 min_
5. 💻 **Práctica**: [NoSQL con documentos](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/notebooks/S03_01_nosql_mongomock.ipynb) (o, si usáis MongoDB Compass, la [guía de MongoDB](guia/NoSQL_MongoDB.md)) · _30 min_

**Martes 27/10**

6. 📖 **Teoría**: [Introducción a AutoML y MLOps](presentaciones/S03.3_AutoML_y_MLOps.pdf) · _30 min_
7. 💻 **Práctica**: [Carga y exploración de datos y primer experimento de AutoML (guía de laboratorio)](guia/Guia_AutoML_AutoGluon.pdf) · _45 min_
8. 🎯 **Reto**: [Reto «Primer modelo en producción»: entender el problema → comparar modelos → elegir el umbral → publicar el servicio → **cerrar y borrar los recursos** → informe (pasos 1–6)](guia/Reto_Sprint_03.md) · _1 h 50 min_
9. 📝 **Test**: [**Test del bloque M6–M8** (bases de datos, AutoML y responsabilidad), solo se abre hoy](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/tests/test_M6-M8.html) · _25 min_
10. 🔔 **Ceremonia**: Entrega en `sprint-03/`, autoevaluación y coevaluación, review y retrospectiva · _40 min_

<!--orden:fin-->

## Qué aprenderás
- Consultar y modificar una base de datos con SQL, y modelarla con claves e índices.
- Guardar datos como documentos en MongoDB y decidir cuándo usar SQL o NoSQL.
- Lanzar un experimento de AutoML, leer sus métricas y elegir un umbral con criterio de negocio.
- Servir un modelo por API y cerrar los recursos. Requisito: Sprint 2 y DB Browser for SQLite; no hace falta programar.

## Prácticas
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

## Reto · «Primer modelo en producción»

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

## 📝 Test de conocimientos · mar 27/10
**Test del bloque M6–M8 · SQL, AutoML e IA responsable** · 10 preguntas · unos 15 min · individual, en el navegador, sin penalización por fallo. Cubre M6–M8 (SQL/NoSQL, AutoML e IA responsable).

👉 **[Abrir el test](https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/tests/test_M6-M8.html)** (`https://ccoolboox.github.io/IFCD107-alumnado/sprints/S03/tests/test_M6-M8.html`)

**Solo se abre el día mar 27/10** (hora de Canarias). Al terminar, copia tu resultado y envíaselo al docente. Cuenta para el 30 % de «tests de conocimientos».

## ✅ Antes de cerrar el sprint
- [ ] Test de conocimientos hecho el mar 27/10
- [ ] Informe con las tres partes, en 4 páginas o menos
- [ ] Métrica y umbral justificados en lenguaje de negocio, y variables excluidas por fuga explicadas
- [ ] Llamada a la API probada, sin credenciales
- [ ] Recursos cerrados o eliminados, con prueba
- [ ] Entregable subido a la carpeta `sprint-03/` del repositorio del equipo
- [ ] Autoevaluación y coevaluación rellenadas
