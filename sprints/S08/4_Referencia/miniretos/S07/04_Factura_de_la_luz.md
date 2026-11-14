# ⚡ Miniapp 4 · ¿Cuánta luz gastará mi casa mañana?

⭐⭐ · 55 min · **una relación que no es recta** · practica S07 (regresión lineal frente a polinómica, sobreajuste, Ridge, kWh y euros)

## Qué construyes
- Un programa que **predice el consumo eléctrico diario** de una casa con placas solares, según el tiempo y quién está en casa.
- Ves con tus ojos cuándo **una recta se queda corta**, cuándo **una curva ayuda** y cuándo **demasiada curva se vuelve loca**.

## Datos
- `consumo_solar.csv`: 1 096 días (3 años) de una vivienda **inventada** en Tenerife: temperatura media, horas de sol, personas en casa, si es fin de semana, si se teletrabaja, producción de las placas y **consumo** del día en kWh.
- Objetivo: `consumo_kwh`. Se consume más con **mucho calor** (aire acondicionado) y también con **frío** (calefacción): la forma es una **U**.

## Paso a paso

1. **Carga y dibuja el consumo frente a la temperatura.**

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/consumo_solar.csv"
df = pd.read_csv(URL, parse_dates=["fecha"])
print(df.shape, "· consumo medio:", round(df["consumo_kwh"].mean(), 1), "kWh al día")
plt.scatter(df["temp_media"], df["consumo_kwh"], s=6, alpha=0.4)
plt.xlabel("temperatura media (°C)"); plt.ylabel("consumo (kWh)"); plt.title("¿Una recta?"); plt.show()
```

2. **Separa y prueba lo básico.** Una recta con todas las variables.

```python
variables = ["temp_media", "horas_sol", "personas_en_casa", "es_finde", "teletrabajo"]
X, y = df[variables], df["consumo_kwh"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)

def evaluar(modelo):
    mae = -cross_val_score(modelo, X_tr, y_tr, cv=5, scoring="neg_mean_absolute_error")
    r2 = cross_val_score(modelo, X_tr, y_tr, cv=5, scoring="r2")
    return round(mae.mean(), 2), round(r2.mean(), 3)

print("Siempre la media (tonto):", evaluar(DummyRegressor()))
print("Recta con todo:          ", evaluar(LinearRegression()))
```

3. **Dale curva a la temperatura.** El grado `2` añade `temp²`; el `3`, `temp³`… Solo la temperatura se curva; el resto sigue igual. Mira qué pasa al subir el grado.

```python
def con_curva(grado, modelo):
    prep = ColumnTransformer([("temp", make_pipeline(StandardScaler(), PolynomialFeatures(grado, include_bias=False), StandardScaler()), ["temp_media"])],
                             remainder=StandardScaler())
    return Pipeline([("prep", prep), ("modelo", modelo)])

grados = range(1, 11)
sin_ridge = [evaluar(con_curva(g, LinearRegression())) for g in grados]
con_ridge = [evaluar(con_curva(g, Ridge(alpha=10))) for g in grados]
tabla = pd.DataFrame({"error (sin Ridge)": [a for a, _ in sin_ridge], "error (con Ridge)": [a for a, _ in con_ridge]}, index=list(grados))
tabla.index.name = "grado"
tabla.plot(marker="o", logy=True, title="Error medio (kWh) según el grado de la curva"); plt.show()
tabla
```

4. **Elige el grado y compara con otros modelos.** El grado más sencillo que dé buen resultado gana.

```python
modelos = {"Siempre la media (tonto)": DummyRegressor(),
           "Recta": LinearRegression(),
           "Curva de grado 2": con_curva(2, LinearRegression()),
           "Curva de grado 2 con Ridge": con_curva(2, Ridge(alpha=10)),
           "Bosque (referencia)": RandomForestRegressor(n_estimators=200, min_samples_leaf=5, random_state=42, n_jobs=2)}
filas = {nombre: dict(zip(["error medio (kWh)", "R²"], evaluar(m))) for nombre, m in modelos.items()}
pd.DataFrame(filas).T
```

5. **Dibuja la curva ganadora.**

```python
campeon = con_curva(2, LinearRegression()).fit(X_tr, y_tr)
temps = np.linspace(df["temp_media"].min(), df["temp_media"].max(), 100)
fila_tipo = pd.DataFrame({"temp_media": temps, "horas_sol": df["horas_sol"].median(), "personas_en_casa": 3, "es_finde": 0, "teletrabajo": 0})
plt.scatter(df["temp_media"], df["consumo_kwh"], s=6, alpha=0.3)
plt.plot(temps, campeon.predict(fila_tipo), color="red", lw=2, label="curva de grado 2")
plt.xlabel("temperatura media (°C)"); plt.ylabel("consumo (kWh)"); plt.legend(); plt.show()
print("Temperatura con menor consumo previsto:", round(float(temps[np.argmin(campeon.predict(fila_tipo))]), 1), "°C")
```

6. **El examen: una vez**, y pásalo a euros (a 0,18 € el kWh).

```python
p = campeon.predict(X_te)
mae = mean_absolute_error(y_te, p)
print(f"Error medio en el examen: {mae:.2f} kWh ({mae * 0.18:.2f} € al día) · R² {r2_score(y_te, p):.3f}")
```

## Tu app
- Una función que prevé el consumo de un día y cuánto cuesta.

```python
def consumo(temp_media, horas_sol, personas_en_casa, es_finde, teletrabajo, euros_kwh=0.18):
    fila = pd.DataFrame([dict(temp_media=temp_media, horas_sol=horas_sol, personas_en_casa=personas_en_casa,
                              es_finde=es_finde, teletrabajo=teletrabajo)])
    kwh = float(campeon.predict(fila)[0])
    return f"{kwh:.1f} kWh → {kwh * euros_kwh:.2f} €"

print(consumo(22, 8, 3, 0, 0), "· día templado entre semana")
print(consumo(33, 11, 4, 1, 0), "· ola de calor en fin de semana")
print(consumo(14, 3, 4, 0, 1), "· día fresco y nublado con teletrabajo")
```

## Qué deberías ver
- 1 096 días, consumo medio **11,9 kWh al día**. La nube temperatura–consumo es **una U**: el mínimo está en torno a **20 °C**.
- CV en `train`: tonto **1,53 kWh** (R² 0) · recta con todo **1,17 kWh · R² 0,43** · curva de grado 2 **0,60 kWh · R² 0,88** · bosque **0,69 kWh · R² 0,82**.
- Por grados: el error baja de 1,17 (grado 1) a **0,60 (grado 2)** y casi no mejora después (0,57–0,59 hasta el 8). A partir del 9 **sin Ridge** sube (0,69 y 0,83 en el 10), mientras que **con Ridge** se queda en ≈ 0,58. **Gana el grado 2:** el más sencillo que da buen resultado.
- La curva roja tiene el mínimo en **≈ 20,4 °C**.
- Examen: **0,60 kWh de error medio (≈ 0,11 € al día)** · R² ≈ 0,87.
- App: día templado ≈ **9,5 kWh (1,72 €)** · ola de calor en fin de semana ≈ **26 kWh (4,68 €)** · día fresco y nublado con teletrabajo ≈ **15,4 kWh (2,78 €)**.

## Extra 🔴
- Prueba el grado **10** con y sin Ridge y compara el error: ¿qué hace el Ridge con los coeficientes que se disparan?
- Añade `produccion_solar_kwh` como variable: ¿mejora? ¿Tiene sentido usarla para **predecir mañana**?
- Mira los días con consumo > 25 kWh: ¿qué los distingue?

## Cuidado
- Una curva que se ajusta de maravilla a los datos de `train` puede **hacerlo fatal** en datos nuevos: por eso se mira la validación cruzada.
- Los datos son **inventados**: no sirven para estimar tu factura real.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

- **Extra 1 · Grado 10 con y sin Ridge:** **0,83 kWh (R² −2,6)** sin Ridge y **0,58 kWh (R² 0,89)** con Ridge. Los coeficientes de la curva llegan a **≈ 25** sin Ridge y se quedan en **≈ 1,2** con él: **Ridge frena los coeficientes que se disparan** (castiga los valores grandes) y evita el sobreajuste.
- **Extra 2 · `produccion_solar_kwh`:** error **0,60 → 0,60** (no mejora): ya está dentro de `horas_sol` (corr. **0,96**). Y **no tiene sentido** para predecir **mañana**: la producción de mañana **no se conoce hoy**; es la «trampa del futuro».
- **Extra 3 · Días con > 25 kWh:** solo **4 días**, de **ola de calor** (34 °C de media frente a 21,8) y casi todos en **fin de semana** (80 %). El modelo los ve poco: son **extremos raros**.
- **Para comentar:** el **grado 2** gana por ser **el más sencillo que da buen resultado**. La U (mínimo ≈ 20 °C) tiene sentido físico: calefacción en frío, aire acondicionado en calor.
- **Tarjeta de ejemplo:**
  - Mi app decide **cuántos kWh gastará la casa mañana** a partir de **temperatura, horas de sol, personas, fin de semana y teletrabajo**.
  - Antes de modelar tuve que **darme cuenta de que la relación con la temperatura es una U** y usar una curva de grado 2.
  - Acierta **±0,60 kWh (≈ 0,11 €/día)**, frente a **±1,53 kWh** del modelo tonto.
  - No debe usarse para **estimar mi factura real**: los datos son inventados y los extremos son raros.
