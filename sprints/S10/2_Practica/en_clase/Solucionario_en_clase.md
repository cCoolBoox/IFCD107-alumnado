# Solucionario · cuadernos «en clase» del Sprint 10

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S10_01`, `S10_02`, `S10_03`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S10_01 · Una red neuronal desde cero, solo con NumPy

### Ejercicio 1 · La neurona: una suma ponderada y un "interruptor suave"

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

### Ejercicio 2 · Funciones de activación

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

### Ejercicio 3 · Propagación hacia delante: de las entradas a la predicción

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

---

## S10_02 · Tu primer MLP en Keras: cancelaciones y precio por noche

### Ejercicio 1 · Preparar los datos para una red neuronal

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

### Ejercicio 2 · Un MLP para clasificar cancelaciones

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

### Ejercicio 3 · Un MLP para clasificar cancelaciones

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

---

## S10_03 · Entrenar bien: sobreajuste, regularización y callbacks

### Ejercicio 1 · Provocar y diagnosticar el sobreajuste

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

### Ejercicio 2 · Las herramientas de regularización

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

### Ejercicio 3 · Parada temprana y callbacks

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

