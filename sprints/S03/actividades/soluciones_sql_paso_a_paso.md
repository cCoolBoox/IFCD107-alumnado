# Solucionario SQL paso a paso · S03 (scripts 01–06)

> **Para quién:** alumnado de IFCD107. **Qué es:** las soluciones de los 50 ejercicios de SQL de [`guia_sql_en_parejas.md`](guia_sql_en_parejas.md), explicadas **paso a paso** y con el **resultado que debe salir**.

## Cómo usar este solucionario

1. **Primero intentadlo vosotros** (en pareja, con el ciclo de 6 pasos de la guía). Si miráis la solución antes, no aprendéis a escribir consultas, solo a copiarlas.
2. Cuando acabéis un ejercicio, mirad **solo «Qué debe salir»**: ¿os coincide el número de filas o el valor? Si coincide, probablemente está bien.
3. Si no coincide, leed **«Cómo pensarlo»** y buscad en qué paso se separa vuestra consulta de la nuestra.
4. Por último, comparad con la **consulta**. Puede haber **más de una forma correcta**: si la vuestra da el mismo resultado, también vale.
5. Corregid con otro color y anotad en la hoja de registro (apartado 8 de la guía) qué os ha costado.

**Nota:** si en un ejercicio no se pide orden, la fila que sale primera puede cambiar de un programa a otro. Lo que debe coincidir es el **número de filas** y los **valores**.

**Los datos:** `turisdata.db` tiene 3 tablas: `alojamientos` (20), `clientes` (2.500) y `reservas` (6.000). Son datos **sintéticos**. Si vuestro número de filas es distinto, comprobad que habéis abierto el archivo correcto.

---

## Script 01 · Elegir columnas y filtrar filas

`SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`. Las 10 consultas son sobre una sola tabla.

### Ejercicio 1.1

**Enunciado:** Muestra el nombre y la categoría de todos los alojamientos.

**Cómo pensarlo:**

1. Piden **dos columnas** (nombre y categoría) y **todas las filas**: no hace falta filtrar.
2. Por eso **no hay `WHERE`**: solo `SELECT` de las dos columnas y `FROM` la tabla.

**La consulta:**

```sql
SELECT nombre, categoria FROM alojamientos;
```

**Qué debe salir:**

- **20 filas**. Columnas: nombre, categoria. Ejemplo de fila: Alojamiento 01, hostal

**Ojo con:** Si ponéis `*` salen todas las columnas: funciona, pero **no es lo que piden**.

---

### Ejercicio 1.2

**Enunciado:** Alojamientos de la isla de Lanzarote (nombre y plazas).

**Cómo pensarlo:**

1. Ahora sí hay que **elegir filas**: solo las de una isla. Eso es un `WHERE`.
2. El texto va **entre comillas simples** y tal cual está escrito en la tabla (`'Lanzarote'`).

**La consulta:**

```sql
SELECT nombre, plazas FROM alojamientos WHERE isla = 'Lanzarote';
```

**Qué debe salir:**

- **5 filas**. Columnas: nombre, plazas. Ejemplo de fila: Alojamiento 03, 43

**Ojo con:** `Lanzarote` sin comillas da error `no such column`; `'lanzarote'` en minúscula no encontrará nada.

---

### Ejercicio 1.3

**Enunciado:** Hoteles con más de 100 plazas, del que tiene más plazas al que tiene menos.

**Cómo pensarlo:**

1. Hay **dos condiciones a la vez**: que sea hotel **y** que tenga más de 100 plazas. Se unen con `AND`.
2. El orden «del que más al que menos» es `ORDER BY plazas DESC` (DESC = descendente, de mayor a menor).

**La consulta:**

```sql
SELECT nombre, isla, plazas
FROM alojamientos
WHERE categoria = 'hotel' AND plazas > 100
ORDER BY plazas DESC;
```

**Qué debe salir:**

- **5 filas**. Columnas: nombre, isla, plazas. Ejemplo de fila: Alojamiento 20, Lanzarote, 199

**Ojo con:** `ORDER BY` va **al final**, después del `WHERE`.

---

### Ejercicio 1.4

**Enunciado:** ¿En qué islas tiene alojamientos TurisData? Cada isla una sola vez.

**Cómo pensarlo:**

1. La tabla repite la isla en varios alojamientos. Para ver **cada isla una sola vez** se pone `DISTINCT` justo después de `SELECT`.
2. El `ORDER BY isla` es un extra para verlas en orden alfabético.

**La consulta:**

```sql
SELECT DISTINCT isla FROM alojamientos ORDER BY isla;
```

**Qué debe salir:**

- **6 filas**. Columnas: isla. Ejemplo de fila: Fuerteventura

**Ojo con:** `DISTINCT` afecta a **todas las columnas** que pidáis: si pedís más de una, quita repetidos de la **combinación**.

---

### Ejercicio 1.5

**Enunciado:** Reservas CANCELADAS (cancelada = 1) del canal 'directo' de más de 5 noches. Muestra id_reserva, noches y precio_noche.

**Cómo pensarlo:**

1. Tres condiciones, **todas a la vez**: cancelada, canal directo y más de 5 noches. Tres condiciones = dos `AND`.
2. `cancelada = 1` (el 1 significa «sí» y el 0 «no»). El canal es texto, así que va entre comillas simples.
3. Las columnas que piden: `id_reserva`, `noches`, `precio_noche`.

**La consulta:**

```sql
SELECT id_reserva, noches, precio_noche
FROM reservas
WHERE cancelada = 1 AND canal = 'directo' AND noches > 5;
```

**Qué debe salir:**

- **209 filas**. Columnas: id_reserva, noches, precio_noche. Ejemplo de fila: 3234, 7, 123.28

**Ojo con:** `noches > 5` es **más de 5**: el 5 no entra. Para incluirlo sería `>= 5`.

---

### Ejercicio 1.6

**Enunciado:** Las 5 reservas con mayor precio por noche (id_reserva, tipo_habitacion, precio_noche).

**Cómo pensarlo:**

1. Primero **ordenamos** por precio de mayor a menor (`ORDER BY precio_noche DESC`).
2. Después **recortamos** a las 5 primeras con `LIMIT 5`.

**La consulta:**

```sql
SELECT id_reserva, tipo_habitacion, precio_noche
FROM reservas
ORDER BY precio_noche DESC
LIMIT 5;
```

**Qué debe salir:**

- **5 filas**. Columnas: id_reserva, tipo_habitacion, precio_noche. Ejemplo de fila: 4246, suite, 249.35

**Ojo con:** Si olvidáis el `DESC` salen las **5 más baratas**.

---

### Ejercicio 1.7

**Enunciado:** Reservas cuya llegada es en agosto de 2025 (las fechas son texto 'AAAA-MM-DD').

**Cómo pensarlo:**

1. Las fechas son **texto** con formato `AAAA-MM-DD`; los textos de ese formato se pueden comparar como si fueran fechas.
2. `BETWEEN '2025-08-01' AND '2025-08-31'` coge todo agosto (incluye los dos extremos).
3. Otra forma válida: `LIKE '2025-08%'` (empieza por 2025-08).

**La consulta:**

```sql
SELECT id_reserva, fecha_llegada, noches
FROM reservas
WHERE fecha_llegada BETWEEN '2025-08-01' AND '2025-08-31';
```

**Qué debe salir:**

- **254 filas**. Columnas: id_reserva, fecha_llegada, noches. Ejemplo de fila: 3607, 2025-08-28, 4

**Ojo con:** Las dos formas dan el mismo número de filas. **Probad las dos** y comprobadlo.

---

### Ejercicio 1.8

**Enunciado:** Clientes de Reino Unido (UK) o Alemania (DE).

**Cómo pensarlo:**

1. Queremos los clientes de **uno u otro** país. Se podría escribir `pais = 'UK' OR pais = 'DE'`, pero `IN ('UK', 'DE')` es más corto y limpio.
2. La tabla es `clientes`, no `reservas`.

**La consulta:**

```sql
SELECT id_cliente, pais FROM clientes WHERE pais IN ('UK', 'DE');
```

**Qué debe salir:**

- **624 filas**. Columnas: id_cliente, pais. Ejemplo de fila: 9, UK

**Ojo con:** El texto va en **mayúsculas** tal como está en la tabla (`'UK'`, `'DE'`).

---

### Ejercicio 1.9

**Enunciado:** Reservas sin país de origen registrado (dato ausente = NULL).

**Cómo pensarlo:**

1. Un dato que falta se guarda como **`NULL`** (ausente). `NULL` no es un valor, así que **no se compara con `=`**.
2. Se pregunta con `IS NULL`.

**La consulta:**

```sql
SELECT id_reserva, canal FROM reservas WHERE pais_origen IS NULL;
```

**Qué debe salir:**

- **138 filas**. Columnas: id_reserva, canal. Ejemplo de fila: 4055, web_intermediaria

**Ojo con:** `WHERE pais_origen = NULL` **no da error pero no devuelve nada**. Es el fallo más típico con `NULL`.

---

### Ejercicio 1.10

**Enunciado:** (reto): Reservas de suites con depósito total que NO se cancelaron y con petición especial (peticiones_especiales >= 1).

**Cómo pensarlo:**

1. Hay **cuatro condiciones** unidas con `AND`: suite, depósito total, no cancelada (`cancelada = 0`) y al menos una petición especial (`peticiones_especiales >= 1`).
2. Se puede escribir en varias líneas para que se lea mejor; SQL no distingue saltos de línea.

**La consulta:**

```sql
SELECT id_reserva, canal, precio_noche
FROM reservas
WHERE tipo_habitacion = 'suite' AND deposito = 'total'
  AND cancelada = 0 AND peticiones_especiales >= 1;
```

**Qué debe salir:**

- **27 filas**. Columnas: id_reserva, canal, precio_noche. Ejemplo de fila: 2951, web_intermediaria, 155.83

**Ojo con:** Revisad **cada condición por separado** si salen 0 filas: una sola mal escrita lo vacía todo.

---

## Script 02 · Unir tablas con `JOIN`

Cada `JOIN` necesita su `ON` con la **clave** que comparten las dos tablas. Usad alias (`r`, `a`, `c`) y ponedlos delante de las columnas.

### Ejercicio 2.1

**Enunciado:** Para cada reserva de Fuerteventura, muestra id_reserva, nombre del alojamiento y noches.

**Cómo pensarlo:**

1. Los alojamientos y las reservas están en **tablas distintas**: el nombre del alojamiento está en `alojamientos` y las noches en `reservas`. Hay que **unirlas**.
2. Se unen por la clave que comparten: `id_alojamiento`. Eso es el `ON`.
3. Los alias `r` y `a` acortan: `reservas r`, `alojamientos a`. Con ellos se escribe `r.noches` y `a.nombre`.
4. Después, el filtro de la isla es un `WHERE` sobre `a.isla`.

**La consulta:**

```sql
SELECT r.id_reserva, a.nombre, r.noches
FROM reservas r
JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
WHERE a.isla = 'Fuerteventura';
```

**Qué debe salir:**

- **867 filas**. Columnas: id_reserva, nombre, noches. Ejemplo de fila: 23, Alojamiento 13, 6

**Ojo con:** Si olvidáis el `ON`, o unís columnas que no son la clave, salen **miles de filas de más**.

---

### Ejercicio 2.2

**Enunciado:** Reservas de alojamientos de categoría 'casa rural' que se cancelaron: id_reserva, nombre y canal.

**Cómo pensarlo:**

1. Un filtro es de **una tabla** (`a.categoria = 'casa rural'`) y el otro de **otra** (`r.cancelada = 1`). Con el `JOIN` se pueden usar los dos en el mismo `WHERE`.
2. Columnas: `id_reserva` (reservas), nombre (alojamientos) y canal (reservas).

**La consulta:**

```sql
SELECT r.id_reserva, a.nombre, r.canal
FROM reservas r
JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
WHERE a.categoria = 'casa rural' AND r.cancelada = 1;
```

**Qué debe salir:**

- **423 filas**. Columnas: id_reserva, nombre, canal. Ejemplo de fila: 6, Alojamiento 08, web_intermediaria

**Ojo con:** Poned el **alias delante** de cada columna para saber de qué tabla viene.

---

### Ejercicio 2.3

**Enunciado:** Reservas de clientes cuya fecha 'cliente_desde' es anterior a 2020-01-01. Muestra id_reserva, id_cliente y cliente_desde.

**Cómo pensarlo:**

1. Aquí la tabla que se une es `clientes`, por `id_cliente`.
2. La fecha `cliente_desde` es texto `AAAA-MM-DD`: «anterior a 2020» es `< '2020-01-01'`.

**La consulta:**

```sql
SELECT r.id_reserva, c.id_cliente, c.cliente_desde
FROM reservas r
JOIN clientes c ON c.id_cliente = r.id_cliente
WHERE c.cliente_desde < '2020-01-01';
```

**Qué debe salir:**

- **1130 filas**. Columnas: id_reserva, id_cliente, cliente_desde. Ejemplo de fila: 4497, 1, 2019-05-28

**Ojo con:** Aunque `id_cliente` está en las dos tablas, **ponedlo con alias** (`c.id_cliente`) o dará `ambiguous column name`.

---

### Ejercicio 2.4

**Enunciado:** Tres tablas a la vez: id_reserva, país del cliente, isla del alojamiento y precio_noche, solo para clientes de 'Nordicos' que reservaron en 'Tenerife'.

**Cómo pensarlo:**

1. Hay que unir **tres tablas**: `reservas` con `clientes` y `reservas` con `alojamientos`. Son **dos `JOIN` seguidos**.
2. Los dos filtros son sobre las tablas unidas: país del cliente y isla del alojamiento.

**La consulta:**

```sql
SELECT r.id_reserva, c.pais, a.isla, r.precio_noche
FROM reservas r
JOIN clientes c ON c.id_cliente = r.id_cliente
JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
WHERE c.pais = 'Nordicos' AND a.isla = 'Tenerife';
```

**Qué debe salir:**

- **218 filas**. Columnas: id_reserva, pais, isla, precio_noche. Ejemplo de fila: 4975, Nordicos, Tenerife, 81.66

**Ojo con:** Cada `JOIN` lleva **su propio `ON`**.

---

### Ejercicio 2.5

**Enunciado:** Clientes que NO tienen ninguna reserva (id_cliente y pais).

**Cómo pensarlo:**

1. Queremos los clientes **sin** reserva. Si hacemos un `JOIN` normal, esos clientes **desaparecen** (no tienen pareja).
2. Con `LEFT JOIN` desde `clientes` **se conservan todos los clientes**; a los que no tienen reserva les sale `NULL` en las columnas de `reservas`.
3. Nos quedamos con los que tienen **`r.id_reserva IS NULL`**.

**La consulta:**

```sql
SELECT c.id_cliente, c.pais
FROM clientes c
LEFT JOIN reservas r ON r.id_cliente = c.id_cliente
WHERE r.id_reserva IS NULL;
```

**Qué debe salir:**

- **212 filas**. Columnas: id_cliente, pais. Ejemplo de fila: 9, UK

**Ojo con:** Con un `JOIN` normal esos clientes no aparecen; por eso aquí hace falta `LEFT JOIN`.

---

### Ejercicio 2.6

**Enunciado:** Ingreso estimado de cada reserva (noches * precio_noche) con el nombre del alojamiento, las 10 más altas.

**Cómo pensarlo:**

1. El ingreso no está en la tabla: **se calcula** `noches * precio_noche`. Se le da nombre con `AS ingreso`.
2. Se ordena por ese nombre de mayor a menor y se recortan las 10 primeras.

**La consulta:**

```sql
SELECT r.id_reserva, a.nombre, r.noches * r.precio_noche AS ingreso
FROM reservas r
JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
ORDER BY ingreso DESC
LIMIT 10;
```

**Qué debe salir:**

- **10 filas**. Columnas: id_reserva, nombre, ingreso. Ejemplo de fila: 3971, Alojamiento 15, 2667.21

**Ojo con:** Se puede ordenar por el **alias** (`ORDER BY ingreso`), pero no usarlo en un `WHERE`.

---

### Ejercicio 2.7

**Enunciado:** (reto): Reservas en las que el país del cliente (clientes.pais) NO coincide con el país de origen que figura en la reserva (reservas.pais_origen), ignorando las que no tienen pais_origen.

**Cómo pensarlo:**

1. Comparamos dos columnas de dos tablas: `clientes.pais` y `reservas.pais_origen`. «No coincide» se escribe `<>`.
2. Las que no tienen `pais_origen` (`NULL`) hay que **excluirlas** con `IS NOT NULL`.

**La consulta:**

```sql
SELECT r.id_reserva, c.pais AS pais_cliente, r.pais_origen
FROM reservas r
JOIN clientes c ON c.id_cliente = r.id_cliente
WHERE r.pais_origen IS NOT NULL AND c.pais <> r.pais_origen;
```

**Qué debe salir:**

- **5158 filas**. Columnas: id_reserva, pais_cliente, pais_origen. Ejemplo de fila: 5760, Nordicos, ES

**Ojo con:** Pensad **por qué** puede diferir (calidad del dato): lo comentáis con la pareja.

---

## Script 03 · Resumir con `GROUP BY`

Una fila por grupo. `WHERE` filtra **filas** (antes de agrupar); `HAVING` filtra **grupos** (después).

### Ejercicio 3.1

**Enunciado:** Número de reservas de cada tipo de habitación.

**Cómo pensarlo:**

1. Queremos **un número por cada tipo de habitación**. Eso es agrupar: `GROUP BY tipo_habitacion`.
2. Y para contar las reservas de cada grupo se usa `COUNT(*)`.

**La consulta:**

```sql
SELECT tipo_habitacion, COUNT(*) AS reservas
FROM reservas
GROUP BY tipo_habitacion;
```

**Qué debe salir:**

- **4 filas**. Columnas: tipo_habitacion, reservas. Ejemplo de fila: estandar, 2961

**Ojo con:** Todo lo que pongáis en el `SELECT` debe estar **en el `GROUP BY` o dentro de una función** como `COUNT`.

---

### Ejercicio 3.2

**Enunciado:** Precio medio por noche de cada tipo de habitación, redondeado a 2 decimales, del más caro al más barato.

**Cómo pensarlo:**

1. Igual que antes, pero ahora el resumen es la **media** (`AVG`) del precio.
2. `ROUND(..., 2)` deja 2 decimales. Se le da nombre (`precio_medio`) para poder **ordenar por ese nombre**.

**La consulta:**

```sql
SELECT tipo_habitacion, ROUND(AVG(precio_noche), 2) AS precio_medio
FROM reservas
GROUP BY tipo_habitacion
ORDER BY precio_medio DESC;
```

**Qué debe salir:**

- **4 filas**. Columnas: tipo_habitacion, precio_medio. Ejemplo de fila: suite, 179.2

**Ojo con:** `ORDER BY precio_medio DESC` deja primero la más cara.

---

### Ejercicio 3.3

**Enunciado:** Tasa de cancelación (en %) por tarifa y por depósito. Una fila por combinación.

**Cómo pensarlo:**

1. Hay **dos columnas** para agrupar: tarifa y depósito. Se escriben **las dos** en el `GROUP BY`, y sale una fila por cada combinación.
2. `cancelada` vale 0 o 1, así que su **media es la proporción de canceladas**. Multiplicada por 100 son % (`100.0 * AVG(cancelada)`).

**La consulta:**

```sql
SELECT tarifa, deposito, COUNT(*) AS reservas, ROUND(100.0 * AVG(cancelada), 1) AS pct_cancelacion
FROM reservas
GROUP BY tarifa, deposito
ORDER BY pct_cancelacion DESC;
```

**Qué debe salir:**

- **6 filas**. Columnas: tarifa, deposito, reservas, pct_cancelacion. Ejemplo de fila: flexible, sin_deposito, 2014, 60.2

**Ojo con:** Salen **6 filas** (6 combinaciones), no 2 ni 3. Si salen menos, os falta una columna en el `GROUP BY`.

---

### Ejercicio 3.4

**Enunciado:** Ingreso estimado total (SUM de noches * precio_noche) de las reservas NO canceladas, por isla.

**Cómo pensarlo:**

1. Necesitamos la isla (en `alojamientos`) y el ingreso (en `reservas`): hay que **unir las dos tablas**.
2. Primero filtramos las **no canceladas** (`WHERE r.cancelada = 0`) y **después** agrupamos por isla con `SUM(noches * precio_noche)`.

**La consulta:**

```sql
SELECT a.isla, ROUND(SUM(r.noches * r.precio_noche), 0) AS ingreso
FROM reservas r
JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
WHERE r.cancelada = 0
GROUP BY a.isla
ORDER BY ingreso DESC;
```

**Qué debe salir:**

- **6 filas**. Columnas: isla, ingreso. Ejemplo de fila: Tenerife, 647663

**Ojo con:** `WHERE` va **antes** del `GROUP BY`: filtra filas, no grupos.

---

### Ejercicio 3.5

**Enunciado:** Canales con más de 500 reservas y su antelación media en días (1 decimal).

**Cómo pensarlo:**

1. Se agrupa por canal y se cuenta. «Más de 500 reservas» es una condición sobre **el grupo**, no sobre cada fila, así que va en **`HAVING`**, no en `WHERE`.
2. `AVG(antelacion_dias)` con `ROUND(..., 1)` da la antelación media con un decimal.

**La consulta:**

```sql
SELECT canal, COUNT(*) AS reservas, ROUND(AVG(antelacion_dias), 1) AS antelacion_media
FROM reservas
GROUP BY canal
HAVING COUNT(*) > 500;
```

**Qué debe salir:**

- **3 filas**. Columnas: canal, reservas, antelacion_media. Ejemplo de fila: agencia, 1190, 89.4

**Ojo con:** `HAVING` va **después** del `GROUP BY`.

---

### Ejercicio 3.6

**Enunciado:** Reservas por mes de llegada en 2025 (mes en formato '2025-01'...).

**Cómo pensarlo:**

1. El mes son los **7 primeros caracteres** de la fecha (`2025-08`). `SUBSTR(fecha_llegada, 1, 7)` los extrae.
2. Se filtra el año con `LIKE '2025%'` y se agrupa por ese mes (con su nombre `mes`).
3. `ORDER BY mes` los deja en orden de enero a diciembre.

**La consulta:**

```sql
SELECT SUBSTR(fecha_llegada, 1, 7) AS mes, COUNT(*) AS llegadas
FROM reservas
WHERE fecha_llegada LIKE '2025%'
GROUP BY mes
ORDER BY mes;
```

**Qué debe salir:**

- **12 filas**. Columnas: mes, llegadas. Ejemplo de fila: 2025-01, 254

**Ojo con:** Si agrupáis por la fecha entera salen **cientos de grupos**, no 12.

---

### Ejercicio 3.7

**Enunciado:** Los 5 clientes con más reservas (id_cliente y número de reservas).

**Cómo pensarlo:**

1. Se cuentan las reservas de cada cliente (`GROUP BY id_cliente`) y se ordenan de más a menos.
2. Se recortan 5 con `LIMIT 5`.
3. Si dos clientes **empatan**, añadimos un segundo criterio (`id_cliente`) para que el resultado sea siempre el mismo.

**La consulta:**

```sql
SELECT id_cliente, COUNT(*) AS reservas
FROM reservas
GROUP BY id_cliente
ORDER BY reservas DESC, id_cliente
LIMIT 5;
```

**Qué debe salir:**

- **5 filas**. Columnas: id_cliente, reservas. Ejemplo de fila: 1549, 10

**Ojo con:** Sin el segundo criterio, el orden entre empatados **puede cambiar** de un programa a otro.

---

### Ejercicio 3.8

**Enunciado:** (reto): Por isla y categoría de alojamiento: número de reservas, tasa de cancelación (%) y precio medio por noche; solo grupos con al menos 100 reservas.

**Cómo pensarlo:**

1. Es la unión de lo anterior: `JOIN`, agrupar por **isla y categoría**, calcular tres cosas (cuántas, % de cancelación, precio medio) y filtrar grupos con `HAVING COUNT(*) >= 100`.
2. Se hace **por partes**: primero el `JOIN`, luego el `GROUP BY`, luego las tres columnas y por último el `HAVING`.

**La consulta:**

```sql
SELECT a.isla, a.categoria, COUNT(*) AS reservas,
       ROUND(100.0 * AVG(r.cancelada), 1) AS pct_cancelacion,
       ROUND(AVG(r.precio_noche), 2) AS precio_medio
FROM reservas r
JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
GROUP BY a.isla, a.categoria
HAVING COUNT(*) >= 100
ORDER BY reservas DESC;
```

**Qué debe salir:**

- **13 filas**. Columnas: isla, categoria, reservas, pct_cancelacion, precio_medio. Ejemplo de fila: Lanzarote, hotel, 1218, 44.5, 105.78

**Ojo con:** Ejecutad **cada versión parcial** para ver cómo crece el resultado.

---

## Script 04 · Una consulta dentro de otra

Subconsultas entre paréntesis y `WITH` (CTE). Consejo: **ejecutad la parte interior sola** antes de juntarla con la de fuera.

### Ejercicio 4.1

**Enunciado:** Reservas con más noches que la media de noches de todas las reservas (id_reserva y noches).

**Cómo pensarlo:**

1. Dos pasos: primero **¿cuánto es la media de noches?** y luego **¿qué reservas la superan?**.
2. El primer paso es la subconsulta `(SELECT AVG(noches) FROM reservas)`; la consulta de fuera compara cada fila con ese valor.

**La consulta:**

```sql
SELECT id_reserva, noches
FROM reservas
WHERE noches > (SELECT AVG(noches) FROM reservas);
```

**Qué debe salir:**

- **2814 filas**. Columnas: id_reserva, noches. Ejemplo de fila: 1488, 7

**Ojo con:** **Probad la subconsulta sola** primero: debe dar un único número.

---

### Ejercicio 4.2

**Enunciado:** Alojamientos con más plazas que la media (nombre, isla y plazas).

**Cómo pensarlo:**

1. Es la misma idea sobre `alojamientos`: plazas mayores que la **media de plazas**.
2. Se ordena por plazas de mayor a menor para verlos bien.

**La consulta:**

```sql
SELECT nombre, isla, plazas
FROM alojamientos
WHERE plazas > (SELECT AVG(plazas) FROM alojamientos)
ORDER BY plazas DESC;
```

**Qué debe salir:**

- **9 filas**. Columnas: nombre, isla, plazas. Ejemplo de fila: Alojamiento 20, Lanzarote, 199

**Ojo con:** La subconsulta lleva **paréntesis**.

---

### Ejercicio 4.3

**Enunciado:** Clientes que han cancelado al menos una reserva (id_cliente y país), sin repetir clientes.

**Cómo pensarlo:**

1. Primero buscamos **qué clientes aparecen en alguna reserva cancelada**: `SELECT id_cliente FROM reservas WHERE cancelada = 1` (una lista).
2. Después pedimos los clientes cuyo `id_cliente` está **`IN`** esa lista.
3. Con `IN` **no salen clientes repetidos**, aunque hayan cancelado muchas veces.

**La consulta:**

```sql
SELECT id_cliente, pais
FROM clientes
WHERE id_cliente IN (SELECT id_cliente FROM reservas WHERE cancelada = 1);
```

**Qué debe salir:**

- **1660 filas**. Columnas: id_cliente, pais. Ejemplo de fila: 1, ES

**Ojo con:** Si hicierais un `JOIN`, cada cliente saldría **tantas veces como reservas canceladas** tenga.

---

### Ejercicio 4.4

**Enunciado:** Clientes que NO tienen ninguna reserva, ahora con NOT IN (compara con el ejercicio 2.5).

**Cómo pensarlo:**

1. Es lo mismo que el 2.5 pero con otro método: clientes cuyo `id_cliente` **NO está** (`NOT IN`) en la lista de clientes que aparecen en `reservas`.
2. Aquí se pide solo el **número** (con `COUNT(*)`) para compararlo con el 2.5.

**La consulta:**

```sql
SELECT COUNT(*)
FROM clientes
WHERE id_cliente NOT IN (SELECT id_cliente FROM reservas);
```

**Qué debe salir:**

- **un solo valor: 212**

**Ojo con:** **Tiene que dar lo mismo que 2.5** (212). Aviso: si la subconsulta devolviera algún `NULL`, `NOT IN` no devolvería nada; aquí no hay `NULL`.

---

### Ejercicio 4.5

**Enunciado:** La reserva (o reservas) con el mayor ingreso estimado (noches * precio_noche): id_reserva e ingreso.

**Cómo pensarlo:**

1. Dos pasos: **¿cuál es el ingreso máximo?** (`MAX(noches * precio_noche)`) y **¿qué reserva(s) lo tienen?**.
2. Si hay empate, salen todas.

**La consulta:**

```sql
SELECT id_reserva, noches * precio_noche AS ingreso
FROM reservas
WHERE noches * precio_noche = (SELECT MAX(noches * precio_noche) FROM reservas);
```

**Qué debe salir:**

- **1 fila**. Columnas: id_reserva, ingreso. Ejemplo de fila: 3971, 2667.21

**Ojo con:** Sirve también para ver si hay **más de una** con el máximo. Es más seguro que `LIMIT 1`.

---

### Ejercicio 4.6

**Enunciado:** Canales cuya tasa de cancelación supera la tasa global (nombre del canal y %). Resuélvelo con una CTE.

**Cómo pensarlo:**

1. Paso 1: una **CTE** con la tasa de cancelación de cada canal: `WITH por_canal AS (...)`. Es darle un nombre a un resultado intermedio.
2. Paso 2: otra subconsulta con la **tasa global** (`SELECT AVG(cancelada) FROM reservas`).
3. Paso 3: nos quedamos con los canales cuya tasa **supera** la global.

**La consulta:**

```sql
WITH por_canal AS (
    SELECT canal, COUNT(*) AS reservas, AVG(cancelada) AS tasa
    FROM reservas
    GROUP BY canal
)
SELECT canal, reservas, ROUND(100 * tasa, 1) AS pct_cancelacion
FROM por_canal
WHERE tasa > (SELECT AVG(cancelada) FROM reservas)
ORDER BY tasa DESC;
```

**Qué debe salir:**

- **1 fila**. Columnas: canal, reservas, pct_cancelacion. Ejemplo de fila: web_intermediaria, 3020, 53.9

**Ojo con:** La CTE va **al principio** de la consulta, antes del `SELECT` final.

---

### Ejercicio 4.7

**Enunciado:** Alojamientos cuyo precio medio por noche está por encima del precio medio global (nombre y precio medio).

**Cómo pensarlo:**

1. Paso 1: una CTE con el **precio medio de cada alojamiento** (en `reservas`).
2. Paso 2: se une con `alojamientos` para tener el nombre.
3. Paso 3: se filtran los que superan **el precio medio global** (otra subconsulta).

**La consulta:**

```sql
WITH medias AS (
    SELECT id_alojamiento, AVG(precio_noche) AS precio_medio
    FROM reservas
    GROUP BY id_alojamiento
)
SELECT a.nombre, ROUND(m.precio_medio, 2) AS precio_medio
FROM medias m
JOIN alojamientos a ON a.id_alojamiento = m.id_alojamiento
WHERE m.precio_medio > (SELECT AVG(precio_noche) FROM reservas)
ORDER BY m.precio_medio DESC;
```

**Qué debe salir:**

- **6 filas**. Columnas: nombre, precio_medio. Ejemplo de fila: Alojamiento 18, 110.72

**Ojo con:** Si salen 20 alojamientos, el filtro no está funcionando.

---

### Ejercicio 4.8

**Enunciado:** (reto): Clientes repetidores "de riesgo": con 4 o más reservas y al menos el 75 % de ellas canceladas (id_cliente, reservas, % canceladas).

**Cómo pensarlo:**

1. Primero una CTE con, **por cliente**, cuántas reservas tiene y qué fracción cancela (`AVG(cancelada)`).
2. Después se filtran los clientes con **4 o más** reservas (`reservas >= 4`) y **al menos el 75 %** canceladas (`tasa >= 0.75`).
3. `ORDER BY` con tres criterios deja el resultado estable.

**La consulta:**

```sql
WITH por_cliente AS (
    SELECT id_cliente, COUNT(*) AS reservas, AVG(cancelada) AS tasa
    FROM reservas
    GROUP BY id_cliente
)
SELECT id_cliente, reservas, ROUND(100 * tasa, 1) AS pct_canceladas
FROM por_cliente
WHERE reservas >= 4 AND tasa >= 0.75
ORDER BY tasa DESC, reservas DESC, id_cliente;
```

**Qué debe salir:**

- **103 filas**. Columnas: id_cliente, reservas, pct_canceladas. Ejemplo de fila: 1868, 6, 100

**Ojo con:** 75 % se escribe **0.75** (con punto).

---

## Script 05 · Crear, modificar y borrar (CRUD)

**Importante: el orden importa.** Estos ejercicios trabajan sobre la copia `reservas_practica` y cada uno depende del anterior (el 5.4 comprueba lo que hizo el 5.3). Si os perdéis, ejecutad otra vez la **PREPARACIÓN** del principio del script 05 y repetid desde el 5.1. Los cambios no se guardan en el archivo hasta pulsar «Escribir cambios» (Ctrl+S); si algo sale mal, «Revertir cambios».

### Ejercicio 5.1

**Enunciado:** Inserta una reserva nueva (id_reserva 900002) del cliente 2 en el alojamiento 3, llegada '2025-11-15', 4 noches, canal 'web_intermediaria', tarifa 'no_reembolsable', precio 88.5, no cancelada.

**Cómo pensarlo:**

1. `INSERT INTO tabla (columnas...) VALUES (valores...)`. **Nombrad siempre las columnas** y poned los valores **en el mismo orden**.
2. Los textos van entre comillas simples; los números, sin comillas. `cancelada = 0` es «no cancelada».

**La consulta:**

```sql
INSERT INTO reservas_practica (id_reserva, id_cliente, id_alojamiento, fecha_llegada, noches, canal, tarifa, precio_noche, cancelada)
VALUES (900002, 2, 3, '2025-11-15', 4, 'web_intermediaria', 'no_reembolsable', 88.5, 0);
```

**Qué debe salir:**

- se inserta 1 fila (DB Browser dice «1 fila afectada»)

**Ojo con:** Si el número de columnas y de valores no coincide, da error.

---

### Ejercicio 5.2

**Enunciado:** Comprueba con un SELECT que la reserva 900002 existe y tiene 4 noches.

**Cómo pensarlo:**

1. Siempre **se comprueba** lo que se ha cambiado: un `SELECT` con `WHERE id_reserva = 900002`.

**La consulta:**

```sql
SELECT id_reserva, noches, precio_noche FROM reservas_practica WHERE id_reserva = 900002;
```

**Qué debe salir:**

- **1 fila**. Columnas: id_reserva, noches, precio_noche. Ejemplo de fila: 900002, 4, 88.5

**Ojo con:** Si no sale nada, el `INSERT` no se ejecutó: mirad si lo seleccionasteis y pulsasteis **Ctrl+Intro**.

---

### Ejercicio 5.3

**Enunciado:** El alojamiento 3 sube un 10 % los precios de las reservas con llegada posterior a '2025-11-01'. Primero haz el SELECT de las filas afectadas y después el UPDATE (precio_noche = precio_noche * 1.10).

**Cómo pensarlo:**

1. **Regla de oro:** antes del `UPDATE`, un `SELECT` con **el mismo `WHERE`** para ver qué filas se van a tocar.
2. Después, el `UPDATE` con ese mismo `WHERE`: `SET precio_noche = ROUND(precio_noche * 1.10, 2)`.

**La consulta:**

```sql
SELECT id_reserva, precio_noche FROM reservas_practica WHERE id_alojamiento = 3 AND fecha_llegada > '2025-11-01';
UPDATE reservas_practica SET precio_noche = ROUND(precio_noche * 1.10, 2)
WHERE id_alojamiento = 3 AND fecha_llegada > '2025-11-01';
```

**Qué debe salir:**

- Orden 1: **22 filas**. Columnas: id_reserva, precio_noche. Ejemplo de fila: 5129, 211.95
- Orden 2: **22 filas** afectadas (update)

**Ojo con:** Si el `UPDATE` no lleva `WHERE`, **cambia todas las filas**. Con el `SELECT` previo lo habríais visto.

---

### Ejercicio 5.4

**Enunciado:** Comprueba que el precio de la reserva 900002 es ahora 97.35.

**Cómo pensarlo:**

1. Se comprueba con un `SELECT`: 88,5 × 1,10 = 97,35.

**La consulta:**

```sql
SELECT precio_noche FROM reservas_practica WHERE id_reserva = 900002;
```

**Qué debe salir:**

- **un solo valor: 97.35**

**Ojo con:** Si no sale 97.35, ejecutasteis el `UPDATE` dos veces (sale un precio mayor) o con otro `WHERE`. Para reiniciar, volved a ejecutar la **PREPARACIÓN** del script 05 y repetid desde el 5.1.

---

### Ejercicio 5.5

**Enunciado:** Marca como canceladas (cancelada = 1) las reservas de la copia con canal 'empresa' y tarifa 'flexible' cuya llegada sea en diciembre de 2025.

**Cómo pensarlo:**

1. Primero **se cuenta** cuántas filas cumplen las tres condiciones (`SELECT COUNT(*)`).
2. Si el número tiene sentido, el mismo `WHERE` en el `UPDATE ... SET cancelada = 1`.
3. `LIKE '2025-12%'` coge cualquier día de diciembre de 2025.

**La consulta:**

```sql
SELECT COUNT(*) FROM reservas_practica WHERE canal = 'empresa' AND tarifa = 'flexible' AND fecha_llegada LIKE '2025-12%';
UPDATE reservas_practica SET cancelada = 1
WHERE canal = 'empresa' AND tarifa = 'flexible' AND fecha_llegada LIKE '2025-12%';
```

**Qué debe salir:**

- Orden 1: **un solo valor: 4**
- Orden 2: **4 filas** afectadas (update)

**Ojo con:** Anotad el número **antes** de ejecutar el `UPDATE`.

---

### Ejercicio 5.6

**Enunciado:** Borra de la copia las reservas con noches = 1 y canceladas (cancelada = 1). Cuenta antes cuántas son.

**Cómo pensarlo:**

1. Primero **se cuenta**; después, el `DELETE` con el **mismo `WHERE`**.

**La consulta:**

```sql
SELECT COUNT(*) FROM reservas_practica WHERE noches = 1 AND cancelada = 1;
DELETE FROM reservas_practica WHERE noches = 1 AND cancelada = 1;
```

**Qué debe salir:**

- Orden 1: **un solo valor: 15**
- Orden 2: **15 filas** afectadas (delete)

**Ojo con:** `DELETE` **sin `WHERE` borra toda la tabla**.

---

### Ejercicio 5.7

**Enunciado:** Comprueba que ya no queda ninguna reserva de 1 noche cancelada (debe salir 0).

**Cómo pensarlo:**

1. El mismo `COUNT(*)` del 5.6, que ahora debe dar **0**.

**La consulta:**

```sql
SELECT COUNT(*) FROM reservas_practica WHERE noches = 1 AND cancelada = 1;
```

**Qué debe salir:**

- **un solo valor: 0**

**Ojo con:** Si no da 0, el `DELETE` no se ejecutó bien.

---

### Ejercicio 5.8

**Enunciado:** Con una transacción: empieza (BEGIN), borra TODAS las reservas de la copia, comprueba que la tabla queda vacía y deshaz con ROLLBACK. Comprueba después que las filas han vuelto.

**Cómo pensarlo:**

1. Una **transacción** agrupa varias órdenes para poder **deshacerlas** juntas.
2. `BEGIN;` abre la transacción. Después el `DELETE` sin `WHERE` (aquí es a propósito) y un `COUNT(*)` que dará 0.
3. `ROLLBACK;` **deshace** todo. Un último `COUNT(*)` comprueba que **las filas han vuelto**.

**La consulta:**

```sql
BEGIN;
DELETE FROM reservas_practica;
SELECT COUNT(*) FROM reservas_practica;
ROLLBACK;
SELECT COUNT(*) FROM reservas_practica;
```

**Qué debe salir:**

- Orden 1: no muestra datos; solo la orden se ejecuta sin error
- Orden 2: **2963 filas** afectadas (delete)
- Orden 3: **un solo valor: 0**
- Orden 4: no muestra datos; solo la orden se ejecuta sin error
- Orden 5: **un solo valor: 2963**

**Ojo con:** Ejecutad **las cinco órdenes una a una**, en orden. Si ejecutáis `COMMIT` en vez de `ROLLBACK`, el borrado **sí queda hecho**. La cifra de filas (2963) depende de que los ejercicios 5.1–5.7 estén bien hechos: lo importante es que la última cifra sea **igual** a la que había antes del `DELETE`.

---

### Ejercicio 5.9

**Enunciado:** (reto): Sin usar la tabla original, ¿cuántas reservas tiene cada canal en la copia tras tus cambios? Escríbelo con GROUP BY y verifica que la suma coincide con COUNT(*).

**Cómo pensarlo:**

1. Se agrupa por canal y se cuenta, solo sobre la **copia** (`reservas_practica`).
2. Para verificar, se suman los 4 resultados y se compara con `SELECT COUNT(*) FROM reservas_practica`.

**La consulta:**

```sql
SELECT canal, COUNT(*) AS reservas FROM reservas_practica GROUP BY canal;
```

**Qué debe salir:**

- **4 filas**. Columnas: canal, reservas. Ejemplo de fila: agencia, 584

**Ojo con:** La suma de los grupos **tiene que dar el total de la copia**. Si no, algo falla en el `GROUP BY`.

---

## Script 06 · Diseñar tablas con reglas e índices

**Importante: el orden importa.** Se usan las tablas de práctica `p_*` que crea el principio del script 06. Los ejercicios **6.2, 6.3 y 6.5 deben dar error**: ese error es la respuesta correcta. Ejecutad cada uno **solo**, seleccionando la sentencia, porque si ejecutáis todo de golpe el script se detiene en el primer error.

### Ejercicio 6.1

**Enunciado:** Inserta en p_reservas la reserva 3 de 'DE', 5 noches, 70.0 € por noche y comprueba con un SELECT que hay 2 filas en total.

**Cómo pensarlo:**

1. Un `INSERT` con las columnas y los valores del enunciado, y un `SELECT COUNT(*)` para comprobar que hay 2 filas (la 1 de antes y la nueva).

**La consulta:**

```sql
INSERT INTO p_reservas (id_reserva, pais, noches, precio_noche) VALUES (3, 'DE', 5, 70.0);
SELECT COUNT(*) FROM p_reservas;
```

**Qué debe salir:**

- Orden 1: se inserta 1 fila (DB Browser dice «1 fila afectada»)
- Orden 2: **un solo valor: 2**

**Ojo con:** Si da error `UNIQUE`, esa reserva ya estaba: no la insertéis dos veces.

---

### Ejercicio 6.2

**Enunciado:** Intenta insertar una reserva con 0 noches (id 4, país 'ES', 60.0 €). ¿Qué error da y por qué es bueno que falle?

**Cómo pensarlo:**

1. Aquí **el error es la respuesta correcta**. La tabla tiene la regla `CHECK (noches >= 1)`, así que **rechaza** una reserva de 0 noches.
2. Ejecutad **solo esta sentencia** y leed el mensaje.

**La consulta:**

```sql
INSERT INTO p_reservas (id_reserva, pais, noches, precio_noche) VALUES (4, 'ES', 0, 60.0);
```

**Qué debe salir:**

- **error** → `CHECK constraint failed: noches >= 1`

**Ojo con:** Por qué es bueno que falle: la base **impide guardar datos imposibles**, aunque se equivoque quien escribe.

---

### Ejercicio 6.3

**Enunciado:** Intenta insertar otra reserva con id_reserva = 1. ¿Qué regla lo impide?

**Cómo pensarlo:**

1. Otra vez **debe fallar**. `id_reserva` es la **clave primaria** y **no se puede repetir**: ya existe una reserva con id 1.

**La consulta:**

```sql
INSERT INTO p_reservas (id_reserva, pais, noches, precio_noche) VALUES (1, 'ES', 2, 60.0);
```

**Qué debe salir:**

- **error** → `UNIQUE constraint failed: p_reservas.id_reserva`

**Ojo con:** El mensaje dice `UNIQUE constraint failed`: significa «repetido».

---

### Ejercicio 6.4

**Enunciado:** Diseña una tabla p_valoraciones: id_valoracion (clave primaria), id_reserva (clave foránea a p_reservas, obligatoria), puntuacion (entero de 1 a 5, obligatoria), comentario (texto opcional). Inserta una valoración de 5 puntos para la reserva 1.

**Cómo pensarlo:**

1. Se diseña la tabla pieza a pieza: `id_valoracion` es la **clave primaria**; `id_reserva` es una **clave foránea** (`REFERENCES p_reservas(id_reserva)`) y obligatoria (`NOT NULL`); `puntuacion` lleva `CHECK (puntuacion BETWEEN 1 AND 5)`; `comentario` es texto opcional (sin `NOT NULL`).
2. Después, un `INSERT` de una valoración de 5 puntos para la reserva 1.

**La consulta:**

```sql
DROP TABLE IF EXISTS p_valoraciones;
CREATE TABLE p_valoraciones (
    id_valoracion INTEGER PRIMARY KEY,
    id_reserva    INTEGER NOT NULL REFERENCES p_reservas(id_reserva),
    puntuacion    INTEGER NOT NULL CHECK (puntuacion BETWEEN 1 AND 5),
    comentario    TEXT
);
INSERT INTO p_valoraciones (id_valoracion, id_reserva, puntuacion, comentario) VALUES (1, 1, 5, 'Todo perfecto');
```

**Qué debe salir:**

- Orden 1: no muestra datos; debe ejecutarse sin error
- Orden 2: no muestra datos; debe ejecutarse sin error
- Orden 3: se inserta 1 fila (DB Browser dice «1 fila afectada»)

**Ojo con:** Si la tabla ya existe, primero `DROP TABLE IF EXISTS p_valoraciones;`.

---

### Ejercicio 6.5

**Enunciado:** Comprueba que tu tabla rechaza una puntuación 7 y una valoración de una reserva inexistente (99). Dos sentencias que deben fallar; ejecútalas por separado.

**Cómo pensarlo:**

1. **Las dos sentencias deben fallar**, cada una por una regla distinta: puntuación 7 (`CHECK`) y reserva 99 que no existe (clave foránea).
2. Ejecutadlas **por separado** y apuntad qué mensaje da cada una.

**La consulta:**

```sql
INSERT INTO p_valoraciones (id_valoracion, id_reserva, puntuacion) VALUES (2, 1, 7);
INSERT INTO p_valoraciones (id_valoracion, id_reserva, puntuacion) VALUES (3, 99, 4);
```

**Qué debe salir:**

- Orden 1: **error** → `CHECK constraint failed: puntuacion BETWEEN 1 AND 5`
- Orden 2: **error** → `FOREIGN KEY constraint failed`

**Ojo con:** Para que la clave foránea funcione hace falta `PRAGMA foreign_keys = ON;` (el script ya lo ejecuta).

---

### Ejercicio 6.6

**Enunciado:** Une p_valoraciones con p_reservas y p_paises para mostrar id_valoracion, puntuacion y nombre del país.

**Cómo pensarlo:**

1. Se parte de `p_valoraciones` y se unen **dos tablas en cadena**: con `p_reservas` por `id_reserva`, y con `p_paises` por el código del país.
2. Se muestra el **nombre** del país, no el código.

**La consulta:**

```sql
SELECT v.id_valoracion, v.puntuacion, p.nombre AS pais
FROM p_valoraciones v
JOIN p_reservas r ON r.id_reserva = v.id_reserva
JOIN p_paises p ON p.codigo = r.pais;
```

**Qué debe salir:**

- **1 fila**. Columnas: id_valoracion, puntuacion, pais. Ejemplo de fila: 1, 5, Reino Unido

**Ojo con:** Cada `JOIN` tiene **su propio `ON`**.

---

### Ejercicio 6.7

**Enunciado:** Crea un índice sobre reservas(canal, cancelada) llamado idx_p_canal_cancelada y comprueba con EXPLAIN QUERY PLAN que la consulta SELECT canal, AVG(cancelada) FROM reservas WHERE canal = 'directo' lo utiliza.

**Cómo pensarlo:**

1. `CREATE INDEX nombre ON tabla (columna1, columna2)` crea el índice.
2. `EXPLAIN QUERY PLAN` delante de una consulta **no la ejecuta**: muestra cómo la resolvería SQLite. Buscamos la palabra **`INDEX`** (por ejemplo `SEARCH ... USING COVERING INDEX`) en lugar de `SCAN`.

**La consulta:**

```sql
CREATE INDEX IF NOT EXISTS idx_p_canal_cancelada ON reservas (canal, cancelada);
EXPLAIN QUERY PLAN SELECT canal, AVG(cancelada) FROM reservas WHERE canal = 'directo';
```

**Qué debe salir:**

- Orden 1: no muestra datos; debe ejecutarse sin error
- Orden 2: una fila con el plan; debe incluir la palabra `INDEX`: `SEARCH reservas USING COVERING INDEX idx_p_canal_cancelada (canal=?)`

**Ojo con:** `SCAN` = recorre toda la tabla; `SEARCH ... USING INDEX` = usa el índice (mucho más rápido).

---

### Ejercicio 6.8

**Enunciado:** (reto de diseño, sobre papel): TurisData quiere guardar las experiencias contratadas en cada reserva (excursión, alquiler de coche...). Una reserva puede tener varias experiencias y una experiencia aparece en muchas reservas. Dibuja las tablas y las claves. ¿Qué tipo de relación es y qué tabla intermedia hace falta?

**Cómo pensarlo:**

1. Una reserva puede tener **muchas** experiencias y una experiencia puede estar en **muchas** reservas: es una relación **de muchos a muchos (N:M)**.
2. No se puede guardar con una sola tabla. Hace falta una **tabla intermedia** con **dos claves foráneas**: `id_reserva` e `id_experiencia`.
3. Su **clave primaria** es la **pareja** de las dos, para que la misma experiencia no se repita en la misma reserva. Además puede llevar `unidades` (cuántas se contratan).

**La consulta:**

```sql
-- Respuesta: relación N:M. Tablas: experiencias(id_experiencia PK, nombre, precio),
-- reservas(id_reserva PK, ...), reserva_experiencia(id_reserva FK, id_experiencia FK,
-- unidades, PRIMARY KEY (id_reserva, id_experiencia)). Se implementa así:
DROP TABLE IF EXISTS p_experiencias;
DROP TABLE IF EXISTS p_reserva_experiencia;
CREATE TABLE p_experiencias (id_experiencia INTEGER PRIMARY KEY, nombre TEXT NOT NULL, precio REAL CHECK (precio >= 0));
CREATE TABLE p_reserva_experiencia (
    id_reserva INTEGER NOT NULL REFERENCES p_reservas(id_reserva),
    id_experiencia INTEGER NOT NULL REFERENCES p_experiencias(id_experiencia),
    unidades INTEGER NOT NULL DEFAULT 1 CHECK (unidades >= 1),
    PRIMARY KEY (id_reserva, id_experiencia)
);
```

**Qué debe salir:**

- Orden 1: no muestra datos; debe ejecutarse sin error
- Orden 2: no muestra datos; debe ejecutarse sin error
- Orden 3: no muestra datos; debe ejecutarse sin error
- Orden 4: no muestra datos; debe ejecutarse sin error

**Ojo con:** Es un reto **de diseño**: primero dibujad en papel las tablas y las flechas, y después escribid el `CREATE TABLE`. Hay más de una solución válida.

---

## Para terminar

- ¿Os han salido todos? Estupendo, pero **lo importante no es el SQL de memoria**: es saber **qué pregunta** hace cada consulta y **dónde mirar** cuando el resultado no cuadra.
- Antes de dar por buena una consulta, haced siempre la **comprobación del paso 5** de la guía: ¿cuántas filas?, ¿tiene sentido?, ¿hay `NULL` o repetidos?
- Para entregar el trabajo, **explicad con vuestras palabras** al menos 3 consultas y anotad **de dónde** habéis sacado cada una (apuntes, guía, compañero, IA). Eso se valora más que el resultado.
