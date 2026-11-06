# Solucionario · cuadernos completos («para casa») del Sprint 7

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S07_01` a `S07_05`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).

---

## S07_01 · Regresión lineal y polinómica: predecir el precio por noche

### Ejercicio 1 · La idea: una recta (o un plano) que se ajusta a los datos

> Separa en `X_train, X_test, y_train, y_test` (20 % de test, `random_state=SEMILLA`),
> ajusta una `LinearRegression` llamada `modelo_lin` y guarda en `r2_test` y `mae_test` sus
> métricas en test.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA)
modelo_lin = LinearRegression().fit(X_train, y_train)
pred = modelo_lin.predict(X_test)
r2_test = r2_score(y_test, pred)
mae_test = mean_absolute_error(y_test, pred)
print(f"R² = {r2_test:.3f} · MAE = {mae_test:.2f} € · RMSE = {mean_squared_error(y_test, pred) ** 0.5:.2f} €")
```

**Tiene que salir:**

```text
R² = 0.915 · MAE = 7.24 € · RMSE = 9.70 €
```

### Ejercicio 2 · Interpretar los coeficientes

> Consulta `modelo_lin.coef_` (van en el mismo orden que las columnas de `X`).
> Guarda en `coefs` un `pd.Series` con los coeficientes y el nombre de columna como índice,
> y responde con números: `extra_suite` (euros extra de una suite frente a la estándar)
> y `efecto_temporada_alta` (euros extra por reservar en temporada alta).

```python
coefs = pd.Series(modelo_lin.coef_, index=X.columns)
extra_suite = coefs["tipo_habitacion_suite"]
efecto_temporada_alta = coefs["temporada_alta"]
print(coefs.round(1))
print("Ordenada en el origen (precio base de una estándar en temporada baja):", round(modelo_lin.intercept_, 1), "€")
```

**Tiene que salir:**

```text
tipo_habitacion_familiar     45.0
tipo_habitacion_suite       101.2
tipo_habitacion_superior     28.4
temporada_alta               22.4
dtype: float64
Ordenada en el origen (precio base de una estándar en temporada baja): 67.3 €
```

### Ejercicio 3 · Residuos: ¿el modelo se equivoca de forma "sana"?

> Calcula `mae_inter_test`: el MAE en test del modelo `con_interacciones`
> ajustado con `X_train, y_train`. Guarda en `mejora_mae` cuántos euros mejora respecto a
> `mae_test` (positivo = mejor).

```python
con_interacciones.fit(X_train, y_train)
mae_inter_test = mean_absolute_error(y_test, con_interacciones.predict(X_test))
mejora_mae = mae_test - mae_inter_test
```

**Valores que tienen que salir:**

```text
mae_inter_test = 6.7576
mejora_mae = 0.4812
```

### Ejercicio 4 · Polinomios para captar curvas... y su peligro

> Compara con validación cruzada (5 folds, `scoring="r2"`) sobre las habitaciones
> estándar dos formas de usar la época del año y guarda las medias en:
> - `r2_grado2`: polinomio de grado 2 sobre `mes_llegada` (con `make_pipeline(PolynomialFeatures(2), LinearRegression())`),
> - `r2_alta`: regresión lineal simple sobre la variable `temporada_alta` (una sola columna).

```python
r2_grado2 = cross_val_score(make_pipeline(PolynomialFeatures(2), LinearRegression()),
                            est[["mes_llegada"]], y_est, cv=5, scoring="r2").mean()
r2_alta = cross_val_score(LinearRegression(), est[["temporada_alta"]], y_est, cv=5, scoring="r2").mean()
print(f"Grado 2 sobre el mes: R² = {r2_grado2:.2f} · temporada_alta (1 columna): R² = {r2_alta:.2f}")
```

**Tiene que salir:**

```text
Grado 2 sobre el mes: R² = 0.09 · temporada_alta (1 columna): R² = 0.65
```

### Mini-reto · tarifa de referencia explicada al cliente

> Con `modelo_lin` (o `con_interacciones`), prepara la función `precio_recomendado(tipo, alta)`
> que devuelva el precio previsto (€) para un tipo de habitación (`"estandar"`, `"superior"`,
> `"suite"`, `"familiar"`) y un valor de `alta` (0 o 1). Usa `modelo_lin`.

```python
def precio_recomendado(tipo, alta):
    fila = pd.DataFrame([{c: 0 for c in X.columns}])
    if f"tipo_habitacion_{tipo}" in fila.columns:
        fila[f"tipo_habitacion_{tipo}"] = 1
    fila["temporada_alta"] = alta
    return float(modelo_lin.predict(fila)[0])
p_std_baja = precio_recomendado("estandar", 0)
p_suite_alta = precio_recomendado("suite", 1)
print(f"Estándar en baja: {p_std_baja:.0f} € · Suite en alta: {p_suite_alta:.0f} €")
```

**Tiene que salir:**

```text
Estándar en baja: 67 € · Suite en alta: 191 €
```

---

## S07_02 · Regularización: Ridge y Lasso

### Ejercicio 1 · El problema: muchas variables, pocos datos

> Guarda en `r2_train_ols` y `r2_test_ols` los R² de `ols` en train y test,
> y en `brecha_ols` su diferencia (train − test). ¿Es una brecha sana?

```python
r2_train_ols = ols.score(X_train, y_train)
r2_test_ols = ols.score(X_test, y_test)
brecha_ols = r2_train_ols - r2_test_ols
```

**Valores que tienen que salir:**

```text
r2_train_ols = 1.0
brecha_ols = 0.2842
```

### Ejercicio 2 · Elegir `alpha` con validación cruzada

> Crea `ridge` con `modelo_con(RidgeCV(alphas=np.logspace(-1, 4, 30)))` y ajústalo
> con train. Guarda en `alpha_ridge` el alpha elegido (`ridge[-1].alpha_`) y en `r2_test_ridge`
> su R² en test.

```python
ridge = modelo_con(RidgeCV(alphas=np.logspace(-1, 4, 30))).fit(X_train, y_train)
alpha_ridge = ridge[-1].alpha_
r2_test_ridge = ridge.score(X_test, y_test)
print(f"Ridge: alpha = {alpha_ridge:.1f} · R² test = {r2_test_ridge:.3f}")
```

**Tiene que salir:**

```text
Ridge: alpha = 25.9 · R² test = 0.728
```

### Ejercicio 3 · Lasso (L1): seleccionar variables

> Crea `lasso` con `modelo_con(LassoCV(cv=5, max_iter=50000, random_state=SEMILLA))`,
> ajústalo con train y guarda en `r2_test_lasso` su R² en test y en `n_no_cero` cuántos
> coeficientes son distintos de cero (`np.sum(lasso[-1].coef_ != 0)`).

```python
lasso = modelo_con(LassoCV(cv=5, max_iter=50000, random_state=SEMILLA)).fit(X_train, y_train)
r2_test_lasso = lasso.score(X_test, y_test)
n_no_cero = int(np.sum(lasso[-1].coef_ != 0))
print(f"Lasso: R² test = {r2_test_lasso:.3f} · coeficientes distintos de cero: {n_no_cero} de {lasso[-1].coef_.shape[0]}")

# ¿Qué variables ha conservado Lasso? (las de mayor peso)
nombres_poly = lasso[:-1].get_feature_names_out()
coef_lasso = pd.Series(lasso[-1].coef_, index=nombres_poly)
principales = coef_lasso[coef_lasso != 0].sort_values(key=np.abs, ascending=False).head(8)
principales.round(2)
```

**Tiene que salir:**

```text
Lasso: R² test = 0.887 · coeficientes distintos de cero: 27 de 665
```

### Mini-reto · ¿cuántos datos hacen falta?

> Repite el experimento con distintos tamaños de entrenamiento (`tamanos = [60, 120, 300, 1000]`)
> y guarda en la tabla `curva` el R² en test de la regresión sin regularizar y de Lasso
> (columnas `"ols"` y `"lasso"`, una fila por tamaño). Usa siempre las mismas 1000 reservas
> de evaluación (`X_eval`, `y_eval`) para comparar de forma justa.

```python
tamanos = [60, 120, 300, 1000]
X_res, X_eval, y_res, y_eval = train_test_split(X, y, test_size=1000, random_state=SEMILLA)
filas = {}
for n in tamanos:
    m_ols = modelo_con(LinearRegression()).fit(X_res.iloc[:n], y_res.iloc[:n])
    m_las = modelo_con(LassoCV(cv=5, max_iter=50000, random_state=SEMILLA)).fit(X_res.iloc[:n], y_res.iloc[:n])
    filas[n] = {"ols": m_ols.score(X_eval, y_eval), "lasso": m_las.score(X_eval, y_eval)}
curva = pd.DataFrame(filas).T.round(3)
curva
```

**Tiene que salir:**

```text
        ols  lasso
60    0.449  0.691
120   0.704  0.848
300  -1.062  0.913
1000  0.836  0.925
```

---

## S07_03 · Regresión logística: predecir cancelaciones

### Ejercicio 1 · Entrenar el modelo

> Crea `logit`, un `Pipeline` con el preprocesado que ves abajo (`prep`) y
> `LogisticRegression(max_iter=1000)`. Ajústalo con train y guarda en `proba_test` la
> probabilidad de cancelar (clase 1) de cada reserva de test.

```python
prep = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore", drop="if_binary"))]), columnas_cat),
])
logit = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))]).fit(X_train, y_train)
proba_test = logit.predict_proba(X_test)[:, 1]
```

### Ejercicio 2 · Interpretar: coeficientes y *odds ratios*

> A partir de `odds` (un `pd.Series` cuyo índice son los nombres de las
> variables), guarda en `or_no_reembolsable` el odds ratio de `cat__tarifa_no_reembolsable`
> y en `or_deposito_total` el de `cat__deposito_total`. Guarda en `mas_riesgo` el nombre de
> la variable con **mayor** odds ratio.

```python
or_no_reembolsable = odds["cat__tarifa_no_reembolsable"]
or_deposito_total = odds["cat__deposito_total"]
mas_riesgo = odds.idxmax()
print(f"Tarifa no reembolsable: los odds de cancelar se multiplican por {or_no_reembolsable:.2f}")
print(f"Depósito total: los odds de cancelar se multiplican por {or_deposito_total:.2f}")
```

**Tiene que salir:**

```text
Tarifa no reembolsable: los odds de cancelar se multiplican por 0.44
Depósito total: los odds de cancelar se multiplican por 0.46
```

### Ejercicio 3 · El umbral y la matriz de confusión

> Usando `metricas_umbral`, calcula sobre test (`y_test`, `proba_test`) las
> métricas con umbral 0,5 (`m05`) y con umbral 0,3 (`m03`). Guarda en `sube_recall` la
> diferencia de recall (`m03` − `m05`) y en `baja_precision` la de precisión (`m05` − `m03`).

```python
m05 = metricas_umbral(y_test, proba_test, 0.5)
m03 = metricas_umbral(y_test, proba_test, 0.3)
sube_recall = m03["recall"] - m05["recall"]
baja_precision = m05["precision"] - m03["precision"]
print(f"Con umbral 0,3 detectas {sube_recall*100:.0f} puntos más de las cancelaciones, pero tu precisión baja {baja_precision*100:.0f} puntos.")
```

**Tiene que salir:**

```text
Con umbral 0,3 detectas 26 puntos más de las cancelaciones, pero tu precisión baja 10 puntos.
```

### Ejercicio 4 · Elegir el umbral según el coste

> Prueba los umbrales `umbrales = np.arange(0.05, 0.96, 0.05)` sobre
> `proba_cv` / `y_train` con `coste_total` (pasándole `COSTE_FN` y `COSTE_FP`) y guarda en `mejor_umbral` el que
> da **menor coste**. Después calcula en `coste_test` el coste de ese umbral sobre test.

```python
umbrales = np.arange(0.05, 0.96, 0.05)
costes = [coste_total(y_train, proba_cv, u, COSTE_FN, COSTE_FP) for u in umbrales]
mejor_umbral = float(umbrales[int(np.argmin(costes))])
coste_test = coste_total(y_test, proba_test, mejor_umbral, COSTE_FN, COSTE_FP)
print(f"Umbral elegido: {mejor_umbral:.2f} · coste en test: {coste_test:.0f} (con 0,5: {coste_total(y_test, proba_test, 0.5, COSTE_FN, COSTE_FP):.0f})")

plt.figure(figsize=(7, 3.8))
plt.plot(umbrales, costes, marker="o", color="#2a6f97")
plt.axvline(mejor_umbral, color="#e63946", ls="--", label=f"Mínimo: {mejor_umbral:.2f}")
plt.title("Coste total según el umbral (FN cuesta 3 veces más que FP)")
plt.xlabel("Umbral de decisión")
plt.ylabel("Coste (unidades relativas)")
plt.legend()
plt.show()
```

**Tiene que salir:**

```text
Umbral elegido: 0.25 · coste en test: 577 (con 0,5: 813)
```

Y además dibuja un gráfico.

### Mini-reto · tabla para el gerente

> Construye `tabla_umbrales`, un DataFrame con **tres filas** (umbrales 0,5, 0,3 y el
> `mejor_umbral`) y las columnas `umbral`, `recall`, `precision` y `coste` medidas en **test**.
> Después escribe en `recomendacion` (texto) qué umbral propondrías y por qué, con al menos una cifra.

```python
filas = []
for u in [0.5, 0.3, mejor_umbral]:
    m = metricas_umbral(y_test, proba_test, u)
    filas.append({"umbral": round(u, 2), "recall": round(m["recall"], 3),
                  "precision": round(m["precision"], 3), "coste": coste_total(y_test, proba_test, u, COSTE_FN, COSTE_FP)})
tabla_umbrales = pd.DataFrame(filas)
recomendacion = (f"Recomiendo el umbral {mejor_umbral:.2f}: detecta el {tabla_umbrales.iloc[2]['recall']:.0%} de las "
                 "cancelaciones a cambio de más falsas alarmas, porque una habitación vacía cuesta más que una alerta innecesaria.")
tabla_umbrales
```

**Tiene que salir:**

```text
   umbral  recall  precision  coste
0    0.50   0.615      0.657  813.0
1    0.30   0.875      0.555  594.0
2    0.25   0.920      0.533  577.0
```

---

## S07_04 · Curvas ROC y PR, y qué hacer con clases desbalanceadas

### Ejercicio 1 · La paradoja de la exactitud

> Entrena un `DummyClassifier(strategy="most_frequent")` con train. Guarda en
> `acc_tonto` su exactitud en test y en `recall_tonto` su recall en test (`recall_score`).
> ¿Qué te dice?

```python
tonto = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
pred_tonto = tonto.predict(X_test)
acc_tonto = accuracy_score(y_test, pred_tonto)
recall_tonto = recall_score(y_test, pred_tonto)
print(f"Exactitud del modelo inútil: {acc_tonto:.1%} · recall: {recall_tonto:.0%}")
```

**Tiene que salir:**

```text
Exactitud del modelo inútil: 94.0% · recall: 0%
```

### Ejercicio 2 · Curva ROC y AUC

> Con `y_test` y `proba_base` calcula `fpr, tpr, _ = roc_curve(...)` y
> `auc = roc_auc_score(...)`.

```python
fpr, tpr, _ = roc_curve(y_test, proba_base)
auc = roc_auc_score(y_test, proba_base)

plt.figure(figsize=(5.5, 5))
plt.plot(fpr, tpr, color="#2a6f97", lw=2, label=f"Regresión logística (AUC = {auc:.2f})")
plt.plot([0, 1], [0, 1], "--", color="gray", label="Azar (AUC = 0,50)")
plt.title("Curva ROC")
plt.xlabel("Tasa de falsos positivos (falsas alarmas)")
plt.ylabel("Tasa de verdaderos positivos (recall)")
plt.legend(loc="lower right")
plt.show()
```

**Valores que tienen que salir:**

```text
auc = 0.7737
```

Y además dibuja un gráfico.

### Ejercicio 3 · Curva precisión–recall (PR) y *average precision*

> Guarda en `ap_base` la *average precision* de `proba_base`, y en `veces_mejor_que_azar`
> cuántas veces mejor es que la prevalencia (`ap_base / prevalencia`).

```python
ap_base = average_precision_score(y_test, proba_base)
veces_mejor_que_azar = ap_base / prevalencia
print(f"AP = {ap_base:.2f}: el modelo es {veces_mejor_que_azar:.1f} veces mejor que el azar en precisión.")
```

**Tiene que salir:**

```text
AP = 0.24: el modelo es 4.0 veces mejor que el azar en precisión.
```

### Ejercicio 4 · Tres remedios para el desbalance

> Crea `con_pesos = nuevo_modelo(class_weight="balanced")`, ajústalo con train y
> guarda en `recall_base` y `recall_pesos` el recall en test (umbral 0,5) del modelo base y del
> ponderado. Guarda también `precision_pesos`.

```python
con_pesos = nuevo_modelo(class_weight="balanced").fit(X_train, y_train)
recall_base = recall_score(y_test, base.predict(X_test))
recall_pesos = recall_score(y_test, con_pesos.predict(X_test))
precision_pesos = precision_score(y_test, con_pesos.predict(X_test))
print(f"Recall: {recall_base:.0%} → {recall_pesos:.0%} · precisión del ponderado: {precision_pesos:.0%}")
```

**Tiene que salir:**

```text
Recall: 3% → 73% · precisión del ponderado: 14%
```

### Ejercicio 5 · Submuestreo

> Crea `X_sub, y_sub` a partir **solo de train**: todas las positivas y
> una muestra aleatoria de negativas del **doble** de tamaño (`resample(..., replace=False,
> n_samples=..., random_state=SEMILLA)`). Entrena `con_submuestreo = nuevo_modelo()` con esos datos.

```python
pos_tr = X_train[y_train == 1]
neg_tr = X_train[y_train == 0]
neg_sub = resample(neg_tr, replace=False, n_samples=2 * len(pos_tr), random_state=SEMILLA)
X_sub = pd.concat([pos_tr, neg_sub])
y_sub = pd.Series([1] * len(pos_tr) + [0] * len(neg_sub), index=X_sub.index)
con_submuestreo = nuevo_modelo().fit(X_sub, y_sub)
```

**Valores que tienen que salir:**

```text
X_sub: tabla de 435 filas y 15 columnas
y_sub:
    24      1
    2014    1
    1389    1
    1616    1
    1089    1
    41      1
    1813    1
    2068    1
```

### Ejercicio 6 · Ajustar el umbral con la curva PR

> El gerente pide **detectar al menos el 70 % de las cancelaciones** con la mayor
> precisión posible. Con las probabilidades de validación cruzada de `base` sobre train (`proba_cv`),
> usa `precision_recall_curve` y guarda en `umbral_70` el **mayor umbral** cuyo recall sea ≥ 0,70.
> Después mide en `recall_test_70` y `precision_test_70` cómo funciona ese umbral en test.

```python
cv = StratifiedKFold(5, shuffle=True, random_state=SEMILLA)
proba_cv = cross_val_predict(nuevo_modelo(), X_train, y_train, cv=cv, method="predict_proba")[:, 1]
p_cv, r_cv, u_cv = precision_recall_curve(y_train, proba_cv)
umbral_70 = float(u_cv[r_cv[:-1] >= 0.70].max())
pred_70 = (proba_base >= umbral_70).astype(int)
recall_test_70 = recall_score(y_test, pred_70)
precision_test_70 = precision_score(y_test, pred_70)
print(f"Umbral {umbral_70:.3f}: recall en test {recall_test_70:.0%}, precisión {precision_test_70:.0%}")
```

**Tiene que salir:**

```text
Umbral 0.048: recall en test 82%, precisión 12%
```

### Mini-reto · comparativa de estrategias

> Crea `comparativa`, un DataFrame con una fila por estrategia (`"base"`, `"pesos"`, `"submuestreo"`)
> y las columnas `AUC`, `AP` (average precision, con probabilidades) y `recall` y `precision`
> (con umbral 0,5), todo en test. Redondea a 3 decimales. Guarda en `ganadora_ap` el nombre de la
> estrategia con mayor AP.

```python
modelos = {"base": base, "pesos": con_pesos, "submuestreo": con_submuestreo}
filas = {}
for nombre, m in modelos.items():
    p = m.predict_proba(X_test)[:, 1]
    yhat = m.predict(X_test)
    filas[nombre] = {"AUC": roc_auc_score(y_test, p), "AP": average_precision_score(y_test, p),
                     "recall": recall_score(y_test, yhat), "precision": precision_score(y_test, yhat, zero_division=0)}
comparativa = pd.DataFrame(filas).T.round(3)
ganadora_ap = comparativa["AP"].idxmax()
comparativa
```

**Tiene que salir:**

```text
               AUC     AP  recall  precision
base         0.774  0.242   0.032      0.667
pesos        0.770  0.245   0.726      0.136
submuestreo  0.752  0.241   0.452      0.172
```

---

## S07_05 · k vecinos (k-NN) y Naive Bayes

### Ejercicio 1 · k-NN: predecir mirando a los vecinos

> Guarda en `pct_antelacion_sin_escalar` y `pct_antelacion_escalada` el % de la
> distancia que aporta `antelacion_dias` (de las Series `sin_escalar` y `escalado`, en tanto por
> ciento). ¿Qué pasa con las demás variables cuando no se escala?

```python
pct_antelacion_sin_escalar = sin_escalar["antelacion_dias"] * 100
pct_antelacion_escalada = escalado["antelacion_dias"] * 100
print(f"Sin escalar, la antelación decide el {pct_antelacion_sin_escalar:.0f} % de la distancia; escalada, el {pct_antelacion_escalada:.0f} %.")
```

**Tiene que salir:**

```text
Sin escalar, la antelación decide el 77 % de la distancia; escalada, el 11 %.
```

### Ejercicio 2 · Elegir `k`

> Para cada `k` de la lista `ks`, calcula el AUC medio en validación cruzada
> (5 folds, `scoring="roc_auc"`) de un `Pipeline` con `prep_onehot()` y `KNeighborsClassifier(n_neighbors=k)`.
> Guarda las medias en la lista `auc_por_k` y el mejor valor de `k` en `mejor_k`.

```python
ks = [1, 5, 15, 31, 61, 101, 201, 401]
auc_por_k = []
for k in ks:
    modelo_k = Pipeline([("prep", prep_onehot()), ("knn", KNeighborsClassifier(n_neighbors=k))])
    auc_por_k.append(cross_val_score(modelo_k, X, y, cv=cv, scoring="roc_auc").mean())
mejor_k = ks[int(np.argmax(auc_por_k))]

plt.figure(figsize=(7, 3.8))
plt.plot(ks, auc_por_k, marker="o", color="#2a6f97")
plt.xscale("log")
plt.axvline(mejor_k, color="#e63946", ls="--", label=f"Mejor k = {mejor_k}")
plt.title("k-NN: AUC según el número de vecinos")
plt.xlabel("k (escala logarítmica)")
plt.ylabel("AUC medio en validación cruzada")
plt.legend()
plt.show()
```

**Valores que tienen que salir:**

```text
ks: list de 8 elementos, [1, 5, 15, 31, 61, 101]
auc_por_k: list de 8 elementos, [0.5848443621959879, 0.6451744563388256, 0.6895946033836353, 0.7074473958303531, 0.7218306741952256, 0.7319696264767561]
mejor_k = 201
```

Y además dibuja un gráfico.

### Ejercicio 3 · Naive Bayes: probabilidades multiplicadas

> Crea `nb_gauss`, un `Pipeline` con `prep_onehot()` y `GaussianNB()`. Guarda en
> `auc_nb_gauss` su AUC medio en validación cruzada (mismo `cv`).

```python
nb_gauss = Pipeline([("prep", prep_onehot()), ("nb", GaussianNB())])
auc_nb_gauss = cross_val_score(nb_gauss, X, y, cv=cv, scoring="roc_auc").mean()
```

**Valores que tienen que salir:**

```text
auc_nb_gauss = 0.719
```

### Ejercicio 4 · Naive Bayes: probabilidades multiplicadas

> `CategoricalNB` necesita números enteros. Crea `nb_cat`, un `Pipeline` con:
> - las numéricas → imputar mediana y `KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="quantile")`,
> - las categóricas → imputar moda y `OrdinalEncoder()`,
> - `CategoricalNB(min_categories=5)`.
> Guarda en `auc_nb_cat` su AUC medio en validación cruzada.

```python
prep_cat = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("bins", KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="quantile"))]), columnas_num),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("ord", OrdinalEncoder())]), columnas_cat),
])
nb_cat = Pipeline([("prep", prep_cat), ("nb", CategoricalNB(min_categories=5))])
auc_nb_cat = cross_val_score(nb_cat, X, y, cv=cv, scoring="roc_auc").mean()
print(f"AUC GaussianNB: {auc_nb_gauss:.3f} · CategoricalNB: {auc_nb_cat:.3f}")
```

**Tiene que salir:**

```text
AUC GaussianNB: 0.719 · CategoricalNB: 0.742
```

### Mini-reto · ¿qué modelo para el equipo de reservas?

> Crea la tabla `tabla` con una fila por modelo (`"logistica"`, `"knn"`, `"nb_gauss"`, `"nb_cat"`) y
> las columnas:
> - `auc_cv`: AUC medio (validación cruzada),
> - `segundos_ajuste`: tiempo en ajustar con todo `X_train` (`time.perf_counter()`),
> - `segundos_predecir`: tiempo en predecir las probabilidades de `X_test`.
> Usa `LogisticRegression(max_iter=1000)` y el mejor `k` de antes. Después, en `recomendacion`,
> escribe tu elección en 2 frases razonando con las tres columnas y con la **explicabilidad**.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEMILLA, stratify=y)
candidatos = {
    "logistica": Pipeline([("prep", prep_onehot()), ("clf", LogisticRegression(max_iter=1000))]),
    "knn": Pipeline([("prep", prep_onehot()), ("clf", KNeighborsClassifier(n_neighbors=mejor_k))]),
    "nb_gauss": nb_gauss,
    "nb_cat": nb_cat,
}
filas = {}
for nombre, m in candidatos.items():
    auc = cross_val_score(m, X, y, cv=cv, scoring="roc_auc").mean()
    t0 = time.perf_counter()
    m.fit(X_train, y_train)
    t1 = time.perf_counter()
    m.predict_proba(X_test)
    t2 = time.perf_counter()
    filas[nombre] = {"auc_cv": auc, "segundos_ajuste": t1 - t0, "segundos_predecir": t2 - t1}
tabla = pd.DataFrame(filas).T.round(3)
recomendacion = ("La regresión logística obtiene el mejor AUC y es la más explicable (odds ratio); k-NN guarda todos los "
                 "datos y es más lento al predecir, y Naive Bayes es rapidísimo pero algo peor. Elegiría la logística.")
tabla
```

**Tiene que salir:**

```text
           auc_cv  segundos_ajuste  segundos_predecir
logistica   0.757            0.084              0.008
knn         0.740            0.067              0.627
nb_gauss    0.719            0.045              0.010
nb_cat      0.742            0.048              0.014
```

