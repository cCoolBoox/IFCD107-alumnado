# 🚑 Miniapp 9 · ¿Este paciente es urgente?

⭐⭐⭐ · 55 min · **explicable frente a potente** · practica S07 (umbral, recall, matriz de confusión) y S08 (árbol, bosque, boosting, elegir campeón)

## Qué construyes
- Una **ayuda para ordenar la sala de espera** de urgencias: con los signos vitales del paciente, dice cuánto se parece a un caso urgente.
- Te enfrentas a una decisión real: ¿un modelo **que se pueda explicar a una enfermera** o uno **más potente pero opaco**?

## Datos
- `triaje_urgencias.csv`: 4 000 pacientes **inventados**, con un **13 % de casos urgentes**. Columnas: edad, frecuencia cardiaca, tensión, saturación de oxígeno, temperatura, dolor (0–10), dolor de pecho, dificultad para respirar y si llega en ambulancia.
- Objetivo: `urgente` (1 = necesitó atención inmediata).
- Es un ejercicio de aprendizaje: **ninguna app de estas decide quién se atiende primero**.

## Paso a paso

1. **Carga y compara.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate, cross_val_predict, StratifiedKFold
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import precision_recall_curve, confusion_matrix, roc_auc_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/triaje_urgencias.csv"
df = pd.read_csv(URL)
print(df.shape, "· urgentes:", int(df["urgente"].sum()), f"({df['urgente'].mean():.1%})")
df.groupby("urgente").mean().round(1).T
```

2. **Separa.**

```python
y = df["urgente"]; X = df.drop(columns="urgente")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
cv = StratifiedKFold(5, shuffle=True, random_state=42)
print(len(X_tr), "para entrenar ·", len(X_te), "para el examen (NO mirar)")
```

3. **El duelo.** Fíjate en el árbol pequeño (explicable) frente al bosque y al boosting (potentes).

```python
modelos = {"Nadie es urgente (tonto)": DummyClassifier(strategy="prior"),
           "Logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
           "Árbol explicable (profundidad 4)": DecisionTreeClassifier(max_depth=4, min_samples_leaf=20, random_state=42),
           "Bosque": RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=42, n_jobs=2),
           "Boosting": HistGradientBoostingClassifier(random_state=42)}
filas = {}
for nombre, m in modelos.items():
    r = cross_validate(m, X_tr, y_tr, cv=cv, scoring=["accuracy", "roc_auc", "average_precision"])
    filas[nombre] = {"precisión global": r["test_accuracy"].mean(), "AUC": r["test_roc_auc"].mean(), "AP": r["test_average_precision"].mean()}
pd.DataFrame(filas).T.round(3)
```

4. **El árbol, en palabras.** Esto sí se le puede explicar a una enfermera.

```python
arbol = DecisionTreeClassifier(max_depth=4, min_samples_leaf=20, random_state=42).fit(X_tr, y_tr)
print(export_text(arbol, feature_names=list(X.columns), max_depth=4))
```

5. **El umbral que piensa en la seguridad.** Se escapa un urgente = muy grave. Exigimos **detectar al 90 %** de los urgentes y miramos **cuántas falsas alarmas cuesta** cada modelo.

```python
def umbral_para_recall(modelo, recall_objetivo=0.90):
    proba = cross_val_predict(modelo, X_tr, y_tr, cv=cv, method="predict_proba")[:, 1]
    precision, recall, umbrales = precision_recall_curve(y_tr, proba)
    i = np.where(recall[:-1] >= recall_objetivo)[0][-1]
    return float(umbrales[i]), float(precision[i])

for nombre in ["Árbol explicable (profundidad 4)", "Bosque", "Boosting"]:
    u, prec = umbral_para_recall(modelos[nombre])
    print(f"{nombre:34s} umbral {u:.2f} · de cada 100 avisos, {prec * 100:.0f} son urgentes de verdad")
```

6. **El examen: una vez, con el campeón y su umbral.** Elige tú el campeón mirando las dos tablas (nota general y falsas alarmas).

```python
campeon_nombre = "Bosque"                       # cámbialo si tu tabla dice otra cosa
campeon = modelos[campeon_nombre]
umbral, _ = umbral_para_recall(campeon)
final = campeon.fit(X_tr, y_tr)
proba = final.predict_proba(X_te)[:, 1]
aviso = proba >= umbral
vn, fp, fn, vp = confusion_matrix(y_te, aviso).ravel()
print(f"{campeon_nombre}: urgentes detectados {vp} de {vp + fn} · falsas alarmas {fp} de {vn + fp} no urgentes · AUC {roc_auc_score(y_te, proba):.3f}")
```

7. **¿Falla más con unos pacientes que con otros?** Compara a los mayores de 65 años con el resto.

```python
mayores = X_te["edad"].values >= 65
for nombre, grupo in [("65 años o más", mayores), ("menores de 65", ~mayores)]:
    urgentes = (y_te.values == 1) & grupo
    print(f"{nombre:15s} → urgentes detectados: {int((aviso & urgentes).sum())} de {int(urgentes.sum())} ({(aviso & urgentes).sum() / max(urgentes.sum(), 1):.0%})")
```

## Tu app
- Una función que ordena **una lista de pacientes** de más a menos prioridad.

```python
def prioridad(pacientes):
    tabla = pd.DataFrame(pacientes)[X.columns]
    tabla["prob_urgente"] = final.predict_proba(tabla)[:, 1].round(2)
    tabla["aviso"] = np.where(tabla["prob_urgente"] >= umbral, "🚨 prioridad", "en cola")
    return tabla.sort_values("prob_urgente", ascending=False)

sala = [dict(edad=70, frecuencia_cardiaca=118, tension_sistolica=95, saturacion_o2=89, temperatura_c=38.5, dolor_0_10=6, dolor_pecho=1, dificultad_respirar=1, llega_en_ambulancia=1),
        dict(edad=25, frecuencia_cardiaca=78, tension_sistolica=118, saturacion_o2=99, temperatura_c=36.6, dolor_0_10=2, dolor_pecho=0, dificultad_respirar=0, llega_en_ambulancia=0),
        dict(edad=52, frecuencia_cardiaca=95, tension_sistolica=130, saturacion_o2=95, temperatura_c=37.0, dolor_0_10=5, dolor_pecho=0, dificultad_respirar=0, llega_en_ambulancia=0)]
prioridad(sala)
```

## Qué deberías ver
- **4 000 pacientes, 13 % urgentes**. Los urgentes tienen más dolor (≈ 4,8 frente a 3,2), pulso más alto (≈ 92 frente a 85), menos saturación (≈ 95,6 % frente a 96,6 %) y más dificultad para respirar.
- Tabla con CV: «nadie es urgente» **86,8 %** (AUC 0,50) · logística AUC 0,78 · **árbol explicable AUC 0,80 · AP 0,47** · **bosque AUC 0,87 · AP 0,64** · boosting AUC 0,85 · AP 0,61.
- El árbol de profundidad 4 se lee en voz alta: *«dolor ≤ 6,5, pulso ≤ 110, saturación ≤ 93,5 y dificultad para respirar → urgente»*.
- Exigiendo **recall del 90 %**: de cada 100 avisos, **15** son urgentes de verdad con el árbol, **24** con el bosque y **22** con el boosting. El potente cuesta menos falsas alarmas, pero **no se puede explicar**: esa es la decisión.
- Examen con el bosque: detectas **119 de 132** urgentes, pero con **364 falsas alarmas** de 868 no urgentes. AUC ≈ 0,89.
- Por edad: **65 o más, 41 de 43 (95 %)**; **menores de 65, 78 de 89 (88 %)**. Con grupos tan pequeños, la diferencia es orientativa, pero hay que mirarla.
- App: el paciente de 70 años con poca saturación y dolor de pecho ≈ **0,80 → prioridad**; el de 52 años con dolor moderado ≈ 0,02; el joven sano ≈ 0,01.

## Extra 🔴
- Baja el objetivo a un **recall del 80 %** y súbelo al **95 %**: ¿cuántas falsas alarmas más cuesta cada paso?
- Mira el recall en **más grupos** (por ejemplo, quien llega en ambulancia y quien no).
- Escribe qué le dirías a una enfermera para que **se fíe del aviso… sin dejar de mirar al paciente**.

## Cuidado
- Esto **no es una herramienta médica**. En urgencias real, una persona decide siempre.
- Un modelo opaco, aunque acierte más, es difícil de **explicar y de auditar**: pregúntate si el pequeño empujón de nota lo compensa.
- Los datos son **inventados**.
