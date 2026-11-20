# Solución extendida · Reto exprés S11

**Para contrastar después de intentarlo** con `Reto_expres_plantilla.ipynb`. Si tu red sale distinta, no pasa nada: las cifras salen de ejecutar el cuaderno con la semilla 42 (y, en la sección 3, media de 3 semillas); tú verás cifras parecidas, no idénticas.

- Cómo leer la tabla de pruebas: **entrenamiento** = lo que acierta con las imágenes con las que aprendió · **validación** = con imágenes que no ha visto y sirven para elegir · **hueco** = entrenamiento − validación, en puntos.
- La **prueba** solo se mira al final y una vez.

---

## 1 · Solución celda a celda

### ✏️ 1 · Elegir problema
- Cualquiera de los 6. Antes de entrenar, apuntar la **línea base** que imprime la celda (acertar sin red) y apostar qué variante ganará.
- Los más didácticos:
  - `formas` → la densa no aprende y hay sobreajuste claro.
  - `fashion_parecidas` → errores razonables (jersey ↔ camisa).
  - `alojamientos` → 100 %: ¿es creíble?

### ✏️ 2 · Comparar variantes y elegir con la validación
Variante elegida = la de **mayor `val_acc`**. `ELEGIDA = "cnn"` viene de ejemplo: hay que cambiarlo si otra gana (en `mnist` gana `cnn_aug`).

| Problema | Línea base | Val. densa | Val. CNN | Val. CNN+aum. | **Elegida** | Hueco de la elegida |
|---|--:|--:|--:|--:|---|--:|
| `digitos` | 10,3 % | 95,3 % | **97,5 %** | 91,4 % | cnn | 1,7 |
| `mnist` | 11,2 % | 92,5 % | 95,6 % | **97,4 %** | cnn_aug | 0,8 |
| `fashion` | 10,0 % | 82,3 % | **84,1 %** | 73,1 % | cnn | 4,9 |
| `fashion_parecidas` | 25,0 % | 76,7 % | **79,5 %** | 67,8 % | cnn | 5,5 |
| `alojamientos` | 20,0 % | 98,0 % | **100 %** | **100 %** | cnn | 0,0 |
| `formas` | 12,5 % | 15,9 % | **86,6 %** | 79,1 % | cnn | 9,0 |

Cómo justificarlo con números (frase modelo): «la CNN subió la validación de **15,9 % a 86,6 %** frente a la densa; con aumento bajó a 79,1 %».

- **Densa en `formas` (15,9 %, casi la línea base):** aplana la imagen y aprende «el píxel 1 000 está oscuro», pero un rectángulo o un círculo aparecen en sitios distintos. Entrenó solo 8 épocas antes de parar porque la validación no mejoraba.
- **Aumento que baja:** en 4 problemas baja y solo sube en `mnist`. El aumento hace el problema más difícil durante el entrenamiento y necesita más épocas; el cuaderno corta a 30.
- **Si `epocas` llega a 30**, la red aún podía aprender (`digitos`, `mnist`+aumento, `alojamientos`).

### ⚙️ Curvas de la elegida
- **Sana:** las dos curvas bajan y quedan cerca (`digitos`, `mnist`).
- **Sobreajuste:** la pérdida de entrenamiento sigue bajando y la de validación se para o sube. Ejemplos:
  - `fashion`: pérdida de entrenamiento 0,24 frente a validación mínima 0,45.
  - `formas`: 0,23 frente a 0,39.
- **Épocas buenas:** el cuaderno ya devuelve los pesos de la **mejor época** (`restore_best_weights`), no los de la última.

### ✏️ 3 · Prueba, peor clase y errores (valores de referencia de la elegida por validación)

| Problema | Prueba | Peor clase (recall) | Mayor confusión | Fallos |
|---|--:|---|---|--:|
| `digitos` | 97,5 % | 8 (85,7 %) | 8 → 1 (4) | 9 de 360 |
| `mnist` | 97,1 % | 9 (93,3 %) | 9 → 3 (5) | 35 de 1 200 |
| `fashion` | 84,0 % | abrigo (59,2 %) | abrigo → jersey (27) | 192 de 1 200 |
| `fashion_parecidas` | 79,1 % | jersey (70,0 %) | jersey → camisa (50) | 251 de 1 200 |
| `alojamientos` | 100 % | hotel (100 %) | ninguna | 0 de 300 |
| `formas` | 86,2 % | rectángulo (72,5 %) | rectángulo → círculo (10) | 44 de 320 |

- **Errores razonables:** jersey ↔ camisa ↔ abrigo a 28×28 los confundiría también una persona.
- **En `formas`** (rectángulo → círculo): no se puede juzgar solo con el número. Abrir las imágenes que fallan y decidir si el error es razonable o raro.
- **100 % en `alojamientos`:** dibujos inventados con reglas fijas; no significa que valga con fotos reales. Probarlo con fotos de verdad (S11_04) es el siguiente paso.

### ✏️ 4 · `probar(i)`
- Probar primero los que **fallan** (`np.where(c != y_pru)`) y mirar la seguridad: un error con 90 % de seguridad es peor que uno con 40 %.
- Prueba para el público: elegir al azar una imagen de la prueba y predecirla en directo.

### 🎤 Frases modelo (ejemplo `fashion_parecidas`)
- **Problema:** «Reconocemos prendas parecidas (camiseta, jersey, abrigo, camisa) para clasificar un catálogo».
- **Variantes:** «Comparamos densa, CNN y CNN con aumento: la CNN subió la validación de 76,7 % a 79,5 %; el aumento la bajó a 67,8 %».
- **Errores:** «Acierta 79,1 % frente a 25 % de la línea base. Su peor clase es jersey (70 %) y se confunde sobre todo con camisa (50 casos): es razonable, se parecen mucho a 28×28».
- **Uso real:** «No la usaríamos sola: con un 21 % de fallos haría falta que una persona revise los casos dudosos».

---

## 2 · Cómo diagnosticar antes de tocar nada

| Lo que veo | Qué significa | Qué hacer |
|---|---|---|
| Entrenamiento ≈ validación y las dos altas | Aprende bien | Nada. Mirar la peor clase |
| Entrenamiento ≈ validación y las dos **bajas** | **Infraajuste**: la red es corta o ha parado pronto | Más filtros o más épocas; **no** regularizar más |
| Entrenamiento mucho mayor que validación (hueco ≥ 5 puntos) | **Sobreajuste** | Sección 3 |
| 100 % en todo | Problema demasiado fácil | Desconfiar: datos más difíciles o reales |
| `epocas` = 30 | Aún aprendía | Subir `epocas` antes de comparar variantes |

Regla de lectura: **el hueco no es el objetivo, la validación sí.** Un hueco pequeño con validación baja es peor que un hueco mediano con validación alta.

---

## 3 · «Bajo los filtros y sigo teniendo sobreajuste, ¿qué hago?»

Primero, qué cuenta como «sobreajuste que importa»: hueco de 5–6 puntos con validación del 80–85 % es normal con unos miles de imágenes. En `formas` (9–12 puntos con solo 960 imágenes de entrenamiento) sí importa.

**Por qué bajar filtros no sirve aquí:** en los tres problemas con hueco, quitar filtros **no cerró el hueco** y la validación bajó (con 3 semillas, `formas` tiene ±3 puntos de ruido: 1–2 puntos de diferencia no se pueden defender).

| Problema | Filtros | Entrenamiento | Validación | Hueco |
|---|--:|--:|--:|--:|
| `formas` | 16 | 94,3 % | 82,4 % | 11,9 |
| | 8 | 93,8 % | 80,8 % | 13,0 |
| | 4 | 94,9 % | 80,2 % | 14,7 |
| `fashion_parecidas` | 16 / 8 / 4 | 84,8 / 83,3 / 83,1 % | 78,5 / 77,9 / 77,0 % | 6,3 / 5,4 / 6,1 |
| `fashion` | 16 / 8 / 4 | 90,3 / 90,0 / 88,4 % | 84,5 / 83,9 / 82,4 % | 5,8 / 6,1 / 6,0 |

**Lección:** la red memoriza con pocos filtros igual (con 4 filtros `formas` sigue acertando 94,9 % en entrenamiento). El problema no es el tamaño, es que **hay pocas imágenes y la red se las aprende**.

### La escalera: de lo que más ayudó a lo que menos

Valores de validación (media de 3 semillas, hasta 60 épocas con parada por validación). «Más datos» usa **4 veces** más imágenes (la validación también es mayor, así que la comparación es orientativa).

| Palanca | `formas` | `fashion_parecidas` | `fashion` | En una frase |
|---|--:|--:|--:|---|
| **Base** | 82,4 % | 78,5 % | 84,5 % | De donde partimos |
| **1. Más datos** | **94,3 %** (+11,9) | **83,9 %** (+5,4) | **88,7 %** (+4,2) | La mejor palanca. Hueco: 11,9 → 3,9 · 6,3 → 5,0 · 5,8 → 3,6 |
| **2. Dropout 0,3–0,5** | **88,2 %** (+5,8) | **81,5 %** (+3,0) | **85,6 %** (+1,1) | Sube la validación aunque el hueco apenas se mueva |
| 3. Aumento de datos | 78,4 % (−4,0) | 70,7 % (−7,8) | 77,1 % (−7,4) | Cierra el hueco pero **baja** la validación (aquí) |
| 4. Regularización L2 (1e-3) | 80,8 % (−1,6) | 77,5 % (−1,0) | 83,1 % (−1,4) | No aporta |
| 5. Pooling global en vez de aplanar | 74,3 % (−8,1) | 68,6 % (−9,9) | 73,7 % (−10,8) | Red demasiado pequeña: infraajuste |
| 6. Todo junto (GAP + Dropout + aumento) | 49,8 % | 52,2 % | 54,6 % | Frena tanto que no aprende |

**Cómo se lee:**
1. **Más datos** es la solución real. Si no se pueden conseguir de verdad, se **fabrican** con aumento (palanca 3) y se deja entrenar más épocas.
2. **Dropout** (apagar al azar neuronas al entrenar para que ninguna se aprenda una foto concreta): primera palanca barata. Probar 0,3 y 0,5; 0,5 tarda más épocas en llegar a su mejor momento (43–49 frente a 13–23 de la base).
3. **Aumento de datos**: cierra el hueco (`fashion_parecidas`: 6,3 → 0,5) pero con el tope de épocas del cuaderno **no llega a aprender** (entrenamiento 71 %). Con 4 veces más imágenes mejora, pero sigue por debajo de no usarlo (79,1 % frente a 83,9 %). Aquí mover, girar y ampliar no se parece a cómo varían las imágenes reales del dataset (prendas centradas y del mismo tamaño), por eso no ayuda.
4. **Cuándo no frenar más:** cuando el hueco se acerca a 0 **y la validación baja**, hemos pasado de sobreajuste a infraajuste (señal: el entrenamiento también baja).
5. **Parar antes** ya lo hace el cuaderno (EarlyStopping con la mejor época).
6. **Menos neuronas y menos filtros:** última opción; solo tiene sentido si la red es claramente enorme para tan pocas imágenes.

### Si nada de eso mejora la validación
- **El límite puede estar en los datos, no en la red.** `fashion_parecidas` con 4 veces más datos queda en 83,9 %: sus clases (camiseta, jersey, abrigo, camisa) se parecen mucho a 28×28.
  - Mirar los errores uno a uno: ¿etiqueta dudosa? ¿imagen ambigua?
  - Más resolución o más información (color) si el problema lo permite.
  - Añadir una salida «no sé»: un umbral de confianza (como en S11_04).
- **Usar una red preentrenada** (transfer learning, S11_02): ya sabe ver formas y texturas, y con pocas imágenes es la opción que más gana (ver `S11_05_imagenet_mini_retos`).
- **Cambiar la métrica de éxito:** si lo que importa es la peor clase, mirar el recall de esa clase y no la media.
- **Contarlo honestamente en la presentación:** «sigue habiendo un hueco de X puntos; probamos A, B y C; solo B mejoró la validación».

### Lo que hay que **no** hacer
- Elegir palanca mirando la **prueba** (se mira una sola vez, al final).
- Dar por buena una mejora de 1–2 puntos con validación pequeña: repetir con otras semillas (`SEMILLA`) antes de afirmar nada.
- Juntar todas las palancas «por si acaso»: la fila 6 de la tabla lo demuestra (el 50 % de `formas`).

---

## 4 · Celda opcional para el cuaderno (probada)

Pegar **después** de las celdas ⚙️ de datos (usa `X`, `N_CLASES`, `X_ent`… del cuaderno). Cada palanca es un valor que se cambia; el resultado muestra el hueco.

```python
from tensorflow import keras
L, R = keras.layers, keras.regularizers

def construir_ext(filtros=16, dropout=0.0, l2=0.0, gap=False, aumento=False):
    """CNN del cuaderno con 'palancas' contra el sobreajuste. Con todo a cero/False es la variante «cnn»."""
    reg = R.l2(l2) if l2 else None
    capas = [L.Input(shape=X.shape[1:])]
    if aumento:                                   # imágenes movidas, giradas y ampliadas un poco
        capas += [L.RandomTranslation(0.1, 0.1), L.RandomRotation(0.05), L.RandomZoom(0.1)]
    capas += [L.Conv2D(filtros, 3, padding="same", activation="relu", kernel_regularizer=reg), L.MaxPooling2D(),
              L.Conv2D(filtros * 2, 3, padding="same", activation="relu", kernel_regularizer=reg), L.MaxPooling2D()]
    capas += [L.GlobalAveragePooling2D() if gap else L.Flatten()]
    if dropout: capas += [L.Dropout(dropout)]     # apaga neuronas al azar al entrenar
    capas += [L.Dense(32, activation="relu", kernel_regularizer=reg)]
    if dropout: capas += [L.Dropout(dropout)]
    capas += [L.Dense(N_CLASES, activation="softmax")]
    m = keras.Sequential(capas)
    m.compile(optimizer=keras.optimizers.Adam(1e-3), loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return m

def probar_ext(nombre, **palancas):
    keras.utils.set_random_seed(SEMILLA)
    m = construir_ext(**palancas)
    parar = keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)
    m.fit(X_ent, y_ent, validation_data=(X_val, y_val), epochs=60, batch_size=64, callbacks=[parar], verbose=0)
    ent = m.evaluate(X_ent, y_ent, verbose=0)[1]; val = m.evaluate(X_val, y_val, verbose=0)[1]
    print(f"{nombre:<28} entrenamiento {ent:.1%} · validación {val:.1%} · hueco {100*(ent-val):+.1f} puntos")
    return m

probar_ext("base")
probar_ext("menos filtros", filtros=8)
probar_ext("Dropout 0.3", dropout=0.3)
probar_ext("aumento", aumento=True)
```

Con `PROBLEMA = "formas"` y semilla 42 sale: base 95,6 % / **86,6 %** / hueco +9,1 · 8 filtros 93,4 % / 78,1 % / +15,3 · **Dropout 0,3 98,4 % / 91,3 % / +7,2**. Con una sola semilla hay ±3 puntos de ruido (sección 3 usa la media de 3).

**Más datos** (en `formas`): en la celda de datos cambiar `generar_lote(dibujar_forma, CLASES_FORMAS, 200)` por `…, 600)` (de 1 600 a 4 800 imágenes) y volver a ejecutar desde ahí; en los problemas de Keras, subir `MAX_IMAGENES` (hasta 24 000 en `fashion_parecidas`).

---

## 5 · Preguntas frecuentes del alumnado
- **«¿Por qué mi validación es mejor que mi entrenamiento?»** Con aumento o Dropout, durante el entrenamiento se «estropean» las imágenes o se apagan neuronas; al medir se usa la red completa. Es normal con esos trucos.
- **«¿Por qué sale distinto cada vez?»** Los pesos empiezan al azar; con `SEMILLA` fija suele salir igual, pero puede variar entre equipos o versiones de TensorFlow. Con validaciones de 300 imágenes, ±3 puntos es ruido.
- **«¿Puedo usar los 3 trucos a la vez?»** Se pueden, pero cada uno frena la red; se prueba uno cada vez y se queda el que **sube la validación**.
- **«¿Y si la prueba sale peor que la validación?»** Poco (1–2 puntos) es normal. Mucho indica que se ha elegido demasiado mirando la validación: decirlo en la presentación.
- **«Mi red saca 100 %, ¿gano?»** No: pregunta si el problema es tan fácil que cualquier red lo acierta y si valdría con imágenes reales.
