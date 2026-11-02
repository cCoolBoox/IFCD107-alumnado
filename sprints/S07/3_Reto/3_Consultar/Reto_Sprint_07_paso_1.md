# Paso 1 · Acordar las hipótesis de coste y abrir el cuaderno (día 1, 5 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 1 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md) · [Paso 2 →](Reto_Sprint_07_paso_2.md)
<!--/nav-->

1. Abrir un cuaderno nuevo en Colab con el nombre `reto_S07`.
2. Responder la pregunta central: ¿qué cuesta más, una cancelación no prevista o una falsa alarma?
3. Escribir una hipótesis de coste para cada error, con una frase de razón.

**En sencillo.** Un modelo que avisa de cancelaciones se puede equivocar de dos maneras, y **cada una cuesta dinero distinto**. Es como una aerolínea que vende más billetes que asientos: si cuenta con que algunos pasajeros no se presentan y acierta, llena el avión; si cuenta con ello y se presentan todos, tiene que compensar a quien se queda en tierra. En el hotel pasa lo mismo, y el modelo solo sirve si sabéis cuánto pesa cada error. Aquí no hay modelos todavía: abrís el cuaderno, miráis dos números de los datos (cuánto cuesta una noche y cuántas noches dura una reserva) y os ponéis de acuerdo en dos cifras en euros, cada una con su razón. No hace falta saber Python: la celda se copia y se ejecuta.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Falso negativo (FN)** | El modelo dice «no se cancelará» y **sí** se cancela. La habitación queda vacía. |
| **Falso positivo (FP)** | El modelo dice «se cancelará» y **no** se cancela. Es una falsa alarma: el cliente llega y puede no haber sitio. |
| **Hipótesis de coste** | Una cifra en euros que el equipo propone para cada error, con una frase que explica de dónde sale. |
| **Variable** | Un nombre que guarda un valor, como `COSTE_FN = 284`. Se escribe en mayúsculas cuando es una cifra que fijáis vosotros. |
| **Comentario (`#`)** | Texto tras un `#`: Python lo ignora. Aquí guarda la razón de cada coste. |
| **`DataFrame`** | La tabla de datos que usa pandas. Aquí se llama `df` y tiene una fila por reserva. |
| **`.mean()`** | Calcula la media de una columna. |

**Cómo se hace**

1. **Abrir el cuaderno.** En [Colab](https://colab.research.google.com), *Archivo → Nuevo cuaderno* y renombradlo `reto_S07`. Con *Compartir* (arriba a la derecha) dad acceso de editor al resto del equipo. Una persona escribe y las demás proponen. Cada bloque de código de abajo va en una **celda nueva** (*+ Código*) y se ejecuta con el botón ▶ o con Mayús + Intro, siempre de arriba abajo.

2. **Preparar y cargar los datos.** Primera celda. Es la celda «Preparación» de [`S07_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S07/2_Practica/S07_01_regresion_lineal_polinomica.ipynb), junto con la carga del CSV:

    ```python
    import os, urllib.request
    import numpy as np
    import pandas as pd

    BASE_URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/"

    def dato(nombre):
        """Devuelve la ruta local de un archivo de datos del curso (lo descarga si no está)."""
        for carpeta in ("datos", "../datos", "../../datos"):
            ruta = os.path.join(carpeta, nombre)
            if os.path.exists(ruta):
                return ruta
        os.makedirs("datos", exist_ok=True)
        ruta = os.path.join("datos", nombre)
        urllib.request.urlretrieve(BASE_URL + nombre, ruta)
        return ruta

    SEMILLA = 42

    df = pd.read_csv(dato("reservas_turisdata.csv"), parse_dates=["fecha_reserva", "fecha_llegada"])
    df["mes_llegada"] = df["fecha_llegada"].dt.month
    df["temporada_alta"] = df["mes_llegada"].isin([1, 2, 3, 7, 8, 12]).astype(int)
    print(df.shape)
    ```

    Qué hace cada línea:

    - `import … as pd`: trae las herramientas (`pandas` para tablas, `numpy` para números). Los nombres cortos `pd` y `np` no se cambian.
    - `def dato(nombre):`: una función que busca el fichero en la carpeta del curso y, si no está, lo descarga de GitHub. No hace falta tocarla.
    - `SEMILLA = 42`: el número que fija el azar para que todo salga igual en cada ejecución.
    - `df = pd.read_csv(…)`: lee `reservas_turisdata.csv` y lo guarda en `df`. `parse_dates` avisa de que esas dos columnas son fechas.
    - `df["mes_llegada"] = …`: crea una columna nueva con el mes (1 a 12) de la fecha de llegada.
    - `df["temporada_alta"] = …`: crea otra con un 1 si el mes es enero, febrero, marzo, julio, agosto o diciembre, y un 0 si no.
    - `print(df.shape)`: escribe (filas, columnas).

3. **Entender los dos errores.** Hablad con esta tabla delante. Es la pregunta central de todo el reto:

    | El modelo dice | En realidad | Cómo se llama | Qué pasa en el hotel |
    |---|---|---|---|
    | «No se cancelará» | **Sí** se cancela | Falso negativo (FN) | La habitación queda vacía y no se vende: se pierde parte de las noches. |
    | «Se cancelará» | **No** se cancela | Falso positivo (FP) | Se sobrevende, el cliente llega y no hay sitio: hay que compensarle. |

4. **Mirar el precio medio y las noches medias.** Celda nueva. Sirve para pasar «una noche» a euros:

    ```python
    precio_medio = df["precio_noche"].mean()
    noches_medias = df["noches"].mean()
    print(round(precio_medio, 2), "€ por noche ·", round(noches_medias, 1), "noches por reserva")
    print(round(0.5 * noches_medias * precio_medio), "€ ≈ la mitad de las noches de una reserva media")
    ```

    Qué hace cada línea:

    - `df["precio_noche"].mean()`: la media de la columna de precios. `noches_medias` hace lo mismo con las noches.
    - `round(x, 2)`: redondea a 2 decimales (y `round(x, 1)`, a 1). Sin el segundo número, redondea a entero.
    - `0.5 * noches_medias * precio_medio`: la mitad de lo que ingresa una reserva media. Es la cuenta del ejemplo de abajo.

5. **Escribir las hipótesis de coste.** Cada persona propone una cifra en un minuto y elegís una por cada error. Celda nueva, **con la razón al lado**:

    ```python
    COSTE_FN = 284   # cancelación no prevista: reserva media de 5,5 noches a ~103 €; solo se revende la mitad (0,5 × 5,52 × 102,87 ≈ 284 €)
    COSTE_FP = 103   # falsa alarma: una noche de compensación (otro alojamiento y una disculpa) ≈ precio medio de una noche
    ```

    Qué hace cada línea:

    - `COSTE_FN = 284`: guarda en la variable `COSTE_FN` lo que cuesta cada falso negativo, en euros. `COSTE_FP`, lo de cada falso positivo. **Los dos nombres no se cambian**: los usan los pasos 3 y 4.
    - Lo que va tras `#`: la razón. Sin razón, el coste no vale.
    - Las cifras 284 y 103 son un ejemplo con estos datos. Podéis elegir otras si las razonáis, pero cada coste necesita su frase. La razón es la del enunciado: solo se revende la mitad de las noches de una reserva media, y de ahí sale la cuenta de arriba.

**Qué deberíais ver.** Una celda con `SEMILLA`, `COSTE_FN` y `COSTE_FP`, cada coste con su razón al lado, y el CSV cargado en un `DataFrame`. Con el CSV del curso:

- `(6000, 20)`: 6000 reservas y 20 columnas (las 18 del fichero más `mes_llegada` y `temporada_alta`).
- `102.87 € por noche · 5.5 noches por reserva`.
- `284 € ≈ la mitad de las noches de una reserva media`.

**Hecho cuando:** el cuaderno abre y carga los datos, y las dos hipótesis de coste están escritas con su razón.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'pd' is not defined` | La celda de preparación no se ha ejecutado (o Colab se reinició). | Ejecutadla primero y luego las demás, de arriba abajo. |
| `NameError: name 'df' is not defined` | Se ejecutó la celda del precio medio antes de cargar los datos. | Ejecutad la celda 2 y repetid. |
| `HTTPError: HTTP Error 404: Not Found` | La dirección de `BASE_URL` o el nombre del fichero tienen una errata. | Copiad de nuevo la celda y comprobad `reservas_turisdata.csv`, en minúsculas. |
| `KeyError: 'precio_noches'` | El nombre de la columna no es exacto. | Copiad el nombre de `df.columns`. |
| Una celda se ejecuta pero no muestra nada | Colab enseña solo la **última** expresión de la celda. | Envolvedlo en `print(…)`. |
| El equipo no se pone de acuerdo en las cifras | Cada persona imagina un hotel distinto. | Apuntad las dos hipótesis, con razón, y seguid: el paso 4 prueba qué pasa si cambian. |

<!--nav-->
---

[Ficha del reto](Reto_Sprint_07.md) · [Paso 2 →](Reto_Sprint_07_paso_2.md)
<!--/nav-->
