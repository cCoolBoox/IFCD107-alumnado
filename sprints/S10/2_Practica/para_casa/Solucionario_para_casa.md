# Solucionario · cuadernos completos («para casa») del Sprint 10

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S10_01` a `S10_03`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).
- El cuaderno del reto (`S10_04`) no se incluye(n): su solución se contrasta con la rúbrica del reto.

---

## S10_01 · Una red neuronal desde cero, solo con NumPy

### A3 · EJERCICIO 1 de 4 — La función neurona

> Escribe la función `neurona(x, pesos, sesgo)` que devuelva la salida
> de la neurona (suma ponderada + sesgo, pasada por `sigmoide`).

```python
def neurona(x, pesos, sesgo):
    return sigmoide(np.dot(x, pesos) + sesgo)

salida_ejemplo = neurona(np.array([1.5, 1.0]), np.array([0.8, 1.2]), -1.0)
```

**Valores que tienen que salir:**

```text
salida_ejemplo = 0.8022
```

### A5 · EJERCICIO 2 de 4 — ReLU y su derivada

> Define `relu(z)` (devuelve `z` si es positivo y 0 si no) y `relu_derivada(z)`
> (vale 1 donde `z > 0` y 0 en el resto). La derivada nos dirá más adelante "por dónde
> fluye el aprendizaje": una neurona ReLU apagada (z ≤ 0) no aprende en esa muestra.

```python
def relu(z):
    return np.maximum(0, z)

def relu_derivada(z):
    return (z > 0).astype(float)

_prueba = np.array([-2.0, 0.0, 3.0])
```

### A8 · EJERCICIO 3 de 4 — Un paso de descenso de gradiente

> Escribe `paso_gradiente(parametros, gradientes, tasa)`: recibe dos diccionarios con
> las mismas claves (`"W1"`, `"b1"`, `"W2"`, `"b2"`) y devuelve un diccionario **nuevo** con cada
> parámetro actualizado: `nuevo = viejo - tasa * gradiente`. `tasa` es la **tasa de aprendizaje**
> (el tamaño del pasito).

```python
def paso_gradiente(parametros, gradientes, tasa):
    return {k: parametros[k] - tasa * gradientes[k] for k in parametros}

_p = {"W1": np.array([1.0, 2.0]), "b1": np.array([0.5])}
_g = {"W1": np.array([0.5, -1.0]), "b1": np.array([1.0])}
_nuevo = paso_gradiente(_p, _g, 0.1)
```

### A14 · EJERCICIO 4 de 4 — Exactitud de la red y mejora sobre el modelo lineal

> Calcula en la variable `exactitud_val` la exactitud (proporción de aciertos) de la red de 8 neuronas
> (`mejor`) sobre `X_val`/`y_val` usando su método `predecir`. Y en `mejora_sobre_lineal`
> guarda cuántos puntos porcentuales (en fracción, p. ej. 0.4) supera al modelo `lineal`.

```python
exactitud_val = (mejor.predecir(X_val) == y_val).mean()
mejora_sobre_lineal = exactitud_val - lineal.score(X_val, y_val)
```

**Valores que tienen que salir:**

```text
exactitud_val = 1.0
mejora_sobre_lineal = 0.5056
```

### A15 · MINI-RETO — Una red con tasa de aprendizaje 0.01

> Entrena una red con **4 neuronas ocultas** y una **tasa de aprendizaje de 0.01** (muy pequeña) durante 1500 épocas,
> guarda la red en `red_lenta` y su exactitud de validación en `exactitud_lenta`.
> Después contesta en la celda de texto: ¿por qué le cuesta tanto más? ¿Qué pasaría con una tasa de 50?

```python
red_lenta = RedNeuronal(2, 4).entrenar(X_ent, y_ent, epocas=1500, tasa=0.01, X_val=X_val, y_val=y_val)
exactitud_lenta = (red_lenta.predecir(X_val) == y_val).mean()

print("Exactitud con tasa 0.01:", round(exactitud_lenta, 3))
```

**Tiene que salir:**

```text
Exactitud con tasa 0.01: 0.606
```

---

## S10_02 · Tu primer MLP en Keras: cancelaciones y precio por noche

### A3 · EJERCICIO 1 de 5 — Columnas numéricas y categóricas

> Define dos listas: `cols_num` (las columnas numéricas: `antelacion_dias`, `noches`, `adultos`, `ninos`,
> `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`, `mes_llegada`) y `cols_cat`
> (las categóricas: `tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito`).
> Para la clasificación añadiremos `precio_noche` a las numéricas más abajo.

```python
cols_num = ["antelacion_dias", "noches", "adultos", "ninos", "peticiones_especiales",
            "cliente_repetidor", "cancelaciones_previas", "mes_llegada"]
cols_cat = ["tipo_habitacion", "regimen", "canal", "pais_origen", "tarifa", "deposito"]
```

**Valores que tienen que salir:**

```text
cols_num: list de 8 elementos, ['antelacion_dias', 'noches', 'adultos', 'ninos', 'peticiones_especiales', 'cliente_repetidor']
cols_cat: list de 6 elementos, ['tipo_habitacion', 'regimen', 'canal', 'pais_origen', 'tarifa', 'deposito']
```

### A5 · EJERCICIO 2 de 5 — Construir el MLP de clasificación

> Escribe `construir_mlp_clasificacion(n_entradas, capas=(32, 16))` que devuelva un modelo
> `keras.Sequential` con una capa `Input`, una capa `Dense` con `relu` por cada número de `capas`, y una
> salida `Dense(1, activation="sigmoid")`. Debe **compilarlo** con el optimizador `adam`, la pérdida
> `binary_crossentropy` y las métricas `AUC` (llamada `auc`) y `accuracy`.

```python
def construir_mlp_clasificacion(n_entradas, capas=(32, 16)):
    modelo = keras.Sequential([keras.layers.Input(shape=(n_entradas,))])
    for unidades in capas:
        modelo.add(keras.layers.Dense(unidades, activation="relu"))
    modelo.add(keras.layers.Dense(1, activation="sigmoid"))
    modelo.compile(optimizer="adam", loss="binary_crossentropy",
                   metrics=[keras.metrics.AUC(name="auc"), "accuracy"])
    return modelo

mlp_c = construir_mlp_clasificacion(Xc_ent.shape[1])
mlp_c.summary()
```

### A8 · EJERCICIO 3 de 5 — ¿Gana el MLP a la regresión logística?

> Guarda en `auc_mlp` el AUC del MLP en prueba y en `auc_log` el de la regresión logística
> (a partir de `prob_mlp` y `prob_log`, con `roc_auc_score`). Después guarda en `mlp_gana` un booleano
> (`True`/`False`) que diga si el MLP supera a la regresión logística **por más de 0.02 de AUC**.
> Esta última respuesta puede ser `False`: no siempre gana la red.

```python
auc_mlp = roc_auc_score(yc_pru, prob_mlp)
auc_log = roc_auc_score(yc_pru, prob_log)
mlp_gana = bool(auc_mlp - auc_log > 0.02)

print(f"AUC MLP = {auc_mlp:.3f} · AUC logística = {auc_log:.3f} · ¿gana la red por más de 0.02? {mlp_gana}")
```

**Tiene que salir:**

```text
AUC MLP = 0.727 · AUC logística = 0.746 · ¿gana la red por más de 0.02? False
```

### A10 · EJERCICIO 4 de 5 — Construir el MLP de regresión

> Escribe `construir_mlp_regresion(n_entradas, capas=(32, 16))`: igual que el de clasificación pero con
> salida `Dense(1)` **sin activación**, pérdida `"mse"` y métrica `"mae"`.

```python
def construir_mlp_regresion(n_entradas, capas=(32, 16)):
    modelo = keras.Sequential([keras.layers.Input(shape=(n_entradas,))])
    for unidades in capas:
        modelo.add(keras.layers.Dense(unidades, activation="relu"))
    modelo.add(keras.layers.Dense(1))
    modelo.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return modelo

mlp_r = construir_mlp_regresion(Xr_ent.shape[1])

hist_r = mlp_r.fit(Xr_ent, esc(yr_ent), validation_data=(Xr_val, esc(yr_val)), epochs=30, batch_size=64, verbose=0)
dibujar_curvas(hist_r, "mae", "MLP de precio_noche: curvas de aprendizaje (escala estandarizada)")

pred_mlp = desesc(mlp_r.predict(Xr_pru, verbose=0).ravel())
ridge = Ridge().fit(Xr_ent, yr_ent)
pred_ridge = ridge.predict(Xr_pru)
mae = lambda p: mean_absolute_error(yr_pru, p)
tabla_r = pd.DataFrame({
    "modelo": ["Siempre el precio medio", "Regresión lineal (Ridge)", "MLP (32-16)"],
    "MAE (€)": [mae(np.full(len(yr_pru), yr_ent.mean())), mae(pred_ridge), mae(pred_mlp)],
}).round(2)
tabla_r
```

**Valores que tienen que salir:**

```text
tabla_r: tabla de 3 filas y 2 columnas
```

Y además dibuja un gráfico.

### A12 · EJERCICIO 5 de 5 — El error en euros y la mejora

> Calcula en `mae_mlp_euros` el error medio absoluto **en euros** del MLP sobre el conjunto de prueba
> (usa `pred_mlp`, que ya está en euros, e `yr_pru`). Calcula también `mejora_vs_media`: en qué fracción
> (0 a 1) reduce el error respecto a predecir siempre el precio medio del entrenamiento.

```python
mae_mlp_euros = mean_absolute_error(yr_pru, pred_mlp)
mae_base = mean_absolute_error(yr_pru, np.full(len(yr_pru), yr_ent.mean()))
mejora_vs_media = 1 - mae_mlp_euros / mae_base

plt.figure(figsize=(5, 5))
plt.scatter(yr_pru, pred_mlp, s=8, alpha=0.4)
lim = [yr_pru.min(), yr_pru.max()]
plt.plot(lim, lim, "r--", label="predicción perfecta")
plt.xlabel("precio real (€/noche)"); plt.ylabel("precio predicho (€/noche)")
plt.title("MLP de precio: real frente a predicho"); plt.legend(); plt.show()
```

**Valores que tienen que salir:**

```text
mae_mlp_euros = 11.814
mejora_vs_media = 0.5371
lim: list de 2 elementos, [54.29, 244.3]
```

Y además dibuja un gráfico.

### A14 · MINI-RETO — Una red más ancha (128-64)

> Construye un MLP de clasificación **más ancho** (`capas=(128, 64)`), entrénalo 15 épocas con `batch_size=64`
> y guarda en `auc_ancho` su AUC en **validación** (la última época: `hist_ancho.history["val_auc"][-1]`).
> ¿Es mejor la red grande? Escribe tu conclusión en la celda de texto.
> Pista de la teoría: más parámetros = más capacidad, pero también más facilidad para memorizar.

```python
keras.utils.set_random_seed(SEMILLA)
mlp_ancho = construir_mlp_clasificacion(Xc_ent.shape[1], capas=(128, 64))
hist_ancho = mlp_ancho.fit(Xc_ent, yc_ent, validation_data=(Xc_val, yc_val), epochs=15, batch_size=64, verbose=0)
auc_ancho = hist_ancho.history["val_auc"][-1]

print(f"AUC en validación de la red ancha: {auc_ancho:.3f} · parámetros: {mlp_ancho.count_params()} frente a {mlp_c.count_params()}")
```

**Tiene que salir:**

```text
AUC en validación de la red ancha: 0.724 · parámetros: 12929 frente a 1697
```

---

## S10_03 · Entrenar bien: sobreajuste, regularización y callbacks

### A5 · EJERCICIO 1 de 4 — Época óptima y brecha final

> A partir de `h_base.history["val_loss"]` calcula:
> - `epoca_optima`: la época (contando desde 1) en la que la pérdida de validación fue **mínima**;
> - `brecha_final`: pérdida de validación de la última época **menos** pérdida de entrenamiento de la última época.
> Si `epoca_optima` es muy inferior al total de épocas, seguir entrenando solo empeoraba el modelo.

```python
perd_val = h_base.history["val_loss"]
perd_ent = h_base.history["loss"]
epoca_optima = int(np.argmin(perd_val)) + 1
brecha_final = perd_val[-1] - perd_ent[-1]

print(f"Mejor época: {epoca_optima} de 60 · brecha final = {brecha_final:.2f}")
```

**Tiene que salir:**

```text
Mejor época: 2 de 60 · brecha final = 2.11
```

### A6 · EJERCICIO 2 de 4 — Entrenar con dropout

> Entrena con `entrenar(A_peq, y_peq, ...)` una red con **dropout de 0.4** y guarda el modelo en
> `m_drop` y el historial en `h_drop`. Después comprueba en `n_dropout` cuántas capas `Dropout` tiene el modelo
> (usa `isinstance(capa, keras.layers.Dropout)`).

```python
m_drop, h_drop = entrenar(A_peq, y_peq, epocas=60, dropout=0.4)
n_dropout = sum(isinstance(capa, keras.layers.Dropout) for capa in m_drop.layers)

configs = {
    "Sin regularizar": dict(),
    "L2 = 0.01": dict(l2=0.01),
    "Dropout 0.4": dict(dropout=0.4),
    "BatchNorm": dict(batchnorm=True),
    "L2 + Dropout": dict(l2=0.005, dropout=0.3),
}
resultados = {}
fig, ejes = plt.subplots(1, len(configs), figsize=(4 * len(configs), 3.6), sharey=True)
for eje, (nombre, cfg) in zip(ejes, configs.items()):
    m, h = entrenar(A_peq, y_peq, epocas=60, **cfg)
    resultados[nombre] = h.history
    curvas(h, nombre, eje)
plt.tight_layout(); plt.show()

resumen = pd.DataFrame({
    nombre: {"mejor pérdida val.": min(h["val_loss"]), "pérdida val. final": h["val_loss"][-1],
             "AUC val. final": h["val_auc"][-1], "AUC val. máximo": max(h["val_auc"])}
    for nombre, h in resultados.items()
}).T.round(3)
resumen
```

**Valores que tienen que salir:**

```text
n_dropout = 2
resumen: tabla de 5 filas y 4 columnas
```

Y además dibuja un gráfico.

### A8 · EJERCICIO 3 de 4 — Parada temprana y reducción de la tasa

> Crea la lista `mis_callbacks` con un `EarlyStopping` (monitoriza `val_loss`, `patience=8`,
> `restore_best_weights=True`) y un `ReduceLROnPlateau` (monitoriza `val_loss`, `factor=0.5`, `patience=4`).
> Después entrena con `entrenar(A_peq, y_peq, epocas=100, callbacks=mis_callbacks, l2=0.005, dropout=0.3)`
> y guarda el resultado en `m_es` y `h_es`.

```python
mis_callbacks = [
    keras.callbacks.EarlyStopping(monitor="val_loss", patience=8, restore_best_weights=True),
    keras.callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=4),
]
m_es, h_es = entrenar(A_peq, y_peq, epocas=100, callbacks=mis_callbacks, l2=0.005, dropout=0.3)

epocas_reales = len(h_es.history["loss"])
print(f"Entrenó {epocas_reales} de 100 épocas posibles. Mejor pérdida de validación: {min(h_es.history['val_loss']):.3f}")

fig, ejes = plt.subplots(1, 2, figsize=(11, 3.6))
curvas(h_es, "Con EarlyStopping y ReduceLROnPlateau", ejes[0])
if "learning_rate" in h_es.history:
    ejes[1].plot(h_es.history["learning_rate"]); ejes[1].set_yscale("log")
    ejes[1].set_xlabel("época"); ejes[1].set_ylabel("tasa de aprendizaje"); ejes[1].set_title("Cómo bajó la tasa")
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Entrenó 26 de 100 épocas posibles. Mejor pérdida de validación: 0.743
```

Y además dibuja un gráfico.

### A11 · EJERCICIO 4 de 4 — Guardar y cargar el modelo

> Guarda `m_es` en el archivo indicado por `ruta_modelo` con `m_es.save(...)`, cárgalo con
> `keras.models.load_model(...)` en `m_cargado` y calcula en `prob_cargado` sus probabilidades sobre `A_val`.
> Se comprobará que son idénticas a las del modelo original.

```python
carpeta_tmp = tempfile.mkdtemp()
ruta_modelo = os.path.join(carpeta_tmp, "modelo_cancelaciones.keras")
m_es.save(ruta_modelo)
m_cargado = keras.models.load_model(ruta_modelo)
prob_cargado = m_cargado.predict(A_val, verbose=0)

prob_original = m_es.predict(A_val, verbose=0)
print("Modelo guardado y recargado correctamente:", round(os.path.getsize(ruta_modelo) / 1024), "KB")

# Limpieza del archivo temporal (en tu proyecto real, conserva el modelo)
import shutil
shutil.rmtree(carpeta_tmp, ignore_errors=True)
```

**Tiene que salir:**

```text
Modelo guardado y recargado correctamente: 525 KB
```

### A14 · MINI-RETO — Gana a la red entrenada a ciegas

> Con el **entrenamiento completo** (`A_ent`, 3840 filas) parte de la red grande sin regularizar
> (`capas=(256, 128)`, 40 épocas, lote 64) y consigue una **menor pérdida de validación del modelo final** combinando lo aprendido:
> guarda en `m_final` tu mejor modelo (con `entrenar`) y en `mejor_perdida_val` su pérdida sobre `A_val`
> (`m_final.evaluate(A_val, y_val, verbose=0)[0]`). Tienes que superar (tener menos pérdida que) la red grande
> entrenada a ciegas, `perdida_referencia`.
> Anota qué combinación usaste y por qué.

```python
_, h_ref = entrenar(A_ent, y_ent, epocas=40, lote=64, capas=(256, 128))
perdida_referencia = h_ref.history["val_loss"][-1]     # lo que obtendrías entrenando "a ciegas" hasta el final
print("Referencia (sin regularizar), pérdida de validación tras 40 épocas:", round(perdida_referencia, 4),
      "· la mejor había sido", round(min(h_ref.history["val_loss"]), 4))

m_final, h_final = entrenar(A_ent, y_ent, epocas=40, lote=64, capas=(64, 32), l2=0.003, dropout=0.3,
                            callbacks=[keras.callbacks.EarlyStopping(monitor="val_loss", patience=6, restore_best_weights=True)])
mejor_perdida_val = m_final.evaluate(A_val, y_val, verbose=0)[0]

print(f"Tu mejor pérdida de validación: {mejor_perdida_val:.4f} (referencia {perdida_referencia:.4f})")
```

**Tiene que salir:**

```text
Referencia (sin regularizar), pérdida de validación tras 40 épocas: 1.3336 · la mejor había sido 0.5915
Tu mejor pérdida de validación: 0.6151 (referencia 1.3336)
```

