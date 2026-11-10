# Solucionario · cuadernos «en clase» del Sprint 7

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S07_01`, `S07_02`, `S07_03`, `S07_04`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S07_01 · Regresión lineal y polinómica: predecir el precio por noche

### A3 · EJERCICIO 1 de 3 — Ajustar la regresión lineal

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

### A5 · EJERCICIO 2 de 3 — Leer los coeficientes en euros

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
Ordenada en el origen (lo que predice el modelo para una estándar en temporada baja): 67.3 €
```

### A8 · EJERCICIO 3 de 3 — Error de las interacciones en test

> Calcula `mae_inter_test`: el MAE en test del modelo `con_interacciones`
> ajustado con `X_train, y_train`. Guarda en `mejora_mae` cuántos euros mejora respecto a
> `mae_test` (positivo = mejor).

```python
con_interacciones.fit(X_train, y_train)
mae_inter_test = mean_absolute_error(y_test, con_interacciones.predict(X_test))
mejora_mae = mae_test - mae_inter_test
```

**Tiene que salir:**

```text
MAE sin interacciones: 7.24 € · con interacciones: 6.76 € · mejora: 0.48 €
```

---

## S07_02 · Regularización: Ridge y Lasso

### A3 · EJERCICIO 1 de 3 — Medir la brecha de sobreajuste

> Guarda en `r2_train_ols` y `r2_test_ols` los R² de `ols` en train y test,
> y en `brecha_ols` su diferencia (train − test). ¿Es una brecha sana?

```python
r2_train_ols = ols.score(X_train, y_train)
r2_test_ols = ols.score(X_test, y_test)
brecha_ols = r2_train_ols - r2_test_ols
```

**Tiene que salir:**

```text
R² train = 1.000 · R² test = 0.716 · brecha = 0.284
```

### A5 · EJERCICIO 2 de 3 — Ridge con alpha elegido por validación cruzada

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

### A6 · EJERCICIO 3 de 3 — Lasso: seleccionar variables

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

---

## S07_03 · Regresión logística: predecir cancelaciones

### A3 · EJERCICIO 1 de 3 — Entrenar el modelo y obtener probabilidades

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

**Tiene que salir:**

```text
1200 probabilidades, de 0.03 a 0.99 · media = 0.466
```

### A5 · EJERCICIO 2 de 3 — Leer los odds ratio

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

### A7 · EJERCICIO 3 de 3 — Efecto de bajar el umbral

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

---

## S07_04 · Curvas ROC y PR, y qué hacer con clases desbalanceadas

### A3 · EJERCICIO 1 de 1 — Calcular la curva ROC y el AUC

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

**Tiene que salir:**

```text
AUC = 0.774
```

Y además dibuja un gráfico.

