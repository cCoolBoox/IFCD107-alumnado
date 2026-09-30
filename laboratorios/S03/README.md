# Sprint 3 · Del dato al modelo en la nube

**Pregunta guía:** ¿podemos tener un primer modelo funcionando, sin programar?
**Fechas:** 23–27/10 · **Horas:** 5 h de teoría (T) · 5 h de práctica (P) · 4 h de proyecto (PBL) = 14 h

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

## Prácticas

### Bloque A · Bases de datos (sin Python)
Abre `turisdata.db` en DB Browser for SQLite, pestaña **Ejecutar SQL**, y sigue los scripts en orden. En cada uno hay ideas con ejemplos y ejercicios; la solución la comprobarás con tu docente o comparando tus resultados con la descripción del ejercicio. Los ejercicios marcados "reto" son opcionales.

| Script | Tema | Tiempo |
|---|---|---|
| [`sql/01_select_where.sql`](sql/01_select_where.sql) | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `NULL` | 20 min |
| [`sql/02_join.sql`](sql/02_join.sql) | `JOIN` de dos y tres tablas, `LEFT JOIN` | 20 min |
| [`sql/03_group_by.sql`](sql/03_group_by.sql) | Agregaciones, `GROUP BY`, `HAVING` | 25 min |
| [`sql/04_subconsultas.sql`](sql/04_subconsultas.sql) | Subconsultas y `WITH` (CTE) | 20 min |
| [`sql/05_crud.sql`](sql/05_crud.sql) | `INSERT`, `UPDATE`, `DELETE` y transacciones (sobre una copia) | 20 min |
| [`sql/06_modelado_indices.sql`](sql/06_modelado_indices.sql) | Claves, restricciones, normalización e índices | 25 min |

| Guía / cuaderno | Tema | Tiempo | Colab |
|---|---|---|---|
| [`NoSQL_MongoDB.md`](NoSQL_MongoDB.md) + `S03_01_nosql_mongomock` (opcional) | El mismo dato de reservas como documentos; consultas y agregaciones con MongoDB | 60 min | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/laboratorios/S03/S03_01_nosql_mongomock.ipynb) |

### Bloque B · AutoML y modelo en producción
**La guía de AutoML se publica el 23/10**, una vez confirmada la plataforma. El flujo es siempre el mismo: dato, experimento, evaluación, explicabilidad, servicio por API e informe de recursos. Tu docente te dirá qué ruta seguimos; el reto y el entregable son los mismos.

---

## Reto PBL · «Primer modelo en producción»  (4 h)

### Contexto del cliente
*TurisData Canarias* nos ha enviado el histórico de sus reservas. Cada cancelación de última hora le deja una habitación vacía y le cuesta ingresos. Quiere saber si un modelo puede **avisar de las reservas con más riesgo de cancelarse** y que su equipo de reservas lo consulte desde otra aplicación. Vosotros sois el equipo que lo pone en marcha, de los datos al servicio.

### Qué tenéis que entregar
Un único documento (Markdown o PDF, máximo 4 páginas) con tres partes:
1. **Informe del mejor modelo:** cómo se ha planteado el problema, qué modelos se compararon, métrica elegida y por qué, resultados en datos no vistos, umbral de decisión elegido con su justificación de negocio y variables más influyentes.
2. **Evidencia de la llamada a la API:** captura o texto de una petición real al servicio del modelo, con la respuesta (probabilidad de cancelación y alerta). Sin claves ni credenciales visibles.
3. **Informe de recursos y costes:** qué recursos se han creado, cuánto tiempo y capacidad se han usado, cuánto ha costado o cuánto habría costado, y **prueba de que se han cerrado o eliminado** todos.

### Restricciones
- **Tiempo:** 4 h de proyecto dentro del sprint.
- **Datos:** solo los datos sintéticos de TurisData. No subáis datos personales reales.
- **Recursos:** se trabaja con el límite de uso que indique el docente; todo recurso creado debe quedar cerrado o eliminado al terminar.
- **Seguridad:** nunca pongáis claves, contraseñas ni cadenas de conexión en el informe ni en repositorios.
- **Evitar la fuga de datos:** el modelo solo puede usar información disponible en el momento de hacer la reserva.

### Criterios de evaluación (rúbrica del curso, 0–4 en cada criterio)
| Criterio | Qué se mirará en este reto |
|---|---|
| **Corrección técnica** | Partición de datos adecuada, métrica coherente con el problema, comparación de modelos, umbral justificado, la API responde. |
| **Reproducibilidad** | Otra persona puede repetir el experimento con vuestro informe: datos, ajustes, versiones y pasos. |
| **Análisis y comunicación al cliente** | Conclusiones claras para alguien no técnico y recomendación accionable: qué hacer con una alerta y con qué límites. |
| **IA responsable** | Riesgos identificados (datos sintéticos, falsas alertas que perjudican a clientes, sesgos por país o canal) y medidas propuestas. |

### Pasos sugeridos
- **Día 1:** revisad el dato en la base (SQL), decidid la variable objetivo y las columnas que no se pueden usar (fuga). Preparad la plataforma elegida.
- **Día 2:** lanzad el experimento, comparad modelos, evaluad con una partición temporal y elegid el umbral. Publicad el servicio y haced la llamada.
- **Día 3:** cerrad y eliminad recursos, completad el informe de recursos, revisad con la rúbrica y preparad la demo.

### Qué se enseña en la review
Una demo de 5 minutos: (1) el problema y la métrica, (2) el mejor modelo y su umbral, (3) una llamada en directo a la API, (4) el informe de recursos con la prueba de cierre, (5) una recomendación para el cliente y un límite del modelo.

### Definition of Done
- [ ] El informe tiene las tres partes y cabe en 4 páginas.
- [ ] La métrica y el umbral están justificados en lenguaje de negocio.
- [ ] Hay evidencia de una llamada real a la API, sin credenciales.
- [ ] Se explica qué variables se excluyeron por posible fuga de datos.
- [ ] Todos los recursos creados están cerrados o eliminados y hay prueba.
- [ ] Se mencionan al menos dos riesgos de IA responsable y una medida.
- [ ] Otra persona del grupo ha revisado el informe con la rúbrica.

## Recursos
- Documentación de SQLite (lenguaje SQL): <https://www.sqlite.org/lang.html>
- DB Browser for SQLite: <https://sqlitebrowser.org/>
- Manual de MongoDB: <https://www.mongodb.com/docs/manual/>
- Documentación de PyMongo: <https://pymongo.readthedocs.io/>
- La guía de AutoML de la ruta elegida (ver arriba).
