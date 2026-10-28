# Listado de los 50 ejercicios SQL · S03

> **Qué es:** el índice de todos los ejercicios de los scripts SQL, para saber **qué toca hacer** y **llevar la cuenta**. Los enunciados completos (con su pista) están **dentro de cada script** de [`sql/`](./): buscad `-- EJERCICIO n.m`. Cómo abrirlos: apartado 1 de la [guía en parejas](guia_sql_en_parejas.md).

**Cómo usarlo:** marcad la casilla cuando el resultado os cuadre (con la comprobación del paso 5 de la guía). Los marcados **(reto)** son opcionales: hacedlos si os sobra tiempo. Cuando acabéis cada ejercicio, podéis contrastar con el [solucionario paso a paso](soluciones_sql_paso_a_paso.md).

**Orden:** hay que hacerlos **en orden dentro de cada script**. En especial, los del **05 y 06** dependen de los anteriores.

## Qué campos tiene cada tabla

Imagen y explicación completa en el [esquema de turisdata.db](../esquema_turisdata/esquema_turisdata.md). Resumen:

| Tabla | Campos |
|---|---|
| `alojamientos` (20) | `id_alojamiento`, `nombre`, `isla`, `categoria`, `plazas` |
| `clientes` (2.500) | `id_cliente`, `pais`, `email_hash`, `cliente_desde` |
| `reservas` (6.000) | `id_reserva`, `id_cliente`, `id_alojamiento`, `fecha_reserva`, `fecha_llegada`, `antelacion_dias`, `noches`, `adultos`, `ninos`, `tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito`, `precio_noche`, `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`, `cancelada` |

**Se unen por:** `reservas.id_alojamiento = alojamientos.id_alojamiento` y `reservas.id_cliente = clientes.id_cliente`.

---

## Script 01 · Elegir columnas y filtrar filas

**Temas:** `SELECT`, `WHERE`, `ORDER BY`, `LIMIT` · **Archivo:** [`01_select_where.sql`](01_select_where.sql) · **10 ejercicios**

| ✓ | Nº | Qué piden |
|---|---|---|
| □ | **1.1** | Muestra el nombre y la categoría de todos los alojamientos. |
| □ | **1.2** | Alojamientos de la isla de Lanzarote (nombre y plazas). |
| □ | **1.3** | Hoteles con más de 100 plazas, del que tiene más plazas al que tiene menos. |
| □ | **1.4** | ¿En qué islas tiene alojamientos TurisData? Cada isla una sola vez. |
| □ | **1.5** | Reservas CANCELADAS (cancelada = 1) del canal 'directo' de más de 5 noches. Muestra id_reserva, noches y precio_noche. |
| □ | **1.6** | Las 5 reservas con mayor precio por noche (id_reserva, tipo_habitacion, precio_noche). |
| □ | **1.7** | Reservas cuya llegada es en agosto de 2025 (las fechas son texto 'AAAA-MM-DD'). |
| □ | **1.8** | Clientes de Reino Unido (UK) o Alemania (DE). |
| □ | **1.9** | Reservas sin país de origen registrado (dato ausente = NULL). |
| □ | **1.10** (reto) | Reservas de suites con depósito total que NO se cancelaron y con petición especial (peticiones_especiales >= 1). |

## Script 02 · Unir tablas con JOIN

**Temas:** `JOIN`, `LEFT JOIN` · **Archivo:** [`02_join.sql`](02_join.sql) · **7 ejercicios**

| ✓ | Nº | Qué piden |
|---|---|---|
| □ | **2.1** | Para cada reserva de Fuerteventura, muestra id_reserva, nombre del alojamiento y noches. |
| □ | **2.2** | Reservas de alojamientos de categoría 'casa rural' que se cancelaron: id_reserva, nombre y canal. |
| □ | **2.3** | Reservas de clientes cuya fecha 'cliente_desde' es anterior a 2020-01-01. Muestra id_reserva, id_cliente y cliente_desde. |
| □ | **2.4** | Tres tablas a la vez: id_reserva, país del cliente, isla del alojamiento y precio_noche, solo para clientes de 'Nordicos' que reservaron en 'Tenerife'. |
| □ | **2.5** | Clientes que NO tienen ninguna reserva (id_cliente y pais). |
| □ | **2.6** | Ingreso estimado de cada reserva (noches * precio_noche) con el nombre del alojamiento, las 10 más altas. |
| □ | **2.7** (reto) | Reservas en las que el país del cliente (clientes.pais) NO coincide con el país de origen que figura en la reserva (reservas.pais_origen), ignorando las que no tienen pais_origen. |

## Script 03 · Resumir con GROUP BY

**Temas:** `GROUP BY`, `HAVING`, funciones de agregación · **Archivo:** [`03_group_by.sql`](03_group_by.sql) · **8 ejercicios**

| ✓ | Nº | Qué piden |
|---|---|---|
| □ | **3.1** | Número de reservas de cada tipo de habitación. |
| □ | **3.2** | Precio medio por noche de cada tipo de habitación, redondeado a 2 decimales, del más caro al más barato. |
| □ | **3.3** | Tasa de cancelación (en %) por tarifa y por depósito. Una fila por combinación. |
| □ | **3.4** | Ingreso estimado total (SUM de noches * precio_noche) de las reservas NO canceladas, por isla. |
| □ | **3.5** | Canales con más de 500 reservas y su antelación media en días (1 decimal). |
| □ | **3.6** | Reservas por mes de llegada en 2025 (mes en formato '2025-01'...). |
| □ | **3.7** | Los 5 clientes con más reservas (id_cliente y número de reservas). |
| □ | **3.8** (reto) | Por isla y categoría de alojamiento: número de reservas, tasa de cancelación (%) y precio medio por noche; solo grupos con al menos 100 reservas. |

## Script 04 · Una consulta dentro de otra

**Temas:** subconsultas y `WITH` · **Archivo:** [`04_subconsultas.sql`](04_subconsultas.sql) · **8 ejercicios**

| ✓ | Nº | Qué piden |
|---|---|---|
| □ | **4.1** | Reservas con más noches que la media de noches de todas las reservas (id_reserva y noches). |
| □ | **4.2** | Alojamientos con más plazas que la media (nombre, isla y plazas). |
| □ | **4.3** | Clientes que han cancelado al menos una reserva (id_cliente y país), sin repetir clientes. |
| □ | **4.4** | Clientes que NO tienen ninguna reserva, ahora con NOT IN (compara con el ejercicio 2.5). |
| □ | **4.5** | La reserva (o reservas) con el mayor ingreso estimado (noches * precio_noche): id_reserva e ingreso. |
| □ | **4.6** | Canales cuya tasa de cancelación supera la tasa global (nombre del canal y %). Resuélvelo con una CTE. |
| □ | **4.7** | Alojamientos cuyo precio medio por noche está por encima del precio medio global (nombre y precio medio). |
| □ | **4.8** (reto) | Clientes repetidores "de riesgo": con 4 o más reservas y al menos el 75 % de ellas canceladas (id_cliente, reservas, % canceladas). |

## Script 05 · Crear, modificar y borrar (CRUD)

**Temas:** `INSERT`, `UPDATE`, `DELETE`, transacciones · **Archivo:** [`05_crud.sql`](05_crud.sql) · **9 ejercicios**

| ✓ | Nº | Qué piden |
|---|---|---|
| □ | **5.1** | Inserta una reserva nueva (id_reserva 900002) del cliente 2 en el alojamiento 3, llegada '2025-11-15', 4 noches, canal 'web_intermediaria', tarifa 'no_reembolsable', precio 88.5, no cancelada. |
| □ | **5.2** | Comprueba con un SELECT que la reserva 900002 existe y tiene 4 noches. |
| □ | **5.3** | El alojamiento 3 sube un 10 % los precios de las reservas con llegada posterior a '2025-11-01'. Primero haz el SELECT de las filas afectadas y después el UPDATE (precio_noche = precio_noche * 1.10). |
| □ | **5.4** | Comprueba que el precio de la reserva 900002 es ahora 97.35. |
| □ | **5.5** | Marca como canceladas (cancelada = 1) las reservas de la copia con canal 'empresa' y tarifa 'flexible' cuya llegada sea en diciembre de 2025. |
| □ | **5.6** | Borra de la copia las reservas con noches = 1 y canceladas (cancelada = 1). Cuenta antes cuántas son. |
| □ | **5.7** | Comprueba que ya no queda ninguna reserva de 1 noche cancelada (debe salir 0). |
| □ | **5.8** | Con una transacción: empieza (BEGIN), borra TODAS las reservas de la copia, comprueba que la tabla queda vacía y deshaz con ROLLBACK. Comprueba después que las filas han vuelto. |
| □ | **5.9** (reto) | Sin usar la tabla original, ¿cuántas reservas tiene cada canal en la copia tras tus cambios? Escríbelo con GROUP BY y verifica que la suma coincide con COUNT(*). |

## Script 06 · Diseñar tablas con reglas e índices

**Temas:** claves, `CHECK`, índices · **Archivo:** [`06_modelado_indices.sql`](06_modelado_indices.sql) · **8 ejercicios**

| ✓ | Nº | Qué piden |
|---|---|---|
| □ | **6.1** | Inserta en p_reservas la reserva 3 de 'DE', 5 noches, 70.0 € por noche y comprueba con un SELECT que hay 2 filas en total. |
| □ | **6.2** | Intenta insertar una reserva con 0 noches (id 4, país 'ES', 60.0 €). ¿Qué error da y por qué es bueno que falle? |
| □ | **6.3** | Intenta insertar otra reserva con id_reserva = 1. ¿Qué regla lo impide? |
| □ | **6.4** | Diseña una tabla p_valoraciones: id_valoracion (clave primaria), id_reserva (clave foránea a p_reservas, obligatoria), puntuacion (entero de 1 a 5, obligatoria), comentario (texto opcional). Inserta una valoración de 5 puntos para la reserva 1. |
| □ | **6.5** | Comprueba que tu tabla rechaza una puntuación 7 y una valoración de una reserva inexistente (99). Dos sentencias que deben fallar; ejecútalas por separado. |
| □ | **6.6** | Une p_valoraciones con p_reservas y p_paises para mostrar id_valoracion, puntuacion y nombre del país. |
| □ | **6.7** | Crea un índice sobre reservas(canal, cancelada) llamado idx_p_canal_cancelada y comprueba con EXPLAIN QUERY PLAN que la consulta SELECT canal, AVG(cancelada) FROM reservas WHERE canal = 'directo' lo utiliza. |
| □ | **6.8** (reto) | TurisData quiere guardar las experiencias contratadas en cada reserva (excursión, alquiler de coche...). Una reserva puede tener varias experiencias y una experiencia aparece en muchas reservas. Dibuja las tablas y las claves. ¿Qué tipo de relación es y qué tabla intermedia hace falta? |

**Total: 50 ejercicios.**
