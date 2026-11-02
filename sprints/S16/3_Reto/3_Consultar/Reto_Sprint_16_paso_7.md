# Paso 7 · Plan B, lista de congelación y coevaluación (día 3, 65 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 7 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 8 →](Reto_Sprint_16_paso_8.md)
<!--/nav-->

1. Grabar el vídeo plan B del demostrador (30 minutos).
2. Pasar la lista de congelación y buscar claves y datos personales olvidados (35 minutos).
3. Rellenar vuestra coevaluación individual (anexo B).

**En sencillo.** Antes de dar una obra por terminada se hacen tres cosas. Un **seguro**: un vídeo de 90 segundos de la demo funcionando, por si el día de la defensa falla internet o la app. Una **revisión final con lista**, como la de un piloto antes de despegar: casilla a casilla, sin fiarse de la memoria. Y una **valoración honesta del equipo**, en privado. No hace falta programar: se graba la pantalla con lo que trae el ordenador, se marcan casillas y se escribe sobre lo que cada persona ha hecho. Un pequeño programa de unas líneas os ayuda a buscar claves y datos personales olvidados en el repositorio.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Plan B** | Lo que usáis si falla el plan A. Aquí, un vídeo del demostrador funcionando (`docs/demo.mp4`). |
| **Guion** | Lista corta de lo que se ve y se dice en cada tramo del vídeo, para no improvisar. |
| **Congelación** | A las 14:30 del 10/12 lo que hay en la rama principal es lo que se evalúa; después no se cambia código ni memoria. |
| **Lista de congelación** | `checklist_congelacion.md`: seis bloques (A a F) de casillas que se marcan **con evidencia**. |
| **Clave (API key)** | Contraseña de un servicio. Va en los **Secretos** de Colab, nunca escrita en un archivo del repositorio. |
| **Dato personal** | Cualquier dato que identifique a una persona (nombre, correo, teléfono, DNI). No puede estar en el repositorio. |
| **Coevaluación (anexo B)** | Cada persona puntúa en privado a todo el equipo, incluida ella. Se entrega al docente, no al repositorio. |

**Cómo se hace**

1. **Repartir (2 minutos).** Tres tareas a la vez: el **vídeo** (la persona D y otra), la **lista de congelación y la búsqueda de claves** (la persona que verificó en el paso 6 y otra) y la **coevaluación** (cada persona, sola, al acabar su parte).

2. **Grabar el vídeo plan B (30 minutos).** Preparad la demo: `streamlit run app.py` en la carpeta `demostrador/`, el navegador con el zoom al 125 % para que se lea, sin pestañas personales abiertas ni avisos que puedan saltar. Elegid las tres entradas **antes** de grabar. Duración: entre 1 y 2 minutos, unos 90 segundos. Guion con las entradas del paso 4:

    | Segundos | Qué se ve | Qué se dice |
    |---|---|---|
    | 0–10 | La app abierta | «Esto es el demostrador de riesgo de cancelación de TurisData. Usa datos sintéticos.» |
    | 10–35 | Una entrada típica y **Calcular riesgo** | «Escribo una reserva con 120 días de antelación y tarifa flexible sin depósito. Da un 81 %, riesgo alto, frente a una media del 46 %.» |
    | 35–55 | Otra entrada distinta | «Con poca antelación, depósito total y tarifa no reembolsable, el riesgo baja al 4 %.» |
    | 55–75 | Una entrada **errónea a propósito** | «Pongo una antelación de 5000 días. La app no se rompe y dice que tiene que estar entre 1 y 400.» |
    | 75–90 | El cuadro azul del aviso | «Cada resultado lleva este aviso: el AUC del modelo y para qué no debe usarse.» |

    Para grabar, lo que trae el ordenador: en **Windows**, la barra de juegos (`Windows + Alt + R` empieza y acaba la grabación de la ventana activa); en **Mac**, `Cmd + Mayús + 5`; o la grabación de una videollamada compartiendo pantalla. Después:

    - **Vedlo entero, con sonido.** ¿Se lee? ¿Aparece la entrada errónea? ¿Hay algo personal en pantalla?
    - **Peso.** Si es menor de 25 MB, subidlo a `sprint-16/docs/demo.mp4` (**Add file → Upload files**). Si pesa más, regrabad una ventana en vez de la pantalla completa o más corto; o subidlo a un sitio estable (un enlace que abra sin iniciar sesión) y poned el enlace en el README.
    - **Formato.** Si vuestro programa no guarda `.mp4` (Mac guarda `.mov`), subidlo con su extensión y cambiad el nombre en el README y en la lista; o preguntad al docente cómo convertirlo.

3. **Pasar la lista de congelación (25 minutos).** Una persona **distinta a la que escribió el README** abre [`checklist_congelacion.md`](../1_Trabajar/plantillas/checklist_congelacion.md) y la copia al tablero o la imprime. Va casilla a casilla y marca solo lo que **ha visto con sus ojos**. Dónde mirar:

    | Bloque | Cómo se comprueba |
    |---|---|
    | A · Repositorio | El icono del reloj (*Commits*): salen las aportaciones de **todas** las personas. `README.md` con todos sus apartados, `requirements.txt` con versiones y versión de Python. Todo subido |
    | B · Reproducibilidad | El registro de fallos del paso 6, con todo resuelto |
    | C · Demostrador | Se lanza con un solo comando; las 5 entradas del paso 4; aviso de incertidumbre en cada resultado; `docs/demo.mp4` o su enlace |
    | D · Evaluación e IA responsable | Test usado una sola vez; subgrupos y mitigación medida; `docs/riesgos_eticos.md` con la Parte D rellena (fecha y firmas incluidas); `docs/model_card.md` sin `______` |
    | E · Memoria | `docs/memoria_tecnica.pdf` con 10 a 15 páginas contadas y las cifras de la tabla del paso 5 iguales en todos los sitios |
    | F · Equipo | Capturas del tablero (backlog, planning, review y retro de los sprints 14, 15 y 16; captura de pantalla con `Windows + Mayús + S` o `Cmd + Mayús + 4`, guardada como PNG y subida con *Add file → Upload files*) en `docs/scrum/`; la retro con una acción concreta; coevaluación hecha |

    El registro de riesgos se cerró en el paso 5. Aquí solo se comprueba, y si el paso 6 destapó algo nuevo (por ejemplo, un modelo que no cabe en el repositorio) se añade como riesgo con su estado. **Cada casilla sin marcar** se arregla ahora, antes de las 14:30, o se apunta en el tablero con responsable y hora. Tras las 14:30 no se cambia código ni memoria.

4. **Buscar claves y datos personales (10 minutos).** Quien pasa la lista descomprime el ZIP del repositorio en Colab y entra en su carpeta con `%cd`, como en el paso 6. Después ejecuta esto en una celda:

    ```python
    import re
    from pathlib import Path

    PATRONES = {
        "posible clave": r"(?:AIza|gsk_|sk-)[0-9A-Za-z_\-]{20,}",
        "clave escrita en el código": r"api_key\s*=\s*[\"'][^\"']{12,}[\"']",
        "correo": r"[\w.+-]+@[\w-]+\.[\w.-]+",
        "teléfono": r"\b[6-9]\d{8}\b",
        "DNI": r"\b\d{8}[A-Za-z]\b",
    }

    for archivo in sorted(Path(".").rglob("*")):
        if archivo.is_file() and ".venv" not in archivo.parts:
            if archivo.name.startswith(".env"):
                print(f"{archivo}: es un archivo de claves, no debe subirse")
            if archivo.suffix in (".py", ".ipynb", ".md", ".txt", ".json", ".csv"):
                texto = archivo.read_text(encoding="utf-8", errors="ignore")
                for nombre, patron in PATRONES.items():
                    for hallazgo in re.findall(patron, texto):
                        print(f"{archivo}: {nombre} → {hallazgo[:6]}…")
    ```

    Qué hace cada parte:

    - `PATRONES` son «formas» de texto que delatan algo: una clave que empieza por `AIza` (Google), `gsk_` (Groq) o `sk-`, un `api_key = "…"` escrito en el código, un correo, un teléfono de 9 cifras o un DNI. Cada forma es una *expresión regular*; no hace falta entenderlas, solo ejecutarlas.
    - El primer `if` avisa si hay un archivo `.env`, que es donde algunos programas guardan claves.
    - El segundo `if` lee los archivos de texto y `re.findall` busca cada forma. Solo se escriben los **6 primeros caracteres** de cada hallazgo, para no volver a mostrar una clave entera.

    Con un repositorio de ejemplo sale, por ejemplo, `sprint-12/asistente.ipynb: posible clave → AIzaSy…`. Un `api_key=userdata.get("GEMINI_API_KEY")` **no** sale: es la forma correcta de usar los Secretos de Colab ([guía de acceso a modelos](../../../../material/Acceso_modelos_de_lenguaje.md)). Revisad cada hallazgo: un correo del README del equipo también es un dato personal. Si encontráis una **clave**, borrarla del archivo no basta, porque queda en el historial de cambios: creadla de nuevo en la web del servicio, desactivad la anterior y avisad al docente. Si es un **dato personal**, quitadlo del archivo y avisad al docente.

5. **Coevaluación individual, anexo B (15 minutos).** La hace **cada persona sola** y no se comenta con el resto. Copiad [`plantilla_coevaluacion.md`](../1_Trabajar/plantillas/plantilla_coevaluacion.md) a un documento **vuestro** (no al repositorio) y rellenadla así:

    - **Puntuaciones (apartado 2).** De 1 a 4 a cada persona, **incluyéndoos a vosotros mismos**, en cinco dimensiones: contribución técnica, cumplimiento de tareas, comunicación, colaboración y fiabilidad. El 3 es «cumplió lo esperado». Un **1 o un 4 llevan un comentario obligatorio** con un hecho concreto.
    - **Reparto (apartado 3).** El esfuerzo global de cada persona en porcentaje; la suma da **100 %**.
    - **Preguntas abiertas (apartado 4).** Cinco respuestas de dos o tres frases con ejemplos: qué ha funcionado mejor; qué cambiaríais y qué acción de la retro sí se cumplió y cuál no; qué habéis aprendido y enseñado; algo que el docente deba saber; si rotasteis los roles de verdad.
    - **Firma.** Vuestro nombre.

    Ejemplo de un equipo de tres (Ana rellena el suyo):

    | Persona | Contribución técnica | Cumplimiento de tareas | Comunicación | Colaboración | Fiabilidad | Comentario (obligatorio si hay 1 o 4) |
    |---|---|---|---|---|---|---|
    | Yo mismo/a (Ana) | 3 | 3 | 3 | 3 | 3 | |
    | Luis | 2 | 2 | 3 | 3 | 3 | |
    | Marta | 3 | 3 | 4 | 4 | 3 | Comunicación y colaboración: el 9/12 vio que el recall no coincidía entre la memoria y el README, avisó en el grupo y lo corrigió en los tres sitios |

    Reparto del ejemplo: Yo 30 % · Luis 30 % · Marta 40 % = 100 %. La plantilla pide **hechos, no etiquetas**. Mal: «Luis es vago». Bien: «Luis, cumplimiento de tareas (2): el apartado 8 de la model card se entregó un día más tarde de lo acordado y lo terminó otra persona». Distinguid lo que hizo de cómo os sentó y recordad el objetivo: mejorar el trabajo del equipo, no castigar. Se entrega **al docente**, en la forma que él indique; **no se sube al repositorio**. No la confundáis con la hoja `autoevaluacion_nombre.md`, que sí se sube (paso 8).

**Qué deberíais ver.**
- **El vídeo:** `docs/demo.mp4` en el repositorio, o su enlace en el README, de unos 90 segundos, con una entrada errónea que no rompe la app.
- **La búsqueda de claves:** ninguna línea, o solo hallazgos revisados y resueltos. Con el demostrador del paso 4 no sale ninguna.
- **La lista de congelación:** las seis secciones con todas las casillas marcadas, o con lo pendiente apuntado (qué, quién y a qué hora).
- **La coevaluación:** cada persona con la suya hecha, con comentario en cada 1 o 4 y reparto que suma 100 %.

**Hecho cuando:** el vídeo plan B existe, la lista de congelación está pasada (con el registro de riesgos ya cerrado en el paso 5) y todo el equipo ha entregado la coevaluación.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| El archivo del vídeo no se sube | Por el navegador, GitHub admite 25 MB por archivo. | Regrabad más corto o una ventana en lugar de la pantalla completa; si sigue pesando, sitio estable y enlace en el README. |
| El vídeo se corta o no se oye | La grabación empezó en otra ventana o sin micrófono. | Repetidlo: son 90 segundos. Probad antes 10 segundos. |
| El buscador marca `posible clave → AIzaSy…` | Hay una clave escrita en un archivo. | Creadla otra vez en la web del servicio, desactivad la vieja, guardad la nueva en los Secretos de Colab y avisad al docente. |
| El buscador marca un `correo` o un `teléfono` en el README | Hay un dato personal. | Quitadlo (una dirección genérica del equipo, o ninguna) y avisad al docente. |
| En *Commits* solo aparece una persona | El resto no ha subido nada con su cuenta. | Que cada persona suba **ahora** lo suyo (su autoevaluación vale) desde su cuenta; no se arregla después de las 14:30. |
| Una casilla de la lista no se puede marcar | Falta algo o no hay evidencia. | Arreglarlo si hay tiempo; si no, apuntad qué falta, quién y cuándo. Una casilla marcada sin mirar es peor que una sin marcar. |
| La coevaluación no da 100 % | Los porcentajes del apartado 3 no suman bien. | Sumadlos y ajustad antes de entregarla. |

<!--nav-->
---

[← Paso 6](Reto_Sprint_16_paso_6.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 8 →](Reto_Sprint_16_paso_8.md)
<!--/nav-->
