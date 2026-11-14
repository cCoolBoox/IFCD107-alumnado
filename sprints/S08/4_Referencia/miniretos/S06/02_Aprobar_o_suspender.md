# 🎓 Miniapp 2 · ¿Aprobará este estudiante?

⭐⭐ · 50 min · **datos reales y fuga de datos** · practica S06 (`ColumnTransformer`, `Pipeline`, fuga, baseline, validación cruzada)

## Qué construyes
- Un modelo que **predice si un estudiante aprobará matemáticas** al final del curso.
- Descubres la **fuga de datos** de la forma más sutil: una columna que parece inocente y **hace trampa**.

## Datos
- `estudiantes_mates.csv`: 395 estudiantes de dos colegios de Portugal (UCI, datos reales). Viene separado por `;`.
- `G1`, `G2` y `G3` son las notas de la 1.ª evaluación, la 2.ª y la final (de 0 a 20). **Aprobar = `G3` ≥ 10.**
- También hay familia, tiempo de estudio, faltas (`absences`), asignaturas suspensas antes (`failures`)…

## Paso a paso

1. **Carga y crea el objetivo.** ¿Cuántos aprueban?

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/estudiantes_mates.csv"
df = pd.read_csv(URL, sep=";")
df["aprobado"] = (df["G3"] >= 10).astype(int)
print(df.shape, "· aprueban:", round(df["aprobado"].mean(), 2))
print(df[["G1", "G2", "G3", "failures", "absences", "studytime"]].corr()["G3"].round(2))
```

2. **Dibuja la sospecha.** ¿Cuánto se parece `G2` a la nota final?

```python
plt.scatter(df["G2"], df["G3"], alpha=0.4)
plt.xlabel("nota de la 2.ª evaluación (G2)"); plt.ylabel("nota final (G3)"); plt.show()
```

3. **Prepara el `Pipeline` con una función**, para poder probar distintos conjuntos de variables. Las categorías pasan a 0 y 1 y los números se escalan; todo dentro, sin fuga.

```python
def construir(columnas, modelo):
    num = [c for c in columnas if df[c].dtype != "object"]
    cat = [c for c in columnas if df[c].dtype == "object"]
    prep = ColumnTransformer([("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), num),
                              ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    return Pipeline([("prep", prep), ("modelo", modelo)])

todas = [c for c in df.columns if c not in ("G3", "aprobado")]
sin_notas = [c for c in todas if c not in ("G1", "G2")]
y = df["aprobado"]
train_idx, test_idx = train_test_split(df.index, test_size=0.2, random_state=42, stratify=y)
print(len(train_idx), "para entrenar ·", len(test_idx), "para el examen (NO mirar)")
```

4. **Tres planes para predecir.** Mismo modelo, distintas variables: ¿cuándo se haría la predicción?

```python
planes = {"Solo con el modelo tonto": (sin_notas, DummyClassifier(strategy="prior")),
          "Al empezar el curso (sin notas)": (sin_notas, LogisticRegression(max_iter=1000)),
          "Con la 1.ª nota (G1)": ([c for c in todas if c != "G2"], LogisticRegression(max_iter=1000)),
          "Con G1 y G2": (todas, LogisticRegression(max_iter=1000))}
for nombre, (cols, modelo) in planes.items():
    auc = cross_val_score(construir(cols, modelo), df.loc[train_idx, cols], y[train_idx], cv=5, scoring="roc_auc").mean()
    print(f"{nombre:34s} AUC {auc:.3f}")
```

5. **Compara modelos con el plan que elijas** (por ejemplo, «Con la 1.ª nota»).

```python
cols = [c for c in todas if c != "G2"]
modelos = {"Logística": LogisticRegression(max_iter=1000),
           "Bosque": RandomForestClassifier(n_estimators=300, min_samples_leaf=3, random_state=42, n_jobs=2)}
for nombre, m in modelos.items():
    r = cross_val_score(construir(cols, m), df.loc[train_idx, cols], y[train_idx], cv=5, scoring="roc_auc")
    print(f"{nombre:10s} AUC {r.mean():.3f} ± {r.std():.3f}")
```

6. **El examen: UNA vez, con el plan y el modelo elegidos.**

```python
elegido = construir(cols, modelos["Logística"]).fit(df.loc[train_idx, cols], y[train_idx])
from sklearn.metrics import roc_auc_score, confusion_matrix
proba = elegido.predict_proba(df.loc[test_idx, cols])[:, 1]
vn, fp, fn, vp = confusion_matrix(y[test_idx], proba >= 0.5).ravel()
print(f"AUC en el examen: {roc_auc_score(y[test_idx], proba):.3f} · suspensos que avisa bien: {vn} de {vn + fp} · aprobados que da por suspensos: {fn}")
```

## Tu app
- Una función que dice la probabilidad de aprobar de un estudiante del examen. Mira dos casos: uno que acierta y uno que falla.

```python
def prediccion(i):
    fila = df.loc[[test_idx[i]], cols]
    p = elegido.predict_proba(fila)[0, 1]
    return f"Estudiante {test_idx[i]}: probabilidad de aprobar {p:.2f} · G1 = {fila['G1'].iloc[0]} · en realidad: {'aprobó' if y[test_idx[i]] else 'suspendió'}"

for i in range(4):
    print(prediccion(i))
```

## Qué deberías ver
- **395 estudiantes**; aprueba el **67 %**. La correlación con la nota final: `G1` 0,80 · `G2` 0,90.
- AUC con CV en `train`: tonto **0,50** · al empezar el curso, sin notas **0,70** · con `G1` **0,92** · con `G1` y `G2` **0,97**.
- Logística y bosque empatan (**0,916**): con pocos datos, el modelo sencillo basta.
- Examen: **AUC ≈ 0,87**; avisa bien de **17 de 26** suspensos y da por suspensos a **11** aprobados. Con solo 79 estudiantes, la nota oscila bastante: no la presentes con tres decimales.
- La conclusión útil: `G2` sube la nota, pero llega **tarde** para ayudar. Con `G1` ya se puede avisar a tiempo.

## Extra 🔴
- Prueba **quitar** `failures` y `absences`: ¿qué variable pesa más de verdad?
- Mira **por sexo** o por colegio (`school`): ¿el modelo acierta igual en todos los grupos?
- Escribe en 3 líneas **cuándo sería legítimo usar G2** y cuándo sería trampa.

## Cuidado
- **No se pueden tomar decisiones sobre una persona con esto.** Un modelo así solo serviría para ofrecer **apoyo** a quien lo necesite, nunca para etiquetar a nadie.
- 395 estudiantes de dos colegios no representan a todos.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**. 🗣️ = respuesta de redacción u opinión: no hay cifra única.

- **Extra 1 · Quitar `failures` y `absences`:** AUC con CV **0,912** (sin ambas) · 0,912 (sin `failures`) · 0,915 (sin `absences`), frente a **0,916**. **Casi nada cambia:** quien manda es **G1** (coeficiente ≈ 3,4; el siguiente no pasa de 0,9).
  - Pista de interpretación: el peso de una variable en un modelo **no es causa**.
- **Extra 2 · Por sexo / colegio (examen de 79):**
  - Sexo F (47): acierto 0,72 · AUC 0,86 · suspensos avisados **11 de 17**.
  - Sexo M (32): acierto 0,78 · AUC 0,88 · suspensos avisados **6 de 9**.
  - Colegio GP (71): AUC 0,86; MS (8): AUC 1,0 (solo 8 estudiantes: **no vale**).
  - Conclusión: **parecido** entre sexos; con 79 estudiantes **no se puede afirmar nada fino**. Lo importante es que **lo miren**.
- **Extra 3 · ¿Cuándo es legítimo usar G2? (redacción 🗣️).** Respuesta modelo:
  - **Legítimo:** cuando el aviso se emite **después de G2** y sirve para **ofrecer apoyo antes del examen final**, y si G2 estará disponible **también en producción**.
  - **Trampa:** usar G2 para «predecir» G3 y presumir de nota, o para una decisión que ocurre **antes** de G2 (no lo tendrás).
  - **Línea roja:** nunca para **etiquetar o decidir sobre una persona**.
- **Para comentar:** AUC 0,70 (sin notas) → 0,92 (con G1) → 0,97 (con G2). Cada nota **sube la cifra, pero llega más tarde**. «Mejor modelo» ≠ «modelo útil».
- **Tarjeta de ejemplo:**
  - Mi app decide **a quién ofrecer apoyo** a partir de **la 1.ª nota y datos del curso**.
  - Antes de modelar tuve que **separar `G2`, que llega tarde, y preparar números y texto con un `ColumnTransformer`**.
  - Acierta **AUC ≈ 0,87** en el examen, frente a **0,50** del modelo tonto.
  - No debe usarse para **decidir sobre una persona**: solo para ofrecer apoyo.
