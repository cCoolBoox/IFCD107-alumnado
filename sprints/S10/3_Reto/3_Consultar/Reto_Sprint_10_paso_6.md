# Paso 6 · Informe, revisión y entrega (día 2, 35 minutos)

<!--nav-->
> Sprint 10 · Reto «¿Vale la pena la red?» · paso 6 de 6 · [Ficha del reto](Reto_Sprint_10.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_10_una_pagina.md)
<!--/nav-->

1. Escribir el informe de 1 página, con la recomendación al principio.
2. Rellenar el README de `sprint-10/`.
3. Pedir a alguien que no escribió esa parte que revise con la rúbrica y anote el resultado al final del informe.
4. Subir los tres ficheros del equipo a `sprint-10/`, y cada persona su autoevaluación.

**En sencillo.** Es el paso de **cerrar el trabajo**. Primero, contar lo que habéis descubierto como se lo contaríais a la dirección de TurisData: en una página y **empezando por la respuesta**, igual que un titular de periódico («Recomendamos… porque…») y después los detalles que la sostienen. Segundo, comprobar que otra persona puede repetir vuestro cuaderno y que alguien con ojos frescos lo revisa con la rúbrica. Tercero, subir todo al repositorio del equipo desde el navegador. No hay código nuevo. Recordad que un «no compensa» bien demostrado es tan válido como un «sí».

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Informe comparativo** | El documento de 1–2 páginas que compara el modelo clásico con la red y termina en una recomendación. |
| **Markdown** (`.md`) | Texto normal con unas pocas marcas: `#` para un título, `**…**` para negrita y barras verticales para las tablas. GitHub lo muestra ya con formato. |
| **Riesgo de IA responsable** | Algo concreto que podría salir mal si se usara el modelo (por ejemplo, datos inventados o un grupo de clientes peor tratado), junto con una **medida** para evitarlo. |
| **README** | La hoja de entrada de la carpeta `sprint-10/`: qué hay, quién lo hizo y cómo se repite. Es lo primero que lee el docente. |
| **Commit** | Cada vez que guardáis un cambio en GitHub con el botón verde **Commit changes**. Queda apuntado con el nombre de quien lo hace. |
| **Rúbrica** | La tabla con la que se evalúa el reto: cuatro criterios, cada uno de 1 a 4. |
| **Reiniciar y ejecutar todo** | Borra la memoria del cuaderno y ejecuta todas las celdas de arriba abajo. Prueba que el cuaderno funciona solo y deja los resultados visibles. |

**Cómo se hace**

1. **Repartir el trabajo.** Cada persona sube lo suyo con su cuenta: así el historial muestra a todo el equipo, que es lo que se evalúa. Un reparto posible: una persona prepara y sube el cuaderno, otra escribe el informe y otra rellena el README. Quien revise con la rúbrica (el punto 5 de esta lista) **no puede ser quien escribió esa parte**.
2. **Escribir el informe** `informe_comparativo.md`. Abrid [`plantilla_informe_comparativo.md`](../1_Trabajar/plantillas/plantilla_informe_comparativo.md), pulsad *Raw*, copiad el texto y, en la carpeta `sprint-10` del repositorio, usad *Add file → Create new file* con el nombre `informe_comparativo.md` y pegadlo. Tiene seis partes **en este orden**; sustituid lo que va entre corchetes por vuestras cifras y frases.


    De dónde sale cada parte:

    | Parte | Qué escribís | De dónde sale |
    |---|---|---|
    | 1. Pregunta y respuesta | Una frase: «Recomendamos mantener / cambiar a… porque…» | Vuestra decisión del paso 5 |
    | 2. Resultados | AUC, AP y F1 de la tabla de la sección 6; media ± desviación del MLP; el intervalo del bootstrap | Pasos 2 y 5 |
    | 3. Curva comentada | Qué se ve y vuestra frase de diagnóstico | Paso 4 |
    | 4. Coste | Tiempo, complejidad y explicabilidad | Paso 5 |
    | 5. Riesgos de IA responsable | Al menos dos, específicos, cada uno con su medida | Vuestra reflexión |
    | 6. Límites | Qué no sabemos y qué haríamos después | Vuestra reflexión |

    Un ejemplo de cómo suena la parte 1 (con huecos; si vuestros números dicen otra cosa, escribid otra cosa): *«Recomendamos mantener el boosting porque la red no lo mejora de forma clara en la prueba (diferencia de AUC de [X], con un intervalo que incluye el 0), tarda [N] veces más en entrenar y es más difícil de explicar»*.

    Los riesgos tienen que ser **específicos de este caso**, no frases generales como «la IA puede tener sesgos». Dos ejemplos del tipo que se pide: *«Riesgo: los datos son sintéticos (inventados), así que el resultado puede no valer con reservas reales. Medida: repetir la comparación con datos reales del hotel antes de cambiar nada»*; *«Riesgo: hay 138 reservas sin país (el cuaderno las trata como un país más) y el modelo puede rendir peor con los países poco frecuentes. Medida: medir el AUC por país antes de usarlo»*. Pensad también en el umbral y en lo que cuesta equivocarse: cancelar de más o de menos provoca *overbooking* o habitaciones vacías.

    **No vale:** un informe sin recomendación, cifras escritas de memoria o copiadas de lo que dijo una IA (todas salen de vuestro cuaderno), ni riesgos genéricos.

3. **Guardar la curva (opcional).** Si queréis ver la curva dentro del informe, guardad la imagen de la gráfica del cuaderno con el nombre `curvas_aprendizaje.png` (clic derecho sobre la gráfica → *Guardar imagen como…*) y subidla a `sprint-10/`. Añadid también la línea de **uso de la IA** (parte final de la plantilla): qué pedisteis, qué comprobasteis a mano y qué cambiasteis.
4. **Rellenar el README.** Abrid `sprint-10/README.md` en el repositorio del equipo → icono del lápiz y completad los cuatro campos que ya trae. Así puede quedar:

    ```text
    # Sprint 10 · Entregable

    - **Reto:** ¿Vale la pena la red?
    - **Qué se entrega:** el cuaderno `reto_vale_la_pena.ipynb` y el informe `informe_comparativo.md`
    - **Quién hizo qué:**
      - Persona 1 (@usuario): cuaderno y ejercicios 1 y 2
      - Persona 2 (@usuario): variantes, diagnóstico y ejercicio 3
      - Persona 3 (@usuario): comparación, ejercicio 4 e informe
    - **Cómo reproducirlo:** abrir el cuaderno en Colab y ejecutar de arriba abajo (*Entorno de ejecución → Reiniciar y ejecutar todo*)
    ```

    Después pulsad **Commit changes**.

5. **La revisión con la rúbrica (5 minutos).** Quien revisa **no escribió esa parte**. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md): reiniciar y ejecutar el cuaderno, leer el informe como si fuera el cliente, mirar el cuaderno, poner un nivel de 1 a 4 por criterio **con una frase de prueba** y apuntar el resultado. Rellena la sección «Revisión con la rúbrica» que la plantilla trae al final del informe:


    Un ejemplo de frase de prueba: «3 · reinicia y ejecuta sin errores y el AUC coincide con el informe, pero falta explicar el coste». Sin frase, el nivel no vale. Si hay tiempo, arreglad lo más fácil; lo demás queda como «lo primero que mejoraríamos». Si sobran minutos, empezad un extra (la variante de precio, o guardar el modelo y recargarlo).

6. **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). Para el cuaderno: en Colab, *Entorno de ejecución → Reiniciar y ejecutar todo*, mirad que ninguna celda dé error y después *Archivo → Descargar → Descargar .ipynb*; renombrad el archivo descargado a `reto_vale_la_pena.ipynb` (minúsculas, sin espacios ni tildes). En el repositorio del equipo: (1) **entrad primero en la carpeta `sprint-10`**; (2) *Add file → Upload files*; (3) arrastrad el fichero; (4) escribid un mensaje corto, por ejemplo `Añado el cuaderno con los resultados`, y pulsad **Commit changes**. El informe también se puede crear directamente con *Add file → Create new file*. Cada subida es un *commit* con el nombre de quien la hace, así que repartid las subidas. El CSV va a `data/` solo si aún no está.
7. **La autoevaluación.** Cada persona copia la plantilla de [autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md), la guarda con su nombre (`autoevaluacion_nombre.md`, sin espacios ni tildes), la rellena y la sube a `sprint-10/`. La coevaluación va dentro del mismo fichero y se hace durante la *review*.

**Qué deberíais ver.** En la carpeta `sprint-10` del repositorio, el cuaderno con sus resultados visibles, el informe, el README relleno y una hoja de autoevaluación por persona (**3 + N**); y en el historial (el icono del reloj), *commits* de personas distintas.

**Hecho cuando:** otra persona podría repetir el cuaderno siguiendo solo el README, el informe termina con «Recomendamos… porque…» y trae la sección «Revisión con la rúbrica» rellena, y los ficheros están en `sprint-10/`.

**Después, en la entrega y la review:** cada persona rellena y sube su autoevaluación y coevaluación a `sprint-10/`, y el equipo enseña, en unos 5 minutos, la tabla comparativa, una curva de aprendizaje comentada y la recomendación en una frase, con el coste y los riesgos.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| El archivo ha caído en la raíz del repositorio y no en `sprint-10/` | Se subió sin entrar antes en la carpeta. | Abrid el archivo → icono del lápiz → en la ruta de arriba escribid `sprint-10/` delante del nombre → **Commit changes**. Lo mueve. |
| El archivo no aparece tras subirlo | Falta pulsar el botón verde **Commit changes**: sin él no se guarda nada. | Volved a subirlo y pulsadlo. |
| No veis el botón *Add file* | No sois colaboradores del repositorio o no habéis aceptado la invitación. | Pedid a quien creó el repositorio que os añada y aceptad la invitación. |
| El cuaderno subido no muestra gráficas ni cifras | Se descargó sin haberlo ejecutado. | *Entorno de ejecución → Reiniciar y ejecutar todo* y descargad de nuevo el `.ipynb`. |
| *Reiniciar y ejecutar todo* se para en una celda con `...` | Falta rellenar el hueco de un ejercicio. | Completad los ejercicios 1 a 4, en orden, y repetid. |
| Aviso de conflicto al guardar | Dos personas editaron el mismo archivo a la vez. | Recargad la página y repetid vuestro cambio sobre la versión actual. |
| El informe termina en cifras y no dice qué hacer | Falta la recomendación. | Añadid, al principio, «Recomendamos… porque…». |

<!--nav-->
---

[← Paso 5](Reto_Sprint_10_paso_5.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_10.md)
<!--/nav-->
