# 👕 Miniapp 1 · Sube la escalera: ¿qué red reconoce mejor la ropa?

⭐⭐⭐ · 55 min · **tu primera red neuronal con imágenes** · practica S10 (red densa, dropout, parada temprana) y S11 (CNN, transfer learning)

## Qué construyes
- Un reconocedor de prendas (camiseta, pantalón, zapatilla…) que **entrenas tú** y que subes de nivel en tres escalones: **red densa → CNN → transfer learning**.
- Comparas cada escalón con la **SVM de S08**: ¿merece la pena una red?

## Datos
- **Fashion-MNIST**: fotos de ropa de 28×28 píxeles en blanco y negro. Se descargan solas desde OpenML y usamos una **muestra de 10 000** para que vaya rápido.
- Si ya hiciste la miniapp 10 de S08, ahí tienes la nota de partida: SVM ≈ 0,85.

## Paso a paso

1. **Descarga, mira y separa en tres partes:** entrenar (`Xa`), validar (`Xv`, para elegir) y examen (`Xte`, **una sola vez**).

```python
import warnings, os; warnings.filterwarnings("ignore"); os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np, pandas as pd, matplotlib.pyplot as plt, tensorflow as tf
from tensorflow import keras
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay

nombres = ["camiseta", "pantalón", "jersey", "vestido", "abrigo", "sandalia", "camisa", "zapatilla", "bolso", "botín"]
bruto = fetch_openml("Fashion-MNIST", version=1, as_frame=False, parser="auto")
azar = np.random.default_rng(42).choice(len(bruto.data), 10000, replace=False)
X = bruto.data[azar] / 255.0
y = bruto.target[azar].astype(int)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
Xa, Xv, ya, yv = train_test_split(X_tr, y_tr, test_size=0.2, random_state=42, stratify=y_tr)
print(len(ya), "para entrenar ·", len(yv), "para validar ·", len(y_te), "para el examen (NO mirar)")
fig, ejes = plt.subplots(1, 10, figsize=(12, 1.8))
for ax, img, n in zip(ejes, Xa, ya):
    ax.imshow(img.reshape(28, 28), cmap="gray_r"); ax.set_title(nombres[n], fontsize=8); ax.axis("off")
plt.show()
```

2. **Las notas de partida:** el modelo tonto y la SVM de S08.

```python
notas = {}
notas["Siempre la más común (tonto)"] = DummyClassifier(strategy="prior").fit(Xa, ya).score(Xv, yv)
notas["SVM (S08)"] = SVC(random_state=42).fit(Xa, ya).score(Xv, yv)
for n, a in notas.items():
    print(f"{n:30s} {a:.3f}")
```

3. **Escalón 1: red densa.** Una red con dos capas ocultas, **con y sin dropout**, y con **parada temprana**. Se repite con **3 semillas**: una red no da siempre lo mismo.

```python
def red_densa(dropout, semilla):
    keras.utils.set_random_seed(semilla)
    m = keras.Sequential([keras.layers.Input((784,)),
                          keras.layers.Dense(128, activation="relu"), keras.layers.Dropout(dropout),
                          keras.layers.Dense(64, activation="relu"), keras.layers.Dropout(dropout),
                          keras.layers.Dense(10, activation="softmax")])
    m.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
    h = m.fit(Xa, ya, validation_data=(Xv, yv), epochs=60, batch_size=64, verbose=0,
              callbacks=[keras.callbacks.EarlyStopping(patience=6, restore_best_weights=True)])
    return m, h

curvas = {}
for dropout in (0.0, 0.3):
    accs = []
    for semilla in range(3):
        m, h = red_densa(dropout, semilla)
        accs.append(m.evaluate(Xv, yv, verbose=0)[1])
        curvas[dropout] = h
    print(f"Red densa con dropout {dropout}: validación {np.mean(accs):.3f} ± {np.std(accs):.3f} (3 semillas)")
    notas[f"Red densa (dropout {dropout})"] = float(np.mean(accs))
for dropout, h in curvas.items():
    plt.plot(h.history["loss"], label=f"entrenamiento · dropout {dropout}"); plt.plot(h.history["val_loss"], "--", label=f"validación · dropout {dropout}")
plt.xlabel("época"); plt.ylabel("error"); plt.legend(); plt.title("Curvas de aprendizaje: cuando se separan, hay sobreajuste"); plt.show()
```

4. **Escalón 2: CNN.** Mira la imagen en 2D con filtros, en vez de como 784 números sueltos.

```python
keras.utils.set_random_seed(0)
cnn = keras.Sequential([keras.layers.Input((28, 28, 1)),
                        keras.layers.Conv2D(16, 3, activation="relu"), keras.layers.MaxPooling2D(),
                        keras.layers.Conv2D(32, 3, activation="relu"), keras.layers.MaxPooling2D(),
                        keras.layers.Flatten(), keras.layers.Dropout(0.3),
                        keras.layers.Dense(64, activation="relu"), keras.layers.Dense(10, activation="softmax")])
cnn.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
h_cnn = cnn.fit(Xa.reshape(-1, 28, 28, 1), ya, validation_data=(Xv.reshape(-1, 28, 28, 1), yv), epochs=40, batch_size=64, verbose=0,
                callbacks=[keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)])
notas["CNN"] = cnn.evaluate(Xv.reshape(-1, 28, 28, 1), yv, verbose=0)[1]
print(f"CNN: validación {notas['CNN']:.3f} · paró en la época {len(h_cnn.history['loss'])} · {cnn.count_params():,} pesos")
```

5. **Escalón 3: transfer learning.** Usamos **MobileNetV2** (ya entrenada con millones de fotos) solo para extraer características, y encima una logística. Las imágenes se agrandan a 96×96 y se pasan a 3 canales.

```python
base = keras.applications.MobileNetV2(input_shape=(96, 96, 3), include_top=False, weights="imagenet", pooling="avg")
def caracteristicas(A):
    img = tf.image.resize(A.reshape(-1, 28, 28, 1), (96, 96))
    img = tf.repeat(img, 3, axis=-1) * 2 - 1
    return base.predict(img, batch_size=128, verbose=0)
Fa, Fv, Fte = caracteristicas(Xa), caracteristicas(Xv), caracteristicas(X_te)
transfer = LogisticRegression(max_iter=2000).fit(Fa, ya)
notas["Transfer (MobileNetV2 + logística)"] = transfer.score(Fv, yv)
print(f"Transfer learning: validación {notas['Transfer (MobileNetV2 + logística)']:.3f}")
```

6. **La tabla y el examen.** Elige el campeón por la nota de validación y mídelo **una sola vez** con el examen.

```python
tabla = pd.Series(notas, name="acierto en validación").sort_values(ascending=False).round(3)
print(tabla)
campeon = tabla.index[0]
print("Campeón:", campeon)
if campeon.startswith("CNN"):
    pred = cnn.predict(X_te.reshape(-1, 28, 28, 1), verbose=0).argmax(1)
elif campeon.startswith("Transfer"):
    pred = transfer.predict(Fte)
elif campeon.startswith("SVM"):
    pred = SVC(random_state=42).fit(Xa, ya).predict(X_te)
else:
    pred = red_densa(0.3, 0)[0].predict(X_te, verbose=0).argmax(1)
print(f"Examen: acierta {(pred == y_te).mean():.3f} · se equivoca en {(pred != y_te).sum()} de {len(y_te)} imágenes")
fig, ax = plt.subplots(figsize=(7, 7))
ConfusionMatrixDisplay.from_predictions(y_te, pred, display_labels=nombres, cmap="Blues", colorbar=False, xticks_rotation=45, ax=ax)
plt.show()
```

## Tu app
- Elige una imagen del examen y mira qué dice tu campeón y busca sus fallos.

```python
def reconoce(i):
    plt.imshow(X_te[i].reshape(28, 28), cmap="gray_r"); plt.axis("off")
    plt.title(f"Dice: {nombres[pred[i]]} · real: {nombres[y_te[i]]}")
    plt.show()

reconoce(0)
reconoce(1)
fallos = np.where(pred != y_te)[0]
print("Primeros fallos (índices):", fallos[:5], "→ pruébalos con reconoce(i)")
```

```python
# (solo Colab) un deslizador para recorrer el examen
from ipywidgets import interact
interact(reconoce, i=(0, len(y_te) - 1));
```

## Qué deberías ver
- **10 000 imágenes:** 6 000 para entrenar, 1 500 para validar y 2 500 para el examen.
- Validación: tonto **0,10** · SVM **0,845** · red densa sin dropout **0,843 ± 0,004** · con dropout 0,3 **0,856 ± 0,002** (3 semillas) · CNN **0,859** (paró en la época ≈ 23, con ≈ 57 000 pesos) · transfer learning **0,853**.
- **Los cuatro escalones quedan a menos de 2 puntos.** Con 6 000 imágenes, una red más grande no es una gran mejora: las redes brillan con muchos más datos. El dropout sí ayuda a la red densa.
- Examen con el campeón (la CNN): acierta ≈ **0,85** (≈ 370 errores de 2 500). Se confunden camisa, camiseta, jersey y abrigo.
- Tus cifras pueden variar unas centésimas: las redes dependen de la semilla.
- La celda del transfer learning y la CNN son las que más tardan (≈ 2 minutos en total).

## Extra 🔴
- Añade una **tercera capa** a la red densa o más filtros a la CNN: ¿mejora?, ¿cuántos pesos más tiene?
- Prueba con solo **2 000 imágenes** para entrenar: ¿qué escalón aguanta mejor con pocos datos?
- Entrena la CNN **con y sin** `EarlyStopping` y mira la curva de aprendizaje.

## Cuidado
- Las redes **dependen de la semilla**: no presentes una sola ejecución como «la» nota.
- Son fotos pequeñas, centradas y de una sola tienda: con la foto de un armario, el modelo no sirve sin más trabajo.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

#### Extra 1 · Más capas o más filtros
- **Qué hacer:**
  1. Escribe funciones que construyan la red densa con las capas que quieras y la CNN con los filtros que quieras (con `count_params()` ves los pesos).
  2. Prueba una **tercera capa** (128-64-32) y una CNN con **32 y 64 filtros**.
```python
def red_densa_capas(capas, semilla=0, X1=Xa, y1=ya):
    keras.utils.set_random_seed(semilla)
    bloques = [c for u in capas for c in (keras.layers.Dense(u, activation="relu"), keras.layers.Dropout(0.3))]
    m = keras.Sequential([keras.layers.Input((784,))] + bloques + [keras.layers.Dense(10, activation="softmax")])
    m.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
    m.fit(X1, y1, validation_data=(Xv, yv), epochs=60, batch_size=64, verbose=0,
          callbacks=[keras.callbacks.EarlyStopping(patience=6, restore_best_weights=True)])
    return m

def crear_cnn(f1=16, f2=32, parada=True, X1=Xa, y1=ya):
    keras.utils.set_random_seed(0)
    c = keras.Sequential([keras.layers.Input((28, 28, 1)),
                          keras.layers.Conv2D(f1, 3, activation="relu"), keras.layers.MaxPooling2D(),
                          keras.layers.Conv2D(f2, 3, activation="relu"), keras.layers.MaxPooling2D(),
                          keras.layers.Flatten(), keras.layers.Dropout(0.3),
                          keras.layers.Dense(64, activation="relu"), keras.layers.Dense(10, activation="softmax")])
    c.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
    callbacks = [keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)] if parada else []
    h = c.fit(X1.reshape(-1, 28, 28, 1), y1, validation_data=(Xv.reshape(-1, 28, 28, 1), yv), epochs=40, batch_size=64, verbose=0, callbacks=callbacks)
    return c, h

for capas in ((128, 64), (128, 64, 32)):
    m = red_densa_capas(capas)
    print("red densa", capas, "· validación", round(m.evaluate(Xv, yv, verbose=0)[1], 3), "· pesos", m.count_params())
c, _ = crear_cnn(32, 64)
print("CNN 32/64 filtros · validación", round(c.evaluate(Xv.reshape(-1, 28, 28, 1), yv, verbose=0)[1], 3), "· pesos", c.count_params())
```
- **Qué sale y por qué:**
  - **Tercera capa** (128-64-32): validación **0,841** (una semilla) frente a **0,856** de la de dos capas. **No mejora**, y suma ≈ 1 800 pesos (111 146 frente a 109 386).
  - **CNN con 32 y 64 filtros**: **0,859** (igual) y **121 930 pesos** (más del doble que los ≈ 57 000 de la original).
  - Más grande **no** es mejor con 6 000 imágenes.

#### Extra 2 · Solo 2 000 imágenes de entrenamiento (validación)
- **Qué hacer:**
  1. Recorta el entrenamiento a las **2 000 primeras imágenes** (`Xa[:2000]`).
  2. Repite los cuatro escalones (SVM, red densa, CNN y transfer con las características `Fa[:2000]`) y compara con la tabla de 6 000.
```python
n = 2000
Xs, ys = Xa[:n], ya[:n]
print("SVM:         ", round(SVC(random_state=42).fit(Xs, ys).score(Xv, yv), 3))
print("Red densa:   ", round(red_densa_capas((128, 64), X1=Xs, y1=ys).evaluate(Xv, yv, verbose=0)[1], 3))
c, _ = crear_cnn(X1=Xs, y1=ys)
print("CNN:         ", round(c.evaluate(Xv.reshape(-1, 28, 28, 1), yv, verbose=0)[1], 3))
print("Transfer:    ", round(LogisticRegression(max_iter=2000).fit(Fa[:n], ys).score(Fv, yv), 3))
```
- **Qué sale y por qué:**
  - SVM **0,815** · red densa **0,815** · CNN **0,819** · **transfer learning 0,847**. **El transfer aguanta mejor** con pocos datos: ya llega «aprendido» de ImageNet (con 6 000: 0,845 · 0,856 · 0,859 · 0,853). Esa es la razón de usarlo.

#### Extra 3 · CNN con y sin `EarlyStopping`
- **Qué hacer:**
  1. Entrena la CNN con `parada=False` (40 épocas, sin `EarlyStopping`) y dibuja la curva de entrenamiento y de validación.
  2. Mira en qué época está la mejor validación y qué pasa con el entrenamiento.
```python
c, h = crear_cnn(parada=False)
plt.plot(h.history["accuracy"], label="entrenamiento"); plt.plot(h.history["val_accuracy"], label="validación")
plt.xlabel("época"); plt.legend(); plt.show()
val = h.history["val_accuracy"]
print("mejor validación:", round(max(val), 3), "en la época", int(np.argmax(val)) + 1, "· al final:", round(val[-1], 3), "· entrenamiento al final:", round(h.history["accuracy"][-1], 3))
```
- **Qué sale y por qué:**
  - Con parada temprana: paró en la época ≈ 23, validación **0,859**.
  - Sin parada (40 épocas): al final **0,859**, la mejor **0,871 en la época 33**, y la precisión en entrenamiento llega a **0,92**: la red **sigue aprendiendo del entrenamiento** mientras la validación se **estanca y oscila**.
  - Para comentar: el 0,871 frente al 0,859 es **ruido** (con 1 500 imágenes, el margen es de ≈ ±0,9 puntos). La **parada temprana** no es para ganar nota, es para **no seguir gastando y no memorizar**.

#### Para cerrar
- **Para comentar:** los cuatro escalones quedan a menos de 2 puntos: **más red no es más acierto** con pocos datos. Pero **sí hay diferencia con el dropout** en la red densa.
- **Tarjeta de ejemplo:**
  - Mi IA decide **qué prenda hay en la foto** a partir de **784 píxeles**.
  - Se equivoca **≈ 370 de 2 500 (15 %)**, frente al **90 %** de error del modelo tonto; entre SVM, red y CNN hay **menos de 2 puntos**.
  - Falla cuando **hay camisas, camisetas, jerséis o abrigos** (se parecen en silueta).
  - No debe usarse para **fotos de un armario real**.
