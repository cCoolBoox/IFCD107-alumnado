# 🩺 Miniapp 4 · ¿Riesgo de diabetes?

⭐⭐ · 50 min · **clasificación** · practica S06 (datos que faltan, `Pipeline`), S07 (ROC, umbral) y S08 (comparar modelos)

## Qué construyes
- Un **cribado**: con glucosa, IMC, edad y poco más, estima la probabilidad de que una persona tenga diabetes.
- Descubres algo habitual: **el modelo más sencillo puede ganar** al más complicado.

## Datos
- `diabetes_pima.csv`: 768 mujeres de un estudio real de EE. UU. (Pima, dominio público). Es un conjunto de ejemplo para aprender, **no una herramienta médica**.
- Objetivo: `diabetes` (1 = sí, 0 = no). Ojo: en `glucosa`, `presion`, `pliegue_piel`, `insulina` e `imc` hay **ceros imposibles** (nadie tiene glucosa 0): son datos que faltan.

## Paso a paso

1. **Carga y arregla los ceros.** Un cero imposible es un dato que falta (`NaN`).

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate, cross_val_predict
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/diabetes_pima.csv"
df = pd.read_csv(URL)
for col in ["glucosa", "presion", "pliegue_piel", "insulina", "imc"]:
    df[col] = df[col].replace(0, np.nan)
print("Con diabetes:", round(df["diabetes"].mean(), 2))
print(df.isna().sum())
```

2. **Dibuja una pista.** ¿La glucosa separa a los dos grupos?

```python
df.groupby("diabetes")["glucosa"].plot.hist(alpha=0.5, bins=20, legend=True)
plt.xlabel("glucosa"); plt.title("0 = sin diabetes · 1 = con diabetes"); plt.show()
```

3. **Separa.** El examen (`test`) no se mira hasta el final.

```python
X, y = df.drop(columns="diabetes"), df["diabetes"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(len(X_train), "para entrenar ·", len(X_test), "para el examen (NO mirar)")
```

4. **El duelo (solo con `train`).** Cada modelo lleva dentro el relleno de los datos que faltan (mediana): así no hay fuga de datos.

```python
rellenar = lambda: SimpleImputer(strategy="median")
modelos = {
    "Nadie tiene diabetes (tonto)": DummyClassifier(strategy="prior"),
    "Logística": make_pipeline(rellenar(), StandardScaler(), LogisticRegression(max_iter=1000)),
    "Árbol (profundidad 3)": make_pipeline(rellenar(), DecisionTreeClassifier(max_depth=3, random_state=42)),
    "Bosque": make_pipeline(rellenar(), RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=42, n_jobs=2)),
    "Boosting": make_pipeline(rellenar(), HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, random_state=42)),
    "SVM": make_pipeline(rellenar(), StandardScaler(), SVC(probability=True, random_state=42)),
}
filas = {}
for n, m in modelos.items():
    r = cross_validate(m, X_train, y_train, cv=5, scoring=["roc_auc", "accuracy"])
    filas[n] = {"AUC": r["test_roc_auc"].mean(), "desviación": r["test_roc_auc"].std(), "acierta": r["test_accuracy"].mean()}
pd.DataFrame(filas).T.round(3).sort_values("AUC", ascending=False)
```

5. **Curvas ROC** de los tres mejores (con predicciones de `train`).

```python
for n in ["Logística", "Bosque", "Boosting"]:
    p = cross_val_predict(modelos[n], X_train, y_train, cv=5, method="predict_proba")[:, 1]
    fpr, tpr, _ = roc_curve(y_train, p)
    plt.plot(fpr, tpr, label=f"{n} (AUC {roc_auc_score(y_train, p):.2f})")
plt.plot([0, 1], [0, 1], "--", color="gray", label="azar")
plt.xlabel("falsas alarmas"); plt.ylabel("casos detectados"); plt.legend(); plt.show()
```

6. **Elige el umbral.** En un cribado conviene **no dejar escapar casos**: se acepta avisar a algunas personas sanas. Mira qué pasa con cada umbral (con `train`).

```python
campeon = modelos["Logística"]                 # cambia por el tuyo
proba_cv = cross_val_predict(campeon, X_train, y_train, cv=5, method="predict_proba")[:, 1]
for u in [0.5, 0.4, 0.3, 0.2]:
    vn, fp, fn, vp = confusion_matrix(y_train, proba_cv >= u).ravel()
    print(f"umbral {u}: detecta {vp / (vp + fn):.2f} de los casos · de sus avisos acierta {vp / (vp + fp):.2f}")
UMBRAL = 0.3                                   # ← vuestra decisión, con su razón
```

7. **El examen: UNA vez.**

```python
campeon.fit(X_train, y_train)
proba = campeon.predict_proba(X_test)[:, 1]
pred = (proba >= UMBRAL).astype(int)
vn, fp, fn, vp = confusion_matrix(y_test, pred).ravel()
print(f"AUC en el examen: {roc_auc_score(y_test, proba):.3f} · casos detectados: {vp} de {vp + fn} · falsas alarmas: {fp}")
ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=["sin diabetes", "con diabetes"], cmap="Blues", colorbar=False)
plt.show()
```

## Tu app
- Rellena solo lo que sepas: lo que falte lo completa el modelo con la mediana.

```python
def riesgo(glucosa=np.nan, imc=np.nan, edad=40, embarazos=1, presion=np.nan, pliegue_piel=np.nan, insulina=np.nan, pedigri=0.4):
    fila = pd.DataFrame([dict(embarazos=embarazos, glucosa=glucosa, presion=presion, pliegue_piel=pliegue_piel,
                              insulina=insulina, imc=imc, pedigri=pedigri, edad=edad)])
    p = campeon.predict_proba(fila[X.columns])[0, 1]
    return f"Probabilidad estimada: {p:.2f} → {'conviene una prueba de glucosa' if p >= UMBRAL else 'riesgo bajo en este modelo'}"

print(riesgo(glucosa=95, imc=22, edad=25))
print(riesgo(glucosa=165, imc=36, edad=52))
```

```python
# (solo Colab) deslizadores
from ipywidgets import interact
interact(riesgo, glucosa=(60, 200), imc=(18.0, 55.0), edad=(21, 80), embarazos=(0, 12));
```

## Qué deberías ver
- **35 % con diabetes** y datos que faltan: `insulina` 374, `pliegue_piel` 227, `presion` 35, `imc` 11 y `glucosa` 5.
- Duelo (AUC): **Logística ≈ 0,84** · Bosque ≈ 0,84 · Boosting ≈ 0,83 · SVM ≈ 0,83 · Árbol ≈ 0,75 · tonto 0,50. **La logística gana** (o empata) y es la más fácil de explicar.
- Umbral (con `train`): con 0,3 detecta ≈ **78 %** de los casos y acierta en ≈ 59 % de sus avisos; con 0,2 detecta ≈ 87 % y acierta en ≈ 52 %.
- Examen (umbral 0,3): **AUC ≈ 0,81**; detecta 43 de 54 casos y da 29 falsas alarmas.
- La app: ≈ 0,03 (glucosa 95, 25 años) y ≈ 0,74 (glucosa 165, IMC 36, 52 años).
- Tus cifras pueden diferir en el último decimal.

## Extra 🔴
- Prueba **quitar** `insulina` y `pliegue_piel` (las que más faltan): ¿empeora algo?
- Cambia el relleno de la mediana a la **media**, o a un valor distinto: ¿cambia el AUC?
- Compara los resultados por **tramos de edad**: ¿el modelo falla más en algún grupo?

## Cuidado
- **No es un diagnóstico.** Son datos de ejemplo de un solo grupo de mujeres: no sirven para otras personas.
- Una prueba de glucosa de verdad vale más que cualquier modelo. Esta IA solo ayudaría a **decidir a quién proponérsela primero**.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

- **Extra 1 · Quitar `insulina` y `pliegue_piel`:** AUC **0,842** frente a **0,843**: **no empeora nada**, a pesar de ser las que más faltan (374 y 227 huecos). Se pueden **descartar** y simplificar la toma de datos.
- **Extra 2 · Relleno con la media:** **0,843** (igual). Con **0 como relleno** baja a **0,832**: meter un valor **imposible** (insulina 0) distorsiona. Moraleja: **el valor de relleno debe ser verosímil**.
- **Extra 3 · Por edad (examen, 154 mujeres, umbral 0,3):**
  - **Menores de 30:** 16 casos, **detecta 9** (56 %), 14 falsas alarmas.
  - **30 a 44:** 26 casos, detecta **22** (85 %), 6 falsas alarmas.
  - **45 o más:** 12 casos, detecta **12** (100 %), 9 falsas alarmas.
  - Lectura: **detecta peor en menores de 30** (9 de 16). Con 16 casos **no se puede concluir por qué**: es una pista para mirar más datos, no una conclusión.
- **Para comentar:** la **logística gana o empata** y es la que mejor se explica. Una prueba de glucosa **vale más** que cualquier modelo: esta IA solo decide **a quién proponérsela primero**.
- **Tarjeta de ejemplo:**
  - Mi app decide **a quién proponer una prueba de glucosa** a partir de **glucosa, IMC, edad y embarazos**.
  - Antes de modelar tuve que **tratar los 0 como datos que faltan y rellenarlos con la mediana dentro del `Pipeline`**.
  - Acierta **AUC ≈ 0,81** en el examen (43 de 54 casos detectados), frente a **0,50** del modelo tonto.
  - No debe usarse para **diagnosticar ni para otras personas**: datos de un solo grupo de mujeres.
