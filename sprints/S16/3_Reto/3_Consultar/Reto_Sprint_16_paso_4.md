# Paso 4 · Pulir el demostrador y probarlo en limpio (día 2, 40 minutos)

<!--nav-->
> Sprint 16 · Reto «Entrega final: evaluar, demostrar y documentar» · paso 4 de 8 · [Ficha del reto](Reto_Sprint_16.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_16_una_pagina.md) · [Paso 5 →](Reto_Sprint_16_paso_5.md)
<!--/nav-->

1. Adaptar el aviso de incertidumbre y las validaciones de `logica.py` a vuestro proyecto.
2. Probar a mano cinco entradas: tres normales, una imposible y una vacía.
3. Escribir tres pruebas propias con `pytest` y fijar las versiones en `requirements.txt`.
4. Lanzarlo en una carpeta nueva siguiendo solo el README.

**En sencillo.** Hasta ahora el demostrador funciona con los datos que vosotros le dais. Hoy lo preparáis para alguien que no sabe nada del modelo: que no se rompa cuando escribe una tontería, que le avise de que el modelo se equivoca y que arranque en un ordenador que no es el vuestro. Es como probar una receta en la cocina de un amigo: si solo sale bien en la vuestra, no está terminada. Las «pruebas automáticas» son comprobaciones de sentido común que el ordenador repite en un segundo (por ejemplo, que una reserva flexible y sin depósito tiene más riesgo que una no reembolsable). No hace falta programar a fondo: cambiáis unos textos, pegáis unos bloques que ya funcionan y escribís unas pocas órdenes que os damos hechas.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Validación** | Comprobar que lo que escribe quien usa el demostrador tiene sentido: un número donde toca un número, dentro del rango permitido. |
| **Regla entre campos** | Validación que mira dos campos a la vez (por ejemplo, noches × precio no puede pasar de 5000 €). La validación campo a campo no la detecta. |
| **Prueba automática** | Función que se llama `test_…` y comprueba algo con `assert` («esto tiene que ser cierto»). Si no lo es, la prueba falla. |
| **`pytest`** | Programa que encuentra todas las pruebas y las ejecuta. Dibuja un símbolo por prueba: `.` pasa, `F` falla, `s` se salta. |
| **`requirements.txt`** | Lista de las librerías que necesita el proyecto, cada una con su versión fija (`scikit-learn==1.9.1`). |
| **Versión fija** | El número exacto de una librería, con `==`. Sin él, otra persona instala una versión más nueva y el modelo puede no cargar o dar otros números. |
| **Entorno virtual (`.venv`)** | Carpeta donde se instalan las librerías de un solo proyecto. Sirve para probar en un «ordenador limpio». |
| **Terminal** | Ventana donde se escriben órdenes como `pytest -q`. En Visual Studio Code: menú **Terminal → Nuevo terminal**. |

**Cómo se hace**

1. **Preparar la carpeta y la terminal (2 minutos).** Trabajad con una copia de `demostrador/` que tenga dentro la carpeta `modelo/` con `modelo_cancelaciones.joblib` y `metadatos.json` (la crea el cuaderno `S16_01` o vuestro entrenamiento). Este paso se hace en un ordenador, no en Colab: Streamlit no se abre en Colab. Si el modelo está en Colab, comprimid la carpeta con `!zip -r demostrador.zip demostrador` y descargad el ZIP desde el panel de archivos. En Visual Studio Code: **Archivo → Abrir carpeta** (elegid `demostrador`) y **Terminal → Nuevo terminal**. Escribid `ls` (Mac y Linux) o `dir` (Windows): tienen que salir `app.py`, `logica.py`, `modelo` y `tests`.

2. **Escribir el aviso de incertidumbre (4 minutos).** Abrid `modelo/metadatos.json`. Cada resultado del demostrador lleva un aviso que construye `logica.py` con dos campos de ese archivo: `auc_test` (no lo toquéis: es la cifra del modelo) y `limitaciones` (vuestro texto, el último campo). Reescribid `limitaciones` con tres cosas: con qué datos se entrenó, dónde falla (lo que ya sabéis por los pasos 1 y 3 y por la model card, apartado 4) y qué usos no se permiten. Ejemplo con TurisData:

    ```json
      "limitaciones": "Entrenado con datos sintéticos de un solo alojamiento ficticio. Detecta peor las cancelaciones del canal directo (ver model card, apartado 4). No usar para decidir sobre personas concretas: solo orienta la gestión de disponibilidad."
    ```

    Qué hay que respetar:

    - Dejad las comillas, escribid todo en **una sola línea** y no pongáis coma al final (es el último campo del archivo).
    - El `auc_test` tiene que coincidir con el AUC del paso 1 y de la model card. En la plantilla de TurisData no coinciden (0,746 en el demostrador y 0,744 en el cuaderno de evaluación) porque el demostrador usa 11 variables y otra partición. En vuestro proyecto el modelo es el mismo: las cifras tienen que ser iguales.
    - Si volvéis a ejecutar la celda del cuaderno que guarda el modelo, este archivo se sobrescribe.
    - Si vuestro demostrador es un asistente, tiene que decir que es una IA y citar sus fuentes; si es de imágenes, avisar de que una imagen rara queda fuera de lo que conoce. Está en «Qué adaptar en vuestro proyecto» del [`README_demostrador.md`](../1_Trabajar/plantillas/demostrador/).

3. **Añadir una regla que cruce dos campos (7 minutos).** Abrid `logica.py`. Primero pegad esta función justo antes de `def nivel_riesgo(probabilidad):`:

    ```python
    def validar_coherencia(reserva):
        """Reglas que cruzan varios campos. Solo se llama cuando cada campo ya es válido por separado."""
        errores = []
        importe = reserva["noches"] * reserva["precio_noche"]
        if importe > 5000:
            errores.append(f"El importe total supera los 5000 € (son {importe:.0f} €). Revisa las noches y el precio.")
        return errores
    ```

    Qué hace cada línea:

    - `def validar_coherencia(reserva):` crea la función. `reserva` es el diccionario con lo que ha escrito la persona.
    - `errores = []` es la lista donde se apuntan los problemas. Vacía significa «todo bien».
    - `importe = reserva["noches"] * reserva["precio_noche"]` multiplica dos campos. Los nombres entre comillas tienen que ser **exactamente** los de `meta["campos"]`.
    - `if importe > 5000:` se cumple solo si la regla se rompe. `errores.append(f"…")` añade el mensaje; `{importe:.0f}` escribe el número sin decimales. El mensaje dice qué falla y qué hacer.
    - `return errores` devuelve la lista.

    Después, dentro de `predecir_reserva`, sustituid estas dos líneas:

    ```python
        errores = validar_reserva(reserva, meta)
        if errores:
            return {"errores": errores}
    ```

    por estas cuatro:

    ```python
        errores = validar_reserva(reserva, meta)
        if not errores:
            errores = validar_coherencia(reserva)
        if errores:
            return {"errores": errores}
    ```

    Qué hace el cambio: `if not errores:` significa «si no hay errores». La regla nueva solo se mira cuando cada campo ya es válido; si se mirase antes, un campo que falta daría `KeyError: 'noches'`. Cambiad la regla de ejemplo por una de **vuestro** proyecto (por ejemplo, una fecha de salida anterior a la de entrada). La regla «niños sin adultos» del ejercicio 1 de `S16_01` aquí no hace falta: `adultos` ya tiene mínimo 1.

4. **Probar a mano cinco entradas (6 minutos).** Cread en `demostrador/` el archivo `probar_a_mano.py` (en VS Code: botón derecho en la carpeta → **Nuevo archivo**) con este código:

    ```python
    from logica import cargar_modelo, predecir_reserva

    modelo, meta = cargar_modelo()

    normal = {"antelacion_dias": 120, "noches": 5, "adultos": 2, "ninos": 1, "precio_noche": 95.0, "cliente_repetidor": 0,
              "cancelaciones_previas": 0, "tipo_habitacion": "estandar", "canal": "web_intermediaria",
              "tarifa": "flexible", "deposito": "sin_deposito"}

    pruebas = {
        "normal 1": normal,
        "normal 2": {**normal, "antelacion_dias": 7, "tarifa": "no_reembolsable", "deposito": "total", "canal": "directo"},
        "normal 3": {**normal, "adultos": 1, "ninos": 0, "noches": 3, "tipo_habitacion": "suite", "precio_noche": 180.0, "cliente_repetidor": 1},
        "imposible": {**normal, "antelacion_dias": 5000},
        "vacía": {},
    }

    for nombre, entrada in pruebas.items():
        r = predecir_reserva(entrada, modelo, meta)
        if r["errores"]:
            print(f"{nombre}: {len(r['errores'])} errores · {r['errores'][0]}")
        else:
            print(f"{nombre}: riesgo {r['nivel']} ({r['probabilidad']:.0%}) · media histórica {r['tasa_base']:.0%}")
    ```

    Qué hace cada línea:

    - `from logica import …` trae las dos funciones de `logica.py`; por eso el archivo tiene que estar en la misma carpeta.
    - `modelo, meta = cargar_modelo()` carga el modelo y `metadatos.json`.
    - `normal = {…}` es una reserva completa y válida. Cambiad los nombres y valores por los campos de **vuestro** proyecto, escritos igual que en `meta["campos"]`.
    - `{**normal, "antelacion_dias": 7}` copia `normal` y cambia solo lo que indicáis. Así cada prueba son dos o tres datos, no once.
    - `"imposible"` tiene que ser un valor absurdo de vuestro proyecto (una edad de 250, una fecha del año 3000). `"vacía": {}` es una entrada sin ningún dato.
    - El bucle `for` ejecuta las cinco y escribe una línea por cada una. `{r['probabilidad']:.0%}` muestra el número como porcentaje sin decimales.

    Ejecutadlo en la terminal con `python probar_a_mano.py`. Las tres normales dan un nivel y un porcentaje; la imposible y la vacía dan un mensaje claro y **ningún error rojo de Python**. Si sale un error rojo, el demostrador no está listo: arreglad `logica.py` hasta que las cinco funcionen.

5. **Escribir tres pruebas propias (7 minutos).** Abrid `tests/test_logica.py`. Cambiad el diccionario `RESERVA` (la línea que termina en `# >>> ADAPTA`) por una reserva de vuestro proyecto. Después pegad **al final del archivo** estas tres pruebas:

    ```python
    def test_flexible_sin_deposito_tiene_mas_riesgo(modelo_y_meta):
        modelo, meta = modelo_y_meta
        flexible = {**RESERVA, "tarifa": "flexible", "deposito": "sin_deposito"}
        segura = {**RESERVA, "tarifa": "no_reembolsable", "deposito": "total"}
        assert predecir_reserva(flexible, modelo, meta)["probabilidad"] > predecir_reserva(segura, modelo, meta)["probabilidad"]


    def test_entrada_vacia_avisa_de_todos_los_campos(modelo_y_meta):
        modelo, meta = modelo_y_meta
        r = predecir_reserva({}, modelo, meta)
        assert len(r["errores"]) == len(meta["campos"]) and "probabilidad" not in r


    def test_importe_demasiado_alto_se_rechaza(modelo_y_meta):
        modelo, meta = modelo_y_meta
        r = predecir_reserva({**RESERVA, "noches": 20, "precio_noche": 400.0}, modelo, meta)
        assert r["errores"] and r["errores"][0].startswith("El importe total supera los 5000 €")
    ```

    Qué hace cada línea:

    - `def test_…(modelo_y_meta):` el nombre **tiene que empezar por `test_`** o `pytest` no la ejecuta. `modelo_y_meta` es la carga del modelo que ya trae el archivo: no la toquéis.
    - `{**RESERVA, "tarifa": …}` copia la reserva de ejemplo y cambia solo esos campos.
    - `assert A > B` significa «A tiene que ser mayor que B». Si no lo es, la prueba falla y `pytest` lo cuenta.
    - La primera prueba es de **sentido común del modelo**, la segunda de **entrada vacía** y la tercera de **entrada imposible** (usa la regla del punto 3). Sustituidlas por tres reglas de vuestro proyecto, una de cada tipo.

    En la terminal, desde `demostrador/`, escribid `pytest -q`. Si `pytest` no está instalado, `pip install pytest` antes.

6. **Fijar las versiones (4 minutos).** Abrid `requirements.txt`. La plantilla trae las versiones del entorno del curso, que **no son necesariamente las vuestras**. Dejad solo lo que usáis, cada librería con `==` y con la versión **con la que guardasteis el modelo**: están en `modelo/metadatos.json`, campo `versiones` (`python`, `scikit-learn`, `pandas`, `numpy`). Para `joblib`, `streamlit` y `pytest` escribid `pip show joblib streamlit pytest` en la terminal y copiad las líneas `Version:`. Quitad `ipywidgets`, `fastapi` y `uvicorn` si no usáis los *widgets* ni `api.py`. Con TurisData queda:

    ```text
    numpy==2.5.3
    pandas==2.3.3
    scikit-learn==1.9.1
    joblib==1.6.0
    streamlit==1.64.0
    pytest==9.1.1
    ```

    Si la versión de `scikit-learn` no coincide con la del modelo, al cargarlo sale un `InconsistentVersionWarning` (mirad la tabla de abajo). Después añadid arriba de `README_demostrador.md` cuatro líneas con la versión de Python (`python` de `versiones`) y las órdenes exactas:

    ```text
    Python: 3.13 (la del campo "versiones" de modelo/metadatos.json)
    Instalar: pip install -r requirements.txt
    Lanzar: streamlit run app.py   (se abre en http://localhost:8501)
    Probar: pytest -q
    ```

7. **Probarlo en limpio con otra persona (8 minutos).** Lo hace alguien que **no ha escrito** el código, siguiendo **solo el README**, con la persona que lo escribió al lado y sin ayudar. Copiad `demostrador/` a una carpeta nueva (por ejemplo, en el Escritorio), abridla en VS Code, abrid una terminal y escribid:

    ```text
    python -m venv .venv
    .venv\Scripts\activate
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest -q
    streamlit run app.py
    ```

    Qué hace cada orden:

    - `python -m venv .venv` crea el entorno limpio en la carpeta `.venv`.
    - Las dos siguientes **activan** el entorno: la de `.venv\Scripts\activate` es para Windows y la de `source …` para Mac y Linux. Escribid solo la que os toque. Si ha funcionado, la línea de la terminal empieza por `(.venv)`.
    - `pip install -r requirements.txt` instala lo de la lista. Tarda unos minutos.
    - `pytest -q` pasa las pruebas y `streamlit run app.py` abre la app en el navegador.

    En la app probad las mismas entradas: una normal, una imposible (el cuadro amarillo tiene que decir qué campo falla) y una vacía (borrad el número de una casilla). Cada vez que quien prueba tenga que **adivinar** algo, apuntadlo y añadidlo al README.

8. **Subir los cambios (2 minutos).** Subid a `sprint-16/demostrador/` del repositorio los archivos cambiados (`logica.py`, `tests/test_logica.py`, `requirements.txt`, `README_demostrador.md`, `probar_a_mano.py` y la carpeta `modelo/`) con **Add file → Upload files**, como explica [Cómo entregar en GitHub](../../../../material/5.%20Como_entregar_en_GitHub.md). **No subáis** la carpeta `.venv/`, que pesa cientos de megas, ni `__pycache__/`.

**Qué deberíais ver.**
- **`python probar_a_mano.py`**, con el ejemplo de TurisData:

    ```text
    normal 1: riesgo alto (81%) · media histórica 46%
    normal 2: riesgo bajo (4%) · media histórica 46%
    normal 3: riesgo alto (63%) · media histórica 46%
    imposible: 1 errores · 'antelacion_dias' debe estar entre 1 y 400 (has escrito 5000).
    vacía: 11 errores · Falta el campo 'antelacion_dias'.
    ```

- **`pytest -q`:** `........` y debajo `8 passed in 1.4s` (el tiempo cambia). Son las 5 pruebas de la plantilla y vuestras 3.
- **`streamlit run app.py`:** en la terminal, `You can now view your Streamlit app in your browser.` y `Local URL: http://localhost:8501`. En el navegador, el formulario. Con los valores que trae por defecto, **Calcular riesgo** da `Probabilidad de cancelación 25%` (`-20% frente a la media`), `Nivel de riesgo BAJO`, una barra y un cuadro azul con el aviso. Con una antelación de 5000 sale un cuadro amarillo: `No se puede calcular todavía:` y `- 'antelacion_dias' debe estar entre 1 y 400 (has escrito 5000).` Si borráis un número, `- Falta el campo …`. Nunca un cuadro rojo con un error de Python.

**Hecho cuando:** el demostrador se lanza en una carpeta limpia con las órdenes del README, no se rompe con las cinco entradas de prueba, el aviso de incertidumbre sale en cada resultado y `pytest -q` pasa con vuestras tres pruebas.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `....F...` y al final `1 failed, 7 passed` | Una prueba ha fallado: hay un error en el código o el modelo contradice el sentido común. | Leed las líneas que empiezan por `>` y `E`: dicen qué comparación falló. Si es el modelo quien contradice la regla, no cambiéis la prueba para que pase: apuntadlo como límite en la model card. |
| `ssss.sss` y `1 passed, 7 skipped`, o en la app un cuadro rojo con `Falta el modelo. Ejecuta primero el notebook S16_01…` | No encuentra la carpeta `modelo/`, así que se saltan las pruebas. | Comprobad que `modelo/` está al lado de `logica.py` con sus dos archivos y que lanzáis `pytest -q` desde `demostrador/`. |
| `ModuleNotFoundError: No module named 'streamlit'` (o `'sklearn'`, `'pytest'`) | La librería no está instalada en el entorno que estáis usando. | Con el entorno activado (la línea empieza por `(.venv)`), `pip install -r requirements.txt`. |
| `python: can't open file '…probar_a_mano.py': [Errno 2] No such file or directory` | La terminal no está en la carpeta `demostrador/`. | Abrid la carpeta en VS Code (**Archivo → Abrir carpeta**) y abrid una terminal nueva. |
| `KeyError: 'noches'` (o el nombre de otro campo) | `validar_coherencia` se ejecutó con un campo que falta. | Llamadla solo dentro de `if not errores:`, como en el punto 3. |
| `InconsistentVersionWarning: Trying to unpickle estimator Pipeline from version 1.9.1 when using version 1.8.0` | `requirements.txt` fija otra versión de `scikit-learn` que la del modelo guardado. | Poned en `requirements.txt` la versión de `versiones` en `metadatos.json` y repetid `pip install -r requirements.txt`. |
| `"python" no se reconoce como un comando interno o externo` (Windows) o `command not found: python` (Mac) | La terminal no encuentra Python. | Probad `python3` en lugar de `python`. Si tampoco, usad la terminal de Visual Studio Code del aula. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_16_paso_3.md) · [Ficha del reto](Reto_Sprint_16.md) · [Paso 5 →](Reto_Sprint_16_paso_5.md)
<!--/nav-->
