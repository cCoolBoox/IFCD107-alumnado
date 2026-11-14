# 🎮 Miniapp 7 · ¿Este jugador hace trampas?

⭐⭐ · 50 min · **clasificación con umbral exigente** · practica S07 (umbral, precisión frente a recall) y S08 (árbol, bosque, boosting, SVM)

## Qué construyes
- Un **detector de tramposos** para un videojuego de disparos: mira cómo juega alguien (puntería, reflejos, partidas…) y avisa si parece un tramposo.
- Aprendes a decidir **a quién se sanciona**: expulsar a un inocente es mucho peor que dejar pasar a un tramposo.

## Datos
- `tramposos_juego.csv`: 4 000 jugadores **inventados**, con un **6 % de tramposos**. Columnas: % de precisión, % de disparos a la cabeza, tiempo de reacción (ms), ratio de bajas/muertes, horas jugadas, partidas al día, antigüedad de la cuenta y reportes recibidos.
- Objetivo: `tramposo` (1 = hace trampas).

## Paso a paso

1. **Carga y compara a los dos grupos.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate, cross_val_predict, StratifiedKFold
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_curve, confusion_matrix, roc_auc_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/tramposos_juego.csv"
df = pd.read_csv(URL)
print(df.shape, "· tramposos:", int(df["tramposo"].sum()), f"({df['tramposo'].mean():.1%})")
df.groupby("tramposo")[["precision_pct", "headshots_pct", "reaccion_ms", "kd_ratio", "reportes_recibidos"]].mean().round(1)
```

2. **Separa** conservando la proporción de tramposos.

```python
y = df["tramposo"]; X = df.drop(columns="tramposo")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
cv = StratifiedKFold(5, shuffle=True, random_state=42)
print(len(X_tr), "para entrenar ·", len(X_te), "para el examen (NO mirar) · tramposos en el examen:", int(y_te.sum()))
```

3. **El duelo, con validación cruzada.** El modelo tonto dice «nadie hace trampas».

```python
modelos = {"Nadie hace trampas (tonto)": DummyClassifier(strategy="prior"),
           "Logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
           "Árbol (profundidad 5)": DecisionTreeClassifier(max_depth=5, min_samples_leaf=10, random_state=42),
           "Bosque": RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=2),
           "Boosting": HistGradientBoostingClassifier(random_state=42),
           "SVM": make_pipeline(StandardScaler(), SVC(probability=True, random_state=42))}
filas = {}
for nombre, m in modelos.items():
    r = cross_validate(m, X_tr, y_tr, cv=cv, scoring=["accuracy", "roc_auc", "average_precision"])
    filas[nombre] = {"precisión global": r["test_accuracy"].mean(), "AUC": r["test_roc_auc"].mean(), "AP": r["test_average_precision"].mean()}
tabla = pd.DataFrame(filas).T.round(3)
tabla
```

4. **Elige el campeón** por la tabla y fija un **umbral exigente**: solo sancionamos si, de los que avisamos, **al menos el 95 % son de verdad tramposos**.

```python
campeon_nombre = tabla["AP"].idxmax()
campeon = modelos[campeon_nombre]
print("Campeón:", campeon_nombre)

proba_cv = cross_val_predict(campeon, X_tr, y_tr, cv=cv, method="predict_proba")[:, 1]
precision, recall, umbrales = precision_recall_curve(y_tr, proba_cv)
ok = np.where(precision[:-1] >= 0.95)[0]
umbral = float(umbrales[ok[0]]) if len(ok) else 0.5
plt.plot(recall, precision); plt.axhline(0.95, color="red", ls="--")
plt.xlabel("tramposos detectados (recall)"); plt.ylabel("avisos acertados (precisión)"); plt.title("Cuanto más exigentes, menos tramposos cazamos"); plt.show()
print(f"Umbral para sancionar: {umbral:.2f} → recall en validación: {recall[ok[0]] if len(ok) else float('nan'):.2f}")
```

5. **El examen: una vez.**

```python
final = campeon.fit(X_tr, y_tr)
proba = final.predict_proba(X_te)[:, 1]
sancion = proba >= umbral
vn, fp, fn, vp = confusion_matrix(y_te, sancion).ravel()
print(f"Tramposos cazados: {vp} de {vp + fn} · inocentes sancionados por error: {fp} de {vn + fp} · AUC {roc_auc_score(y_te, proba):.3f}")
```

6. **¿En qué se fija?** Mira qué pesa más con un bosque (aunque el campeón sea otro, sirve para entender).

```python
bosque = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=2).fit(X_tr, y_tr)
pd.Series(bosque.feature_importances_, index=X.columns).sort_values().plot(kind="barh", title="Qué mira el bosque"); plt.show()
```

## Tu app
- Una función que valora **un jugador** y dice si se sanciona, se vigila o no pasa nada.

```python
def jugador(precision_pct, headshots_pct, reaccion_ms, kd_ratio, horas_jugadas, partidas_por_dia, antiguedad_cuenta_dias, reportes_recibidos):
    fila = pd.DataFrame([dict(precision_pct=precision_pct, headshots_pct=headshots_pct, reaccion_ms=reaccion_ms, kd_ratio=kd_ratio,
                              horas_jugadas=horas_jugadas, partidas_por_dia=partidas_por_dia,
                              antiguedad_cuenta_dias=antiguedad_cuenta_dias, reportes_recibidos=reportes_recibidos)])[X.columns]
    p = final.predict_proba(fila)[0, 1]
    veredicto = "🚫 sancionar" if p >= umbral else ("👀 vigilar" if p >= umbral / 2 else "✅ normal")
    return f"probabilidad de trampa {p:.0%} → {veredicto}"

print(jugador(35, 22, 240, 1.2, 800, 4, 900, 0))
print(jugador(88, 70, 120, 4.5, 60, 9, 15, 6))
print(jugador(50, 34, 200, 2.2, 600, 6, 200, 2))
```

## Qué deberías ver
- **4 000 jugadores, 235 tramposos (5,9 %)**; el examen tiene 59. Los tramposos disparan más a la cabeza (≈ 30 % frente a ≈ 20 %), reaccionan antes (≈ 232 ms frente a ≈ 259) y reciben más reportes (1,4 frente a 0,5).
- Tabla con CV: «nadie hace trampas» acierta el **94,1 %** (AUC 0,50) · **logística 98,0 % · AUC 0,988 · AP 0,90** · bosque AUC 0,982 · boosting 0,985 · SVM 0,977 · árbol de profundidad 5 **AUC 0,88**.
- **Gana el modelo sencillo**: la logística iguala o supera a bosque y boosting en este problema. Más complejo no siempre es mejor.
- Umbral exigente (precisión ≥ 95 % en validación): **≈ 0,77**, con un recall de ≈ 0,59.
- Examen: cazas **33 de 59** tramposos y sancionas por error a **2 de 941** inocentes. AUC **≈ 0,99**.
- App: el jugador corriente sale **0 % → normal**; el de 88 % de precisión y 120 ms, **100 % → sancionar**; el caso difícil (buen jugador, 600 horas) ≈ **70 % → vigilar**, sin sanción.

## Extra 🔴
- Baja la exigencia a **90 %** y a **99 %**: ¿cuántos tramposos más o menos cazas?
- Quita `reportes_recibidos`: ¿cambia algo? ¿Te fiarías de los reportes de otros jugadores?
- Escribe en 3 líneas **cómo se apelaría** una sanción: ¿qué dato le enseñarías al jugador?

## Cuidado
- Sancionar es una decisión **sobre una persona**: el modelo avisa y **una persona revisa** antes de expulsar.
- Un buen jugador puede parecer tramposo (mucha puntería, muchas horas): mira a quién falla.
- Los datos son **inventados**.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**. 🗣️ = respuesta de redacción u opinión: no hay cifra única.

#### Extra 1 · Exigencia de precisión (examen, 59 tramposos)
- **Qué hacer:**
  1. Define una función que elija el umbral con una precisión mínima y mida el examen. Pruébala con 90 %, 95 % y 99 %.
  2. Apunta tramposos cazados e inocentes sancionados en cada una.
```python
def sancionar(precision_minima, columnas=None):
    columnas = columnas or list(X.columns)
    modelo = modelos[campeon_nombre]
    p_cv = cross_val_predict(modelo, X_tr[columnas], y_tr, cv=cv, method="predict_proba")[:, 1]
    precision, recall, umbrales = precision_recall_curve(y_tr, p_cv)
    u = float(umbrales[np.where(precision[:-1] >= precision_minima)[0][0]])
    p = modelo.fit(X_tr[columnas], y_tr).predict_proba(X_te[columnas])[:, 1]
    vn, fp, fn, vp = confusion_matrix(y_te, p >= u).ravel()
    print(f"precisión ≥ {precision_minima:.0%}: umbral {u:.2f} · cazas {vp} de {vp + fn} · inocentes sancionados {fp}")

for exigencia in (0.90, 0.95, 0.99):
    sancionar(exigencia)
```
- **Qué sale y por qué:**
  - **90 %:** umbral 0,65, caza **38** (4 inocentes sancionados por error).
  - **95 %:** umbral 0,77, caza **33** (2 inocentes).
  - **99 %:** umbral 0,92, caza **24** (1 inocente).
  - Más exigencia = **menos tramposos cazados** y menos errores. Es un **compromiso**, y lo decide la plataforma.

#### Extra 2 · Quitar `reportes_recibidos`
- **Qué hacer:**
  1. Llama a la misma función pasando todas las columnas **menos** `reportes_recibidos`.
  2. Compara cazados y AUC. Después piensa: ¿quién puede inflar los reportes?
```python
from sklearn.model_selection import cross_val_score
sin_reportes = [c for c in X.columns if c != "reportes_recibidos"]
sancionar(0.95, sin_reportes)
for nombre, columnas in (("con reportes", list(X.columns)), ("sin reportes", sin_reportes)):
    auc = cross_val_score(modelos[campeon_nombre], X_tr[columnas], y_tr, cv=cv, scoring="roc_auc").mean()
    print(f"{nombre}: AUC {auc:.3f}")
```
- **Qué sale y por qué:**
  - AUC **0,985** frente a **0,988** y caza **35 de 59** con 2 errores (con reportes: 33). **Casi igual**. ¿Fiarse de los reportes de otros jugadores? **No como prueba**: se pueden **usar en falso** (acoso, «reportes en grupo»). Mejor usarlos como **aviso para revisar**, no para sancionar.

#### Extra 3 · Cómo se apelaría (🗣️)
- **Qué hacer:**
  1. Escribe 3 líneas: **qué dato le enseñarías al jugador** (qué pesó más), **con quién lo compararías** y **quién revisa** antes de expulsar.
  2. Apóyate en el gráfico «Qué mira el bosque» y en la probabilidad que da `jugador(...)`.
- **Qué sale y por qué:**
  - Modelo: *«Se le enseña qué datos tenían más peso (precisión, reacción, reportes), se compara con jugadores de su nivel y una persona revisa partidas concretas. Hasta entonces: nada de expulsión automática.»*

#### Para cerrar
- **Para comentar:** **gana el modelo sencillo** (logística: AUC 0,988, AP 0,90). Un **buen jugador** (600 horas) puede parecer tramposo: **vigilar, no sancionar**.
- **Tarjeta de ejemplo:**
  - Mi app decide **a quién vigilar o proponer para sanción** a partir de **precisión, reacción, headshots y reportes**.
  - Antes de modelar tuve que **elegir un umbral exigente (precisión ≥ 95 %, umbral 0,77)** porque sancionar a un inocente es grave.
  - Caza **33 de 59** tramposos y sanciona por error a **2 de 941** inocentes, frente a **0** del modelo tonto.
  - No debe usarse para **expulsar sin que una persona revise**.
