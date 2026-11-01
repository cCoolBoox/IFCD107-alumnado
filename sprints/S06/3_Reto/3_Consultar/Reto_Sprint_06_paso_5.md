# Paso 5 · Informe, README y revisión con la rúbrica (día 2, 20 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 5 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md)
<!--/nav-->

1. Completar `informe_calidad.md` a partir de la plantilla.
2. Rellenar el `README.md` y comprobar *Reiniciar y ejecutar todo*.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado.

**En sencillo.** Ya tenéis el trabajo hecho; falta **contarlo** para que otra persona lo entienda sin vosotros delante. El informe es para el gerente del hotel, que no programa: qué estaba mal, cuántas filas afecta y qué habéis hecho con cada cosa. El README es el «manual de instrucciones»: con él, alguien de fuera debería poder abrir el cuaderno y obtener las mismas cifras. Después, una persona que no ha escrito esa parte lo revisa con la rúbrica, como un corrector con ojos frescos. Casi todo sale de lo que ya habéis ejecutado en los pasos 2, 3 y 4; solo hay una celda de código nueva y es pequeña.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Informe** | El documento (`informe_calidad.md`) donde se cuenta el trabajo a quien no programa. |
| **README** | La «portada» de la carpeta: qué hay, cómo ejecutarlo y quién hizo qué. |
| **Reiniciar y ejecutar todo** | Borra la memoria del cuaderno y ejecuta todas las celdas de arriba abajo. Es la prueba de que no depende de nada «escondido». |
| **Versión** | El número de edición de Python o de una librería. Con otra versión, algunos números pueden cambiar un poco. |
| **Rúbrica** | La tabla con la que se evalúa: cuatro criterios, cada uno de 1 a 4. |
| **Sesgo / discriminar** | Que el modelo trate peor a un grupo (por ejemplo, por su país) sin que haya una razón válida. |
| ***Commit*** | Guardar vuestros cambios en GitHub con un mensaje corto y vuestro nombre. Sin pulsar **Commit changes**, no se guarda nada. |
| ***Review* y *retro*** | La *review* enseña el trabajo a otros equipos; la *retro* es hablar de cómo trabajasteis. |

**Cómo se hace**

1. **Rellenar el informe.** Abrid `informe_calidad.md` (lo creasteis en el paso 2; para editarlo, pulsad el icono del lápiz) y completad cada apartado con **vuestras cifras**, sacadas de las celdas ya ejecutadas:

    | Apartado | Qué se escribe | De dónde sale |
    |---|---|---|
    | 1 · Resumen para el gerente (máx. 5 líneas) | ¿Se puede usar el fichero tal cual? ¿Qué fracción de filas necesita corrección? ¿Qué es lo más grave? | Pasos 2 y 3 |
    | 2 · Tabla de defectos | 6 o más filas, con los **tres más graves en negrita** | Paso 2 |
    | 3 · Antes y después | Una tabla pequeña: filas 1545 → 1500, duplicados 45 → 0, valores de `canal` 9 → 4 y de país 12 → 8, y los nulos que cambian | Paso 3 |
    | 4 · *Pipeline* y modelo de referencia | Columnas numéricas y de texto; qué va **dentro** del *pipeline* (imputar, escalar, codificar) y qué **antes** (las reglas fijas de `limpiar_reservas`); la frase con media ± desviación | Pasos 3 y 4 |
    | 5 · Preguntas para el cliente | Al menos 3, con lo que haréis mientras no respondan | Paso 2 |
    | 6 · IA responsable | Ejemplos del dataset (ver el punto 2) | Punto 2 |
    | 7 · Cómo reproducirlo | Versiones de Python y librerías, orden de ejecución, ficheros | Punto 3 |

    **Para el nivel mínimo** bastan los apartados 1, 2 y 3. **Para el estándar**, completad también el resto. La tabla del apartado 3 se escribe a mano con los números que salieron en el paso 3, por ejemplo:

    ```text
    | | Antes | Después |
    |---|---|---|
    | Filas | 1545 | 1500 |
    | Duplicados | 45 | 0 |
    | Valores distintos de `canal` | 9 | 4 |
    ```

2. **Responder a la IA responsable con datos.** Las preguntas son: ¿qué pasa si el país de origen se imputa mal? ¿Podría el modelo discriminar por nacionalidad? ¿Hay columnas que no deberían usarse? Para contestar con números, celda nueva:

    ```python
    print(limpia.groupby("pais_origen")["cancelada"].agg(["mean", "count"]).round(2))
    print(limpia["pais_origen"].isna().sum(), round(limpia["pais_origen"].isna().mean(), 3))
    ```

    Qué hace cada línea:

    - `limpia.groupby("pais_origen")`: agrupa las reservas por país.
    - `["cancelada"].agg(["mean", "count"])`: para cada grupo, la proporción de canceladas (`mean`) y cuántas reservas hay (`count`).
    - `.isna().sum()` y `.isna().mean()`: cuántas reservas no tienen país y qué parte del total son.

    Con estas cifras podéis escribir, por ejemplo: «Italia cancela mucho más (0,60 sobre 77 reservas) que Países Bajos (0,37 sobre 75). Faltan 112 países (7,5 %); el imputador pondría `ES`, el más frecuente, y mezclaría reservas de otros países. Si el modelo usa el país, podría tratar distinto a quien reserva desde un lugar concreto». Decid también qué columnas dejaríais fuera (por ejemplo `id_reserva`) y por qué.

3. **Escribir el README.** En la carpeta `sprint-06/` del repositorio, abrid `README.md` y pulsad el icono del lápiz. Cuatro cosas, en pocas líneas: qué hace el cuaderno; cómo ejecutarlo y en qué orden (*abrir en Colab y ejecutar de arriba abajo*); las versiones; y quién hizo qué y **qué le pedisteis a la IA y qué revisasteis**. Las versiones salen de esta celda, que ejecutáis en el cuaderno:

    ```python
    import sys, pandas, sklearn
    print(sys.version, pandas.__version__, sklearn.__version__)
    ```

    Qué hace cada línea:

    - `import sys, pandas, sklearn`: trae los tres módulos para preguntarles su versión.
    - `print(sys.version, pandas.__version__, sklearn.__version__)`: escribe la versión de Python, la de pandas y la de scikit-learn. Copiadlas tal cual a vuestro README. Salen otras en cada ordenador, y eso es normal.

4. **Reiniciar y ejecutar todo.** En Colab, *Entorno de ejecución → Reiniciar y ejecutar todo* y confirmad. Mirad hasta el final que ninguna celda muestre un error en rojo. Si falla, hay celdas que dependen de un orden: arreglad antes de seguir y repetid.

5. **La revisión con la rúbrica (5 minutos).** La hace una persona que **no escribió** esa parte. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md): ejecutar el cuaderno según el README, leer el informe como el gerente, mirar el código (¿algún `fit` usa el *test*?), poner un nivel y apuntar el resultado en la sección «Revisión con la rúbrica» del final del informe. Es una tabla con un nivel de 1 a 4 por criterio y **una frase de prueba** (lo que ha comprobado), más «Lo primero que mejoraríamos». Si hay tiempo, arreglad lo más fácil; lo demás queda como mejora. Si sobran minutos, empezad el extra.

**Qué deberíais ver.** `informe_calidad.md` con todos los apartados rellenos y la sección «Revisión con la rúbrica» completa, un `README.md` con los comandos y las versiones, y el cuaderno ejecutándose de arriba abajo sin errores. La celda del punto 2 escribe, aproximadamente, `IT 0.60 77`, `NL 0.37 75`, `ES 0.45 388` y, en la segunda línea, `112 0.075`. La de las versiones escribe una línea con Python, pandas y scikit-learn (en Colab serán las suyas).

**Hecho cuando:** otra persona podría repetir el cuaderno siguiendo solo el README, y el informe tiene anotados el nivel y la prueba de cada criterio.

**Después, 35 minutos de entrega, review y retro** (también el día 2):

- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) en Colab, *Archivo → Descargar → Descargar .ipynb* (después de *Reiniciar y ejecutar todo*); (2) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-06`**; (3) *Add file → Upload files* y arrastrad el fichero; (4) escribid un mensaje corto y pulsad **Commit changes**. Los nombres, **en minúsculas y sin espacios**; el CSV va a `data/` solo si aún no está. Un reparto posible: la persona A sube `informe_calidad.md` («Añado informe de calidad»), la B sube `reto_S06.ipynb` («Añado cuaderno»), la C actualiza `README.md` («Completo el README»).
- **La autoevaluación.** Cada persona copia [la plantilla](../2_Entregar/autoevaluacion_y_coevaluacion.md) (botón **Raw**), la rellena y la sube a `sprint-06/` como `autoevaluacion_nombre.md`; la coevaluación va dentro del mismo fichero.
- **La review (5 minutos por equipo).** Enseñad: (1) la tabla de defectos, los 3 más graves y por qué; (2) el cuaderno corriendo desde cero; (3) la métrica del *baseline* frente al modelo tonto.
- **La retro.** Pensad: ¿qué defecto nos costó más encontrar? ¿Qué decisión de limpieza discutimos más? ¿Qué haríamos distinto con el siguiente fichero del cliente?

**Qué deberíais ver.** En la carpeta `sprint-06` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**), con *commits* de personas distintas en el historial (el icono del reloj).

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Al *Reiniciar y ejecutar todo* sale un error y se para | Una celda depende de otra que está más abajo o que falla. | Leed el error de la **primera** celda en rojo, corregidla y repetid. |
| `NameError: name 'limpia' is not defined` | La celda de la limpieza no se ha ejecutado antes de esta. | Ejecutad desde arriba con *Reiniciar y ejecutar todo*. |
| `KeyError: 'pais_origen '` | El nombre de la columna lleva un espacio o una errata. | Copiadlo de `limpia.columns`. |
| El archivo aparece fuera de `sprint-06/` | Se subió desde la raíz del repositorio. | Entrad primero en `sprint-06` y repetid la subida; el de la raíz se borra desde el lápiz o los tres puntos del archivo. |
| La tabla del informe se ve rota en *Preview* | Falta una `\|` en alguna fila o hay un salto de línea dentro de una celda. | Cada fila, en una sola línea y con las mismas `\|` que la cabecera. |
| No sabéis qué nivel poner en la rúbrica | Los niveles están descritos en [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). | Leed la fila del criterio, elegid el nivel cuyo texto se cumple **entero** y escribid la prueba. |

<!--nav-->
---

[← Paso 4](Reto_Sprint_06_paso_4.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_06.md)
<!--/nav-->
