# Solucionario · cuadernos «en clase» del Sprint 11

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S11_01`, `S11_02`, `S11_03`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

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

