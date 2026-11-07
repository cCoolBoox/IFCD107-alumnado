# Solucionario · cuadernos completos («para casa») del Sprint 6

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S06_01` a `S06_04`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).

---

## S06_01 · Conocer los datos: pandas y exploración (EDA)

### A5 · EJERCICIO 1 de 6 — Cargar la tabla

> Carga `reservas_turisdata.csv` en un DataFrame llamado `df`
> (con las dos fechas parseadas) y guarda en `n_filas` y `n_columnas` sus dimensiones.

```python
df = pd.read_csv(ruta, parse_dates=["fecha_reserva", "fecha_llegada"])
n_filas, n_columnas = df.shape
```

**Valores que tienen que salir:**

```text
df: tabla de 6000 filas y 18 columnas
n_filas = 6000
n_columnas = 18
```

### A8 · EJERCICIO 2 de 6 — Tasa de cancelación por depósito

> Calcula `tasa_por_deposito`: la tasa de cancelación (media de `cancelada`)
> para cada valor de `deposito`, ordenada de mayor a menor.

```python
tasa_por_deposito = df.groupby("deposito")["cancelada"].mean().sort_values(ascending=False)
```

**Valores que tienen que salir:**

```text
tasa_por_deposito:
    deposito
    sin_deposito    0.5404
    parcial         0.4086
    total           0.2640
```

### A10 · EJERCICIO 3 de 6 — Unir con las temporadas

> Une `df` con `temporadas` por `mes_llegada` (unión `left`, para no perder
> reservas) y guarda el resultado en `df_temp`. Después calcula `tasa_por_temporada`.

```python
df_temp = df.merge(temporadas, on="mes_llegada", how="left")
tasa_por_temporada = df_temp.groupby("temporada")["cancelada"].mean()
```

**Valores que tienen que salir:**

```text
df_temp: tabla de 6000 filas y 20 columnas
tasa_por_temporada:
    temporada
    alta    0.4792
    baja    0.4384
```

### A13 · EJERCICIO 4 de 6 — Mediana de precio por tipo de habitación

> Calcula `mediana_por_tipo`: la mediana de `precio_noche` por `tipo_habitacion`.
> Luego dibuja un gráfico de barras con ella (título y ejes en español) y responde en la
> variable `tipo_mas_caro` (texto) cuál es el tipo con mediana más alta.

```python
mediana_por_tipo = df.groupby("tipo_habitacion")["precio_noche"].median().sort_values()
mediana_por_tipo.plot(kind="bar", color="#2a6f97")
plt.title("Precio mediano por tipo de habitación")
plt.xlabel("Tipo de habitación")
plt.ylabel("Precio mediano por noche (€)")
plt.show()
tipo_mas_caro = mediana_por_tipo.idxmax()
```

**Valores que tienen que salir:**

```text
mediana_por_tipo:
    tipo_habitacion
    estandar     77.60
    superior    105.71
    familiar    122.99
    suite       175.47
tipo_mas_caro = 'suite'
```

Y además dibuja un gráfico.

### A15 · EJERCICIO 5 de 6 — Variable más ligada a la cancelación

> Usando la matriz `corr`, guarda en `var_mas_ligada` el nombre de la variable
> (distinta de `cancelada`) con **mayor correlación absoluta** con `cancelada`.

```python
var_mas_ligada = corr["cancelada"].drop("cancelada").abs().idxmax()
```

**Valores que tienen que salir:**

```text
var_mas_ligada = 'antelacion_dias'
```

### A17 · EJERCICIO 6 de 6 — Duplicados y nulos de país

> Calcula `filas_duplicadas` (número de filas repetidas) y `pct_nulos_pais`
> (porcentaje de nulos de `pais_origen`, redondeado a 1 decimal).

```python
filas_duplicadas = int(df.duplicated().sum())
pct_nulos_pais = round(df["pais_origen"].isna().mean() * 100, 1)
```

**Valores que tienen que salir:**

```text
filas_duplicadas = 0
pct_nulos_pais = 2.3
```

### A18 · MINI-RETO — Tres hallazgos para el cliente

> Escribe en la lista `hallazgos` **tres frases** (texto) que un gerente de hotel entendería,
> apoyadas en lo que has visto (por ejemplo, sobre canales, depósitos, precios o temporada).
> Cada frase debe incluir al menos **una cifra** que hayas calculado.

```python
hallazgos = [
    f"Con depósito total cancela el {tasa_por_deposito['total']:.0%} de las reservas frente al {tasa_por_deposito['sin_deposito']:.0%} sin depósito.",
    f"La suite tiene el precio mediano más alto ({mediana_por_tipo['suite']:.0f} € por noche).",
    f"Las reservas en temporada alta cancelan un {tasa_por_temporada['alta']:.0%} frente a un {tasa_por_temporada['baja']:.0%} en baja.",
]
```

---

## S06_02 · Limpieza de datos: encontrar defectos y sus causas

### A5 · EJERCICIO 1 de 5 — Quitar duplicados

> Guarda en `n_duplicados` cuántas filas están repetidas y crea `d1`,
> una copia de `crudo` **sin duplicados** y con el índice reiniciado.

```python
n_duplicados = int(crudo.duplicated().sum())
d1 = crudo.drop_duplicates().reset_index(drop=True)
```

**Valores que tienen que salir:**

```text
n_duplicados = 45
d1: tabla de 1500 filas y 18 columnas
```

### A7 · EJERCICIO 2 de 5 — Precio como número

> Crea `d2` (copia de `d1`) donde `precio_noche` sea numérico (float),
> cambiando la coma por punto. Guarda en `nulos_precio` el número de nulos resultantes.

```python
d2 = d1.copy()
d2["precio_noche"] = pd.to_numeric(d2["precio_noche"].astype(str).str.replace(",", "."), errors="coerce")
nulos_precio = int(d2["precio_noche"].isna().sum())
```

**Valores que tienen que salir:**

```text
d2: tabla de 1500 filas y 18 columnas
nulos_precio = 79
```

### A9 · EJERCICIO 3 de 5 — Fechas como fechas

> Crea `d3` (copia de `d2`) con `fecha_reserva` y `fecha_llegada` como fechas
> (`datetime64`). Para `fecha_reserva` combina los dos formatos (pista: `iso.fillna(espanol)`).

```python
d3 = d2.copy()
d3["fecha_reserva"] = iso.fillna(espanol)
d3["fecha_llegada"] = pd.to_datetime(d3["fecha_llegada"], format="%Y-%m-%d")
```

**Valores que tienen que salir:**

```text
d3: tabla de 1500 filas y 18 columnas
```

### A11 · EJERCICIO 4 de 5 — Normalizar canal y país

> Normaliza `canal`: sin espacios sobrantes, en minúsculas y con `_` en lugar
> de espacios. Después normaliza `pais_origen` con el diccionario `equivalencias` para que
> queden solo los 8 valores válidos (`ES, UK, DE, NL, IT, FR, Nordicos, otros`).
> Guarda el resultado en `d4`.

```python
equivalencias = {"es": "ES", "españa": "ES", "uk": "UK", "reino unido": "UK", "de": "DE",
                 "nl": "NL", "it": "IT", "fr": "FR", "nordicos": "Nordicos", "otros": "otros"}
d4 = d3.copy()
d4["canal"] = d4["canal"].str.strip().str.lower().str.replace(" ", "_")
d4["pais_origen"] = d4["pais_origen"].str.strip().str.lower().map(equivalencias)
```

**Valores que tienen que salir:**

```text
d4: tabla de 1500 filas y 18 columnas
```

### A13 · EJERCICIO 5 de 5 — Valores imposibles a nulo

> Crea `d5` (copia de `d4`) aplicando estas reglas de negocio, convirtiendo
> en `np.nan` (no borrando filas) los valores que las incumplan:
> - `precio_noche` debe estar entre 20 y 1000 €,
> - `noches` debe estar entre 1 y 60.
> (La antelación negativa la trataremos en la sección 7, cruzándola con las fechas.)
> Guarda en `n_imposibles` cuántos valores has convertido en nulo en total.

```python
d5 = d4.copy()
antes = d5[["precio_noche", "noches"]].isna().sum().sum()
d5["precio_noche"] = d5["precio_noche"].where(d5["precio_noche"].between(20, 1000))
d5["noches"] = d5["noches"].where(d5["noches"].between(1, 60))
n_imposibles = int(d5[["precio_noche", "noches"]].isna().sum().sum() - antes)
```

**Valores que tienen que salir:**

```text
d5: tabla de 1500 filas y 18 columnas
n_imposibles = 14
```

### A16 · MINI-RETO — Tu función limpiar_reservas

> Junta todo lo anterior en una función que reciba el DataFrame crudo y devuelva **dos cosas**: la tabla limpia y un
> diccionario `resumen` que cuente lo que has cambiado (`filas_antes`, `duplicados_quitados`, `imposibles_a_nulo`,
> `antelaciones_recalculadas`, `filas_despues`). Debe ser **reproducible** (misma entrada → misma salida) y
> **no modificar** el original.
> Pasos: duplicados → precio a número → fechas → categorías → imposibles a nulo →
> antelación recalculada. Llámala así: `limpio, resumen = limpiar_reservas(crudo)`.

```python
def limpiar_reservas(tabla):
    t = tabla.copy()
    resumen = {"filas_antes": len(t)}
    t = t.drop_duplicates().reset_index(drop=True)
    resumen["duplicados_quitados"] = resumen["filas_antes"] - len(t)
    t["precio_noche"] = pd.to_numeric(t["precio_noche"].astype(str).str.replace(",", "."), errors="coerce")
    iso_ = pd.to_datetime(t["fecha_reserva"], format="%Y-%m-%d", errors="coerce")
    esp_ = pd.to_datetime(t["fecha_reserva"], format="%d/%m/%Y", errors="coerce")
    t["fecha_reserva"] = iso_.fillna(esp_)
    t["fecha_llegada"] = pd.to_datetime(t["fecha_llegada"], format="%Y-%m-%d")
    t["canal"] = t["canal"].str.strip().str.lower().str.replace(" ", "_")
    t["pais_origen"] = t["pais_origen"].str.strip().str.lower().map(equivalencias)
    nulos_antes = t[["precio_noche", "noches"]].isna().sum().sum()
    t["precio_noche"] = t["precio_noche"].where(t["precio_noche"].between(20, 1000))
    t["noches"] = t["noches"].where(t["noches"].between(1, 60))
    resumen["imposibles_a_nulo"] = int(t[["precio_noche", "noches"]].isna().sum().sum() - nulos_antes)
    antes = t["antelacion_dias"]
    t["antelacion_dias"] = (t["fecha_llegada"] - t["fecha_reserva"]).dt.days
    resumen["antelaciones_recalculadas"] = int((t["antelacion_dias"] != antes).sum())
    resumen["filas_despues"] = len(t)
    return t, resumen

limpio, resumen = limpiar_reservas(crudo)

# Comparación antes/después
comparacion = pd.DataFrame({
    "antes": [len(crudo), crudo.duplicated().sum(), crudo["canal"].nunique(), crudo["pais_origen"].nunique()],
    "después": [len(limpio), limpio.duplicated().sum(), limpio["canal"].nunique(), limpio["pais_origen"].nunique()],
}, index=["filas", "duplicados", "valores distintos de canal", "valores distintos de país"])
comparacion
```

**Tiene que salir:**

```text
                            antes  después
filas                        1545     1500
duplicados                     45        0
valores distintos de canal      9        4
valores distintos de país      12        8
```

---

## S06_03 · Preprocesado y *pipelines* reproducibles

### Ejercicio 1 · Separar entrenamiento y prueba

> Separa `X` e `y` en `X_train, X_test, y_train, y_test` con un 20 % para
> prueba, `random_state=SEMILLA` y estratificando por `y`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
```

**Valores que tienen que salir:**

```text
X_train: tabla de 1200 filas y 15 columnas
X_test: tabla de 300 filas y 15 columnas
y_train:
    1057    1
    975     1
    447     0
    575     0
    1210    0
    903     0
    439     0
    261     0
y_test:
    865     0
    1248    1
    361     1
    729     0
…
```

### Ejercicio 2 · Escalado

> Crea un `MinMaxScaler` llamado `esc_minmax`, ajústalo **solo con
> `X_train[["precio_noche"]].dropna()`** y guarda en `precio_test_esc` el precio de test
> transformado (rellena antes los nulos de test con la mediana de train: `mediana_precio`).

```python
esc_minmax = MinMaxScaler()
esc_minmax.fit(X_train[["precio_noche"]].dropna())
mediana_precio = X_train["precio_noche"].median()
precio_test_esc = esc_minmax.transform(X_test[["precio_noche"]].fillna(mediana_precio))
```

**Valores que tienen que salir:**

```text
mediana_precio = 93.65
```

### Ejercicio 3 · Codificación de categóricas

> Codifica `deposito` con un `OrdinalEncoder` que respete el orden
> `["sin_deposito", "parcial", "total"]`. Guarda el encoder en `ord_dep` y el resultado
> de train en `dep_train_cod`.

```python
ord_dep = OrdinalEncoder(categories=[["sin_deposito", "parcial", "total"]])
dep_train_cod = ord_dep.fit_transform(X_train[["deposito"]])
```

### Ejercicio 4 · `ColumnTransformer` y `Pipeline`: la receta completa

> Construye `preprocesado` (un `ColumnTransformer`) con dos ramas:
> `"num"` (imputador de mediana + `StandardScaler`) sobre `columnas_num`, y `"cat"`
> (imputador `most_frequent` + `OneHotEncoder(handle_unknown="ignore")`) sobre `columnas_cat`.

```python
preprocesado = ColumnTransformer([
    ("num", Pipeline([("imputar", SimpleImputer(strategy="median")),
                      ("escalar", StandardScaler())]), columnas_num),
    ("cat", Pipeline([("imputar", SimpleImputer(strategy="most_frequent")),
                      ("codificar", OneHotEncoder(handle_unknown="ignore"))]), columnas_cat),
])
matriz = preprocesado.fit_transform(X_train)
print("Columnas tras el preprocesado:", matriz.shape[1])
```

**Tiene que salir:**

```text
Columnas tras el preprocesado: 34
```

### Ejercicio 5 · `ColumnTransformer` y `Pipeline`: la receta completa

> Crea `modelo`, un `Pipeline` con los pasos `("prep", preprocesado)` y
> `("clf", LogisticRegression(max_iter=1000, random_state=SEMILLA))`. Ajústalo con train y
> guarda en `acc_test` su exactitud (`score`) en test.

```python
modelo = Pipeline([("prep", preprocesado),
                   ("clf", LogisticRegression(max_iter=1000, random_state=SEMILLA))])
modelo.fit(X_train, y_train)
acc_test = modelo.score(X_test, y_test)
print(f"Exactitud en test: {acc_test:.3f}  (referencia «siempre la clase mayoritaria»: {max(y_test.mean(), 1 - y_test.mean()):.3f})")
```

**Tiene que salir:**

```text
Exactitud en test: 0.680  (referencia «siempre la clase mayoritaria»: 0.530)
```

### Mini-reto · comprueba que tu pipeline es reproducible

> Un pipeline reproducible da **las mismas predicciones** si lo vuelves a ajustar con los
> mismos datos. Crea `modelo2` (otra instancia del mismo pipeline usando `clone`), ajústalo
> y guarda en `son_iguales` un booleano que diga si las predicciones de test coinciden con
> las de `modelo`.

```python
modelo2 = clone(modelo).fit(X_train, y_train)
son_iguales = bool(np.array_equal(modelo.predict(X_test), modelo2.predict(X_test)))
```

---

## S06_04 · scikit-learn básico: métricas y validación

### Ejercicio 1 · La API de scikit-learn y el *baseline*

> Crea `logistica`, un `Pipeline` con `hacer_preprocesado()` y
> `LogisticRegression(max_iter=1000)`. Ajústalo con train y guarda en `acc_logistica`
> la exactitud en test y en `mejora` la diferencia con `tonto.score(...)`.

```python
logistica = Pipeline([("prep", hacer_preprocesado()), ("clf", LogisticRegression(max_iter=1000))])
logistica.fit(X_train, y_train)
acc_logistica = logistica.score(X_test, y_test)
mejora = acc_logistica - tonto.score(X_test, y_test)
```

**Valores que tienen que salir:**

```text
acc_logistica = 0.6717
mejora = 0.1308
```

### Ejercicio 2 · Métricas: ¿cómo de bueno es?

> Entrena una regresión lineal para predecir `precio_noche` usando solo
> `tipo_habitacion` y `mes_llegada` (usa `hacer_preprocesado(num=["mes_llegada"], cat=["tipo_habitacion"])`).
> Con los datos de test, guarda `mae`, `rmse` y `r2`.

```python
Xp = df[["tipo_habitacion", "mes_llegada"]]
yp = df["precio_noche"]
Xp_tr, Xp_te, yp_tr, yp_te = train_test_split(Xp, yp, test_size=0.2, random_state=SEMILLA)
reg = Pipeline([("prep", hacer_preprocesado(num=["mes_llegada"], cat=["tipo_habitacion"])),
                ("reg", LinearRegression())]).fit(Xp_tr, yp_tr)
pred_p = reg.predict(Xp_te)
mae = mean_absolute_error(yp_te, pred_p)
rmse = mean_squared_error(yp_te, pred_p) ** 0.5
r2 = r2_score(yp_te, pred_p)
```

**Valores que tienen que salir:**

```text
mae = 11.849
rmse = 14.9267
r2 = 0.7991
```

### Ejercicio 3 · Sobreajuste y sesgo-varianza

> A partir de las listas `acc_te` y `profundidades`, guarda en `mejor_profundidad`
> la profundidad con mejor exactitud en test, y en `brecha_maxima` la diferencia
> (train − test) con profundidad 20 (`acc_tr[-1] - acc_te[-1]`).

```python
mejor_profundidad = list(profundidades)[int(np.argmax(acc_te))]
brecha_maxima = acc_tr[-1] - acc_te[-1]
print(f"Mejor profundidad en test: {mejor_profundidad} · brecha con profundidad 20: {brecha_maxima:.2f}")
```

**Tiene que salir:**

```text
Mejor profundidad en test: 4 · brecha con profundidad 20: 0.40
```

### Ejercicio 4 · Sobreajuste y sesgo-varianza

> Calcula `auc_cv`: el array de puntuaciones de validación cruzada de
> `logistica` con `scoring="roc_auc"` y el mismo `cv` (5 folds). Guarda su media en `auc_medio`.

```python
auc_cv = cross_val_score(logistica, X_train, y_train, cv=cv, scoring="roc_auc")
auc_medio = auc_cv.mean()
```

**Valores que tienen que salir:**

```text
auc_cv: array de forma (5,), empieza por [0.7415 0.7442 0.7584 0.7543 0.7757]
auc_medio = 0.7548
```

### Ejercicio 5 · Fuga de datos (*data leakage*)

> De la lista `candidatas`, indica en `columnas_con_fuga` (lista) cuáles **no
> se conocerían en el momento de hacer la reserva** y por tanto provocarían fuga.

```python
candidatas = {
    "antelacion_dias": "días entre reservar y llegar (se conoce al reservar)",
    "importe_devuelto": "euros reembolsados al cliente tras cancelar",
    "tarifa": "flexible o no reembolsable (se elige al reservar)",
    "fecha_cancelacion": "fecha en que el cliente canceló (vacía si no canceló)",
    "cancelaciones_previas": "cancelaciones de reservas anteriores del cliente",
}
columnas_con_fuga = ["importe_devuelto", "fecha_cancelacion"]
```

**Valores que tienen que salir:**

```text
columnas_con_fuga: list de 2 elementos, ['importe_devuelto', 'fecha_cancelacion']
```

### Ejercicio 6 · Partición temporal

> Usa `TimeSeriesSplit(n_splits=4)` sobre `Xo`, `yo` (ya ordenados por fecha)
> para calcular `auc_temporal`: array con la AUC ROC de cada corte (`scoring="roc_auc"`).

```python
auc_temporal = cross_val_score(mod_t, Xo, yo, cv=TimeSeriesSplit(n_splits=4), scoring="roc_auc")
```

**Valores que tienen que salir:**

```text
auc_temporal: array de forma (4,), empieza por [0.7451 0.7497 0.7563 0.7322]
```

### Mini-reto · tabla de resultados honesta

> Crea `resultados`, un DataFrame con una fila por modelo (`"baseline"`, `"logistica"`) y las
> columnas `auc_cv_media` y `auc_cv_desv` (validación cruzada de 5 folds sobre train, `roc_auc`).
> Para el baseline usa `DummyClassifier(strategy="prior")`. Añade una frase en `conclusion`
> que diga si compensa el modelo frente al baseline.

```python
base = Pipeline([("prep", hacer_preprocesado()), ("clf", DummyClassifier(strategy="prior"))])
punt = {"baseline": cross_val_score(base, X_train, y_train, cv=cv, scoring="roc_auc"),
        "logistica": cross_val_score(logistica, X_train, y_train, cv=cv, scoring="roc_auc")}
resultados = pd.DataFrame({m: {"auc_cv_media": p.mean(), "auc_cv_desv": p.std()} for m, p in punt.items()}).T.round(3)
conclusion = (f"La regresión logística logra AUC {resultados.loc['logistica', 'auc_cv_media']:.2f} frente a 0,50 del "
              "baseline: compensa, porque distingue reservas de riesgo.")
resultados
```

**Tiene que salir:**

```text
           auc_cv_media  auc_cv_desv
baseline          0.500        0.000
logistica         0.755        0.012
```

