-- =====================================================================
-- 02 · JOIN: combinar tablas   (TurisData Canarias · turisdata.db)
-- Tiempo estimado: 20 min (los ejercicios marcados "reto" son opcionales)
-- Idea: en una base relacional cada dato vive en UNA tabla y se enlaza
-- con claves. reservas.id_alojamiento apunta a alojamientos.id_alojamiento
-- y reservas.id_cliente apunta a clientes.id_cliente.
-- Las fechas son texto ISO (AAAA-MM-DD). Datos sintéticos.
-- =====================================================================

-- ---------- IDEA 1: INNER JOIN (solo filas con pareja en ambas tablas) ----------
-- Los alias (r, a) acortan la escritura y evitan ambigüedades.
SELECT r.id_reserva, a.nombre, a.isla, r.noches, r.precio_noche
FROM reservas AS r
JOIN alojamientos AS a ON a.id_alojamiento = r.id_alojamiento
LIMIT 5;

-- ---------- IDEA 2: unir tres tablas ----------
SELECT r.id_reserva, c.pais AS pais_cliente, a.isla, r.canal
FROM reservas r
JOIN clientes c ON c.id_cliente = r.id_cliente
JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
LIMIT 5;

-- ---------- IDEA 3: LEFT JOIN (conserva todas las filas de la tabla izquierda) ----------
-- Clientes que aparecen aunque no tengan reservas (las columnas de reservas salen NULL).
SELECT c.id_cliente, c.pais, r.id_reserva
FROM clientes c
LEFT JOIN reservas r ON r.id_cliente = c.id_cliente
WHERE r.id_reserva IS NULL
LIMIT 5;

-- ---------- EJERCICIOS ----------

-- EJERCICIO 2.1: Para cada reserva de Fuerteventura, muestra id_reserva, nombre del alojamiento y noches.
-- PISTA: JOIN con alojamientos y WHERE sobre a.isla.
-- (escribe aquí tu consulta)

-- EJERCICIO 2.2: Reservas de alojamientos de categoría 'casa rural' que se cancelaron: id_reserva, nombre y canal.
-- PISTA: dos filtros; el de categoría es de una tabla y el de cancelada, de otra.
-- (escribe aquí tu consulta)

-- EJERCICIO 2.3: Reservas de clientes cuya fecha 'cliente_desde' es anterior a 2020-01-01. Muestra id_reserva, id_cliente y cliente_desde.
-- PISTA: JOIN con clientes; compara textos de fecha con <.
-- (escribe aquí tu consulta)

-- EJERCICIO 2.4: Tres tablas a la vez: id_reserva, país del cliente, isla del alojamiento y precio_noche, solo para clientes de 'Nordicos' que reservaron en 'Tenerife'.
-- PISTA: dos JOIN encadenados.
-- (escribe aquí tu consulta)

-- EJERCICIO 2.5: Clientes que NO tienen ninguna reserva (id_cliente y pais).
-- PISTA: LEFT JOIN desde clientes y filtra r.id_reserva IS NULL.
-- (escribe aquí tu consulta)

-- EJERCICIO 2.6: Ingreso estimado de cada reserva (noches * precio_noche) con el nombre del alojamiento, las 10 más altas.
-- PISTA: una expresión con AS ingreso y ORDER BY ingreso DESC.
-- (escribe aquí tu consulta)

-- EJERCICIO 2.7 (reto): Reservas en las que el país del cliente (clientes.pais) NO coincide con el país de origen que figura en la reserva (reservas.pais_origen), ignorando las que no tienen pais_origen.
-- PISTA: <> y IS NOT NULL. ¿Por qué puede diferir? Coméntalo con tu grupo (calidad del dato).
-- (escribe aquí tu consulta)
