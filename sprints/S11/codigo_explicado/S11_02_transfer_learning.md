# Código explicado · S11.02 · S11 · Práctica 2 — *Transfer learning* y *fine-tuning*

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_02_transfer_learning.ipynb) · [descargar](../notebooks/S11_02_transfer_learning.ipynb) · ⏱ en clase: 75 min · 🏫 7 celdas de código en clase · 🏠 5 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_random_seed`. |
| 2 | 0. Generador de imágenes sintéticas | Practica `tuple`, `astype`, `new`, `Draw` y más (sección «0. Generador de imágenes sintét… |
| 3 | 0. Generador de imágenes sintéticas | Practica `subplots`, `suptitle`, `tight_layout`, `imshow` y más (sección «0. Generador de… |
| 4 | 1. La tarea real, con pocos datos | Practica `partial`, `shape` (sección «1. La tarea real, con pocos datos»). |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `CLASES_ALOJ` | `["hotel", "apartamentos", "casa_rural", "camping", "pisci…` | 2 |
| `CLASES_FORMAS` | `["rayas_horizontales", "rayas_verticales", "diagonales",…` | 2 |
| `PARECIDAS` | `{"hotel": "apartamentos", "apartamentos": "hotel", "casa_…` | 2 |
| `N_POR_CLASE` | `6` | 4 |
| `alojamiento` | `functools.partial(dibujar_alojamiento, ruido=40)` | 4 |
| `desde_cero` | `con_cabeza(construir_base("base_desde_cero"), 5)` | 5 |
| `h_cero` | `entrenar(desde_cero, epocas=40)` | 5 |
| `acc_cero` | `desde_cero.evaluate(X_pru, y_pru, verbose=0)[1]` | 5 |
| `base_pre` | `construir_base("base_preentrenada")` | 6 |
| `modelo_aux` | `con_cabeza(base_pre, len(CLASES_FORMAS), dropout=0.0)` | 6 |
| `transfer` | `con_cabeza(copia_base, 5)` | 8 |
| `n_entrenables` | `sum(int(np.prod(p.shape)) for p in transfer.trainable_wei…` | 8 |
| `h_transfer` | `entrenar(transfer, epocas=30)` | 8 |
| `acc_transfer` | `transfer.evaluate(X_pru, y_pru, verbose=0)[1]` | 8 |
| `n_ent_ft` | `descongelar_bloque(copia_base, 3)` | 10 |
| `h_ft` | `entrenar(transfer, epocas=25, semilla=1)` | 10 |
| `acc_ft` | `transfer.evaluate(X_pru, y_pru, verbose=0)[1]` | 10 |
| `filas` | `[experimento(s) for s in (1, 2, 3)]` | 11 |
| `comparacion` | `pd.DataFrame(filas, columns=["Desde cero", "Base congelad…` | 11 |
| `USAR_INTERNET` | `False` | 14 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `_color` | Color aleatorio cercano a `base` (tupla RGB). |
| `_final` | Convierte a uint8 con un poco de ruido y variación de brillo. |
| `_ventanas` | Cuadrícula de ventanas dentro del rectángulo (x0, y0, x1, y1). |
| `dibujar_alojamiento` | Dibujo esquemático (tam×tam×3, uint8) de un tipo de alojamiento. Datos SINTÉTICOS, no fotos reales. |
| `dibujar_forma` | Formas y texturas abstractas (tarea auxiliar de preentrenamiento). Devuelve tam×tam×3 uint8. |
| `generar_lote` | Devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas. |
| `crear_dataset_carpetas` | Escribe PNG en carpeta/<clase>/img_000.png (estructura que espera image_dataset_from_directory). |
| `construir_base` | Función definida en el cuaderno. |
| `con_cabeza` | Base + cabeza nueva (Dropout y Dense softmax), ya compilado. |
| `entrenar` | Función definida en el cuaderno. |
| `congelar` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `copiar_base` | Copia independiente de la base con los mismos pesos (para no modificar la original). *(La escribís vosotros en un ejercicio.)* |
| `descongelar_bloque` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `experimento` | Devuelve la precisión en prueba de (desde cero, base congelada, base con fine-tuning). |
| `construir_mobilenet` | pesos=None (aleatorios, offline) o pesos='imagenet' (requiere internet, se descarga ≈ 10 MB). |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `abs` | Valor absoluto: quita el signo negativo. | 2 |
| `Adam` | Optimizador Adam: decide cómo ajustar los pesos en cada paso. | 5, 10, 11, 13, 14 |
| `agg` | Calcula varias estadísticas a la vez (media, suma…) por grupo. | 11 |
| `append` | Añade un elemento al final de una lista. | 2 |
| `arange` | Crea una secuencia de números con un paso fijo. | 2 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 2 |
| `asarray` | Convierte algo en array de NumPy sin copiarlo si ya lo es. | 2 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 2 |
| `axis` | Controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas. | 3 |
| `base` | La red preentrenada que se reutiliza (el «cuerpo» del modelo). | 5, 13 |
| `choice` | Elige un elemento al azar. | 2 |
| `clip` | Limita los valores a un mínimo y un máximo. | 2 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 5, 10, 11, 13, 14 |
| `Conv2D` | Capa convolucional: detecta patrones (bordes, formas) en imágenes. | 5 |
| `count_params` | Cuenta cuántos pesos tiene el modelo. | 6, 8, 13 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 11 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 2 |
| `Dense` | Capa de neuronas totalmente conectadas. | 5, 13 |
| `Draw` | Dibuja sobre una imagen (clase de Pillow). | 2 |
| `Dropout` | Capa que apaga neuronas al azar al entrenar para evitar el sobreajuste. | 5, 13 |
| `ellipse` | Dibuja una elipse. | 2 |
| `enumerate` | Recorre una lista dando a la vez la posición y el valor. | 5 |
| `evaluate` | Calcula la pérdida y las métricas del modelo con unos datos. | 5, 6, 8, 10, 11, 14 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 5, 6, 14 |
| `Flatten` | Capa que aplana la imagen en un vector. | 5 |
| `fromarray` | Convierte un array de NumPy en imagen. | 2 |
| `funcion` | La función que se pasa como argumento y se llama dentro. | 2 |
| `GlobalAveragePooling2D` | Capa que resume cada mapa de características en un solo número (su media). | 13 |
| `imshow` | Muestra una imagen o una matriz como imagen. | 3 |
| `Input` | Define la forma de los datos de entrada del modelo. | 5, 13 |
| `int` | Convierte un valor en número entero. | 2, 8, 13 |
| `integers` | Genera números enteros aleatorios. | 2 |
| `join` | Une una lista de textos en uno solo con un separador. | 2 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2, 5, 6, 13 |
| `line` | Dibuja una línea. | 2 |
| `loc` | Selecciona filas/columnas por su etiqueta o por una condición. | 12 |
| `makedirs` | Crea una carpeta (y las que falten). | 2 |
| `max` | Devuelve el valor más grande. | 2 |
| `MaxPooling2D` | Capa que reduce la imagen quedándose con el valor máximo de cada zona. | 5 |
| `MobileNetV2` | Red ya entrenada con millones de imágenes, lista para reutilizar. | 13 |
| `Model` | Crea un modelo de Keras indicando entradas y salidas. | 5, 13 |
| `new` | Crea una imagen nueva en blanco (Pillow) del tamaño y color indicados. | 2 |
| `normal` | Genera números aleatorios con forma de campana (normal). | 2 |
| `open` | Abre un fichero para leerlo o escribirlo. | 2 |
| `partial` | Fija algunos argumentos de una función. | 4 |
| `permutation` | Devuelve un orden aleatorio de los índices. | 2 |
| `plot` | Dibuja una línea (o puntos unidos). | 12 |
| `polygon` | Dibuja un polígono. | 2 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 13 |
| `preprocess_input` | Prepara las imágenes como espera la red preentrenada. | 13 |
| `print` | Muestra un valor por pantalla. | 4, 5, 6, 8, 10, 13… |
| `prod` | Multiplica todos los valores. | 8, 13 |
| `random` | Número aleatorio entre 0 y 1. | 2 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 2, 3 |
| `rectangle` | Dibuja un rectángulo. | 2 |
| `repeat` | Repite cada elemento varias veces. | 2 |
| `Rescaling` | Capa de Keras que reescala los píxeles (por ejemplo, de 0–255 a 0–1). | 5 |
| `resize` | Cambia el tamaño de una imagen. | 2 |
| `Resizing` | Capa de Keras que cambia el tamaño de las imágenes. | 13 |
| `round` | Redondea un número a los decimales indicados. | 6, 11, 13, 14 |
| `save` | Guarda el modelo (o el objeto) en un fichero. | 2 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 1, 5, 6, 11 |
| `set_title` | Pone el título de un gráfico. | 3 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2, 4, 8, 13 |
| `show` | Muestra el gráfico. | 3, 12 |
| `stack` | Apila arrays en una dimensión nueva. | 2 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 3 |
| `sum` | Suma todos los valores. | 2, 8, 13 |
| `suptitle` | Pone un título general a toda la figura. | 3 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 3 |
| `title` | Pone el título del gráfico. | 12 |
| `tuple` | Crea una tupla (como una lista que no se puede modificar). | 2 |
| `uniform` | Número aleatorio decimal entre dos límites. | 2 |
| `write` | Escribe en un fichero. | 2 |
| `xticks` | Fija las marcas del eje horizontal. | 12 |
| `ylabel` | Pone el nombre del eje vertical. | 12 |
| `ylim` | Fija el rango del eje vertical. | 12 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_random_seed`.

```python
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import functools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

SEMILLA = 42
keras.utils.set_random_seed(SEMILLA)
```

**Qué hace cada línea:**

- `import os` → Trae `os` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import functools` → Trae `functools` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import tensorflow as tf` → Trae `tensorflow` (lo llamamos `tf`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- … y 1 más con las mismas ideas.

### Celda 2 · 0. Generador de imágenes sintéticas · 🏫

**Qué hace:** Practica `tuple`, `astype`, `new`, `Draw` y más (sección «0. Generador de imágenes sintéticas»).

```python
from PIL import Image, ImageDraw

CLASES_ALOJ = ["hotel", "apartamentos", "casa_rural", "camping", "piscina"]
CLASES_FORMAS = ["rayas_horizontales", "rayas_verticales", "diagonales", "cuadricula", "puntos", "circulo", "rectangulo", "triangulo"]


def _color(rng, base, var=30):
    """Color aleatorio cercano a `base` (tupla RGB)."""
    return tuple(int(np.clip(c + rng.integers(-var, var + 1), 0, 255)) for c in base)


def _final(img, rng, ruido=8):
    """Convierte a uint8 con un poco de ruido y variación de brillo."""
    a = np.asarray(img, dtype="float32") * rng.uniform(0.85, 1.15)
    a = a + rng.normal(0, ruido, a.shape)
    return np.clip(a, 0, 255).astype("uint8")


def _ventanas(d, x0, y0, x1, y1, filas, cols, color, margen):
    """Cuadrícula de ventanas dentro del rectángulo (x0, y0, x1, y1)."""
    ancho, alto = (x1 - x0) / cols, (y1 - y0) / filas
    for f in range(filas):
        for c in range(cols):
            a, b = x0 + c * ancho + margen * ancho, y0 + f * alto + margen * alto
            d.rectangle([a, b, a + ancho * (1 - 2 * margen), b + alto * (1 - 2 * margen)], fill=color)


def dibujar_alojamiento(clase, rng, tam=48, ruido=8):
    """Dibujo esquemático (tam×tam×3, uint8) de un tipo de alojamiento. Datos SINTÉTICOS, no fotos reales."""
    E = 3                                   # supermuestreo para suavizar bordes
    S = tam * E
    img = Image.new("RGB", (S, S), _color(rng, (170, 205, 235), 25))          # cielo
    d = ImageDraw.Draw(img)
    if rng.random() < 0.5:                                                    # sol opcional
        cx, cy, r = rng.uniform(0.1, 0.9) * S, rng.uniform(0.08, 0.25) * S, rng.uniform(0.05, 0.08) * S
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 235, 120))
    hor = rng.uniform(0.62, 0.72) * S                                         # línea del horizonte
    verde = _color(rng, (120, 170, 90), 25)
    if clase == "piscina":
        d.rectangle([0, hor * 0.6, S, S], fill=_color(rng, (225, 210, 170), 15))   # terraza
        x0, x1 = rng.uniform(0.08, 0.2) * S, rng.uniform(0.75, 0.92) * S
        y0, y1 = rng.uniform(0.5, 0.58) * S, rng.uniform(0.82, 0.94) * S
        d.rectangle([x0 - 3, y0 - 3, x1 + 3, y1 + 3], fill=(245, 245, 245))
        d.rectangle([x0, y0, x1, y1], fill=_color(rng, (60, 150, 210), 20))
        for k in range(3):
            yy = y0 + (k + 1) * (y1 - y0) / 4
            d.line([x0 + 6, yy, x1 - 6, yy], fill=(150, 210, 240), width=2)
        for k in range(2):                                                    # tumbonas
            tx = rng.uniform(0.1, 0.8) * S
            d.rectangle([tx, hor * 0.72, tx + 0.1 * S, hor * 0.72 + 0.04 * S], fill=_color(rng, (240, 120, 60), 30))
    else:
        d.rectangle([0, hor, S, S], fill=verde)                                # césped
    if clase == "hotel":
        w, h = rng.uniform(0.30, 0.42) * S, rng.uniform(0.5, 0.66) * S
        x0 = rng.uniform(0.1 * S, 0.9 * S - w); y0 = hor - h + 0.05 * S
        d.rectangle([x0, y0, x0 + w, hor + 0.05 * S], fill=_color(rng, (220, 200, 170)))
        _ventanas(d, x0, y0 + 0.02 * S, x0 + w, hor, int(rng.integers(4, 6)), 3, (60, 90, 140), 0.22)
    elif clase == "apartamentos":
        w, h = rng.uniform(0.7, 0.86) * S, rng.uniform(0.28, 0.38) * S
        x0 = rng.uniform(0.02 * S, 0.98 * S - w); y0 = hor - h + 0.05 * S
        d.rectangle([x0, y0, x0 + w, hor + 0.05 * S], fill=_color(rng, (235, 225, 205)))
        _ventanas(d, x0, y0, x0 + w, hor + 0.05 * S, 2, int(rng.integers(5, 7)), (70, 100, 150), 0.25)
        for k in (1, 2):                                                       # balcones (líneas horizontales)
            yy = y0 + k * (hor + 0.05 * S - y0) / 2
            d.line([x0, yy, x0 + w, yy], fill=(120, 110, 100), width=2)
    elif clase == "casa_rural":
        w, h = rng.uniform(0.32, 0.44) * S, rng.uniform(0.2, 0.28) * S
        x0 = rng.uniform(0.1 * S, 0.9 * S - w); y0 = hor - h + 0.05 * S
        d.rectangle([x0, y0, x0 + w, hor + 0.05 * S], fill=_color(rng, (235, 225, 200)))
        d.polygon([(x0 - 0.04 * S, y0), (x0 + w + 0.04 * S, y0), (x0 + w / 2, y0 - rng.uniform(0.14, 0.2) * S)],
                  fill=_color(rng, (170, 70, 50), 25))
        d.rectangle([x0 + w * 0.42, y0 + h * 0.4, x0 + w * 0.58, hor + 0.05 * S], fill=(110, 70, 40))
        d.rectangle([x0 + w * 0.1, y0 + h * 0.2, x0 + w * 0.3, y0 + h * 0.5], fill=(70, 100, 150))
    elif clase == "camping":
        d.rectangle([0, hor - 0.08 * S, S, S], fill=verde)
        w, h = rng.uniform(0.34, 0.5) * S, rng.uniform(0.28, 0.4) * S
        x0 = rng.uniform(0.05 * S, 0.95 * S - w); base = hor + 0.1 * S
        c = _color(rng, [(240, 140, 40), (60, 120, 200), (230, 200, 60)][int(rng.integers(0, 3))], 20)
        d.polygon([(x0, base), (x0 + w, base), (x0 + w / 2, base - h)], fill=c)
        d.polygon([(x0 + w * 0.4, base), (x0 + w * 0.6, base), (x0 + w / 2, base - h * 0.5)], fill=(50, 40, 40))
    if clase != "piscina" and rng.random() < 0.6:                              # árbol de adorno
        tx = rng.choice([rng.uniform(0.03, 0.12), rng.uniform(0.88, 0.97)]) * S
        d.rectangle([tx - 2, hor - 0.02 * S, tx + 2, hor + 0.12 * S], fill=(100, 70, 40))
        d.ellipse([tx - 0.07 * S, hor - 0.16 * S, tx + 0.07 * S, hor + 0.01 * S], fill=(50, 120, 60))
    return _final(img.resize((tam, tam), Image.LANCZOS), rng, ruido)


def dibujar_forma(clase, rng, tam=48):
    """Formas y texturas abstractas (tarea auxiliar de preentrenamiento). Devuelve tam×tam×3 uint8."""
    fondo, tinta = _color(rng, (rng.integers(20, 235),) * 3, 20), _color(rng, tuple(int(v) for v in rng.integers(0, 256, 3)), 10)
    if np.abs(np.array(fondo, dtype=int) - np.array(tinta, dtype=int)).sum() < 150:      # asegura contraste
        tinta = tuple(255 - c for c in fondo)
    E = 2
    S = tam * E
    img = Image.new("RGB", (S, S), fondo)
    d = ImageDraw.Draw(img)
    paso = int(rng.integers(6, 12)) * E
    off = int(rng.integers(0, paso))
    if clase == "rayas_horizontales":
        for y in range(off, S, paso): d.rectangle([0, y, S, y + paso // 2], fill=tinta)
    elif clase == "rayas_verticales":
        for x in range(off, S, paso): d.rectangle([x, 0, x + paso // 2, S], fill=tinta)
    elif clase == "diagonales":
        for k in range(-S, S, paso): d.line([k + off, 0, k + off + S, S], fill=tinta, width=max(2, paso // 3))
    elif clase == "cuadricula":
        for y in range(off, S, paso): d.line([0, y, S, y], fill=tinta, width=2)
        for x in range(off, S, paso): d.line([x, 0, x, S], fill=tinta, width=2)
    elif clase == "puntos":
        r = max(2, paso // 4)
        for y in range(off, S, paso):
            for x in range(off, S, paso): d.ellipse([x - r, y - r, x + r, y + r], fill=tinta)
    else:
        r = rng.uniform(0.18, 0.38) * S
        cx, cy = rng.uniform(r, S - r), rng.uniform(r, S - r)
        if clase == "circulo": d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=tinta)
        elif clase == "rectangulo": d.rectangle([cx - r, cy - r * rng.uniform(0.5, 1), cx + r, cy + r * rng.uniform(0.5, 1)], fill=tinta)
        else: d.polygon([(cx - r, cy + r), (cx + r, cy + r), (cx, cy - r)], fill=tinta)
    return _final(img.resize((tam, tam), Image.LANCZOS), rng)


def generar_lote(funcion, clases, n_por_clase, semilla=42, tam=48):
    """Devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas."""
    rng = np.random.default_rng(semilla)
    X = np.stack([funcion(c, rng, tam) for c in clases for _ in range(n_por_clase)])
    y = np.repeat(np.arange(len(clases)), n_por_clase)
    orden = rng.permutation(len(y))
    return X[orden], y[orden]


PARECIDAS = {"hotel": "apartamentos", "apartamentos": "hotel", "casa_rural": "camping", "camping": "casa_rural", "piscina": "camping"}


def crear_dataset_carpetas(carpeta, n_por_clase=100, semilla=7, tam=48, ruido=8, prop_ambiguas=0.0):
    """Escribe PNG en carpeta/<clase>/img_000.png (estructura que espera image_dataset_from_directory).

    prop_ambiguas: fracción de imágenes cuyo dibujo corresponde a una clase parecida (PARECIDAS) pero se guarda
    en la carpeta de la otra: simula etiquetas dudosas o erróneas. Se anotan en carpeta/_ambiguas.csv (solo docente).
    """
    import os
    rng = np.random.default_rng(semilla)
    ambiguas = []
    for clase in CLASES_ALOJ:
        os.makedirs(os.path.join(carpeta, clase), exist_ok=True)
        for i in range(n_por_clase):
            dibujo = PARECIDAS[clase] if rng.random() < prop_ambiguas else clase
            if dibujo != clase:
                ambiguas.append(f"{clase}/img_{i:03d}.png,{dibujo}")
            Image.fromarray(dibujar_alojamiento(dibujo, rng, tam, ruido)).save(os.path.join(carpeta, clase, f"img_{i:03d}.png"))
    with open(os.path.join(carpeta, "_ambiguas.csv"), "w") as f:
        f.write("archivo,dibujo_real\n" + "\n".join(ambiguas) + "\n")
    return carpeta
```

**Qué hace cada línea:**

- `from PIL import Image, ImageDraw` → Trae `Image`, `ImageDraw` de `PIL` para poder usarlo.
- `CLASES_ALOJ = ["hotel", "apartamentos", "casa_rural", "camping", "piscina"]` → Guarda el valor en `CLASES_ALOJ`.
- `CLASES_FORMAS = ["rayas_horizontales", "rayas_verticales", "diagonales", "c…` → Guarda el valor en `CLASES_FORMAS`.
- `def _color(rng, base, var=30):` → Define la función `_color`: Color aleatorio cercano a `base` (tupla RGB).
- `def _final(img, rng, ruido=8):` → Define la función `_final`: Convierte a uint8 con un poco de ruido y variación de brillo.
- `def _ventanas(d, x0, y0, x1, y1, filas, cols, color, margen):` → Define la función `_ventanas`: Cuadrícula de ventanas dentro del rectángulo (x0, y0, x1, y1).
- `def dibujar_alojamiento(clase, rng, tam=48, ruido=8):` → Define la función `dibujar_alojamiento`: Dibujo esquemático (tam×tam×3, uint8) de un tipo de alojamiento. Datos SINTÉTICOS, no fotos reales.
- `def dibujar_forma(clase, rng, tam=48):` → Define la función `dibujar_forma`: Formas y texturas abstractas (tarea auxiliar de preentrenamiento). Devuelve tam×tam×3 uint8.
- `def generar_lote(funcion, clases, n_por_clase, semilla=42, tam=48):` → Define la función `generar_lote`: Devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- … y 2 más con las mismas ideas.

### Celda 3 · 0. Generador de imágenes sintéticas · 🏫

**Qué hace:** Practica `subplots`, `suptitle`, `tight_layout`, `imshow` y más (sección «0. Generador de imágenes sintéticas»).

```python
X_f, y_f = generar_lote(dibujar_forma, CLASES_FORMAS, 6, semilla=1)
X_a, y_a = generar_lote(dibujar_alojamiento, CLASES_ALOJ, 6, semilla=1)
fig, ejes = plt.subplots(2, 10, figsize=(14, 3.2))
for i in range(10):
    ejes[0, i].imshow(X_f[i]); ejes[0, i].set_title(CLASES_FORMAS[y_f[i]], fontsize=7); ejes[0, i].axis("off")
    ejes[1, i].imshow(X_a[i]); ejes[1, i].set_title(CLASES_ALOJ[y_a[i]], fontsize=7); ejes[1, i].axis("off")
plt.suptitle("Arriba: tarea auxiliar (formas y texturas) · Abajo: tarea real (tipos de alojamiento esquemáticos)")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `X_f, y_f = generar_lote(dibujar_forma, CLASES_FORMAS, 6, semilla=1)` → Guarda en `X_f, y_f` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `X_a, y_a = generar_lote(dibujar_alojamiento, CLASES_ALOJ, 6, semilla=1)` → Guarda en `X_a, y_a` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `fig, ejes = plt.subplots(2, 10, figsize=(14, 3.2))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `for i in range(10):` → Repite el bloque de debajo para cada valor de `i` en `range(10)`. Dentro del bloque: `imshow`: muestra una imagen o una matriz como imagen; `set_title`: pone el título de un gráfico; `axis`: controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas.
- `plt.suptitle("Arriba: tarea auxiliar (formas y texturas) · Abajo: tarea rea…` → `suptitle`: pone un título general a toda la figura.
- `plt.tight_layout(); plt.show()` → `tight_layout`: ajusta los márgenes para que nada se solape.
- `plt.tight_layout(); plt.show()` → `show`: muestra el gráfico.

### Celda 4 · 1. La tarea real, con pocos datos · 🏫

**Qué hace:** Practica `partial`, `shape` (sección «1. La tarea real, con pocos datos»).

```python
N_POR_CLASE = 6
alojamiento = functools.partial(dibujar_alojamiento, ruido=40)     # imágenes "sucias": mucho ruido, como fotos de mala calidad
X_ent, y_ent = generar_lote(alojamiento, CLASES_ALOJ, N_POR_CLASE, semilla=10)
X_val, y_val = generar_lote(alojamiento, CLASES_ALOJ, 40, semilla=11)
X_pru, y_pru = generar_lote(alojamiento, CLASES_ALOJ, 60, semilla=12)
print("entrenamiento", X_ent.shape, "· validación", X_val.shape, "· prueba", X_pru.shape)
```

**Qué hace cada línea:**

- `N_POR_CLASE = 6` → Guarda el valor en `N_POR_CLASE`.
- `alojamiento = functools.partial(dibujar_alojamiento, ruido=40) # imágenes "…` → Guarda en `alojamiento` el resultado. `partial`: fija algunos argumentos de una función.
- `X_ent, y_ent = generar_lote(alojamiento, CLASES_ALOJ, N_POR_CLASE, semilla=…` → Guarda en `X_ent, y_ent` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `X_val, y_val = generar_lote(alojamiento, CLASES_ALOJ, 40, semilla=11)` → Guarda en `X_val, y_val` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `X_pru, y_pru = generar_lote(alojamiento, CLASES_ALOJ, 60, semilla=12)` → Guarda en `X_pru, y_pru` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `print("entrenamiento", X_ent.shape, "· validación", X_val.shape, "· prueba"…` → `print`: muestra un valor por pantalla; `shape`: tamaño de la tabla: (filas, columnas).

### Celda 5 · 2. Punto de partida: una CNN desde cero · 🏫

**Qué hace:** Practica `set_random_seed`, `Input`, `enumerate`, `Model` y más (sección «2. Punto de partida: una CNN desde cero»).

```python
def construir_base(nombre="base"):
    entrada = keras.layers.Input(shape=(48, 48, 3))
    x = keras.layers.Rescaling(1 / 255)(entrada)                     # la propia red normaliza los píxeles
    for i, f in enumerate((16, 32, 64), start=1):
        x = keras.layers.Conv2D(f, 3, padding="same", activation="relu", name=f"bloque{i}_conv")(x)
        x = keras.layers.MaxPooling2D(name=f"bloque{i}_pool")(x)
    x = keras.layers.Flatten(name="aplanar")(x)                       # 6×6×64 = 2304 rasgos
    return keras.Model(entrada, x, name=nombre)

def con_cabeza(base, n_clases, dropout=0.2, tasa=1e-3):
    """Base + cabeza nueva (Dropout y Dense softmax), ya compilado."""
    entrada = keras.layers.Input(shape=(48, 48, 3))
    x = base(entrada)
    x = keras.layers.Dropout(dropout)(x)
    salida = keras.layers.Dense(n_clases, activation="softmax", name="cabeza")(x)
    modelo = keras.Model(entrada, salida)
    modelo.compile(keras.optimizers.Adam(tasa), "sparse_categorical_crossentropy", metrics=["accuracy"])
    return modelo

def entrenar(modelo, epocas=30, semilla=SEMILLA, X=None, y=None):
    keras.utils.set_random_seed(semilla)
    X = X_ent if X is None else X
    y = y_ent if y is None else y
    return modelo.fit(X, y, validation_data=(X_val, y_val), epochs=epocas, batch_size=16, verbose=0)

keras.utils.set_random_seed(SEMILLA)
desde_cero = con_cabeza(construir_base("base_desde_cero"), 5)
h_cero = entrenar(desde_cero, epocas=40)
acc_cero = desde_cero.evaluate(X_pru, y_pru, verbose=0)[1]
print(f"CNN desde cero con {len(X_ent)} imágenes → precisión en prueba: {acc_cero:.3f}")
```

**Qué hace cada línea:**

- `def construir_base(nombre="base"):` → Define la función `construir_base`: Función definida en el cuaderno.
- `def con_cabeza(base, n_clases, dropout=0.2, tasa=1e-3):` → Define la función `con_cabeza`: Base + cabeza nueva (Dropout y Dense softmax), ya compilado.
- `def entrenar(modelo, epocas=30, semilla=SEMILLA, X=None, y=None):` → Define la función `entrenar`: Función definida en el cuaderno.
- `keras.utils.set_random_seed(SEMILLA)` → `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados.
- `desde_cero = con_cabeza(construir_base("base_desde_cero"), 5)` → Guarda en `desde_cero` el resultado. `con_cabeza`: base + cabeza nueva (Dropout y Dense softmax), ya compilado; `construir_base`: función definida en el cuaderno.
- `h_cero = entrenar(desde_cero, epocas=40)` → Guarda en `h_cero` el resultado. `entrenar`: función definida en el cuaderno.
- `acc_cero = desde_cero.evaluate(X_pru, y_pru, verbose=0)[1]` → Guarda en `acc_cero` el resultado. `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.
- `print(f"CNN desde cero con {len(X_ent)} imágenes → precisión en prueba: {ac…` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.

### Celda 6 · 3. Preentrenar la base en una tarea auxiliar · 🏫

**Qué hace:** Practica `set_random_seed`, `fit`, `round`, `count_params` y más (sección «3. Preentrenar la base en una tarea aux…»).

```python
X_aux, y_aux = generar_lote(dibujar_forma, CLASES_FORMAS, 400, semilla=3)
X_aux_v, y_aux_v = generar_lote(dibujar_forma, CLASES_FORMAS, 50, semilla=4)

keras.utils.set_random_seed(SEMILLA)
base_pre = construir_base("base_preentrenada")
modelo_aux = con_cabeza(base_pre, len(CLASES_FORMAS), dropout=0.0)
modelo_aux.fit(X_aux, y_aux, epochs=12, batch_size=64, verbose=0)
print("Precisión en la tarea auxiliar (validación):", round(modelo_aux.evaluate(X_aux_v, y_aux_v, verbose=0)[1], 3))
print("La base tiene", base_pre.count_params(), "parámetros y ya sabe extraer rasgos visuales.")
```

**Qué hace cada línea:**

- `X_aux, y_aux = generar_lote(dibujar_forma, CLASES_FORMAS, 400, semilla=3)` → Guarda en `X_aux, y_aux` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `X_aux_v, y_aux_v = generar_lote(dibujar_forma, CLASES_FORMAS, 50, semilla=4)` → Guarda en `X_aux_v, y_aux_v` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `keras.utils.set_random_seed(SEMILLA)` → `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados.
- `base_pre = construir_base("base_preentrenada")` → Guarda en `base_pre` el resultado. `construir_base`: función definida en el cuaderno.
- `modelo_aux = con_cabeza(base_pre, len(CLASES_FORMAS), dropout=0.0)` → Guarda en `modelo_aux` el resultado. `con_cabeza`: base + cabeza nueva (Dropout y Dense softmax), ya compilado; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `modelo_aux.fit(X_aux, y_aux, epochs=12, batch_size=64, verbose=0)` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `print("Precisión en la tarea auxiliar (validación):", round(modelo_aux.eval…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.
- `print("La base tiene", base_pre.count_params(), "parámetros y ya sabe extra…` → `print`: muestra un valor por pantalla; `count_params`: cuenta cuántos pesos tiene el modelo.

### Celda 7 · 4. Congelar la base y entrenar solo una cabeza… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 4. Congelar la base y entrenar solo una cabeza… · 🏫

**Qué hace:** Practica `sum`, `evaluate`, `prod`, `count_params` y más (sección «4. Congelar la base y entrenar solo una…»).

```python
transfer = con_cabeza(copia_base, 5)
n_entrenables = sum(int(np.prod(p.shape)) for p in transfer.trainable_weights)
print(f"Parámetros totales: {transfer.count_params()} · entrenables (solo la cabeza): {n_entrenables}")
h_transfer = entrenar(transfer, epocas=30)
acc_transfer = transfer.evaluate(X_pru, y_pru, verbose=0)[1]
print(f"Transfer learning (base congelada) → precisión en prueba: {acc_transfer:.3f}")
```

**Qué hace cada línea:**

- `transfer = con_cabeza(copia_base, 5)` → Guarda en `transfer` el resultado. `con_cabeza`: base + cabeza nueva (Dropout y Dense softmax), ya compilado.
- `n_entrenables = sum(int(np.prod(p.shape)) for p in transfer.trainable_weigh…` → Guarda en `n_entrenables` el resultado. `sum`: suma todos los valores; `int`: convierte un valor en número entero; `prod`: multiplica todos los valores.
- `print(f"Parámetros totales: {transfer.count_params()} · entrenables (solo l…` → `print`: muestra un valor por pantalla; `count_params`: cuenta cuántos pesos tiene el modelo.
- `h_transfer = entrenar(transfer, epocas=30)` → Guarda en `h_transfer` el resultado. `entrenar`: función definida en el cuaderno.
- `acc_transfer = transfer.evaluate(X_pru, y_pru, verbose=0)[1]` → Guarda en `acc_transfer` el resultado. `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.
- `print(f"Transfer learning (base congelada) → precisión en prueba: {acc_tran…` → `print`: muestra un valor por pantalla.

### Celda 9 · 5. *Fine-tuning*: descongelar las últimas capas… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 5. *Fine-tuning*: descongelar las últimas capas… · 🏠

**Qué hace:** Fine-tuning: partimos del modelo transfer ya entrenado (cabeza lista), descongelamos el bloque 3 y bajamos la tasa.

```python
# Fine-tuning: partimos del modelo transfer ya entrenado (cabeza lista), descongelamos el bloque 3 y bajamos la tasa
n_ent_ft = descongelar_bloque(copia_base, 3)
transfer.compile(keras.optimizers.Adam(1e-4), "sparse_categorical_crossentropy", metrics=["accuracy"])   # ¡recompilar!
h_ft = entrenar(transfer, epocas=25, semilla=1)
acc_ft = transfer.evaluate(X_pru, y_pru, verbose=0)[1]
print(f"Tras fine-tuning del bloque 3 → precisión en prueba: {acc_ft:.3f}")
```

**Qué hace cada línea:**

- `n_ent_ft = descongelar_bloque(copia_base, 3)` → Guarda en `n_ent_ft` el resultado. `descongelar_bloque`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `transfer.compile(keras.optimizers.Adam(1e-4), "sparse_categorical_crossentr…` → `compile`: prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas); `Adam`: optimizador Adam: decide cómo ajustar los pesos en cada paso.
- `h_ft = entrenar(transfer, epocas=25, semilla=1)` → Guarda en `h_ft` el resultado. `entrenar`: función definida en el cuaderno.
- `acc_ft = transfer.evaluate(X_pru, y_pru, verbose=0)[1]` → Guarda en `acc_ft` el resultado. `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.
- `print(f"Tras fine-tuning del bloque 3 → precisión en prueba: {acc_ft:.3f}")` → `print`: muestra un valor por pantalla.

### Celda 11 · 5. *Fine-tuning*: descongelar las últimas capas… · 🏠

**Qué hace:** Practica `round`, `set_random_seed`, `compile`, `evaluate` y más (sección «Comparación con varias semillas»).

```python
def experimento(semilla, X=None, y=None, epocas=30):
    """Devuelve la precisión en prueba de (desde cero, base congelada, base con fine-tuning)."""
    keras.utils.set_random_seed(semilla)
    m0 = con_cabeza(construir_base("cero"), 5)
    entrenar(m0, epocas + 10, semilla, X, y)
    b = congelar(copiar_base(base_pre, "b"))
    m1 = con_cabeza(b, 5)
    entrenar(m1, epocas, semilla, X, y)
    a1 = m1.evaluate(X_pru, y_pru, verbose=0)[1]
    descongelar_bloque(b, 3)
    m1.compile(keras.optimizers.Adam(1e-4), "sparse_categorical_crossentropy", metrics=["accuracy"])
    entrenar(m1, epocas - 5, semilla, X, y)
    return m0.evaluate(X_pru, y_pru, verbose=0)[1], a1, m1.evaluate(X_pru, y_pru, verbose=0)[1]

filas = [experimento(s) for s in (1, 2, 3)]
comparacion = pd.DataFrame(filas, columns=["Desde cero", "Base congelada", "Fine-tuning bloque 3"]).agg(["mean", "std"]).round(3)
comparacion
```

**Qué hace cada línea:**

- `def experimento(semilla, X=None, y=None, epocas=30):` → Define la función `experimento`: Devuelve la precisión en prueba de (desde cero, base congelada, base con fine-tuning).
- `filas = [experimento(s) for s in (1, 2, 3)]` → Guarda en `filas` el resultado. `experimento`: devuelve la precisión en prueba de (desde cero, base congelada, base con fine-tuning).
- `comparacion = pd.DataFrame(filas, columns=["Desde cero", "Base congelada",…` → Guarda en `comparacion` el resultado. `round`: redondea un número a los decimales indicados; `agg`: calcula varias estadísticas a la vez (media, suma…) por grupo; `DataFrame`: crea una tabla de pandas (filas y columnas).

### Celda 12 · 5. *Fine-tuning*: descongelar las últimas capas… · 🏠

**Qué hace:** Practica `plot`, `ylabel`, `ylim`, `xticks` y más (sección «Comparación con varias semillas»).

```python
comparacion.loc["mean"].plot(kind="bar", yerr=comparacion.loc["std"], capsize=4, color=["gray", "steelblue", "seagreen"])
plt.ylabel("precisión en prueba"); plt.ylim(0, 1); plt.xticks(rotation=0)
plt.title(f"Con solo {N_POR_CLASE} imágenes por clase (media de 3 semillas)"); plt.show()
```

**Qué hace cada línea:**

- `comparacion.loc["mean"].plot(kind="bar", yerr=comparacion.loc["std"], capsi…` → `plot`: dibuja una línea (o puntos unidos); `loc`: selecciona filas/columnas por su etiqueta o por una condición.
- `plt.ylabel("precisión en prueba"); plt.ylim(0, 1); plt.xticks(rotation=0)` → `ylabel`: pone el nombre del eje vertical.
- `plt.ylabel("precisión en prueba"); plt.ylim(0, 1); plt.xticks(rotation=0)` → `ylim`: fija el rango del eje vertical.
- `plt.ylabel("precisión en prueba"); plt.ylim(0, 1); plt.xticks(rotation=0)` → `xticks`: fija las marcas del eje horizontal.
- `plt.title(f"Con solo {N_POR_CLASE} imágenes por clase (media de 3 semillas)…` → `title`: pone el título del gráfico.
- `plt.title(f"Con solo {N_POR_CLASE} imágenes por clase (media de 3 semillas)…` → `show`: muestra el gráfico.

### Celda 13 · 6. Con pesos reales: MobileNetV2 (rama Colab) y… · 🏠

**Qué hace:** Esta celda funciona SIN internet: construye MobileNetV2 con pesos aleatorios (weights=None) para ver su estructura.

```python
# Esta celda funciona SIN internet: construye MobileNetV2 con pesos aleatorios (weights=None) para ver su estructura.
def construir_mobilenet(pesos=None, tam=96):
    """pesos=None (aleatorios, offline) o pesos='imagenet' (requiere internet, se descarga ≈ 10 MB)."""
    base = keras.applications.MobileNetV2(input_shape=(tam, tam, 3), include_top=False, weights=pesos, alpha=0.35)
    base.trainable = False
    entrada = keras.layers.Input(shape=(48, 48, 3))
    x = keras.layers.Resizing(tam, tam)(entrada)                                     # de 48×48 a tam×tam
    x = keras.applications.mobilenet_v2.preprocess_input(x)                          # píxeles → [−1, 1]
    x = base(x, training=False)                                                      # ¡training=False al congelar!
    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.Dropout(0.2)(x)
    salida = keras.layers.Dense(5, activation="softmax")(x)
    modelo = keras.Model(entrada, salida)
    modelo.compile(keras.optimizers.Adam(1e-3), "sparse_categorical_crossentropy", metrics=["accuracy"])
    return modelo, base

mn, mn_base = construir_mobilenet(pesos=None)
print("MobileNetV2 (alpha 0.35): capas de la base =", len(mn_base.layers), "· parámetros totales =", mn.count_params(),
      "· entrenables =", sum(int(np.prod(p.shape)) for p in mn.trainable_weights))
print("Salida del modelo para 2 imágenes sintéticas:", mn.predict(X_ent[:2], verbose=0).round(2))
```

**Qué hace cada línea:**

- `def construir_mobilenet(pesos=None, tam=96):` → Define la función `construir_mobilenet`: pesos=None (aleatorios, offline) o pesos='imagenet' (requiere internet, se descarga ≈ 10 MB).
- `mn, mn_base = construir_mobilenet(pesos=None)` → Guarda en `mn, mn_base` el resultado. `construir_mobilenet`: pesos=None (aleatorios, offline) o pesos='imagenet' (requiere internet, se descarga ≈ 10 MB).
- `print("MobileNetV2 (alpha 0.35): capas de la base =", len(mn_base.layers),…` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `count_params`: cuenta cuántos pesos tiene el modelo.
- `print("Salida del modelo para 2 imágenes sintéticas:", mn.predict(X_ent[:2]…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `predict`: pide al modelo ya entrenado que haga predicciones.

### Celda 14 · 6. Con pesos reales: MobileNetV2 (rama Colab) y… · 🏠

**Qué hace:** Fine-tuning: se descongelan las últimas capas de la base y se baja la tasa (recompilar siempre).

```python
USAR_INTERNET = False        # ← True solo con conexión (Colab)

if USAR_INTERNET:
    mn_real, mn_real_base = construir_mobilenet(pesos="imagenet")           # ← aquí se descargan los pesos
    mn_real.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=15, batch_size=16, verbose=0)
    print("MobileNetV2 con ImageNet, precisión en prueba:", round(mn_real.evaluate(X_pru, y_pru, verbose=0)[1], 3))
    # Fine-tuning: se descongelan las últimas capas de la base y se baja la tasa (recompilar siempre)
    mn_real_base.trainable = True
    for capa in mn_real_base.layers[:-20]:
        capa.trainable = False
    mn_real.compile(keras.optimizers.Adam(1e-5), "sparse_categorical_crossentropy", metrics=["accuracy"])
    mn_real.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=10, batch_size=16, verbose=0)
    print("Tras fine-tuning:", round(mn_real.evaluate(X_pru, y_pru, verbose=0)[1], 3))
else:
    print("Rama de Colab desactivada (USAR_INTERNET = False).")
```

**Qué hace cada línea:**

- `USAR_INTERNET = False # ← True solo con conexión (Colab)` → Guarda el valor en `USAR_INTERNET`.
- `if USAR_INTERNET:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `construir_mobilenet`: pesos=None (aleatorios, offline) o pesos='imagenet' (requiere internet, se descarga ≈ 10 MB); `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.

### Celda 15 · 7. Mini-reto integrador: ¿cuántas imágenes nece… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S11_02_transfer_learning.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
