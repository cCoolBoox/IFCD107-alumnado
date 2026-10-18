-- =====================================================================
-- 01 · SELECT, WHERE, ORDER BY, LIMIT   (TurisData Canarias · turisdata.db)
-- Tiempo estimado: 20 min (los ejercicios marcados "reto" son opcionales)
-- Cómo usarlo: abre turisdata.db en DB Browser for SQLite (o súbelo a un
-- cliente SQLite en línea), pestaña "Ejecutar SQL". Selecciona UNA consulta
-- y ejecútala (Ctrl+Intro). Cada consulta termina en punto y coma.
-- Tablas: alojamientos(id_alojamiento, nombre, isla, categoria, plazas)
--         clientes(id_cliente, pais, email_hash, cliente_desde)
--         reservas(id_reserva, id_cliente, id_alojamiento, fecha_reserva,
--                  fecha_llegada, antelacion_dias, noches, adultos, ninos,
--                  tipo_habitacion, regimen, canal, pais_origen, tarifa,
--                  deposito, precio_noche, peticiones_especiales,
--                  cliente_repetidor, cancelaciones_previas, cancelada)
-- Los datos son SINTÉTICOS: no son estadísticas reales del turismo canario.
-- =====================================================================

-- ---------- IDEA 1: SELECT elige columnas; FROM elige la tabla ----------
SELECT nombre, isla, plazas FROM alojamientos;

-- El asterisco trae todas las columnas (útil para mirar, no para producción).
SELECT * FROM alojamientos LIMIT 5;

-- ---------- IDEA 2: WHERE filtra filas ----------
SELECT nombre, categoria, plazas
FROM alojamientos
WHERE isla = 'Tenerife' AND plazas > 100;

-- ---------- IDEA 3: ORDER BY ordena y LIMIT recorta ----------
SELECT id_reserva, canal, noches, precio_noche
FROM reservas
ORDER BY precio_noche DESC
LIMIT 3;

-- ---------- EJERCICIOS ----------

-- EJERCICIO 1.1: Muestra el nombre y la categoría de todos los alojamientos.
-- PISTA: solo dos columnas, sin WHERE.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.2: Alojamientos de la isla de Lanzarote (nombre y plazas).
-- PISTA: el texto va entre comillas simples y respeta mayúsculas.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.3: Hoteles con más de 100 plazas, del que tiene más plazas al que tiene menos.
-- PISTA: dos condiciones con AND y ORDER BY ... DESC.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.4: ¿En qué islas tiene alojamientos TurisData? Cada isla una sola vez.
-- PISTA: DISTINCT delante de la columna.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.5: Reservas CANCELADAS (cancelada = 1) del canal 'directo' de más de 5 noches. Muestra id_reserva, noches y precio_noche.
-- PISTA: tres condiciones unidas con AND.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.6: Las 5 reservas con mayor precio por noche (id_reserva, tipo_habitacion, precio_noche).
-- PISTA: ORDER BY ... DESC y LIMIT.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.7: Reservas cuya llegada es en agosto de 2025 (las fechas son texto 'AAAA-MM-DD').
-- PISTA: BETWEEN '2025-08-01' AND '2025-08-31' o LIKE '2025-08%'.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.8: Clientes de Reino Unido (UK) o Alemania (DE).
-- PISTA: IN ('UK', 'DE') es más limpio que dos OR.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.9: Reservas sin país de origen registrado (dato ausente = NULL).
-- PISTA: no se escribe = NULL; existe IS NULL.
-- (escribe aquí tu consulta)

-- EJERCICIO 1.10 (reto): Reservas de suites con depósito total que NO se cancelaron y con petición especial (peticiones_especiales >= 1).
-- PISTA: usa paréntesis si mezclas AND y OR; aquí solo necesitas AND.
-- (escribe aquí tu consulta)
