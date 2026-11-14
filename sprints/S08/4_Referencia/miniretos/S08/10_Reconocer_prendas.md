# 👕 Miniapp 10 · ¿Qué prenda de ropa es?

⭐⭐ · 50 min · **clasificación con imágenes de ropa** · practica S08 (k-NN, SVM, bosque, logística)

## Qué construyes
- Un programa que **mira una foto pequeña (28×28 píxeles) y dice qué prenda es**: camiseta, pantalón, jersey, vestido, abrigo, sandalia, camisa, zapatilla, bolso o botín.
- Ves **dónde se confunde** una IA: con prendas parecidas (camiseta, camisa, jersey) falla como un humano con prisa.

## Datos
- **Fashion-MNIST**, un conjunto abierto de fotos de prendas de una tienda online (70 000 imágenes en blanco y negro). Se **descarga solo** desde OpenML al ejecutar la celda (unos segundos) y trabajamos con una **muestra de 6 000 imágenes** para que todo vaya rápido.
- Cada imagen son 784 números (28×28), de 0 (nada) a 255 (blanco). Los dividimos entre 255 para que queden entre 0 y 1.

## Paso a paso

1. **Descarga una muestra y mírala.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import ConfusionMatrixDisplay

nombres = ["camiseta", "pantalón", "jersey", "vestido", "abrigo", "sandalia", "camisa", "zapatilla", "bolso", "botín"]
bruto = fetch_openml("Fashion-MNIST", version=1, as_frame=False, parser="auto")
azar = np.random.default_rng(42).choice(len(bruto.data), 6000, replace=False)
X = bruto.data[azar] / 255.0
y = bruto.target[azar].astype(int)
print(X.shape, "→", X.shape[0], "imágenes de", X.shape[1], "píxeles")
fig, ejes = plt.subplots(2, 10, figsize=(12, 3))
for ax, img, n in zip(ejes.ravel(), X, y):
    ax.imshow(img.reshape(28, 28), cmap="gray_r"); ax.set_title(nombres[n], fontsize=8); ax.axis("off")
plt.show()
```

2. **Separa.** El examen (`test`) no se mira hasta el final.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print(len(y_train), "para entrenar ·", len(y_test), "para el examen (NO mirar)")
```

3. **El duelo (solo con `train`).** Acierto con validación cruzada. Es la celda que más tarda: un par de minutos.

```python
modelos = {
    "Siempre la más común (tonto)": DummyClassifier(strategy="prior"),
    "Logística": LogisticRegression(max_iter=300),
    "k-NN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Bosque": RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=2),
    "SVM": SVC(random_state=42),
}
for n, m in modelos.items():
    print(f"{n:30s} {cross_val_score(m, X_train, y_train, cv=3).mean():.3f}")
```

4. **El examen: UNA vez, con el campeón** (cambia `campeon` por el tuyo). Y la matriz de confusión: ¿qué prendas se confunden?

```python
campeon = modelos["SVM"].fit(X_train, y_train)
pred = campeon.predict(X_test)
print(f"Acierta {(pred == y_test).mean():.3f} · se equivoca en {(pred != y_test).sum()} de {len(y_test)} imágenes")
fig, ax = plt.subplots(figsize=(7, 7))
ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=nombres, cmap="Blues", colorbar=False, xticks_rotation=45, ax=ax)
plt.show()
```

5. **Las confusiones, con números.** Los 5 pares que más se mezclan.

```python
conf = pd.crosstab(pd.Series(y_test).map(dict(enumerate(nombres))), pd.Series(pred).map(dict(enumerate(nombres))))
pares = [(a, b, conf.loc[a, b]) for a in conf.index for b in conf.columns if a != b]
pd.DataFrame(sorted(pares, key=lambda t: -t[2])[:5], columns=["real", "el modelo dice", "veces"])
```

6. **Míralo con tus ojos.** Las 10 primeras imágenes en las que se ha equivocado.

```python
malas = np.where(pred != y_test)[0][:10]
fig, ejes = plt.subplots(1, len(malas), figsize=(1.5 * len(malas), 2.2))
for ax, i in zip(np.atleast_1d(ejes), malas):
    ax.imshow(X_test[i].reshape(28, 28), cmap="gray_r")
    ax.set_title(f"real: {nombres[y_test[i]]}\nmodelo: {nombres[pred[i]]}", fontsize=7); ax.axis("off")
plt.show()
```

## Tu app
- Elige una imagen del examen y mira qué dice el modelo.

```python
def reconoce(i):
    plt.imshow(X_test[i].reshape(28, 28), cmap="gray_r"); plt.axis("off")
    plt.title(f"El modelo dice: {nombres[campeon.predict(X_test[i:i + 1])[0]]}  ·  real: {nombres[y_test[i]]}")
    plt.show()

reconoce(0)
reconoce(1)
```

```python
# (solo Colab) un deslizador para recorrer el examen
from ipywidgets import interact
interact(reconoce, i=(0, len(y_test) - 1));
```

## Qué deberías ver
- **6 000 imágenes de 784 píxeles** y una fila de 20 prendas de muestra.
- Duelo (acierto, CV con 3 particiones): tonto **0,10** · logística ≈ 0,82 · k-NN ≈ 0,78 · bosque ≈ **0,83** · SVM ≈ **0,83**. Está todo muy igualado: con ropa es más difícil que con los números (donde se llega al 0,99).
- Examen con la SVM: acierta ≈ **0,85** (≈ 220 errores de 1 500 imágenes).
- Las confusiones que más se repiten: **camisa → camiseta**, **jersey → abrigo**, **camisa → abrigo** y **camisa → jersey**. Las prendas de arriba se confunden entre sí; **pantalón, bolso y botín se reconocen en ≈ 95 % de los casos** y la **camisa solo en ≈ 59 %**.
- Tus cifras pueden diferir unas centésimas según el reloj del equipo y la versión de las librerías.

## Extra 🔴
- Prueba la SVM con `gamma` de **0,0001**, **0,001** y **0,1**: ¿qué pasa?
- Usa **solo la mitad de los datos** para entrenar: ¿cuánto baja el acierto?
- ¿Qué tres prendas confunde más una persona a primera vista? ¿Coincide con el modelo?

## Cuidado
- Son fotos **pequeñas, centradas y en blanco y negro** de una sola tienda: con la foto de un armario, el modelo no sirve sin más trabajo (por eso existen las redes neuronales).
- Tu cifra puede variar unas centésimas según la muestra que salga.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**. 🗣️ = respuesta de redacción u opinión: no hay cifra única.

- **Extra 1 · `gamma` de la SVM (CV con 3 particiones):** **0,0001 → 0,641** (se queda corta) · **0,001 → 0,764** · **0,1 → 0,740** (memoriza) · el valor por defecto (`scale` ≈ 0,010) da ≈ 0,83. El óptimo está **en medio**: ni muy suave ni muy pegado a cada imagen.
- **Extra 2 · Mitad de los datos (2 250 de las 4 500 de entrenamiento):** examen **0,826** frente a **0,851** con todos: **baja unos 2,5 puntos**. Con 6 000 imágenes ya estamos en la parte plana de la curva.
- **Extra 3 · Qué confunde una persona (🗣️):** camisa, camiseta y jersey/abrigo, a primera vista. **Coincide con el modelo**: las prendas de arriba se parecen en silueta. Es un buen momento para decir que **la IA se equivoca donde se equivocan las personas** cuando solo ve una silueta pequeña.
- **Para comentar:** pantalón, bolso y botín: ≈ 95 %; la camisa solo ≈ 59 %. Por eso existen las **redes** (ver S12-01).
- **Tarjeta de ejemplo:**
  - Mi app decide **qué prenda hay en la foto** a partir de **784 píxeles en gris**.
  - Antes de modelar tuve que **escalar los píxeles (0 a 1) y comparar cinco modelos**.
  - Acierta **0,85** en el examen (≈ 220 errores de 1 500), frente a **0,10** del modelo tonto.
  - No debe usarse para **fotos de un armario real**: son fotos pequeñas, centradas y en gris.
