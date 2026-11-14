# 🌸 Miniapp 6 · El zoo de fronteras

⭐ · 40 min · **clasificación visual** · practica S08 (árbol, bosque, SVM, k-NN) · ideal para empezar

## Qué construyes
- Un clasificador de **flores** (iris) y un **mapa** de cómo decide cada modelo.
- Ves que **un árbol corta en rectángulos, la SVM puede dibujar curvas y el bosque junta muchos rectángulos**. Es la forma más rápida de entender los modelos del sprint.

## Datos
- Vienen **dentro de scikit-learn**: 150 flores de 3 especies (`setosa`, `versicolor`, `virginica`). Usamos solo **2 medidas** del pétalo (largo y ancho) para poder dibujar.

## Paso a paso

1. **Carga y dibuja las flores.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay

iris = load_iris(as_frame=True)
X = iris.data[["petal length (cm)", "petal width (cm)"]]
y = iris.target
nombres = list(iris.target_names)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap="viridis", edgecolor="k")
plt.xlabel("largo del pétalo (cm)"); plt.ylabel("ancho del pétalo (cm)"); plt.title(" · ".join(nombres)); plt.show()
```

2. **Separa.** El examen (`test`) no se mira hasta el final.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print(len(y_train), "para entrenar ·", len(y_test), "para el examen (NO mirar)")
```

3. **El zoo.** Siete modelos, y para cada uno su mapa de decisión y su acierto con validación cruzada (solo `train`).

```python
zoo = {
    "Logística": LogisticRegression(max_iter=1000),
    "Árbol (profundidad 2)": DecisionTreeClassifier(max_depth=2, random_state=42),
    "Árbol sin límite": DecisionTreeClassifier(random_state=42),
    "k-NN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "SVM lineal": SVC(kernel="linear"),
    "SVM curva (RBF)": SVC(kernel="rbf", gamma=2, C=1),
    "Bosque": RandomForestClassifier(n_estimators=100, random_state=42),
}
fig, ejes = plt.subplots(2, 4, figsize=(16, 7))
for ax, (nombre, modelo) in zip(ejes.ravel(), zoo.items()):
    modelo.fit(X_train, y_train)
    DecisionBoundaryDisplay.from_estimator(modelo, X_train, ax=ax, response_method="predict", cmap="viridis", alpha=0.35, grid_resolution=300)
    ax.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, cmap="viridis", edgecolor="k", s=25)
    acierto = cross_val_score(modelo, X_train, y_train, cv=5).mean()
    ax.set_title(f"{nombre}\nacierto {acierto:.2f}", fontsize=10); ax.set_xlabel(""); ax.set_ylabel("")
ejes.ravel()[-1].axis("off")
plt.tight_layout(); plt.show()
```

4. **Fíjate y contesta** (en la hoja del equipo):
   - ¿Qué modelos dibujan **rectas**? ¿Cuáles **rectángulos**? ¿Cuáles **curvas**?
   - Compara el **árbol de profundidad 2** con el **árbol sin límite** y con el **bosque**: ¿en qué cambian los rectángulos? ¿Qué te recuerda a S08_01 y S08_02?
   - ¿Por qué el acierto de todos es parecido, si los mapas son tan distintos?

5. **El examen: UNA vez, con el campeón** (cambia `campeon` por el tuyo).

```python
campeon = zoo["SVM curva (RBF)"]
pred = campeon.predict(X_test)
print(f"Acierta {(pred == y_test).mean():.3f} · se equivoca en {(pred != y_test).sum()} de {len(y_test)} flores")
```

## Tu app
- Una función que dice la especie de una flor a partir de su pétalo.

```python
def flor(largo, ancho):
    fila = pd.DataFrame([[largo, ancho]], columns=X.columns)
    return nombres[int(campeon.predict(fila)[0])]

print(flor(1.5, 0.2), "·", flor(4.5, 1.4), "·", flor(6.0, 2.1))
```

```python
# (solo Colab) deslizadores
from ipywidgets import interact
interact(flor, largo=(1.0, 7.0, 0.1), ancho=(0.1, 2.5, 0.1));
```

## Qué deberías ver
- Un mapa de **7 modelos**: la logística y la SVM lineal, con **rectas**; los árboles y el bosque, con **rectángulos**; la SVM RBF y k-NN, con **curvas**.
- Acierto con validación cruzada: casi igual en todos (≈ **0,95 a 0,97**).
- Examen con la SVM curva: ≈ **0,93** (3 errores de 45 flores).
- La app: `setosa` · `versicolor` · `virginica` para los tres ejemplos.
- Tus cifras pueden diferir en el último decimal.

## Extra 🔴
- Cambia `gamma` de la SVM a 0,5, 2 y 50: ¿cuándo empieza a **memorizar**?
- Cambia `max_depth` del árbol de 1 a 6: ¿cuántos «rectángulos» salen en cada caso?
- Vuelve a probar con **las 4 medidas** en vez de 2 (no se puede dibujar): ¿mejora el acierto?

## Cuidado
- Con 150 flores y 2 medidas, **todos los modelos aciertan casi lo mismo**: la diferencia es **cómo** deciden. Con datos más difíciles (como en las otras miniapps), sí hay un campeón claro.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

- **Extra 1 · `gamma` de la SVM:** **0,5 y 2 → CV 0,971 / examen 0,933**; **50 → CV 0,886 / examen 0,867** (con 0,981 en `train`). A **50 empieza a memorizar**: sube en `train` y baja en validación y examen.
- **Extra 2 · `max_depth`:** profundidad **1 → 2 rectángulos (CV 0,667)**; **2 → 3 (0,952)**; 3 → 5; 4 → 6; 5 y 6 → 7 (todos con CV 0,952). **A partir de profundidad 2 no mejora**: más rectángulos solo complican.
- **Extra 3 · Las 4 medidas:** SVM con CV **0,971**, igual que con 2 medidas: **no mejora**, pero **no se puede dibujar**. Con 2 medidas ya hay casi todo lo que hace falta.
- **Para comentar:** «todos aciertan casi lo mismo, lo que cambia es **cómo** deciden»: rectas, rectángulos o curvas. Es la ficha ideal para empezar.
- **Tarjeta de ejemplo:**
  - Mi app decide **la especie de la flor** a partir de **largo y ancho del pétalo**.
  - Antes de modelar tuve que **dibujar la frontera de cada modelo para ver cómo decide**.
  - Acierta **≈ 0,93** en el examen (3 errores de 45 flores), frente a **0,33** del modelo tonto.
  - No debe usarse para **otras plantas**: son 150 flores de tres especies.
