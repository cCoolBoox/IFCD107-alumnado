# Solucionario · cuadernos «en clase» del Sprint 6

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S06_01`, `S06_02`, `S06_03`, `S06_04`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S06_01 · Conocer los datos: pandas y exploración (EDA)

### A5 · EJERCICIO 1 de 4 — Cargar la tabla

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

### A8 · EJERCICIO 2 de 4 — Tasa de cancelación por depósito

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

### A10 · EJERCICIO 3 de 4 — Unir con las temporadas

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

### A12 · EJERCICIO 4 de 4 — Duplicados y nulos de país

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

---

## S06_02 · Limpieza de datos: encontrar defectos y sus causas

### Ejercicio 1 · Diagnóstico inicial

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

### Ejercicio 2 · Tipos incorrectos: números escritos como texto

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

### Ejercicio 3 · Fechas en formatos mezclados

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

### Ejercicio 5 · Valores imposibles y *outliers*

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

---

## S06_03 · Preprocesado y *pipelines* reproducibles

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

