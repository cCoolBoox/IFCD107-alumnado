# Paso 4 · Cierre, entrega y review (día 3, 40 minutos)

<!--nav-->
> Sprint 12 · Reto «Escuchar al cliente» · paso 4 de 4 · [Ficha del reto](Reto_Sprint_12.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_12_una_pagina.md)
<!--/nav-->

1. Redactar el informe de reseñas, la nota de IA responsable y el `LEEME.md`.
2. Ejecutar todo desde cero y pedir a alguien que no escribió esa parte que lo revise con la rúbrica.
3. Subir los ficheros a `sprint-12/`, cada persona los suyos.
4. Ensayar los 5 minutos de la review.

**Cómo se hace**
- **El informe de reseñas** (2 páginas como máximo). Copiad el texto de la [plantilla](../1_Trabajar/plantillas/plantilla_informe_cliente.md) en un fichero `informe_resenas.md` y rellenad los huecos: resumen para la dirección, sentimiento (para ver el gráfico dentro del informe, escribid la línea `<img src="grafico_resenas.png" width="500">`), temas, **3 recomendaciones que el cliente pueda ejecutar el lunes** y límites. Cada recomendación dice qué, quién y cómo sabremos que funciona. Decid que los datos son sintéticos y que el análisis no entiende la ironía.
- **La nota de IA responsable** (1 página, `nota_ia_responsable.md`). Una lista de riesgos concretos (qué pasa con la pregunta sin respuesta, con datos personales en las reseñas, con un texto que intenta manipular al asistente, con los sesgos) y, para cada uno, qué medida aplicasteis y cómo la medisteis. Si habéis usado una IA para algo, contad qué le pedisteis y qué comprobasteis.
- **El `LEEME.md`** (5 líneas). Qué contiene la carpeta, en qué orden se ejecutan los cuadernos, qué datos necesitan (y dónde están), las versiones de las librerías (`pip list` o `!pip show nombre`) y que usan `SEMILLA = 42`. Al final, añadid esta sección para la revisión:

```
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

- **Ejecutar todo desde cero.** En cada cuaderno, menú *Entorno de ejecución → Reiniciar sesión y ejecutar todo*, sin conexión a internet si es posible. Si falla algo, arreglad el cuaderno **antes** de descargarlo. Descargadlo con *Archivo → Descargar → Descargar .ipynb* (así lleva los resultados guardados). Comprobad que no hay ninguna clave en ningún fichero.
- **La revisión con la rúbrica (15 minutos).** Quien revisa sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) y rellena la sección del `LEEME.md`: un nivel de 1 a 4 por criterio y **una frase de prueba**. Lo más fácil se arregla; lo demás queda como «lo primero que mejoraríamos».
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-12`**; (2) *Add file → Upload files*; (3) arrastrad los ficheros; (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace, así que cada persona sube lo de su parte con su cuenta: la A, `informe_resenas.md`, `grafico_resenas.png` y `resenas.ipynb`; la B, `ocupacion.ipynb`; la C, `asistente_rag.ipynb` y `evaluacion_asistente.csv`; quien lleve la IA responsable y la coordinación, `nota_ia_responsable.md` y `LEEME.md`. Los nombres de archivo, **en minúsculas y sin espacios**. Los cuatro ficheros de datos van a `data/` solo si aún no están.
- **La review (5 minutos por equipo).** Presentad **una cifra, un gráfico y una demo**: cuánto se equivoca la previsión frente al método simple; el tema más criticado y qué haría el cliente; y una pregunta que el asistente responde bien, **la que no sabe** y un ataque frenado. Después, 3 minutos de preguntas.

**Qué deberíais ver.** En la carpeta `sprint-12` del repositorio, los ocho ficheros del equipo y una hoja de autoevaluación por persona (**8 + N**), y en el historial (el icono del reloj), *commits* de personas distintas.

**Hecho cuando:** otra persona podría repetir todo siguiendo solo el `LEEME.md`, la sección «Revisión con la rúbrica» está rellena, cada persona ha subido su autoevaluación y coevaluación, y el equipo ha ensayado su presentación de 5 minutos.

<!--nav-->
---

[← Paso 3](Reto_Sprint_12_paso_3.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_12.md)
<!--/nav-->
