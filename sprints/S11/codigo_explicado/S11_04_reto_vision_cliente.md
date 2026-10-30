# Código explicado · S11.04 · S11 · Reto PBL — Visión artificial para el cliente

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/notebooks/S11_04_reto_vision_cliente.ipynb) · [descargar](../notebooks/S11_04_reto_vision_cliente.ipynb) · ⏱ en clase: 60 min · 🏫 11 celdas de código en clase · 🏠 3 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `set_random_seed`. |
| 2 | 0. Generador de imágenes sintéticas | Practica `tuple`, `astype`, `new`, `Draw` y más (sección «0. Generador de imágenes sintét… |
| 3 | 1. El dataset: una carpeta por clase | Practica `join`, `isdir` (sección «1. El dataset: una carpeta por clase»). |
| 5 | 1. El dataset: una carpeta por clase | Practica `image_dataset_from_directory`, `subplots`, `zip`, `suptitle` y más (sección «Ca… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `CLASES_ALOJ` | `["hotel", "apartamentos", "casa_rural", "camping", "pisci…` | 2 |
| `CLASES_FORMAS` | `["rayas_horizontales", "rayas_verticales", "diagonales",…` | 2 |
| `PARECIDAS` | `{"hotel": "apartamentos", "apartamentos": "hotel", "casa_…` | 2 |
| `USAR_DATASET_PROPIO` | `False` | 3 |
| `RUTA_PROPIA` | `"mis_fotos"` | 3 |
| `RUTA` | `RUTA_PROPIA if USAR_DATASET_PROPIO else os.path.join("dat…` | 3 |
| `TAM` | `48` | 5 |
| `NOMBRES` | `ds_ent.class_names` | 5 |
| `N_CLASES` | `len(NOMBRES)` | 5 |
| `rutas_resto` | `ds_resto.file_paths` | 5 |
| `mitad` | `len(X_resto) // 2` | 5 |
| `rutas_pru` | `rutas_resto[mitad:]` | 5 |
| `base_pre` | `construir_base("base_preentrenada")` | 6 |
| `h` | `modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val),…` | 8 |
| `desde_cero` | `con_cabeza(construir_base("desde_cero"), N_CLASES)` | 8 |
| `prob_pru` | `modelo.predict(X_pru, verbose=0)` | 9 |
| `pred_pru` | `prob_pru.argmax(axis=1)` | 9 |
| `pred_cero` | `desde_cero.predict(X_pru, verbose=0).argmax(axis=1)` | 9 |
| `cm` | `confusion_matrix(y_pru, pred_pru, labels=range(N_CLASES))` | 9 |
| `errores` | `indices_errores(y_pru, prob_pru)` | 12 |
| `n_mostrar` | `min(10, len(errores))` | 12 |
| `pares` | `pd.Series([f"{NOMBRES[y_pru[i]]} → {NOMBRES[pred_pru[i]]}…` | 13 |
| `umbrales` | `[0.0, 0.5, 0.7, 0.9, 0.95]` | 16 |
| `tabla` | `pd.DataFrame([cobertura_y_precision(prob_pru, y_pru, u) f…` | 16 |
| `demo_ruta` | `rutas_pru[0]` | 17 |
| `carpeta_tmp` | `tempfile.mkdtemp()` | 17 |
| `recargado` | `keras.models.load_model(os.path.join(carpeta_tmp, "clasif…` | 17 |
| … | otras 2 variables | |

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
| `contar_por_clase` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `a_numpy` | Función definida en el cuaderno. |
| `construir_base` | Función definida en el cuaderno. |
| `con_cabeza` | Función definida en el cuaderno. |
| `modelo_transfer` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `indices_errores` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `cobertura_y_precision` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `clasificar_foto` | Devuelve (clase, confianza, probabilidades por clase) o 'revisar a mano' si la confianza es baja. |
| `construir_mobilenet` | MobileNetV2 (alpha 0.35) congelada + cabeza nueva. pesos='imagenet' descarga los pesos (requiere internet). |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `abs` | Valor absoluto: quita el signo negativo. | 2 |
| `accuracy_score` | Calcula el porcentaje de aciertos. | 9 |
| `Adam` | Optimizador Adam: decide cómo ajustar los pesos en cada paso. | 6, 8, 18 |
| `append` | Añade un elemento al final de una lista. | 2 |
| `arange` | Crea una secuencia de números con un paso fijo. | 2 |
| `argmax` | Devuelve la posición del valor más grande. | 9, 17 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 2 |
| `asarray` | Convierte algo en array de NumPy sin copiarlo si ya lo es. | 2 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 2, 5, 12 |
| `axis` | Controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas. | 5, 12 |
| `base` | La red preentrenada que se reutiliza (el «cuerpo» del modelo). | 6, 18 |
| `basename` | Devuelve solo el nombre del fichero, sin la carpeta. | 12 |
| `choice` | Elige un elemento al azar. | 2 |
| `classification_report` | Resumen de precisión, sensibilidad y F1 por clase. | 9 |
| `clip` | Limita los valores a un mínimo y un máximo. | 2 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 6, 8, 18 |
| `concatenate` | Une arrays uno detrás de otro. | 5 |
| `confusion_matrix` | Cuenta aciertos y fallos de cada tipo (matriz de confusión). | 9 |
| `Conv2D` | Capa convolucional: detecta patrones (bordes, formas) en imágenes. | 6 |
| `count_params` | Cuenta cuántos pesos tiene el modelo. | 6, 18 |
| `DataFrame` | Crea una tabla de pandas (filas y columnas). | 16 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 2 |
| `Dense` | Capa de neuronas totalmente conectadas. | 6, 18 |
| `dict` | Crea un diccionario (parejas nombre: valor). | 17 |
| `Draw` | Dibuja sobre una imagen (clase de Pillow). | 2 |
| `Dropout` | Capa que apaga neuronas al azar al entrenar para evitar el sobreajuste. | 6, 18 |
| `ellipse` | Dibuja una elipse. | 2 |
| `enumerate` | Recorre una lista dando a la vez la posición y el valor. | 6 |
| `evaluate` | Calcula la pérdida y las métricas del modelo con unos datos. | 8, 18 |
| `expand_dims` | Añade una dimensión de tamaño 1. | 17 |
| `f1_score` | Calcula el F1: equilibrio entre precisión y sensibilidad. | 9 |
| `figure` | Crea la figura (el lienzo) donde se dibuja. | 9 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 6, 8, 18 |
| `Flatten` | Capa que aplana la imagen en un vector. | 6 |
| `float` | Convierte un valor en número decimal. | 17 |
| `fromarray` | Convierte un array de NumPy en imagen. | 2 |
| `funcion` | La función que se pasa como argumento y se llama dentro. | 2 |
| `GlobalAveragePooling2D` | Capa que resume cada mapa de características en un solo número (su media). | 18 |
| `head` | Muestra las primeras filas. | 13 |
| `image_dataset_from_directory` | Carga imágenes de carpetas (una por clase) como conjunto de datos. | 5 |
| `img_to_array` | Convierte una imagen en un array de números. | 17 |
| `imshow` | Muestra una imagen o una matriz como imagen. | 5, 9, 12 |
| `Input` | Define la forma de los datos de entrada del modelo. | 6, 18 |
| `int` | Convierte un valor en número entero. | 2, 17 |
| `integers` | Genera números enteros aleatorios. | 2 |
| `isdir` | Comprueba si una ruta es una carpeta. | 3, 19 |
| `join` | Une una lista de textos en uno solo con un separador. | 2, 3, 14, 17 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 2, 5, 6, 12, 13, 14 |
| `line` | Dibuja una línea. | 2 |
| `list` | Crea una lista (o convierte algo en lista). | 5 |
| `load_img` | Carga una imagen desde un fichero. | 17 |
| `load_model` | Carga un modelo guardado. | 17 |
| `makedirs` | Crea una carpeta (y las que falten). | 2 |
| `max` | Devuelve el valor más grande. | 2, 9, 12, 17 |
| `MaxPooling2D` | Capa que reduce la imagen quedándose con el valor máximo de cada zona. | 6 |
| `min` | Devuelve el valor más pequeño. | 12 |
| `mkdtemp` | Crea una carpeta temporal que se borra sola al acabar. | 17 |
| `MobileNetV2` | Red ya entrenada con millones de imágenes, lista para reutilizar. | 18 |
| `Model` | Crea un modelo de Keras indicando entradas y salidas. | 6, 18 |
| `new` | Crea una imagen nueva en blanco (Pillow) del tamaño y color indicados. | 2 |
| `normal` | Genera números aleatorios con forma de campana (normal). | 2 |
| `numpy` | Convierte un tensor de TensorFlow en un array de NumPy. | 5 |
| `open` | Abre un fichero para leerlo o escribirlo. | 2 |
| `permutation` | Devuelve un orden aleatorio de los índices. | 2 |
| `polygon` | Dibuja un polígono. | 2 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 9, 17 |
| `preprocess_input` | Prepara las imágenes como espera la red preentrenada. | 18 |
| `print` | Muestra un valor por pantalla. | 3, 5, 6, 8, 9, 12… |
| `random` | Número aleatorio entre 0 y 1. | 2 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 2, 5, 9 |
| `ravel` | Aplana un array a una sola dimensión. | 12 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 14 |
| `rectangle` | Dibuja un rectángulo. | 2 |
| `relpath` | Devuelve la ruta relativa de un fichero. | 14 |
| `repeat` | Repite cada elemento varias veces. | 2 |
| `replace` | Sustituye un trozo de texto (o valores de una tabla) por otro. | 14 |
| `Rescaling` | Capa de Keras que reescala los píxeles (por ejemplo, de 0–255 a 0–1). | 6 |
| `resize` | Cambia el tamaño de una imagen. | 2 |
| `Resizing` | Capa de Keras que cambia el tamaño de las imágenes. | 18 |
| `rmtree` | Borra una carpeta con todo lo que contiene. | 17, 19 |
| `round` | Redondea un número a los decimales indicados. | 8, 16, 17, 18 |
| `save` | Guarda el modelo (o el objeto) en un fichero. | 2, 17 |
| `Series` | Crea una columna de pandas (una sola serie de valores). | 13 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 14 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 1, 6, 8 |
| `set_title` | Pone el título de un gráfico. | 5, 12 |
| `shape` | Tamaño de la tabla: (filas, columnas). | 2, 5 |
| `show` | Muestra el gráfico. | 5, 9, 12 |
| `stack` | Apila arrays en una dimensión nueva. | 2 |
| `startswith` | Comprueba si un texto empieza por algo. | 8 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 5, 12 |
| `sum` | Suma todos los valores. | 2, 14 |
| `suptitle` | Pone un título general a toda la figura. | 5, 12 |
| `text` | Escribe un texto en una posición del gráfico. | 9, 12 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 5, 9, 12 |
| `title` | Pone el título del gráfico. | 9 |
| `tuple` | Crea una tupla (como una lista que no se puede modificar). | 2 |
| `uniform` | Número aleatorio decimal entre dos límites. | 2 |
| `value_counts` | Cuenta cuántas veces aparece cada valor. | 13 |
| `write` | Escribe en un fichero. | 2 |
| `xlabel` | Pone el nombre del eje horizontal. | 9 |
| `xticks` | Fija las marcas del eje horizontal. | 9 |
| `ylabel` | Pone el nombre del eje vertical. | 9 |
| `yticks` | Fija las marcas del eje vertical. | 9 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 5, 12, 17 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `set_random_seed`.

```python
import os, functools, tempfile, shutil
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score

SEMILLA = 42
keras.utils.set_random_seed(SEMILLA)
```

**Qué hace cada línea:**

- `import os, functools, tempfile, shutil` → Trae `os`, `functools`, `tempfile`, `shutil` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import tensorflow as tf` → Trae `tensorflow` (lo llamamos `tf`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `from sklearn.metrics import confusion_matrix, classification_report, accura…` → Trae `confusion_matrix`, `classification_report`, `accuracy_score`, `f1_score` de `sklearn.metrics` para poder usarlo.
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

### Celda 3 · 1. El dataset: una carpeta por clase · 🏫

**Qué hace:** Practica `join`, `isdir` (sección «1. El dataset: una carpeta por clase»).

```python
USAR_DATASET_PROPIO = False
RUTA_PROPIA = "mis_fotos"                       # carpeta con una subcarpeta por clase
RUTA = RUTA_PROPIA if USAR_DATASET_PROPIO else os.path.join("datos_sinteticos", "alojamientos")

if not USAR_DATASET_PROPIO and not os.path.isdir(RUTA):
    crear_dataset_carpetas(RUTA, n_por_clase=60, semilla=7, tam=48, ruido=40, prop_ambiguas=0.12)
    print("Dataset sintético generado en", RUTA)
```

**Qué hace cada línea:**

- `USAR_DATASET_PROPIO = False` → Guarda el valor en `USAR_DATASET_PROPIO`.
- `RUTA_PROPIA = "mis_fotos" # carpeta con una subcarpeta por clase` → Guarda el valor en `RUTA_PROPIA`.
- `RUTA = RUTA_PROPIA if USAR_DATASET_PROPIO else os.path.join("datos_sintetic…` → Guarda en `RUTA` el resultado. `join`: une una lista de textos en uno solo con un separador.
- `if not USAR_DATASET_PROPIO and not os.path.isdir(RUTA):` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `crear_dataset_carpetas`: escribe PNG en carpeta/<clase>/img_000.png (estructura que espera image_dataset_from_directory).

### Celda 4 · 1. El dataset: una carpeta por clase · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 1. El dataset: una carpeta por clase · 🏫

**Qué hace:** Practica `image_dataset_from_directory`, `subplots`, `zip`, `suptitle` y más (sección «Cargar con `image_dataset_from_director…»).

```python
TAM = 48
ds_ent, ds_resto = keras.utils.image_dataset_from_directory(
    RUTA, validation_split=0.4, subset="both", seed=SEMILLA, image_size=(TAM, TAM), batch_size=32, label_mode="int")
NOMBRES = ds_ent.class_names
N_CLASES = len(NOMBRES)
rutas_resto = ds_resto.file_paths

def a_numpy(ds):
    lotes = list(ds)                  # UNA sola pasada: el entrenamiento se baraja en cada pasada y separar X e y las desalinearía
    X = np.concatenate([x.numpy() for x, _ in lotes]).astype("float32")
    y = np.concatenate([y.numpy() for _, y in lotes]).astype(int)
    return X, y

X_ent, y_ent = a_numpy(ds_ent)
X_resto, y_resto = a_numpy(ds_resto)
mitad = len(X_resto) // 2
X_val, y_val = X_resto[:mitad], y_resto[:mitad]
X_pru, y_pru = X_resto[mitad:], y_resto[mitad:]
rutas_pru = rutas_resto[mitad:]
print("Clases:", NOMBRES)
print(f"entrenamiento {X_ent.shape} · validación {X_val.shape} · prueba {X_pru.shape}")

fig, ejes = plt.subplots(1, 8, figsize=(14, 2.2))
for eje, i in zip(ejes, range(8)):
    eje.imshow(X_ent[i].astype("uint8")); eje.set_title(NOMBRES[y_ent[i]], fontsize=8); eje.axis("off")
plt.suptitle("Ejemplos del entrenamiento"); plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `TAM = 48` → Guarda el valor en `TAM`.
- `ds_ent, ds_resto = keras.utils.image_dataset_from_directory(` → Guarda en `ds_ent, ds_resto` el resultado. `image_dataset_from_directory`: carga imágenes de carpetas (una por clase) como conjunto de datos.
- `NOMBRES = ds_ent.class_names` → Guarda el valor en `NOMBRES`.
- `N_CLASES = len(NOMBRES)` → Guarda en `N_CLASES` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `rutas_resto = ds_resto.file_paths` → Guarda el valor en `rutas_resto`.
- `def a_numpy(ds):` → Define la función `a_numpy`: Función definida en el cuaderno.
- `X_ent, y_ent = a_numpy(ds_ent)` → Guarda en `X_ent, y_ent` el resultado. `a_numpy`: función definida en el cuaderno.
- `X_resto, y_resto = a_numpy(ds_resto)` → Guarda en `X_resto, y_resto` el resultado. `a_numpy`: función definida en el cuaderno.
- `mitad = len(X_resto) // 2` → Guarda en `mitad` el resultado. `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- … y 10 más con las mismas ideas.

### Celda 6 · 2. El modelo: *transfer learning* (rama offline) · 🏫

**Qué hace:** Tarea auxiliar: formas y texturas (ejecuta unos 15 s).

```python
def construir_base(nombre="base"):
    entrada = keras.layers.Input(shape=(TAM, TAM, 3))
    x = keras.layers.Rescaling(1 / 255)(entrada)
    for i, f in enumerate((16, 32, 64), start=1):
        x = keras.layers.Conv2D(f, 3, padding="same", activation="relu", name=f"bloque{i}_conv")(x)
        x = keras.layers.MaxPooling2D(name=f"bloque{i}_pool")(x)
    x = keras.layers.Flatten(name="aplanar")(x)
    return keras.Model(entrada, x, name=nombre)

def con_cabeza(base, n_clases, dropout=0.3, tasa=1e-3):
    entrada = keras.layers.Input(shape=(TAM, TAM, 3))
    x = keras.layers.Dropout(dropout)(base(entrada))
    salida = keras.layers.Dense(n_clases, activation="softmax", name="cabeza")(x)
    m = keras.Model(entrada, salida)
    m.compile(keras.optimizers.Adam(tasa), "sparse_categorical_crossentropy", metrics=["accuracy"])
    return m

# Tarea auxiliar: formas y texturas (ejecuta unos 15 s)
X_aux, y_aux = generar_lote(dibujar_forma, CLASES_FORMAS, 400, semilla=3, tam=TAM)
keras.utils.set_random_seed(SEMILLA)
base_pre = construir_base("base_preentrenada")
con_cabeza(base_pre, len(CLASES_FORMAS), dropout=0.0).fit(X_aux, y_aux, epochs=12, batch_size=64, verbose=0)
print("Base preentrenada lista:", base_pre.count_params(), "parámetros")
```

**Qué hace cada línea:**

- `def construir_base(nombre="base"):` → Define la función `construir_base`: Función definida en el cuaderno.
- `def con_cabeza(base, n_clases, dropout=0.3, tasa=1e-3):` → Define la función `con_cabeza`: Función definida en el cuaderno.
- `X_aux, y_aux = generar_lote(dibujar_forma, CLASES_FORMAS, 400, semilla=3, t…` → Guarda en `X_aux, y_aux` el resultado. `generar_lote`: devuelve (X uint8 [n, tam, tam, 3], y int [n]) con n_por_clase imágenes por clase, mezcladas.
- `keras.utils.set_random_seed(SEMILLA)` → `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados.
- `base_pre = construir_base("base_preentrenada")` → Guarda en `base_pre` el resultado. `construir_base`: función definida en el cuaderno.
- `con_cabeza(base_pre, len(CLASES_FORMAS), dropout=0.0).fit(X_aux, y_aux, epo…` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `con_cabeza`: función definida en el cuaderno; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `print("Base preentrenada lista:", base_pre.count_params(), "parámetros")` → `print`: muestra un valor por pantalla; `count_params`: cuenta cuántos pesos tiene el modelo.

### Celda 7 · 2. El modelo: *transfer learning* (rama offline) · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 2. El modelo: *transfer learning* (rama offline) · 🏫

**Qué hace:** Fine-tuning del último bloque con tasa pequeña (y recompilando).

```python
keras.utils.set_random_seed(SEMILLA)
modelo, base_congelada = modelo_transfer(base_pre, N_CLASES)
modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=30, batch_size=16, verbose=0)
print("Precisión de validación con base congelada:", round(modelo.evaluate(X_val, y_val, verbose=0)[1], 3))

# Fine-tuning del último bloque con tasa pequeña (y recompilando)
for capa in base_congelada.layers:
    capa.trainable = capa.name.startswith("bloque3")
modelo.compile(keras.optimizers.Adam(1e-4), "sparse_categorical_crossentropy", metrics=["accuracy"])
h = modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=25, batch_size=16, verbose=0)
print("Precisión de validación tras fine-tuning:", round(modelo.evaluate(X_val, y_val, verbose=0)[1], 3))

# Referencia: la misma arquitectura entrenada desde cero
keras.utils.set_random_seed(SEMILLA)
desde_cero = con_cabeza(construir_base("desde_cero"), N_CLASES)
desde_cero.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=40, batch_size=16, verbose=0)
```

**Qué hace cada línea:**

- `keras.utils.set_random_seed(SEMILLA)` → `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados.
- `modelo, base_congelada = modelo_transfer(base_pre, N_CLASES)` → Guarda en `modelo, base_congelada` el resultado. `modelo_transfer`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=30, batch_s…` → `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `print("Precisión de validación con base congelada:", round(modelo.evaluate(…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.
- `for capa in base_congelada.layers:` → Repite el bloque de debajo para cada valor de `capa` en `base_congelada.layers`. Dentro del bloque: `startswith`: comprueba si un texto empieza por algo.
- `modelo.compile(keras.optimizers.Adam(1e-4), "sparse_categorical_crossentrop…` → `compile`: prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas); `Adam`: optimizador Adam: decide cómo ajustar los pesos en cada paso.
- `h = modelo.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=25, bat…` → Guarda en `h` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»).
- `print("Precisión de validación tras fine-tuning:", round(modelo.evaluate(X_…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.
- `keras.utils.set_random_seed(SEMILLA)` → `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados.
- … y 2 más con las mismas ideas.

### Celda 9 · 3. Rendimiento en el conjunto de prueba · 🏫

**Qué hace:** Practica `predict`, `argmax`, `confusion_matrix`, `figure` y más (sección «3. Rendimiento en el conjunto de prueba»).

```python
prob_pru = modelo.predict(X_pru, verbose=0)
pred_pru = prob_pru.argmax(axis=1)
pred_cero = desde_cero.predict(X_pru, verbose=0).argmax(axis=1)
print(f"Precisión en prueba → transfer + fine-tuning: {accuracy_score(y_pru, pred_pru):.3f} · desde cero: {accuracy_score(y_pru, pred_cero):.3f}")
print(f"F1 macro → transfer: {f1_score(y_pru, pred_pru, average='macro'):.3f} · desde cero: {f1_score(y_pru, pred_cero, average='macro'):.3f}")
print(classification_report(y_pru, pred_pru, target_names=NOMBRES, zero_division=0))

cm = confusion_matrix(y_pru, pred_pru, labels=range(N_CLASES))
plt.figure(figsize=(5.6, 4.8)); plt.imshow(cm, cmap="Blues")
for i in range(N_CLASES):
    for j in range(N_CLASES):
        plt.text(j, i, cm[i, j], ha="center", va="center", color="white" if cm[i, j] > cm.max() / 2 else "black")
plt.xticks(range(N_CLASES), NOMBRES, rotation=30); plt.yticks(range(N_CLASES), NOMBRES)
plt.xlabel("predicho"); plt.ylabel("real"); plt.title("Matriz de confusión (prueba)"); plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `prob_pru = modelo.predict(X_pru, verbose=0)` → Guarda en `prob_pru` el resultado. `predict`: pide al modelo ya entrenado que haga predicciones.
- `pred_pru = prob_pru.argmax(axis=1)` → Guarda en `pred_pru` el resultado. `argmax`: devuelve la posición del valor más grande.
- `pred_cero = desde_cero.predict(X_pru, verbose=0).argmax(axis=1)` → Guarda en `pred_cero` el resultado. `argmax`: devuelve la posición del valor más grande; `predict`: pide al modelo ya entrenado que haga predicciones.
- `print(f"Precisión en prueba → transfer + fine-tuning: {accuracy_score(y_pru…` → `print`: muestra un valor por pantalla; `accuracy_score`: calcula el porcentaje de aciertos.
- `print(f"F1 macro → transfer: {f1_score(y_pru, pred_pru, average='macro'):.3…` → `print`: muestra un valor por pantalla; `f1_score`: calcula el F1: equilibrio entre precisión y sensibilidad.
- `print(classification_report(y_pru, pred_pru, target_names=NOMBRES, zero_div…` → `print`: muestra un valor por pantalla; `classification_report`: resumen de precisión, sensibilidad y F1 por clase.
- `cm = confusion_matrix(y_pru, pred_pru, labels=range(N_CLASES))` → Guarda en `cm` el resultado. `confusion_matrix`: cuenta aciertos y fallos de cada tipo (matriz de confusión); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `plt.figure(figsize=(5.6, 4.8)); plt.imshow(cm, cmap="Blues")` → `figure`: crea la figura (el lienzo) donde se dibuja.
- `plt.figure(figsize=(5.6, 4.8)); plt.imshow(cm, cmap="Blues")` → `imshow`: muestra una imagen o una matriz como imagen.
- … y 8 más con las mismas ideas.

### Celda 10 · 3. Rendimiento en el conjunto de prueba · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 4. Análisis de errores: mirar los ejemplos mal… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 12 · 4. Análisis de errores: mirar los ejemplos mal… · 🏫

**Qué hace:** Practica `min`, `subplots`, `ravel`, `zip` y más (sección «4. Análisis de errores: mirar los ejemp…»).

```python
errores = indices_errores(y_pru, prob_pru)
print(f"{len(errores)} imágenes mal clasificadas de {len(y_pru)}")
n_mostrar = min(10, len(errores))
if n_mostrar:
    fig, ejes = plt.subplots(2, 5, figsize=(13, 6.2))
    for eje in ejes.ravel():
        eje.axis("off")
    for eje, i in zip(ejes.ravel(), errores[:n_mostrar]):
        eje.imshow(X_pru[i].astype("uint8"))
        eje.set_title(f"real: {NOMBRES[y_pru[i]]}\npredicho: {NOMBRES[pred_pru[i]]} ({prob_pru[i].max():.0%})", fontsize=8, color="darkred")
        eje.text(0, -4, os.path.basename(rutas_pru[i]), fontsize=6)
    plt.suptitle("Errores del modelo con más confianza (los primeros son los más preocupantes)"); plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `errores = indices_errores(y_pru, prob_pru)` → Guarda en `errores` el resultado. `indices_errores`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `print(f"{len(errores)} imágenes mal clasificadas de {len(y_pru)}")` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `n_mostrar = min(10, len(errores))` → Guarda en `n_mostrar` el resultado. `min`: devuelve el valor más pequeño; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- `if n_mostrar:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `subplots`: crea una figura con uno o varios ejes (gráficos) dentro; `ravel`: aplana un array a una sola dimensión; `axis`: controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas.

### Celda 13 · 4. Análisis de errores: mirar los ejemplos mal… · 🏫

**Qué hace:** Qué pares de clases se confunden más.

```python
# Qué pares de clases se confunden más
pares = pd.Series([f"{NOMBRES[y_pru[i]]} → {NOMBRES[pred_pru[i]]}" for i in errores]).value_counts()
print(pares.head(5) if len(pares) else "No hay errores en la prueba.")
```

**Qué hace cada línea:**

- `pares = pd.Series([f"{NOMBRES[y_pru[i]]} → {NOMBRES[pred_pru[i]]}" for i in…` → Guarda en `pares` el resultado. `value_counts`: cuenta cuántas veces aparece cada valor; `Series`: crea una columna de pandas (una sola serie de valores).
- `print(pares.head(5) if len(pares) else "No hay errores en la prueba.")` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla; `head`: muestra las primeras filas.

### Celda 14 · 4. Análisis de errores: mirar los ejemplos mal… · 🏫

**Qué hace:** SOLO DOCENTE: ¿cuántos errores del modelo son imágenes "ambiguas" (etiqueta dudosa)?.

```python
# SOLO DOCENTE: ¿cuántos errores del modelo son imágenes "ambiguas" (etiqueta dudosa)?
if not USAR_DATASET_PROPIO:
    amb = pd.read_csv(os.path.join(RUTA, "_ambiguas.csv"))
    marcadas = set(amb["archivo"])
    rel = [os.path.relpath(rutas_pru[i], RUTA).replace(os.sep, "/") for i in errores]
    print(f"Errores del modelo que son etiquetas ambiguas: {sum(r in marcadas for r in rel)} de {len(rel)}")
```

**Qué hace cada línea:**

- `if not USAR_DATASET_PROPIO:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `read_csv`: lee un fichero CSV y lo convierte en una tabla; `join`: une una lista de textos en uno solo con un separador; `set`: crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez.

### Celda 15 · 5. IA responsable: cuándo el modelo debe pedir… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 16 · 5. IA responsable: cuándo el modelo debe pedir… · 🏫

**Qué hace:** Practica `round`, `DataFrame` (sección «5. IA responsable: cuándo el modelo deb…»).

```python
umbrales = [0.0, 0.5, 0.7, 0.9, 0.95]
tabla = pd.DataFrame([cobertura_y_precision(prob_pru, y_pru, u) for u in umbrales], index=umbrales,
                     columns=["cobertura", "precisión en las aceptadas"]).round(3)
tabla.index.name = "umbral de confianza"
tabla
```

**Qué hace cada línea:**

- `umbrales = [0.0, 0.5, 0.7, 0.9, 0.95]` → Guarda el valor en `umbrales`.
- `tabla = pd.DataFrame([cobertura_y_precision(prob_pru, y_pru, u) for u in um…` → Guarda en `tabla` el resultado. `round`: redondea un número a los decimales indicados; `DataFrame`: crea una tabla de pandas (filas y columnas); `cobertura_y_precision`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `tabla.index.name = "umbral de confianza"` → Guarda el valor en `tabla.index.name`.

### Celda 17 · 6. Demostrador · 🏠

**Qué hace:** Guardar y recargar el modelo (para el demostrador).

```python
def clasificar_foto(ruta_imagen, modelo_=None, umbral=0.7):
    """Devuelve (clase, confianza, probabilidades por clase) o 'revisar a mano' si la confianza es baja."""
    modelo_ = modelo_ or modelo
    img = keras.utils.load_img(ruta_imagen, target_size=(TAM, TAM))
    p = modelo_.predict(np.expand_dims(keras.utils.img_to_array(img), 0), verbose=0)[0]
    clase = NOMBRES[int(p.argmax())] if p.max() >= umbral else "revisar a mano"
    return clase, float(p.max()), dict(zip(NOMBRES, p.round(3)))

demo_ruta = rutas_pru[0]
print("Foto:", demo_ruta, "· real:", NOMBRES[y_pru[0]])
print(clasificar_foto(demo_ruta))

# Guardar y recargar el modelo (para el demostrador)
carpeta_tmp = tempfile.mkdtemp()
modelo.save(os.path.join(carpeta_tmp, "clasificador_alojamientos.keras"))
recargado = keras.models.load_model(os.path.join(carpeta_tmp, "clasificador_alojamientos.keras"))
assert clasificar_foto(demo_ruta, recargado)[0] == clasificar_foto(demo_ruta)[0], "El modelo recargado debe dar la misma respuesta"
shutil.rmtree(carpeta_tmp, ignore_errors=True)
```

**Qué hace cada línea:**

- `def clasificar_foto(ruta_imagen, modelo_=None, umbral=0.7):` → Define la función `clasificar_foto`: Devuelve (clase, confianza, probabilidades por clase) o 'revisar a mano' si la confianza es baja.
- `demo_ruta = rutas_pru[0]` → Guarda el valor en `demo_ruta`.
- `print("Foto:", demo_ruta, "· real:", NOMBRES[y_pru[0]])` → `print`: muestra un valor por pantalla.
- `print(clasificar_foto(demo_ruta))` → `print`: muestra un valor por pantalla; `clasificar_foto`: devuelve (clase, confianza, probabilidades por clase) o 'revisar a mano' si la confianza es baja.
- `carpeta_tmp = tempfile.mkdtemp()` → Guarda en `carpeta_tmp` el resultado. `mkdtemp`: crea una carpeta temporal que se borra sola al acabar.
- `modelo.save(os.path.join(carpeta_tmp, "clasificador_alojamientos.keras"))` → `save`: guarda el modelo entrenado en un fichero; `join`: une una lista de textos en uno solo con un separador.
- `recargado = keras.models.load_model(os.path.join(carpeta_tmp, "clasificador…` → Guarda en `recargado` el resultado. `load_model`: carga un modelo guardado; `join`: une una lista de textos en uno solo con un separador.
- `assert clasificar_foto(demo_ruta, recargado)[0] == clasificar_foto(demo_rut…` → Comprueba que es verdad; si no, para con un mensaje.
- `shutil.rmtree(carpeta_tmp, ignore_errors=True)` → `rmtree`: borra una carpeta con todo lo que contiene.

### Celda 18 · 7. Rama Colab: MobileNetV2 con pesos de ImageNe… · 🏠

**Qué hace:** Practica `MobileNetV2`, `Input`, `preprocess_input`, `Model` y más (sección «7. Rama Colab: MobileNetV2 con pesos de…»).

```python
USAR_INTERNET = False        # ← True solo con conexión (Colab)

def construir_mobilenet(n_clases, tam=96, pesos=None):
    """MobileNetV2 (alpha 0.35) congelada + cabeza nueva. pesos='imagenet' descarga los pesos (requiere internet)."""
    base = keras.applications.MobileNetV2(input_shape=(tam, tam, 3), include_top=False, weights=pesos, alpha=0.35)
    base.trainable = False
    entrada = keras.layers.Input(shape=(TAM, TAM, 3))
    x = keras.layers.Resizing(tam, tam)(entrada)
    x = keras.applications.mobilenet_v2.preprocess_input(x)          # [0, 255] → [-1, 1]
    x = keras.layers.GlobalAveragePooling2D()(base(x, training=False))
    x = keras.layers.Dropout(0.3)(x)
    m = keras.Model(entrada, keras.layers.Dense(n_clases, activation="softmax")(x))
    m.compile(keras.optimizers.Adam(1e-3), "sparse_categorical_crossentropy", metrics=["accuracy"])
    return m

mn = construir_mobilenet(N_CLASES, pesos="imagenet" if USAR_INTERNET else None)      # offline: pesos aleatorios, solo estructura
print("MobileNetV2 construida:", mn.count_params(), "parámetros ·", "pesos de ImageNet" if USAR_INTERNET else "pesos aleatorios (sin entrenar)")
if USAR_INTERNET:
    mn.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=15, batch_size=16, verbose=0)
    print("MobileNetV2 + ImageNet, precisión en prueba:", round(mn.evaluate(X_pru, y_pru, verbose=0)[1], 3))
```

**Qué hace cada línea:**

- `USAR_INTERNET = False # ← True solo con conexión (Colab)` → Guarda el valor en `USAR_INTERNET`.
- `def construir_mobilenet(n_clases, tam=96, pesos=None):` → Define la función `construir_mobilenet`: MobileNetV2 (alpha 0.35) congelada + cabeza nueva. pesos='imagenet' descarga los pesos (requiere internet).
- `mn = construir_mobilenet(N_CLASES, pesos="imagenet" if USAR_INTERNET else N…` → Guarda en `mn` el resultado. `construir_mobilenet`: mobileNetV2 (alpha 0.35) congelada + cabeza nueva. pesos='imagenet' descarga los pesos (requiere internet).
- `print("MobileNetV2 construida:", mn.count_params(), "parámetros ·", "pesos…` → `print`: muestra un valor por pantalla; `count_params`: cuenta cuántos pesos tiene el modelo.
- `if USAR_INTERNET:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `evaluate`: calcula la pérdida y las métricas del modelo con unos datos.

### Celda 19 · 11. Resumen: qué has aprendido · 🏠

**Qué hace:** Limpieza (opcional): borra el dataset sintético generado; se puede regenerar cuando quieras con el script.

```python
# Limpieza (opcional): borra el dataset sintético generado; se puede regenerar cuando quieras con el script
if not USAR_DATASET_PROPIO and os.path.isdir("datos_sinteticos"):
    shutil.rmtree("datos_sinteticos", ignore_errors=True)
    print("Dataset sintético eliminado (no debe subirse al repositorio).")
```

**Qué hace cada línea:**

- `if not USAR_DATASET_PROPIO and os.path.isdir("datos_sinteticos"):` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `rmtree`: borra una carpeta con todo lo que contiene.

---
*Generado a partir de `laboratorios/fuentes/S11_04_reto_vision_cliente.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
