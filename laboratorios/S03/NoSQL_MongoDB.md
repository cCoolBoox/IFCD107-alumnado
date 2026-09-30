# NoSQL con MongoDB · guía de laboratorio (Sprint 3)

**Tiempo:** 60 min · **Nivel:** sin conocimientos previos de MongoDB · **Programación:** ninguna en el bloque de Compass; el cuaderno opcional usa Python.

## Objetivo
Guardar las reservas de *TurisData Canarias* como **documentos**, consultarlas, modificarlas y agruparlas, y comparar el resultado con lo que ya hiciste en SQL.

## Tres formas de hacerlo (elige una)
| Opción | Qué necesitas | Cuándo elegirla |
|---|---|---|
| **A. Cuaderno sin instalación** | Navegador + Colab, o Python en local | Es la opción recomendada si tu equipo no permite instalar programas. Usa `pymongo` con `mongomock` (una imitación en memoria). |
| **B. MongoDB Compass + MongoDB local** | Instalar MongoDB Community y Compass (interfaz gráfica) | Si puedes instalar software y quieres ver la herramienta real. |
| **C. MongoDB Atlas (nube), nivel gratuito M0** | Cuenta en Atlas | Si quieres ver un servidor en la nube. **[verificar]** qué datos pide el alta (por ejemplo, si solicita tarjeta), qué límites tiene el nivel M0 y qué red/IP hay que permitir; la información cambia y la confirmará el docente antes de la sesión. |

> Los datos son sintéticos. No subas datos reales de clientes a ningún servicio en la nube.

## Opción A · Cuaderno `S03_01_nosql_mongomock`
1. Abre el cuaderno desde la tabla del `README` del sprint (insignia de Colab).
2. Ejecútalo de arriba abajo: verás cómo se construyen los documentos, el CRUD, las agregaciones y la comparación con SQL.
3. Completa los 7 ejercicios: cada uno se autocorrige con un mensaje de ayuda.

## Opción B · Compass con MongoDB local
1. Instala **MongoDB Community Server** y **MongoDB Compass** desde la web oficial de MongoDB **[verificar la versión y el instalador de tu sistema]**.
2. Abre Compass y conéctate a `mongodb://localhost:27017`.
3. Crea la base `turisdata` y la colección `reservas`.
4. Genera el archivo de documentos con el cuaderno de la opción A (o con este fragmento, ejecutado donde tengas `turisdata.db`):

```python
import sqlite3, json
con = sqlite3.connect("turisdata.db"); con.row_factory = sqlite3.Row
docs = []
for r in con.execute("""SELECT r.*, a.nombre AS an, a.isla, a.categoria, c.pais AS cp
                        FROM reservas r JOIN alojamientos a USING(id_alojamiento)
                        JOIN clientes c USING(id_cliente)"""):
    docs.append({"_id": r["id_reserva"], "canal": r["canal"], "noches": r["noches"],
                 "precio_noche": r["precio_noche"], "cancelada": bool(r["cancelada"]),
                 "alojamiento": {"nombre": r["an"], "isla": r["isla"], "categoria": r["categoria"]},
                 "cliente": {"pais": r["cp"]}})
json.dump(docs, open("reservas.json", "w", encoding="utf8"), ensure_ascii=False)
```

5. En Compass: colección `reservas` > **Add Data > Import JSON or CSV file** > elige `reservas.json`. **[verificar el nombre exacto de los botones en tu versión de Compass]**
6. Pestaña **Documents**, campo *Filter*. Prueba estos filtros:

| Pregunta | Filtro |
|---|---|
| Reservas del canal directo | `{ "canal": "directo" }` |
| Más de 10 noches en Lanzarote | `{ "alojamiento.isla": "Lanzarote", "noches": { "$gt": 10 } }` |
| Canceladas de agencia o de empresa | `{ "cancelada": true, "canal": { "$in": ["agencia", "empresa"] } }` |

7. Pestaña **Aggregations**: crea la pipeline de la tasa de cancelación por canal:

```json
[
  { "$group": { "_id": "$canal",
                "reservas": { "$sum": 1 },
                "tasa": { "$avg": { "$cond": ["$cancelada", 1, 0] } } } },
  { "$sort": { "tasa": -1 } }
]
```
8. Comprueba que la tasa por canal coincide con la de la consulta SQL del script `03_group_by.sql` (ejemplo "IDEA 2").

## Opción C · Atlas M0
Sigue los pasos que indique el docente el día de la sesión (creación de la cuenta, clúster gratuito, usuario de base de datos, acceso de red y cadena de conexión). Todos los detalles de la interfaz están **[verificar]**. Después, en el cuaderno, cambia `USAR_MONGO_REAL = True` y pega tu cadena de conexión en `MONGO_URI`. **Nunca subas la cadena de conexión (contiene tu contraseña) a un repositorio.**

## Preguntas para el cuaderno de aprendizaje
1. ¿Qué información has embebido en cada reserva y qué inconveniente tiene repetirla?
2. Escribe el mismo filtro de "más de 10 noches en Lanzarote" en SQL y en MongoDB. ¿Qué es más claro para ti?
3. Cita un caso de TurisData donde elegirías MongoDB y otro donde seguirías con SQL. Justifica.

## Cuando termines
- Cierra Compass o desconecta Colab. Si usaste un servicio en la nube, **elimina el clúster** al acabar el curso (o cuando el docente lo indique).
