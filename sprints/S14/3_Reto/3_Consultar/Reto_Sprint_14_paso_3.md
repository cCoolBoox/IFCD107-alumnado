# Paso 3 · Buscar y validar datos (día 1, 60 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 3 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 4 →](Reto_Sprint_14_paso_4.md)
<!--/nav-->

1. Hacer una lista de fuentes candidatas para vuestro brief.
2. Responder, para cada fuente, a cinco preguntas de validación.
3. Rellenar `plan_datos_licencias.md` con lo que sabéis y quedaros con las fuentes que valen.

**En sencillo.** Un proyecto de IA vive de sus datos, y no todos los datos se pueden usar: igual que no se puede coger la foto de otra persona y ponerla en un cartel sin permiso. Este paso consiste en **buscar de dónde van a salir los datos y comprobar que son legales y utilizables**, antes de gastar horas en ellos. Se hace leyendo páginas web, no programando; solo al final hay un trozo de código opcional de cuatro líneas para comprobar que el archivo se abre. **Las licencias se leen vosotros en la web de la fuente**: una IA puede inventarse un enlace o una licencia.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Fuente** | Quién publica los datos y dónde (por ejemplo, el ISTAC o datos.gob.es). |
| **Licencia** | Lo que os permite hacer con los datos. **CC BY**: usarlos citando la fuente. **CC BY-SA**: además, compartir con la misma licencia. **CC BY-NC**: solo uso no comercial. **CC0**: dominio público. Si no hay licencia clara, no se usan. |
| **Datos personales** | Cualquier dato que identifique a una persona: nombre, correo, foto con cara, ubicación exacta. Si son sensibles, no se aceptan. |
| **Variable** | Cada columna de una tabla de datos (por ejemplo, `precio_noche`). |
| **Inventario de fuentes** | La tabla del plan de datos donde se anota cada fuente con su enlace, licencia y tamaño. |
| **Plan de datos** | El documento `plan_datos_licencias.md`: fuente, licencia, variables, calidad, linaje, partición y privacidad. |

**Cómo se hace**

1. **Repartir la búsqueda.** El **responsable de datos** lleva la plantilla del plan de datos y las demás personas buscan y validan **una fuente cada una**. Para empezar, las candidatas de vuestro brief están en la sección 2 de [`briefs_y_rubrica.md`](../../../../proyecto-final/briefs_y_rubrica.md): ISTAC, Frontur-Canarias, datos.gob.es y AEMET para el brief 1; REData y AEMET para el 4; PlantVillage para el 2; el catálogo oficial de FP para el 3. Si elegís el brief 3, mirad también la [guía de acceso gratuito a modelos de lenguaje](../../../../material/Acceso_modelos_de_lenguaje.md).

2. **Responder a las cinco preguntas.** Para cada fuente, **entrad en su web** y apuntad la respuesta a cada pregunta:

    | Pregunta | Dónde se mira | Si la respuesta es mala |
    |---|---|---|
    | ¿Tiene una **licencia** que permita usarla? | En la página del conjunto de datos: buscad «Licencia», «Términos de uso» o «Aviso legal». | Si no está clara, **no se usa**. Kaggle y Hugging Face: cada conjunto tiene su licencia, no asumáis que es libre. |
    | ¿Se puede **descargar**, y podemos repetir la descarga? | Botón de descarga, enlace directo o API. | Si no se puede repetir con un enlace o un script, buscad otra fuente. |
    | ¿Qué **tamaño** tiene? | Debajo del enlace de descarga. | Si no cabe en Colab ni en vuestro ordenador, usad una parte o descartadla. |
    | ¿Qué **variables y qué periodo** trae? ¿Responden a nuestra pregunta? | Descripción del conjunto o diccionario de datos. | Si faltan las variables que necesita vuestra pregunta, cambiad de fuente o de pregunta. |
    | ¿Hay **datos personales**? | Descripción y columnas. | Si los hay y son sensibles, **no se aceptan**. |

3. **Copiar la plantilla.** En GitHub, abrid [`plantilla_plan_datos_licencias.md`](../1_Trabajar/plantillas/plantilla_plan_datos_licencias.md), pulsad **Raw**, copiad todo el texto y, en la carpeta `sprint-14` del repositorio de vuestro equipo, usad *Add file → Create new file*, llamadlo `plan_datos_licencias.md`, pegad y pulsad **Commit changes** (el paso a paso con capturas está en [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md)). Hoy rellenáis tres apartados:

    - **Apartado 1, inventario de fuentes.** Una fila por fuente (D1, D2…): nombre del conjunto, enlace, fecha de descarga, licencia, si permite uso académico o redistribución, formato y tamaño, y si hay datos personales (sí / no). Ejemplo de redacción (inventado): «D1 · Ocupación diaria de un alojamiento · [enlace] · [fecha de descarga] · CC BY 4.0 · sí, citando la fuente · CSV, 60 KB · no».
    - **Apartado 2, diccionario de variables.** Una fila por columna: tipo, unidad, significado, valores válidos y porcentaje de nulos (el porcentaje de nulos lo dejáis vacío hasta el EDA del paso 5).
    - **Apartado 6, privacidad.** ¿Hay datos personales? ¿Hay datos de menores, salud o biometría? (Si la respuesta es sí, **consultad al docente antes de seguir**.) Y qué datos **no** subiréis al repositorio.

    Los apartados 3, 4 y 5 (calidad, linaje y partición) se completan el día 2 con el EDA y el baseline.

4. **(Opcional, si la fuente es un CSV) Comprobar que el archivo se abre.** En Colab, *Archivo → Cuaderno nuevo*, subid el archivo con el panel de archivos (el icono de la carpeta 📁 de la izquierda) y ejecutad en una celda:

    ```python
    import pandas as pd

    datos = pd.read_csv("mis_datos.csv")
    print(datos.shape)
    print(datos.dtypes)
    print((datos.isna().mean() * 100).round(1))
    ```

    Qué hace cada línea:

    - `import pandas as pd` carga la librería que lee tablas y la apoda `pd`.
    - `pd.read_csv("mis_datos.csv")` lee el archivo y lo guarda en `datos`. **Cambiad `mis_datos.csv`** por el nombre exacto de vuestro archivo (o por la URL de descarga, entre comillas).
    - `datos.shape` da (filas, columnas), `datos.dtypes` da el tipo de cada columna y la última línea da el porcentaje de valores vacíos por columna.

    Con el conjunto de práctica `ocupacion_diaria.csv` sale `(1096, 5)`, los tipos `fecha` (texto), `ocupacion_pct`, `temperatura_c`, `festivo` y `precio_medio`, y 0.0 de nulos en todas. Con vuestros datos saldrán otras cifras: lo que importa es que **se abra** y que las columnas tengan sentido.

5. **Quedarse con las fuentes que valen.** Dejad en el inventario las que pasan las cinco preguntas. Si descartáis alguna, escribid la **razón** en su fila («descartada: licencia no indicada»). Recordad la regla de oro: **no se aceptan proyectos «a la espera de datos»**; los datos han de estar identificados y accesibles hoy.

**Qué deberíais ver.** Un inventario con al menos una fuente validada (enlace, licencia, tamaño, variables y «datos personales: no»), la razón escrita de cada fuente descartada y, si hicisteis el paso opcional, el tamaño de la tabla y los tipos de las columnas.

**Hecho cuando:** tenéis al menos una fuente con licencia clara, descargable y sin datos personales sensibles.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| La fuente no dice nada de licencia | Sin licencia no se sabe qué se permite. | Buscad en «Aviso legal» o «Términos de uso»; si sigue sin aparecer, descartadla o preguntad al docente. |
| La IA os da un enlace o una licencia | Las IA pueden inventarlos. | Entrad en el enlace vosotros y leed la licencia en la propia web. |
| `FileNotFoundError: [Errno 2] No such file or directory: 'mis_datos.csv'` | El archivo no está subido en Colab o el nombre no coincide. | Subidlo con el panel 📁 y copiad el nombre exacto, con mayúsculas y extensión. |
| `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1…` | El archivo usa otra codificación (tildes y eñes). | Añadid `encoding="latin-1"`: `pd.read_csv("mis_datos.csv", encoding="latin-1")`. |
| `datos.shape` da `(filas, 1)` y la única columna lleva todos los nombres pegados con `;` | El archivo separa con punto y coma. | Añadid `sep=";"`: `pd.read_csv("mis_datos.csv", sep=";")`. |
| Los datos incluyen nombres, correos o fotos con caras | Son datos personales. | Si son sensibles, no se aceptan: buscad otra fuente o consultad al docente. |
| No hay forma de repetir la descarga | El dato no cumple la segunda pregunta. | Buscad otra fuente, o anotad en el plan cómo descargarla a mano y guardad la fecha. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_14_paso_2.md) · [Ficha del reto](Reto_Sprint_14.md) · [Paso 4 →](Reto_Sprint_14_paso_4.md)
<!--/nav-->
