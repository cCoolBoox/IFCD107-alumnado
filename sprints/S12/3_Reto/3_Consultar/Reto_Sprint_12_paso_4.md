# Paso 4 · Cierre, entrega y review (día 3, 40 minutos)

<!--nav-->
> Sprint 12 · Reto «Escuchar al cliente» · paso 4 de 4 · [Ficha del reto](Reto_Sprint_12.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_12_una_pagina.md)
<!--/nav-->

1. Redactar el informe de reseñas, la nota de IA responsable y el `LEEME.md`.
2. Ejecutar todo desde cero y pedir a alguien que no escribió esa parte que lo revise con la rúbrica.
3. Subir los ficheros a `sprint-12/`, cada persona los suyos.
4. Ensayar los 5 minutos de la review.

**En sencillo.** Queda lo que decide si el cliente os entiende y si otra persona puede repetir vuestro trabajo. Hay que escribir tres textos cortos (un informe, una nota y un `LEEME.md`): no son código, son archivos de texto en formato Markdown (`.md`), donde `##` hace un título y `-` una viñeta. Después se comprueba todo desde cero, alguien que no escribió esa parte lo revisa con la rúbrica, se sube a GitHub y se ensaya la review de 5 minutos. Las cifras que escribáis salen de los cuadernos, nunca de la memoria ni de una IA. No hace falta saber Git: todo se hace desde el navegador.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Markdown** (`.md`) | Texto con marcas sencillas: `## Título`, `- viñeta`, `**negrita**`. GitHub lo muestra ya con formato. |
| **Recomendación ejecutable** | Dice qué hacer, quién y cómo sabremos que funciona. «Mejorar la limpieza» no lo es. |
| **Riesgo y medida** | Algo que puede salir mal con el asistente y lo que hacéis contra ello, medido con una cifra. |
| **Reproducible** | Otra persona repite lo que hicisteis y obtiene los mismos números (`SEMILLA = 42`). |
| **Reiniciar sesión y ejecutar todo** | Opción de Colab que borra la memoria del cuaderno y lo ejecuta de arriba abajo. Si así funciona, funciona de verdad. |
| ***Commit*** | Guardar cambios en GitHub con un mensaje corto y **vuestro nombre**. Sin el botón **Commit changes** no se guarda nada. |
| **Revisión con la rúbrica** | Alguien que no escribió esa parte pone de 1 a 4 en cada criterio y una frase de prueba de lo que ha comprobado. |

**Cómo se hace**

1. **Escribir `informe_resenas.md` (2 páginas como máximo).** Abrid la [plantilla](../1_Trabajar/plantillas/plantilla_informe_cliente.md), pulsad *Raw*, seleccionad todo (`Ctrl + A`) y copiadlo (`Ctrl + C`). En vuestro repositorio, dentro de `sprint-12`: *Add file → Create new file*, nombre `informe_resenas.md`, pegad (`Ctrl + V`) y sustituid cada `…` por vuestro texto. Borrad la nota de niveles del principio. Así queda cada apartado, con las cifras reales del cuaderno de reseñas (las vuestras salen de vuestro código):

    ```text
    ## 1. Resumen para la dirección
    - Qué opina la clientela: el 46,9 % de las 1.500 reseñas es positivo, el 21,2 % neutro y el 31,9 % negativo.
    - Lo más criticado y lo más valorado: la limpieza es el tema más mencionado en las críticas (171 de 478, el 36 %), pero los seis temas aparecen casi igual en críticas y en elogios.
    - Lo que recomendamos hacer primero: revisar la limpieza de las habitaciones.

    ## 2. Sentimiento
    <img src="grafico_resenas.png" width="500">
    46,9 % positivas · 21,2 % neutras · 31,9 % negativas.
    1. «Viajamos en familia. La limpieza deja mucho que desear...» (`id_resena`: 13)
    2. «Pasamos una semana aquí. La habitación estaba sucia.» (`id_resena`: 17)
    3. «Pasamos una semana aquí. Tardaron una hora en resolver un problema simple. Ruido constante por la noche. La habitación estaba sucia.» (`id_resena`: 20)
    Exactitud en prueba: 99,2 % (372 de 375 reseñas). Siempre decir «positivo» acertaría el 46,9 %.

    ## 4. Recomendaciones
    1. **Qué:** revisar la limpieza de las habitaciones antes de cada llegada. **Quién:** la dirección del alojamiento. **Cómo sabremos que funciona:** baja el porcentaje de críticas que mencionan limpieza (hoy, el 36 %).
    2. **Qué:** … **Quién:** … **Cómo sabremos que funciona:** …
    3. **Qué:** … **Quién:** … **Cómo sabremos que funciona:** …

    ## 5. Límites y cautelas
    - Datos sintéticos (inventados para el curso): las reseñas son más repetitivas que las reales.
    - El método no entiende negaciones: «La limpieza no es impecable» la clasifica como positiva.
    - Con datos reales habría que anonimizar las reseñas antes de analizarlas.
    ```

    La línea `<img …>` enseña el gráfico dentro del informe: `grafico_resenas.png` tiene que estar **en la misma carpeta**, `sprint-12/`. El apartado 3 (tabla de temas con un ejemplo real de cada uno) es del nivel extra: una fila por tema con los números de vuestra tabla de la parte A. Las tres recomendaciones se escriben con vuestras cifras, y se dice siempre que los datos son sintéticos.

2. **Escribir `nota_ia_responsable.md` (1 página).** Con *Add file → Create new file* en `sprint-12`. Una tabla con los riesgos concretos del reto y, para cada uno, qué medida aplicasteis y cómo la medisteis. Ejemplo con las cifras de los pasos 2 y 3 (las vuestras salen de vuestra evaluación):

    ```text
    | Riesgo | Qué pasa | Medida | Cómo la medimos |
    |---|---|---|---|
    | El asistente responde a lo que no sabe | Con umbral 0, «¿Tienen gimnasio?» se contesta con la norma de fumar | Umbral 0.15 y la frase «No consta…» | Con 25 preguntas: umbral 0 → 2 alucinaciones; umbral 0.15 → 0 |
    | Datos personales en las reseñas | Las reseñas reales pueden traer nombres o contactos; las de este reto son sintéticas | Anonimizar antes de guardarlas y no pegarlas en una IA externa | No medida: lo decimos |
    | Texto que manipula al asistente | 3 de 3 ataques funcionan sin defensa | Filtro de frases sospechosas (`es_seguro`) | Con filtro: 0 de 3 ataques y 0 de 25 preguntas legítimas bloqueadas; se esquiva con «I-g-n-o-r-a» o en inglés |
    | Sesgos y límites del clasificador | No entiende negaciones y confunde 3 neutras con negativas | Decirlo en el informe y no usarlo para decidir sobre personas | Matriz de confusión: 3 errores en 375 reseñas |

    **Uso de la IA:** Le pedí [qué]; comprobé [cómo]; cambié [qué].
    ```

    Si usasteis una IA para algo, contad qué le pedisteis y qué comprobasteis; si no, decidlo. Si la pregunta sin respuesta de vuestra evaluación falló (el caso de la lavandería del paso 3), ese es uno de vuestros riesgos reales: ponedlo.

3. **Escribir `LEEME.md` (cinco líneas).** Con *Add file → Create new file* en `sprint-12`. Para las versiones, ejecutad esta celda en cualquier cuaderno y copiad lo que escriba:

    ```python
    import sys, numpy, pandas, sklearn, statsmodels, matplotlib
    print("python", sys.version.split()[0])
    for lib in (numpy, pandas, sklearn, statsmodels, matplotlib):
        print(lib.__name__, lib.__version__)
    ```

    Qué hace cada línea:

    - `import …` trae las librerías que usan los cuadernos. `sys` es la del propio Python.
    - `sys.version.split()[0]` es el número de versión de Python.
    - El `for` repite `print(nombre, versión)` para cada librería: `lib.__name__` es su nombre y `lib.__version__`, su versión.

    El `LEEME.md` tiene cinco líneas:

    ```text
    # LEEME · Sprint 12 · Escuchar al cliente
    1. Contenido: informe_resenas.md, grafico_resenas.png, resenas.ipynb, ocupacion.ipynb, asistente_rag.ipynb, evaluacion_asistente.csv y nota_ia_responsable.md.
    2. Orden: resenas.ipynb, ocupacion.ipynb y asistente_rag.ipynb; en cada uno, Entorno de ejecución → Reiniciar sesión y ejecutar todo.
    3. Datos: resenas.csv, ocupacion_diaria.csv, politica_alojamiento.md y preguntas_referencia.csv, en data/ (los cuadernos los descargan con la función dato()).
    4. Versiones: python …, numpy …, pandas …, scikit-learn …, statsmodels …, matplotlib …
    5. Semilla: SEMILLA = 42 en los tres cuadernos; el asistente usa el simulador, sin ninguna clave.
    ```

    Al final del `LEEME.md` se añade la sección de revisión del punto 5.

4. **Ejecutar todo desde cero y descargar los cuadernos.** En cada cuaderno: *Entorno de ejecución → Reiniciar sesión y ejecutar todo*. Mirad **hasta el final** que ninguna celda tenga un error en rojo. Si falla algo, arreglad el cuaderno **antes** de descargarlo (el paso 2 trae los errores más frecuentes). Después, *Archivo → Descargar → Descargar .ipynb*: así lleva los resultados guardados. El nombre tiene que ser `resenas.ipynb`, `ocupacion.ipynb` y `asistente_rag.ipynb`, en minúsculas y sin espacios: si trae `Copia de…`, cambiadlo antes de subirlo. Comprobad que no hay **ninguna clave** en ningún fichero.
5. **Revisión con la rúbrica (15 minutos).** Quien revisa **no escribió esa parte**. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md): ejecutar cada cuaderno siguiendo solo el `LEEME.md`, leer el informe como si fuera la dirección de TurisData, probar el asistente y comparar la nota con lo que hace, poner nivel con una frase de prueba y apuntarlo. Se anota **al final del `LEEME.md`** con este formato:

    ```text
    ## Revisión con la rúbrica
    **Revisado por:** <nombre> · **Fecha:** <dd/mm/aaaa>

    | Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
    |---|---|---|
    | Corrección técnica | <1–4> | <p. ej. «MAE del modelo y del baseline en la misma tabla; falta la matriz de confusión»> |
    | Reproducibilidad | <1–4> | <¿obtienes los mismos números siguiendo solo este LEEME?> |
    | Análisis y comunicación al cliente | <1–4> | <¿se entienden las 3 recomendaciones sin saber programar?> |
    | IA responsable | <1–4> | <¿cada riesgo de la nota tiene una medida y alguna está medida?> |

    **Lo primero que mejoraríamos:** <una cosa concreta>
    ```

    Sin frase de prueba, el nivel no vale. Lo más fácil de arreglar se arregla ya; lo demás queda en «lo primero que mejoraríamos».

6. **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-12`**; (2) *Add file → Upload files*; (3) arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace, así que cada persona sube lo suyo con su cuenta: la A, `informe_resenas.md`, `grafico_resenas.png` y `resenas.ipynb`; la B, `ocupacion.ipynb`; la C, `asistente_rag.ipynb` y `evaluacion_asistente.csv`; quien lleve la IA responsable y la coordinación, `nota_ia_responsable.md` y `LEEME.md`. Cada persona sube también su `autoevaluacion_nombre.md`. Los nombres de archivo, **en minúsculas y sin espacios**. Los cuatro ficheros de datos van a `data/` solo si aún no están. Si `sprint-12/` trae un `README.md`, rellenadlo también (qué se entrega, quién hizo qué y cómo reproducirlo).
7. **Ensayar la review (5 minutos por equipo).** Presentad **una cifra, un gráfico y una demo**, hablando todas las personas. Por ejemplo: la cifra, «la previsión se equivoca 3.2 puntos de ocupación frente a 4.5 del método simple»; el gráfico, el de las reseñas o el de la previsión; y la demo, una pregunta que el asistente responde bien, **la que no sabe** («¿Tienen gimnasio?» → «No consta…») y un ataque frenado. Cronometradlo una vez. Después, 3 minutos de preguntas, que pueden ir a cualquier persona.

**Qué deberíais ver.** En la carpeta `sprint-12` del repositorio, los ocho ficheros del equipo y una hoja de autoevaluación por persona (**8 + N**), y en el historial (el icono del reloj), *commits* de personas distintas. El `informe_resenas.md` muestra el gráfico y el `LEEME.md` termina con la revisión rellena.

**Hecho cuando:** otra persona podría repetir todo siguiendo solo el `LEEME.md`, la sección «Revisión con la rúbrica» está rellena, cada persona ha subido su autoevaluación y coevaluación, y el equipo ha ensayado su presentación de 5 minutos.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| En `informe_resenas.md` el gráfico sale como un icono roto | `grafico_resenas.png` no está en la misma carpeta que el informe o el nombre no coincide. | Subid el PNG a `sprint-12/` con ese nombre exacto, en minúsculas. |
| *Reiniciar sesión y ejecutar todo* se detiene con un error en rojo | Hay una celda de ejercicio sin completar o una celda que depende de otra que falta. | Mirad el nombre del error y buscadlo en «Si algo falla» del paso 2. Arreglad antes de descargar. |
| Subí el archivo a la raíz, no a `sprint-12/` | Se subió sin entrar antes en la carpeta. | Abrid el archivo, pulsad el icono del lápiz, escribid `sprint-12/` delante del nombre en la ruta y pulsad **Commit changes**: lo mueve. |
| No veo «Add file» | No sois colaboradores o no habéis aceptado la invitación. | Aceptad la invitación (correo o github.com/notifications) o avisad al docente. |
| El archivo no aparece en la carpeta | Faltó pulsar el botón verde **Commit changes**. | Volved a subirlo y pulsadlo. |
| Se subió una clave o un dato personal | Borrarlo no basta: queda en el historial. | Avisad al docente de inmediato. |
| El informe pasa de dos páginas | Hay adornos o frases que no son cifras, recomendaciones ni límites. | Recortad: quedan las cifras, las 3 recomendaciones y los límites. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_12_paso_3.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_12.md)
<!--/nav-->
