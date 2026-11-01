# Paso 6 · Verificar en limpio y corregir (día 3, 80 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 6 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 7 →](Reto_Sprint_16_paso_7.md)
<!--/nav-->

1. Una persona que no escribió el README lo sigue en un Colab nuevo o una carpeta limpia (60 minutos).
2. Mientras tanto, el resto cierra la memoria y la exporta a PDF.
3. Corregir lo que haya fallado (20 minutos).

**En sencillo.** «A mí me funciona» no es una prueba. Un proyecto está terminado cuando **otra persona, en otro sitio, lo hace funcionar leyendo solo el README**. Es como la receta que escribís para un amigo: no vale que a vosotros os salga el plato, tiene que salirle a él sin llamaros por teléfono. Por eso hoy una persona que no escribió el README ejecuta todo desde cero, apunta cada tropiezo con su mensaje exacto, y el equipo lo arregla. No hace falta saber programar: quien prueba solo obedece el README y copia los mensajes de error; arreglar suele ser añadir una línea al README o a `requirements.txt`. Mientras, el resto del equipo deja la memoria lista y la exporta a PDF.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Prueba en limpio** | Ejecutar el proyecto en un sitio donde no hay nada vuestro instalado ni guardado, para ver si funciona solo con lo que hay en el repositorio. |
| **ZIP del repositorio** | Todo el repositorio en un solo archivo, que se descarga con **Code → Download ZIP**. Lo que no está subido, no está en el ZIP. |
| **Ruta absoluta** | Dirección de un archivo en *vuestro* ordenador (`/content/drive/MyDrive/datos.csv`, `C:\Users\Ana\…`). En otro ordenador no existe. |
| **Dependencia** | Una librería que el proyecto necesita (`seaborn`, `streamlit`). Si no está en `requirements.txt`, otra persona no la tiene. |
| **Semilla** | El número (`42`) que hace que un reparto al azar salga igual en cada ejecución. Sin semilla, las cifras cambian y no coinciden con la memoria. |
| **Registro de fallos** | Tabla donde se apunta cada tropiezo: qué se hacía, qué se esperaba y qué pasó (con el mensaje copiado). |
| **Exportar a PDF** | Guardar el documento en un formato que se ve igual en todos los ordenadores. |

**Cómo se hace**

1. **Repartir los papeles (3 minutos).**

    | Papel | Quién | Qué hace |
    |---|---|---|
    | Verificador/a | Alguien que **no** escribió el README | Ejecuta todo siguiendo solo el README, en voz alta. Si lo prueba quien lo escribió, no vale: ya conoce los trucos que no están anotados |
    | Observador/a | Quien escribió el README | **No ayuda ni explica.** Apunta cada fallo en el registro y ejecuta el punto 4 |
    | Memoria | El resto del equipo | Punto 5, a la vez |

2. **Preparar el entorno limpio (10 minutos).** El/la verificador/a descarga el repositorio del equipo: en github.com, botón verde **Code → Download ZIP**. En Colab (colab.research.google.com → **Nuevo cuaderno**) abre el panel de archivos (icono de carpeta, a la izquierda), arrastra el ZIP y ejecuta esta celda cambiando el nombre por el de vuestro ZIP:

    ```text
    !unzip -q ifcd107-equipo-NOMBRE-main.zip
    %cd ifcd107-equipo-NOMBRE-main
    !ls
    !pip install -r requirements.txt
    ```

    Qué hace cada línea:

    - `!unzip -q …` descomprime el ZIP (el `!` le dice a Colab que es una orden de terminal, no de Python). La carpeta que aparece se llama como el repositorio más `-main`.
    - `%cd …` entra en esa carpeta; a partir de aquí las rutas del README funcionan.
    - `!ls` lista lo que hay. Con un repositorio de ejemplo salen `README.md`, `requirements.txt`, `sprint-14`, `sprint-15` y `sprint-16`. Si falta algo, **no se subió**.
    - `!pip install -r requirements.txt` instala la lista del proyecto.

    Si el README empieza con `git clone`, saltadlo: ya tenéis el contenido.

3. **Seguir el README al pie de la letra (40 minutos).** Quien verifica va leyendo el README y ejecutando **exactamente** lo que dice, en orden: datos, cuadernos de arriba abajo (**Entorno de ejecución → Ejecutar todo**), demostrador (`streamlit run app.py` no se abre en Colab: se hace en un ordenador, como en el paso 4) y pruebas. Reglas:

    - Si tiene que **adivinar** algo, es un fallo del README, aunque al final lo consiga.
    - Si hay un error, **copia el mensaje entero**; no lo resume.
    - Compara cada cifra del cuaderno con la de la memoria y el README (con tres decimales). Tienen que ser iguales.

    El/la observador/a apunta cada fallo en una tabla como esta (ejemplos):

    | Hora | Qué se hacía (línea del README) | Qué se esperaba | Qué pasó (mensaje copiado) | Arreglo | Quién |
    |---|---|---|---|---|---|
    | 10:20 | Ejecutar `04_evaluacion.ipynb` | Que cargase los datos | `FileNotFoundError: [Errno 2] No such file or directory: '/content/drive/MyDrive/reservas_turisdata.csv'` | Ruta relativa o `dato(...)` | Ana |
    | 10:45 | Lanzar el demostrador | Que se abriese la app | `FileNotFoundError: Falta el modelo. Ejecuta primero el notebook S16_01…` | Subir `modelo/` o explicar en el README cómo generarlo | Luis |

4. **Buscar lo que siempre falla (7 minutos).** Lo hace el/la observador/a (que no puede ayudar a quien verifica). Desde la carpeta del repositorio descomprimido, estas dos revisiones. **Primera:** rutas de vuestro ordenador dentro de los archivos.

    ```python
    from pathlib import Path

    RUTAS_SOSPECHOSAS = ["/content/", "/home/", "/Users/", "C:\\Users", "C:/Users", "drive/MyDrive"]

    for archivo in sorted(Path(".").rglob("*")):
        if archivo.suffix in (".py", ".ipynb", ".md", ".txt", ".json") and ".venv" not in archivo.parts:
            texto = archivo.read_text(encoding="utf-8", errors="ignore")
            for marca in RUTAS_SOSPECHOSAS:
                if marca in texto:
                    print(f"{archivo}: contiene '{marca}'")
    ```

    Qué hace cada línea:

    - `RUTAS_SOSPECHOSAS` es la lista de trozos de dirección que delatan un ordenador concreto. Podéis añadir los vuestros.
    - `Path(".").rglob("*")` recorre **todas** las carpetas desde donde estáis. El `if` se queda con los archivos de texto y se salta `.venv`.
    - `archivo.read_text(…)` lee el archivo y el bucle `for marca` escribe una línea por cada marca encontrada.

    Con un repositorio de ejemplo sale `sprint-16/notebooks/04_evaluacion.ipynb: contiene '/content/'`. Cada línea es una ruta que hay que cambiar por una relativa. Un `/content/` legítimo (una ruta de Colab en un comentario) se puede dejar si el README lo explica. **Segunda:** las librerías que usan vuestros cuadernos, para compararlas con `requirements.txt`.

    ```python
    import json
    import re
    import sys
    from pathlib import Path

    librerias = set()
    for cuaderno in Path(".").rglob("*.ipynb"):
        for celda in json.loads(cuaderno.read_text(encoding="utf-8"))["cells"]:
            if celda["cell_type"] == "code":
                for linea in "".join(celda["source"]).splitlines():
                    m = re.match(r"\s*(?:import|from)\s+([A-Za-z0-9_]+)", linea)
                    if m:
                        librerias.add(m.group(1))
    print(sorted(librerias - set(sys.stdlib_module_names)))
    ```

    Escribe la lista de librerías que importan los cuadernos, sin las que ya trae Python (`sys.stdlib_module_names`). Con los cuadernos `S13_02` y `S16_01` sale `['IPython', 'api', 'fastapi', 'ipywidgets', 'joblib', 'logica', 'matplotlib', 'numpy', 'pandas', 'pydantic', 'seaborn', 'sklearn', 'streamlit']`. `api` y `logica` son archivos del propio demostrador, no librerías, e `IPython` ya viene con Jupyter y Colab. Comprobad que cada una de las demás está en `requirements.txt`; `sklearn` se instala como `scikit-learn`.

5. **Memoria a limpio y PDF (el resto del equipo, 60 minutos).** Por este orden:

    - **Pendientes.** Buscad `PENDIENTE` con `Ctrl + F` y resolvedlos uno a uno.
    - **Sección 0, resumen ejecutivo.** Se escribe **la última**, con las cuatro viñetas del esqueleto y vuestras cifras. Ejemplo con TurisData:

        ```text
        Problema y decisión: cada cancelación sin aviso deja una habitación vacía; quien gestiona la disponibilidad decide si pide depósito.
        Qué hicimos: comparamos modelos con validación cruzada y evaluamos el candidato una sola vez en el test.
        Resultado: AUC 0,744 (95 %: 0,719–0,767) frente a 0,50 del baseline; recall 82,8 %. Con los costes supuestos, 17.810 € frente a 34.400 € sin modelo en 1500 reservas de prueba.
        Recomendación y límites: usarlo para orientar, con una persona que decida; umbral propio en el canal directo; no usarlo para decidir sobre personas. Datos sintéticos de un solo alojamiento.
        ```

    - **Portada, índice y «Referencias y licencias».** En las referencias: cada fuente de datos con la cita que dejasteis en `plan_datos_licencias.md` (apartado 7: fuente, autor, título, año, versión, enlace, licencia), las librerías con sus versiones y la declaración del uso de IA del paso 5.
    - **Anexos A a G** del esqueleto (ficha de proyecto, plan de datos, registro de experimentos, model card, registro de riesgos, capturas del tablero y retros, enlace al repositorio y a `v1.0-entrega`; la dirección de la etiqueta acaba en `/releases/tag/v1.0-entrega`, así que podéis escribirla ya aunque la etiqueta se cree en el paso 8).
    - **Lista de calidad** del final del esqueleto, con una persona que **no** escribió esa sección: cada figura con título que dice lo que se ve, ejes con nombre y citada en el texto; cifras iguales que en el README y el registro; cada afirmación importante con evidencia; sin párrafos genéricos sobre «qué es la IA».
    - **Contar las páginas.** Las que cuentan son las de las secciones 0 a 9; no cuentan portada, índice, referencias ni anexos. Ejemplo de cuenta (no es vuestro número):

        | Parte | Páginas | ¿Cuenta? |
        |---|---|---|
        | Portada e índice | 2 | No |
        | Secciones 0 a 9 | 13 | **Sí** (tiene que dar entre 10 y 15) |
        | Referencias y licencias | 1 | No |
        | Anexos A a G | 4 | No |
        | Total del PDF | 20 | |

        Si pasáis de 15, recortad texto repetido y figuras grandes antes de quitar contenido (el esqueleto da el presupuesto de cada sección). Si no llegáis a 10, falta contenido en alguna sección.

    - **Exportar.** En Google Docs: **Archivo → Descargar → Documento PDF**; en Word: **Archivo → Guardar como → PDF**. Nombre: `memoria_tecnica.pdf`. Abrid el PDF y mirad cada página: figuras sin cortar, tablas dentro del margen, números de página. Subidlo a `sprint-16/docs/` con **Add file → Upload files**.

6. **Corregir y repetir (20 minutos).** Con el registro de fallos delante, arreglad uno a uno y **repetid solo la parte que falló**:

    | Fallo | Arreglo |
    |---|---|
    | Falta una librería | `pip show NOMBRE` y copiad la línea `Version:` a `requirements.txt` como `NOMBRE==x.y.z` |
    | Ruta absoluta | Una ruta relativa desde la carpeta del archivo, o `dato("archivo.csv")` si el dato es del curso |
    | Falta un archivo (datos, `modelo/`) | Subirlo si pesa poco y la licencia lo permite; si no, un script de descarga y una frase en el README |
    | Falta un paso en el README | Añadidlo con la orden exacta y qué se debe ver |
    | Las cifras cambian de una ejecución a otra | Fijad `SEMILLA = 42` y usadla en el reparto de datos y en el modelo; ejecutad de arriba abajo |

    Cuando algo cambie, subidlo (**Add file → Upload files** o el lápiz ✏️), y que quien verifica repita ese fragmento. Lo que no se pueda arreglar hoy, apuntadlo en la model card y en la memoria como limitación.

**Qué deberíais ver.**
- **El registro de fallos:** corto, con cada fila resuelta y con el mensaje de error copiado.
- **En el entorno limpio:** `pip install -r requirements.txt` termina sin errores, los cuadernos se ejecutan de arriba abajo con las mismas cifras que la memoria y, en un ordenador, `pytest -q` da `8 passed` (el número de vuestras pruebas) y la app se abre en `http://localhost:8501`.
- **Los dos buscadores:** el de rutas sin ninguna línea (o solo las que justificáis) y el de librerías con todas dentro de `requirements.txt`.
- **En `sprint-16/docs/`:** `memoria_tecnica.pdf` con 10 a 15 páginas contadas.

**Hecho cuando:** otra persona ha reproducido el proyecto con solo el README, lo que falló está corregido y existe `docs/memoria_tecnica.pdf`.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'seaborn'` (o `scipy`, `streamlit`…) | La librería estaba instalada en vuestro entorno, pero no está en `requirements.txt`. | Añadidla con su versión (`pip show seaborn`) y volved a instalar. El buscador de librerías del punto 4 las encuentra todas. |
| `FileNotFoundError: [Errno 2] No such file or directory: '/content/drive/MyDrive/…'` | Una ruta absoluta de otro ordenador. | Cambiadla por una ruta relativa; el buscador de rutas del punto 4 localiza el resto. |
| `ERROR: Could not find a version that satisfies the requirement numpy==9.9.9` y debajo `ERROR: No matching distribution found for numpy==9.9.9` | La versión de `requirements.txt` no existe o está mal escrita. | Copiad la línea `Version:` de `pip show` tal cual, sin cambiar ninguna cifra. |
| `FileNotFoundError: Falta el modelo. Ejecuta primero el notebook S16_01…` | `demostrador/modelo/` no está en el repositorio. | Subid la carpeta `modelo/` (pesa poco) o explicad en el README cómo generarla. |
| Las cifras del cuaderno no coinciden con las de la memoria | La semilla no está fijada, o la memoria se escribió con otra versión del cuaderno. | Fijad `SEMILLA`, ejecutad de arriba abajo y corregid la memoria con las cifras nuevas **en todos los sitios** (paso 5, punto 7). |
| El PDF tiene más de 15 páginas contadas (o menos de 10) | Texto repetido, figuras muy grandes, o secciones demasiado cortas. | Recortad o ampliad según el presupuesto de páginas del esqueleto y volved a exportar. |
| `[Errno 2] No such file or directory: 'ifcd107-equipo-…'` al ejecutar `%cd` | El nombre de la carpeta no es el que escribisteis. | Ejecutad `!ls` y copiad el nombre exacto que sale. |

<!--nav-->
---

[← Paso 5](Reto_Sprint_16_paso_5.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 7 →](Reto_Sprint_16_paso_7.md)
<!--/nav-->
