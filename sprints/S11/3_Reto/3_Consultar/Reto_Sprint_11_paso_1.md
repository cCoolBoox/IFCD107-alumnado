# Paso 1 · Preparar los datos (día 1, 25 minutos)

<!--nav-->
> Sprint 11 · Reto «Visión artificial para el cliente» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_11.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_11_una_pagina.md) · [Paso 2 →](Reto_Sprint_11_paso_2.md)
<!--/nav-->

1. Abrir el cuaderno `S11_04` en Colab, hacer una copia y compartirla con el equipo.
2. Decidir si usáis las fotos sintéticas del cuaderno o un conjunto propio.
3. Comprobar cuántas fotos hay por clase y mirarlas.
4. Anotar las etiquetas dudosas y ver cómo se parten los datos.

**En sencillo.** Antes de entrenar nada hay que saber con qué fotos se trabaja, igual que un cocinero abre la despensa y mira qué ingredientes tiene y en qué estado antes de ponerse a cocinar. En este paso abrís el cuaderno, comprobáis cuántas fotos hay de cada tipo de alojamiento (hotel, apartamentos, casa rural, camping y piscina), **las miráis con vuestros propios ojos** y veis cómo se reparten en tres montones (uno para aprender, otro para ensayar y otro para el examen final). Algunas fotos llevan **a propósito** una etiqueta dudosa, como pasa con los datos reales: vuestro trabajo es encontrarlas. Por defecto no son fotos reales, sino dibujos esquemáticos que genera el propio cuaderno. No hace falta saber programar: escribís una función corta de contar, que tenéis aquí línea a línea.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Celda** | Cada caja del cuaderno. Las de código se **ejecutan** con el botón ▶ (o con `Mayús + Intro`). |
| **Función** | Una receta con nombre: se escribe una vez con `def` y se usa las veces que haga falta. Aquí escribiréis `contar_por_clase`. |
| **Diccionario** | Una lista de parejas «nombre: valor» entre llaves, por ejemplo `{"hotel": 60, "camping": 60}`. |
| **Clase y etiqueta** | La clase es el tipo de alojamiento (hotel, camping…). La etiqueta es el nombre de la clase que lleva cada foto; aquí, el de su carpeta. |
| **Dataset sintético** | Un conjunto de datos creado por un programa y no recogido de la realidad. Aquí, dibujos de 48 × 48 píxeles, **no fotos reales**. |
| **Etiqueta dudosa** | Una foto que está en la carpeta de una clase pero se parece más a otra (por ejemplo, una tienda de campaña en la carpeta de casas rurales). |
| **Partición** | El reparto de las fotos en tres montones: **entrenamiento** (con las que aprende el modelo), **validación** (con las que se ensaya y se decide) y **prueba** (el examen final, que se mira una sola vez). |
| **Semilla** | Un número que fija el azar para que, al repetir el reparto, salga siempre lo mismo. Aquí, `SEMILLA = 42`. |
| **Dimensiones** (`shape`) | El tamaño de una tabla de números. `(180, 48, 48, 3)` son 180 fotos de 48 × 48 píxeles con 3 colores (rojo, verde y azul). |

**Cómo se hace**

1. **Abrir vuestra copia del cuaderno.** Entrad en el [cuaderno `S11_04_reto_vision_cliente`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_04_reto_vision_cliente.ipynb) (se abre en Colab). Arriba, *Archivo → Guardar una copia en Drive*: así trabajáis en una copia vuestra y el original no se toca. Pulsad *Compartir* (arriba a la derecha) y añadid los correos del equipo con permiso de **Editor**. Una persona escribe y las demás miran y opinan; cambiad de turno cada pocos minutos. Colab puede desconectarse: si pasa, volved a ejecutar las celdas desde arriba.
2. **Ejecutar las celdas de preparación, por orden.** Pulsad ▶ en cada una, de arriba abajo: primero «Preparación» (**siempre la primera**: crea la función `dato(…)`), después la de las importaciones y la semilla (`SEMILLA = 42`; tarda unos segundos porque trae TensorFlow, la librería de redes neuronales) y después la del «0. Generador de imágenes sintéticas». Esta última no escribe nada y **no hace falta estudiarla**: solo enseña a Python a dibujar los alojamientos. Sabréis que han terminado porque aparece un ✓ y un número entre corchetes. **Ejecutad celda a celda, sin «Ejecutar todo»**: el cuaderno tiene huecos (`...`) que dan error hasta que los rellenéis.
3. **Decidir con qué fotos se trabaja.** Para el nivel mínimo y el estándar vale el conjunto sintético, que es lo que hace la celda del apartado «1 · El dataset: una carpeta por clase». Ejecutadla; su código es este:

    ```python
    USAR_DATASET_PROPIO = False
    RUTA_PROPIA = "mis_fotos"                       # carpeta con una subcarpeta por clase
    RUTA = RUTA_PROPIA if USAR_DATASET_PROPIO else os.path.join("datos_sinteticos", "alojamientos")

    if not USAR_DATASET_PROPIO and not os.path.isdir(RUTA):
        crear_dataset_carpetas(RUTA, n_por_clase=60, semilla=7, tam=48, ruido=40, prop_ambiguas=0.12)
        print("Dataset sintético generado en", RUTA)
    ```

    Qué hace cada línea:

    - `USAR_DATASET_PROPIO = False`: un interruptor. `False` = se usan los dibujos del cuaderno; `True` = se usan vuestras fotos.
    - `RUTA_PROPIA = "mis_fotos"`: el nombre de la carpeta con vuestras fotos, si las usáis. Lo que va tras `#` es un comentario: Python lo ignora.
    - `RUTA = … if … else …`: elige una carpeta u otra según el interruptor. Con las sintéticas, `RUTA` vale `datos_sinteticos/alojamientos`.
    - `if not USAR_DATASET_PROPIO and not os.path.isdir(RUTA):`: «si vais a usar las sintéticas y la carpeta todavía no existe…».
    - `crear_dataset_carpetas(RUTA, n_por_clase=60, …)`: …las crea: 60 dibujos por clase, con `ruido=40` (grano, para que no sean perfectos) y `prop_ambiguas=0.12` (un 12 %, aproximadamente, lleva una etiqueta dudosa a propósito). Solo lo hace la primera vez.
    - `print("Dataset sintético generado en", RUTA)`: avisa de que ya están.

    Si queréis usar **fotos propias** (es un extra), poned `USAR_DATASET_PROPIO = True` y consultad con el docente cómo subirlas a Colab. Reglas: **una carpeta por clase**, con nombres sin espacios ni tildes (`casa_rural`); mínimo 30 fotos por clase (mejor 100 o más); hechas por vosotros o con licencia abierta; **sin personas reconocibles**; y apuntad autor y licencia de cada una.

4. **Ejercicio 1: contar las fotos por clase.** Bajad al enunciado «Ejercicio 1 (comprobar el dataset)». En su celda hay una línea `# TODO` (una pista), tres puntos `...` y varias líneas con `assert`. Borrad **solo los tres puntos** y escribid esto, respetando mayúsculas, comillas, paréntesis y la sangría de 4 espacios por nivel:

    ```python
    def contar_por_clase(ruta):
        conteo = {}
        for clase in sorted(os.listdir(ruta)):
            carpeta = os.path.join(ruta, clase)
            if os.path.isdir(carpeta):
                conteo[clase] = sum(f.lower().endswith((".png", ".jpg", ".jpeg")) for f in os.listdir(carpeta))
        return conteo
    ```

    Qué hace cada línea:

    - `def contar_por_clase(ruta):`: define la función. Recibe `ruta`, el nombre de la carpeta que contiene una subcarpeta por clase. Los dos puntos del final son obligatorios.
    - `conteo = {}`: un diccionario vacío donde se irá apuntando «clase: número de fotos».
    - `for clase in sorted(os.listdir(ruta)):`: `os.listdir(ruta)` lista lo que hay dentro de la carpeta; `sorted` lo ordena alfabéticamente; y el `for` repite lo de debajo una vez por cada elemento, llamándolo `clase`.
    - `carpeta = os.path.join(ruta, clase)`: pega la ruta y el nombre para tener el camino completo a esa subcarpeta (por ejemplo, `datos_sinteticos/alojamientos/hotel`).
    - `if os.path.isdir(carpeta):`: «solo si es una carpeta». Es importante: dentro de `RUTA` hay también un archivo suelto, `_ambiguas.csv`, que **no** es una clase.
    - `conteo[clase] = sum(… for f in os.listdir(carpeta))`: para cada archivo `f` de la carpeta pregunta si su nombre acaba en `.png`, `.jpg` o `.jpeg` (`f.lower()` lo pasa a minúsculas para aceptar también `.PNG`; `.endswith((…))` responde `True` o `False`) y `sum` suma los `True` (cada uno vale 1). El resultado se apunta en el diccionario.
    - `return conteo`: devuelve el diccionario terminado. **Sin esta línea la función no devuelve nada.**

    Pulsad ▶. Debajo, el cuaderno imprime el diccionario y comprueba que hay al menos 2 clases, que ninguna está vacía y que, con las sintéticas, hay 60 fotos en cada una de las 5 clases.

5. **Mirar las fotos.** «Primero se mira, después se mide.» Para ver unas cuantas de cada clase, añadid una celda nueva (**+ Código**) y ejecutad:

    ```python
    fig, ejes = plt.subplots(len(conteo), 8, figsize=(14, 2 * len(conteo)))
    for fila, clase in zip(ejes, conteo):
        for eje, nombre in zip(fila, sorted(os.listdir(os.path.join(RUTA, clase)))):
            eje.imshow(Image.open(os.path.join(RUTA, clase, nombre)))
            eje.set_title(f"{clase}/{nombre}", fontsize=6)
            eje.axis("off")
    plt.tight_layout(); plt.show()
    ```

    Qué hace cada línea:

    - `plt.subplots(len(conteo), 8, …)`: prepara una rejilla con una fila por clase (`len(conteo)` es cuántas hay: 5) y 8 columnas.
    - `for fila, clase in zip(ejes, conteo):`: recorre a la vez las filas de la rejilla y los nombres de las clases.
    - `for eje, nombre in zip(fila, sorted(os.listdir(…))):`: dentro de cada fila, empareja cada hueco con un archivo de esa carpeta (solo caben 8, así que se ven los 8 primeros).
    - `eje.imshow(Image.open(…))`: abre la imagen y la dibuja en su hueco.
    - `eje.set_title(f"{clase}/{nombre}", …)` y `eje.axis("off")`: ponen encima la carpeta y el nombre del archivo, y quitan los ejes numerados.

    Con el conjunto sintético veréis, de forma aproximada: **hotel**, un edificio alto y estrecho con ventanas en filas; **apartamentos**, uno bajo y ancho; **casa_rural**, una casita con tejado rojo; **camping**, una tienda de campaña triangular; **piscina**, un rectángulo azul rodeado de arena. Mirad con calma. **Una foto es dudosa** si su dibujo corresponde a otra clase: por ejemplo, una tienda de campaña en `casa_rural` (en la generación que hemos comprobado, `casa_rural/img_001.png` lo es; si vuestra copia genera otras, buscad las vuestras), un edificio bajo y ancho en `hotel` o uno alto en `apartamentos`. Apuntad las que encontréis en el documento del equipo (os servirá luego), con este formato: `carpeta/nombre → qué dibuja de verdad`. Si queréis ver una foto más grande, abrid el panel de archivos (📁) y haced doble clic sobre ella.

6. **Ver cómo se parten los datos.** Ejecutad la celda «Cargar con `image_dataset_from_directory`». Ya está escrita y **no hay que modificarla**. Sus líneas más importantes:

    ```python
    TAM = 48
    ds_ent, ds_resto = keras.utils.image_dataset_from_directory(
        RUTA, validation_split=0.4, subset="both", seed=SEMILLA, image_size=(TAM, TAM), batch_size=32, label_mode="int")
    NOMBRES = ds_ent.class_names
    N_CLASES = len(NOMBRES)
    rutas_resto = ds_resto.file_paths
    ```

    ```python
    X_ent, y_ent = a_numpy(ds_ent)
    X_resto, y_resto = a_numpy(ds_resto)
    mitad = len(X_resto) // 2
    X_val, y_val = X_resto[:mitad], y_resto[:mitad]
    X_pru, y_pru = X_resto[mitad:], y_resto[mitad:]
    rutas_pru = rutas_resto[mitad:]
    ```

    Qué hace cada parte:

    - `image_dataset_from_directory(RUTA, …)`: carga las fotos de las carpetas y usa **el nombre de cada carpeta como etiqueta**. `validation_split=0.4, subset="both"` devuelve dos montones: el 60 % para entrenamiento (`ds_ent`) y el 40 % restante (`ds_resto`). `seed=SEMILLA` fija el reparto y `image_size=(TAM, TAM)` pone todas las fotos al mismo tamaño.
    - `NOMBRES = ds_ent.class_names`: los nombres de las clases, en orden alfabético. `N_CLASES` es cuántas hay.
    - `mitad = len(X_resto) // 2` y las dos líneas siguientes: el 40 % se parte por la mitad en **validación** (20 %) y **prueba** (20 %). Las dos primeras líneas del segundo bloque convierten las fotos en tablas de números (`X`, las fotos; `y`, su clase).
    - `rutas_pru`: los nombres de archivo de las fotos de prueba, para poder localizarlas luego.

    **La prueba no se toca hasta el paso 3**: se usa **una sola vez**, al final.

**Qué deberíais ver.**
- **Al generar las fotos:** `Dataset sintético generado en datos_sinteticos/alojamientos` (solo la primera vez).
- **El ejercicio 1:** `{'apartamentos': 60, 'camping': 60, 'casa_rural': 60, 'hotel': 60, 'piscina': 60}`: las cinco clases, con 60 fotos cada una.
- **La rejilla de fotos:** cinco filas de ocho dibujos, una fila por clase.
- **La partición:** unos mensajes de Keras parecidos a `Found 300 files belonging to 5 classes.`, `Using 180 files for training.` y `Using 120 files for validation.`; después `Clases: ['apartamentos', 'camping', 'casa_rural', 'hotel', 'piscina']` y una línea `entrenamiento (180, 48, 48, 3) · validación (60, 48, 48, 3) · prueba (60, 48, 48, 3)`, más una fila de ocho fotos de ejemplo del entrenamiento, cada una con su clase.

**Hecho cuando:** `contar_por_clase` pasa sus comprobaciones, habéis mirado las fotos y anotado las dudosas, y todo el equipo sabe que la prueba no se toca hasta el paso 3.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'crear_dataset_carpetas' is not defined` (o `'keras'`, `'os'`, `'CLASES_ALOJ'`) | No se ha ejecutado una celda anterior, o Colab se desconectó y se olvidó de todo. | Ejecutad desde la primera celda hacia abajo, una a una, hasta la que falla. |
| `NameError: name 'contar_por_clase' is not defined` | La celda del ejercicio 1 todavía tiene los `...` y no define la función. | Borrad los tres puntos, escribid la función y volved a pulsar ▶. |
| `TypeError: object of type 'NoneType' has no len()` | La función no devuelve nada: falta el `return`. | Poned `return conteo` como última línea, con 4 espacios de sangría. |
| `NotADirectoryError: [Errno 20] Not a directory: 'datos_sinteticos/alojamientos/_ambiguas.csv'` | Se ha tratado como clase el archivo suelto `_ambiguas.csv`, que crea el cuaderno como lista de apoyo del docente. | Añadid `if os.path.isdir(carpeta):` como en el código de arriba. Ignorad ese archivo: las dudosas se encuentran mirando las fotos. |
| `AssertionError: Debe haber al menos 2 subcarpetas…`, `Hay alguna clase sin imágenes` o `El dataset sintético debe tener 60 imágenes en cada una de las 5 clases` | El diccionario no sale como se espera. | Escribid `print(conteo)` y mirad qué clase falla. Si la carpeta se quedó a medias, eliminad `datos_sinteticos` en el panel de archivos (📁, clic derecho → *Eliminar*) y ejecutad de nuevo la celda del apartado 1. |
| `ValueError: No images found in directory …` | Con fotos propias: la ruta de `RUTA_PROPIA` no existe o sus carpetas no tienen imágenes. | Comprobad el nombre de la carpeta en el panel 📁 y que cada clase tenga fotos `.png`, `.jpg` o `.jpeg`. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_11.md) · [Paso 2 →](Reto_Sprint_11_paso_2.md)
<!--/nav-->
