# Paso 1 · Entender el problema y los datos (día 2, 10 minutos)

<!--nav-->
> Sprint 3 · Reto «Primer modelo en producción» · paso 1 de 6 · [Ficha del reto](Reto_Sprint_03.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md) · [Paso 2 →](Reto_Sprint_03_paso_2.md)
<!--/nav-->

1. Escribir en una frase qué se predice y para qué lo usará el equipo de reservas.
2. Calcular con SQL el porcentaje de cancelaciones por canal.
3. Revisar las columnas una a una: ¿se conocen el día que se hace la reserva?

**En sencillo.** Antes de pedirle nada a un modelo hay que saber qué se le pregunta y con qué información. Es como un médico: antes de recetar pregunta qué le pasa al paciente y mira los datos que tiene *en la consulta*, no los que tendrá la semana que viene. Aquí la pregunta es «¿se cancelará esta reserva?» y los datos son los de TurisData. La trampa más habitual se llama **fuga de datos**: usar una columna que solo existe cuando la reserva ya se ha cancelado. El modelo parecería un genio y, en la vida real, no serviría para nada. En este paso no se programa: usáis una consulta SQL que ya hicisteis el lunes y una tabla hecha con lápiz y papel. No hace falta saber nada de modelos.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Variable objetivo** | Lo que queremos predecir. Aquí, la columna `cancelada`: 1 si la reserva se canceló, 0 si no. |
| **Columna (o variable)** | Cada dato de una reserva: `canal`, `tarifa`, `noches`, etc. |
| **Fuga de datos** | Usar para predecir un dato que **no tendríamos en el momento de decidir**. Hace trampa y los resultados parecen mejores de lo que son. |
| **Identificador** | Un número que solo distingue una fila de otra (`id_reserva`). No describe la reserva. |
| **Porcentaje de cancelación** | Cuántas de cada 100 reservas se cancelan. Como `cancelada` vale 0 o 1, su media (`AVG`) es esa proporción. |

**Cómo se hace**

1. **Escribir la frase del cliente.** Entre todo el equipo, en la hoja o el tablero: «Queremos predecir ______ para que el equipo de reservas pueda ______». Ejemplo de redacción (no lo copiéis): «Queremos predecir qué reservas tienen riesgo de cancelarse para que el equipo pueda decidir a quién llamar antes». Esta frase abre vuestro informe.

2. **Calcular el porcentaje de cancelaciones por canal.** Abrid `turisdata.db` en DB Browser (*Abrir base de datos*, `Ctrl + O`; si no la tenéis, [descargadla](../../../../datos/turisdata.db) con *Download raw file*). Pestaña *Ejecutar SQL*, pegad la consulta, **seleccionadla con el ratón** y pulsad `Ctrl + Intro`. Es la «IDEA 2» del script [`03_group_by.sql`](../../2_Practica/sql/03_group_by.sql) que hicisteis el lunes:

    ```sql
    SELECT canal, COUNT(*) AS reservas, ROUND(100.0 * AVG(cancelada), 1) AS pct_cancelacion
    FROM reservas
    GROUP BY canal
    ORDER BY pct_cancelacion DESC;
    ```

    Qué hace cada línea:

    - `SELECT canal, COUNT(*) AS reservas, …`: pide el canal, cuántas reservas hay en él (`COUNT(*)`) y el porcentaje de canceladas.
    - `ROUND(100.0 * AVG(cancelada), 1) AS pct_cancelacion`: la media de `cancelada` (0 o 1) por 100 es el porcentaje; `ROUND(…, 1)` deja un decimal.
    - `FROM reservas`: de la tabla `reservas`.
    - `GROUP BY canal`: una fila por cada canal, en lugar de una para todo.
    - `ORDER BY pct_cancelacion DESC`: de mayor a menor porcentaje.

    Apuntad las cuatro filas: irán al informe.

3. **Decidir la variable objetivo.** Es `cancelada`. Escribidlo en la hoja junto a la frase del paso 1.

4. **Hacer la tabla de las 18 columnas.** Son las del archivo que usa el cuaderno, `reservas_turisdata.csv`; las tenéis agrupadas en el [listado de pasos de AutoML](../../2_Practica/automl/listado_pasos_automl.md) y explicadas en el [esquema de `turisdata.db`](../../2_Practica/esquema_turisdata/esquema_turisdata.md). Haced una fila por columna y contestad la misma pregunta en todas: **«¿La tendríamos ya el día que queremos dar la alerta?»** Así queda (tres filas de ejemplo; rellenad las otras 15):

    ```text
    | Columna    | ¿La conoceríamos el día de la reserva? | ¿Entra en el modelo?    |
    |------------|-----------------------------------------|-------------------------|
    | id_reserva | Sí, pero es solo un número de serie     | No: no explica nada     |
    | canal      | Sí: se sabe por dónde reserva el cliente | Sí                      |
    | cancelada  | No: es justo lo que queremos predecir   | No: es la variable objetivo |
    ```

    Qué no vale: poner «sí» a todas sin pensarlo, o dar por buena una columna sin saber qué es (mirad el esquema). Si dudáis de una, preguntaos si cuenta algo de **antes** de reservar o de **después**. Con este archivo no hay columnas que delaten la cancelación (no existe, por ejemplo, una `fecha_cancelacion`): lo normal es que solo queden fuera `id_reserva` y `cancelada`. Aun así hay que **razonarlo columna a columna y anotarlo**, porque eso es parte del informe.

5. **Guardar lo anotado para el informe.** La frase, el porcentaje por canal y la tabla de columnas (en el informe basta con decir qué columnas quedan fuera y por qué) se usan en el apartado 1 de la [plantilla del informe](../1_Trabajar/plantillas/plantilla_informe_modelo.md).

**Qué deberíais ver.** En SQL, cuatro filas (`agencia`, `directo`, `empresa` y `web_intermediaria`) con tres columnas; los porcentajes quedan entre el 30 % y el 55 % aproximadamente, y las reservas de las cuatro filas suman 6.000. En la hoja del equipo, una frase, una variable objetivo y una tabla de 18 filas en la que `id_reserva` y `cancelada` no entran en el modelo y cada «sí» tiene una razón.

**Hecho cuando:** tenéis la frase del cliente, el porcentaje por canal anotado y la tabla de las 18 columnas con las excluidas explicadas.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `no such table: reservas` | La base abierta no es `turisdata.db`, o está vacía. | Mirad la pestaña *Estructura de la base de datos*: deben aparecer `alojamientos`, `clientes` y `reservas`. Si no, abrid otra vez el archivo; si sigue vacía, importad `turisdata.sql` como explica la [guía de SQL en parejas](../../2_Practica/sql/guia_sql_en_parejas.md). |
| Se ejecutan todas las consultas del script y salen muchas pestañas | No seleccionasteis la consulta antes de pulsar `Ctrl + Intro`. | Seleccionad solo esas líneas con el ratón y volved a ejecutar. |
| No encontráis la lista de las 18 columnas | Está en el listado de pasos de AutoML y en el esquema de la base. | Abrid el [listado de pasos de AutoML](../../2_Practica/automl/listado_pasos_automl.md) (apartado «Qué datos usa»). |
| No sabéis si una columna se conoce al reservar | Hay que razonarla, no adivinarla. | Preguntaos «¿la tendría el día que doy la alerta?»; si seguís sin saberlo, apuntad la duda en la hoja y preguntad al docente. |
| Una columna no se conocería al reservar (no pasa con este archivo) | Es una fuga de datos. | En la celda de la partición del cuaderno (paso 3 del cuaderno), cambiad las dos líneas `.drop(columns=["id_reserva"])` por `.drop(columns=["id_reserva", "nombre_de_la_columna"])` y repetid desde esa celda, porque habrá que **volver a entrenar**. |
| Ya habéis entrenado en la práctica y ahora dudáis de una columna | El orden del día pone el laboratorio antes del reto. | No pasa nada si la columna es válida. Si no lo es, aplicad el arreglo de la fila anterior y volved a entrenar (con `LIMITE_TIEMPO = 15` tarda unos 15 segundos). |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_03.md) · [Paso 2 →](Reto_Sprint_03_paso_2.md)
<!--/nav-->
