# 🚗 Miniapp 3 · ¿Cuánto vale este coche de segunda mano?

⭐⭐⭐ · 70 min · **datos muy sucios** · practica S06 (limpieza, duplicados, `Pipeline`, línea base, validación cruzada)

## Qué construyes
- Un **tasador de coches** de segunda mano a partir de anuncios escritos a mano, con todos sus despistes.
- Pasas la mayor parte del tiempo limpiando, que es **lo normal en un proyecto real**.

## Datos
- `coches_sucio.csv`: 1 245 anuncios inventados (marca, modelo, año, km, combustible, potencia, ciudad, precio). Están sucios **a propósito**.
- Objetivo: `precio` en euros.
- Defectos que verás (haz tu **inventario** antes de arreglar nada): mayúsculas y espacios en marcas, `VW`, puntos en `Toyota.`, combustible escrito de 10 maneras, la misma ciudad con 3 nombres, `km` como `15.215 km`, `179 mil` o `-1`, años como `19` o `2.013`, precios como `15.890 €`, `a consultar`, `1` o `9999999`, y **anuncios repetidos**.

## Paso a paso

1. **Mira cómo viene.** Aún no arregles nada: anota los problemas.

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/coches_sucio.csv"
df = pd.read_csv(URL)
print(df.shape, "· repetidos (sin contar el id):", df.drop(columns="id_anuncio").duplicated().sum())
print("marcas distintas:", df["marca"].nunique(), "· combustibles:", df["combustible"].nunique(), "· ciudades:", df["ciudad"].nunique())
print(df.isna().sum()[lambda s: s > 0].to_dict())
df.head(8)
```

2. **Limpia lo que no depende de los datos** (textos, formatos, repetidos). Esto se puede hacer antes de separar: no «aprende» nada. Los **repetidos hay que quitarlos antes de separar**, o un mismo coche caería en `train` y en `test`.

```python
d = df.drop_duplicates(subset=[c for c in df.columns if c != "id_anuncio"]).copy()

d["marca"] = d["marca"].str.strip().str.rstrip(".").str.title().replace({"Vw": "Volkswagen"})
d["combustible"] = (d["combustible"].str.lower().str.replace("é", "e").str.replace("í", "i")
                    .replace({"diesel": "diésel", "hibrido": "híbrido", "electrico": "eléctrico"}))
d["ciudad"] = (d["ciudad"].str.lower().replace({"s/c de tenerife": "santa cruz", "las palmas de gc": "las palmas"}).str.title())

def a_numero(x):
    if pd.isna(x): return np.nan
    t = str(x).lower().replace("km", "").replace("eur", "").replace("€", "").replace(",00", "").strip()
    if t.endswith("mil"): return float(t.replace("mil", "").strip()) * 1000
    try: return float(t.replace(".", ""))
    except ValueError: return np.nan

d["km"] = d["km"].map(a_numero)
d.loc[d["km"] < 0, "km"] = np.nan
d["precio"] = d["precio"].map(a_numero)

def arreglar_anio(a):
    if pd.isna(a): return np.nan
    if a < 10 and a % 1 != 0: return round(a * 1000)   # 2.013 → 2013 (el punto era de los miles)
    if a < 100: return 2000 + a                        # 19 → 2019 (año con dos cifras)
    return a
d["anio"] = d["anio"].map(arreglar_anio)

print(d.shape, "· años entre", d["anio"].min(), "y", d["anio"].max(), "· km máx.", d["km"].max())
print(d["marca"].unique(), d["combustible"].unique(), d["ciudad"].unique())
```

3. **Decide qué hacer con lo imposible.** Sin precio no podemos entrenar; un precio de `1 €` o de `9 999 999 €` es un error de escritura. Lo apuntamos en el diario de limpieza.

```python
antes = len(d)
d = d[d["precio"].between(500, 80000)]
print("anuncios quitados por precio imposible o sin precio:", antes - len(d), "· quedan", len(d))
d["precio"].describe().round(0)
```

4. **Separa y comprueba el modelo tonto.** Los huecos que quedan (`km`, `anio`, `combustible`, `potencia_cv`) se rellenan **dentro** del `Pipeline`.

```python
X = d.drop(columns=["precio", "id_anuncio"])
y = d["precio"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
num = ["anio", "km", "potencia_cv"]
cat = ["marca", "modelo", "combustible", "ciudad"]

def con_modelo(m):
    prep = ColumnTransformer([("num", SimpleImputer(strategy="median"), num),
                              ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")), ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat)])
    return Pipeline([("prep", prep), ("modelo", m)])

print("Un coche cualquiera, siempre la media de", round(y_tr.mean()), "€ → se equivoca de media", round(mean_absolute_error(y_te, [y_tr.mean()] * len(y_te))), "€")
```

5. **El duelo: validación cruzada en `train`.**

```python
modelos = {"Siempre la media (tonto)": DummyRegressor(),
           "Regresión con Ridge": Ridge(alpha=1.0),
           "Bosque": RandomForestRegressor(n_estimators=300, min_samples_leaf=2, random_state=42, n_jobs=2)}
for nombre, m in modelos.items():
    mae = -cross_val_score(con_modelo(m), X_tr, y_tr, cv=5, scoring="neg_mean_absolute_error")
    print(f"{nombre:26s} error medio {mae.mean():6.0f} € ± {mae.std():.0f}")
```

6. **El examen: una vez.** Elige el mejor y mide en euros.

```python
final = con_modelo(modelos["Bosque"]).fit(X_tr, y_tr)
p = final.predict(X_te)
print("Error medio en el examen:", round(mean_absolute_error(y_te, p)), "€")
pd.DataFrame({"real": y_te.values, "predicho": p.round(-1), "error €": (p - y_te.values).round(-1)}).head(6)
```

## Tu app
- Un tasador que acepta los datos de **un coche** (con la misma ortografía que dejó tu limpieza: `híbrido`, `Santa Cruz`…).

```python
def tasar(marca, modelo, anio, km, combustible, potencia_cv, ciudad):
    fila = pd.DataFrame([{"marca": marca, "modelo": modelo, "anio": anio, "km": km, "combustible": combustible,
                          "potencia_cv": potencia_cv, "ciudad": ciudad}])
    return round(float(final.predict(fila)[0]), -2)

print(tasar("Seat", "Ibiza", 2018, 80000, "gasolina", 95, "Telde"), "€")
print(tasar("Toyota", "Yaris", 2023, 15000, "híbrido", 100, "La Laguna"), "€")
print(tasar("Ford", "Kuga", 2010, 220000, "diésel", 150, "Arona"), "€")
```

## Qué deberías ver
- Al cargar: **1 245 filas**, **45 repetidas** (sin contar el id), **41 marcas distintas** que en realidad son 8, y 13 formas de escribir el combustible.
- Tras limpiar: **1 200 anuncios**, años entre **2008 y 2025**, 5 ciudades, 8 marcas.
- Quitas **32 anuncios** por precio imposible (`1 €`, `9 999 999 €`) o «a consultar»: quedan **1 168**.
- Error medio en euros, con CV en `train`: siempre la media **≈ 4 950 €** · Ridge **≈ 2 600 €** · bosque **≈ 800 €**.
- Examen: error medio **≈ 940 €** (el precio medio es ≈ 8 700 €). Un coche de 16 000 € puede fallar casi 3 000 €: mira dónde.
- Si dejas los repetidos **sin quitar antes de separar**, el examen sale algo más optimista (≈ 910 € en lugar de ≈ 940 €): el modelo ya vio esos coches. Poca diferencia aquí, pero con más repetidos sería grande.

## Extra 🔴
- Quita `ciudad`: ¿empeora? Si no, **descártala** y simplifica.
- Prueba `np.log(y)` como objetivo (después, deshaz con `np.exp`). ¿Baja el error en euros?
- Mira los 5 anuncios donde más falla el modelo: ¿hay algo raro en ellos?
- Escribe tu **diario de limpieza** en 8 líneas: qué defecto, cuántas filas, qué decidiste.

## Cuidado
- Los datos son **inventados**: el tasador no vale para comprar un coche de verdad.
- Quitar anuncios «imposibles» es una decisión. **Escríbela**, porque cambia el resultado.
