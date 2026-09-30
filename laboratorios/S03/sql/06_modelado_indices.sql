-- =====================================================================
-- 06 · Modelado relacional, restricciones e índices   (TurisData Canarias)
-- Tiempo estimado: 25 min (los ejercicios marcados "reto" son opcionales)
-- Idea: diseñar bien las tablas evita errores de datos antes de que ocurran.
--  - Clave primaria (PRIMARY KEY): identifica cada fila, única y sin nulos.
--  - Clave foránea (FOREIGN KEY): obliga a que la referencia exista.
--  - CHECK / NOT NULL / UNIQUE: reglas de calidad dentro de la base.
--  - Índice: "índice de un libro"; acelera búsquedas, cuesta espacio y escrituras.
-- Trabajamos con tablas nuevas de práctica (prefijo p_) que se borran al final.
-- En SQLite las claves foráneas hay que activarlas con PRAGMA foreign_keys = ON;
-- (en DB Browser suele estar activo por defecto).
-- =====================================================================
PRAGMA foreign_keys = ON;

-- ---------- IDEA 1: normalizar = no repetir información ----------
-- En 'reservas' aparece el país de origen como texto en cada fila.
-- Una tabla de países aparte evita errores tipo 'UK' / 'uk' / 'Reino Unido'.
DROP TABLE IF EXISTS p_reservas;
DROP TABLE IF EXISTS p_paises;

CREATE TABLE p_paises (
    codigo  TEXT PRIMARY KEY,          -- 'ES', 'UK'...
    nombre  TEXT NOT NULL UNIQUE
);

INSERT INTO p_paises (codigo, nombre) VALUES
    ('ES', 'España'), ('UK', 'Reino Unido'), ('DE', 'Alemania');

-- ---------- IDEA 2: tabla con clave primaria, foránea y CHECK ----------
CREATE TABLE p_reservas (
    id_reserva  INTEGER PRIMARY KEY,
    pais        TEXT REFERENCES p_paises(codigo),
    noches      INTEGER NOT NULL CHECK (noches >= 1),
    precio_noche REAL NOT NULL CHECK (precio_noche > 0)
);

INSERT INTO p_reservas (id_reserva, pais, noches, precio_noche) VALUES (1, 'UK', 3, 95.0);

-- Esta inserción DEBE fallar (el país 'XX' no existe). Selecciona solo esta sentencia y ejecútala:
-- lee el error. Si ejecutas todo el script de golpe, se detendrá aquí; continúa desde la siguiente sentencia.
INSERT INTO p_reservas (id_reserva, pais, noches, precio_noche) VALUES (2, 'XX', 2, 80.0);

-- ---------- IDEA 3: índices ----------
-- EXPLAIN QUERY PLAN muestra cómo piensa ejecutar la consulta SQLite.
-- SCAN = recorre toda la tabla; SEARCH ... USING INDEX = usa el índice.
EXPLAIN QUERY PLAN SELECT COUNT(*) FROM reservas WHERE id_cliente = 100;
CREATE INDEX IF NOT EXISTS idx_p_reservas_cliente ON reservas (id_cliente);
EXPLAIN QUERY PLAN SELECT COUNT(*) FROM reservas WHERE id_cliente = 100;

-- ---------- EJERCICIOS ----------

-- EJERCICIO 6.1: Inserta en p_reservas la reserva 3 de 'DE', 5 noches, 70.0 € por noche y comprueba con un SELECT que hay 2 filas en total.
-- PISTA: INSERT ... VALUES y luego SELECT COUNT(*).
-- (escribe aquí tu consulta)

-- EJERCICIO 6.2: Intenta insertar una reserva con 0 noches (id 4, país 'ES', 60.0 €). ¿Qué error da y por qué es bueno que falle?
-- PISTA: mira el CHECK de noches. Ejecútala sola.
-- (escribe aquí tu consulta)

-- EJERCICIO 6.3: Intenta insertar otra reserva con id_reserva = 1. ¿Qué regla lo impide?
-- PISTA: PRIMARY KEY implica UNIQUE. Ejecútala sola.
-- (escribe aquí tu consulta)

-- EJERCICIO 6.4: Diseña una tabla p_valoraciones: id_valoracion (clave primaria), id_reserva (clave foránea a p_reservas, obligatoria), puntuacion (entero de 1 a 5, obligatoria), comentario (texto opcional). Inserta una valoración de 5 puntos para la reserva 1.
-- PISTA: sigue el modelo de p_reservas; la puntuación lleva CHECK (puntuacion BETWEEN 1 AND 5).
-- (escribe aquí tu consulta)

-- EJERCICIO 6.5: Comprueba que tu tabla rechaza una puntuación 7 y una valoración de una reserva inexistente (99). Dos sentencias que deben fallar; ejecútalas por separado.
-- PISTA: INSERT con puntuacion = 7; INSERT con id_reserva = 99.
-- (escribe aquí tu consulta)

-- EJERCICIO 6.6: Une p_valoraciones con p_reservas y p_paises para mostrar id_valoracion, puntuacion y nombre del país.
-- PISTA: dos JOIN en cadena.
-- (escribe aquí tu consulta)

-- EJERCICIO 6.7: Crea un índice sobre reservas(canal, cancelada) llamado idx_p_canal_cancelada y comprueba con EXPLAIN QUERY PLAN que la consulta SELECT canal, AVG(cancelada) FROM reservas WHERE canal = 'directo' lo utiliza.
-- PISTA: CREATE INDEX nombre ON tabla (col1, col2); luego EXPLAIN QUERY PLAN + la consulta. Busca la palabra INDEX en el resultado.
-- (escribe aquí tu consulta)

-- EJERCICIO 6.8 (reto de diseño, sobre papel): TurisData quiere guardar las experiencias contratadas en cada reserva (excursión, alquiler de coche...). Una reserva puede tener varias experiencias y una experiencia aparece en muchas reservas. Dibuja las tablas y las claves. ¿Qué tipo de relación es y qué tabla intermedia hace falta?
-- PISTA: relación muchos a muchos -> tabla intermedia con dos claves foráneas.
-- (escribe aquí tu consulta)

-- ---------- LIMPIEZA (al terminar) ----------
DROP TABLE IF EXISTS p_reserva_experiencia;
DROP TABLE IF EXISTS p_experiencias;
DROP TABLE IF EXISTS p_valoraciones;
DROP TABLE IF EXISTS p_reservas;
DROP TABLE IF EXISTS p_paises;
DROP INDEX IF EXISTS idx_p_reservas_cliente;
DROP INDEX IF EXISTS idx_p_canal_cancelada;
