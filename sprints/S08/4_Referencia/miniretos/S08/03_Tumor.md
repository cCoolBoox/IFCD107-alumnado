# 🎗️ Miniapp 3 · ¿Tumor benigno o maligno?

⭐ · 45 min · **clasificación** · practica S07 (umbral, matriz de confusión) y S08 (árbol, bosque, SVM, boosting)

## Qué construyes
- Un **sistema de apoyo** que mira las medidas de un tumor (radio, textura, perímetro…) y dice cuánto se parece a un tumor maligno.
- Aprendes la lección más importante de la IA en salud: **no es lo mismo fallar a un lado que al otro**.

## Datos
- Vienen **dentro de scikit-learn**: 569 pacientes con 30 medidas de imágenes de células. Es un conjunto de ejemplo para aprender, **no una herramienta médica**.
- Lo que queremos detectar: `y = 1` es **maligno**, `y = 0` es benigno.

## Paso a paso

1. **Carga y cuenta.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_validate, cross_val_predict
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

datos = load_breast_cancer(as_frame=True)
X = datos.data
y = (datos.target == 0).astype(int)          # 1 = maligno (lo que hay que detectar)
print(X.shape, "· malignos:", y.sum(), "· benignos:", (y == 0).sum())
X.iloc[:, :6].describe().round(1)
```

2. **Separa.** El examen (`test`) no se mira hasta el final.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(len(X_train), "para entrenar ·", len(X_test), "para el examen (NO mirar)")
```

3. **El duelo (solo con `train`).** Mirad dos números: lo que **acierta** y cuántos malignos **detecta** (recall).

```python
modelos = {
    "Todos benignos (tonto)": DummyClassifier(strategy="prior"),
    "Logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "Árbol (profundidad 3)": DecisionTreeClassifier(max_depth=3, random_state=42),
    "Bosque": RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=2),
    "Boosting": HistGradientBoostingClassifier(random_state=42),
    "SVM": make_pipeline(StandardScaler(), SVC(probability=True, random_state=42)),
}
filas = {}
for n, m in modelos.items():
    r = cross_validate(m, X_train, y_train, cv=5, scoring=["accuracy", "recall"])
    filas[n] = {"acierta": r["test_accuracy"].mean(), "detecta malignos (recall)": r["test_recall"].mean()}
pd.DataFrame(filas).T.round(3)
```

4. **Mira por dentro.** Un árbol pequeño se lee como preguntas; el bosque dice qué medidas pesan más.

```python
arbol = modelos["Árbol (profundidad 3)"].fit(X_train, y_train)
plt.figure(figsize=(12, 5))
plot_tree(arbol, feature_names=list(X.columns), class_names=["benigno", "maligno"], filled=True, fontsize=8)
plt.show()

bosque = modelos["Bosque"].fit(X_train, y_train)
pd.Series(bosque.feature_importances_, index=X.columns).nlargest(8).sort_values().plot.barh(title="Medidas que más pesan")
plt.show()
```

5. **Elige el umbral con el coste.** Perder un maligno (FN) es mucho peor que una falsa alarma (FP). Probad umbrales con las probabilidades de `train` y quedaos con el que **detecte casi todos**.

```python
campeon = modelos["Logística"]                # cambia por el tuyo (con predict_proba)
proba_cv = cross_val_predict(campeon, X_train, y_train, cv=5, method="predict_proba")[:, 1]
for u in [0.5, 0.3, 0.2, 0.1]:
    vn, fp, fn, vp = confusion_matrix(y_train, proba_cv >= u).ravel()
    print(f"umbral {u}: malignos que se escapan (FN) {fn} · falsas alarmas (FP) {fp}")
UMBRAL = 0.2                                  # ← vuestra decisión, con su razón
```

6. **El examen: UNA vez.**

```python
campeon.fit(X_train, y_train)
proba = campeon.predict_proba(X_test)[:, 1]
pred = (proba >= UMBRAL).astype(int)
vn, fp, fn, vp = confusion_matrix(y_test, pred).ravel()
print(f"Malignos detectados: {vp} de {vp + fn} · se escapan: {fn} · falsas alarmas: {fp}")
ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=["benigno", "maligno"], cmap="Blues", colorbar=False)
plt.show()
```

## Tu app
- Una ficha por paciente: probabilidad de que sea maligno y qué era en realidad.

```python
def paciente(i):
    p = proba[i]
    real = "maligno" if y_test.iloc[i] == 1 else "benigno"
    aviso = "REVISAR" if p >= UMBRAL else "sin aviso"
    return f"Paciente {i}: probabilidad de maligno {p:.2f} → {aviso} · en realidad: {real}"

for i in range(6):
    print(paciente(i))
```

## Qué deberías ver
- **569 pacientes**: 212 malignos y 357 benignos.
- Duelo (acierto / detecta malignos): tonto **0,63 / 0** · logística ≈ 0,97 / 0,95 · SVM ≈ **0,97 / 0,95** · bosque ≈ 0,96 / 0,94 · boosting ≈ 0,96 / 0,92 · árbol ≈ 0,93 / 0,88.
- Umbral (con `train`): con 0,5 se escapan **9** malignos y hay 4 falsas alarmas; con 0,2, se escapan **3** y hay 15; con 0,1, se escapa 1 y hay 28.
- Examen con umbral 0,2: **41 de 42 malignos detectados**, 1 se escapa y 4 falsas alarmas.
- El árbol se lee como preguntas: la primera es por el **perímetro** de las células (`worst perimeter`), y luego por su forma (`worst concave points`) y su tamaño (`mean area`). El bosque da más peso a `worst perimeter`, `worst area` y `worst concave points`.
- Tus cifras pueden diferir en el último decimal.

## Extra 🔴
- Cambia el `UMBRAL` a 0,5 y a 0,05 y mira cómo se mueven FN y FP. ¿Cuál elegiría un hospital?
- Entrena con solo **2 medidas** (por ejemplo `worst radius` y `worst concave points`): ¿cuánto pierdes?
- Busca los pacientes que **se escapan** y mira si se parecen a los benignos.

## Cuidado
- **Esto no diagnostica nada.** Son datos de ejemplo para aprender. Una IA así solo sería un **apoyo** para que una persona experta mire antes un caso.
- Un recall alto sale a costa de falsas alarmas: personas asustadas y pruebas de más. Hay que **decidir con el médico**, no solo con el modelo.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

- **Extra 1 · Umbral 0,5 y 0,05 (examen, logística):**
  - **0,5:** **3 malignos se escapan**, 1 falsa alarma.
  - **0,2:** se escapa **1**, 4 falsas alarmas (el de la ficha).
  - **0,05:** **0 se escapan**, 11 falsas alarmas (en `train` con validación cruzada: 1 se escapa y 49 falsas alarmas).
  - Un hospital **no elegiría 0,5**: no detectar un maligno es peor que repetir una prueba. Pero **bajar sin límite** llena la consulta de falsas alarmas. Se **decide con el médico**.
- **Extra 2 · Solo `worst radius` y `worst concave points`:** acierto **0,949** y detecta **0,918** (con todas las medidas: ≈ 0,97 / 0,95). **Pierdes ≈ 2–3 puntos** a cambio de un modelo que se explica con **dos números**.
- **Extra 3 · El maligno que se escapa:** se le asigna **0,06** de probabilidad. Sus medidas (`worst radius` 16,6; `worst concave points` 0,14) están **entre las de benignos (13,3 / 0,07) y malignos (20,5 / 0,18)**: **se parece a los benignos**. Un modelo **no puede ver lo que los datos no distinguen**.
- **Para comentar:** «no diagnostica nada»: una persona experta mira antes un caso. Subrayar **recall alto = más falsas alarmas = gente asustada**.
- **Tarjeta de ejemplo:**
  - Mi app decide **qué pacientes revisar primero** a partir de **30 medidas de las células**.
  - Antes de modelar tuve que **escoger el umbral (0,2) pensando en que un maligno que se escapa es peor que una falsa alarma**.
  - Detecta **41 de 42 malignos** en el examen, frente a **0** del modelo tonto.
  - No debe usarse para **diagnosticar**: solo como apoyo a una persona experta.
