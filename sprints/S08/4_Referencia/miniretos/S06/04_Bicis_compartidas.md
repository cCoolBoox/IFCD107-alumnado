# 🚲 Miniapp 4 · ¿Cuántas bicis se alquilarán a las 8 de la mañana?

⭐⭐ · 55 min · **datos reales con fechas** · practica S06 (columnas trampa, fuga, partición temporal, línea base)

## Qué construyes
- Un programa que **predice cuántas bicis se alquilan en una hora** del día, según la hora, el día y el tiempo.
- Aprendes dos trampas a la vez: **una columna que ya contiene la respuesta** y **separar bien el pasado del futuro**.

## Datos
- `bicis_horas.csv`: **17 379 horas** del sistema de bicis compartidas de Washington D. C., de 2011 a 2012 (UCI, datos reales; licencia CC BY 4.0).
- Objetivo: `cnt`, bicis alquiladas esa hora.
- Columnas: `hr` (hora), `weekday`, `workingday`, `holiday`, `weathersit` (1 = despejado … 4 = tormenta), `temp`, `hum`, `windspeed`…
- Sospechosas: `casual` y `registered` (bicis de cada tipo de usuario), `instant` (el número de fila) y `dteday` (la fecha).

## Paso a paso

1. **Carga y mira.** Fíjate en `casual + registered`.

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/bicis_horas.csv"
df = pd.read_csv(URL, parse_dates=["dteday"])
print(df.shape, "· huecos:", int(df.isna().sum().sum()), "· del", df["dteday"].min().date(), "al", df["dteday"].max().date())
print("¿casual + registered = cnt en todas las filas?", bool((df["casual"] + df["registered"] == df["cnt"]).all()))
df.groupby("hr")["cnt"].mean().plot(marker="o", title="Bicis alquiladas por hora del día"); plt.show()
```

2. **Descarta lo que no existirá cuando predigas.** Si mañana quieres predecir las 8:00, **aún no sabrás** cuántos son «casuales» y cuántos «registrados»: esas columnas **son la respuesta partida en dos**. `instant` es solo un contador.

```python
fuga = ["casual", "registered", "instant", "dteday", "cnt"]
variables = [c for c in df.columns if c not in fuga]
print("Entran:", variables)
df = df.sort_values(["dteday", "hr"]).reset_index(drop=True)
```

3. **Separa por el calendario.** Entrena con el pasado (el 80 % más antiguo) y examina con el futuro.

```python
corte = int(len(df) * 0.8)
tr, te = df.iloc[:corte], df.iloc[corte:]
print("Entrena hasta", tr["dteday"].max().date(), "· examen desde", te["dteday"].min().date(), "·", len(te), "horas")
y_tr, y_te = tr["cnt"], te["cnt"]
```

4. **El duelo.** Primero el tonto y después dos modelos, **con y sin la columna trampa**.

```python
def probar(cols):
    modelos = {"Siempre la media (tonto)": DummyRegressor(),
               "Regresión lineal": make_pipeline(StandardScaler(), LinearRegression()),
               "Bosque": RandomForestRegressor(n_estimators=200, min_samples_leaf=3, random_state=42, n_jobs=2)}
    filas = {}
    for nombre, m in modelos.items():
        p = m.fit(tr[cols], y_tr).predict(te[cols])
        filas[nombre] = {"error medio (bicis)": mean_absolute_error(y_te, p), "R²": r2_score(y_te, p)}
    return pd.DataFrame(filas).T.round(2)

print("SIN trampa (lo honesto)")
print(probar(variables))
print("\nCON casual y registered (trampa)")
print(probar(variables + ["casual", "registered"]))
```

5. **Mira dónde falla.** El error depende de la hora: ¿falla más en las horas punta?

```python
modelo = RandomForestRegressor(n_estimators=200, min_samples_leaf=3, random_state=42, n_jobs=2).fit(tr[variables], y_tr)
te = te.assign(prediccion=modelo.predict(te[variables]))
te["error"] = (te["prediccion"] - te["cnt"]).abs()
te.groupby("hr")["error"].mean().plot(kind="bar", title="Error medio por hora"); plt.show()
print("Hora con más error:", int(te.groupby("hr")["error"].mean().idxmax()), "h")
```

## Tu app
- Una función que dice cuántas bicis esperar según la hora, el día y el tiempo.

```python
def bicis(hr, weekday, workingday, weathersit, temp_c, hum_pct, viento, mes=6, holiday=0):
    fila = pd.DataFrame([{"season": (mes % 12) // 3 + 1, "yr": 1, "mnth": mes, "hr": hr, "holiday": holiday, "weekday": weekday,
                          "workingday": workingday, "weathersit": weathersit, "temp": (temp_c + 8) / 47,
                          "atemp": (temp_c + 8) / 47, "hum": hum_pct / 100, "windspeed": viento / 67}])
    return round(float(modelo.predict(fila[variables])[0]))

print(bicis(8, 2, 1, 1, 22, 50, 10), "bicis un martes laborable a las 8:00, soleado")
print(bicis(8, 2, 1, 3, 12, 90, 25), "bicis ese mismo martes con lluvia")
print(bicis(14, 6, 0, 1, 25, 45, 8), "bicis un sábado a las 14:00")
```

## Qué deberías ver
- `casual + registered = cnt` en **todas** las filas: es la respuesta partida en dos.
- Entrenas hasta el **7 de agosto de 2012** y examinas con las **3 476 horas** siguientes.
- **Sin trampa**: tonto, error ≈ **175 bicis** (R² ≈ −0,1) · lineal **≈ 138** (R² ≈ 0,31) · bosque **≈ 46** (R² ≈ 0,90).
- **Con trampa**: lineal **0,00** y bosque **≈ 2,5** (R² = 1,00). Es perfecto porque **no predice nada**, solo suma.
- La lineal flojea porque la demanda por hora **no es una recta** (dos picos: ≈ 8 h y ≈ 17–18 h). El bosque lo capta.
- El bosque falla más a las **17 h**, una hora punta.
- App: ≈ **650** bicis un martes laborable soleado a las 8:00; ≈ **430** con lluvia; ≈ **580** un sábado a las 14:00.

## Extra 🔴
- Compara con una **separación al azar**: ¿sale mejor nota? ¿Por qué es engañosa?
- Quita `yr`: ¿qué pasa con el examen? (El sistema **crece** de un año a otro.)
- Prueba a predecir solo `registered` o solo `casual`: ¿cuál depende más de la hora?

## Cuidado
- Datos de **una ciudad y dos años**: no sirven para predecir las bicis de Santa Cruz.
- El sistema crece con el tiempo: un modelo así se debe **reentrenar** cada cierto tiempo.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

#### Extra 1 · Separación al azar
- **Qué hacer:**
  1. Separa **al azar** con `train_test_split` y entrena el mismo bosque.
  2. Compara con el temporal. Sale mejor al azar: pregúntate **por qué** (horas pegadas a las que ya vio).
```python
from sklearn.model_selection import train_test_split
Xa, Xb, ya, yb = train_test_split(df[variables], df["cnt"], test_size=0.2, random_state=42)   # al azar
def bosque(): return RandomForestRegressor(n_estimators=200, min_samples_leaf=3, random_state=42, n_jobs=2)
p_azar = bosque().fit(Xa, ya).predict(Xb)
p_temporal = bosque().fit(tr[variables], y_tr).predict(te[variables])
print("al azar:   ", round(mean_absolute_error(yb, p_azar), 1), "bicis · R²", round(r2_score(yb, p_azar), 2))
print("temporal:  ", round(mean_absolute_error(y_te, p_temporal), 1), "bicis · R²", round(r2_score(y_te, p_temporal), 2))
```
- **Qué sale y por qué:**
  - Bosque **MAE 25 · R² 0,94**, frente a **46 · 0,90** del temporal. Sale mejor por **engañosa**: examina horas pegadas a las que vio (9:00 con 8:00 y 10:00 en el entrenamiento) → **fuga de vecindad**.

#### Extra 2 · Quitar `yr`
- **Qué hacer:**
  1. Quita `yr` de la lista de variables y repite el examen temporal con el bosque.
```python
sin_yr = [c for c in variables if c != "yr"]
p = bosque().fit(tr[sin_yr], y_tr).predict(te[sin_yr])
print("sin yr:", round(mean_absolute_error(y_te, p), 1), "bicis · R²", round(r2_score(y_te, p), 2))
```
- **Qué sale y por qué:**
  - El bosque pasa de **46 a 86 bicis de error (R² 0,69)**. El sistema **crece de 2011 a 2012**: sin saber el año, el modelo no sabe que hay más bicis. Pero **`yr` no se puede extrapolar** a 2027 → motivo para **reentrenar**.

#### Extra 3 · `registered` y `casual`
- **Qué hacer:**
  1. Cambia el objetivo `cnt` por `registered` y luego por `casual` (siguen siendo variables prohibidas como entrada).
  2. Compara el error con la media de cada una y mira cuándo tienen su pico.
```python
for objetivo_nuevo in ("registered", "casual"):
    p = bosque().fit(tr[variables], tr[objetivo_nuevo]).predict(te[variables])
    por_hora = df.groupby("hr")[objetivo_nuevo].mean()
    print(f"{objetivo_nuevo}: error {mean_absolute_error(te[objetivo_nuevo], p):.1f} · media {te[objetivo_nuevo].mean():.1f} · horas pico {list(por_hora.sort_values(ascending=False).index[:3])}")
```
- **Qué sale y por qué:**
  - `registered`: MAE **42** sobre una media de 207 (R² 0,88).
  - `casual`: MAE **12** sobre una media de 42 (R² 0,85).
  - Los `registered` tienen picos a las **8 h y 17–18 h** (ir y volver del trabajo) y **bajan en fin de semana** (×0,74); los `casual` se concentran a las **14–15 h** y **se multiplican por 2,25 en fin de semana**. Los `registered` se predicen algo mejor (error del 20 % de la media frente al 28 % en `casual`).

#### Para cerrar
- **Para comentar:** la trampa de columnas (`casual + registered = cnt`) es la más fácil de **no ver**: errores de 0,00 son una **pista**, no un éxito.
- **Tarjeta de ejemplo:**
  - Mi app decide **cuántas bicis se alquilan en una hora** a partir de **hora, día, tiempo y temporada**.
  - Antes de modelar tuve que **quitar `casual` y `registered`, que suman la respuesta, y separar por fecha**.
  - Acierta **±46 bicis** en el examen, frente a **±175** del modelo tonto.
  - No debe usarse para **otra ciudad ni para años futuros sin reentrenar**.
