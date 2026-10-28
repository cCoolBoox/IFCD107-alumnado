# Solucionario NoSQL paso a paso · S03 (cuaderno `S03_01_nosql_mongomock`)

> **Para quién:** alumnado de IFCD107. **Qué es:** las soluciones de los 7 ejercicios y del mini-reto del cuaderno de NoSQL, explicadas **paso a paso**, con **lo que debe salir** y los errores más típicos. Va con la [guía en parejas](guia_nosql_en_parejas.md) y el [listado de ejercicios](listado_ejercicios_nosql.md).

## Cómo usar este solucionario

1. **Primero intentadlo vosotros** (en pareja, con el ciclo de 6 pasos de la guía). Si miráis la solución antes, no aprendéis a escribir filtros, solo a copiarlos.
2. Cuando la celda os diga **«Correcto»**, mirad **«Qué debe salir»**: ¿coincide la cifra?
3. Si no coincide, leed **«Cómo pensarlo»** y buscad en qué paso se separa vuestro código del nuestro.
4. Por último, comparad con **el código**. Puede haber **más de una forma correcta**: si la vuestra pasa el `assert`, también vale.
5. Anotad en la hoja de registro (apartado 8 de la guía) qué os ha costado.

**Los datos:** el cuaderno construye **6.000 documentos** (una reserva cada uno) a partir de `turisdata.db`. Cada documento lleva dentro un subdocumento `alojamiento` (con `nombre`, `isla`, `categoria`, `plazas`) y otro `cliente` (con `pais`). Son datos **sintéticos**.

**Importante:** los ejercicios 1 a 5 se hacen **en orden**. El ejercicio 5 **borra** documentos; antes de las agregaciones, el propio cuaderno **vuelve a cargar** los 6.000.

---

## Ejercicio 1 · Contar documentos

**Enunciado:** guarda en `n_canceladas` cuántas reservas tienen `cancelada` igual a `True`.

**Cómo pensarlo:**

1. Piden **un número**: cuántos documentos cumplen una condición. Para contar se usa `count_documents(filtro)`.
2. El filtro es un **diccionario**: `{"cancelada": True}` (campo y valor).
3. Se guarda el resultado en la variable que pide el enunciado.

**El código:**

```python
n_canceladas = reservas.count_documents({"cancelada": True})
```

**Qué debe salir:** `Correcto: 2754 reservas canceladas`. Es la misma cifra que en SQL (`cancelada = 1`).

**Ojo con:** `True` lleva **mayúscula inicial**. Con `true` Python da `NameError`.

---

## Ejercicio 2 · Filtrar

**Enunciado:** guarda en `caras_tenerife` la lista de reservas de alojamientos de **Tenerife** con `precio_noche` mayor que 150.

**Cómo pensarlo:**

1. Hay **dos condiciones a la vez** (Tenerife **y** más de 150 €). En un diccionario, dos campos separados por coma son un **Y**.
2. La isla no está en la reserva, sino **dentro del subdocumento** `alojamiento`. Se escribe con **punto**: `"alojamiento.isla"`.
3. «Mayor que» es `$gt`: `{"precio_noche": {"$gt": 150}}`.
4. `find` devuelve un **cursor**; el enunciado pide una **lista**, así que se envuelve con `list(...)`.

**El código:**

```python
caras_tenerife = list(reservas.find({"alojamiento.isla": "Tenerife", "precio_noche": {"$gt": 150}}))
```

**Qué debe salir:** `Correcto: 194 reservas`.

**Ojo con:** sin `list(...)` el `assert` dice «Envuelve el cursor con list(...)». Y sin el `$` de `$gt` no filtra bien.

---

## Ejercicio 3 · Operadores lógicos

**Enunciado:** guarda en `n_riesgo` cuántas reservas son de canal `web_intermediaria` **o** de tarifa `flexible`, y además tienen `deposito` igual a `"sin_deposito"`.

**Cómo pensarlo:**

1. Hay un **O** (canal web **o** tarifa flexible) y un **Y** (y además sin depósito).
2. Para el **O** se usa `$or` con una **lista** de dos filtros: `{"$or": [{...}, {...}]}`.
3. El **Y** con el depósito se pone **en el mismo diccionario**, al lado del `$or`.
4. Como solo piden **cuántas**, se cuenta con `count_documents`.

**El código:**

```python
n_riesgo = reservas.count_documents({
    "$or": [{"canal": "web_intermediaria"}, {"tarifa": "flexible"}],
    "deposito": "sin_deposito",
})
```

**Qué debe salir:** `Correcto: 2682`.

**Ojo con:** si ponéis el depósito **dentro** del `$or`, cuenta otra cosa (sale una cifra mayor). La condición del depósito **tiene que ir fuera**.

---

## Ejercicio 4 · Actualizar

**Enunciado:** sube 5 euros el `precio_noche` de la reserva con `_id` igual a 5760 usando `$inc`. Guarda el nuevo precio leído de la base en `precio_nuevo`.

**Cómo pensarlo:**

1. Hay que cambiar **un solo documento**: `update_one(filtro, cambio)`. El filtro es `{"_id": 5760}`.
2. El cambio **suma** a un número, así que se usa `$inc`: `{"$inc": {"precio_noche": 5}}`.
3. Después se **lee** el documento (`find_one`) para comprobar qué hay ahora **en la base**, no lo que creéis que hay.

**El código:**

```python
reservas.update_one({"_id": 5760}, {"$inc": {"precio_noche": 5}})
precio_nuevo = reservas.find_one({"_id": 5760})["precio_noche"]
```

**Qué debe salir:** `Correcto: 94.24` (era 89.24).

**Ojo con:** si ejecutáis la celda **dos veces**, el precio sube 10 (sale 99.24) y el `assert` falla. Para repetir, volved a ejecutar la celda que carga los 6.000 documentos.

---

## Ejercicio 5 · Borrar con cuidado

**Enunciado:** guarda en `a_borrar` cuántas reservas hay con `noches` igual a 1 y `cancelada` `True`; después bórralas con `delete_many` y guarda en `quedan` cuántas quedan con ese mismo filtro (debe ser 0).

**Cómo pensarlo:**

1. **Regla de oro** (la misma que en SQL): **primero se cuenta, después se borra, con el mismo filtro**.
2. Para no equivocarse, se guarda el filtro **en una variable** y se usa tres veces: contar, borrar y volver a contar.
3. El último recuento debe dar **0**.

**El código:**

```python
filtro = {"noches": 1, "cancelada": True}
a_borrar = reservas.count_documents(filtro)
reservas.delete_many(filtro)
quedan = reservas.count_documents(filtro)
```

**Qué debe salir:** `Correcto: borradas 34 reservas`. Quedan 5.966 documentos en la colección.

**Ojo con:** `delete_many({})` **sin filtro borra los 6.000**. Si os pasa, ejecutad de nuevo la celda que carga los documentos. Si ejecutáis el borrado **dos veces**, la segunda no encuentra nada y el `assert` («Antes de borrar tenía que haber alguna reserva») falla.

---

## Ejercicio 6 · Tasa de cancelación por canal (en casa)

**Enunciado:** crea la lista `tasa_canal` con la pipeline que agrupa por `canal` y calcula el número de reservas y el número de canceladas.

**Cómo pensarlo:**

1. Es el **`GROUP BY`** de MongoDB: una etapa `$group` cuyo **`_id`** es el campo por el que agrupamos: `"$canal"` (con `$`).
2. Dentro del `$group` hay **dos cálculos**: el número de reservas (`{"$sum": 1}`, suma 1 por cada documento) y el de canceladas.
3. Para contar solo las canceladas se suma **1 si es cancelada y 0 si no**: `{"$sum": {"$cond": ["$cancelada", 1, 0]}}`.
4. El porcentaje lo calcula el propio cuaderno con pandas.

**El código:**

```python
tasa_canal = list(reservas.aggregate([
    {"$group": {"_id": "$canal",
                "reservas": {"$sum": 1},
                "canceladas": {"$sum": {"$cond": ["$cancelada", 1, 0]}}}},
]))
```

**Qué debe salir:** una fila por canal (**4**) y la suma de reservas igual a **6000**:

| canal | reservas | canceladas | % cancelación |
|---|---|---|---|
| web_intermediaria | 3020 | 1628 | 53.9 |
| agencia | 1190 | 524 | 44.0 |
| empresa | 328 | 142 | 43.3 |
| directo | 1462 | 460 | 31.5 |

**Ojo con:** el campo dentro de `$group` lleva `$` delante (`"$canal"`); el `_id` **sin** `$` sería el texto «canal». Y el orden de las filas puede variar: lo importante son las cifras.

---

## Ejercicio 7 · Ingreso por isla, con subdocumentos (en casa)

**Enunciado:** calcula en `ingreso_isla` el ingreso estimado (`noches * precio_noche`) de las reservas **no canceladas**, agrupado por `alojamiento.isla`.

**Cómo pensarlo:**

1. **Primero se filtra** (`$match`, el `WHERE`): `{"cancelada": False}`.
2. **Después se agrupa** (`$group`) por la isla del subdocumento: `"$alojamiento.isla"`.
3. El ingreso de cada reserva se **calcula** multiplicando dos campos con `{"$multiply": ["$noches", "$precio_noche"]}`, y se **suma** por grupo con `$sum`.
4. `$sort` por el ingreso, de mayor a menor (`-1`), para ver primero la isla que más ingresa.

**El código:**

```python
ingreso_isla = list(reservas.aggregate([
    {"$match": {"cancelada": False}},
    {"$group": {"_id": "$alojamiento.isla",
                "ingreso": {"$sum": {"$multiply": ["$noches", "$precio_noche"]}}}},
    {"$sort": {"ingreso": -1}},
]))
```

**Qué debe salir:** **6 filas**, una por isla. Debe coincidir con el ejercicio 3.4 de SQL:

| isla | ingreso (€) |
|---|---|
| Tenerife | 647663 |
| Lanzarote | 504308 |
| Fuerteventura | 271672 |
| La Gomera | 182485 |
| Gran Canaria | 170764 |
| La Palma | 92935 |

**Ojo con:** el orden de las etapas: si agrupáis **antes** de filtrar, contáis también las canceladas.

---

## Mini-reto · La misma pregunta en SQL y en MongoDB (en casa)

**Enunciado:** ¿cuál es la tasa de cancelación (%) de cada isla? Escribe la consulta SQL (`tasa_sql`), la pipeline de MongoDB (`tasa_mongo`) y comprueba que coinciden.

**Cómo pensarlo:**

1. **En SQL:** une `reservas` con `alojamientos` (`JOIN`), agrupa por isla (`GROUP BY`) y calcula la media de `cancelada` (que vale 0 o 1, así que su media es la proporción). Se multiplica por 100 y se redondea a **1 decimal**. `dict(...)` convierte las filas en `{isla: %}`.
2. **En MongoDB:** agrupa por `"$alojamiento.isla"` y calcula la media (`$avg`) de la condición `{"$cond": ["$cancelada", 1, 0]}`. Después, en Python, se multiplica por 100 y se redondea a **1 decimal**, igual que en SQL.
3. **Comprobad:** si los dos diccionarios son iguales, habéis respondido **lo mismo** con dos formas de guardar los datos.

**El código:**

```python
tasa_sql = dict(con.execute("""
    SELECT a.isla, ROUND(100.0 * AVG(r.cancelada), 1)
    FROM reservas r JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
    GROUP BY a.isla""").fetchall())

tasa_mongo = {
    fila["_id"]: round(100 * fila["media"], 1)
    for fila in reservas.aggregate([
        {"$group": {"_id": "$alojamiento.isla",
                    "media": {"$avg": {"$cond": ["$cancelada", 1, 0]}}}}
    ])
}
```

**Qué debe salir:** `¡Coinciden!` con este diccionario:

| isla | % cancelación |
|---|---|
| Fuerteventura | 45.6 |
| Gran Canaria | 46.5 |
| La Gomera | 46.7 |
| La Palma | 46.0 |
| Lanzarote | 45.3 |
| Tenerife | 46.0 |

**Ojo con:** si **no** recargasteis la colección tras el ejercicio 5, faltan 34 reservas y las cifras de MongoDB serán **ligeramente distintas** de las de SQL. El cuaderno ya la recarga en la sección 5; si ejecutáis celdas sueltas, volved a ejecutarla.

---

## Para reflexionar · ideas de respuesta

Son **orientativas**: con vuestras palabras y con ejemplos de TurisData valen más.

1. **Ventaja y problema de embeber el alojamiento en la reserva.** *Ventaja:* una sola lectura trae todo lo necesario (sin `JOIN`), cómodo para una ficha en una app móvil. *Problema:* el dato del alojamiento **se repite** en miles de reservas; si cambia de nombre hay que actualizarlo **en todas** y es fácil que queden versiones distintas.
2. **Cuándo MongoDB y cuándo SQL.** *MongoDB:* datos con **forma variable** o que se leen juntos: reseñas, registros de navegación, catálogo de experiencias con atributos distintos. *SQL:* datos con **reglas estrictas** y relaciones claras, como las facturas, donde importan la integridad y las transacciones.
3. **Pasar de `mongomock` a un servidor real.** Usuarios y contraseñas, **copias de seguridad**, **índices** para que las consultas sean rápidas, **coste** del servicio y de las copias, y **seguridad** (no subir la cadena de conexión a un repositorio).

---

## Para terminar

- ¿Os han salido todos? Estupendo, pero **lo importante no es memorizar los operadores**: es saber **qué pregunta** hace cada filtro o pipeline y **dónde mirar** cuando la cifra no cuadra.
- Si os cuesta pasar de SQL a MongoDB, usad la tabla de equivalencias del cuaderno: `WHERE` ↔ filtro de `find` / `$match`, `GROUP BY` ↔ `$group`, `ORDER BY` ↔ `$sort`.
- Para entregar el trabajo, **explicad con vuestras palabras** al menos 2 ejercicios y anotad **de dónde** habéis sacado cada solución (apuntes, guía, compañero, IA). Eso se valora más que el resultado.
