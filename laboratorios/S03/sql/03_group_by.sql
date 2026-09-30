-- =====================================================================
-- 03 · GROUP BY y agregaciones   (TurisData Canarias · turisdata.db)
-- Tiempo estimado: 25 min (los ejercicios marcados "reto" son opcionales)
-- Idea: agrupar filas y resumirlas con COUNT, SUM, AVG, MIN, MAX.
-- Truco útil: 'cancelada' vale 0/1, así que AVG(cancelada) es la
-- proporción de cancelaciones y SUM(cancelada) su número.
-- =====================================================================

-- ---------- IDEA 1: agregaciones sobre toda la tabla ----------
SELECT COUNT(*) AS reservas, ROUND(AVG(precio_noche), 2) AS precio_medio, SUM(cancelada) AS canceladas
FROM reservas;

-- ---------- IDEA 2: GROUP BY ----------
SELECT canal, COUNT(*) AS reservas, ROUND(100.0 * AVG(cancelada), 1) AS pct_cancelacion
FROM reservas
GROUP BY canal
ORDER BY pct_cancelacion DESC;

-- ---------- IDEA 3: HAVING filtra GRUPOS (WHERE filtra filas antes de agrupar) ----------
SELECT tipo_habitacion, COUNT(*) AS reservas
FROM reservas
GROUP BY tipo_habitacion
HAVING COUNT(*) > 1000;

-- ---------- EJERCICIOS ----------

-- EJERCICIO 3.1: Número de reservas de cada tipo de habitación.
-- PISTA: GROUP BY tipo_habitacion con COUNT(*).
-- (escribe aquí tu consulta)

-- EJERCICIO 3.2: Precio medio por noche de cada tipo de habitación, redondeado a 2 decimales, del más caro al más barato.
-- PISTA: ROUND(AVG(...), 2) y ORDER BY sobre el alias.
-- (escribe aquí tu consulta)

-- EJERCICIO 3.3: Tasa de cancelación (en %) por tarifa y por depósito. Una fila por combinación.
-- PISTA: GROUP BY con dos columnas.
-- (escribe aquí tu consulta)

-- EJERCICIO 3.4: Ingreso estimado total (SUM de noches * precio_noche) de las reservas NO canceladas, por isla.
-- PISTA: JOIN con alojamientos, WHERE cancelada = 0 y GROUP BY a.isla.
-- (escribe aquí tu consulta)

-- EJERCICIO 3.5: Canales con más de 500 reservas y su antelación media en días (1 decimal).
-- PISTA: HAVING COUNT(*) > 500.
-- (escribe aquí tu consulta)

-- EJERCICIO 3.6: Reservas por mes de llegada en 2025 (mes en formato '2025-01'...).
-- PISTA: SUBSTR(fecha_llegada, 1, 7) extrae AAAA-MM; filtra el año con LIKE '2025%'.
-- (escribe aquí tu consulta)

-- EJERCICIO 3.7: Los 5 clientes con más reservas (id_cliente y número de reservas).
-- PISTA: GROUP BY id_cliente, ORDER BY COUNT(*) DESC, LIMIT 5. ¿Hay empates? Añade un segundo criterio (id_cliente) para que el resultado sea estable.
-- (escribe aquí tu consulta)

-- EJERCICIO 3.8 (reto): Por isla y categoría de alojamiento: número de reservas, tasa de cancelación (%) y precio medio por noche; solo grupos con al menos 100 reservas.
-- PISTA: JOIN + GROUP BY a.isla, a.categoria + HAVING.
-- (escribe aquí tu consulta)
