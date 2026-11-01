# Paso 6 · Responder al cliente en 150 palabras, reiniciar y revisar (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 6 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md)
<!--/nav-->

1. Escribir la respuesta al cliente y contar las palabras.
2. Reiniciar el cuaderno y ejecutarlo todo de arriba abajo.
3. Pedir a alguien que no escribió esa parte que lo revise con la rúbrica y anotar el resultado.

**En sencillo.** Es el paso de **cerrar el trabajo**. Primero, contestar al cliente: una persona del alojamiento que no sabe de estadística necesita leer en 150 palabras qué habéis encontrado, qué le recomendáis y de qué no os fiáis. Después, comprobar que el cuaderno **funciona de principio a fin** (si alguien lo abre mañana y lo ejecuta, sale lo mismo) y que otra persona del equipo, con ojos frescos, lo revisa. No hay código nuevo, salvo una línea para contar palabras.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Reiniciar y ejecutar todo** | Borra la memoria del cuaderno y ejecuta todas las celdas de arriba abajo. Es la prueba de que no depende de nada «escondido». |
| **Reproducibilidad** | Que cualquiera, ejecutando el cuaderno, obtenga los mismos resultados. |
| **Rúbrica** | La tabla con la que se evalúa el reto: cuatro criterios, cada uno de 1 a 4. |
| **Comillas triples** (`"""…"""`) | Sirven para guardar un texto de varias líneas en una variable. |
| **`len` y `.split()`** | `.split()` corta un texto en palabras y `len(…)` cuenta cuántas hay. |

**Cómo se hace**

1. **Escribir la respuesta.** En la celda de texto de la sección «6 · Respuesta al cliente» (doble clic para editarla). Contestad **cuatro cosas**, para una persona que no es técnica:
    1. **Qué encontráis**, con cifras e incertidumbre, para la temperatura y para los festivos. *Molde:* «Con los datos de tres años, por cada grado más de temperatura la ocupación [sube/baja] [X] puntos (entre [A] y [B]), una vez descontado el mes. Los festivos suman unos [X] puntos…».
    2. **Qué recomendáis**, algo que el cliente pueda hacer con el personal o los precios. *Molde:* «Recomendamos…».
    3. **Qué no podéis afirmar**: correlación no es causalidad, el mes confunde, los datos son sintéticos y de un solo alojamiento. *Molde:* «No podemos afirmar que… porque…».
    4. **Una frase de IA responsable**, por ejemplo que el modelo no debería usarse para fijar precios sin revisión humana.

    **Toda cifra sale de vuestro cuaderno**: nada de números de memoria ni de lo que diga un asistente de IA.

2. **Contar las palabras.** Pegad la respuesta dentro de las comillas de esta celda de código y ejecutadla:

    ```python
    texto = """Pegad aquí vuestra respuesta al cliente."""
    print(len(texto.split()), "palabras")
    ```

    Si sale más de 150, **recortad**: quitad adornos y dejad cifras, recomendación y límites.

3. **Reiniciar y ejecutar todo.** Arriba, *Entorno de ejecución → Reiniciar y ejecutar todo* (y confirmad). Tardará un poco. Mirad **hasta el final** que ninguna celda muestre un error en rojo. Si alguna falla, corregidla **antes de entregar** y repetid. Marcad también la lista de la sección 7 del cuaderno.
4. **Dos celdas de texto al final del cuaderno.**

    - **«Uso de IA»:** qué le pedisteis a la IA, qué comprobasteis y qué cambiasteis. Si no la usasteis, decidlo. *Molde:* «Le pedí [qué]; comprobé [cómo]; cambié [qué]».
    - **«Revisión con la rúbrica»:** copiad y rellenad esto, siguiendo los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md):

```
## Revisión con la rúbrica
**Revisado por:** (nombre) · **Fecha:** (dd/mm/aaaa)

| Criterio | Nivel (1-4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | | |
| Reproducibilidad | | |
| Análisis y comunicación al cliente | | |
| IA responsable | | |

**Lo primero que mejoraríamos:** (una cosa concreta)
```

    Si no cabe en los 10 minutos, la revisión se hace al empezar la entrega.

5. **La revisión.** La hace una persona que **no escribió** esa parte del cuaderno: lee el cuaderno ya reiniciado, pone un nivel de 1 a 4 en cada criterio y apunta **una frase de prueba** (lo que ha comprobado: «he reiniciado y todo corre»). Después, una mejora concreta para la próxima vez.

**Qué deberíais ver.** El cuaderno entero ejecutado sin errores y con los cuatro puntos de control superados, una respuesta de 150 palabras o menos y las dos celdas finales rellenas.

**Hecho cuando:** *Reiniciar y ejecutar todo* funciona sin errores, la respuesta cumple las cuatro preguntas y la «Revisión con la rúbrica» tiene un nivel y una frase de prueba por criterio.

**Después, 40 minutos de entrega, review y retro** (comparten tiempo con el Sprint 4):
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) en Colab, *Archivo → Descargar → Descargar .ipynb* (después de *Reiniciar y ejecutar todo*) y descargad también `turisdata_reto.db` desde el panel de archivos (clic derecho sobre el archivo → *Descargar*); (2) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-05`**; (3) *Add file → Upload files* y arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace: repartid las subidas entre personas (por ejemplo, una sube el cuaderno y otra la base de datos). Nombres de archivo sin espacios ni tildes. El CSV va a `data/` solo si aún no está.
- **La autoevaluación.** Cada persona rellena y sube la suya a `sprint-05/`; la coevaluación va dentro del mismo fichero.
- **La review (5 minutos por equipo).** Enseñad: (1) la pregunta y la base de datos; (2) cómo converge vuestro descenso del gradiente y su comparación con la librería; (3) el resultado clave con su intervalo; (4) cómo habéis distinguido lo que los datos muestran de lo que no pueden demostrar; (5) la recomendación al cliente.

**Qué deberíais ver.** En la carpeta `sprint-05` del repositorio, el cuaderno, la base de datos y una hoja de autoevaluación por persona (**2 + N**), con *commits* de personas distintas en el historial (el icono del reloj).

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Al *Reiniciar y ejecutar todo* sale un error en una celda y se para | Una celda depende de otra que no está arriba o que falla. | Leed el error de la **primera** celda en rojo; corregidla y repetid. |
| `NameError` justo después de reiniciar | Algo se definió en una celda que ahora está debajo de donde se usa. | Mover la celda arriba, o ejecutar siempre de arriba abajo. |
| `ProgrammingError: Cannot operate on a closed database` | Se ejecutó `con.close()` antes de tiempo. | Ejecutad todo desde arriba con *Reiniciar y ejecutar todo*. |
| El texto da más de 150 palabras | La respuesta es demasiado larga. | Recortad: quedaos con cifra e intervalo, una recomendación, los límites y la frase de IA responsable. |
| No sabéis qué nivel poner en la rúbrica | Los niveles están descritos en [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md). | Leed la fila del criterio y elegid el nivel que describa lo que habéis comprobado; escribid la prueba. |

<!--nav-->
---

[← Paso 5](Reto_Sprint_05_paso_5.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_05.md)
<!--/nav-->
