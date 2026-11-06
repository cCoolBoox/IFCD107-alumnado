# Paso 1 · Cargar los datos en una base de datos (día 2, 30 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 1 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 2 →](Reto_Sprint_05_paso_2.md)
<!--/nav-->

1. Abrir el cuaderno `S05_07` en Colab, guardar una copia y compartirla con el equipo.
2. Ejecutar las dos primeras celdas de código (preparación e importaciones).
3. Crear `turisdata_reto.db` con la tabla `ocupacion_diaria` y un índice, y leerla con SQL.

**En sencillo.** Los datos del cliente vienen en un archivo de texto (`ocupacion_diaria.csv`): una fila por día, con la ocupación, la temperatura y si fue festivo. En este paso los metéis en una **base de datos**, que es como un armario con cajones ordenados: guarda tablas y deja pedir datos con preguntas muy precisas. Después hacéis una de esas preguntas (en un idioma que se llama **SQL**) para traer los datos de vuelta al cuaderno, ya con una columna nueva: el **mes**. No hace falta saber programar: escribís unas pocas líneas que aquí tenéis casi hechas, las ejecutáis y comprobáis que el cuaderno os da el visto bueno.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Celda** | Cada caja del cuaderno. Las de texto se leen; las de código se **ejecutan** con el botón ▶ (o con `Mayús + Intro`). |
| **Variable** | Un nombre al que se guarda un valor para usarlo después. `datos = …` guarda lo que haya a la derecha con el nombre `datos`. |
| **Librería** | Un paquete de herramientas ya hechas. Se traen con `import`; `pd` es el apodo de `pandas`. |
| **CSV** | Un archivo de texto con una tabla: cada línea es una fila y los valores van separados por comas. |
| **DataFrame** | La tabla de `pandas` dentro de Python: filas, columnas con nombre y valores. |
| **Base de datos y tabla** | La base es el archivo (`turisdata_reto.db`); dentro hay tablas, como las hojas de un libro de cálculo. |
| **SQL** | El idioma para pedir datos a una base. `SELECT` significa «dame» y `FROM`, «de esta tabla». |
| **Índice** | Como el índice de un libro: hace que buscar por una columna (aquí, `fecha`) sea rápido. |
| **Conexión (`con`)** | La línea abierta con la base: por ella enviáis órdenes y recibís respuestas. |

**Cómo se hace**

1. **Abrir vuestra copia del cuaderno.** Entrad en el [cuaderno `S05_07`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_07_reto_ocupacion.ipynb) (se abre en Colab). Arriba, *Archivo → Guardar una copia en Drive*: así trabajáis en una copia vuestra y el original no se toca. Pulsad *Compartir* (arriba a la derecha) y añadid los correos del equipo con permiso de **Editor**. Una persona escribe y las demás miran y opinan; cambiad de turno cada pocos minutos.
2. **Ejecutar las dos celdas de preparación.** Son las dos primeras celdas con código («Preparación» e importaciones). Pulsad ▶ en cada una, **por orden**. No escriben nada en pantalla: sabréis que han terminado porque aparece un ✓ y un número entre corchetes (`[1]`, `[2]`). La primera crea la función `dato(…)`, que localiza (y descarga si hace falta) los datos del curso; la segunda trae las librerías.
3. **Ir a la celda del apartado «1 · Base de datos».** Veréis una línea que empieza por `# TODO` (es una pista, Python la ignora), tres puntos `...` y varias líneas con `assert` y `print`. **Borrad solo los tres puntos** y escribid ahí el código de abajo. No toquéis las líneas `assert`: son el **punto de control**, que comprueba vuestro trabajo.
4. **Escribir el código.** Copiad o escribid esto, respetando mayúsculas, comillas y paréntesis:

    ```python
    datos = pd.read_csv(dato("ocupacion_diaria.csv"))
    con = sqlite3.connect(RUTA_BD)
    datos.to_sql("ocupacion_diaria", con, if_exists="replace", index=False)
    con.execute("CREATE INDEX IF NOT EXISTS idx_ocupacion_fecha ON ocupacion_diaria(fecha)")
    con.commit()
    diaria = pd.read_sql_query(
        "SELECT *, CAST(SUBSTR(fecha, 6, 2) AS INTEGER) AS mes FROM ocupacion_diaria", con)
    ```

    Qué hace cada línea:

    - `datos = pd.read_csv(dato("ocupacion_diaria.csv"))`: `dato(…)` da la ruta del archivo; `pd.read_csv` lo lee y lo guarda en la variable `datos` como un DataFrame (1096 filas: un día por fila, tres años).
    - `con = sqlite3.connect(RUTA_BD)`: abre (o crea) la base `turisdata_reto.db` y guarda la conexión en `con`. **Tiene que llamarse `con`**: el punto de control usa ese nombre.
    - `datos.to_sql(…)`: copia la tabla `datos` dentro de la base con el nombre `ocupacion_diaria`. `if_exists="replace"` borra la tabla vieja si ya existía, y así podéis ejecutar la celda varias veces sin duplicar filas; `index=False` evita una columna de números sobrante.
    - `con.execute("CREATE INDEX …")`: crea el índice. El nombre `idx_ocupacion_fecha` tiene que ser **exactamente ese**.
    - `con.commit()`: confirma los cambios, como «guardar». Sin esta línea la base puede quedarse sin ellos.
    - `diaria = pd.read_sql_query("SELECT …", con)`: lanza la pregunta SQL y guarda la respuesta en `diaria`. `SELECT *` pide todas las columnas; `SUBSTR(fecha, 6, 2)` recorta de `2023-07-14` los caracteres 6 y 7 (`07`, el mes); `CAST(… AS INTEGER)` lo convierte en el número `7`; y `AS mes` pone nombre a la columna nueva.

    Este paso es la práctica de CRUD (crear y leer datos en una base). Si ya hicisteis [`S05_06`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/en_clase/S05_06_crud_python_en_clase.ipynb), podéis copiar el código de ahí.

5. **Ejecutar y mirar.** Pulsad ▶. Si todo va bien, abajo aparece `Punto de control 1 superado`. Para ver los datos, añadid una celda nueva con estas dos líneas (`diaria.shape` dice cuántas filas y columnas; `diaria.head()` muestra las cinco primeras filas):

    ```python
    print(diaria.shape)
    diaria.head()
    ```

    **Ojo:** Colab solo enseña por sí mismo el resultado de la **última** línea de la celda. Por eso `diaria.shape` va dentro de `print(…)` y `diaria.head()` va al final. Si escribís las dos sin `print` en la misma celda, solo veréis una de ellas.

**Qué deberíais ver.** El mensaje `Punto de control 1 superado`. Con `diaria.head()`, una tabla de seis columnas (`fecha`, `ocupacion_pct`, `temperatura_c`, `festivo`, `precio_medio` y `mes`) cuya primera fila es `2023-01-01`, 89.0, 18.1, 1, 97.43 y mes 1; con `diaria.shape`, `(1096, 6)`. Y en el panel de archivos de Colab (el icono de la carpeta 📁 de la izquierda; si no aparece, pulsad el icono de refrescar) el fichero `turisdata_reto.db`. Si falla, el mensaje del `assert` dice qué falta (el archivo, las 1096 filas, la columna `mes` o el índice).

**Hecho cuando:** `turisdata_reto.db` existe, `diaria` tiene 1096 filas con la columna `mes` y el punto de control 1 está superado.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'pd' is not defined` (o `'sqlite3'`, `'dato'`, `'RUTA_BD'`) | No se ha ejecutado una celda de preparación, o Colab se reinició y se olvidó de todo. | Ejecutad las dos celdas de preparación por orden y después la vuestra. |
| `AssertionError: Debe existir el archivo turisdata_reto.db` | La celda corre, pero la base aún no se ha creado. | Comprobad que habéis borrado los `...` y que está la línea con `sqlite3.connect(RUTA_BD)`. |
| `AssertionError: Deben leerse 1096 días y has leído …` | `diaria` no tiene las 1096 filas. | Mirad `diaria.shape` y comprobad que leéis la tabla `ocupacion_diaria`. |
| `AssertionError: Falta la columna mes (1-12)` | La consulta SQL no crea la columna `mes`. | Revisad `CAST(SUBSTR(fecha, 6, 2) AS INTEGER) AS mes`: el 6, el 2 y el `AS mes`. |
| `AssertionError: Falta el índice idx_ocupacion_fecha` | El índice no existe o tiene otro nombre. | Copiad el nombre tal cual y no olvidéis `con.commit()`. |
| `FileNotFoundError: … 'ocupacion_diaria.csv'` | Habéis escrito el nombre del archivo directamente en `read_csv`. | Usad `pd.read_csv(dato("ocupacion_diaria.csv"))`: `dato(…)` sabe dónde está el archivo. |
| `ProgrammingError: Cannot operate on a closed database` | La última celda del cuaderno (`con.close()`) cierra la conexión y se ejecutó antes de tiempo. | Volved a ejecutar la celda del apartado 1 (abre otra conexión) y dejad `con.close()` para el final. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_05.md) · [Paso 2 →](Reto_Sprint_05_paso_2.md)
<!--/nav-->
