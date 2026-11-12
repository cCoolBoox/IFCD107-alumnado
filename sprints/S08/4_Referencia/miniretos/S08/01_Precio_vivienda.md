# 🏠 Miniapp 1 · ¿Cuánto vale este piso en Tenerife?

⭐⭐ · 50 min · **regresión** · practica S07 (regresión lineal) y S08 (árbol, bosque, boosting)

## Qué construyes
- Una **tasadora**: le dices metros, zona y extras, y te devuelve un precio estimado.
- Compruebas si una **recta** basta o si un **bosque** o un **boosting** tasan mejor.

## Datos
- `viviendas_tenerife.csv`: 1 800 viviendas **inventadas**. No son precios reales.
- Objetivo: `precio` (en euros). Variables: `zona`, `metros`, `habitaciones`, `banos`, `antiguedad`, `vista_mar`, `garaje`, `terraza`, `ascensor`, `estado`.

## Paso a paso (en Colab, una celda por paso)

1. **Carga y mira.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/viviendas_tenerife.csv"
df = pd.read_csv(URL)
print(df.shape)
print(df.groupby("zona")["precio"].median().sort_values())
df.head()
```

2. **Dibuja la pregunta.** ¿Los puntos siguen una recta?

```python
for zona, g in df.groupby("zona"):
    plt.scatter(g["metros"], g["precio"], s=8, alpha=0.5, label=zona)
plt.xlabel("metros"); plt.ylabel("precio (€)"); plt.legend(); plt.show()
```

3. **Prepara y separa.** Las categorías (`zona`, `estado`) pasan a columnas de 0 y 1. El examen (`test`) no se mira hasta el final.

```python
X = pd.get_dummies(df.drop(columns="precio"), columns=["zona", "estado"], dtype=int)
y = df["precio"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(len(X_train), "para entrenar ·", len(X_test), "para el examen (NO mirar)")
```

4. **El duelo (solo con `train`).** Error medio en euros (MAE) con validación cruzada: menos es mejor.

```python
modelos = {
    "Siempre la media": DummyRegressor(),
    "Regresión lineal": LinearRegression(),
    "Árbol (profundidad 5)": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Bosque": RandomForestRegressor(n_estimators=200, min_samples_leaf=3, random_state=42, n_jobs=2),
    "Boosting": HistGradientBoostingRegressor(random_state=42),
}
tabla = {n: -cross_val_score(m, X_train, y_train, cv=5, scoring="neg_mean_absolute_error").mean()
         for n, m in modelos.items()}
pd.Series(tabla).round(0).sort_values().rename("MAE en € (validación cruzada)")
```

5. **El examen: UNA vez, con el campeón.** Cambia `campeon` si el tuyo es otro.

```python
campeon = "Boosting"
final = modelos[campeon].fit(X_train, y_train)
pred = final.predict(X_test)
print(f"{campeon}: se equivoca de media {mean_absolute_error(y_test, pred):,.0f} € · R² = {r2_score(y_test, pred):.3f}")
plt.scatter(y_test, pred, s=8, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--", label="acierto perfecto")
plt.xlabel("precio real (€)"); plt.ylabel("precio estimado (€)"); plt.legend(); plt.show()
```

6. **Dónde falla.** Las 5 viviendas peor tasadas del examen.

```python
fallos = X_test.assign(real=y_test, estimado=pred.round(-3), error=(y_test - pred).abs().round(-3))
fallos.sort_values("error", ascending=False).head(5)[["metros", "vista_mar", "estado_reformada", "real", "estimado", "error"]]
```

## Tu app
- Una función que tasa cualquier piso. Pruébala con tres casos distintos y comenta si el resultado tiene sentido.

```python
def tasar(metros=90, habitaciones=3, banos=2, antiguedad=20, vista_mar=0, garaje=0, terraza=0,
          ascensor=0, zona="Norte", estado="buen estado"):
    fila = pd.DataFrame([dict(metros=metros, habitaciones=habitaciones, banos=banos, antiguedad=antiguedad,
                              vista_mar=vista_mar, garaje=garaje, terraza=terraza, ascensor=ascensor,
                              zona=zona, estado=estado)])
    fila = pd.get_dummies(fila, columns=["zona", "estado"], dtype=int).reindex(columns=X.columns, fill_value=0)
    return int(round(final.predict(fila)[0], -3))

print(tasar(zona="Sur costa", metros=110, vista_mar=1), "€  · piso con vista en el sur")
print(tasar(zona="Interior", metros=70, antiguedad=45, estado="a reformar"), "€  · piso viejo en el interior")
print(tasar(zona="Área metropolitana", metros=95, garaje=1, ascensor=1), "€  · piso con garaje en la capital")
```

```python
# (solo Colab) deslizadores para jugar con la tasadora
from ipywidgets import interact
interact(tasar, metros=(30, 300, 5), habitaciones=(1, 7), banos=(1, 5), antiguedad=(0, 80),
         vista_mar=(0, 1), garaje=(0, 1), terraza=(0, 1), ascensor=(0, 1),
         zona=["Sur costa", "Área metropolitana", "Norte", "Este", "Interior"],
         estado=["a reformar", "buen estado", "reformada"]);
```

## Qué deberías ver
- Mediana de precio por zona: de unos **101 000 €** (Interior) a unos **378 500 €** (Sur costa).
- Duelo (MAE con validación cruzada): **Boosting ≈ 19 000 €** · Bosque ≈ 22 200 € · Lineal ≈ 31 200 € · Árbol ≈ 39 600 € · «siempre la media» ≈ 104 600 €.
- Examen: **Boosting se equivoca de media ≈ 18 000 € y R² ≈ 0,95**.
- Los mayores fallos son sobre todo **casas grandes** (más de 180 m²), con errores de 80 000 € o más: hay pocas y el modelo las ha visto poco.
- La app: unos 555 000 € (vista en el sur), unos 64 000 € (viejo en el interior) y unos 202 000 € (capital con garaje).
- La recta (lineal) se queda atrás porque el precio **no sube en línea recta**: los metros valen más en el sur que en el interior.
- Tus cifras pueden diferir en el último decimal.

## Extra 🔴
- Prueba con el **logaritmo del precio** (`np.log(y)`): ¿mejora la recta? Piensa por qué (los precios suben en porcentaje, no en euros).
- Añade **Ridge** (S07) y mira si cambia algo.
- Calcula cuánto «vale» de media tener **vista al mar** en cada zona.

## Cuidado
- **No es una tasación oficial**: los datos son inventados y no hay calles, fechas ni estado real de la casa.
- Un piso muy distinto de los que ha visto (por ejemplo, de 500 m²) recibe un precio poco fiable.
