# 🔥 Miniapp 8 · ¿Hoy hay riesgo de incendio forestal?

⭐⭐⭐ · 55 min · **suceso raro y semáforo de riesgo** · practica S07 (umbral, PR) y S08 (árbol con reglas, bosque, boosting, búsqueda de hiperparámetros)

## Qué construyes
- Un **semáforo de riesgo de incendio** para una zona de las islas: verde, amarillo o rojo, según el tiempo y el terreno.
- Aprendes a trabajar con un suceso **raro** (6 %) y a usar el modelo para **ordenar** zonas y mandar recursos donde más hacen falta.

## Datos
- `incendios_canarias.csv`: 5 000 situaciones **inventadas** (zona y día) en Tenerife, Gran Canaria y La Palma. Columnas: isla, altitud, si es zona de pinar, temperatura, humedad, viento, días sin lluvia y calima.
- Objetivo: `incendio` (1 = se declaró un incendio ese día en esa zona).

## Paso a paso

1. **Carga y cuenta.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate, cross_val_predict, StratifiedKFold, RandomizedSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/incendios_canarias.csv"
df = pd.read_csv(URL)
print(df.shape, "· incendios:", int(df["incendio"].sum()), f"({df['incendio'].mean():.1%})")
df.groupby("incendio")[["temperatura", "humedad", "viento_kmh", "dias_sin_lluvia", "calima"]].mean().round(1)
```

2. **Separa y prepara.** Solo `isla` es texto: pasa a columnas de 0 y 1.

```python
y = df["incendio"]; X = df.drop(columns="incendio")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
cv = StratifiedKFold(5, shuffle=True, random_state=42)
def con_modelo(m):
    prep = ColumnTransformer([("isla", OneHotEncoder(), ["isla"])], remainder="passthrough")
    return Pipeline([("prep", prep), ("modelo", m)])
```

3. **Las reglas de un árbol pequeño.** Antes de comparar, mira qué reglas encuentra un árbol de profundidad 3 (explicables a un técnico de emergencias). Casi todas las hojas dicen `0` porque el incendio es raro; **fíjate en el camino que llega a un `1`**.

```python
arbol = con_modelo(DecisionTreeClassifier(max_depth=3, min_samples_leaf=30, random_state=42)).fit(X_tr, y_tr)
nombres = [n.replace("remainder__", "").replace("isla__", "") for n in arbol[0].get_feature_names_out()]
print(export_text(arbol[1], feature_names=nombres, max_depth=3))
```

4. **El duelo.** Con un suceso tan raro, la **AP** (precisión–recall) es la nota que más cuenta.

```python
modelos = {"Nunca hay incendio (tonto)": DummyClassifier(strategy="prior"),
           "Logística": LogisticRegression(max_iter=2000),
           "Árbol (profundidad 5)": DecisionTreeClassifier(max_depth=5, min_samples_leaf=10, random_state=42),
           "Bosque": RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=42, n_jobs=2),
           "Boosting": HistGradientBoostingClassifier(random_state=42)}
filas = {}
for nombre, m in modelos.items():
    r = cross_validate(con_modelo(m), X_tr, y_tr, cv=cv, scoring=["accuracy", "roc_auc", "average_precision"])
    filas[nombre] = {"precisión global": r["test_accuracy"].mean(), "AUC": r["test_roc_auc"].mean(), "AP": r["test_average_precision"].mean()}
pd.DataFrame(filas).T.round(3)
```

5. **Afina el boosting con una búsqueda** (15 combinaciones al azar). Mira si mejora al bosque.

```python
espacio = {"modelo__learning_rate": [0.02, 0.05, 0.1], "modelo__max_depth": [2, 3, 4, None],
           "modelo__max_leaf_nodes": [5, 10, 31], "modelo__min_samples_leaf": [10, 30, 60], "modelo__l2_regularization": [0, 1, 10]}
busqueda = RandomizedSearchCV(con_modelo(HistGradientBoostingClassifier(max_iter=200, random_state=42)), espacio, n_iter=15,
                              scoring="average_precision", cv=cv, random_state=42, n_jobs=2).fit(X_tr, y_tr)
print("Mejor AP en validación:", round(busqueda.best_score_, 3))
print("Parámetros:", busqueda.best_params_)
```

6. **El semáforo.** El campeón es el boosting afinado (supera al bosque en validación). Convierte su probabilidad en tres colores y comprueba, **en el examen y una sola vez**, cuántos incendios caen en cada color. Los cortes los fijamos nosotros: rojo si la probabilidad es ≥ 25 %, amarillo si está entre 10 % y 25 %.

```python
campeon = busqueda.best_estimator_                      # ya viene entrenado con todo `train`
proba = campeon.predict_proba(X_te)[:, 1]
color = pd.cut(proba, [-0.01, 0.10, 0.25, 1.0], labels=["🟢 verde", "🟡 amarillo", "🔴 rojo"])
resumen = pd.DataFrame({"color": color, "incendio": y_te.values}).groupby("color").agg(zonas=("incendio", "size"), incendios=("incendio", "sum"))
resumen["% con incendio"] = (100 * resumen["incendios"] / resumen["zonas"]).round(1)
print(resumen)
print(f"AUC {roc_auc_score(y_te, proba):.3f} · AP {average_precision_score(y_te, proba):.3f} · el tonto tendría AP {y_te.mean():.3f}")
```

## Tu app
- El semáforo para **una zona y un día**.

```python
def semaforo(isla, altitud_m, zona_pinar, temperatura, humedad, viento_kmh, dias_sin_lluvia, calima):
    fila = pd.DataFrame([dict(isla=isla, altitud_m=altitud_m, zona_pinar=zona_pinar, temperatura=temperatura, humedad=humedad,
                              viento_kmh=viento_kmh, dias_sin_lluvia=dias_sin_lluvia, calima=calima)])[X.columns]
    p = campeon.predict_proba(fila)[0, 1]
    c = "🔴 rojo" if p >= 0.25 else ("🟡 amarillo" if p >= 0.10 else "🟢 verde")
    return f"{c} · probabilidad de incendio {p:.0%}"

print(semaforo("Tenerife", 1500, 1, 38, 12, 40, 60, 1), "· pinar, calor, seco y con viento")
print(semaforo("Gran Canaria", 300, 0, 24, 65, 10, 3, 0), "· costa tranquila")
print(semaforo("La Palma", 900, 1, 30, 30, 20, 25, 0), "· un día intermedio")
```

## Qué deberías ver
- **5 000 zonas-día, 302 incendios (6,0 %)**. Los días con incendio: más calor (≈ 29 °C frente a ≈ 24,5), menos humedad (32 % frente a 53 %), más días sin lluvia (≈ 19 frente a ≈ 14) y más calima.
- El árbol pequeño dice `0` casi siempre; el camino a un `1` es **humedad ≤ 29,5 % + temperatura > 31 °C + más de 17 días sin lluvia**.
- Tabla con CV: tonto **94 %** de precisión global (AUC 0,50, AP 0,06) · logística AUC 0,81 · AP 0,35 · árbol AP 0,36 · **bosque AUC 0,83 · AP 0,45** · boosting AP 0,39. Es un problema **difícil**: la precisión global casi no se mueve, pero la AP multiplica por 7 la del tonto.
- La búsqueda (15 combinaciones) deja el boosting en **AP ≈ 0,47** en validación, por encima del bosque.
- Semáforo en el examen (1 250 zonas, 75 incendios): 🔴 **91 zonas** con **44 incendios** (**48 %** de ellas) · 🟡 57 zonas con 7 incendios (12 %) · 🟢 1 102 zonas con 24 incendios (**2,2 %**). Con el 7 % de las zonas en rojo, se cubre el **59 %** de los incendios. AUC ≈ 0,82 · AP ≈ 0,49.
- App: pinar, calor, seco y con viento ≈ **86 % → rojo**; costa tranquila ≈ **1 % → verde**; el día intermedio ≈ **14 % → amarillo**.

## Extra 🔴
- Cambia los cortes del semáforo a **15 %** y **35 %**: ¿cuántas zonas caen en rojo?, ¿qué cuesta más, un falso rojo o un incendio en verde?
- Mira la importancia de las variables con `permutation_importance` sobre `train`: ¿qué manda?
- Dibuja la **curva precisión–recall** del campeón y compárala con una línea horizontal en el 6 %.

## Cuidado
- Un suceso raro hace que **cada incendio pese mucho** en la nota: con 5 000 zonas, la nota oscila.
- Los datos son **inventados**: para un riesgo real hay que usar datos de los servicios de emergencias y la previsión meteorológica.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**. 🗣️ = respuesta de redacción u opinión: no hay cifra única.

#### Extra 1 · Cortes al 15 % y 35 % (examen, 1 250 zonas, 75 incendios)
- **Qué hacer:**
  1. Cambia los dos cortes de `pd.cut` a 0,15 y 0,35 y cuenta zonas e incendios por color.
  2. Compara con los cortes de la ficha (0,10 y 0,25).
```python
for corte_amarillo, corte_rojo in ((0.10, 0.25), (0.15, 0.35)):
    color = pd.cut(proba, [-0.01, corte_amarillo, corte_rojo, 1.0], labels=["verde", "amarillo", "rojo"])
    print(f"cortes {corte_amarillo} y {corte_rojo}")
    print(pd.DataFrame({"color": color, "incendio": y_te.values}).groupby("color", observed=False).agg(zonas=("incendio", "size"), incendios=("incendio", "sum")))
```
- **Qué sale y por qué:**
  - 🔴 **58 zonas** con **34 incendios** (59 %); 🟡 54 zonas con **16**; 🟢 1 138 zonas con **25** incendios.
  - Con los cortes de la ficha (10 % y 25 %): 🔴 91 zonas con 44 incendios.
  - Con cortes **más altos** hay menos zonas en rojo (58 frente a 91): el rojo cubre **menos incendios (34 frente a 44)** y el amarillo recoge más (16 frente a 7). En verde apenas cambia (25 frente a 24).
  - **¿Qué cuesta más?** Un incendio en verde es **mucho más grave** que un falso rojo (que cuesta una patrulla). Por eso se prefieren **cortes más bajos**. Es una decisión de **emergencias**, no del modelo.

#### Extra 2 · `permutation_importance` (sobre `train`, AP)
- **Qué hacer:**
  1. Usa `permutation_importance` con `scoring="average_precision"` sobre `train`.
  2. Ordena de mayor a menor.
```python
from sklearn.inspection import permutation_importance
r = permutation_importance(campeon, X_tr, y_tr, scoring="average_precision", n_repeats=5, random_state=42, n_jobs=2)
print(pd.Series(r.importances_mean, index=X_tr.columns).sort_values(ascending=False).round(3))
```
- **Qué sale y por qué:**
  - **humedad 0,41** · **temperatura 0,24** · días sin lluvia 0,18 · viento 0,14 · zona pinar 0,06 · calima 0,03 · isla y altitud ≈ 0,01. **Manda la humedad.** Coincide con el árbol, que empezaba por humedad.

#### Extra 3 · Curva precisión–recall (🗣️ con dibujo)
- **Qué hacer:**
  1. Dibuja la curva precisión–recall con `PrecisionRecallDisplay`.
  2. Añade una línea horizontal en la tasa de incendios (lo que haría el modelo tonto).
```python
from sklearn.metrics import PrecisionRecallDisplay
PrecisionRecallDisplay.from_predictions(y_te, proba)
plt.axhline(y_te.mean(), color="gray", linestyle="--", label=f"el tonto ({y_te.mean():.0%})")
plt.legend(); plt.show()
```
- **Qué sale y por qué:**
  - La curva del boosting está **muy por encima de la línea horizontal del 6 %** (lo que daría el tonto) en la parte izquierda, y **cae al subir el recall**: cuanto más incendios quieres cubrir, **más falsos rojos**. Con AP ≈ 0,49 frente a 0,06 del tonto: **×8**.

#### Para cerrar
- **Para comentar:** el problema es **difícil** (cada incendio pesa mucho en la nota) y se explica con **semáforo, no con un sí/no**.
- **Tarjeta de ejemplo:**
  - Mi app decide **el color del semáforo de riesgo** a partir de **humedad, temperatura, días sin lluvia y viento**.
  - Antes de modelar tuve que **olvidar la precisión global (94 % del tonto) y usar la AP**.
  - Con **el 7 % de las zonas en rojo cubre el 59 % de los incendios**, frente a **≈ 7 %** que cubriría un reparto al azar.
  - No debe usarse para **decidir evacuaciones**: son datos inventados.
