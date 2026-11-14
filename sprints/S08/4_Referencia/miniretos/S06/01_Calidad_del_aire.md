# 🌫️ Miniapp 1 · ¿Cuánto benceno hay en el aire?

⭐⭐ · 55 min · **datos reales que faltan** · practica S06 (nulos, fechas, `Pipeline`, partición temporal)

## Qué construyes
- Un programa que **estima el benceno del aire** (un contaminante) a partir de sensores baratos.
- Descubres cómo se marcan los datos que faltan en el mundo real (**-200**) y por qué **no se puede mezclar el futuro con el pasado**.

## Datos
- `aire_calidad.csv`: una hora por fila, de marzo de 2004 a abril de 2005, en una ciudad italiana (UCI, datos reales). Viene **como lo exporta el aparato**: separado por `;`, con la coma como decimal, dos columnas vacías y filas en blanco.
- Objetivo: `C6H6(GT)` (benceno medido por un aparato de referencia, en µg/m³). Predictores: los sensores baratos `PT08.S1…S5`, temperatura `T`, humedad `RH` y `AH`.

## Paso a paso

1. **Carga como viene y arréglalo.** Hay filas y columnas vacías, y el `-200` significa «sin dato».

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/aire_calidad.csv"
df = pd.read_csv(URL, sep=";", decimal=",")
print("Al cargar:", df.shape)
df = df.dropna(how="all").loc[:, ~df.columns.str.startswith("Unnamed")]
df = df.replace(-200, np.nan)
print("Después de quitar filas y columnas vacías:", df.shape)
(df.isna().mean() * 100).round(1).sort_values(ascending=False).head(6).rename("% de datos que faltan")
```

2. **Pon bien las fechas y mira un patrón.**

```python
df["momento"] = pd.to_datetime(df["Date"] + " " + df["Time"].str.replace(".", ":", regex=False), format="%d/%m/%Y %H:%M:%S")
df["hora"] = df["momento"].dt.hour
df = df.sort_values("momento").reset_index(drop=True)
df.groupby("hora")["C6H6(GT)"].mean().plot(marker="o", title="Benceno medio por hora del día")
plt.xlabel("hora"); plt.show()
```

3. **Elige qué entra.** `NMHC(GT)` falta casi siempre: fuera. Los otros `(GT)` son aparatos de referencia caros: **no los tendremos en producción**, así que tampoco entran. Sin objetivo no se puede entrenar: esas filas se quitan. Mira también cuánto se parece cada sensor al benceno: **si uno se parece demasiado, sospecha**.

```python
objetivo = "C6H6(GT)"
sensores = ["PT08.S1(CO)", "PT08.S2(NMHC)", "PT08.S3(NOx)", "PT08.S4(NO2)", "PT08.S5(O3)", "T", "RH", "AH", "hora"]
datos = df.dropna(subset=[objetivo])
print(datos[sensores + [objetivo]].corr()[objetivo].round(2).drop(objetivo))
```

`PT08.S2(NMHC)` sale con una correlación casi perfecta: este sensor está **calibrado con el propio benceno**, es casi una copia. Con él, cualquier modelo saca un 100 % y no hemos aprendido nada. Lo dejamos fuera (en el Extra 🔴 puedes comprobarlo).

```python
variables = [v for v in sensores if v != "PT08.S2(NMHC)"]
X, y = datos[variables], datos[objetivo]
print(len(datos), "horas con benceno medido ·", int(X.isna().sum().sum()), "huecos en los sensores hoy (mañana puede haberlos: por eso el Pipeline)")
```

4. **Separa de dos formas.** Mezclar horas al azar es **mirar el futuro**; separar por fechas es lo que pasaría de verdad.

```python
corte = int(len(datos) * 0.8)
X_tr_t, X_te_t, y_tr_t, y_te_t = X.iloc[:corte], X.iloc[corte:], y.iloc[:corte], y.iloc[corte:]      # temporal: pasado → futuro
X_tr_a, X_te_a, y_tr_a, y_te_a = train_test_split(X, y, test_size=0.2, random_state=42)             # al azar
print("Temporal: entrena hasta", datos["momento"].iloc[corte - 1].date(), "· examen desde", datos["momento"].iloc[corte].date())
```

5. **El duelo, con los dos exámenes.** El relleno de los huecos (`mediana`) va **dentro** del `Pipeline`: así solo aprende de `train`.

```python
modelos = {
    "Siempre la media (tonto)": make_pipeline(SimpleImputer(strategy="median"), DummyRegressor()),
    "Regresión lineal": make_pipeline(SimpleImputer(strategy="median"), LinearRegression()),
    "Bosque": make_pipeline(SimpleImputer(strategy="median"), RandomForestRegressor(n_estimators=200, min_samples_leaf=3, random_state=42, n_jobs=2)),
}
filas = {}
for nombre, m in modelos.items():
    p_t = m.fit(X_tr_t, y_tr_t).predict(X_te_t)
    p_a = m.fit(X_tr_a, y_tr_a).predict(X_te_a)
    filas[nombre] = {"MAE temporal": mean_absolute_error(y_te_t, p_t), "R² temporal": r2_score(y_te_t, p_t),
                     "MAE al azar": mean_absolute_error(y_te_a, p_a), "R² al azar": r2_score(y_te_a, p_a)}
pd.DataFrame(filas).T.round(2)
```

6. **Escribe tu hallazgo** (en la hoja del equipo): ¿qué examen da mejor nota?, ¿cuál es el **honesto** y por qué? ¿Gana el bosque a la lineal en los dos?

## Tu app
- Una función que estima el benceno de **una hora nueva**, aunque falle algún sensor (lo que falte lo rellena el `Pipeline`).

```python
final = modelos["Bosque"].fit(X_tr_t, y_tr_t)

def benceno(**lecturas):
    fila = pd.DataFrame([{v: lecturas.get(v, np.nan) for v in variables}])
    return round(float(final.predict(fila)[0]), 1)

print(benceno(**{"PT08.S1(CO)": 1200, "PT08.S3(NOx)": 900, "PT08.S4(NO2)": 1500, "PT08.S5(O3)": 1000, "T": 15, "RH": 50, "AH": 0.8, "hora": 8}), "µg/m³ con todos los sensores")
print(benceno(**{"PT08.S1(CO)": 1200, "T": 15, "hora": 8}), "µg/m³ con casi todos los sensores rotos")
```

## Qué deberías ver
- Al cargar: **9 471 filas × 17 columnas**; tras limpiar: **9 357 × 15**. `NMHC(GT)` falta un **90 %**; `CO(GT)`, un 18 %.
- `PT08.S2(NMHC)` se parece al benceno un **0,98**: sospechosa. Quedan **8 991 horas** para trabajar.
- Examen **temporal**: lineal **MAE ≈ 2,0 · R² ≈ 0,86**; bosque **MAE ≈ 2,0 · R² ≈ 0,85**; el tonto, R² negativo.
- Examen **al azar**: el bosque «mejora» a **MAE ≈ 0,8 · R² ≈ 0,97**. Es la trampa: parece que acierta más, pero ha visto horas vecinas de las que examina. **Manda el temporal.**
- Con `PT08.S2(NMHC)` dentro, el bosque saca R² = 1,00. Demasiado bueno para ser verdad.
- La app da ≈ 8,4 µg/m³ con todos los sensores y ≈ 8,5 con casi todos rotos (el `Pipeline` rellena).

## Extra 🔴
- Vuelve a meter `PT08.S2(NMHC)`: ¿qué nota sacan los modelos?, ¿te lo creerías?
- Prueba **otro relleno** (`mean` o un valor fijo): ¿cambia algo?
- Añade el **día de la semana** como variable: ¿mejora el examen temporal?
- ¿Qué pasa si quitas `hora`?

## Cuidado
- Son datos de **un sitio y un año**: no sirven para estimar el aire de Tenerife hoy.
- Un sensor que se estropea en silencio es un riesgo: hay que **vigilar** cuántos huecos llegan.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

- **Extra 1 · Volver a meter `PT08.S2(NMHC)`:**
  - Lineal **MAE 1,25 · R² 0,94** y bosque **MAE 0,01 · R² 1,00**.
  - ¿Te lo creerías? **No.** Es un sensor que mide casi lo mismo que el benceno (corr. 0,98): el modelo «copia» la respuesta. Hay que preguntar **«¿tendré ese dato cuando tenga que predecir?»** y **«¿mide lo mismo que la respuesta?»**.
- **Extra 2 · Otro relleno (`mean` o valor fijo):** **no cambia nada** (lineal 1,97 · bosque 2,02, igual que con la mediana). Motivo: tras `dropna` en el objetivo, **no quedan huecos** en los sensores (0 de 8 991 filas). El `Pipeline` es un **seguro para mañana**, no para estos datos.
  - Para comentar: es normal que un cambio **no tenga efecto**; saber **por qué** es lo importante.
- **Extra 3 · Día de la semana:** lineal 1,93 · bosque 2,04 (frente a 1,97 · 2,02): **no mejora**: los sensores ya recogen el ciclo semanal del tráfico.
- **Extra 4 · Quitar `hora`:** lineal 1,98 · bosque 2,09: **casi igual**: los sensores ya reflejan el ciclo del día. Una variable **redundante** se puede quitar y el modelo queda más simple.
- **Para comentar:** el examen **al azar** sale mejor (MAE ≈ 0,8) por **vecindad de horas**; el temporal es el honesto. Un **sensor que falla en silencio** exige vigilar cuántos huecos llegan.
- **Tarjeta de ejemplo:**
  - Mi app decide **cuántos µg/m³ de benceno hay** a partir de **8 sensores y la hora**.
  - Antes de modelar tuve que **tratar el −200 como hueco y quitar la columna que casi copiaba el benceno**.
  - Acierta **±2 µg/m³** en el examen temporal, frente a **≈ 6** del modelo tonto (siempre la media).
  - No debe usarse para **avisos de salud ni para otro lugar u otro año**.
