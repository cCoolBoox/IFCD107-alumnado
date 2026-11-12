# 💎 Miniapp 3 · ¿Cuánto vale este diamante?

⭐⭐ · 50 min · **regresión que se dobla** · practica S07 (lineal, transformación logarítmica, Ridge, variables de texto, error en euros)

## Qué construyes
- Un **tasador de diamantes** que dice un precio a partir del peso (quilates), el corte, el color y la pureza.
- Descubres cómo una **transformación (el logaritmo)** convierte una curva en una recta y baja el error a la mitad **sin cambiar de modelo**.

## Datos
- `diamantes.csv`: una **muestra al azar de 6 000 diamantes reales** (conjunto `diamonds`, de la librería ggplot2). Columnas: `carat` (peso), `cut` (corte), `color`, `clarity` (pureza), medidas `x`, `y`, `z` y `price` en dólares.
- Hay unas pocas filas con medidas **0**: son errores de medición.

## Paso a paso

1. **Carga y dibuja el precio frente al peso.** ¿Es una recta?

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/diamantes.csv"
df = pd.read_csv(URL)
print(df.shape, "· filas con alguna medida 0:", int(((df[["x", "y", "z"]] == 0).any(axis=1)).sum()))
plt.scatter(df["carat"], df["price"], s=4, alpha=0.4); plt.xlabel("quilates"); plt.ylabel("precio ($)"); plt.show()
```

2. **Limpia y prepara.** Quita las medidas imposibles. Después crea las columnas con **logaritmo** (el peso y el precio crecen «en porcentajes», no «a golpe de euros»).

```python
df = df[(df[["x", "y", "z"]] > 0).all(axis=1)].copy()
df["log_carat"] = np.log(df["carat"])
fig, ejes = plt.subplots(1, 2, figsize=(9, 3.2))
ejes[0].scatter(df["carat"], df["price"], s=4, alpha=0.4); ejes[0].set_title("peso y precio, como vienen")
ejes[1].scatter(df["log_carat"], np.log(df["price"]), s=4, alpha=0.4); ejes[1].set_title("con logaritmo en los dos"); plt.show()
```

3. **Separa y arma los dos juegos de variables.** Las medidas `x`, `y`, `z` son casi lo mismo que el peso: para la versión con logaritmo las quitamos.

```python
y = df["price"]
X = df.drop(columns="price")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)
cat = ["cut", "color", "clarity"]
num_original = ["carat", "depth", "table", "x", "y", "z"]
num_log = ["log_carat", "depth", "table"]

def construir(numericas, modelo, log_precio=False):
    prep = ColumnTransformer([("n", StandardScaler(), numericas), ("c", OneHotEncoder(drop="first"), cat)])
    pipe = Pipeline([("prep", prep), ("modelo", modelo)])
    return TransformedTargetRegressor(pipe, func=np.log, inverse_func=np.exp) if log_precio else pipe
```

4. **El duelo, en dólares.** Cada modelo, con validación cruzada sobre `train`.

```python
candidatos = {"Siempre la media (tonto)": construir(num_original, DummyRegressor()),
              "Lineal con el precio tal cual": construir(num_original, LinearRegression()),
              "Lineal con log(precio)": construir(num_original, LinearRegression(), log_precio=True),
              "Lineal con log(precio) y log(peso)": construir(num_log, LinearRegression(), log_precio=True),
              "Ridge con log y log": construir(num_log, Ridge(alpha=1.0), log_precio=True),
              "Bosque (referencia)": construir(num_original, RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=2))}
filas = {}
for nombre, m in candidatos.items():
    mae = -cross_val_score(m, X_tr, y_tr, cv=5, scoring="neg_mean_absolute_error")
    r2 = cross_val_score(m, X_tr, y_tr, cv=5, scoring="r2")
    filas[nombre] = {"error medio ($)": mae.mean(), "± ": mae.std(), "R²": r2.mean()}
pd.DataFrame(filas).T.round(3)
```

5. **Lee el modelo.** En la versión con logaritmo, cada coeficiente de una categoría se lee como **un porcentaje** (¿cuánto más cuesta un color `D` que uno `J` con el mismo peso y pureza?).

```python
ganador = construir(num_log, LinearRegression(), log_precio=True).fit(X_tr, y_tr)
lineal = ganador.regressor_
nombres = lineal[0].get_feature_names_out()
efecto = pd.Series((np.exp(lineal[1].coef_) - 1) * 100, index=[n.split("__")[1] for n in nombres])
efecto = efecto[efecto.index.str.startswith(("cut_", "color_", "clarity_"))]
print("Efecto aproximado en % sobre el precio, frente al grupo que falta en cada lista (corte Fair, color D, pureza I1):")
efecto.round(0).sort_values()
```

6. **El examen: una vez.**

```python
p = ganador.predict(X_te)
print(f"Error medio en el examen: {mean_absolute_error(y_te, p):.0f} $ (el precio medio es {y_te.mean():.0f} $) · R² {r2_score(y_te, p):.3f}")
pd.DataFrame({"precio real": y_te.values, "predicho": p.round(-1), "error": (p - y_te.values).round(-1)}).head(6)
```

## Tu app
- Un tasador que acepta las características de **un diamante**.

```python
def tasar(carat, cut, color, clarity, depth=61.8, table=57.0):
    fila = pd.DataFrame([dict(log_carat=np.log(carat), depth=depth, table=table, cut=cut, color=color, clarity=clarity)])
    return round(float(ganador.predict(fila)[0]), -1)

print(tasar(0.5, "Ideal", "E", "VS1"), "$ · medio quilate, buen corte")
print(tasar(1.0, "Good", "J", "SI2"), "$ · un quilate, de calidad modesta")
print(tasar(2.0, "Ideal", "D", "IF"), "$ · dos quilates, el mejor color y pureza (¿te lo crees? Mira el Extra)")
```

## Qué deberías ver
- **6 000 diamantes**, **4** con alguna medida a 0 (se quitan). La nube precio–peso **se curva**; con logaritmo en los dos ejes casi es una recta.
- Error medio con CV en `train`, en dólares: tonto **≈ 3 010** · lineal con el precio tal cual **≈ 737** (R² 0,92) · lineal con log(precio) **≈ 426** (R² 0,95) · log y log **≈ 413** (R² 0,96) · Ridge **≈ 417** · bosque **≈ 434** (R² 0,95).
- La lección: **cambiar la forma del problema** (logaritmo) bajó el error casi a la mitad. Un modelo lineal sencillo **empata o gana** al bosque.
- Ridge casi no cambia nada: con pocas variables y muchos datos no hace falta.
- Lectura en %: respecto al color `D`, el `J` cuesta ≈ **−40 %**, el `I` ≈ −31 %. Frente a pureza `I1`, la `IF` cuesta ≈ **+195 %**. El corte `Ideal` ≈ +20 % sobre `Fair`.
- Examen: error medio **≈ 381 $** sobre un precio medio de ≈ 3 900 $ (R² ≈ 0,97).
- App: medio quilate ≈ **1 760 $** · un quilate modesto ≈ **2 550 $** · dos quilates perfectos ≈ **33 800 $**, **mucho más que cualquier diamante de la muestra** (máx. ≈ 18 800 $): el modelo se pasa fuera de lo que ha visto.

## Extra 🔴
- Prueba `alpha` de **0,001** y de **100** en el Ridge: ¿cambia algo?, ¿cuándo notarías el Ridge?
- Añade `log_carat ** 2`: ¿mejora?
- Mira los 5 diamantes donde más falla el modelo: ¿qué tienen en común?
- El tercer caso de la app sale carísimo. Mira el **precio máximo** de `y_tr`: ¿por qué el modelo se pasa con las piedras extremas?

## Cuidado
- Es una muestra de **un conjunto concreto** de diamantes y de **precios en dólares** de hace años: no vale para tasar una joya real.
- Si un modelo con log(precio) predice mal los precios caros, **mira el error en dólares**, no solo el R².
