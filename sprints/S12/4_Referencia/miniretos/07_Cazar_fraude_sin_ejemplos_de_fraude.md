# 🕵️ Miniapp 7 · Cazar lo raro sin haber visto nunca un fraude

⭐⭐⭐ · 55 min · **autoencoder / detectar anomalías** · practica S12 (autoencoder, error de reconstrucción) y S07 (clases desiguales, AUC, AP)

## Qué construyes
- Un **autoencoder**: una red que aprende a **copiar compras normales** pasando por un cuello de botella pequeño. Si una compra rara no se deja copiar bien (**error alto**), es sospechosa.
- La red **solo ve compras normales** al entrenar: nunca un fraude. Después comparas su olfato con modelos más sencillos.

## Datos
- `fraude_tarjeta.csv`, el de S07: 20 000 compras **inventadas**, 1,5 % de fraudes. Aquí **no se usan las etiquetas para entrenar la red**, solo para ver cómo de bien lo hace.

## Paso a paso

1. **Carga y separa.** Entrenar (solo las normales), validar y examen.

```python
import warnings, os; warnings.filterwarnings("ignore"); os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score, precision_recall_curve

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/fraude_tarjeta.csv"
df = pd.read_csv(URL)
y = df["es_fraude"]
X = pd.get_dummies(df.drop(columns="es_fraude"), columns=["comercio"]).astype("float32")
X["importe"] = np.log1p(X["importe"])            # importes muy desiguales: usamos su logaritmo
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
Xa, Xv, ya, yv = train_test_split(X_tr, y_tr, test_size=0.2, random_state=42, stratify=y_tr)
normales = Xa[ya == 0]                            # ¡la red solo verá estas!
esc = StandardScaler().fit(normales)
print(len(normales), "compras normales para entrenar · fraudes que verá la red: 0")
print(f"En validación: {len(yv)} compras, {int(yv.sum())} fraudes · en el examen: {len(y_te)} y {int(y_te.sum())} (NO mirar)")
```

2. **El autoencoder.** Entra la compra (14 números), se comprime a 3 y se reconstruye. Aprende lo que **tienen en común las compras normales**.

```python
keras.utils.set_random_seed(0)
n = normales.shape[1]
auto = keras.Sequential([keras.layers.Input((n,)),
                         keras.layers.Dense(8, activation="relu"),
                         keras.layers.Dense(3, activation="relu"),       # el cuello de botella
                         keras.layers.Dense(8, activation="relu"),
                         keras.layers.Dense(n)])
auto.compile("adam", "mse")
Za = esc.transform(normales)
h = auto.fit(Za, Za, epochs=100, batch_size=64, validation_split=0.15, verbose=0,
             callbacks=[keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)])
plt.plot(h.history["loss"], label="entrenamiento"); plt.plot(h.history["val_loss"], "--", label="validación")
plt.xlabel("época"); plt.ylabel("error al copiar"); plt.legend(); plt.title("El autoencoder aprende a copiar lo normal"); plt.show()
print("Pesos de la red:", auto.count_params())

def rareza(datos):
    Z = esc.transform(datos)
    return ((auto.predict(Z, verbose=0) - Z) ** 2).mean(axis=1)           # error medio al copiar
```

3. **¿Se nota?** Mira el error de copia de las compras normales y de las fraudulentas.

```python
r = rareza(Xv)
print(f"Error medio al copiar: normales {r[yv.values == 0].mean():.2f} · fraudes {r[yv.values == 1].mean():.2f}")
plt.hist(np.log10(r[yv.values == 0]), bins=40, alpha=.6, density=True, label="normales")
plt.hist(np.log10(r[yv.values == 1]), bins=15, alpha=.6, density=True, label="fraudes")
plt.xlabel("log10 del error al copiar"); plt.legend(); plt.title("Los fraudes se copian peor"); plt.show()
```

4. **Compara con otros detectores** (en validación). El **tonto** puntúa al azar; el **«z máximo»** mira cuánto se aleja la compra de lo normal en su rasgo más raro; la **logística** sí ha visto fraudes (es la que **hace trampa** respecto al reto).

```python
rng = np.random.default_rng(0)
z_max = lambda datos: np.abs(esc.transform(datos)).max(axis=1)
logistica = LogisticRegression(max_iter=1000).fit(StandardScaler().fit(Xa).transform(Xa), ya)
puntuaciones = {
    "Al azar (tonto)": rng.random(len(yv)),
    "z máximo (lo más raro de la compra)": z_max(Xv),
    "Autoencoder (sin ver fraudes)": r,
    "Logística (viendo fraudes)": logistica.predict_proba(StandardScaler().fit(Xa).transform(Xv))[:, 1],
}
tabla = pd.DataFrame({k: {"AUC": roc_auc_score(yv, v), "AP": average_precision_score(yv, v)} for k, v in puntuaciones.items()}).T.round(3)
print(tabla)
```

5. **Elige el umbral con la validación.** Tienes personal para revisar, por ejemplo, **el 5 % de las compras**: fijamos el error que deja pasar al 95 %.

```python
umbral = float(np.quantile(r, 0.95))
aviso_v = r >= umbral
print(f"Umbral {umbral:.2f} → avisa del {aviso_v.mean():.0%} de las compras y caza {int((aviso_v & (yv.values == 1)).sum())} de {int(yv.sum())} fraudes de la validación")
```

6. **Examen, una vez.**

```python
r_te = rareza(X_te)
aviso = r_te >= umbral
vp = int((aviso & (y_te.values == 1)).sum()); fp = int((aviso & (y_te.values == 0)).sum())
print(f"Examen: avisa del {aviso.mean():.1%} de las compras · fraudes cazados {vp} de {int(y_te.sum())} · falsas alarmas {fp}")
print(f"AUC en el examen: {roc_auc_score(y_te, r_te):.3f} · AP: {average_precision_score(y_te, r_te):.3f}")
```

## Tu app
- Una función que recibe **una compra** y dice si hay que revisarla, con su «rareza» frente al umbral.

```python
def revisa(importe, hora, distancia_casa_km, es_extranjero, comercio, compras_ultima_hora, antiguedad_tarjeta_meses, pago_online):
    fila = pd.DataFrame([dict(importe=np.log1p(importe), hora=hora, distancia_casa_km=distancia_casa_km, es_extranjero=es_extranjero,
                              compras_ultima_hora=compras_ultima_hora, antiguedad_tarjeta_meses=antiguedad_tarjeta_meses, pago_online=pago_online)])
    for c in X.columns:
        if c.startswith("comercio_"): fila[c] = float(c == f"comercio_{comercio}")
    rr = float(rareza(fila[X.columns].astype("float32"))[0])
    return f"rareza {rr:.2f} (umbral {umbral:.2f}) → {'🚨 revisar' if rr >= umbral else '✅ normal'}"

print(revisa(35, 18, 3, 0, "supermercado", 1, 40, 0))
print(revisa(1200, 3, 4500, 1, "electronica", 4, 2, 1))
print(revisa(60, 15, 8, 0, "gasolinera", 0, 24, 0))
```
> Los nombres válidos de `comercio` son los de la columna del fichero: `print(df["comercio"].unique())`.

## Qué deberías ver
- ≈ 11 800 compras normales para entrenar, **0 fraudes**; en validación 46 fraudes entre 3 000 compras y en el examen 77 entre 5 000. La red tiene **305 pesos**: muy pequeña.
- Error medio al copiar: **normales ≈ 0,5, fraudes ≈ 1,7** (tres veces más). El histograma muestra las dos montañas solapadas, no separadas.
- Validación (AUC / AP): azar ≈ 0,49 / 0,015 · **z máximo 0,83 / 0,16** · **autoencoder 0,92 / 0,23** · **logística viendo fraudes 0,98 / 0,63**. La red **gana a lo simple, pero queda muy por debajo del supervisado**.
- Con el 5 % de revisiones: en validación caza 22 de 46 fraudes; **en el examen caza 34 de 77 (44 %) con ≈ 209 falsas alarmas**. El AUC del examen (≈ 0,84) es **menor** que el de validación (≈ 0,92): con solo 46 fraudes la validación es un número **inestable**.
- App: la compra normal sale ≈ 0,15–0,2 → ✅; la de 1 200 € a las 3 de la madrugada, a 4 500 km y con tarjeta nueva sale con una rareza enorme → 🚨.
- Lección: sin etiquetas, **lo raro es una pista, no una prueba**.

## Extra 🔴
- Cambia el cuello de botella de **3 a 1** o a **6** neuronas: ¿qué pasa con el AUC? ¿Y si lo haces **tan grande** que copie todo (14)?
- Entrena el autoencoder **con las compras normales + algún fraude** (el 1 %): ¿se «acostumbra» a lo raro?
- Calcula cuántos fraudes cazas si revisas el **1 %**, el **5 %** y el **10 %** de las compras.

## Cuidado
- **Raro no es lo mismo que fraude.** El autoencoder marca como sospechosa una compra legítima muy grande o muy lejana.
- Si tienes ejemplos etiquetados de fraude, **un modelo supervisado casi siempre cazará más**. El autoencoder vale cuando **no los tienes** o aparecen fraudes de un tipo nuevo.
- Los datos son inventados: con compras reales habría que cuidar la privacidad.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

#### Extra 1 · Cuello de botella de 1, 3, 6 y 14 (validación, AUC / AP)
- **Qué hacer:**
  1. Escribe una función que construya el autoencoder con el cuello de botella que quieras y mide AUC y AP en validación con `rareza`.
  2. Prueba 1, 3, 6 y 14. Mira que las capas de 8 de alrededor siguen comprimiendo.
```python
def autoencoder(cuello, datos=normales, semilla=0):
    keras.utils.set_random_seed(semilla)
    n = datos.shape[1]
    a = keras.Sequential([keras.layers.Input((n,)), keras.layers.Dense(8, activation="relu"), keras.layers.Dense(cuello, activation="relu"),
                          keras.layers.Dense(8, activation="relu"), keras.layers.Dense(n)])
    a.compile("adam", "mse")
    Z = esc.transform(datos)
    a.fit(Z, Z, epochs=100, batch_size=64, validation_split=0.15, verbose=0, callbacks=[keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)])
    return a

def notas_val(a):
    r = ((a.predict(esc.transform(Xv), verbose=0) - esc.transform(Xv)) ** 2).mean(axis=1)
    return round(roc_auc_score(yv, r), 3), round(average_precision_score(yv, r), 3)

for cuello in (1, 3, 6, 14):
    a = autoencoder(cuello)
    print(f"cuello {cuello:2d} · pesos {a.count_params()} · AUC / AP en validación {notas_val(a)}")
```
- **Qué sale y por qué:**
  - **1:** 0,915 / 0,263 (271 pesos).
  - **3 (la ficha):** 0,923 / 0,232 (305 pesos).
  - **6:** 0,936 / 0,266 (356 pesos).
  - **14:** **0,938 / 0,294** (492 pesos).
  - **Casi no cambia** (≈ 0,92–0,94); con 46 fraudes en validación **las diferencias son ruido**. Y **«tan grande que copie todo» no ha empeorado el AUC**: en esta red las capas de **8** neuronas de alrededor ya comprimen 14 → 8, así que **no puede copiar de verdad**. Para ver el efecto hay que subir **también** esas capas (por ejemplo, a 32). Buen momento para decir que **un experimento que no sale como se esperaba también enseña**.

#### Extra 2 · Con el 1 % de fraudes mezclados (118 casos)
- **Qué hacer:**
  1. Añade a `normales` un 1 % de fraudes de `Xa` (los que tienen `ya == 1`) y reentrena.
  2. Compara AUC y AP con los del autoencoder limpio.
```python
fraudes_entrenamiento = Xa[ya == 1]
k = int(0.01 * len(normales))
mezcla = pd.concat([normales, fraudes_entrenamiento.iloc[:k]])
print("fraudes añadidos:", min(k, len(fraudes_entrenamiento)), "de", len(mezcla), "compras")
print("con el 1 % de fraudes dentro · AUC / AP en validación:", notas_val(autoencoder(3, mezcla)))
```
- **Qué sale y por qué:**
  - AUC **0,929 / AP 0,264** frente a 0,923 / 0,232: **casi igual**. El autoencoder **apenas se «acostumbra»** porque 118 fraudes entre ≈ 12 000 normales **siguen siendo raros**. Con **más** fraudes mezclados sí perdería el efecto (lo raro dejaría de serlo).

#### Extra 3 · Revisar el 1 %, 5 % y 10 % (examen, 77 fraudes)
- **Qué hacer:**
  1. Calcula la rareza de la validación y del examen y fija el umbral con **la validación** (el cuantil que deje pasar a una persona el 1 %, 5 % o 10 %).
  2. Aplica ese umbral al examen y cuenta fraudes cazados y falsas alarmas.
```python
r_val, r_test = rareza(Xv), rareza(X_te)
for porcentaje in (0.01, 0.05, 0.10):
    umbral_p = np.quantile(r_val, 1 - porcentaje)
    aviso_p = r_test >= umbral_p
    print(f"revisas el {porcentaje:.0%}: cazas {int((aviso_p & (y_te.values == 1)).sum())} de {int(y_te.sum())} fraudes · falsas alarmas {int((aviso_p & (y_te.values == 0)).sum())}")
```
- **Qué sale y por qué:**
  - **1 %:** caza **15** (46 falsas alarmas).
  - **5 %:** caza **34 (44 %)** (209 falsas alarmas).
  - **10 %:** caza **42 (55 %)** (445 falsas alarmas).
  - Duplicar la revisión **no duplica los fraudes cazados**: cada euro de revisión **rinde menos**. El punto lo marca **lo que cuesta revisar**.

#### Para cerrar
- **Para comentar:** «**raro no es lo mismo que fraude**». El autoencoder (AUC 0,92) **gana a lo simple** (0,83) pero **queda lejos** de la logística que **sí vio fraudes** (0,98): **sin etiquetas, lo raro es una pista, no una prueba**.
- **Tarjeta de ejemplo:**
  - Mi IA decide **qué compras revisar** a partir de **lo raras que son frente a las compras normales**.
  - Se equivoca **cazando 34 de 77 fraudes (44 %)** con el 5 % de revisiones y **209 falsas alarmas**, frente a **≈ 4 de 77 (5 %)** que cazaría una revisión al azar.
  - Falla cuando **una compra legítima es muy grande o muy lejana**, o **aparece un fraude que se parece a una compra normal**.
  - No debe usarse para **bloquear una tarjeta**: solo para decidir **qué revisa una persona**; si hay ejemplos etiquetados, un modelo supervisado caza más.
