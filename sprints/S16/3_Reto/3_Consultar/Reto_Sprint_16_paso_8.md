# Paso 8 · Revisión con la rúbrica, review, retro y congelación (día 3, 55 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 8 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md)
<!--/nav-->

1. Revisar el trabajo con la rúbrica y anotar el resultado en el README.
2. Hacer la review (unos 5 minutos por equipo) y la retro.
3. Subir todo a `sprint-16/`, crear la etiqueta `v1.0-entrega` y subir las autoevaluaciones, **antes de las 14:30**.

**En sencillo.** Es el último paso, y el que más se parece a entregar un trabajo de verdad. Primero, **una persona que no escribió esa parte lo corrige con la rúbrica**, como lo corregiría el docente, y anota la nota con una frase de prueba. Luego se enseña el trabajo (la *review*) y el equipo mira cómo ha trabajado (la *retro*). Por último se sube todo al repositorio y se pone una **etiqueta**: es como cerrar el sobre y firmar la hora, para que quede claro qué versión se evalúa. No hace falta Git ni programar: casi todo se hace desde el navegador, con los botones de GitHub.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Rúbrica** | La tabla de 4 criterios por 4 niveles con la que se puntúa el reto. El equipo la usa para revisarse y el docente para puntuar. |
| **Frase de prueba** | La razón comprobable de un nivel: «3 · el README funciona en un Colab nuevo, pero falta la versión de Python». Sin ella, el nivel no vale. |
| **Review** | Enseñar el trabajo terminado al docente y a la clase (unos 5 minutos por equipo). |
| **Retro** | Reunión del equipo para mejorar la forma de trabajar: qué mantener, qué cambiar y qué acción concreta. |
| **Etiqueta (*tag*, `v1.0-entrega`)** | Marca con nombre y hora que apunta a una versión del repositorio. Lo que tiene a las 14:30 es lo que se evalúa. |
| **Release** | La página de GitHub desde la que se crea la etiqueta, con un título y una descripción. |
| **Commit** | Guardar un cambio en GitHub con un mensaje. Cada commit lleva el nombre de quien lo hace. |

**Cómo se hace**

1. **Revisar con la rúbrica (20 minutos).** Lo hace una persona que **no escribió esa parte** (una el repositorio y el demostrador; otra, la memoria y la model card). Abrid [entrega y rúbrica](../2_Entregar/entrega_y_rubrica.md), apartado 3, y los cinco pasos de «Cómo se revisa». Para cada uno de los cuatro criterios: leed las columnas de izquierda a derecha y parad en la primera cuyo texto **no se cumple entero**; vuestro nivel es el de la columna anterior (si lo de un nivel se cumple a medias, es el de abajo). Escribid **una frase de prueba** con algo que habéis comprobado. Después abrid `README.md`, lápiz ✏️, y sustituid el texto de la sección **«Revisión con la rúbrica»** (el final del README) por algo así:

    ```text
    ## Revisión con la rúbrica

    *Sprint 16. Revisó: Luis (no escribió el README) · 10/12/2026.*

    | Criterio | Nivel (1-4) | Frase de prueba |
    |---|---|---|
    | Corrección técnica | 3 | Test usado una vez (AUC 0,744); recall del canal directo 61,6 % → 79,2 % medido antes y después; `pytest -q` da 8 passed |
    | Reproducibilidad | 3 | El README funciona en un Colab nuevo; versiones fijas; falta indicar el tiempo total. Etiqueta pendiente de crear |
    | Análisis y comunicación al cliente | 3 | Memoria de 13 páginas; cifras iguales en memoria, README y model card; dice qué no hacer con el modelo |
    | IA responsable | 3 | Clasificación justificada (riesgo mínimo, sin datos personales); R-01 mitigado con evidencia; uso de IA declarado |

    **Lo primero que mejoraríamos:** indicar el tiempo total de reproducción en el README.
    ```

    Qué hay que respetar: la etiqueta se crea **después** de esta revisión, así que en Reproducibilidad anotad «etiqueta pendiente» y comprobadla en el punto 5. Lo fácil de arreglar, arreglarlo ya; lo demás, en «Lo primero que mejoraríamos». Nada de niveles sin frase de prueba. Si dos personas editan el README a la vez, GitHub avisa de un conflicto (mirad la tabla de abajo).

2. **Prepararse para la review (5 minutos).** Tenéis unos 5 minutos: **4 de demostración y 1 con una diapositiva**. Repartid los papeles: quien enseña la app, quien cuenta el sesgo, quien cuenta los riesgos, quien apunta el tiempo y el resultado de la prueba del docente. Guion:

    | Minuto | Qué se hace |
    |---|---|
    | 0–1 | Qué es el proyecto y qué decide el cliente con él |
    | 1–2:30 | Demostrador: una entrada típica y su aviso de incertidumbre |
    | 2:30–4 | Una entrada errónea a propósito y **la entrada difícil que propone el docente**, en directo |
    | 4–5 | Una diapositiva: tabla de sesgo y mitigación (antes y después, por subgrupo) y los riesgos altos con su estado |

    Si la app falla con la entrada del docente, no os justifiquéis: abrid el vídeo plan B (`docs/demo.mp4`), contad qué ha pasado y apuntadlo como limitación. Durante las reviews de los demás equipos, tomad notas para la **Parte 2 de vuestra hoja de autoevaluación y coevaluación** (punto 6).

3. **La retro (10 minutos, el equipo).** Una cosa que **mantener**, una que **cambiar** y una **acción concreta** (qué, quién y para cuándo). Revisad también la acción de la retro anterior: ¿se hizo y qué cambió? Apuntadlo en el tablero y haced una captura para `docs/scrum/`. Ejemplo:

    | Mantener | Cambiar | Acción (qué · quién · cuándo) | Acción de la retro anterior |
    |---|---|---|---|
    | La revisión cruzada de cifras antes de congelar | Dejamos la memoria hasta el día 2 y fue muy justo | Ensayar la defensa completa, con cronómetro · Marta · antes de la defensa | Cumplida: revisar las cifras entre dos personas evitó un recall distinto en la memoria y el README |

4. **Subir los ficheros (10 minutos).** Con [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md): abrid el repositorio del equipo; **Add file → Create new file** y escribid la ruta completa (cada barra crea una carpeta), o **Add file → Upload files** y arrastrad los archivos (o la carpeta entera); mensaje corto y **Commit changes**. Nombres en minúsculas y sin espacios. **Que suban personas distintas, cada una desde su cuenta**: el historial es la prueba de que trabajó todo el equipo. Reparto de ejemplo con tres personas:

    | Quién | Qué sube | Dónde |
    |---|---|---|
    | Ana | `README.md` (y la raíz al día) · `04_evaluacion.ipynb` | `sprint-16/` · `sprint-16/notebooks/` |
    | Luis | `logica.py` · `app.py` · `requirements.txt` · `tests/test_logica.py` · `modelo/` (si pesa poco) | `sprint-16/demostrador/` (y `…/demostrador/tests/`) |
    | Marta | `riesgos_eticos.md` · `model_card.md` · `memoria_tecnica.pdf` · `demo.mp4` (si pesa menos de 25 MB) | `sprint-16/docs/` |

    El cuaderno se descarga desde Colab con **Archivo → Descargar → Descargar .ipynb**; ejecutadlo antes de arriba abajo para que se guarden las salidas. Si ya subisteis algo en los pasos anteriores, no lo repitáis. Comprobad con el reloj de *Commits* que sale **cada persona**.

5. **Crear la etiqueta (5 minutos).** Es lo **último**, cuando todo lo anterior está subido. En la página principal del repositorio, a la derecha, **Releases → Create a new release**; en *Choose a tag* escribid `v1.0-entrega` y elegid *Create new tag*; el destino es `main`; poned un título (por ejemplo «Entrega final») y pulsad **Publish release**. Los nombres de los botones pueden cambiar un poco. Con Git en un terminal sería `git tag v1.0-entrega` y `git push origin v1.0-entrega`. Comprobad que la etiqueta aparece en la lista de *Releases* y que se publicó **antes de las 14:30**. Después de esa hora no se cambia código ni memoria; un fallo crítico del demostrador solo se corrige con permiso del docente y dejándolo documentado.

6. **Autoevaluación y coevaluación (5 minutos por persona, en paralelo).** Cada persona, con su propia cuenta, sube su hoja: copia el texto de [`autoevaluacion_y_coevaluacion.md`](../2_Entregar/autoevaluacion_y_coevaluacion.md) (**Raw** → `Ctrl + A` → `Ctrl + C`), **Add file → Create new file** en `sprint-16/` con el nombre `autoevaluacion_marta.md` (vuestro nombre, minúsculas, sin tildes ni espacios), pega, rellena y **Commit changes**. Rellenad:

    - **Parte 1 (autoevaluación).** Contestad las nueve preguntas con Sí / No / A medias, puntuad de 1 a 4 los cuatro criterios con **una frase** y completad «He usado IA para ……, y lo que he comprobado a mano es ……».
    - **Parte 2 (coevaluación del trabajo revisado).** Nombrad el trabajo del equipo que os ha tocado, marcad ✔, ✘ o — en cada entregable y puntuad los cuatro criterios con un comentario. Ejemplo de fila: *Demostrador · ✔ · «Se abrió con un comando y la entrada errónea dio un mensaje claro»*. Valorad el **trabajo**, no a las personas.

    No es la coevaluación confidencial (anexo B) del paso 7: esa va al docente, y esta hoja sí se sube al repositorio.

**Qué deberíais ver.** En `sprint-16/` los 9 ficheros del equipo (`README.md`, `notebooks/04_evaluacion.ipynb`, `demostrador/logica.py`, `app.py`, `tests/test_logica.py`, `requirements.txt`, y en `docs/` `riesgos_eticos.md`, `model_card.md` y `memoria_tecnica.pdf`) y una hoja `autoevaluacion_nombre.md` por persona (**9 + N**; un equipo de 3 sube 12). En el historial, commits de todas las personas. En el README, la sección «Revisión con la rúbrica» con cuatro niveles y su frase de prueba. En *Releases*, `v1.0-entrega` con una hora anterior a las 14:30.

**Hecho cuando:** la sección «Revisión con la rúbrica» del README está rellena, todo está subido, la etiqueta existe antes de las 14:30 y cada persona ha subido su autoevaluación y coevaluación.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| No aparece **Add file** | No sois colaboradores o no habéis aceptado la invitación. | Aceptad la invitación (correo o github.com/notifications) o pedidla a quien creó el repositorio. |
| El archivo quedó en la raíz, no en `sprint-16/` | Se subió sin la ruta de la carpeta. | Abridlo, lápiz ✏️, y escribid delante del nombre `sprint-16/docs/` (la ruta que toque); **Commit changes** lo mueve. |
| Subisteis algo y no aparece | No se pulsó el botón verde **Commit changes**. | Subidlo otra vez y pulsadlo: sin él no se guarda nada. |
| Aviso de conflicto al guardar el README | Dos personas lo editaron a la vez. | Recargad la página y repetid vuestro cambio sobre la versión actual. |
| No encontráis **Releases** o **Create a new release** | Los botones de GitHub cambian de sitio, o vuestra cuenta no puede escribir en el repositorio. | Buscad *Releases* en la columna derecha de la página principal. Si no hay forma, que lo haga otra persona del equipo o avisad al docente. |
| En `sprint-16/` no salen 9 + N ficheros | Falta algún archivo o alguna hoja de autoevaluación. | Comparad con la tabla del punto 4 y con la lista de «Qué deberíais ver»; cada persona comprueba el suyo. |
| Son las 14:30 y la etiqueta no está | Se pasó la hora de congelación. | Avisad al docente **ya**, explicad qué falta y no cambiéis nada más. |

<!--nav-->
---

[← Paso 7](Reto_Sprint_16_paso_7.md) · [Ficha del reto: ayudas, errores frecuentes y qué hacer si os atascáis](Reto_Sprint_16.md)
<!--/nav-->
