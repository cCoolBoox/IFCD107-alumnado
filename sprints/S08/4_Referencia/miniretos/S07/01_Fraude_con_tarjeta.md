# 💳 Miniapp 1 · ¿Esta compra es un fraude?

⭐⭐⭐ · 55 min · **clases muy desiguales** · practica S07 (precisión engañosa, matriz de confusión, ROC y PR, umbral por coste)

## Qué construyes
- Un **detector de compras sospechosas** para un banco: de cada 100 compras, solo 1 o 2 son fraude.
- Descubres por qué **«acierta el 98 %» puede ser un modelo inútil** y cómo elegir el umbral con **euros**, no con intuición.

## Datos
- `fraude_tarjeta.csv`: 20 000 compras **inventadas**, con un **1,5 % de fraudes**. Columnas: importe, hora, distancia a casa, si es en el extranjero, tipo de comercio, compras en la última hora, antigüedad de la tarjeta, pago online.
- Objetivo: `es_fraude` (1 = fraude).

## Paso a paso

1. **Carga y cuenta.** Mira lo desigual que es.

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, roc_auc_score, average_precision_score, precision_score, recall_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/fraude_tarjeta.csv"
df = pd.read_csv(URL)
print(df.shape, "· fraudes:", int(df["es_fraude"].sum()), f"({df['es_fraude'].mean():.2%})")
df.groupby("es_fraude")[["importe", "distancia_casa_km", "compras_ultima_hora", "antiguedad_tarjeta_meses"]].mean().round(1)
```

2. **Separa conservando la proporción** (`stratify`), o el examen podría quedarse con pocos fraudes.

```python
y = df["es_fraude"]; X = df.drop(columns="es_fraude")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print("fraudes en train:", int(y_tr.sum()), "· en el examen:", int(y_te.sum()))
numericas = [c for c in X.columns if c != "comercio"]
def con_modelo(m):
    prep = ColumnTransformer([("n", StandardScaler(), numericas), ("c", OneHotEncoder(), ["comercio"])])
    return Pipeline([("prep", prep), ("modelo", m)])
```

3. **La trampa.** Un modelo que dice **siempre «no es fraude»**. ¿Qué nota saca?

```python
cv = StratifiedKFold(5, shuffle=True, random_state=42)
tonto = con_modelo(DummyClassifier(strategy="most_frequent"))
acc = cross_val_score(tonto, X_tr, y_tr, cv=cv, scoring="accuracy").mean()
print(f"El modelo que nunca avisa acierta el {acc:.1%}... y no detecta ni un fraude")
```

4. **Compara con las métricas buenas.** Mira la precisión global, el **AUC** (ROC) y la **AP** (área de la curva precisión–recall). Con tan pocos fraudes, la AP es la que más se fija.

```python
modelos = {"Siempre «no» (tonto)": DummyClassifier(strategy="most_frequent"),
           "Logística": LogisticRegression(max_iter=1000),
           "Logística con pesos": LogisticRegression(max_iter=1000, class_weight="balanced"),
           "k-NN (k=15)": KNeighborsClassifier(15),
           "Naive Bayes": GaussianNB()}
filas = {}
for nombre, m in modelos.items():
    p = con_modelo(m)
    filas[nombre] = {"precisión global": cross_val_score(p, X_tr, y_tr, cv=cv, scoring="accuracy").mean(),
                     "AUC": cross_val_score(p, X_tr, y_tr, cv=cv, scoring="roc_auc").mean(),
                     "AP": cross_val_score(p, X_tr, y_tr, cv=cv, scoring="average_precision").mean()}
pd.DataFrame(filas).T.round(3)
```

5. **El umbral con euros.** Dejar pasar un fraude cuesta **el importe de esa compra**; una falsa alarma cuesta **3 €** (llamar al cliente). Probamos umbrales con las predicciones de validación cruzada **de `train`**.

```python
logistica = con_modelo(LogisticRegression(max_iter=1000))
proba_cv = cross_val_predict(logistica, X_tr, y_tr, cv=cv, method="predict_proba")[:, 1]
def coste(y_real, proba, importes, umbral, falsa_alarma=3):
    aviso = proba >= umbral
    perdido = importes[(y_real == 1) & ~aviso].sum()
    molestias = falsa_alarma * ((y_real == 0) & aviso).sum()
    return perdido + molestias

umbrales = np.arange(0.01, 0.9, 0.01)
costes = [coste(y_tr.values, proba_cv, X_tr["importe"].values, u) for u in umbrales]
mejor = umbrales[int(np.argmin(costes))]
plt.plot(umbrales, costes); plt.axvline(mejor, color="red", ls="--"); plt.xlabel("umbral"); plt.ylabel("coste en train (€)")
plt.title("¿A partir de qué probabilidad avisamos?"); plt.show()
print(f"Umbral con menor coste: {mejor:.2f} (con 0,50 por defecto el coste era {coste(y_tr.values, proba_cv, X_tr['importe'].values, 0.5):,.0f} € frente a {min(costes):,.0f} €)")
```

6. **El examen: una vez**, con el umbral ya elegido.

```python
final = logistica.fit(X_tr, y_tr)
proba = final.predict_proba(X_te)[:, 1]
aviso = proba >= mejor
vn, fp, fn, vp = confusion_matrix(y_te, aviso).ravel()
print(f"Fraudes detectados: {vp} de {vp + fn} · falsas alarmas: {fp} · fraudes que se escapan: {fn}")
print(f"AUC {roc_auc_score(y_te, proba):.3f} · AP {average_precision_score(y_te, proba):.3f}")
sin_modelo = X_te["importe"].values[y_te.values == 1].sum()
print(f"Sin modelo se pierden {sin_modelo:,.0f} € · con el modelo {coste(y_te.values, proba, X_te['importe'].values, mejor):,.0f} € (incluidas las molestias)")
```

## Tu app
- Una función que valora **una compra** y dice si hay que **avisar**.

```python
def revisar(importe, hora, distancia_casa_km, es_extranjero, comercio, compras_ultima_hora, antiguedad_tarjeta_meses, pago_online):
    fila = pd.DataFrame([dict(importe=importe, hora=hora, distancia_casa_km=distancia_casa_km, es_extranjero=es_extranjero,
                              comercio=comercio, compras_ultima_hora=compras_ultima_hora,
                              antiguedad_tarjeta_meses=antiguedad_tarjeta_meses, pago_online=pago_online)])
    p = final.predict_proba(fila)[0, 1]
    return f"{'⚠️ AVISAR' if p >= mejor else '✅ normal'} · probabilidad de fraude {p:.1%}"

print(revisar(35, 13, 4, 0, "supermercado", 1, 40, 0))
print(revisar(950, 3, 800, 1, "electronica", 5, 2, 1))
print(revisar(120, 23, 60, 1, "juegos_online", 2, 6, 1))
```

## Qué deberías ver
- **20 000 compras, 309 fraudes (1,54 %)**: 232 en `train` y 77 en el examen. Los fraudes son más caros (≈ 142 € frente a 60 €), más lejanos y de tarjetas más nuevas.
- El modelo que **nunca avisa** acierta el **98,5 %**, con AUC **0,50** y AP **0,015**.
- Tabla con CV: logística **98,8 % · AUC 0,93 · AP 0,54**; con pesos baja la precisión global a **88 %** (avisa mucho más) y la AP a 0,48; k-NN **AUC 0,82**; Naive Bayes **AUC 0,91 · AP 0,32**.
- Umbral por coste: el mejor sale **≈ 0,05** (no 0,50): en `train` pasa de ≈ **17 200 €** a ≈ **7 500 €** de pérdidas.
- Examen: detectas **52 de 77** fraudes, con **212 falsas alarmas** y **25 fraudes** que se escapan. Pierdes **≈ 3 200 €** (molestias incluidas) frente a **≈ 11 150 €** sin modelo.
- App: la compra normal da ≈ 0,1 %; la de 950 € en el extranjero de madrugada, ≈ 100 %; la de juegos online, ≈ 30 %, y avisa.

## Extra 🔴
- Cambia el coste de una falsa alarma a **20 €**: ¿sube o baja el umbral?, ¿por qué?
- Prueba el umbral **0,5** en el examen y compáralo con el tuyo.
- ¿Qué cuenta más: avisar de más o de menos? Escribe cómo se lo explicarías a un directivo del banco.

## Cuidado
- Los datos son **inventados**; un banco real tiene muchos más datos y fraudes que **cambian de forma** cada mes.
- Con pocos fraudes en el examen, **la nota oscila mucho**: no te fíes de una cifra con decimales.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**. 🗣️ = respuesta de redacción u opinión: no hay cifra única.

#### Extra 1 · Falsa alarma a 20 €
- **Qué hacer:**
  1. Repite la búsqueda de umbral con `falsa_alarma=20` (el último parámetro de `coste`).
  2. Compara el mejor umbral con el de 3 €. Después mira el examen con ese umbral.
```python
for falsa_alarma in (3, 20):
    costes = [coste(y_tr.values, proba_cv, X_tr["importe"].values, u, falsa_alarma) for u in umbrales]
    print(f"falsa alarma {falsa_alarma} € → mejor umbral {umbrales[int(np.argmin(costes))]:.2f} · coste {min(costes):,.0f} €")
```
- **Qué sale y por qué:**
  - El umbral óptimo **sube de 0,05 a 0,12**.
  - ¿Por qué? Cada falsa alarma cuesta más → hay que **estar más seguro** antes de avisar.
  - En el examen con **umbral 0,12**: detecta **46 de 77** (con 70 falsas alarmas), coste **4 596 €** (con falsa alarma de 20 €), frente a **6 768 €** si se hubiera mantenido el 0,05.

#### Extra 2 · Umbral 0,5 en el examen
- **Qué hacer:**
  1. Calcula la matriz de confusión del examen con el umbral 0,5 y con el tuyo.
  2. Compara fraudes detectados, falsas alarmas y **pérdida en euros**.
```python
for u in (0.5, mejor):
    vn, fp, fn, vp = confusion_matrix(y_te, proba >= u).ravel()
    perdida = coste(y_te.values, proba, X_te["importe"].values, u)
    print(f"umbral {u:.2f}: detecta {vp} de {vp + fn} · falsas alarmas {fp} · pérdida {perdida:,.0f} €")
```
- **Qué sale y por qué:**
  - Detecta solo **27 de 77** (50 escapan), con **7 falsas alarmas**, y pierde **≈ 5 090 €** frente a **≈ 3 200 €** con 0,05. Parece más «fino» (pocas falsas alarmas) y **sale más caro**.

#### Extra 3 · Para un directivo (🗣️)
- **Qué hacer:**
  1. Escribe 3 frases: **qué cuesta cada error** (fraude que se escapa / falsa alarma), **por qué el umbral no es 0,5** y **cuándo lo revisarías**.
  2. Usa los euros de la celda del umbral, no palabras vagas.
- **Qué sale y por qué:**
  - Respuesta modelo: *«Avisar de más cuesta unos euros de molestias; avisar de menos cuesta el fraude entero. Por eso el umbral no es 0,5: lo fijamos donde el coste total es menor, y lo revisamos cuando cambie lo que cuesta una falsa alarma.»*

#### Para cerrar
- **Para comentar:** el «nunca avisa» acierta el 98,5 %: la **precisión engaña** cuando una clase es rara. Mirar **AUC, AP y matriz de confusión**.
- **Tarjeta de ejemplo:**
  - Mi app decide **si avisar de una compra** a partir de **importe, distancia, hora, tarjeta y comercio**.
  - Antes de modelar tuve que **olvidarme de la precisión y fijar el umbral por coste (0,05, no 0,50)**.
  - Acierta **52 de 77 fraudes** en el examen, frente a **0 del modelo tonto**.
  - No debe usarse para **bloquear una tarjeta sin que lo revise una persona**.
