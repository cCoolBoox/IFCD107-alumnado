# Solucionario · cuadernos completos («para casa») del Sprint 8

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S08_01` a `S08_05`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).
- El cuaderno del reto (`S08_06`) no se incluye(n): su solución se contrasta con la rúbrica del reto.

---

## S08_01 · Árboles de decisión: sobreajuste, poda e importancia

### A4 · EJERCICIO 1 de 4 — La variable de la raíz y el número de hojas

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

### A5 · EJERCICIO 2 de 4 — El árbol libre memoriza

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

### A7 · EJERCICIO 3 de 4 — Elegir la poda y medirla en test

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

### A9 · EJERCICIO 4 de 4 — Las tres variables más importantes

> Guarda en `top3` la lista de los **nombres** de las 3 variables más importantes de
> `arbol_podado` (usa la Series `importancias` ya ordenada) y en `suma_top3` cuánta importancia
> acumulan entre las tres.

```python
top3 = list(importancias.head(3).index)
suma_top3 = float(importancias.head(3).sum())
print("Top 3:", top3, f"· acumulan {suma_top3:.0%} de la importancia")
```

**Tiene que salir:**

```text
Top 3: ['num__antelacion_dias', 'cat__deposito_sin_deposito', 'cat__canal_directo'] · acumulan 70% de la importancia
```

### A11 · MINI-RETO — Reglas para el gerente

> Entrena `arbol_gerente = DecisionTreeClassifier(max_depth=3, min_samples_leaf=50, random_state=SEMILLA)`
> con train. Después escribe en la lista `reglas` **tres frases** en lenguaje de negocio (con cifras
> si puedes) que resuman lo que hace el árbol (mira `export_text`). Guarda su AUC en test en
> `auc_test_gerente`.

```python
arbol_gerente = DecisionTreeClassifier(max_depth=3, min_samples_leaf=50, random_state=SEMILLA).fit(Xtr, y_train)
auc_test_gerente = roc_auc_score(y_test, arbol_gerente.predict_proba(Xte)[:, 1])
print(export_text(arbol_gerente, feature_names=list(nombres)))
reglas = [
    "Si reservan con menos de unos 110 días de antelación y pagan algún depósito, casi nunca cancelan.",
    "Si reservan con poca antelación pero sin depósito y por una web intermediaria, el riesgo de cancelar es alto.",
    "Con más de unos 110 días de antelación, salvo en el canal directo, la mayoría acaba cancelando.",
]
```

**Tiene que salir:**

```text
|--- num__antelacion_dias <= 110.50
|   |--- cat__deposito_sin_deposito <= 0.50
|   |   |--- cat__deposito_parcial <= 0.50
|   |   |   |--- class: 0
|   |   |--- cat__deposito_parcial >  0.50
|   |   |   |--- class: 0
|   |--- cat__deposito_sin_deposito >  0.50
|   |   |--- cat__canal_web_intermediaria <= 0.50
|   |   |   |--- class: 0
|   |   |--- cat__canal_web_intermediaria >  0.50
|   |   |   |--- class: 1
|--- num__antelacion_dias >  110.50
|   |--- cat__canal_directo <= 0.50
|   |   |--- num__antelacion_dias <= 202.50
…
```

---

## S08_02 · Random Forest: la sabiduría de muchos árboles

### A3 · EJERCICIO 1 de 3 — Bosque de 300 árboles frente a un árbol podado

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

### A5 · EJERCICIO 2 de 3 — Rendimientos decrecientes

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

### A7 · EJERCICIO 3 de 3 — La variable principal y las irrelevantes

> Guarda en `variable_top` el nombre de la variable más importante según la permutación
> (Series `imp_perm`, ya ordenada) y en `n_irrelevantes` cuántas variables tienen una importancia media
> **menor de 0,002** (prácticamente nula).

```python
variable_top = imp_perm.index[0]
n_irrelevantes = int((imp_perm < 0.002).sum())
print(f"Variable más importante: {variable_top} · variables casi irrelevantes: {n_irrelevantes}")
```

**Tiene que salir:**

```text
Variable más importante: antelacion_dias · variables casi irrelevantes: 6
```

### A9 · MINI-RETO — Duelo: árbol, bosque y regresión logística

> Calcula con validación cruzada (5 folds, AUC, sobre **train**) el rendimiento de tres modelos y guárdalo
> en `duelo` (DataFrame, filas `"arbol"`, `"bosque"` y `"logistica"`; columnas `auc_media` y `auc_desv`).
> Para la logística usa un `Pipeline` con `StandardScaler` tras el mismo `prep` (o una versión con
> escalado). Guarda en `mejor_modelo` el nombre del ganador y escribe en `comentario` (texto) una
> frase sobre qué modelo elegirías teniendo en cuenta su explicabilidad.

```python
modelos = {
    "arbol": Pipeline([("prep", prep), ("m", DecisionTreeClassifier(min_samples_leaf=80, random_state=SEMILLA))]),
    "bosque": Pipeline([("prep", prep), ("m", RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2))]),
    "logistica": Pipeline([("prep", prep), ("esc", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]),
}
filas = {}
for nombre, m in modelos.items():
    p = cross_val_score(m, X_train, y_train, cv=cv, scoring="roc_auc")
    filas[nombre] = {"auc_media": p.mean(), "auc_desv": p.std()}
duelo = pd.DataFrame(filas).T.round(3)
mejor_modelo = duelo["auc_media"].idxmax()
comentario = ("El bosque supera con claridad al árbol, pero la regresión logística rinde igual o mejor y es mucho más "
              "explicable (odds ratio) y barata: en estos datos no compensa la complejidad del bosque.")
duelo
```

**Tiene que salir:**

```text
           auc_media  auc_desv
arbol          0.716     0.016
bosque         0.741     0.014
logistica      0.758     0.012
```

---

## S08_03 · Boosting: Gradient Boosting, XGBoost y LightGBM

### A3 · EJERCICIO 1 de 3 — El mejor número de árboles y cuánto cae el AUC

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

### A4 · EJERCICIO 2 de 3 — XGBoost con parada temprana

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

### A5 · EJERCICIO 3 de 3 — LightGBM con parada temprana

> Entrena `modelo_lgb = lgb.LGBMClassifier(n_estimators=1000, learning_rate=0.05, num_leaves=8,
> subsample=0.8, subsample_freq=1, colsample_bytree=0.8, random_state=SEMILLA, n_jobs=2, verbose=-1)` con
> `Xfit, yfit`, `eval_set=[(Xval, yval)]`, `eval_metric="auc"` y `callbacks=[lgb.early_stopping(30, verbose=False)]`.
> Guarda `arboles_lgb` (`modelo_lgb.best_iteration_`) y `auc_test_lgb`.

```python
modelo_lgb = lgb.LGBMClassifier(n_estimators=1000, learning_rate=0.05, num_leaves=8, subsample=0.8,
                                subsample_freq=1, colsample_bytree=0.8, random_state=SEMILLA, n_jobs=2, verbose=-1)
modelo_lgb.fit(Xfit, yfit, eval_set=[(Xval, yval)], eval_metric="auc",
               callbacks=[lgb.early_stopping(30, verbose=False)])
arboles_lgb = int(modelo_lgb.best_iteration_)
auc_test_lgb = roc_auc_score(y_test, modelo_lgb.predict_proba(Xte)[:, 1])
print(f"LightGBM paró en {arboles_lgb} árboles · AUC test = {auc_test_lgb:.3f}")
```

**Tiene que salir:**

```text
LightGBM paró en 49 árboles · AUC test = 0.745
```

### A7 · MINI-RETO — Comparar sklearn, XGBoost y LightGBM

> Crea `tabla`, un DataFrame con filas `"sklearn_gb"`, `"xgboost"` y `"lightgbm"` y columnas `auc_test`,
> `arboles` y `segundos_ajuste` (tiempo de `fit` medido con `time.perf_counter()`). Para
> `sklearn_gb` usa `GradientBoostingClassifier(learning_rate=0.05, max_depth=3, subsample=0.8,
> n_estimators=1000, n_iter_no_change=30, validation_fraction=0.2, random_state=SEMILLA)` sobre **todo** `Xtr`
> (esta versión también sabe parar antes: `n_estimators_` dice cuántos árboles usó). Para XGBoost y LightGBM
> reentrénalos con los mismos parámetros de los ejercicios (con `Xfit`/`Xval`) midiendo el tiempo.

```python
filas = {}
t0 = time.perf_counter()
gb2 = GradientBoostingClassifier(learning_rate=0.05, max_depth=3, subsample=0.8, n_estimators=1000,
                                 n_iter_no_change=30, validation_fraction=0.2, random_state=SEMILLA).fit(Xtr, y_train)
filas["sklearn_gb"] = {"auc_test": roc_auc_score(y_test, gb2.predict_proba(Xte)[:, 1]),
                       "arboles": int(gb2.n_estimators_), "segundos_ajuste": time.perf_counter() - t0}
t0 = time.perf_counter()
x2 = xgb.XGBClassifier(n_estimators=1000, learning_rate=0.05, max_depth=3, subsample=0.8, colsample_bytree=0.8,
                       early_stopping_rounds=30, eval_metric="auc", random_state=SEMILLA, n_jobs=2)
x2.fit(Xfit, yfit, eval_set=[(Xval, yval)], verbose=False)
filas["xgboost"] = {"auc_test": roc_auc_score(y_test, x2.predict_proba(Xte)[:, 1]),
                    "arboles": int(x2.best_iteration), "segundos_ajuste": time.perf_counter() - t0}
t0 = time.perf_counter()
l2 = lgb.LGBMClassifier(n_estimators=1000, learning_rate=0.05, num_leaves=8, subsample=0.8, subsample_freq=1,
                        colsample_bytree=0.8, random_state=SEMILLA, n_jobs=2, verbose=-1)
l2.fit(Xfit, yfit, eval_set=[(Xval, yval)], eval_metric="auc", callbacks=[lgb.early_stopping(30, verbose=False)])
filas["lightgbm"] = {"auc_test": roc_auc_score(y_test, l2.predict_proba(Xte)[:, 1]),
                     "arboles": int(l2.best_iteration_), "segundos_ajuste": time.perf_counter() - t0}
tabla = pd.DataFrame(filas).T
tabla["arboles"] = tabla["arboles"].astype(int)
tabla = tabla.round(3)
tabla
```

**Tiene que salir:**

```text
            auc_test  arboles  segundos_ajuste
sklearn_gb     0.744      139            1.403
xgboost        0.745       69            6.460
lightgbm       0.745       49            2.234
```

---

## S08_04 · Máquinas de vectores de soporte (SVM)

### A3 · EJERCICIO 1 de 4 — SVM lineal frente a SVM RBF en las dos lunas

> Entrena en `Xm_train, ym_train` una SVM lineal (`svm_lineal = SVC(kernel="linear", C=1)`) y una
> RBF (`svm_rbf = SVC(kernel="rbf", C=1, gamma=1)`). Guarda `acc_lineal` y `acc_rbf` (exactitud en
> `Xm_test, ym_test` con `.score`) y en `n_soporte_rbf` el número de vectores de soporte de la RBF
> (`svm_rbf.n_support_.sum()`).

```python
svm_lineal = SVC(kernel="linear", C=1).fit(Xm_train, ym_train)
svm_rbf = SVC(kernel="rbf", C=1, gamma=1).fit(Xm_train, ym_train)
acc_lineal = svm_lineal.score(Xm_test, ym_test)
acc_rbf = svm_rbf.score(Xm_test, ym_test)
n_soporte_rbf = int(svm_rbf.n_support_.sum())

fig, ejes = plt.subplots(1, 2, figsize=(11, 4))
dibujar_frontera(svm_lineal, ejes[0], f"Kernel lineal (exactitud test {acc_lineal:.2f})")
dibujar_frontera(svm_rbf, ejes[1], f"Kernel RBF (exactitud test {acc_rbf:.2f})")
plt.tight_layout()
plt.show()
```

**Valores que tienen que salir:**

```text
acc_lineal = 0.8083
acc_rbf = 0.9083
n_soporte_rbf = 91
```

Y además dibuja un gráfico.

### A6 · EJERCICIO 2 de 4 — El AUC con y sin escalado

> Crea `svm_rbf_res = Pipeline([("prep", prep_escalado()), ("svm", SVC(kernel="rbf", C=1))])` y
> `svm_rbf_sin = Pipeline([("prep", prep_sin_escalar()), ("svm", SVC(kernel="rbf", C=1))])`. Ajústalos con train
> y guarda `auc_con_escalado` y `auc_sin_escalado`: el AUC en test con `decision_function`.

```python
svm_rbf_res = Pipeline([("prep", prep_escalado()), ("svm", SVC(kernel="rbf", C=1))]).fit(X_train, y_train)
svm_rbf_sin = Pipeline([("prep", prep_sin_escalar()), ("svm", SVC(kernel="rbf", C=1))]).fit(X_train, y_train)
auc_con_escalado = roc_auc_score(y_test, svm_rbf_res.decision_function(X_test))
auc_sin_escalado = roc_auc_score(y_test, svm_rbf_sin.decision_function(X_test))
print(f"AUC con escalado: {auc_con_escalado:.3f} · sin escalar: {auc_sin_escalado:.3f}")
```

**Tiene que salir:**

```text
AUC con escalado: 0.735 · sin escalar: 0.671
```

### A8 · EJERCICIO 3 de 4 — Buscar los mejores C y gamma

> Crea `busqueda = GridSearchCV(Pipeline([("prep", prep_escalado()), ("svm", SVC(kernel="rbf"))]),
> rejilla, cv=cv, scoring="roc_auc")` y ajústala con `sub_X, sub_y`. Guarda `mejores_params`
> (`busqueda.best_params_`) y `mejor_auc_cv` (`busqueda.best_score_`).

```python
busqueda = GridSearchCV(Pipeline([("prep", prep_escalado()), ("svm", SVC(kernel="rbf"))]),
                        rejilla, cv=cv, scoring="roc_auc").fit(sub_X, sub_y)
mejores_params = busqueda.best_params_
mejor_auc_cv = busqueda.best_score_
print("Mejores parámetros:", mejores_params, f"· AUC CV = {mejor_auc_cv:.3f}")

resultados = pd.DataFrame(busqueda.cv_results_)
tabla_grid = resultados.pivot_table(index="param_svm__C", columns="param_svm__gamma", values="mean_test_score").astype(float)
plt.figure(figsize=(5.5, 3.8))
sns.heatmap(tabla_grid, annot=True, fmt=".3f", cmap="Blues", cbar_kws={"label": "AUC (validación cruzada)"})
plt.title("SVM RBF: AUC según C y gamma")
plt.xlabel("gamma")
plt.ylabel("C")
plt.show()
```

**Tiene que salir:**

```text
Mejores parámetros: {'svm__C': 10, 'svm__gamma': 0.003} · AUC CV = 0.752
```

Y además dibuja un gráfico.

### A10 · EJERCICIO 4 de 4 — Cuánto crece el tiempo con el número de filas

> Mide en `segundos` el tiempo de ajuste de `SVC(kernel="rbf", C=1, gamma=0.01)` sobre los
> datos ya preparados `Z` con `tamanos = [500, 1000, 2000, 4000]` (las primeras `n` filas de `Z`). Guarda
> en `factor_x4` cuántas veces más tarda con 4000 filas que con 1000 (`segundos[-1] / segundos[1]`).

```python
Z = prep_escalado().fit_transform(X_train)
yz = y_train.to_numpy()
tamanos = [500, 1000, 2000, 4000]
segundos = []
for n in tamanos:
    t0 = time.perf_counter()
    SVC(kernel="rbf", C=1, gamma=0.01).fit(Z[:n], yz[:n])
    segundos.append(time.perf_counter() - t0)
factor_x4 = segundos[-1] / segundos[1]
print("Segundos:", [round(s, 2) for s in segundos], f"· 4× filas → {factor_x4:.1f}× tiempo")
```

**Tiene que salir:**

```text
Segundos: [0.02, 0.05, 0.19, 0.84] · 4× filas → 16.9× tiempo
```

### A11 · MINI-RETO — Lineal, RBF por defecto y RBF ajustada

> Crea `tabla_svm`, un DataFrame con filas `"lineal"`, `"rbf_defecto"` y `"rbf_ajustada"` y columnas
> `auc_test`, `n_soporte` (nº de vectores de soporte) y `segundos_ajuste`. Usa `prep_escalado()`;
> `rbf_defecto` es `SVC(kernel="rbf", C=1)` y `rbf_ajustada` usa los `mejores_params` de la búsqueda
> (recuerda quitar el prefijo `svm__`). Entrena todo con el train completo.

```python
C_aj = mejores_params["svm__C"]
g_aj = mejores_params["svm__gamma"]
variantes = {
    "lineal": SVC(kernel="linear", C=1),
    "rbf_defecto": SVC(kernel="rbf", C=1),
    "rbf_ajustada": SVC(kernel="rbf", C=C_aj, gamma=g_aj),
}
filas = {}
for nombre, svm in variantes.items():
    pipe = Pipeline([("prep", prep_escalado()), ("svm", svm)])
    t0 = time.perf_counter()
    pipe.fit(X_train, y_train)
    seg = time.perf_counter() - t0
    filas[nombre] = {"auc_test": roc_auc_score(y_test, pipe.decision_function(X_test)),
                     "n_soporte": int(pipe["svm"].n_support_.sum()), "segundos_ajuste": seg}
tabla_svm = pd.DataFrame(filas).T
tabla_svm["n_soporte"] = tabla_svm["n_soporte"].astype(int)
tabla_svm = tabla_svm.round(3)
tabla_svm
```

**Tiene que salir:**

```text
              auc_test  n_soporte  segundos_ajuste
lineal           0.743       3327            2.359
rbf_defecto      0.735       3515            1.586
rbf_ajustada     0.744       3374            1.157
```

---

## S08_05 · Buscar buenos hiperparámetros: GridSearchCV y RandomizedSearchCV

### A3 · EJERCICIO 1 de 4 — GridSearchCV con un bosque

> Define un `Pipeline` `pipe_rf` con `prep` y `RandomForestClassifier(random_state=SEMILLA, n_jobs=2)`
> (paso llamado `"rf"`) y una rejilla. En un `Pipeline`, los hiperparámetros de un paso se escriben `paso__nombre`
> (por ejemplo `rf__max_depth`):
> - `n_estimators`: `[100, 200]`,
> - `max_depth`: `[4, 8]`,
> - `min_samples_leaf`: `[10, 40]`.
> Crea `busqueda_grid = GridSearchCV(pipe_rf, rejilla, cv=cv, scoring="roc_auc")`, ajústala con **train** y guarda
> en `n_combinaciones` cuántas combinaciones hay (con `len(busqueda_grid.cv_results_["params"])`) y en `mejor_auc_grid`
> su `best_score_`.

```python
pipe_rf = Pipeline([("prep", prep), ("rf", RandomForestClassifier(random_state=SEMILLA, n_jobs=2))])
rejilla = {"rf__n_estimators": [100, 200], "rf__max_depth": [4, 8], "rf__min_samples_leaf": [10, 40]}
t0 = time.perf_counter()
busqueda_grid = GridSearchCV(pipe_rf, rejilla, cv=cv, scoring="roc_auc").fit(X_train, y_train)
segundos_grid = time.perf_counter() - t0
n_combinaciones = len(busqueda_grid.cv_results_["params"])
mejor_auc_grid = busqueda_grid.best_score_
print(f"{n_combinaciones} combinaciones × 3 folds = {n_combinaciones * 3} entrenamientos en {segundos_grid:.0f} s")
print("Mejores parámetros:", busqueda_grid.best_params_, f"· AUC CV = {mejor_auc_grid:.3f}")
```

**Tiene que salir:**

```text
8 combinaciones × 3 folds = 24 entrenamientos en 18 s
Mejores parámetros: {'rf__max_depth': 8, 'rf__min_samples_leaf': 40, 'rf__n_estimators': 100} · AUC CV = 0.747
```

### A4 · EJERCICIO 2 de 4 — RandomizedSearchCV con LightGBM

> Crea `pipe_lgb` (`prep` + `lgb.LGBMClassifier(n_estimators=200, random_state=SEMILLA, n_jobs=2, verbose=-1)`,
> paso `"lgb"`) y una búsqueda `busqueda_rand = RandomizedSearchCV(pipe_lgb, distribuciones, n_iter=25, cv=cv,
> scoring="roc_auc", random_state=SEMILLA)` con estas `distribuciones`:
> - `lgb__learning_rate`: `loguniform(0.01, 0.3)`,
> - `lgb__num_leaves`: `randint(3, 40)`,
> - `lgb__min_child_samples`: `randint(10, 200)`,
> - `lgb__subsample`: `uniform(0.6, 0.4)` (equivale a valores entre 0,6 y 1,0; recuerda añadir `subsample_freq=1` al modelo).
> Ajústala con train y guarda `mejor_auc_rand` (`best_score_`).

```python
pipe_lgb = Pipeline([("prep", prep), ("lgb", lgb.LGBMClassifier(n_estimators=200, subsample_freq=1,
                                                                random_state=SEMILLA, n_jobs=2, verbose=-1))])
distribuciones = {"lgb__learning_rate": loguniform(0.01, 0.3), "lgb__num_leaves": randint(3, 40),
                  "lgb__min_child_samples": randint(10, 200), "lgb__subsample": uniform(0.6, 0.4)}
t0 = time.perf_counter()
busqueda_rand = RandomizedSearchCV(pipe_lgb, distribuciones, n_iter=25, cv=cv, scoring="roc_auc",
                                   random_state=SEMILLA).fit(X_train, y_train)
segundos_rand = time.perf_counter() - t0
mejor_auc_rand = busqueda_rand.best_score_
print(f"25 combinaciones aleatorias × 3 folds en {segundos_rand:.0f} s · AUC CV = {mejor_auc_rand:.3f}")
print("Mejores parámetros:", {k: round(v, 3) if isinstance(v, float) else v for k, v in busqueda_rand.best_params_.items()})
```

**Tiene que salir:**

```text
25 combinaciones aleatorias × 3 folds en 335 s · AUC CV = 0.749
Mejores parámetros: {'lgb__learning_rate': np.float64(0.019), 'lgb__min_child_samples': 199, 'lgb__num_leaves': 23, 'lgb__subsample': np.float64(0.755)}
```

### A5 · EJERCICIO 3 de 4 — Configuraciones empatadas: la regla del «1 error estándar»

> Con `resultados = pd.DataFrame(busqueda_rand.cv_results_)`, guarda en `top5` las 5 mejores
> filas (columnas `param_lgb__num_leaves`, `param_lgb__learning_rate`, `mean_test_score`, `std_test_score`,
> ordenadas por `mean_test_score` descendente), en `n_empatadas` cuántas combinaciones tienen una media dentro
> de **una desviación** (`std_test_score` de la mejor) de la mejor media, y en `mas_simple` el **menor**
> `num_leaves` entre esas empatadas.

```python
resultados = pd.DataFrame(busqueda_rand.cv_results_)
resultados_ord = resultados.sort_values("mean_test_score", ascending=False)
top5 = resultados_ord[["param_lgb__num_leaves", "param_lgb__learning_rate", "mean_test_score", "std_test_score"]].head(5)
mejor_fila = resultados_ord.iloc[0]
umbral_1se = mejor_fila["mean_test_score"] - mejor_fila["std_test_score"]
empatadas = resultados_ord[resultados_ord["mean_test_score"] >= umbral_1se]
n_empatadas = len(empatadas)
mas_simple = int(empatadas["param_lgb__num_leaves"].astype(int).min())
print(f"{n_empatadas} de 25 configuraciones están a menos de 1 error estándar de la mejor; la más sencilla usa {mas_simple} hojas.")
top5.round(3)

plt.figure(figsize=(7, 4))
plt.scatter(resultados["param_lgb__learning_rate"].astype(float), resultados["mean_test_score"], c=resultados["param_lgb__num_leaves"].astype(int),
            cmap="viridis", s=50)
plt.colorbar(label="num_leaves")
plt.xscale("log")
plt.title("LightGBM: AUC (validación cruzada) según learning_rate")
plt.xlabel("learning_rate (escala logarítmica)")
plt.ylabel("AUC medio en validación cruzada")
plt.show()
```

**Tiene que salir:**

```text
13 de 25 configuraciones están a menos de 1 error estándar de la mejor; la más sencilla usa 4 hojas.
```

Y además dibuja un gráfico.

### A7 · EJERCICIO 4 de 4 — La nota de la búsqueda frente al test

> Con el mejor modelo de cada búsqueda (`busqueda_grid.best_estimator_` y
> `busqueda_rand.best_estimator_`, ya reentrenados con todo train), guarda `auc_test_grid` y `auc_test_rand`
> (AUC en test con `predict_proba`) y en `optimismo_rand` la diferencia `mejor_auc_rand - auc_test_rand`.

```python
auc_test_grid = roc_auc_score(y_test, busqueda_grid.best_estimator_.predict_proba(X_test)[:, 1])
auc_test_rand = roc_auc_score(y_test, busqueda_rand.best_estimator_.predict_proba(X_test)[:, 1])
optimismo_rand = mejor_auc_rand - auc_test_rand
print(f"Rejilla + RF: AUC CV {mejor_auc_grid:.3f} → test {auc_test_grid:.3f}")
print(f"Aleatorio + LightGBM: AUC CV {mejor_auc_rand:.3f} → test {auc_test_rand:.3f} (diferencia {optimismo_rand:+.3f})")
```

**Tiene que salir:**

```text
Rejilla + RF: AUC CV 0.747 → test 0.734
Aleatorio + LightGBM: AUC CV 0.749 → test 0.740 (diferencia +0.009)
```

### A8 · MINI-RETO — Informe de la búsqueda

> Completa el diccionario `informe` con estas claves (para el **mejor de los dos buscadores según su AUC en
> validación**):
> - `"modelo"`: `"random_forest"` o `"lightgbm"`,
> - `"parametros"`: los `best_params_` correspondientes,
> - `"auc_validacion"` y `"auc_test"`,
> - `"n_entrenamientos"`: total de ajustes hechos en su búsqueda (combinaciones × folds),
> - `"recomendacion"`: una frase (texto) que diga si el resultado te parece fiable y por qué (menciona la
>   diferencia validación–test o los empates).

```python
if mejor_auc_rand >= mejor_auc_grid:
    ganador, nombre, busq, auc_val, auc_te = busqueda_rand, "lightgbm", busqueda_rand, mejor_auc_rand, auc_test_rand
else:
    ganador, nombre, busq, auc_val, auc_te = busqueda_grid, "random_forest", busqueda_grid, mejor_auc_grid, auc_test_grid
informe = {
    "modelo": nombre,
    "parametros": busq.best_params_,
    "auc_validacion": round(float(auc_val), 3),
    "auc_test": round(float(auc_te), 3),
    "n_entrenamientos": len(busq.cv_results_["params"]) * 3,
    "recomendacion": (f"El AUC en test ({auc_te:.3f}) es parecido al de validación ({auc_val:.3f}) y hay varias "
                      "configuraciones empatadas, así que el resultado es fiable pero mejorar más sería marginal."),
}
informe
```

**Tiene que salir:**

```text
{'modelo': 'lightgbm',
 'parametros': {'lgb__learning_rate': np.float64(0.019475582306295428),
  'lgb__min_child_samples': 199,
  'lgb__num_leaves': 23,
  'lgb__subsample': np.float64(0.7554709158757928)},
 'auc_validacion': 0.749,
 'auc_test': 0.74,
 'n_entrenamientos': 75,
 'recomendacion': 'El AUC en test (0.740) es parecido al de validación (0.749) y hay varias configuraciones empatadas, así que el resultado es fiable pero mejorar más sería marginal.'}
```

