# 🚲 Miniapp 6 · ¿Cuántas bicis se alquilarán mañana?

⭐⭐⭐ · 55 min · **series temporales con red recurrente** · practica S12 (ventanas, GRU, separar por fecha, ganar a lo simple)

## Qué construyes
- Un programa que mira las **bicis alquiladas en los últimos 14 días** y predice **las de mañana**.
- Enfrentas una **red GRU** a modelos muy simples («mañana = hoy», «mañana = hace 7 días», una recta con los últimos días).
- Aprendes la regla de oro de las series: **el examen siempre es el futuro**.

## Datos
- `bicis_horas.csv`: el sistema de bicis compartidas de Washington D. C. (UCI, datos reales, CC BY 4.0) que ya conoces. Lo **sumamos por día**: ≈ 731 días (2011–2012).
- Objetivo: `cnt` total del día siguiente.

## Paso a paso

1. **Carga, suma por día y mira la serie.** Una serie tiene **orden**: no se puede barajar.

```python
import warnings, os; warnings.filterwarnings("ignore"); os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/bicis_horas.csv"
horas = pd.read_csv(URL, parse_dates=["dteday"])
dias = horas.groupby("dteday")["cnt"].sum()
print(len(dias), "días desde", dias.index[0].date(), "hasta", dias.index[-1].date())
dias.plot(figsize=(9, 3), title="Bicis alquiladas por día"); plt.show()
```

2. **Ventanas: 14 días → el día 15.** Y la **separación por fecha**: lo más antiguo para entrenar, lo siguiente para elegir, **lo último** para el examen. Nunca se mezclan.

```python
V = 14
serie = dias.values.astype("float32")
X = np.array([serie[i:i + V] for i in range(len(serie) - V)])
y = serie[V:]
fechas = dias.index[V:]
n = len(y); a, v = int(n * 0.6), int(n * 0.8)
Xa, ya = X[:a], y[:a]; Xv, yv = X[a:v], y[a:v]; Xte, yte = X[v:], y[v:]
print("entrenar:", fechas[0].date(), "→", fechas[a - 1].date())
print("validar: ", fechas[a].date(), "→", fechas[v - 1].date())
print("examen:  ", fechas[v].date(), "→", fechas[-1].date(), "(NO mirar)")
escala = Xa.mean()                              # solo con lo de entrenar
```

3. **Los modelos simples.** Si la red no les gana, no merece la pena.

```python
tabla = {}
tabla["Mañana = hoy"] = mean_absolute_error(yv, Xv[:, -1])
tabla["Mañana = hace 7 días"] = mean_absolute_error(yv, Xv[:, -7])
tabla["Media de la última semana"] = mean_absolute_error(yv, Xv[:, -7:].mean(axis=1))
lineal = Ridge(alpha=10).fit(Xa / escala, ya / escala)
tabla["Recta con los 14 días"] = mean_absolute_error(yv, lineal.predict(Xv / escala) * escala)
pd.Series(tabla).round(0)
```

4. **La red GRU.** Lee los 14 días en orden y predice el siguiente. Se repite con **3 semillas**.

```python
def gru(semilla):
    keras.utils.set_random_seed(semilla)
    m = keras.Sequential([keras.layers.Input((V, 1)), keras.layers.GRU(16), keras.layers.Dense(1)])
    m.compile("adam", "mae")
    m.fit((Xa / escala)[..., None], ya / escala, validation_data=((Xv / escala)[..., None], yv / escala),
          epochs=200, batch_size=32, verbose=0,
          callbacks=[keras.callbacks.EarlyStopping(patience=20, restore_best_weights=True)])
    return m

def predice(m, X): return m.predict((X / escala)[..., None], verbose=0).ravel() * escala

redes = [gru(s) for s in range(3)]
errores = [mean_absolute_error(yv, predice(m, Xv)) for m in redes]
print("GRU, error medio en la validación:", [round(e) for e in errores], "→ media", round(np.mean(errores)))
tabla["GRU (media de 3 semillas)"] = float(np.mean(errores))
resumen = pd.Series(tabla).sort_values().round(0)
print(resumen.to_string())
```

5. **Mira qué predice, no solo el número.** Real contra predicho en la validación.

```python
plt.figure(figsize=(9, 3))
plt.plot(fechas[a:v], yv, label="real")
plt.plot(fechas[a:v], Xv[:, -1], ":", label="mañana = hoy")
plt.plot(fechas[a:v], predice(redes[0], Xv), label="GRU")
plt.legend(); plt.title("Validación: lo que pasó y lo que dijo cada modelo"); plt.show()
```

6. **Examen, una vez, con el campeón** y comparado con «mañana = hoy».

```python
campeon = resumen.index[0]
if campeon == "Mañana = hoy": p = Xte[:, -1]
elif campeon == "Mañana = hace 7 días": p = Xte[:, -7]
elif campeon == "Media de la última semana": p = Xte[:, -7:].mean(axis=1)
elif campeon == "Recta con los 14 días": p = lineal.predict(Xte / escala) * escala
else: p = np.mean([predice(m, Xte) for m in redes], axis=0)
print(f"Campeón: {campeon}")
print(f"Examen → error medio {mean_absolute_error(yte, p):.0f} bicis · «mañana = hoy»: {mean_absolute_error(yte, Xte[:, -1]):.0f} · el día medio tiene {yte.mean():.0f}")
```

## Tu app
- Una función que recibe las bicis de los **últimos 14 días** y da la previsión de mañana con el modelo campeón.

```python
def prevision(ultimos_14_dias):
    x = np.array(ultimos_14_dias, dtype="float32")[None, :]
    if campeon == "Mañana = hoy": return float(x[0, -1])
    if campeon == "Mañana = hace 7 días": return float(x[0, -7])
    if campeon == "Media de la última semana": return float(x[0, -7:].mean())
    if campeon == "Recta con los 14 días": return float(lineal.predict(x / escala)[0] * escala)
    return float(np.mean([predice(m, x) for m in redes]))

ultimos = list(dias.values[-14:])
print("Últimos 14 días reales:", [int(u) for u in ultimos])
print(f"Previsión para mañana: {prevision(ultimos):.0f} bicis")
print(f"Si los últimos días fueran muy flojos: {prevision([1500] * 14):.0f} bicis")
print(f"Si los últimos días fueran muy altos: {prevision([6500] * 14):.0f} bicis")
```

## Qué deberías ver
- 731 días; entrenar hasta marzo de 2012, validar hasta agosto, examen de **agosto a diciembre de 2012**.
- Validación (error medio en bicis/día): **recta con los 14 días ≈ 800**, media de la semana ≈ 824, «mañana = hoy» ≈ 871, **GRU ≈ 973** (semillas ≈ 937–1 030), «hace 7 días» ≈ 1 094.
- **La red GRU pierde contra una recta con rezagos y contra «mañana = hoy».** Con ≈ 430 días para entrenar y una serie tan marcada por el tiempo que hace, una red recurrente no tiene datos para aprender más que lo simple.
- Examen con el campeón (recta): **≈ 878 bicis de error** frente a ≈ 891 de «mañana = hoy», con ≈ 5 900 bicis de media al día. **La ganancia sobre lo tonto es mínima** (≈ 1 %).
- App: con los últimos 14 días reales la previsión es ≈ 2 400 bicis; con 14 días a 1 500 da ≈ 1 700, y con 14 días a 6 500 da ≈ 6 300.
- Lección: parte de la variación diaria depende del **tiempo de mañana** y de si es laborable, que los 14 días no contienen (mira el Extra: ayuda, pero no lo arregla todo).

## Extra 🔴
- Añade como entrada **el tiempo de mañana** (temperatura, lluvia): el modelo sabe algo que los 14 días no cuentan. ¿Cambia el orden de la tabla?
- Prueba ventanas de **7** y de **28** días.
- Cambia `GRU(16)` por `LSTM(16)` o por `GRU(64)`: ¿cuántos pesos tiene cada uno y ayuda?

## Cuidado
- **Si mezclas los días al separar, haces trampa**: la red vería «el futuro» en el entrenamiento y el resultado sería falso.
- Es **una ciudad y dos años**: no sirve para predecir ninguna otra ciudad ni los próximos años.
- Las predicciones de series **fallan en los cambios bruscos** (tormenta, huelga, evento): nadie ve venir lo que los datos no cuentan.
