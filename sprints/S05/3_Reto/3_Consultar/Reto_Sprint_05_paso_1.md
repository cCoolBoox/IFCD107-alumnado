# Paso 1 · Cargar los datos en una base de datos (día 2, 30 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 1 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 2 →](Reto_Sprint_05_paso_2.md)
<!--/nav-->

1. Abrir el cuaderno `S05_07` en Colab, guardar una copia y compartirla con el equipo.
2. Ejecutar las dos primeras celdas de código (preparación e importaciones).
3. Crear `turisdata_reto.db` con la tabla `ocupacion_diaria` y un índice, y leerla con SQL.

**Cómo se hace**
- **Preparar el cuaderno.** Abrid el [cuaderno](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_07_reto_ocupacion.ipynb), pulsad *Archivo → Guardar una copia en Drive* y compartidla con el equipo. Una persona escribe y las demás miran y opinan; cambiad de turno cada pocos minutos. Ejecutad la celda de «Preparación» y la de importaciones.
- **Cargar el CSV.** La función `dato("ocupacion_diaria.csv")` os da la ruta del fichero. Leedlo con `pd.read_csv`.
- **Crear la base.** Abrid una conexión con `sqlite3.connect(RUTA_BD)` y llamadla **`con`** (los puntos de control usan ese nombre). Guardad la tabla con `to_sql("ocupacion_diaria", con, if_exists="replace", index=False)`. Sin `replace`, al repetir la celda os daría error o duplicaría datos.
- **Crear el índice.** Con `con.execute`, la orden `CREATE INDEX IF NOT EXISTS idx_ocupacion_fecha ON ocupacion_diaria(fecha)` y después `con.commit()`. El nombre del índice tiene que ser exactamente ese.
- **Leer con SQL.** `pd.read_sql_query(...)` con una consulta `SELECT ..., CAST(SUBSTR(fecha, 6, 2) AS INTEGER) AS mes FROM ocupacion_diaria`. El resultado se llama **`diaria`** y trae, además de las columnas del CSV, la columna `mes` (un número del 1 al 12). Este paso es la práctica de CRUD: si ya hicisteis [`S05_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_06_crud_python.ipynb), copiad el código.

**Qué deberíais ver.** El mensaje `Punto de control 1 superado`, y en el panel de archivos de Colab el fichero `turisdata_reto.db`. Si falla, el mensaje del `assert` dice qué falta (el archivo, las 1096 filas, la columna `mes` o el índice).

**Hecho cuando:** `turisdata_reto.db` existe, `diaria` tiene 1096 filas con la columna `mes` y el punto de control 1 está superado.

<!--nav-->
---

[Ficha del reto](Reto_Sprint_05.md) · [Paso 2 →](Reto_Sprint_05_paso_2.md)
<!--/nav-->
