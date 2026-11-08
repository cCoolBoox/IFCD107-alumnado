# Solucionario · cuadernos «en clase» del Sprint 8

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S08_01`, `S08_02`, `S08_03`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S08_01 · Árboles de decisión: sobreajuste, poda e importancia

### A4 · EJERCICIO 1 de 3 — La variable de la raíz y el número de hojas

> El árbol pequeño empieza preguntando por la variable que mejor separa. Guarda
> en `variable_raiz` el **nombre** de esa variable (pista: `arbol_peq.tree_.feature[0]` es el índice
> de la columna en `nombres`) y en `n_hojas` cuántas hojas tiene (`arbol_peq.get_n_leaves()`).

```python
variable_raiz = nombres[arbol_peq.tree_.feature[0]]
n_hojas = arbol_peq.get_n_leaves()
print("El árbol empieza preguntando por:", variable_raiz)
```

**Tiene que salir:**

```text
El árbol empieza preguntando por: num__antelacion_dias
```

### A5 · EJERCICIO 2 de 3 — El árbol libre memoriza

> Entrena `arbol_libre = DecisionTreeClassifier(random_state=SEMILLA)` (sin
> límites) con train. Guarda `auc_train_libre` y `auc_test_libre` (AUC con `predict_proba`)
> y `hojas_libre` (número de hojas).

```python
arbol_libre = DecisionTreeClassifier(random_state=SEMILLA).fit(Xtr, y_train)
auc_train_libre = roc_auc_score(y_train, arbol_libre.predict_proba(Xtr)[:, 1])
auc_test_libre = roc_auc_score(y_test, arbol_libre.predict_proba(Xte)[:, 1])
hojas_libre = arbol_libre.get_n_leaves()
print(f"Árbol libre: {hojas_libre} hojas · AUC train {auc_train_libre:.3f} · AUC test {auc_test_libre:.3f}")
```

**Tiene que salir:**

```text
Árbol libre: 1206 hojas · AUC train 1.000 · AUC test 0.587
```

### A7 · EJERCICIO 3 de 3 — Elegir la poda y medirla en test

> Con las listas `hojas_min` y `auc_cv_hojas`, guarda en `mejor_min_hoja` el valor
> con mejor AUC. Entrena `arbol_podado` con ese valor sobre train y guarda `auc_test_podado`
> (AUC en test).

```python
mejor_min_hoja = hojas_min[int(np.argmax(auc_cv_hojas))]
arbol_podado = DecisionTreeClassifier(min_samples_leaf=mejor_min_hoja, random_state=SEMILLA).fit(Xtr, y_train)
auc_test_podado = roc_auc_score(y_test, arbol_podado.predict_proba(Xte)[:, 1])
print(f"min_samples_leaf = {mejor_min_hoja} · AUC test: {auc_test_podado:.3f} (libre: {auc_test_libre:.3f}) · hojas: {arbol_podado.get_n_leaves()}")
```

**Tiene que salir:**

```text
min_samples_leaf = 80 · AUC test: 0.716 (libre: 0.587) · hojas: 46
```

---

## S08_02 · Random Forest: la sabiduría de muchos árboles

### A3 · EJERCICIO 1 de 2 — Bosque de 300 árboles frente a un árbol podado

> Entrena `bosque = RandomForestClassifier(n_estimators=300, min_samples_leaf=5,
> random_state=SEMILLA, n_jobs=2)` con train. Guarda `auc_test_bosque` (AUC en test con `predict_proba`) y
> el AUC en test del árbol podado de la práctica anterior (`DecisionTreeClassifier(min_samples_leaf=80,
> random_state=SEMILLA)`) en `auc_test_arbol`.

```python
bosque = RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2).fit(Xtr, y_train)
auc_test_bosque = roc_auc_score(y_test, bosque.predict_proba(Xte)[:, 1])
arbol = DecisionTreeClassifier(min_samples_leaf=80, random_state=SEMILLA).fit(Xtr, y_train)
auc_test_arbol = roc_auc_score(y_test, arbol.predict_proba(Xte)[:, 1])
print(f"Árbol podado: {auc_test_arbol:.3f} · Bosque de 300 árboles: {auc_test_bosque:.3f}")
```

**Tiene que salir:**

```text
Árbol podado: 0.716 · Bosque de 300 árboles: 0.734
```

### A5 · EJERCICIO 2 de 2 — Rendimientos decrecientes

> Con la lista `oob_auc`, guarda en `mejora_5_a_400` cuánto sube el AUC OOB al pasar de 5 a
> 400 árboles (`oob_auc[-1] - oob_auc[0]`) y en `mejora_100_a_400` lo que sube de 100 a 400 árboles.
> Fíjate en que la segunda es mucho menor: los rendimientos son decrecientes.

```python
mejora_5_a_400 = oob_auc[-1] - oob_auc[0]
mejora_100_a_400 = oob_auc[-1] - oob_auc[n_arboles.index(100)]
print(f"5 → 400 árboles: +{mejora_5_a_400:.3f} · 100 → 400 árboles: {mejora_100_a_400:+.3f}")
```

**Tiene que salir:**

```text
5 → 400 árboles: +0.103 · 100 → 400 árboles: +0.005
```

---

## S08_03 · Boosting: Gradient Boosting, XGBoost y LightGBM

### A3 · EJERCICIO 1 de 2 — El mejor número de árboles y cuánto cae el AUC

> Con la lista `auc_val_por_arbol`, guarda en `mejor_n_arboles` el número de árboles
> (empezando a contar en 1) con mejor AUC de validación, y en `caida_final` cuánto ha caído el AUC de
> validación con los 300 árboles respecto a ese máximo (valor positivo).

```python
mejor_n_arboles = int(np.argmax(auc_val_por_arbol)) + 1
caida_final = max(auc_val_por_arbol) - auc_val_por_arbol[-1]
print(f"Mejor nº de árboles: {mejor_n_arboles} · pérdida de AUC si seguimos hasta 300: {caida_final:.3f}")
```

**Tiene que salir:**

```text
Mejor nº de árboles: 12 · pérdida de AUC si seguimos hasta 300: 0.039
```

### A4 · EJERCICIO 2 de 2 — XGBoost con parada temprana

> Entrena `modelo_xgb = xgb.XGBClassifier(n_estimators=1000, learning_rate=0.05, max_depth=3,
> subsample=0.8, colsample_bytree=0.8, early_stopping_rounds=30, eval_metric="auc", random_state=SEMILLA, n_jobs=2)`
> con `Xfit, yfit` y `eval_set=[(Xval, yval)]` (usa `verbose=False`). Guarda `arboles_xgb`
> (`modelo_xgb.best_iteration`) y `auc_test_xgb` (AUC en test).

```python
modelo_xgb = xgb.XGBClassifier(n_estimators=1000, learning_rate=0.05, max_depth=3, subsample=0.8,
                               colsample_bytree=0.8, early_stopping_rounds=30, eval_metric="auc",
                               random_state=SEMILLA, n_jobs=2)
modelo_xgb.fit(Xfit, yfit, eval_set=[(Xval, yval)], verbose=False)
arboles_xgb = int(modelo_xgb.best_iteration)
auc_test_xgb = roc_auc_score(y_test, modelo_xgb.predict_proba(Xte)[:, 1])
print(f"XGBoost paró en {arboles_xgb} árboles · AUC test = {auc_test_xgb:.3f}")
```

**Tiene que salir:**

```text
XGBoost paró en 69 árboles · AUC test = 0.745
```

