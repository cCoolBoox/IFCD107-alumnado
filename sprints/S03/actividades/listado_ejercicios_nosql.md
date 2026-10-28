# Listado de ejercicios NoSQL · S03 (cuaderno `S03_01_nosql_mongomock`)

> **Qué es:** el índice de todos los ejercicios del cuaderno de NoSQL, para saber **qué toca hacer** y **llevar la cuenta**. Los enunciados completos (con su pista) están **dentro del cuaderno**, justo encima de cada celda con `...`. Cómo abrirlo: apartado 1 de la [guía en parejas](guia_nosql_en_parejas.md).

**Cómo usarlo:** marcad la casilla cuando la celda os diga **«Correcto»**. Cuando acabéis cada ejercicio, podéis contrastar con el [solucionario paso a paso](soluciones_nosql_paso_a_paso.md).

**Orden:** hay que hacerlos **de arriba abajo**. El ejercicio 5 **borra** documentos; la sección 5 vuelve a cargar la colección completa.

**Archivo:** [`S03_01_nosql_mongomock.ipynb`](../notebooks/S03_01_nosql_mongomock.ipynb) · [Abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S03/notebooks/S03_01_nosql_mongomock.ipynb)

---

## En clase (≈ 30 minutos)

| ✓ | Nº | Variable | Qué piden |
|---|---|---|---|
| □ | **1** | `n_canceladas` | **Contar documentos:** cuántas reservas tienen `cancelada` igual a `True`. |
| □ | **2** | `caras_tenerife` | **Filtrar:** lista de reservas de alojamientos de **Tenerife** con `precio_noche` mayor que 150. |
| □ | **3** | `n_riesgo` | **Operadores lógicos:** cuántas reservas son de canal `web_intermediaria` **o** de tarifa `flexible`, y además tienen `deposito` igual a `"sin_deposito"`. |
| □ | **4** | `precio_nuevo` | **Actualizar:** subir 5 euros el `precio_noche` de la reserva con `_id` 5760 usando `$inc`, y leer el nuevo precio. |
| □ | **5** | `a_borrar`, `quedan` | **Borrar con cuidado:** contar y borrar las reservas con `noches` igual a 1 y `cancelada` `True`; comprobar que no queda ninguna. |

## En casa

| ✓ | Nº | Variable | Qué piden |
|---|---|---|---|
| □ | **6** | `tasa_canal` | **Tasa de cancelación por canal:** pipeline que agrupa por `canal` y cuenta reservas y canceladas. |
| □ | **7** | `ingreso_isla` | **Ingreso por isla:** ingreso estimado (`noches * precio_noche`) de las reservas **no canceladas**, agrupado por `alojamiento.isla`. |
| □ | **Mini-reto** | `tasa_sql`, `tasa_mongo` | **La misma pregunta en SQL y en MongoDB:** tasa de cancelación (%) de cada isla, con las dos herramientas, y comprobar que coinciden. |
| □ | **Reflexión 1** | *(cuaderno de aprendizaje)* | Ventaja de guardar el alojamiento **dentro** de cada reserva y problema si cambia de nombre. |
| □ | **Reflexión 2** | *(cuaderno de aprendizaje)* | Para qué datos de TurisData usaríais MongoDB y para cuáles seguiríais con SQL. |
| □ | **Reflexión 3** | *(cuaderno de aprendizaje)* | Qué hay que pensar además al pasar de `mongomock` a un MongoDB real. |

**Total: 7 ejercicios + 1 mini-reto + 3 preguntas de reflexión.**

*Además hay tres «ejemplos resueltos» (de `find`, de `update_many` y de agregación) y un ejemplo con `$unwind`: **no son ejercicios**, son para ejecutar y mirar.*
