# ✍️ Miniapp 5 · Reconoce números escritos a mano

⭐ · 45 min · **clasificación con imágenes** · practica S08 (k-NN, SVM, bosque, árbol)

## Qué construyes
- Un programa que **mira una imagen de 8×8 píxeles y dice qué número es** (del 0 al 9).
- Ves **con tus ojos** en qué números se confunde, y cómo la SVM gana a un árbol.

## Datos
- Vienen **dentro de scikit-learn**: 1 797 imágenes de dígitos escritos a mano, de 8×8 píxeles (64 números por imagen, del 0 al 16: cuánta tinta hay en cada píxel).

## Paso a paso

1. **Carga y mira.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import ConfusionMatrixDisplay

digitos = load_digits()
X, y = digitos.data, digitos.target
print(X.shape, "→", X.shape[0], "imágenes de", X.shape[1], "píxeles")
fig, ejes = plt.subplots(2, 10, figsize=(12, 3))
for ax, img, n in zip(ejes.ravel(), digitos.images, y):
    ax.imshow(img, cmap="gray_r"); ax.set_title(n); ax.axis("off")
plt.show()
```

2. **Separa.** El examen (`test`) no se mira hasta el final.

```python
X_train, X_test, y_train, y_test, img_train, img_test = train_test_split(
    X, y, digitos.images, test_size=0.25, random_state=42, stratify=y)
print(len(y_train), "para entrenar ·", len(y_test), "para el examen (NO mirar)")
```

3. **El duelo (solo con `train`).** Acierto con validación cruzada.

```python
modelos = {
    "Siempre el más común (tonto)": DummyClassifier(strategy="prior"),
    "Logística": LogisticRegression(max_iter=3000),
    "Árbol": DecisionTreeClassifier(random_state=42),
    "k-NN (k=3)": KNeighborsClassifier(n_neighbors=3),
    "Bosque": RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=2),
    "SVM": SVC(random_state=42),
}
for n, m in modelos.items():
    print(f"{n:30s} {cross_val_score(m, X_train, y_train, cv=5).mean():.3f}")
```

4. **Prueba la SVM con distintos `gamma`** (cuánto «mira de cerca» cada punto, como en S08_04). Con valores extremos, aprende de memoria o se queda corta.

```python
for gamma in [0.0001, 0.001, 0.01, 0.1]:
    acierto = cross_val_score(SVC(gamma=gamma, random_state=42), X_train, y_train, cv=5).mean()
    print(f"gamma {gamma:<7} acierto {acierto:.3f}")
```

5. **El examen: UNA vez, con el campeón** (cambia `campeon` por el tuyo).

```python
campeon = modelos["SVM"].fit(X_train, y_train)
pred = campeon.predict(X_test)
print(f"Acierta {(pred == y_test).mean():.3f} · se equivoca en {(pred != y_test).sum()} de {len(y_test)} imágenes")
ConfusionMatrixDisplay.from_predictions(y_test, pred, cmap="Blues", colorbar=False)
plt.show()
```

6. **Dónde falla: míralo con tus ojos.** Las 10 imágenes que se ha equivocado.

```python
malas = np.where(pred != y_test)[0][:10]
fig, ejes = plt.subplots(1, len(malas), figsize=(1.4 * len(malas), 2))
for ax, i in zip(np.atleast_1d(ejes), malas):
    ax.imshow(img_test[i], cmap="gray_r"); ax.set_title(f"real {y_test[i]}\nmodelo {pred[i]}", fontsize=9); ax.axis("off")
plt.show()
```

## Tu app
- Elige una imagen del examen y mira qué dice el modelo.

```python
def reconoce(i):
    plt.imshow(img_test[i], cmap="gray_r"); plt.axis("off")
    plt.title(f"El modelo dice: {campeon.predict(X_test[i:i + 1])[0]}  ·  real: {y_test[i]}")
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
- **1 797 imágenes** de 64 píxeles; 10 de ellas dibujadas en la primera figura.
- Duelo (acierto): tonto **0,10** · árbol ≈ 0,85 · logística ≈ 0,97 · bosque ≈ 0,98 · SVM ≈ **0,99** · k-NN ≈ **0,99**.
- `gamma`: 0,0001 → 0,97 · **0,001 → 0,99** · 0,01 → 0,83 · 0,1 → 0,11. Si `gamma` es grande, la SVM **memoriza** cada imagen y deja de acertar con las nuevas.
- Examen con la SVM: acierta ≈ **0,99** (unos 4 errores de 450 imágenes).
- Tus cifras pueden diferir en el último decimal.

## Extra 🔴
- ¿Qué **dos números** se confunden más? Búscalos en la matriz y mira por qué.
- Prueba k-NN con `k=1` y con `k=15`: ¿cuál va mejor y por qué?
- Dibuja **tu propio número** en una cuadrícula de 8×8 (con valores de 0 a 16) y mira si lo reconoce.

## Cuidado
- Estas imágenes son **muy pequeñas y limpias**: con fotos de un móvil, el modelo no funcionaría sin más trabajo (por eso se usan redes neuronales).

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**. 🗣️ = respuesta de redacción u opinión: no hay cifra única.

#### Extra 1 · Dos números más confundidos
- **Qué hacer:**
  1. Pon a cero la diagonal de la matriz de confusión: lo que queda son los errores.
  2. Ordena y mira los pares (número real, número que dijo el modelo).
```python
from sklearn.metrics import confusion_matrix
errores = confusion_matrix(y_test, pred)
np.fill_diagonal(errores, 0)
print("(real, el modelo dijo, veces)")
for i in np.argsort(-errores.ravel())[:4]:
    real, dijo = divmod(int(i), 10)
    print(real, dijo, int(errores[real, dijo]))
```
- **Qué sale y por qué:**
  - Con solo **≈ 4 errores** de 450 los pares cambian de una partición a otra; en esta salen **8 → 1 (2 veces)**, 5 → 9 y 9 → 7. Son números que, **escritos a mano con 8 × 8 píxeles**, comparten trazos (el 8 con el 1 y el 9). **No hay un par «oficial»**: mira tu propia matriz.

#### Extra 2 · k-NN
- **Qué hacer:**
  1. Cambia `n_neighbors` a 1, 3 y 15 y compara la validación cruzada.
```python
for k in (1, 3, 15):
    print(f"k = {k:2d}: acierto {cross_val_score(KNeighborsClassifier(n_neighbors=k), X_train, y_train, cv=5).mean():.3f}")
```
- **Qué sale y por qué:**
  - **k = 1 → 0,991** · k = 3 → 0,988 · **k = 15 → 0,972**. Con pocos vecinos se pega a lo que **más se parece** (los dígitos limpios lo permiten); con 15 mira a **demasiados vecinos** y se mezcla con otras clases. Es el mismo equilibrio memorizar/generalizar del `gamma`.

#### Extra 3 · Su propio número (🗣️)
- **Qué hacer:**
  1. Escribe una matriz de 8×8 con valores de 0 (blanco) a 16 (tinta) dibujando tu número, **centrado**.
  2. Pásala aplanada (`reshape(1, -1)`) al campeón. Prueba también a **desplazarla** tres columnas y a **girarla** 90°, y mira si lo sigue reconociendo.
```python
mi_uno = np.array([[0, 0, 0, 12, 12, 0, 0, 0],
                   [0, 0, 8, 14, 12, 0, 0, 0],
                   [0, 0, 0, 12, 12, 0, 0, 0],
                   [0, 0, 0, 12, 12, 0, 0, 0],
                   [0, 0, 0, 12, 12, 0, 0, 0],
                   [0, 0, 0, 12, 12, 0, 0, 0],
                   [0, 0, 0, 12, 12, 0, 0, 0],
                   [0, 0, 8, 14, 14, 8, 0, 0]], dtype=float)
print("centrado:", campeon.predict(mi_uno.reshape(1, -1))[0])
print("desplazado tres columnas:", campeon.predict(np.roll(mi_uno, 3, axis=1).reshape(1, -1))[0])
print("girado 90°:", campeon.predict(np.rot90(mi_uno).reshape(1, -1))[0])
```
- **Qué sale y por qué:**
  - Con el 1 de ejemplo: **centrado → 1** (acierta), **desplazado tres columnas → 7** y **girado 90° → 4** (falla). Con tu dibujo saldrá otra cosa, pero la idea se repite: centrado suele acertar; **desplazado o girado, falla**. Es la lección: el modelo conoce **imágenes iguales a las que vio**.

#### Para cerrar
- **Para comentar:** `gamma` 0,1 → acierto 0,11: **memoriza** y deja de acertar. Con fotos de móvil haría falta una red (S11/S12).
- **Tarjeta de ejemplo:**
  - Mi app decide **qué número hay en la imagen** a partir de **64 píxeles**.
  - Antes de modelar tuve que **ajustar `gamma` de la SVM (0,001; con 0,1 memoriza)**.
  - Acierta **≈ 0,99** en el examen, frente a **0,10** del modelo tonto.
  - No debe usarse para **fotos reales de móvil**: son imágenes muy pequeñas y limpias.
