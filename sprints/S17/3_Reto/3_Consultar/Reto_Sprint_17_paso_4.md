# Paso 4 · Subir la presentación en PDF (día 1, 15 minutos; como tarde, antes de las 8:30 del día 2)

<!--nav-->
> Sprint 17 · Reto «La defensa» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_17.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_17_una_pagina.md) · [Paso 5 →](Reto_Sprint_17_paso_5.md)
<!--/nav-->

1. Exportar las diapositivas a PDF con el nombre `presentacion_defensa.pdf`.
2. Comprobar que son 12 o menos y que todas las cifras coinciden con la memoria congelada.
3. Subir el PDF a `sprint-17/` en el repositorio del equipo.

**En sencillo.** El PDF es la prueba de vuestras diapositivas: una vez exportado y subido, es lo que se evalúa. Pasa como con una invitación impresa: si hay una errata, ya no se arregla, así que se revisa **antes** de imprimir. La revisión más importante es la de las cifras. La memoria del Sprint 16 está congelada y es la verdad; si una cifra de una diapositiva no coincide con ella, se cambia **la diapositiva**, nunca la memoria. La comprueba **otra persona**, que ve con ojos nuevos lo que quien la hizo ya no ve. No hay código: se exporta, se compara y se sube.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Exportar a PDF** | Guardar las diapositivas como un documento que se ve igual en cualquier ordenador y que ya no se edita. |
| **Carpeta `sprint-17`** | La carpeta del repositorio de vuestro equipo donde va todo lo que se entrega en este sprint. |
| **Commit changes** | El botón verde de GitHub que guarda lo subido con un mensaje corto. Sin pulsarlo no se guarda nada. |
| **Historial (el reloj)** | El icono del reloj de una carpeta o archivo en GitHub: enseña quién subió cada versión y a qué hora. |
| **Revisión cruzada** | Cada cifra la comprueba una persona que **no** hizo esa diapositiva. |

**Cómo se hace**

1. **Exportar el PDF.** En el editor de diapositivas: *Archivo → Descargar* (o *Exportar*) *→ PDF*. El archivo se llama **`presentacion_defensa.pdf`**, en minúsculas, sin espacios y sin tildes. Si el editor lo guarda con otro nombre (por ejemplo, `Presentación sin título.pdf`), cambiadlo en vuestro ordenador **antes** de subirlo. Después, abrid el PDF y pasad página por página:

    - **Máximo 12 páginas.** Las diapositivas de reserva, si las hicisteis, no van en este PDF: se exportan aparte como `presentacion_reserva.pdf` (si vuestro editor deja elegir las páginas al exportar, por ejemplo de la 13 en adelante).
    - **Se lee bien:** nada cortado, imágenes visibles, letra grande.
    - **Orden del storyboard:** la 1 y la 12 llevan el mensaje único.
    - **Cada título es una frase** (un título-conclusión), con una sola idea y unas 25 palabras como máximo, y cada término técnico lleva su frase de traducción.

2. **Comprobar las cifras, con una persona que no hizo la diapositiva.** Abrid el PDF y la memoria congelada **una al lado de la otra**. La persona que comprueba lee en voz alta cada cifra de cada diapositiva y la busca en la memoria. Repartid las comprobaciones de modo que **nadie revise su propia diapositiva** (por ejemplo, con 3 personas: A comprueba las de B, B las de C y C las de A). Apuntad el resultado en una tabla como esta (el ejemplo es el del hotel de los apuntes):

    | Diapositiva | Cifra o frase | Dónde está en la memoria | ¿Coincide? |
    |---|---|---|---|
    | 6 | «Supera al método simple en 9 de 12 meses» | Tabla frente al baseline | sí |
    | 6 | «Error del 7 %» | Gráfico de errores por mes | sí |
    | 9 | «En reservas por móvil acierta menos» | Tabla por subgrupos | no: la memoria dice otra cifra |

    Qué hacer según el resultado:

    - **Coincide:** nada.
    - **No coincide:** se corrige **la diapositiva** (y se vuelve a exportar). **No se cambia la memoria.**
    - **No está en la memoria:** la cifra se quita. **No se presentan resultados nuevos.**

3. **Subir el PDF a GitHub.** Una persona lo hace con su cuenta. Los pasos, de la [guía de entrega](../../../../material/5.%20Como_entregar_en_GitHub.md):

    - Abrid el repositorio del equipo y **entrad primero en la carpeta `sprint-17`**, para que el archivo caiga ahí y no en la raíz.
    - Arriba a la derecha, **Add file → Upload files**.
    - Arrastrad `presentacion_defensa.pdf` a la zona gris (o pulsad *choose your files*) y esperad a que termine la barra de carga.
    - Más abajo, en **Commit changes**, escribid un mensaje corto («Añado la presentación de la defensa»), dejad marcado *Commit directly to the main branch* y pulsad el botón verde **Commit changes**.
    - Si ya subisteis la versión del ensayo, subid esta **con el mismo nombre**: la sustituye y el historial guarda las dos. Si hicisteis `presentacion_reserva.pdf`, se sube igual.

    Después, **recargad la carpeta**: el archivo tiene que aparecer. Pulsad el icono del reloj (*History*) para ver la hora de la subida. Y guardad **una copia del PDF** en el ordenador con el que vais a defender.

**Qué deberíais ver.** En `sprint-17/`, el archivo `presentacion_defensa.pdf` con la hora de la subida anterior a las 8:30 del 14/12. Al abrirlo desde GitHub se ven 12 páginas o menos, y la tabla de comprobación tiene un «sí» en cada cifra.

**Hecho cuando:** el PDF final está subido, tiene 12 diapositivas o menos y una persona ajena a cada diapositiva ha comprobado sus cifras.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| El PDF tiene más de 12 páginas | Se exportó también lo de reserva | Exportad solo las 12 primeras y llevad lo de reserva a otro PDF (`presentacion_reserva.pdf`) |
| Una cifra no coincide con la memoria | Se retocó la diapositiva o se calculó otra vez | Corregid la diapositiva y exportad de nuevo. La memoria no se cambia |
| El archivo se llama `Presentación sin título.pdf` o lleva mayúsculas, espacios o tildes | El editor pone su propio nombre | Renombradlo a `presentacion_defensa.pdf` antes de subirlo |
| Una página del PDF tiene el texto cortado o una imagen que no se ve | El editor exportó algo distinto de lo que veíais | Revisad en el editor esa diapositiva, exportad otra vez y volved a mirar el PDF. No se edita el PDF a mano |
| GitHub no deja subir el archivo | El límite por el navegador es de 25 MB por archivo | Comprimid las imágenes del editor o avisad al docente |
| El PDF salió en la raíz del repositorio y no en `sprint-17` | No se entró antes en la carpeta | Abridlo, icono del lápiz y escribid `sprint-17/` delante del nombre en la ruta; después **Commit changes**: lo mueve |
| Tras subirlo, el archivo no aparece | No se pulsó **Commit changes** | Subidlo otra vez y pulsad el botón verde |

<!--nav-->
---

[← Paso 3](Reto_Sprint_17_paso_3.md) · [Ficha del reto](Reto_Sprint_17.md) · [Paso 5 →](Reto_Sprint_17_paso_5.md)
<!--/nav-->
