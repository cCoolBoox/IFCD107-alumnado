-- =====================================================================
-- 04 · Subconsultas y CTE   (TurisData Canarias · turisdata.db)
-- Tiempo estimado: 20 min (los ejercicios marcados "reto" son opcionales)
-- Idea: una consulta dentro de otra. Sirve para comparar cada fila con un
-- valor calculado (la media, el máximo...) o para trabajar por pasos.
-- =====================================================================

-- ---------- IDEA 1: subconsulta escalar (devuelve UN valor) ----------
SELECT id_reserva, precio_noche
FROM reservas
WHERE precio_noche > (SELECT AVG(precio_noche) FROM reservas)
LIMIT 5;

-- ---------- IDEA 2: subconsulta con IN (devuelve una lista) ----------
SELECT id_alojamiento, nombre
FROM alojamientos
WHERE id_alojamiento IN (SELECT id_alojamiento FROM reservas WHERE noches >= 20);

-- ---------- IDEA 3: CTE con WITH (dar nombre a un paso intermedio) ----------
WITH por_canal AS (
    SELECT canal, AVG(cancelada) AS tasa FROM reservas GROUP BY canal
)
SELECT canal, ROUND(100 * tasa, 1) AS pct
FROM por_canal
WHERE tasa > (SELECT AVG(cancelada) FROM reservas);

-- ---------- EJERCICIOS ----------

-- EJERCICIO 4.1: Reservas con más noches que la media de noches de todas las reservas (id_reserva y noches).
-- PISTA: subconsulta escalar con AVG(noches).
-- (escribe aquí tu consulta)

-- EJERCICIO 4.2: Alojamientos con más plazas que la media (nombre, isla y plazas).
-- PISTA: la misma idea, sobre la tabla alojamientos.
-- (escribe aquí tu consulta)

-- EJERCICIO 4.3: Clientes que han cancelado al menos una reserva (id_cliente y país), sin repetir clientes.
-- PISTA: WHERE id_cliente IN (SELECT ... FROM reservas WHERE cancelada = 1).
-- (escribe aquí tu consulta)

-- EJERCICIO 4.4: Clientes que NO tienen ninguna reserva, ahora con NOT IN (compara con el ejercicio 2.5).
-- PISTA: NOT IN sobre id_cliente de reservas. Ojo: si la subconsulta devolviera algún NULL, NOT IN no daría resultados; aquí no hay.
-- (escribe aquí tu consulta)

-- EJERCICIO 4.5: La reserva (o reservas) con el mayor ingreso estimado (noches * precio_noche): id_reserva e ingreso.
-- PISTA: compara con (SELECT MAX(noches * precio_noche) FROM reservas).
-- (escribe aquí tu consulta)

-- EJERCICIO 4.6: Canales cuya tasa de cancelación supera la tasa global (nombre del canal y %). Resuélvelo con una CTE.
-- PISTA: mira el ejemplo de la IDEA 3 y cámbialo para mostrar también el número de reservas.
-- (escribe aquí tu consulta)

-- EJERCICIO 4.7: Alojamientos cuyo precio medio por noche está por encima del precio medio global (nombre y precio medio).
-- PISTA: una CTE con el precio medio por alojamiento y una subconsulta escalar con el global.
-- (escribe aquí tu consulta)

-- EJERCICIO 4.8 (reto): Clientes repetidores "de riesgo": con 4 o más reservas y al menos el 75 % de ellas canceladas (id_cliente, reservas, % canceladas).
-- PISTA: CTE por cliente con COUNT(*) y AVG(cancelada); luego filtra.
-- (escribe aquí tu consulta)
