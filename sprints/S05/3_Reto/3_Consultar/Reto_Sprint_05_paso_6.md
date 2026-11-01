# Paso 6 · Responder al cliente en 150 palabras, reiniciar y revisar (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 6 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md)
<!--/nav-->

1. Escribir la respuesta al cliente y contar las palabras.
2. Reiniciar el cuaderno y ejecutarlo todo de arriba abajo.
3. Pedir a alguien que no escribió esa parte que lo revise con la rúbrica y anotar el resultado.

**Cómo se hace**
- **La respuesta** contesta **cuatro cosas**, para una persona que no es técnica: (1) **qué encontráis**, con cifras e incertidumbre, para la temperatura y para los festivos; (2) **qué recomendáis**, algo que el cliente pueda hacer con personal o precios; (3) **qué no podéis afirmar** (correlación no es causalidad, el mes confunde, datos sintéticos de un solo alojamiento); (4) **una frase de IA responsable**, por ejemplo que el modelo no debería fijar precios sin revisión humana. Escribidla en la celda de texto de la sección 6. Contad las palabras (`len(texto.split())`); si pasa de 150, se recorta. **Toda cifra sale de vuestro cuaderno.**
- **Reiniciar.** En Colab: *Entorno de ejecución → Reiniciar y ejecutar todo*. Si algo falla, corregidlo antes de entregar. Marcad también la lista de la sección 7 del cuaderno.
- **Dos celdas de texto al final del cuaderno.** «Uso de IA»: qué pedisteis, qué comprobasteis y qué cambiasteis. «Revisión con la rúbrica»: copiad y rellenad esto, siguiendo los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md):

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

**Qué deberíais ver.** El cuaderno entero ejecutado sin errores y con los cuatro puntos de control superados, una respuesta de 150 palabras o menos y las dos celdas finales rellenas.

**Hecho cuando:** *Reiniciar y ejecutar todo* funciona sin errores, la respuesta cumple las cuatro preguntas y la «Revisión con la rúbrica» tiene un nivel y una frase de prueba por criterio.

**Después, 40 minutos de entrega, review y retro** (comparten tiempo con el Sprint 4):
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) en Colab, *Archivo → Descargar → Descargar .ipynb* (después de *Reiniciar y ejecutar todo*) y descargad también `turisdata_reto.db` desde el panel de archivos; (2) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-05`**; (3) *Add file → Upload files* y arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace: repartid las subidas entre personas (por ejemplo, una sube el cuaderno y otra la base de datos). Nombres de archivo sin espacios ni tildes. El CSV va a `data/` solo si aún no está.
- **La autoevaluación.** Cada persona rellena y sube la suya a `sprint-05/`; la coevaluación va dentro del mismo fichero.
- **La review (5 minutos por equipo).** Enseñad: (1) la pregunta y la base de datos; (2) cómo converge vuestro descenso del gradiente y su comparación con la librería; (3) el resultado clave con su intervalo; (4) cómo habéis distinguido lo que los datos muestran de lo que no pueden demostrar; (5) la recomendación al cliente.

**Qué deberíais ver.** En la carpeta `sprint-05` del repositorio, el cuaderno, la base de datos y una hoja de autoevaluación por persona (**2 + N**), con *commits* de personas distintas en el historial (el icono del reloj).

<!--nav-->
---

[← Paso 5](Reto_Sprint_05_paso_5.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_05.md)
<!--/nav-->
