# Paso 6 · Redactar el informe (día 2, 15 minutos)

<!--nav-->
> Sprint 3 · Reto «Primer modelo en producción» · paso 6 de 6 · [Ficha del reto](Reto_Sprint_03.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_03_una_pagina.md)
<!--/nav-->

1. Crear `informe_modelo.md` a partir de la plantilla y rellenar los apartados 1 a 5 con lo que anotasteis en los pasos 1 a 5.
2. Escribir los riesgos de IA responsable (apartado 6) y la recomendación al cliente (apartado 7).
3. Pedir a alguien que no escribió esa parte que lo revise con la rúbrica, y subir el informe y la captura de cierre.

**En sencillo.** Este paso no se programa: se **cuenta** lo que habéis hecho a un directivo que no sabe de modelos. Es como volver de una consulta médica y explicárselo a la familia: hay que decir qué se hizo, qué salió, qué se recomienda y qué no se sabe todavía. Casi todo el informe es copiar con orden lo que ya tenéis anotado; lo nuevo son los riesgos y la recomendación. En el bloque del reto tenéis 15 minutos para dejarlo montado; lo demás se remata en el bloque de entrega y, si hace falta, en casa esa tarde. No hace falta saber nada técnico más.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Informe** | El documento único que entregáis al cliente: modelo, llamada a la API y recursos y costes, en 4 páginas como máximo. |
| **Riesgo de IA responsable** | Algo que puede salir mal para las personas o para el negocio si se usa el modelo sin cuidado. |
| **Medida** | Lo que hacéis para que ese riesgo sea menor. Un riesgo sin medida no cuenta. |
| **Recomendación** | Qué debe hacer el cliente con una alerta y hasta dónde puede fiarse del modelo. |
| **Revisión con la rúbrica** | Una persona que no escribió esa parte la lee como el cliente, pone un nivel de 1 a 4 a cada criterio y apunta una frase que lo demuestra. |
| **Commit changes** | El botón verde de GitHub que guarda lo que habéis escrito. Sin él no se guarda nada. |

**Cómo se hace**

1. **Crear el informe y repartirlo.** Abrid la [plantilla del informe](../1_Trabajar/plantillas/plantilla_informe_modelo.md), pulsad **Raw**, seleccionad todo (`Ctrl + A`) y copiad (`Ctrl + C`). En el repositorio del equipo, carpeta `sprint-03/`: **Add file → Create new file**, nombre `informe_modelo.md`, pegad (`Ctrl + V`) y **Commit changes**. La guía [subir a GitHub sin instalar nada](../../../../material/5.%20Como_entregar_en_GitHub.md) lo explica con capturas. Repartid los apartados entre las personas; para no pisaros, cada una escribe el suyo en la hoja del equipo y **una sola persona** lo pasa al fichero.

2. **Rellenar los apartados 1 a 5.** Sustituid cada `______` por lo anotado:

    | Apartado | Se rellena con lo anotado en… | Qué lleva |
    |---|---|---|
    | 1 · Problema, datos y métrica | Pasos 1 y 2 | La frase del cliente, el porcentaje de cancelaciones, las columnas excluidas con su razón y la métrica elegida |
    | 2 · Modelos y umbral | Pasos 2 y 3 | Partición, tres modelos con sus notas, vuestros importes con su razón, umbral, costes y la frase para el directivo |
    | 3 · Qué pesa y cómo repetirlo | Pasos 2 y 4 | Tres variables que pesan más, versión, preset, límite de tiempo, semilla y partición |
    | 4 · Llamada a la API | Paso 4 | El texto de la salida del apartado 10, tal cual, y qué significa |
    | 5 · Recursos y costes | Paso 5 | La tabla de recursos, la captura de cierre y la frase sobre la plataforma de pago |

    **Todo número sale de vuestro cuaderno**, no de la plantilla ni de la guía. Al terminar no debe quedar ningún `______` ni ninguna nota en cursiva.

3. **Escribir los riesgos (apartado 6).** Hacen falta **al menos dos**, cada uno con lo que veis en vuestro caso y una medida. Los habituales de este reto: que los datos son sintéticos (inventados) y no valen para decidir en un hotel real; que una alerta falsa moleste a un cliente; que el trato sea desigual por canal o país; que el modelo envejezca; que los importes sean supuestos vuestros. Que sea **vuestro** significa que «Qué vemos» lleva un dato de vuestro cuaderno. Ejemplo de redacción (no lo copiéis): «Alertas falsas que molestan | con nuestro umbral, ___ de cada 10 alertas son falsas (paso 3) | una persona decide antes de contactar y el mensaje es opcional y amable». Qué no vale: «cuidado con los sesgos», que serviría para cualquier proyecto. Para subir de nivel: mirad el porcentaje de cancelaciones por canal del paso 1; si es muy distinto, las alertas caerán más en unos canales que en otros, y decid qué haríais.

4. **Escribir la recomendación (apartado 7).** Completad tres cosas: qué hace una persona del equipo de reservas cuando llega una alerta (por ejemplo, llamar o escribir al cliente para confirmar: **la alerta no cancela ni cambia nada sola**), para qué sirve el modelo y para qué no, y qué debería validar TurisData antes de fiarse de los euros (vuestros importes son hipótesis). Qué no vale: «hay que usar el modelo».

5. **Revisar con la rúbrica (unos 10 minutos).** Una persona que **no escribió esa parte** lee el informe con la [rúbrica](../2_Entregar/entrega_y_rubrica.md), como si fuera el director de TurisData: ¿están las tres partes y cabe en 4 páginas?, ¿se partió por fecha y se dicen las columnas excluidas?, ¿se ve la petición y la respuesta de la API sin claves?, ¿sabría repetir el experimento sin preguntar a nadie?, ¿sabe qué hacer con una alerta? Después pone un nivel (1 a 4) a cada criterio **con una frase que lo demuestre** («2 · la partición es al azar») en la tabla del final y corrige lo más fácil. Sin frase, el nivel no vale.

6. **Subir.** Guardad el informe con **Commit changes**. Subid la captura: **Add file → Upload files**, arrastrad `captura_cierre.png` a `sprint-03/` y **Commit changes**. Si preferís entregar un PDF (exportado desde Word o Google Docs), subid `informe_modelo.pdf` en lugar del `.md`, con la captura pegada dentro; un solo informe, no los dos. Cada persona sube además su autoevaluación en el bloque de entrega. El máximo son **4 páginas**; la tabla «Revisión con la rúbrica» no cuenta. Si os pasáis, recortad antes de subir y no peguéis tablas enteras del cuaderno.

**Qué deberíais ver.** En `sprint-03/` del repositorio: `informe_modelo.md` con los siete apartados y la tabla de revisión rellena, y `captura_cierre.png`. Al abrir el informe en GitHub, las tablas se ven como tablas y no queda ningún `______`. En el apartado 6, dos filas con su medida; en el 7, una frase que diga qué hacer con una alerta.

**Hecho cuando:** el informe está subido con los siete apartados rellenos, una persona que no lo escribió lo ha revisado con la rúbrica y la captura de cierre está en `sprint-03/`.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Al guardar, GitHub dice que el archivo cambió mientras editabais | Dos personas editaron `informe_modelo.md` a la vez. | Copiad lo vuestro a la hoja del equipo, volved a abrir el fichero y pegadlo. Que escriba una sola persona. |
| En la vista previa, las tablas salen como texto con barras | Se borró alguna barra vertical o la línea de guiones. | Comparadlo con la [plantilla](../1_Trabajar/plantillas/plantilla_informe_modelo.md) y recuperad las barras. |
| Se pasa de 4 páginas | Hay tablas del cuaderno enteras o texto repetido. | Dejad solo tres modelos, las dos frases del directivo y los datos que pide cada apartado. |
| Los riesgos podrían valer para cualquier proyecto | Falta un dato vuestro en «Qué vemos». | Añadid una cifra de vuestro cuaderno o de vuestra tabla de costes. |
| Quien revisa no sabe qué nivel poner | Hay que leer el texto de cada nivel, no adivinar. | Poned el nivel cuyo texto se cumple **entero**; si se cumple a medias, el de abajo. |
| El `.png` es muy grande o no se sube | La captura pesa demasiado. | Recortad la imagen o haced la captura de menos área. |
| Falta alguna cifra que no anotasteis | Se cerró Colab antes de apuntarla. | Abrid la copia del cuaderno guardada en Drive en el paso 5 y copiadla de ahí. |

<!--nav-->
---

[← Paso 5](Reto_Sprint_03_paso_5.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_03.md)
<!--/nav-->
