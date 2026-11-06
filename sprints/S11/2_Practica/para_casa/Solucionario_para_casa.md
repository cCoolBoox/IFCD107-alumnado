# Solucionario · cuadernos completos («para casa») del Sprint 11

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S11_01` a `S11_03`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).
- El cuaderno del reto (`S11_04`) no se incluye(n): su solución se contrasta con la rúbrica del reto.

---

## S11_01 · Redes convolucionales (CNN): cómo "ve" una red

### Ejercicio 1 · Una imagen es una matriz de números

> Prepara los datos para una red: en `X` guarda las imágenes **normalizadas entre 0 y 1**
> (divide entre 16) con forma `(n, 8, 8, 1)` (Keras espera un canal explícito). Después crea con
> `train_test_split` (`test_size=0.25`, `random_state=SEMILLA`, `stratify=etiquetas`) los conjuntos
> `X_ent, X_pru, y_ent, y_pru`.

```python
X = (imagenes / 16.0).astype("float32")[..., np.newaxis]
X_ent, X_pru, y_ent, y_pru = train_test_split(X, etiquetas, test_size=0.25, random_state=SEMILLA, stratify=etiquetas)
```

### Ejercicio 2 · Calcular el tamaño de salida

> Para una entrada de `n` píxeles, filtro de `k`, relleno (*padding*) `p`
> a cada lado y paso (*stride*) `s`, la salida mide `(n - k + 2p) / s + 1` (parte entera). Escribe
> `tam_salida(n, k, p=0, s=1)` que devuelva ese número entero. Sirve para entender por qué las imágenes "encogen"
> capa tras capa (y por qué Keras ofrece `padding="same"`).

```python
def tam_salida(n, k, p=0, s=1):
    return (n - k + 2 * p) // s + 1

# Imagen de prueba: rectángulo claro sobre fondo oscuro
prueba = np.zeros((14, 14)); prueba[3:11, 4:10] = 1.0
filtro_vertical = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])     # detecta bordes verticales (Sobel)
filtro_horizontal = filtro_vertical.T                                  # detecta bordes horizontales

fig, ejes = plt.subplots(1, 3, figsize=(11, 3.6))
for eje, im, titulo in zip(ejes, [prueba, convolucion2d(prueba, filtro_vertical), convolucion2d(prueba, filtro_horizontal)],
                           ["Imagen original", "Bordes verticales", "Bordes horizontales"]):
    eje.imshow(im, cmap="gray"); eje.set_title(titulo); eje.axis("off")
plt.tight_layout(); plt.show()
print("Tamaño de la salida:", convolucion2d(prueba, filtro_vertical).shape, "(14 - 3 + 1 = 12)")
```

**Tiene que salir:**

```text
Tamaño de la salida: (12, 12) (14 - 3 + 1 = 12)
```

Y además dibuja un gráfico.

### Ejercicio 3 · Pooling: quedarse con lo importante

> Escribe `max_pooling(mapa, t=2)` que divida un mapa 2D (con lados múltiplos de `t`) en bloques de
> `t × t` y devuelva el máximo de cada bloque (salida de lado `alto // t`). Pista: recorre los bloques con dos bucles
> o busca cómo reorganizar el mapa con `reshape` para agrupar cada bloque.

```python
def max_pooling(mapa, t=2):
    alto, ancho = mapa.shape
    return mapa.reshape(alto // t, t, ancho // t, t).max(axis=(1, 3))

_m = np.array([[1, 2, 0, 0], [3, 4, 0, 1], [0, 0, 5, 6], [0, 9, 7, 8]])

salida_conv = convolucion2d(prueba, filtro_vertical)
fig, ejes = plt.subplots(1, 2, figsize=(8, 3.6))
ejes[0].imshow(np.abs(salida_conv), cmap="gray"); ejes[0].set_title("Mapa 12×12 tras la convolución"); ejes[0].axis("off")
ejes[1].imshow(max_pooling(np.abs(salida_conv)), cmap="gray"); ejes[1].set_title("Tras max pooling 2×2 (6×6)"); ejes[1].axis("off")
plt.tight_layout(); plt.show()
```

**Tiene que salir:** un gráfico.

### Ejercicio 4 · Una CNN completa en Keras

> Escribe `construir_cnn(filtros=(16, 32))` que devuelva un modelo compilado con:
> `Input(8,8,1)` → por cada valor de `filtros`: `Conv2D(f, 3, padding="same", activation="relu")` +
> `MaxPooling2D(2)` → `Flatten` → `Dense(10, activation="softmax")`.
> Compílalo igual que el MLP (`adam`, `sparse_categorical_crossentropy`, métrica `accuracy`).

```python
def construir_cnn(filtros=(16, 32)):
    m = keras.Sequential([keras.layers.Input(shape=(8, 8, 1))])
    for f in filtros:
        m.add(keras.layers.Conv2D(f, 3, padding="same", activation="relu"))
        m.add(keras.layers.MaxPooling2D(2))
    m.add(keras.layers.Flatten())
    m.add(keras.layers.Dense(10, activation="softmax"))
    m.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
    return m

cnn = construir_cnn()
cnn.summary()

keras.utils.set_random_seed(SEMILLA)
cnn = construir_cnn()
h_cnn = cnn.fit(X_ent, y_ent, validation_split=0.2, epochs=30, batch_size=32, verbose=0)
acc_cnn = cnn.evaluate(X_pru, y_pru, verbose=0)[1]
acc_mlp = mlp.evaluate(X_pru, y_pru, verbose=0)[1]

plt.plot(h_cnn.history["val_accuracy"], label="CNN"); plt.plot(h_mlp.history["val_accuracy"], label="MLP")
plt.xlabel("época"); plt.ylabel("exactitud de validación"); plt.title("CNN frente a MLP en dígitos 8×8"); plt.legend(); plt.show()
print(f"MLP: {mlp.count_params()} parámetros, exactitud {acc_mlp:.3f}")
print(f"CNN: {cnn.count_params()} parámetros, exactitud {acc_cnn:.3f}")
```

**Tiene que salir:**

```text
MLP: 4810 parámetros, exactitud 0.964
CNN: 6090 parámetros, exactitud 0.976
```

Y además dibuja un gráfico.

### Mini-reto integrador

> Construye `cnn_aug`: una CNN igual que `construir_cnn()` pero con las capas de `aumento`
> **al principio** del modelo (usa `keras.Sequential([keras.layers.Input((8, 8, 1)), aumento, ...])` o añádelas con `add`).
> Entrénala 40 épocas (`epochs=40`, `batch_size=32`, `validation_split=0.2`) y guarda en `acc_aug_desp` su exactitud
> sobre `X_pru_desp`. Guarda también en `acc_cnn_desp` la de la CNN sin aumento. Compáralas en la celda de texto.

```python
keras.utils.set_random_seed(SEMILLA)
cnn_aug = keras.Sequential([keras.layers.Input(shape=(8, 8, 1)), aumento])
for f in (16, 32):
    cnn_aug.add(keras.layers.Conv2D(f, 3, padding="same", activation="relu"))
    cnn_aug.add(keras.layers.MaxPooling2D(2))
cnn_aug.add(keras.layers.Flatten())
cnn_aug.add(keras.layers.Dense(10, activation="softmax"))
cnn_aug.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
cnn_aug.fit(X_ent, y_ent, validation_split=0.2, epochs=40, batch_size=32, verbose=0)
acc_aug_desp = cnn_aug.evaluate(X_pru_desp, y_pru, verbose=0)[1]
acc_cnn_desp = cnn.evaluate(X_pru_desp, y_pru, verbose=0)[1]

print(f"Con dígitos desplazados → CNN normal: {acc_cnn_desp:.3f} · CNN con aumento: {acc_aug_desp:.3f} · MLP: {mlp.evaluate(X_pru_desp, y_pru, verbose=0)[1]:.3f}")
```

**Tiene que salir:**

```text
Con dígitos desplazados → CNN normal: 0.264 · CNN con aumento: 0.651 · MLP: 0.144
```

---

## S11_02 · *Transfer learning* y *fine-tuning*

### Ejercicio 1 · Congelar la base y entrenar solo una cabeza nueva

> Escribe `congelar(modelo)` que ponga `trainable = False` en **todas** las capas del modelo dado
> (es decir, `modelo.trainable = False`) y lo devuelva. Después crea `copia_base` (una copia independiente de
> `base_pre`, ya lo tienes hecho abajo) y congélala.

```python
def congelar(modelo):
    modelo.trainable = False
    return modelo

def copiar_base(base, nombre):
    """Copia independiente de la base con los mismos pesos (para no modificar la original)."""
    copia = keras.models.clone_model(base)
    copia.set_weights(base.get_weights())
    copia._name = nombre
    return copia

copia_base = congelar(copiar_base(base_pre, "base_congelada"))

transfer = con_cabeza(copia_base, 5)
n_entrenables = sum(int(np.prod(p.shape)) for p in transfer.trainable_weights)
print(f"Parámetros totales: {transfer.count_params()} · entrenables (solo la cabeza): {n_entrenables}")
h_transfer = entrenar(transfer, epocas=30)
acc_transfer = transfer.evaluate(X_pru, y_pru, verbose=0)[1]
print(f"Transfer learning (base congelada) → exactitud en prueba: {acc_transfer:.3f}")
```

**Tiene que salir:**

```text
Parámetros totales: 35109 · entrenables (solo la cabeza): 11525
Transfer learning (base congelada) → exactitud en prueba: 0.833
```

### Ejercicio 2 · *Fine-tuning*: descongelar las últimas capas con cuidado

> Escribe `descongelar_bloque(base, n)` que ponga `trainable = True` **solo** en las capas de la base cuyo
> nombre empieza por `f"bloque{n}"` (por ejemplo `bloque3_conv`) y devuelva el número de pesos entrenables resultantes
> (`len(base.trainable_weights)`). Antes, `base.trainable` debe estar en `True` para poder cambiar capas sueltas,
> así que pon ese valor y después congela a mano las demás capas.

```python
def descongelar_bloque(base, n):
    base.trainable = True
    for capa in base.layers:
        capa.trainable = capa.name.startswith(f"bloque{n}")
    return len(base.trainable_weights)

_prueba = copiar_base(base_pre, "prueba")

# Fine-tuning: partimos del modelo transfer ya entrenado (cabeza lista), descongelamos el bloque 3 y bajamos la tasa
n_ent_ft = descongelar_bloque(copia_base, 3)
transfer.compile(keras.optimizers.Adam(1e-4), "sparse_categorical_crossentropy", metrics=["accuracy"])   # ¡recompilar!
h_ft = entrenar(transfer, epocas=25, semilla=1)
acc_ft = transfer.evaluate(X_pru, y_pru, verbose=0)[1]
print(f"Tras fine-tuning del bloque 3 → exactitud en prueba: {acc_ft:.3f}")
```

**Tiene que salir:**

```text
Tras fine-tuning del bloque 3 → exactitud en prueba: 0.830
```

### Mini-reto integrador · ¿cuántas imágenes necesito?

> El cliente pregunta: *"¿Cuántas fotos por tipo de alojamiento tenemos que etiquetar?"* Responde con datos:
> entrena la **CNN desde cero** y el **transfer learning con base congelada** con
> `n` ∈ {3, 6, 12, 24} imágenes por clase (genéralas con `generar_lote(alojamiento, CLASES_ALOJ, n, semilla=20)`)
> y guarda en el diccionario `curva_datos` la exactitud en prueba de cada estrategia, con la forma
> `{n: (acc_desde_cero, acc_transfer)}`. Usa 40 épocas para "desde cero" y 30 para "transfer".

```python
curva_datos = {}
for n in (3, 6, 12, 24):
    Xn, yn = generar_lote(alojamiento, CLASES_ALOJ, n, semilla=20)
    keras.utils.set_random_seed(SEMILLA)
    m_cero = con_cabeza(construir_base("cero"), 5)
    entrenar(m_cero, 40, SEMILLA, Xn, yn)
    m_tr = con_cabeza(congelar(copiar_base(base_pre, "b")), 5)
    entrenar(m_tr, 30, SEMILLA, Xn, yn)
    curva_datos[n] = (m_cero.evaluate(X_pru, y_pru, verbose=0)[1], m_tr.evaluate(X_pru, y_pru, verbose=0)[1])

ns = sorted(curva_datos)
plt.plot(ns, [curva_datos[n][0] for n in ns], "o-", label="desde cero")
plt.plot(ns, [curva_datos[n][1] for n in ns], "s-", label="transfer learning (base congelada)")
plt.xlabel("imágenes por clase"); plt.ylabel("exactitud en prueba"); plt.ylim(0, 1.02)
plt.title("¿Cuántas imágenes hacen falta?"); plt.legend(); plt.show()
```

**Tiene que salir:** un gráfico.

---

## S11_03 · Detección de objetos y segmentación

### Ejercicio 1 · Cajas y la IoU (*Intersection over Union*)

> Escribe `iou(a, b)` que reciba dos cajas `[x1, y1, x2, y2]` y devuelva su IoU (un número entre 0 y 1).
> Cuidado con el caso en que no se solapan (la intersección vale 0, no negativa).

```python
def iou(a, b):
    ancho = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    alto = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    inter = ancho * alto
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    union = area_a + area_b - inter
    return inter / union if union > 0 else 0.0
```

### Ejercicio 2 · NMS (*Non-Maximum Suppression*): quedarse con una caja por objeto

> Escribe `nms(cajas, puntuaciones, umbral_iou=0.5)` que devuelva la **lista de índices** de las cajas que se
> conservan, en orden de confianza decreciente. Usa tu función `iou`.

```python
def nms(cajas, puntuaciones, umbral_iou=0.5):
    orden = list(np.argsort(puntuaciones)[::-1])
    conservadas = []
    while orden:
        mejor = orden.pop(0)
        conservadas.append(int(mejor))
        orden = [i for i in orden if iou(cajas[mejor], cajas[i]) <= umbral_iou]
    return conservadas

_cajas = [[10, 10, 50, 50], [12, 12, 52, 52], [100, 100, 140, 140], [11, 9, 49, 51]]
_punt = [0.9, 0.8, 0.7, 0.6]
```

### Ejercicio 3 · Métricas: precisión, recall, AP y mAP con números

> Escribe `average_precision(es_tp, n_reales)`: recibe una lista de 0/1 con las detecciones **ya ordenadas por
> confianza decreciente** (1 = verdadero positivo) y el número de objetos reales `n_reales`, y devuelve el AP.
> Pasos: acumula TP y FP; calcula `precision = TP/(TP+FP)` y `recall = TP/n_reales` en cada puesto; haz la precisión
> monótona (de derecha a izquierda, cada valor pasa a ser el máximo de los que tiene a su derecha); suma
> `(recall_i − recall_{i−1}) × precision_i`.

```python
def average_precision(es_tp, n_reales):
    es_tp = np.asarray(es_tp, dtype=float)
    if len(es_tp) == 0 or n_reales == 0:
        return 0.0
    tp = np.cumsum(es_tp)
    fp = np.cumsum(1 - es_tp)
    precision = tp / (tp + fp)
    recall = tp / n_reales
    precision = np.maximum.accumulate(precision[::-1])[::-1]
    recall_previo = np.concatenate([[0.0], recall[:-1]])
    return float(np.sum((recall - recall_previo) * precision))
```

### Ejercicio 4 · Un detector clásico con OpenCV sobre imágenes sintéticas

> Calcula el **mAP@[.5:.9]** simplificado del detector de color: la media del AP con umbrales de IoU
> `0.5, 0.6, 0.7, 0.8, 0.9` (usa `evaluar_detector(detector_color, umbral_iou=u)["AP"]`). Guarda la media en `map_iou`
> y, en `ap_por_umbral`, la lista de los 5 AP. Como solo hay una clase (sombrilla), el mAP coincide con el AP.

```python
umbrales = [0.5, 0.6, 0.7, 0.8, 0.9]      # los umbrales de IoU que vas a probar (ya escritos)
ap_por_umbral = [evaluar_detector(detector_color, umbral_iou=u)["AP"] for u in umbrales]
map_iou = float(np.mean(ap_por_umbral))

plt.plot(umbrales, ap_por_umbral, "o-"); plt.xlabel("umbral de IoU exigido"); plt.ylabel("AP")
plt.title(f"Detector de color: AP según el umbral de IoU (media = {map_iou:.2f})"); plt.ylim(0, 1.02); plt.show()
```

**Valores que tienen que salir:**

```text
ap_por_umbral: list de 5 elementos, [0.5365371508049828, 0.5085113065064644, 0.47706314294414587, 0.29002944715918677, 0.003652170016356344]
map_iou = 0.3632
```

Y además dibuja un gráfico.

### Ejercicio 5 · Segmentación

> Escribe `iou_mascara(pred, real)` y `dice(pred, real)` para máscaras booleanas del mismo tamaño
> (`True` = sombrilla). Devuelve 1.0 si ambas están vacías.

```python
def iou_mascara(pred, real):
    inter = np.logical_and(pred, real).sum()
    union = np.logical_or(pred, real).sum()
    return float(inter / union) if union > 0 else 1.0

def dice(pred, real):
    inter = np.logical_and(pred, real).sum()
    total = pred.sum() + real.sum()
    return float(2 * inter / total) if total > 0 else 1.0

_p = np.array([[1, 1, 0], [0, 0, 0]], dtype=bool); _r = np.array([[1, 0, 0], [1, 0, 0]], dtype=bool)

rng = np.random.default_rng(200)
ious_umbral = []
for _ in range(20):
    im, _, real = escena(rng)
    _, _, pred = detectar_color(im)
    ious_umbral.append((iou_mascara(pred, real), dice(pred, real)))
print("Segmentación por umbral de color: IoU media =", round(np.mean([a for a, _ in ious_umbral]), 3),
      "· Dice medio =", round(np.mean([b for _, b in ious_umbral]), 3))
```

**Tiene que salir:**

```text
Segmentación por umbral de color: IoU media = 0.629 · Dice medio = 0.756
```

### Mini-reto integrador · contar sombrillas y afinar el detector

> El cliente quiere un **contador de sombrillas** por foto de la playa. Con 30 escenas nuevas (`semilla=500`):
> 1. Calcula en `error_conteo` el error absoluto medio entre el número de cajas del `detector_color` y el número real.
> 2. Prueba `sat_min` ∈ {60, 90, 120, 150, 180} y guarda en `mejor_sat` el valor que da mayor **F1** de detección
>    (F1 = 2·P·R/(P+R), con IoU ≥ 0,5, usando `evaluar_detector` con un detector que fije ese `sat_min`) y en `f1_mejor` su valor.
> Con sat_min bajo la arena "cuela" como sombrilla; con sat_min alto se pierden sombrillas amarillas.

```python
rng = np.random.default_rng(500)
errores = []
for _ in range(30):
    im, reales, _ = escena(rng)
    errores.append(abs(len(detector_color(im)[0]) - len(reales)))
error_conteo = float(np.mean(errores))

f1_por_sat = {}
for s in (60, 90, 120, 150, 180):
    r = evaluar_detector(lambda im, s=s: detectar_color(im, sat_min=s)[:2], n_escenas=30, semilla=500)
    p, rec = r["precisión"], r["recall"]
    f1_por_sat[s] = 2 * p * rec / (p + rec) if p + rec > 0 else 0.0
mejor_sat = max(f1_por_sat, key=f1_por_sat.get)
f1_mejor = f1_por_sat[mejor_sat]

print(f"Error medio de conteo: {error_conteo:.2f} sombrillas por foto · mejor sat_min = {mejor_sat} (F1 = {f1_mejor:.2f})")
print({s: round(v, 2) for s, v in f1_por_sat.items()})
```

**Tiene que salir:**

```text
Error medio de conteo: 1.87 sombrillas por foto · mejor sat_min = 90 (F1 = 0.71)
{60: 0.08, 90: 0.71, 120: 0.69, 150: 0.69, 180: 0.69}
```

