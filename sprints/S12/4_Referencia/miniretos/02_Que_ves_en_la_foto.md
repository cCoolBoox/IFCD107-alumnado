# 📷 Miniapp 2 · ¿Qué ve una IA en tu foto?

⭐⭐ · 55 min · **visión con una red ya entrenada** · practica S11 (CNN, transfer learning, qué mira una red)

## Qué construyes
- Una app que **mira una foto y dice qué hay**, usando **MobileNetV2**, una red que ya vio un millón de fotos.
- La **pones a prueba** (girada, borrosa, recortada, en blanco y negro) y después le **enseñas dos objetos tuyos** con 15 fotos de cada uno.

## Datos
- **Dos fotos de ejemplo** que ya vienen con scikit-learn (un templo y una flor), y **tus propias fotos** en Colab.
- Para el último paso: **15 fotos o más de dos objetos** (por ejemplo, tu taza y tu mochila; o gatos y perros). Se suben a Colab arrastrándolas al panel de archivos.

## Paso a paso

1. **Carga la red** (se descarga sola, unos 14 MB) y define la función que pregunta «¿qué ves?». Los nombres de las clases están en inglés (son las de ImageNet).

```python
import warnings, os; warnings.filterwarnings("ignore"); os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np, pandas as pd, matplotlib.pyplot as plt, tensorflow as tf
from tensorflow import keras
from sklearn.datasets import load_sample_images
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

modelo = keras.applications.MobileNetV2(weights="imagenet")
print("Pesos de la red:", f"{modelo.count_params():,}", "· 1 000 clases posibles")

def que_ves(imagen, top=3):
    """imagen: matriz (alto, ancho, 3) con valores de 0 a 255."""
    x = tf.image.resize(np.asarray(imagen, dtype="float32")[None], (224, 224)).numpy()
    return [(nombre, round(float(p), 2)) for _, nombre, p in decode_predictions(modelo.predict(preprocess_input(x), verbose=0), top=top)[0]]

ejemplos = load_sample_images().images
templo, flor = ejemplos
fig, ejes = plt.subplots(1, 2, figsize=(9, 3))
for ax, img, t in zip(ejes, ejemplos, ["templo", "flor"]):
    ax.imshow(img); ax.set_title(t); ax.axis("off")
plt.show()
print("Templo:", que_ves(templo))
print("Flor:  ", que_ves(flor))
```

2. **Ponla a prueba.** Cambia la foto de cinco formas y mira si sigue acertando.

```python
def variantes(img):
    img = np.asarray(img, dtype="float32")
    gris = img.mean(axis=2, keepdims=True).repeat(3, axis=2)
    borrosa = tf.nn.avg_pool2d(img[None], 15, 1, "SAME").numpy()[0]
    alto, ancho = img.shape[:2]
    return {"original": img, "girada 90°": np.rot90(img), "en blanco y negro": gris, "borrosa": borrosa,
            "oscura": img * 0.25, "recorte pequeño": img[alto // 3: alto // 3 + alto // 4, ancho // 3: ancho // 3 + ancho // 4]}

filas = []
for nombre_foto, foto in [("templo", templo), ("flor", flor)]:
    for cambio, v in variantes(foto).items():
        mejor, p = que_ves(v, top=1)[0]
        filas.append({"foto": nombre_foto, "cambio": cambio, "dice": mejor, "seguridad": p})
pd.DataFrame(filas)
```

3. **Sube tus fotos y mira qué dicen.** (Solo en Colab: arrastra una foto o más al panel de archivos y pon su nombre.)

```python
# (solo Colab) cambia el nombre por el de tu foto, subida al panel de la izquierda
from PIL import Image
foto_propia = np.asarray(Image.open("mi_foto.jpg").convert("RGB"))
plt.imshow(foto_propia); plt.axis("off"); plt.show()
print(que_ves(foto_propia))
```

4. **Enséñale lo tuyo (transfer learning).** Crea en Colab una carpeta `fotos/` con **una subcarpeta por objeto** (por ejemplo, `fotos/taza/` y `fotos/mochila/`, 15 fotos o más en cada una). La red se queda como «ojos» y entrenamos encima una logística. Si no hay fotos, la celda te lo dice y no falla.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
ojos = keras.Model(modelo.input, modelo.get_layer("global_average_pooling2d").output)
clases = sorted(d for d in os.listdir("fotos") if os.path.isdir(f"fotos/{d}")) if os.path.isdir("fotos") else []
if len(clases) < 2:
    print("Aún no hay fotos: crea fotos/objeto_a/ y fotos/objeto_b/ con 15 fotos o más en cada una y vuelve a ejecutar.")
else:
    def caracteristicas(ruta):
        img = keras.utils.load_img(ruta, target_size=(224, 224))
        return ojos.predict(preprocess_input(np.asarray(img, dtype="float32")[None]), verbose=0)[0]
    rutas = [(f"fotos/{c}/{f}", c) for c in clases for f in sorted(os.listdir(f"fotos/{c}")) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    Fotos = np.array([caracteristicas(r) for r, _ in rutas]); etiquetas = np.array([c for _, c in rutas])
    print({c: int((etiquetas == c).sum()) for c in clases}, "fotos por objeto")
    acierto = cross_val_score(LogisticRegression(max_iter=2000), Fotos, etiquetas, cv=min(5, int(min((etiquetas == c).sum() for c in clases)))).mean()
    print(f"Acierto con validación cruzada: {acierto:.2f} (el tonto acertaría {1 / len(clases):.2f})")
    tuyo = LogisticRegression(max_iter=2000).fit(Fotos, etiquetas)
```

## Tu app
- Una función que dice **qué ve la red general** y, si has entrenado la tuya, **qué ve tu red**.

```python
def mi_app(imagen):
    print("La red general dice:", que_ves(imagen))
    if "tuyo" in globals():
        x = tf.image.resize(np.asarray(imagen, dtype="float32")[None], (224, 224)).numpy()
        f = ojos.predict(preprocess_input(x), verbose=0)
        print("Tu red dice:", tuyo.predict(f)[0], "·", {str(c): round(float(p), 2) for c, p in zip(tuyo.classes_, tuyo.predict_proba(f)[0])})

mi_app(flor)
```

## Qué deberías ver
- MobileNetV2 tiene **≈ 3,5 millones de pesos** y 1 000 clases posibles. Con las fotos de ejemplo: el **templo** sale `monastery` (0,31), `palace` (0,18), `church` (0,11); la **flor** sale `honeycomb` (0,20), `bee` (0,08)… **no acierta a la primera**, y eso es parte de la lección.
- Al cambiar el templo: girado 90° dice `freight_car` (0,46); recorte pequeño dice `organ` (0,52); en blanco y negro dice `church`. La flor sigue en `honeycomb` casi siempre, y borrosa dice `fig` con **0,71** de seguridad. **Se equivoca con mucha seguridad.**
- Los pasos 3 y 4 dependen de tus fotos: si aún no hay, las celdas lo dicen y no fallan. Con 15 fotos de dos objetos distintos, lo normal es acertar **más del 90 %** (el tonto, 50 %). No hay cifra de referencia: es la tuya.
- La app muestra primero lo que dice la red general y, si has entrenado la tuya, qué dice ella y con qué probabilidad.

## Extra 🔴
- Prueba con **fotos difíciles**: un objeto a medias, de noche, con otra cosa delante. ¿Cuándo se equivoca más?
- En el paso 4, pon fotos de **dos objetos muy parecidos** (dos tazas de colores distintos): ¿sigue acertando?
- Mide cuántas fotos hacen falta: entrena con 5, 10 y 15 por objeto y compara.

## Cuidado
- La red general **solo conoce 1 000 cosas** de ImageNet: si tu objeto no está, te dirá algo parecido con mucha seguridad.
- Sube solo **fotos tuyas o libres**, sin personas reconocibles: no son datos para compartir.
