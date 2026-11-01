# Paso 4 · Probar con otro equipo, revisar con la rúbrica y dejarlo listo (día 1, 5 minutos)

<!--nav-->
> Sprint 13 · Reto «Informe visual para dirección» · paso 4 de 4 · [Ficha del reto](Reto_Sprint_13.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_13_una_pagina.md)
<!--/nav-->

1. Pasar la página a otro equipo y preguntar: **«¿Entiendes la decisión en 30 segundos?»**
2. Si no la entienden o entienden otra cosa, reescribir el titular.
3. Pedir a alguien que no escribió esa parte que la revise con la rúbrica y anote el resultado en `informe_visual.md`.

**En sencillo.** Un informe se prueba como una receta: si quien la lee no consigue hacer el plato, el fallo está en la receta, no en quien cocina. Marcos tendrá 10 minutos, así que se hace una prueba de **30 segundos** con alguien que no ha visto vuestra página. Después, una persona de vuestro equipo que **no escribió** esa parte la revisa con una rúbrica (una tabla que dice qué hay que comprobar y qué nota merece) y apunta lo que ha visto. Por último se deja todo listo para subirlo a GitHub. No hace falta programar: se mira, se pregunta, se escribe un par de frases y se descargan dos archivos.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Prueba de los 30 segundos** | Alguien ajeno mira vuestra página medio minuto y dice **con sus palabras** qué decisión entiende. Si no es la vuestra, el mensaje no está claro. |
| **Rúbrica** | La tabla de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md) que describe, para cada criterio, qué significa un 1, un 2, un 3 y un 4. |
| **Nivel y frase de prueba** | El nivel (1 a 4) que ponéis a cada criterio y **una frase** con lo que habéis comprobado. Sin la frase, el nivel no vale. |
| **Revisión** | La hace una persona del equipo que no escribió esa parte, para que mire con ojos nuevos. |
| **Reiniciar y ejecutar todo** | Opción de Colab (menú *Entorno de ejecución*) que borra la memoria del cuaderno y ejecuta todas las celdas de arriba abajo. Si funciona, otra persona podrá repetirlo. |
| **`.ipynb`** | El formato de un cuaderno de Colab. Se descarga con *Archivo → Descargar → Descargar .ipynb*. |
| **Definition of Done** | La lista de comprobación del final de `informe_visual.md`: lo que tiene que cumplirse para dar el trabajo por acabado. |

**Cómo se hace**

1. **La prueba de los 30 segundos.** Buscad a una persona de **otro equipo** y enseñadle la página: el panel (doble clic en `informe_visual_panel.png` en el panel de archivos de Colab, icono de la carpeta 📁) y `informe_visual.md` en la pestaña Preview. Ponedle el reloj a 30 segundos, **sin explicarle nada**, y preguntadle:

    - «¿Entiendes la decisión? Dímela con tus palabras.» Apuntad lo que diga, literal.
    - «¿Hay alguna palabra que no entiendas o una cifra de la que no sepas de dónde sale?»

    Si coincide con vuestro titular, pasasteis la prueba. Hacedlo también al revés: leed la página de ese equipo.

2. **Si no coincide, reescribir el titular (el lector no tiene la culpa).** Mirad qué os ha dicho y qué cambiar:

    | Lo que dice quien lee | Qué falla | Qué hacer |
    |---|---|---|
    | «Que predice cancelaciones» | El titular cuenta qué hace el modelo, no qué hay que hacer | Empezad por un verbo de acción y decid a quién: «Avisar a las reservas de mayor riesgo…» |
    | «No sé qué es el 83%» | Una cifra sin contexto | Decid de qué es parte: «el 83% de las cancelaciones» |
    | «Que el modelo es bueno» | Se queda en la calidad y no hay decisión | Añadid el efecto en euros: «…evitaría unos 16 600 € de pérdidas por cada 1 500 reservas» |
    | «No entiendo AUC» (o «umbral», «F1») | Jerga | Usad la tabla de traducción del paso 3 |

    El titular se cambia en **dos sitios**: en `informe_visual.md` (icono del lápiz, cambiad y **Commit changes**) y en el cuaderno (`TITULAR = "…"` de la celda de parámetros; después, ejecutad otra vez la celda del panel). Que no pase de unos 100 caracteres.

3. **La revisión con la rúbrica.** La hace una persona de vuestro equipo que **no escribió esa parte** de la página. Sigue los cinco pasos de «Cómo se revisa» de [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md), aquí con lo que toca mirar:

    - **Ejecutar** el cuaderno en una pestaña nueva de Colab con *Entorno de ejecución → Reiniciar y ejecutar todo* y comparar el PNG y las cifras con las del informe. Con el modelo de ejemplo salen `AUC en prueba: 0.744 · reservas de prueba: 1500` y `Coste sin modelo: 34,400 € · con modelo: 17,810 € · ahorro: 16,590 €`.
    - **Leer la página como si fuerais Marcos**, con 30 segundos en el reloj. Subrayar toda la jerga y toda cifra de la que no sepáis el origen.
    - **Mirar los gráficos uno a uno:** ¿el título es una conclusión?, ¿los ejes tienen nombre?, ¿las barras empiezan en 0?, ¿se calcula sobre el test?
    - **Poner un nivel (1 a 4) en cada criterio, con una frase de prueba.** Se pone el nivel de la columna cuyo texto **se cumple entero**; si algo se cumple a medias, es el nivel de abajo; **0** es que no se entregó nada de ese criterio.
    - **Apuntar el resultado** y corregir lo más fácil de arreglar; lo demás, como mejora.

    Para el nivel 3 (estándar), lo que comprobáis en cada criterio es esto:

    | Criterio | Para un 3 se cumple entero… |
    |---|---|
    | Corrección técnica | Cuatro gráficos sobre el test, barras desde 0, sin 3D y 3–4 colores con sentido; umbral y costes explicados; el ahorro del gráfico coincide con el del cuaderno |
    | Reproducibilidad | Otra persona hace *Reiniciar y ejecutar todo* y obtiene el mismo PNG y las mismas cifras; el pie indica datos, modelo, umbral y semilla |
    | Análisis y comunicación al cliente | Titular-decisión, **todos** los títulos con conclusión, tres viñetas sin jerga; cifras del texto = cifras del gráfico; otro equipo entiende la decisión en 30 segundos |
    | IA responsable | Un riesgo específico con su medida, qué se pidió a la IA y qué se revisó, y se dice que los datos son sintéticos |

    El resultado se escribe en la sección **«Revisión con la rúbrica»**, al final de `informe_visual.md` (abrid el archivo en GitHub, icono del lápiz). Esa parte va debajo de la página y no se proyecta. Sustituid cada `<…>` por vuestro texto sin tocar las barras `|`. Un ejemplo, con las cifras del modelo de ejemplo:

    ```text
    **Revisado por:** Luis · **Fecha:** la de hoy, en formato dd/mm/aaaa

    | Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
    |---|---|---|
    | Corrección técnica | 3 | Los cuatro gráficos salen de X_test, con barras desde 0 y sin 3D; el ahorro del gráfico (16,590 €) coincide con el de la celda de cálculos. |
    | Reproducibilidad | 3 | Reinicio y ejecuto todo y sale el mismo PNG y AUC en prueba 0.744; el pie dice datos, modelo, umbral y semilla. |
    | Análisis y comunicación al cliente | 2 | Otro equipo entendió la decisión en 30 segundos, pero la viñeta 3 todavía dice «AUC» sin explicarlo. |
    | IA responsable | 3 | Hay un riesgo concreto con su medida, se dice qué se pidió a la IA y que los datos son sintéticos. |

    **Lo primero que mejoraríamos:** explicar «AUC» en la viñeta 3 con la frase de la tabla de jerga.
    ```

    Si no da tiempo, la revisión se acaba al empezar la franja de entrega.

4. **Dejarlo listo para subir.** Una persona hace estas cuatro cosas:

    - **Repasar la lista de comprobación** del final de `informe_visual.md` (la «Definition of Done»): cambiad `[ ]` por `[x]` en lo que se cumpla y arreglad lo que no.
    - **Reiniciar y ejecutar todo** en el cuaderno (*Entorno de ejecución → Reiniciar y ejecutar todo*). Así el PNG que descargaréis es el de la última versión.
    - **Descargar el cuaderno:** *Archivo → Descargar → Descargar .ipynb*. Debe llamarse `informe_visual.ipynb`: si se llama `Copia de …`, cambiad el título del cuaderno en Colab (arriba a la izquierda) y descargadlo otra vez.
    - **Descargar el PNG:** en el panel de archivos (📁), clic derecho sobre `informe_visual_panel.png` → *Descargar*. No se edita a mano.

**Qué deberíais ver.** Una página que otro equipo entiende, la sección «Revisión con la rúbrica» rellena con un nivel y una frase de prueba por criterio, y, tras la subida, en la carpeta `sprint-13` del repositorio, los tres ficheros del equipo y una hoja de autoevaluación por persona (**3 + N**: un equipo de 3 personas sube 6).

**Hecho cuando:** otro equipo ha dicho la misma decisión que vosotros, la revisión con la rúbrica está anotada y los ficheros están listos para subir a `sprint-13/`.

**Después, en la franja de entrega y review:**
- **Subir los ficheros (la vía del curso, desde el navegador).** Seguid [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): (1) abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-13`**; (2) *Add file → Upload files*; (3) arrastrad `informe_visual_panel.png` e `informe_visual.ipynb` (`informe_visual.md` ya está allí si lo creasteis en GitHub en el paso 3; si lo hicisteis en vuestro ordenador, arrastradlo también); (4) escribid un mensaje corto y pulsad **Commit changes**. Cada subida es un *commit* con el nombre de quien la hace, así que repartidlas entre personas. Los nombres de archivo, **en minúsculas y sin espacios**. Al recargar `informe_visual.md`, el panel ya se ve.
- **El README del sprint.** La guía de entrega pide dejar relleno `sprint-13/README.md` (abridlo y pulsad el icono del lápiz): qué se entrega, quién hizo qué y cómo reproducirlo («abrir `informe_visual.ipynb` en Colab y ejecutar de arriba abajo»).
- **La autoevaluación y coevaluación.** Cada persona sube **la suya** a `sprint-13/`: copia con *Raw* el texto de [autoevaluación y coevaluación](../2_Entregar/autoevaluacion_y_coevaluacion.md), entra en `sprint-13`, *Add file → Create new file*, la llama `autoevaluacion_nombre.md` (su nombre, en minúsculas, sin espacios ni tildes), sustituye los `……` sin borrar las barras `|` y pulsa **Commit changes**. La coevaluación va **dentro del mismo fichero**.
- **La review.** Cada equipo proyecta su página 30 segundos. **El resto de la clase dice la decisión que entiende**; si no coincide con la del equipo, el mensaje no está claro. Se comparan los titulares y se elige el más claro.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| Quien lee entiende una decisión distinta de la vuestra | El titular no enuncia la decisión | Reescribid el titular con la tabla del punto 2, no el lector |
| En `informe_visual.md`, el panel sale como una imagen rota | `informe_visual_panel.png` aún no está en `sprint-13`, o su nombre no coincide | Subidlo a `sprint-13` con el nombre exacto, en minúsculas |
| Al *Reiniciar y ejecutar todo* sale `NameError` en una celda que antes funcionaba | Esa celda está colocada **antes** de la que crea el nombre (por ejemplo, la del umbral encima de la de datos y modelo) | Moved la celda debajo de la que crea ese nombre (flechas de la barra de la celda, o cortar y pegar) y repetid |
| El PNG nuevo no tiene las mismas cifras que el texto | Cambiasteis modelo, umbral o costes después de escribir el texto, o no se volvió a ejecutar | Reiniciad y ejecutad todo, y actualizad las cifras del texto con las nuevas |
| El cuaderno descargado se llama `Copia de …ipynb` o lleva espacios | El título del cuaderno en Colab no es `informe_visual` | Cambiad el título en Colab y descargadlo otra vez |
| Subisteis un archivo a la raíz del repositorio | No se entró antes en `sprint-13` | Abrid el archivo, icono del lápiz, escribid `sprint-13/` delante del nombre en la ruta y **Commit changes**: lo mueve |
| Tras subir, el archivo no aparece | No se pulsó **Commit changes** | Subidlo otra vez y pulsad el botón verde |

<!--nav-->
---

[← Paso 3](Reto_Sprint_13_paso_3.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_13.md)
<!--/nav-->
