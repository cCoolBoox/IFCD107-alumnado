-- =====================================================================
-- 05 · CRUD: INSERT, SELECT, UPDATE, DELETE   (TurisData Canarias)
-- Tiempo estimado: 20 min (los ejercicios marcados "reto" son opcionales)
-- IMPORTANTE: NO modificamos las tablas originales. Trabajamos sobre una
-- COPIA llamada reservas_practica. Así puedes equivocarte sin miedo.
-- En DB Browser for SQLite, los cambios no quedan guardados en el archivo
-- hasta pulsar "Escribir cambios" (Ctrl+S). Si algo sale mal: "Revertir cambios".
-- Regla de oro: antes de un UPDATE o DELETE, escribe el mismo WHERE en un
-- SELECT y comprueba QUÉ filas vas a tocar. Sin WHERE se modifica TODO.
-- =====================================================================

-- ---------- PREPARACIÓN: una copia de trabajo con las reservas de 2025 ----------
DROP TABLE IF EXISTS reservas_practica;
CREATE TABLE reservas_practica AS
SELECT id_reserva, id_cliente, id_alojamiento, fecha_llegada, noches, canal, tarifa, precio_noche, cancelada
FROM reservas
WHERE fecha_llegada LIKE '2025%';

SELECT COUNT(*) AS filas_copia FROM reservas_practica;

-- ---------- IDEA 1: INSERT (crear) ----------
-- Siempre nombra las columnas: el código sigue funcionando si la tabla cambia.
INSERT INTO reservas_practica (id_reserva, id_cliente, id_alojamiento, fecha_llegada, noches, canal, tarifa, precio_noche, cancelada)
VALUES (900001, 1, 1, '2025-12-24', 3, 'directo', 'flexible', 120.0, 0);

-- ---------- IDEA 2: UPDATE (modificar) ----------
-- Paso 1: SELECT para ver qué se va a tocar. Paso 2: el UPDATE con el mismo WHERE.
SELECT id_reserva, precio_noche FROM reservas_practica WHERE id_reserva = 900001;
UPDATE reservas_practica SET precio_noche = 135.0 WHERE id_reserva = 900001;

-- ---------- IDEA 3: DELETE (borrar) ----------
DELETE FROM reservas_practica WHERE id_reserva = 900001;

-- ---------- IDEA 4: transacciones (todo o nada) ----------
BEGIN;
DELETE FROM reservas_practica WHERE canal = 'agencia';
SELECT COUNT(*) AS quedan_tras_borrar_agencia FROM reservas_practica;
ROLLBACK;   -- deshace el borrado; con COMMIT se confirmaría
SELECT COUNT(*) AS quedan_tras_rollback FROM reservas_practica;

-- ---------- EJERCICIOS ----------

-- EJERCICIO 5.1: Inserta una reserva nueva (id_reserva 900002) del cliente 2 en el alojamiento 3, llegada '2025-11-15', 4 noches, canal 'web_intermediaria', tarifa 'no_reembolsable', precio 88.5, no cancelada.
-- PISTA: INSERT INTO reservas_practica (columnas...) VALUES (valores...).
-- (escribe aquí tu consulta)

-- EJERCICIO 5.2: Comprueba con un SELECT que la reserva 900002 existe y tiene 4 noches.
-- PISTA: WHERE id_reserva = 900002.
-- (escribe aquí tu consulta)

-- EJERCICIO 5.3: El alojamiento 3 sube un 10 % los precios de las reservas con llegada posterior a '2025-11-01'. Primero haz el SELECT de las filas afectadas y después el UPDATE (precio_noche = precio_noche * 1.10).
-- PISTA: el WHERE del SELECT y del UPDATE debe ser idéntico.
-- (escribe aquí tu consulta)

-- EJERCICIO 5.4: Comprueba que el precio de la reserva 900002 es ahora 97.35.
-- PISTA: SELECT precio_noche ... ; el valor esperado sale de 88.5 * 1.10.
-- (escribe aquí tu consulta)

-- EJERCICIO 5.5: Marca como canceladas (cancelada = 1) las reservas de la copia con canal 'empresa' y tarifa 'flexible' cuya llegada sea en diciembre de 2025.
-- PISTA: primero cuenta cuántas son con un SELECT COUNT(*).
-- (escribe aquí tu consulta)

-- EJERCICIO 5.6: Borra de la copia las reservas con noches = 1 y canceladas (cancelada = 1). Cuenta antes cuántas son.
-- PISTA: SELECT COUNT(*) primero; luego DELETE con el mismo WHERE.
-- (escribe aquí tu consulta)

-- EJERCICIO 5.7: Comprueba que ya no queda ninguna reserva de 1 noche cancelada (debe salir 0).
-- PISTA: el mismo COUNT(*) del ejercicio anterior.
-- (escribe aquí tu consulta)

-- EJERCICIO 5.8: Con una transacción: empieza (BEGIN), borra TODAS las reservas de la copia, comprueba que la tabla queda vacía y deshaz con ROLLBACK. Comprueba después que las filas han vuelto.
-- PISTA: BEGIN; DELETE FROM reservas_practica; SELECT COUNT(*) ...; ROLLBACK; SELECT COUNT(*) ...
-- (escribe aquí tu consulta)

-- EJERCICIO 5.9 (reto): Sin usar la tabla original, ¿cuántas reservas tiene cada canal en la copia tras tus cambios? Escríbelo con GROUP BY y verifica que la suma coincide con COUNT(*).
-- PISTA: SELECT canal, COUNT(*) ... GROUP BY canal.
-- (escribe aquí tu consulta)

-- ---------- LIMPIEZA (al terminar) ----------
DROP TABLE IF EXISTS reservas_practica;
