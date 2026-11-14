# 🎬 Miniapp 2 · ¿Quién va a darse de baja?

⭐⭐ · 55 min · **regresión logística explicada** · practica S07 (odds ratios, probabilidades, umbral, coste de campaña)

## Qué construyes
- Un programa que **avisa a una plataforma de series de qué clientes están a punto de irse**, para ofrecerles una oferta a tiempo.
- Aprendes a **leer los coeficientes** de la logística («diez días más sin entrar multiplica por 1,5 las posibilidades de irse») y a decidir **a quién llamar** con euros.

## Datos
- `abandono_streaming.csv`: 5 000 clientes **inventados**. Columnas: plan, meses de antigüedad, horas al mes, series vistas, incidencias de soporte, días sin entrar, método de pago, perfiles.
- Objetivo: `abandona` (1 = se da de baja el mes siguiente). Se va el **21 %**.

## Paso a paso

1. **Carga y compara a los que se van con los que se quedan.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import roc_auc_score, confusion_matrix

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/abandono_streaming.csv"
df = pd.read_csv(URL)
print(df.shape, "· se van:", f"{df['abandona'].mean():.1%}")
df.groupby("abandona")[["meses_antiguedad", "horas_mes", "series_mes", "incidencias_soporte", "dias_sin_usar", "perfiles"]].mean().round(1)
```

2. **Separa y prepara.** `precio_mensual` repite lo que dice `plan` (cada plan tiene un precio fijo): la quitamos para que los coeficientes se entiendan.

```python
y = df["abandona"]
X = df.drop(columns=["abandona", "precio_mensual"])
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
cat = ["plan", "metodo_pago"]
num = [c for c in X.columns if c not in cat]
def con_modelo(m):
    prep = ColumnTransformer([("n", StandardScaler(), num), ("c", OneHotEncoder(drop="first"), cat)])
    return Pipeline([("prep", prep), ("modelo", m)])
cv = StratifiedKFold(5, shuffle=True, random_state=42)
```

3. **El duelo** (con el modelo tonto).

```python
modelos = {"Siempre «se queda» (tonto)": DummyClassifier(strategy="most_frequent"),
           "Logística": LogisticRegression(max_iter=1000),
           "k-NN (k=25)": KNeighborsClassifier(25),
           "Naive Bayes": GaussianNB()}
for nombre, m in modelos.items():
    p = con_modelo(m)
    acc = cross_val_score(p, X_tr, y_tr, cv=cv, scoring="accuracy").mean()
    auc = cross_val_score(p, X_tr, y_tr, cv=cv, scoring="roc_auc")
    print(f"{nombre:28s} precisión {acc:.3f} · AUC {auc.mean():.3f} ± {auc.std():.3f}")
```

4. **Lee la logística: los odds ratios.** Una variable con **1,5** multiplica por 1,5 las posibilidades de irse; con **0,5**, las divide por dos. Los números están escalados: el efecto es de **«una desviación típica» más**. Los planes y métodos de pago se comparan con el que falta en la lista (`básico` y `paypal`).

```python
logistica = con_modelo(LogisticRegression(max_iter=1000)).fit(X_tr, y_tr)
nombres = logistica[0].get_feature_names_out()
odds = pd.Series(np.exp(logistica[1].coef_[0]), index=nombres).sort_values()
odds.index = [n.split("__")[1] for n in odds.index]
odds.round(2).plot(kind="barh", title="Odds ratios (1 = no cambia nada)"); plt.axvline(1, color="gray"); plt.show()
odds.round(2)
```

5. **¿A quién llamamos?** Una oferta cuesta **10 €** a cada cliente contactado, convence al **40 %** de los que se iban y un cliente que se queda vale **80 €**. Contactar compensa si `p · 0,40 · 80 − 10 > 0`, es decir, si **p > 0,31**.

```python
coste_oferta, exito, valor = 10, 0.40, 80
umbral = coste_oferta / (exito * valor)
print(f"Umbral para contactar: {umbral:.2f}")

proba = logistica.predict_proba(X_te)[:, 1]
def beneficio(contactar, y_real):
    return (contactar * (y_real * exito * valor - coste_oferta)).sum()

print("Examen (1 250 clientes):")
print("  No contactar a nadie        →", 0, "€")
print("  Contactar a todos           →", round(beneficio(np.ones(len(y_te)), y_te.values)), "€")
print("  Contactar si p >", round(umbral, 2), "      →", round(beneficio(proba >= umbral, y_te.values)), "€",
      f"({int((proba >= umbral).sum())} clientes contactados)")
print(f"AUC en el examen: {roc_auc_score(y_te, proba):.3f}")
```

## Tu app
- Una función que dice la probabilidad de baja de **un cliente** y si hay que contactarle.

```python
def cliente(plan, meses_antiguedad, horas_mes, series_mes, incidencias_soporte, dias_sin_usar, metodo_pago, perfiles):
    fila = pd.DataFrame([dict(plan=plan, meses_antiguedad=meses_antiguedad, horas_mes=horas_mes, series_mes=series_mes,
                              incidencias_soporte=incidencias_soporte, dias_sin_usar=dias_sin_usar, metodo_pago=metodo_pago, perfiles=perfiles)])
    p = logistica.predict_proba(fila)[0, 1]
    return f"probabilidad de baja {p:.0%} → {'📞 contactar con oferta' if p >= umbral else 'no hace falta'}"

print(cliente("basico", 2, 3, 1, 3, 25, "prepago", 1))
print(cliente("premium", 40, 25, 4, 0, 2, "tarjeta", 4))
print(cliente("estandar", 10, 8, 2, 1, 14, "paypal", 2))
```

## Qué deberías ver
- Se van el **21,2 %** (1 060 de 5 000). Los que se van entran **12,5 días** sin conectar (los que se quedan, 7,1) y ven **16 horas** al mes (frente a 23).
- CV en `train`: tonto **0,788** (AUC 0,50) · logística **0,802 · AUC 0,726** · k-NN **AUC 0,689** · Naive Bayes **AUC 0,708**. Es un problema **difícil**: ninguna nota pasa de 0,75, y es normal.
- Odds ratios (por desviación típica): `dias_sin_usar` **1,50** · `incidencias_soporte` **1,34** · pago `prepago` **1,86** · `horas_mes` **0,53** · plan `premium` **0,51** · `meses_antiguedad` **0,79**.
- Umbral por coste: **0,31**. En el examen: contactar a todos **−4 020 €** · no hacer nada **0 €** · contactar si p > 0,31 **+980 €** (238 clientes contactados). AUC **0,736**.
- App: cliente de plan básico, prepago y 25 días sin entrar ≈ **89 %**; el premium que entra a diario ≈ **3 %**; el intermedio ≈ **37 %**, y se le contacta.

## Extra 🔴
- Cambia el éxito de la oferta a **20 %**: ¿a cuántos contactas?, ¿sigue compensando?
- Compara con el umbral **0,5** de siempre: ¿a cuántos clientes dejas de llamar?
- `series_mes` sale con un odds ratio **por encima de 1**: ¿más series, más bajas? ¿Será una causa o una casualidad de los datos?

## Cuidado
- Los coeficientes dicen **qué se parece a qué**, no **qué causa qué**: dar de baja a quien no entra no evita que se vaya.
- Los datos son **inventados**; el modelo no vale para una plataforma real.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

- **Extra 1 · Éxito de la oferta al 20 %:** el umbral sube de 0,31 a **0,625** y solo se contacta a **28 clientes**; el beneficio cae de **+980 € a +24 €**. **Casi no compensa.** Contactar a todos pierde **−8 260 €**.
- **Extra 2 · Umbral 0,5:** contacta a **64** clientes (**+448 €**) frente a **238** (**+980 €**): con 0,5 **dejas de llamar a 174 clientes** y pierdes más de la mitad del beneficio.
- **Extra 3 · `series_mes` con odds ratio 1,13 (>1):** ¿más series, más bajas? **No: es colinealidad.**
  - `series_mes` y `horas_mes` van casi pegadas (**corr. 0,89**). Solas, quien ve más series **se va menos** (corr. −0,17).
  - Si se **quita `horas_mes`**, `series_mes` pasa a **OR 0,68 (<1)**. Con las dos, el modelo reparte el efecto y puede salir «al revés».
  - Moraleja: **un coeficiente suelto no se lee solo**, y menos aún como causa.
- **Para comentar:** problema **difícil** (AUC 0,72–0,74): una nota «baja» aquí **no es un fallo**. Aun así, con el umbral por coste sale **+980 €**.
- **Tarjeta de ejemplo:**
  - Mi app decide **a quién ofrecer una oferta de retención** a partir de **días sin entrar, horas al mes, plan y pago**.
  - Antes de modelar tuve que **calcular el umbral con el coste (0,31) en vez de usar 0,5**.
  - Gana **+980 €** en el examen contactando a 238 clientes, frente a **0 €** sin hacer nada y **−4 020 €** contactando a todos.
  - No debe usarse para **afirmar que una variable *causa* la baja**.
