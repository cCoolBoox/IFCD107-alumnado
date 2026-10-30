# Código explicado · S11.03 · S11 · Práctica 3 — Detección de objetos y segmentación

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S11/2_Practica/S11_03_deteccion_segmentacion.ipynb) · [descargar](../S11_03_deteccion_segmentacion.ipynb) · ⏱ en clase: 35 min · 🏫 1 celdas de código en clase · 🏠 8 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `check_call`. |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `rng` | `np.random.default_rng(SEMILLA)` | 5 |
| `plantilla_img` | `Image.new("RGB", (24, 24), (230, 210, 160))` | 6 |
| `plantilla` | `saturacion(np.asarray(plantilla_img))` | 6 |
| `LADO` | `16` | 6 |
| `quedan` | `nms(cajas_brutas, punt_brutas, umbral_iou=0.3)` | 6 |
| `resultado` | `evaluar_detector(detector_color)` | 8 |
| `ious_umbral` | `[]` | 11 |
| `foto` | `load_sample_images().images[1]` | 12 |
| `peq` | `cv2.resize(foto, (160, 107)).reshape(-1, 3).astype("float…` | 12 |
| `criterio` | `(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20,…` | 12 |
| `segmentada` | `centros.astype("uint8")[etiquetas.ravel()].reshape(107, 1…` | 12 |
| `datos` | `[escena(rng) for _ in range(360)]` | 13 |
| `X_seg` | `np.stack([d[0] for d in datos]).astype("float32") / 255` | 13 |
| `Y_seg` | `np.stack([d[2] for d in datos]).astype("float32")[..., No…` | 13 |
| `seg` | `construir_segmentador()` | 13 |
| `h_seg` | `seg.fit(X_s_ent, Y_s_ent, epochs=12, batch_size=16, valid…` | 13 |
| `pred_seg` | `seg.predict(X_s_pru, verbose=0)[..., 0] > 0.5` | 13 |
| `iou_red` | `np.mean([iou_mascara(p, r[..., 0] > 0) for p, r in zip(pr…` | 13 |
| `iou_umb` | `np.mean([iou_mascara(detectar_color((x * 255).astype("uin…` | 13 |
| `USAR_INTERNET` | `False` | 14 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `iou` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `nms` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `average_precision` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `_col` | Función definida en el cuaderno. |
| `escena` | Devuelve (imagen RGB uint8, cajas reales [x1,y1,x2,y2], máscara booleana de sombrillas). |
| `dibujar_cajas` | Función definida en el cuaderno. |
| `saturacion` | Función definida en el cuaderno. |
| `detectar_plantilla` | Función definida en el cuaderno. |
| `detectar_color` | Devuelve (cajas, confianzas, máscara) de zonas de color vivo rojo–naranja–amarillo. |
| `emparejar` | Devuelve la lista de 0/1 (TP/FP) de las detecciones ordenadas por confianza decreciente. |
| `evaluar_detector` | AP, precisión y recall globales sobre n_escenas nuevas. `detector(img)` devuelve (cajas, confianzas). |
| `detector_color` | Función definida en el cuaderno. |
| `iou_mascara` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `dice` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `construir_segmentador` | Función definida en el cuaderno. |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `add` | Añade una capa al modelo de Keras (o un elemento a un conjunto). | 8 |
| `add_patch` | Añade una figura (rectángulo, círculo…) al gráfico. | 5 |
| `any` | Dice si ALGUNA condición es verdadera. | 5 |
| `append` | Añade un elemento al final de una lista. | 5, 7, 8, 11 |
| `argsort` | Devuelve las posiciones que ordenarían el array. | 8 |
| `array` | Crea una matriz o vector de NumPy (números que se pueden operar todos a la vez). | 5 |
| `asarray` | Convierte algo en array de NumPy sin copiarlo si ya lo es. | 5, 6 |
| `astype` | Cambia el tipo de los datos (por ejemplo, de texto a número). | 5, 7, 12, 13 |
| `axis` | Controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas. | 5, 6, 7, 12, 13, 14 |
| `boundingRect` | Calcula el rectángulo que encierra un contorno (OpenCV). | 7 |
| `check_call` | Ejecuta un comando del sistema y falla si algo sale mal. | 1, 14 |
| `clip` | Limita los valores a un mínimo y un máximo. | 5 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 13 |
| `contourArea` | Calcula el área de un contorno (OpenCV). | 7 |
| `Conv2D` | Capa convolucional: detecta patrones (bordes, formas) en imágenes. | 13 |
| `cvtColor` | Cambia el espacio de color de una imagen, por ejemplo a gris o a HSV (OpenCV). | 6, 7 |
| `default_rng` | Crea un generador de números aleatorios reproducible (con semilla). | 5, 8, 11, 13 |
| `detector` | La función detectora que se pasa como argumento. | 8 |
| `Draw` | Dibuja sobre una imagen (clase de Pillow). | 5, 6 |
| `ellipse` | Dibuja una elipse. | 5, 6 |
| `enumerate` | Recorre una lista dando a la vez la posición y el valor. | 5, 8 |
| `findContours` | Encuentra los contornos de los objetos de una máscara (OpenCV). | 7 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 13 |
| `float` | Convierte un valor en número decimal. | 6, 7 |
| `hypot` | Calcula la distancia (hipotenusa) entre dos puntos. | 5 |
| `imshow` | Muestra una imagen o una matriz como imagen. | 5, 6, 7, 12, 13, 14 |
| `Input` | Define la forma de los datos de entrada del modelo. | 13 |
| `int` | Convierte un valor en número entero. | 5, 14 |
| `integers` | Genera números enteros aleatorios. | 5 |
| `isinstance` | Comprueba si un valor es de un tipo concreto. | 8 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 8 |
| `kmeans` | Agrupa los píxeles por color con k-means (OpenCV). | 12 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 5, 6, 8 |
| `load_sample_images` | Carga dos fotos de ejemplo de scikit-learn. | 12 |
| `matchTemplate` | Busca en una imagen el lugar donde más se parece una plantilla (OpenCV). | 6 |
| `max` | Devuelve el valor más grande. | 8 |
| `MaxPooling2D` | Capa que reduce la imagen quedándose con el valor máximo de cada zona. | 13 |
| `mean` | Calcula la media. | 11, 13 |
| `min` | Devuelve el valor más pequeño. | 7 |
| `Model` | Crea un modelo de Keras indicando entradas y salidas. | 13 |
| `modelo_yolo` | El modelo YOLO ya cargado: detecta objetos en una imagen. | 14 |
| `morphologyEx` | Limpia una máscara quitando ruido o rellenando huecos (OpenCV). | 7 |
| `new` | Crea una imagen nueva en blanco (Pillow) del tamaño y color indicados. | 5, 6 |
| `normal` | Genera números aleatorios con forma de campana (normal). | 5 |
| `ones` | Crea un array lleno de unos. | 7 |
| `plot` | Dibuja una línea (o puntos unidos). | 14 |
| `predict` | Pide al modelo ya entrenado que haga predicciones. | 13 |
| `print` | Muestra un valor por pantalla. | 1, 6, 8, 11, 13, 14 |
| `random` | Número aleatorio entre 0 y 1. | 5 |
| `range` | Genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`. | 5, 8, 11, 13 |
| `ravel` | Aplana un array a una sola dimensión. | 12 |
| `rectangle` | Dibuja un rectángulo. | 5 |
| `Rectangle` | Dibuja un rectángulo. | 5 |
| `reshape` | Cambia la forma de un array (filas × columnas) sin cambiar los datos. | 12 |
| `resize` | Cambia el tamaño de una imagen. | 12 |
| `round` | Redondea un número a los decimales indicados. | 8, 11, 14 |
| `set` | Crea un conjunto (valores sin repetir) o, en un gráfico, fija varias opciones a la vez. | 8 |
| `set_random_seed` | Fija la semilla del azar de TensorFlow/Keras para repetir resultados. | 13 |
| `set_title` | Pone el título de un gráfico. | 5, 6, 7, 12, 13 |
| `setRNGSeed` | Fija la semilla del azar de OpenCV. | 12 |
| `show` | Muestra el gráfico. | 5, 6, 7, 12, 13, 14 |
| `stack` | Apila arrays en una dimensión nueva. | 13 |
| `subplots` | Crea una figura con uno o varios ejes (gráficos) dentro. | 5, 6, 7, 12, 13 |
| `sum` | Suma todos los valores. | 8 |
| `suptitle` | Pone un título general a toda la figura. | 6 |
| `text` | Escribe un texto en una posición del gráfico. | 5 |
| `tight_layout` | Ajusta los márgenes para que nada se solape. | 5, 6, 7, 12, 13 |
| `title` | Pone el título del gráfico. | 14 |
| `tolist` | Convierte un array o una columna en una lista de Python. | 14 |
| `tuple` | Crea una tupla (como una lista que no se puede modificar). | 5 |
| `uniform` | Número aleatorio decimal entre dos límites. | 5 |
| `UpSampling2D` | Capa que agranda la imagen repitiendo píxeles. | 13 |
| `where` | Elige un valor u otro según una condición (como un `if` para todos los datos a la vez). | 6 |
| `YOLO` | Modelo de detección de objetos YOLO (librería ultralytics). | 14 |
| `zip` | Recorre varias listas a la vez, emparejando sus elementos. | 6, 13, 14 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `check_call`.

```python
import os, sys, subprocess
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image, ImageDraw

try:
    import cv2
except ImportError:      # en Colab y en el taller ya viene instalado; esta celda solo actúa si faltara
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "opencv-python-headless"])
    import cv2

SEMILLA = 42
print("OpenCV", cv2.__version__)
```

**Qué hace cada línea:**

- `import os, sys, subprocess` → Trae `os`, `sys`, `subprocess` para poder usarlo.
- `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` → Guarda el valor en `os.environ["TF_CPP_MIN_…`.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import matplotlib.pyplot as plt` → Trae `matplotlib.pyplot` (lo llamamos `plt`) para poder usarlo.
- `import matplotlib.patches as mpatches` → Trae `matplotlib.patches` (lo llamamos `mpatches`) para poder usarlo.
- `from PIL import Image, ImageDraw` → Trae `Image`, `ImageDraw` de `PIL` para poder usarlo.
- `try:` → Intenta el bloque; si ocurre un error, pasa al `except` en vez de romperse. Dentro del bloque: `check_call`: ejecuta un comando del sistema y falla si algo sale mal.
- `SEMILLA = 42` → Guarda el valor en `SEMILLA`.
- `print("OpenCV", cv2.__version__)` → `print`: muestra un valor por pantalla.

### Celda 2 · 2. Cajas y la IoU (*Intersection over Union*) · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 3 · 3. NMS (*Non-Maximum Suppression*): quedarse co… · 🏫 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 4 · 4. Métricas: precisión, recall, AP y mAP con nú… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 5 · 5. Un detector clásico con OpenCV sobre imágene… · 🏠

**Qué hace:** Practica `default_rng`, `subplots`, `imshow`, `set_title` y más (sección «5. Un detector clásico con OpenCV sobre…»).

```python
def _col(rng, base, var=12):
    return tuple(int(np.clip(c + rng.integers(-var, var + 1), 0, 255)) for c in base)

def escena(rng, tam=128, n_max=8):
    """Devuelve (imagen RGB uint8, cajas reales [x1,y1,x2,y2], máscara booleana de sombrillas)."""
    img = Image.new("RGB", (tam, tam), _col(rng, (230, 210, 160)))
    d = ImageDraw.Draw(img)
    mar = int(tam * rng.uniform(0.15, 0.28))
    d.rectangle([0, 0, tam, mar], fill=_col(rng, (60, 140, 200), 15))
    masc = Image.new("L", (tam, tam), 0)
    dm = ImageDraw.Draw(masc)
    ocupados, cajas = [], []
    n = int(rng.integers(3, n_max + 1))
    for _ in range(300):
        if len(cajas) >= n + int(rng.integers(2, 5)) and len(cajas) >= n:
            break
        r = int(rng.integers(6, 10))
        cx, cy = int(rng.integers(r + 2, tam - r - 2)), int(rng.integers(mar + r + 3, tam - r - 2))
        if any(np.hypot(cx - x, cy - y) < r + rr - 4 for x, y, rr, _ in ocupados):   # se permite algo de solape
            continue
        if len([o for o in ocupados if o[3] == "s"]) < n:                      # sombrilla
            color = [(220, 40, 40), (240, 140, 30), (240, 210, 40), (245, 225, 140)][int(rng.integers(0, 4))]   # la 4.ª es pastel (poco saturada)
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=_col(rng, color, 10))
            d.ellipse([cx - 1, cy - 1, cx + 1, cy + 1], fill=(90, 60, 40))
            dm.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
            cajas.append([cx - r, cy - r, cx + r, cy + r]); ocupados.append((cx, cy, r, "s"))
        elif rng.random() < 0.5:                                                # palmera (distractor verde)
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=_col(rng, (30, 140, 60), 15)); ocupados.append((cx, cy, r, "p"))
        else:                                                                   # tumbona (distractor gris)
            d.rectangle([cx - r, cy - 3, cx + r, cy + 3], fill=_col(rng, (150, 150, 155), 15)); ocupados.append((cx, cy, r, "t"))
    a = np.asarray(img, dtype="float32") + rng.normal(0, 6, (tam, tam, 3))
    return np.clip(a, 0, 255).astype("uint8"), np.array(cajas), np.asarray(masc) > 0

def dibujar_cajas(eje, cajas, color, etiquetas=None):
    for k, (x1, y1, x2, y2) in enumerate(cajas):
        eje.add_patch(mpatches.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, edgecolor=color, lw=1.6))
        if etiquetas is not None:
            eje.text(x1, y1 - 1, etiquetas[k], color=color, fontsize=7, va="bottom")

rng = np.random.default_rng(SEMILLA)
img0, cajas0, masc0 = escena(rng)
fig, ejes = plt.subplots(1, 2, figsize=(9, 4.4))
ejes[0].imshow(img0); ejes[0].set_title("Escena sintética"); ejes[0].axis("off")
ejes[1].imshow(img0); dibujar_cajas(ejes[1], cajas0, "lime"); ejes[1].set_title(f"Cajas reales ({len(cajas0)} sombrillas)"); ejes[1].axis("off")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `def _col(rng, base, var=12):` → Define la función `_col`: Función definida en el cuaderno.
- `def escena(rng, tam=128, n_max=8):` → Define la función `escena`: Devuelve (imagen RGB uint8, cajas reales [x1,y1,x2,y2], máscara booleana de sombrillas).
- `def dibujar_cajas(eje, cajas, color, etiquetas=None):` → Define la función `dibujar_cajas`: Función definida en el cuaderno.
- `rng = np.random.default_rng(SEMILLA)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `img0, cajas0, masc0 = escena(rng)` → Guarda en `img0, cajas0, masc0` el resultado. `escena`: devuelve (imagen RGB uint8, cajas reales [x1,y1,x2,y2], máscara booleana de sombrillas).
- `fig, ejes = plt.subplots(1, 2, figsize=(9, 4.4))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ejes[0].imshow(img0); ejes[0].set_title("Escena sintética"); ejes[0].axis("…` → `imshow`: muestra una imagen o una matriz como imagen.
- `ejes[0].imshow(img0); ejes[0].set_title("Escena sintética"); ejes[0].axis("…` → `set_title`: pone el título de un gráfico.
- `ejes[0].imshow(img0); ejes[0].set_title("Escena sintética"); ejes[0].axis("…` → `axis`: controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas.
- … y 6 más con las mismas ideas.

### Celda 6 · 5. Un detector clásico con OpenCV sobre imágene… · 🏠

**Qué hace:** Practica `new`, `ellipse`, `subplots`, `suptitle` y más (sección «Detector 1: *template matching* (compar…»).

```python
def saturacion(img_rgb):
    return cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)[:, :, 1]

plantilla_img = Image.new("RGB", (24, 24), (230, 210, 160))
ImageDraw.Draw(plantilla_img).ellipse([4, 4, 20, 20], fill=(230, 100, 30))
plantilla = saturacion(np.asarray(plantilla_img))
LADO = 16    # caja que asignamos a cada acierto (diámetro aproximado de una sombrilla)

def detectar_plantilla(img_rgb, umbral=0.6):
    res = cv2.matchTemplate(saturacion(img_rgb), plantilla, cv2.TM_CCOEFF_NORMED)
    ys, xs = np.where(res >= umbral)
    cajas = [[x + 4, y + 4, x + 4 + LADO, y + 4 + LADO] for x, y in zip(xs, ys)]      # el círculo está a 4 px del borde de la plantilla
    return cajas, [float(res[y, x]) for x, y in zip(xs, ys)]

cajas_brutas, punt_brutas = detectar_plantilla(img0)
quedan = nms(cajas_brutas, punt_brutas, umbral_iou=0.3)
print(f"Detecciones brutas: {len(cajas_brutas)} → tras NMS: {len(quedan)} (sombrillas reales: {len(cajas0)})")

fig, ejes = plt.subplots(1, 2, figsize=(9, 4.4))
for eje, cajas, titulo in [(ejes[0], cajas_brutas, f"Antes de NMS ({len(cajas_brutas)} cajas)"),
                           (ejes[1], [cajas_brutas[i] for i in quedan], f"Después de NMS ({len(quedan)} cajas)")]:
    eje.imshow(img0); dibujar_cajas(eje, cajas, "red"); dibujar_cajas(eje, cajas0, "lime"); eje.set_title(titulo); eje.axis("off")
plt.suptitle("Rojo = detecciones · verde = cajas reales"); plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `def saturacion(img_rgb):` → Define la función `saturacion`: Función definida en el cuaderno.
- `plantilla_img = Image.new("RGB", (24, 24), (230, 210, 160))` → Guarda en `plantilla_img` el resultado. `new`: crea una imagen nueva en blanco (Pillow) del tamaño y color indicados.
- `ImageDraw.Draw(plantilla_img).ellipse([4, 4, 20, 20], fill=(230, 100, 30))` → `ellipse`: dibuja una elipse; `Draw`: dibuja sobre una imagen (clase de Pillow).
- `plantilla = saturacion(np.asarray(plantilla_img))` → Guarda en `plantilla` el resultado. `saturacion`: función definida en el cuaderno; `asarray`: convierte algo en array de NumPy sin copiarlo si ya lo es.
- `LADO = 16 # caja que asignamos a cada acierto (diámetro aproximado de una s…` → Guarda el valor en `LADO`.
- `def detectar_plantilla(img_rgb, umbral=0.6):` → Define la función `detectar_plantilla`: Función definida en el cuaderno.
- `cajas_brutas, punt_brutas = detectar_plantilla(img0)` → Guarda en `cajas_brutas, punt_brut…` el resultado. `detectar_plantilla`: función definida en el cuaderno.
- `quedan = nms(cajas_brutas, punt_brutas, umbral_iou=0.3)` → Guarda en `quedan` el resultado. `nms`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `print(f"Detecciones brutas: {len(cajas_brutas)} → tras NMS: {len(quedan)} (…` → `print`: muestra un valor por pantalla; `len`: cuenta cuántos elementos tiene una lista, texto o tabla.
- … y 5 más con las mismas ideas.

### Celda 7 · 5. Un detector clásico con OpenCV sobre imágene… · 🏠

**Qué hace:** Practica `subplots`, `imshow`, `set_title`, `axis` y más (sección «Detector 2: color + contornos»).

```python
def detectar_color(img_rgb, sat_min=120, area_min=40):
    """Devuelve (cajas, confianzas, máscara) de zonas de color vivo rojo–naranja–amarillo."""
    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    h, s, v = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
    mascara = (((h <= 35) | (h >= 170)) & (s >= sat_min) & (v >= 120)).astype("uint8") * 255
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cajas, conf = [], []
    for c in contornos:
        area = cv2.contourArea(c)
        if area < area_min:
            continue
        x, y, w, h_ = cv2.boundingRect(c)
        cajas.append([x, y, x + w, y + h_])
        conf.append(float(min(1.0, area / (np.pi / 4 * w * h_))))          # 1 = perfectamente circular/relleno
    return cajas, conf, mascara > 0

cajas_c, conf_c, masc_c = detectar_color(img0)
fig, ejes = plt.subplots(1, 3, figsize=(13, 4.2))
ejes[0].imshow(img0); ejes[0].set_title("Imagen"); ejes[0].axis("off")
ejes[1].imshow(masc_c, cmap="gray"); ejes[1].set_title("Máscara de color vivo (tras apertura)"); ejes[1].axis("off")
ejes[2].imshow(img0); dibujar_cajas(ejes[2], cajas_c, "red", [f"{c:.2f}" for c in conf_c]); dibujar_cajas(ejes[2], cajas0, "lime")
ejes[2].set_title("Cajas del detector (rojo) y reales (verde)"); ejes[2].axis("off")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `def detectar_color(img_rgb, sat_min=120, area_min=40):` → Define la función `detectar_color`: Devuelve (cajas, confianzas, máscara) de zonas de color vivo rojo–naranja–amarillo.
- `cajas_c, conf_c, masc_c = detectar_color(img0)` → Guarda en `cajas_c, conf_c, masc_c` el resultado. `detectar_color`: devuelve (cajas, confianzas, máscara) de zonas de color vivo rojo–naranja–amarillo.
- `fig, ejes = plt.subplots(1, 3, figsize=(13, 4.2))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ejes[0].imshow(img0); ejes[0].set_title("Imagen"); ejes[0].axis("off")` → `imshow`: muestra una imagen o una matriz como imagen.
- `ejes[0].imshow(img0); ejes[0].set_title("Imagen"); ejes[0].axis("off")` → `set_title`: pone el título de un gráfico.
- `ejes[0].imshow(img0); ejes[0].set_title("Imagen"); ejes[0].axis("off")` → `axis`: controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas.
- `ejes[1].imshow(masc_c, cmap="gray"); ejes[1].set_title("Máscara de color vi…` → `imshow`: muestra una imagen o una matriz como imagen.
- `ejes[1].imshow(masc_c, cmap="gray"); ejes[1].set_title("Máscara de color vi…` → `set_title`: pone el título de un gráfico.
- `ejes[1].imshow(masc_c, cmap="gray"); ejes[1].set_title("Máscara de color vi…` → `axis`: controla los ejes del gráfico (`axis("off")` los oculta); en pandas/NumPy, `axis` indica si se opera por filas o por columnas.
- … y 7 más con las mismas ideas.

### Celda 8 · 5. Un detector clásico con OpenCV sobre imágene… · 🏠

**Qué hace:** Practica `default_rng`, `argsort`, `set`, `enumerate` y más (sección «Evaluar el detector: emparejar deteccio…»).

```python
def emparejar(cajas_det, conf, cajas_reales, umbral_iou=0.5):
    """Devuelve la lista de 0/1 (TP/FP) de las detecciones ordenadas por confianza decreciente."""
    orden = np.argsort(conf)[::-1]
    usadas, es_tp = set(), []
    for i in orden:
        mejor, mejor_iou = None, umbral_iou
        for j, real in enumerate(cajas_reales):
            u = iou(cajas_det[i], real)
            if j not in usadas and u >= mejor_iou:
                mejor, mejor_iou = j, u
        if mejor is not None:
            usadas.add(mejor); es_tp.append(1)
        else:
            es_tp.append(0)
    return es_tp

def evaluar_detector(detector, n_escenas=30, semilla=100, umbral_iou=0.5):
    """AP, precisión y recall globales sobre n_escenas nuevas. `detector(img)` devuelve (cajas, confianzas)."""
    rng = np.random.default_rng(semilla)
    todos_conf, todos_tp, n_reales, n_detectadas = [], [], 0, 0
    for _ in range(n_escenas):
        img, reales, _ = escena(rng)
        cajas, conf = detector(img)
        n_reales += len(reales); n_detectadas += len(cajas)
        tp = emparejar(cajas, conf, reales, umbral_iou) if len(cajas) else []
        orden = np.argsort(conf)[::-1] if len(cajas) else []
        todos_conf += [conf[i] for i in orden]; todos_tp += tp
    orden = np.argsort(todos_conf)[::-1]
    tp_global = [todos_tp[i] for i in orden]
    return {"AP": average_precision(tp_global, n_reales),
            "precisión": sum(tp_global) / max(1, n_detectadas), "recall": sum(tp_global) / n_reales,
            "reales": n_reales, "detectadas": n_detectadas}

def detector_color(img):
    cajas, conf, _ = detectar_color(img)
    return cajas, conf

resultado = evaluar_detector(detector_color)
print({k: round(v, 3) if isinstance(v, float) else v for k, v in resultado.items()})
```

**Qué hace cada línea:**

- `def emparejar(cajas_det, conf, cajas_reales, umbral_iou=0.5):` → Define la función `emparejar`: Devuelve la lista de 0/1 (TP/FP) de las detecciones ordenadas por confianza decreciente.
- `def evaluar_detector(detector, n_escenas=30, semilla=100, umbral_iou=0.5):` → Define la función `evaluar_detector`: AP, precisión y recall globales sobre n_escenas nuevas. `detector(img)` devuelve (cajas, confianzas).
- `def detector_color(img):` → Define la función `detector_color`: Función definida en el cuaderno.
- `resultado = evaluar_detector(detector_color)` → Guarda en `resultado` el resultado. `evaluar_detector`: AP, precisión y recall globales sobre n_escenas nuevas. `detector(img)` devuelve (cajas, confianzas).
- `print({k: round(v, 3) if isinstance(v, float) else v for k, v in resultado.…` → `print`: muestra un valor por pantalla; `isinstance`: comprueba si un valor es de un tipo concreto; `round`: redondea un número a los decimales indicados.

### Celda 9 · 5. Un detector clásico con OpenCV sobre imágene… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 10 · 6. Segmentación · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 11 · 6. Segmentación · 🏠

**Qué hace:** Practica `default_rng`, `append`, `round`, `mean` (sección «6. Segmentación»).

```python
rng = np.random.default_rng(200)
ious_umbral = []
for _ in range(20):
    im, _, real = escena(rng)
    _, _, pred = detectar_color(im)
    ious_umbral.append((iou_mascara(pred, real), dice(pred, real)))
print("Segmentación por umbral de color: IoU media =", round(np.mean([a for a, _ in ious_umbral]), 3),
      "· Dice medio =", round(np.mean([b for _, b in ious_umbral]), 3))
```

**Qué hace cada línea:**

- `rng = np.random.default_rng(200)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `ious_umbral = []` → Guarda el valor en `ious_umbral`.
- `for _ in range(20):` → Repite el bloque de debajo para cada valor de `_` en `range(20)`. Dentro del bloque: `escena`: devuelve (imagen RGB uint8, cajas reales [x1,y1,x2,y2], máscara booleana de sombrillas); `detectar_color`: devuelve (cajas, confianzas, máscara) de zonas de color vivo rojo–naranja–amarillo; `iou_mascara`: función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)*.
- `print("Segmentación por umbral de color: IoU media =", round(np.mean([a for…` → `print`: muestra un valor por pantalla; `round`: redondea un número a los decimales indicados; `mean`: calcula la media.

### Celda 12 · 6. Segmentación · 🏠

**Qué hace:** Practica `astype`, `setRNGSeed`, `kmeans`, `reshape` y más (sección «Segmentación por agrupación de colores…»).

```python
from sklearn.datasets import load_sample_images
foto = load_sample_images().images[1]                                # flor (427×640×3)
peq = cv2.resize(foto, (160, 107)).reshape(-1, 3).astype("float32")
criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
cv2.setRNGSeed(SEMILLA)
_, etiquetas, centros = cv2.kmeans(peq, 4, None, criterio, 3, cv2.KMEANS_PP_CENTERS)
segmentada = centros.astype("uint8")[etiquetas.ravel()].reshape(107, 160, 3)
fig, ejes = plt.subplots(1, 2, figsize=(10, 3.6))
ejes[0].imshow(foto); ejes[0].set_title("Foto original"); ejes[0].axis("off")
ejes[1].imshow(segmentada); ejes[1].set_title("Segmentada con k-means (4 colores)"); ejes[1].axis("off")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `from sklearn.datasets import load_sample_images` → Trae `load_sample_images` de `sklearn.datasets` para poder usarlo.
- `foto = load_sample_images().images[1] # flor (427×640×3)` → Guarda en `foto` el resultado. `load_sample_images`: carga dos fotos de ejemplo de scikit-learn.
- `peq = cv2.resize(foto, (160, 107)).reshape(-1, 3).astype("float32")` → Guarda en `peq` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `reshape`: cambia la forma de un array (filas × columnas) sin cambiar los datos; `resize`: cambia el tamaño de una imagen.
- `criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)` → Guarda el valor en `criterio`.
- `cv2.setRNGSeed(SEMILLA)` → `setRNGSeed`: fija la semilla del azar de OpenCV.
- `_, etiquetas, centros = cv2.kmeans(peq, 4, None, criterio, 3, cv2.KMEANS_PP…` → Guarda en `_, etiquetas, centros` el resultado. `kmeans`: agrupa los píxeles por color con k-means (OpenCV).
- `segmentada = centros.astype("uint8")[etiquetas.ravel()].reshape(107, 160, 3)` → Guarda en `segmentada` el resultado. `reshape`: cambia la forma de un array (filas × columnas) sin cambiar los datos; `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `ravel`: aplana un array a una sola dimensión.
- `fig, ejes = plt.subplots(1, 2, figsize=(10, 3.6))` → Guarda en `fig, ejes` el resultado. `subplots`: crea una figura con uno o varios ejes (gráficos) dentro.
- `ejes[0].imshow(foto); ejes[0].set_title("Foto original"); ejes[0].axis("off…` → `imshow`: muestra una imagen o una matriz como imagen.
- … y 7 más con las mismas ideas.

### Celda 13 · 6. Segmentación · 🏠

**Qué hace:** Practica `set_random_seed`, `default_rng`, `fit`, `mean` y más (sección «Una mini red de segmentación (encoder-d…»).

```python
import tensorflow as tf
from tensorflow import keras
keras.utils.set_random_seed(SEMILLA)

rng = np.random.default_rng(300)
datos = [escena(rng) for _ in range(360)]
X_seg = np.stack([d[0] for d in datos]).astype("float32") / 255
Y_seg = np.stack([d[2] for d in datos]).astype("float32")[..., None]
X_s_ent, Y_s_ent, X_s_pru, Y_s_pru = X_seg[:300], Y_seg[:300], X_seg[300:], Y_seg[300:]

def construir_segmentador():
    e = keras.layers.Input(shape=(128, 128, 3))
    x = keras.layers.Conv2D(8, 3, padding="same", activation="relu")(e)
    x = keras.layers.MaxPooling2D()(x)                                         # 64×64
    x = keras.layers.Conv2D(16, 3, padding="same", activation="relu")(x)
    x = keras.layers.UpSampling2D()(x)                                         # 128×128
    x = keras.layers.Conv2D(8, 3, padding="same", activation="relu")(x)
    s = keras.layers.Conv2D(1, 1, activation="sigmoid")(x)                      # probabilidad por píxel
    m = keras.Model(e, s)
    m.compile("adam", "binary_crossentropy")
    return m

seg = construir_segmentador()
h_seg = seg.fit(X_s_ent, Y_s_ent, epochs=12, batch_size=16, validation_split=0.1, verbose=0)
pred_seg = seg.predict(X_s_pru, verbose=0)[..., 0] > 0.5
iou_red = np.mean([iou_mascara(p, r[..., 0] > 0) for p, r in zip(pred_seg, Y_s_pru)])
iou_umb = np.mean([iou_mascara(detectar_color((x * 255).astype("uint8"))[2], r[..., 0] > 0) for x, r in zip(X_s_pru, Y_s_pru)])
print(f"IoU de máscaras en 60 escenas nuevas → mini red: {iou_red:.3f} · umbral de color: {iou_umb:.3f}")

fig, ejes = plt.subplots(1, 3, figsize=(11, 3.8))
ejes[0].imshow(X_s_pru[0]); ejes[0].set_title("Imagen"); ejes[1].imshow(Y_s_pru[0, ..., 0], cmap="gray"); ejes[1].set_title("Máscara real")
ejes[2].imshow(pred_seg[0], cmap="gray"); ejes[2].set_title("Predicción de la red")
for e in ejes: e.axis("off")
plt.tight_layout(); plt.show()
```

**Qué hace cada línea:**

- `import tensorflow as tf` → Trae `tensorflow` (lo llamamos `tf`) para poder usarlo.
- `from tensorflow import keras` → Trae `keras` de `tensorflow` para poder usarlo.
- `keras.utils.set_random_seed(SEMILLA)` → `set_random_seed`: fija la semilla del azar de TensorFlow/Keras para repetir resultados.
- `rng = np.random.default_rng(300)` → Guarda en `rng` el resultado. `default_rng`: crea un generador de números aleatorios reproducible (con semilla).
- `datos = [escena(rng) for _ in range(360)]` → Guarda en `datos` el resultado. `escena`: devuelve (imagen RGB uint8, cajas reales [x1,y1,x2,y2], máscara booleana de sombrillas); `range`: genera la secuencia 0, 1, 2… (hasta uno antes del final); se usa en bucles `for`.
- `X_seg = np.stack([d[0] for d in datos]).astype("float32") / 255` → Guarda en `X_seg` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `stack`: apila arrays en una dimensión nueva.
- `Y_seg = np.stack([d[2] for d in datos]).astype("float32")[..., None]` → Guarda en `Y_seg` el resultado. `astype`: cambia el tipo de los datos (por ejemplo, de texto a número); `stack`: apila arrays en una dimensión nueva.
- `X_s_ent, Y_s_ent, X_s_pru, Y_s_pru = X_seg[:300], Y_seg[:300], X_seg[300:],…` → Guarda el valor en `X_s_ent, Y_s_ent, X_s_p…`.
- `def construir_segmentador():` → Define la función `construir_segmentador`: Función definida en el cuaderno.
- … y 16 más con las mismas ideas.

### Celda 14 · 7. Colab (opcional): un detector moderno con YO… · 🏠

**Qué hace:** Para tu dataset propio: modelo_yolo.train(data="datos.yaml", epochs=30, imgsz=640) (requiere etiquetas en formato YOLO).

```python
USAR_INTERNET = False        # ← True solo con conexión (Colab)

if USAR_INTERNET:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "ultralytics"])
    from ultralytics import YOLO
    modelo_yolo = YOLO("yolov8n.pt")                                                     # descarga los pesos
    resultados = modelo_yolo("https://ultralytics.com/images/bus.jpg", conf=0.25, iou=0.5)    # descarga la imagen
    r = resultados[0]
    plt.imshow(r.plot()[:, :, ::-1]); plt.axis("off"); plt.title("YOLOv8n (COCO)"); plt.show()
    for caja, cls, c in zip(r.boxes.xyxy.tolist(), r.boxes.cls.tolist(), r.boxes.conf.tolist()):
        print(r.names[int(cls)], round(c, 2), [round(v) for v in caja])
    # Para tu dataset propio: modelo_yolo.train(data="datos.yaml", epochs=30, imgsz=640)  (requiere etiquetas en formato YOLO)
else:
    print("Rama de Colab desactivada (USAR_INTERNET = False). El resto del notebook no la necesita.")
```

**Qué hace cada línea:**

- `USAR_INTERNET = False # ← True solo con conexión (Colab)` → Guarda el valor en `USAR_INTERNET`.
- `if USAR_INTERNET:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `check_call`: ejecuta un comando del sistema y falla si algo sale mal; `YOLO`: modelo de detección de objetos YOLO (librería ultralytics); `modelo_yolo`: el modelo YOLO ya cargado: detecta objetos en una imagen.

### Celda 15 · 8. Mini-reto integrador: contar sombrillas y af… · 🏠 · ejercicio

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

---
*Generado a partir de `laboratorios/fuentes/S11_03_deteccion_segmentacion.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
