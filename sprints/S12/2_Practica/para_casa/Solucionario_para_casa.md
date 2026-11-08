# Solucionario · cuadernos completos («para casa») del Sprint 12

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S12_01` a `S12_07`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).

---

## S12_01 · Series temporales: baseline, descomposición y ARIMA/SARIMAX

### A4 · EJERCICIO 1 de 4 — Día de más ocupación y mes de menos

> ¿Qué día de la semana tiene más ocupación media y qué mes tiene menos?
> Guarda el nombre del día en `dia_max` (texto, p. ej. `"sáb"`) y el número de mes en `mes_min` (entero de 1 a 12).

```python
dia_max = por_dia.idxmax()
mes_min = int(por_mes.idxmin())
```

**Valores que tienen que salir:**

```text
dia_max = 'sáb'
mes_min = 9
```

### A7 · EJERCICIO 2 de 4 — Baseline: media de las últimas 4 semanas

> Un tercer baseline: la **media de las últimas 4 semanas** para cada día de la semana
> (más estable que copiar solo la última semana). Completa `pred_media4`: debe devolver 7 valores, uno por día,
> promediando `historia.iloc[-7]`, `historia.iloc[-14]`, `historia.iloc[-21]` y `historia.iloc[-28]`, y así para
> cada día de la semana siguiente. Después se calcula `mae_media4`.

```python
def pred_media4(historia, o):
    ultimas = historia.iloc[-28:].values.reshape(4, 7)
    return ultimas.mean(axis=0)

mae_media4, p_media4 = evaluar_semanal(pred_media4)
print(f"MAE media 4 semanas: {mae_media4:.2f}")
```

**Tiene que salir:**

```text
MAE media 4 semanas: 4.45
```

### A9 · EJERCICIO 3 de 4 — Amplitud semanal y resto

> ¿Cuánta de la variación se explica por la estacionalidad semanal? Calcula en `amplitud_semanal`
> la diferencia entre el mayor y el menor efecto estacional (`desc.seasonal.max() - desc.seasonal.min()`),
> redondeada a 1 decimal, y guarda en `resto_std` la desviación típica del resto (sin NaN).

```python
amplitud_semanal = round(float(desc.seasonal.max() - desc.seasonal.min()), 1)
resto_std = float(desc.resid.dropna().std())
```

**Valores que tienen que salir:**

```text
amplitud_semanal = 9.4
resto_std = 3.6693
```

### A12 · EJERCICIO 4 de 4 — SARIMAX sin exógenas

> Prueba una segunda especificación **sin** los festivos ni Fourier (solo `order=(1,0,1)`, `seasonal_order=(1,1,1,7)`)
> y compara. Guarda su MAE en `mae_sin_exog`. Pista: `SARIMAX(entrenamiento, order=..., seasonal_order=...)`,
> y en `res2.apply(historia, refit=False)` no hay `exog`.

```python
res2 = SARIMAX(entrenamiento, order=(1, 0, 1), seasonal_order=(1, 1, 1, 7),
               enforce_stationarity=False, enforce_invertibility=False).fit(disp=False, maxiter=200)

def pred_sarimax_simple(historia, o):
    return res2.apply(historia, refit=False).forecast(HORIZONTE).values

mae_sin_exog, _ = evaluar_semanal(pred_sarimax_simple)
print(f"MAE SARIMAX sin exógenas: {mae_sin_exog:.2f}  |  con exógenas: {mae_sar:.2f}")
```

**Tiene que salir:**

```text
MAE SARIMAX sin exógenas: 3.93  |  con exógenas: 3.18
```

### A14 · MINI-RETO — El número de control para la dirección

> La dirección pide un **número de control**: ¿cuánto mejora (en %) el mejor modelo respecto al mejor baseline?
> Guarda en `mejor_baseline` el menor MAE entre los tres baselines y en `mejora_pct` el porcentaje de mejora
> de `mae_sar` respecto a él (`100 * (baseline - modelo) / baseline`, redondeado a 1 decimal; puede ser negativo).
> Escribe además en `conclusion` una frase (texto) para el cliente.

```python
mejor_baseline = min(mae_ing, mae_est, mae_media4)
mejora_pct = round(100 * (mejor_baseline - mae_sar) / mejor_baseline, 1)
conclusion = (f"El modelo SARIMAX se equivoca de media {mae_sar:.1f} puntos de ocupación a 7 días, "
              f"un {mejora_pct}% respecto al mejor método simple.")
print(conclusion)
```

**Tiene que salir:**

```text
El modelo SARIMAX se equivoca de media 3.2 puntos de ocupación a 7 días, un 28.5% respecto al mejor método simple.
```

---

## S12_02 · Redes recurrentes (RNN, LSTM, GRU) para predecir la ocupación

### A4 · EJERCICIO 1 de 3 — Escalar sin fuga de datos

> Crea `escalador = MinMaxScaler()`, ajústalo con la columna de ocupación de las primeras `n_ent` filas
> y guarda en `ocup_esc` la ocupación de **toda** la serie transformada (array de una dimensión).

```python
escalador = MinMaxScaler()
escalador.fit(df[["ocupacion"]].iloc[:n_ent])
ocup_esc = escalador.transform(df[["ocupacion"]]).ravel()

X_feat = df.copy()
X_feat["ocupacion"] = ocup_esc
matriz = X_feat.values.astype("float32")          # (días, 6 variables)
objetivo = ocup_esc.astype("float32")             # lo que queremos predecir
print("Matriz de variables:", matriz.shape)
```

**Tiene que salir:**

```text
Matriz de variables: (1096, 6)
```

### A6 · EJERCICIO 2 de 3 — Crear las ventanas deslizantes

> Completa `crear_ventanas(origenes)`, que recibe una lista de posiciones `t` y devuelve
> `X` con forma `(n, 28, 6)` e `y` con forma `(n, 7)`.

```python
def crear_ventanas(origenes):
    X = np.array([matriz[t - VENTANA:t] for t in origenes], dtype="float32")
    y = np.array([objetivo[t:t + HORIZONTE] for t in origenes], dtype="float32")
    return X, y

# Orígenes de entrenamiento: todas las posiciones cuyo futuro (7 días) cae DENTRO del entrenamiento
orig_ent = list(range(VENTANA, n_ent - HORIZONTE + 1))
# Orígenes de prueba: igual que en S12_01, uno por semana
orig_test = [o for o in range(n_ent, len(df), HORIZONTE) if o + HORIZONTE <= len(df)]

X_ent, y_ent = crear_ventanas(orig_ent)
X_test, y_test = crear_ventanas(orig_test)
print("Entrenamiento:", X_ent.shape, y_ent.shape, "| Prueba:", X_test.shape, y_test.shape)
```

**Tiene que salir:**

```text
Entrenamiento: (971, 28, 6) (971, 7) | Prueba: (13, 28, 6) (13, 7)
```

### A10 · EJERCICIO 3 de 3 — Entrenar SimpleRNN, LSTM y GRU

> Entrena las tres redes en un diccionario `modelos` con claves `"SimpleRNN"`, `"LSTM"` y `"GRU"`,
> donde cada valor es la tupla `(modelo, historial)` que devuelve `entrenar`. Después se calcula el MAE de cada una en `resultados`.

```python
modelos = {nombre: entrenar(nombre) for nombre in ["SimpleRNN", "LSTM", "GRU"]}

resultados = {}
for nombre, (m, h) in modelos.items():
    pred = m.predict(X_test, verbose=0)
    resultados[nombre] = mae_puntos(y_test, pred)
    print(f"{nombre:10s} MAE prueba: {resultados[nombre]:.2f} puntos | épocas: {len(h.history['loss'])}")
print(f"{'Baseline':10s} MAE prueba: {mae_base:.2f} puntos")

fig, ejes = plt.subplots(1, 3, figsize=(12, 3), sharey=True)
for ax, (nombre, (m, h)) in zip(ejes, modelos.items()):
    ax.plot(h.history["loss"], label="entrenamiento"); ax.plot(h.history["val_loss"], label="validación")
    ax.set_title(nombre); ax.set_xlabel("Época")
ejes[0].set_ylabel("Error (MAE, escala 0-1)"); ejes[0].legend()
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
SimpleRNN  MAE prueba: 3.79 puntos | épocas: 31
LSTM       MAE prueba: 3.51 puntos | épocas: 15
GRU        MAE prueba: 3.28 puntos | épocas: 22
Baseline   MAE prueba: 4.46 puntos
```

Y además dibuja un gráfico.

### A13 · MINI-RETO — ¿Y si la ventana es demasiado corta?

> Comprueba cuánto **empeora** una red si la ventana es demasiado corta. Entrena una **GRU** con ventana de 7 días
> (en lugar de 28) y guarda su MAE en `mae_ventana7`.
> Pista: cambia `VENTANA` y vuelve a crear las ventanas con `crear_ventanas`; recuerda restaurarla al final para no romper el resto.
> Guarda en `ventana_larga_mejor` (True/False) si con 28 días la GRU ha ido mejor que con 7.

```python
VENTANA_ORIG = VENTANA
VENTANA = 7
X_ent7, y_ent7 = crear_ventanas(orig_ent)      # los orígenes son los mismos; solo cambia el largo de la ventana
X_test7, y_test7 = crear_ventanas(orig_test)
keras.utils.set_random_seed(SEMILLA)
m7 = keras.Sequential([layers.Input(shape=(7, 6)), layers.GRU(32), layers.Dense(HORIZONTE)])
m7.compile(optimizer=keras.optimizers.Adam(0.005), loss="mae")
m7.fit(X_ent7[:-60], y_ent7[:-60], validation_data=(X_ent7[-60:], y_ent7[-60:]), epochs=40, batch_size=32,
       callbacks=[keras.callbacks.EarlyStopping(patience=6, restore_best_weights=True)], verbose=0)
mae_ventana7 = mae_puntos(y_test7, m7.predict(X_test7, verbose=0))
VENTANA = VENTANA_ORIG
ventana_larga_mejor = bool(resultados["GRU"] < mae_ventana7)
print(f"GRU ventana 28: {resultados['GRU']:.2f} | GRU ventana 7: {mae_ventana7:.2f}")
```

**Tiene que salir:**

```text
GRU ventana 28: 3.28 | GRU ventana 7: 3.41
```

---

## S12_03 · NLP clásico: sentimiento y temas en las reseñas de TurisData

### A4 · EJERCICIO 1 de 5 — Limpiar un texto

> Completa `limpiar(texto)`: pasa a minúsculas, cambia todo lo que no sean letras (incluidas tildes y ñ) o espacios por un espacio,
> y colapsa espacios repetidos. Debe cumplir `limpiar("¡Qué BUENO!...  Sí") == "qué bueno sí"`.

```python
def limpiar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúüñ\s]", " ", texto)
    return " ".join(texto.split())

PALABRAS_VACIAS = {"a", "al", "con", "de", "del", "el", "en", "es", "esta", "estaba", "era", "fue", "la", "las", "lo", "los",
                   "me", "mi", "muy", "nos", "para", "por", "que", "se", "su", "un", "una", "y", "o", "u", "e"}

def tokenizar(texto, quitar_vacias=True):
    tokens = limpiar(texto).split()
    return [t for t in tokens if not (quitar_vacias and t in PALABRAS_VACIAS)]

print(tokenizar("La limpieza de la habitación era impecable!"))
resenas["limpio"] = resenas["texto"].apply(limpiar)
```

**Tiene que salir:**

```text
['limpieza', 'habitación', 'impecable']
```

### A6 · EJERCICIO 2 de 5 — Las 5 palabras más frecuentes

> ¿Cuáles son las 5 palabras (tokens, ya sin palabras vacías) más frecuentes de todo el corpus?
> Guarda en `top5` una lista de 5 tuplas `(palabra, veces)`. Pista: `collections.Counter` y `.most_common(5)`.

```python
from collections import Counter
contador = Counter(t for texto in resenas["texto"] for t in tokenizar(texto))
top5 = contador.most_common(5)
print(top5)
```

**Tiene que salir:**

```text
[('semana', 504), ('desayuno', 391), ('todo', 382), ('habitación', 284), ('escapada', 256)]
```

### A9 · EJERCICIO 3 de 5 — Regresión logística frente a Naive Bayes

> Crea y entrena dos modelos y guarda su exactitud en prueba:
> - `modelo_lr`: `TfidfVectorizer(preprocessor=limpiar)` + `LogisticRegression(max_iter=1000)` → `acc_lr`
> - `modelo_nb`: `CountVectorizer(preprocessor=limpiar)` + `MultinomialNB()` → `acc_nb`
> Usa `make_pipeline(vectorizador, clasificador)` y `.fit(X_ent, y_ent)`.

```python
modelo_lr = make_pipeline(TfidfVectorizer(preprocessor=limpiar), LogisticRegression(max_iter=1000)).fit(X_ent, y_ent)
modelo_nb = make_pipeline(CountVectorizer(preprocessor=limpiar), MultinomialNB()).fit(X_ent, y_ent)
acc_lr = accuracy_score(y_test, modelo_lr.predict(X_test))
acc_nb = accuracy_score(y_test, modelo_nb.predict(X_test))
print(f"Regresión logística + TF-IDF : {acc_lr:.3f}")
print(f"Naive Bayes + bolsa de palabras: {acc_nb:.3f}")
baseline = y_test.value_counts(normalize=True).max()
print(f"(Un clasificador que siempre dice la clase mayoritaria acertaría {baseline:.3f})")

print(classification_report(y_test, modelo_lr.predict(X_test)))
fig, ax = plt.subplots(figsize=(4.5, 4))
ConfusionMatrixDisplay.from_predictions(y_test, modelo_lr.predict(X_test), ax=ax, cmap="Blues", colorbar=False)
ax.set_title("Matriz de confusión (regresión logística)"); ax.set_xlabel("Predicho"); ax.set_ylabel("Real"); ax.grid(False)
plt.show()
```

**Tiene que salir:**

```text
Regresión logística + TF-IDF : 0.992
Naive Bayes + bolsa de palabras: 0.989
(Un clasificador que siempre dice la clase mayoritaria acertaría 0.469)
              precision    recall  f1-score   support
    negativo       0.98      1.00      0.99       120
      neutro       1.00      0.96      0.98        79
    positivo       1.00      1.00      1.00       176
    accuracy                           0.99       375
   macro avg       0.99      0.99      0.99       375
weighted avg       0.99      0.99      0.99       375
```

Y además dibuja un gráfico.

### A13 · EJERCICIO 4 de 5 — ¿Falla con las negaciones?

> Observa los resultados y escribe en `falla_negacion` (True/False) si el modelo trata igual las frases
> "con negación" que las "sin negación" (es decir, ¿se equivoca con "no es impecable"?). Después, en `bigrama_util`, escribe
> (texto) por qué usar **bigramas** (`ngram_range=(1, 2)`) podría ayudar en una frase.
> Pista: los bigramas conservan pares como "no es".

```python
falla_negacion = modelo_lr.predict([pruebas[1]])[0] == "positivo"
bigrama_util = "Un bigrama junta dos palabras seguidas (p. ej. «no es»), así conserva parte del orden y de la negación."
```

**Valores que tienen que salir:**

```text
falla_negacion = True
bigrama_util = 'Un bigrama junta dos palabras seguidas (p. ej. «no es»), así conserva parte del orden y de la negación.'
```

### A15 · EJERCICIO 5 de 5 — El tema peor detectado

> ¿Cuál es el tema con peor F1 (`tema_peor`, texto) y cuántas reseñas del corpus mencionan **realmente** el tema `precio`
> (`n_precio`, entero, usando `temas_reales`)?
> Después mira los casos donde falla ese tema y decide qué cambio harías en el diccionario (¿quitar una clave demasiado amplia? ¿añadir otra?).

```python
tema_peor = f1_por_tema.idxmin()
n_precio = int(resenas["temas_reales"].apply(lambda l: "precio" in l).sum())
print("Tema peor:", tema_peor, "| n precio:", n_precio)

errores = resenas[resenas["temas_reales"].apply(lambda l: tema_peor in l) != resenas["temas_detectados"].apply(lambda l: tema_peor in l)]
print(f"{len(errores)} reseñas donde falla «{tema_peor}». Ejemplos:")
for _, fila in errores.head(5).iterrows():
    print("-", fila["texto"], "| real:", fila["temas_reales"], "| detectado:", fila["temas_detectados"])
```

**Tiene que salir:**

```text
Tema peor: ruido | n precio: 455
55 reseñas donde falla «ruido». Ejemplos:
- Viajamos en familia. La zona es ruidosa y poco segura de noche. No compensa el precio. El desayuno era escaso y repetitivo. | real: ['desayuno', 'precio', 'ubicacion'] | detectado: ['desayuno', 'precio', 'ruido', 'ubicacion']
- Viajamos en familia. La limpieza deja mucho que desear. La zona es ruidosa y poco segura de noche... | real: ['limpieza', 'ubicacion'] | detectado: ['limpieza', 'ruido', 'ubicacion']
- Viajamos en familia. Demasiado caro para lo que ofrece. El personal fue borde. La zona es ruidosa y poco segura de noche. | real: ['personal', 'precio', 'ubicacion'] | detectado: ['personal', 'precio', 'ruido', 'ubicacion']
```

### A18 · MINI-RETO — Panel de quejas por tema

> Construye `quejas`, una serie con el **número de reseñas negativas por tema** (usa `temas_detectados` y solo reseñas con `sentimiento == "negativo"`),
> ordenada de mayor a menor. Dibuja un gráfico de barras y guarda en `queja_principal` el tema más frecuente.
> **Antes de fiarte del resultado:** `temas_detectados` sale del diccionario de palabras clave, no de las etiquetas del corpus. Compara tu `quejas` con `resenas.loc[resenas["sentimiento"] == "negativo", "temas_reales"].explode().value_counts()`: si el tema principal no coincide, la lista de palabras de ese tema es demasiado amplia (recuerda el ejercicio 5).

```python
quejas = resenas.loc[resenas["sentimiento"] == "negativo", "temas_detectados"].explode().value_counts()
queja_principal = quejas.index[0]
fig, ax = plt.subplots()
quejas.sort_values().plot.barh(ax=ax, color="#c0463a")
ax.set_title("Reseñas negativas por tema"); ax.set_xlabel("Número de reseñas")
plt.show()
```

**Tiene que salir:** un gráfico.

---

## S12_04 · Embeddings: representar el significado con vectores (LSA)

### A4 · EJERCICIO 1 de 3 — Reducir a 12 dimensiones con LSA

> Reduce `M` a **12 dimensiones** con `TruncatedSVD(n_components=12, random_state=SEMILLA)`.
> Guarda el modelo en `lsa` y los vectores de las reseñas en `Z` (forma `(1500, 12)`).
> Guarda también en `var_explicada` la suma de la varianza explicada (`lsa.explained_variance_ratio_.sum()`).

```python
lsa = TruncatedSVD(n_components=12, random_state=SEMILLA)
Z = lsa.fit_transform(M)
var_explicada = float(lsa.explained_variance_ratio_.sum())
print("Forma de Z:", Z.shape, "| varianza explicada con 12 ejes:", round(var_explicada, 3))
```

**Tiene que salir:**

```text
Forma de Z: (1500, 12) | varianza explicada con 12 ejes: 0.438
```

### A7 · EJERCICIO 2 de 3 — Las reseñas más parecidas a una dada

> Completa `parecidas(i, k=3)`: devuelve los índices de las `k` reseñas más parecidas (por coseno sobre `Z`)
> a la reseña número `i`, **excluyendo la propia `i`**, de más a menos parecida.

```python
def parecidas(i, k=3):
    sim = cosine_similarity([Z[i]], Z)[0]
    sim[i] = -1
    return list(np.argsort(sim)[::-1][:k])

vecinas = parecidas(0, 3)
print("Reseña 0:", resenas.loc[0, "texto"])
for j in vecinas:
    print("  ≈", resenas.loc[j, "texto"])
sim0 = cosine_similarity([Z[0]], Z)[0]
```

**Tiene que salir:**

```text
Reseña 0: Escapada de fin de semana. La música del bar no nos dejó dormir. Vistas al mar increíbles. Estancia normal, sin más!
  ≈ Fuimos por trabajo. Vistas al mar increíbles.
  ≈ Viajamos en familia. Vistas al mar increíbles.
  ≈ Pasamos una semana aquí. Vistas al mar increíbles.
```

### A10 · EJERCICIO 3 de 3 — LSA de 12 columnas frente a TF-IDF completo

> Parte los datos en entrenamiento y prueba (ya hecho abajo). Ajusta `tfidf_e` y `lsa_e` **solo con `X_ent`**, entrena una
> regresión logística sobre los vectores LSA de entrenamiento y guarda en `acc_lsa` la exactitud en prueba.

```python
X_ent, X_test, y_ent, y_test = train_test_split(resenas["texto"], resenas["sentimiento"], test_size=0.25,
                                                stratify=resenas["sentimiento"], random_state=SEMILLA)
tfidf_e = TfidfVectorizer(preprocessor=limpiar, min_df=2)
Me_ent = tfidf_e.fit_transform(X_ent)
Me_test = tfidf_e.transform(X_test)
lsa_e = TruncatedSVD(n_components=12, random_state=SEMILLA)
Ze_ent = lsa_e.fit_transform(Me_ent)
Ze_test = lsa_e.transform(Me_test)
clf_lsa = LogisticRegression(max_iter=1000).fit(Ze_ent, y_ent)
acc_lsa = accuracy_score(y_test, clf_lsa.predict(Ze_test))
clf_tfidf = LogisticRegression(max_iter=1000).fit(Me_ent, y_ent)
acc_tfidf = accuracy_score(y_test, clf_tfidf.predict(Me_test))
print(f"TF-IDF completo ({Me_ent.shape[1]} columnas): {acc_tfidf:.3f}")
print(f"LSA (12 columnas)                : {acc_lsa:.3f}")
```

**Tiene que salir:**

```text
TF-IDF completo (105 columnas): 0.995
LSA (12 columnas)                : 0.891
```

### A11 · MINI-RETO — Buscador semántico de reseñas

> Crea `buscar(consulta, k=3)`: convierte la consulta al espacio LSA (`tfidf.transform` y `lsa.transform`; usa `limpiar` como ya está en `tfidf`),
> calcula el coseno con `Z` y devuelve los `k` textos más parecidos. Prueba con `"no me dejó dormir el ruido"`.

```python
def buscar(consulta, k=3):
    q = lsa.transform(tfidf.transform([consulta]))
    sim = cosine_similarity(q, Z)[0]
    return [resenas.loc[i, "texto"] for i in np.argsort(sim)[::-1][:k]]

hallazgos = buscar("no me dejó dormir el ruido")
for h in hallazgos:
    print("-", h)
```

**Tiene que salir:**

```text
- Pasamos una semana aquí. No compensa el precio. Ruido constante por la noche. Encontramos pelos en el baño...
- En general, Ruido constante por la noche. No compensa el precio. Encontramos pelos en el baño.
- No compensa el precio. Ruido constante por la noche. Tardaron una hora en resolver un problema simple...
```

---

## S12_05 · Transformers y LLM: tokenización y atención paso a paso

### A3 · EJERCICIO 1 de 6 — El par de letras más común

> Comprueba que `contar_pares` funciona: calcula `pares` sobre las palabras del corpus troceadas en letras
> (`[list(p) for p in corpus]`) y guarda en `par_mas_comun` el par más frecuente (una tupla de 2 letras).

```python
pares = contar_pares([list(p) for p in corpus])
par_mas_comun = pares.most_common(1)[0][0]
print("Par más común:", par_mas_comun, "→", pares[par_mas_comun], "veces")

def entrenar_bpe(palabras, n_fusiones):
    """Aplica n_fusiones: en cada paso fusiona el par más frecuente en un solo símbolo."""
    palabras = [list(p) for p in palabras]
    fusiones = []
    for _ in range(n_fusiones):
        pares = contar_pares(palabras)
        if not pares:
            break
        a, b = pares.most_common(1)[0][0]
        fusiones.append((a, b))
        nuevas = []
        for simbolos in palabras:
            i, salida = 0, []
            while i < len(simbolos):
                if i < len(simbolos) - 1 and simbolos[i] == a and simbolos[i + 1] == b:
                    salida.append(a + b); i += 2
                else:
                    salida.append(simbolos[i]); i += 1
            nuevas.append(salida)
        palabras = nuevas
    return fusiones, palabras

fusiones, tokens = entrenar_bpe(corpus, 12)
print("Fusiones aprendidas:", fusiones)
for p, t in zip(corpus, tokens):
    print(f"{p:12s} → {t}")
```

**Tiene que salir:**

```text
Par más común: ('d', 'e') → 4 veces
Fusiones aprendidas: [('d', 'e'), ('de', 's'), ('des', 'a'), ('desa', 'y'), ('desay', 'u'), ('desayu', 'n'), ('l', 'i'), ('li', 'm'), ('lim', 'p'), ('limp', 'i'), ('o', 's'), ('desayun', 'a')]
desayuno     → ['desayun', 'o']
desayunos    → ['desayun', 'os']
desayunar    → ['desayuna', 'r']
limpio       → ['limpi', 'o']
limpieza     → ['limpi', 'e', 'z', 'a']
limpiar      → ['limpi', 'a', 'r']
limpiamos    → ['limpi', 'a', 'm', 'os']
desayunamos  → ['desayuna', 'm', 'os']
```

### A5 · EJERCICIO 2 de 6 — Razón de compresión del BPE

> Cuenta cuántos tokens hay en total tras las 12 fusiones (`n_tokens_bpe`) y cuántas letras tenía el corpus (`n_letras`).
> ¿Cuál es la **razón de compresión** (`n_letras / n_tokens_bpe`, redondeada a 2 decimales) en `compresion`?

```python
n_tokens_bpe = sum(len(t) for t in tokens)
n_letras = sum(len(p) for p in corpus)
compresion = round(n_letras / n_tokens_bpe, 2)
print(f"{n_letras} letras → {n_tokens_bpe} tokens (compresión {compresion}x)")
```

**Tiene que salir:**

```text
67 letras → 22 tokens (compresión 3.05x)
```

### A8 · EJERCICIO 3 de 6 — Escribir softmax por filas

> Escribe `softmax(m)` que aplique el softmax **por filas** a una matriz (resta el máximo de cada fila antes
> de exponenciar, por estabilidad numérica).

```python
def softmax(m):
    e = np.exp(m - m.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)

_p = softmax(np.array([[1., 2., 3.], [0., 0., 0.]]))

d = K.shape[1]
pesos = softmax(puntuaciones / np.sqrt(d))
print("Pesos de atención (cada fila suma 1):\n", pesos)
```

**Tiene que salir:**

```text
Pesos de atención (cada fila suma 1):
 [[0.11 0.45 0.45]
 [0.05 0.89 0.05]
 [0.09 0.73 0.18]]
```

### A10 · EJERCICIO 4 de 6 — La función de atención completa

> Completa `atencion(X, Wq, Wk, Wv)` que devuelve `(salida, pesos)` siguiendo los 4 pasos.

```python
def atencion(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    pesos = softmax(Q @ K.T / np.sqrt(K.shape[1]))
    return pesos @ V, pesos

salida, pesos2 = atencion(X, Wq, Wk, Wv)
print("Salida:\n", salida)

fig, ax = plt.subplots(figsize=(4.5, 4))
im = ax.imshow(pesos, cmap="Blues", vmin=0, vmax=1)
ax.set_xticks(range(3)); ax.set_xticklabels(palabras); ax.set_yticks(range(3)); ax.set_yticklabels(palabras)
for i in range(3):
    for j in range(3):
        ax.text(j, i, f"{pesos[i, j]:.2f}", ha="center", va="center", color="black" if pesos[i, j] < .6 else "white")
ax.set_xlabel("Mira a…"); ax.set_ylabel("Palabra que pregunta"); ax.set_title("Pesos de atención")
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Salida:
 [[0.66 3.78]
 [0.16 3.89]
 [0.35 3.82]]
```

Y además dibuja un gráfico.

### A12 · EJERCICIO 5 de 6 — Atención con máscara causal

> Completa `atencion_causal(X, Wq, Wk, Wv)`: igual que `atencion`, pero antes del softmax
> pon `-1e9` en las posiciones **por encima de la diagonal** (`np.triu(..., k=1)`).

```python
def atencion_causal(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    p = Q @ K.T / np.sqrt(K.shape[1])
    mascara = np.triu(np.ones_like(p), k=1) == 1
    p[mascara] = -1e9
    pesos = softmax(p)
    return pesos @ V, pesos

_, pesos_c = atencion_causal(X, Wq, Wk, Wv)
print(pesos_c)
```

**Tiene que salir:**

```text
[[1.   0.   0.  ]
 [0.06 0.94 0.  ]
 [0.09 0.73 0.18]]
```

### A14 · EJERCICIO 6 de 6 — Probabilidad máxima con T baja y alta

> Calcula `prob_max_T03` (la probabilidad del token más probable con `T = 0.3`) y `prob_max_T25` (con `T = 2.5`).
> ¿Cuál de las dos es mayor? Escribe la respuesta en `mas_seguro`: `"T baja"` o `"T alta"`.

```python
prob_max_T03 = float(softmax(logits / 0.3).max())
prob_max_T25 = float(softmax(logits / 2.5).max())
mas_seguro = "T baja" if prob_max_T03 > prob_max_T25 else "T alta"
print(round(prob_max_T03, 3), round(prob_max_T25, 3), mas_seguro)
```

**Tiene que salir:**

```text
0.816 0.302 T baja
```

### A15 · MINI-RETO — Que «hotel» preste más atención a «limpio»

> Con las mismas matrices Wq, Wk y Wv, modifica el embedding de "limpio" para que la palabra "hotel" le **preste más atención**.
> Crea `X2` (una copia de `X` con la fila de "limpio", índice 2, cambiada) para que `pesos_nuevos[0, 2]` (cuánto mira "hotel" a "limpio") sea **mayor** que `pesos[0, 2]`
> (la atención original). Guarda en `subio` (True/False) el resultado de la comparación.

```python
X2 = X.copy()
X2[2] = X2[2] * 2
_, pesos_nuevos = atencion(X2, Wq, Wk, Wv)
subio = bool(pesos_nuevos[0, 2] > pesos[0, 2])
print("Antes:", round(float(pesos[0, 2]), 3), "| Ahora:", round(float(pesos_nuevos[0, 2]), 3))
```

**Tiene que salir:**

```text
Antes: 0.446 | Ahora: 0.932
```

---

## S12_06 · Mini RAG: un asistente que responde con la política del alojamiento

### A3 · EJERCICIO 1 de 6 — Trocear la política en frases

> Completa `trocear(texto)`: recorre las líneas, detecta las secciones (`## Título`), ignora líneas vacías y el título `# ...`,
> quita los asteriscos `**` y separa cada línea en frases (`re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ])", linea)`).
> Devuelve una lista de diccionarios `{"seccion": ..., "texto": ...}`.

```python
def trocear(texto):
    fragmentos, seccion = [], None
    for linea in texto.splitlines():
        linea = linea.strip().replace("**", "")
        if not linea or linea.startswith("# "):
            continue
        if linea.startswith("## "):
            seccion = linea[3:]
            continue
        for frase in re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ])", linea):
            if frase.strip():
                fragmentos.append({"seccion": seccion, "texto": frase.strip()})
    return fragmentos

fragmentos = trocear(politica)
print(len(fragmentos), "fragmentos. Ejemplo:", fragmentos[3])
```

**Tiene que salir:**

```text
25 fragmentos. Ejemplo: {'seccion': '1. Reservas y cancelaciones', 'texto': 'Si el cliente ha pagado un depósito parcial, se devuelve íntegro en las cancelaciones gratuitas.'}
```

### A5 · EJERCICIO 2 de 6 — Recuperar los fragmentos más parecidos

> Completa `recuperar(pregunta, k=3)`: devuelve una lista de `(puntuación, fragmento)` con los `k` fragmentos más parecidos,
> de mayor a menor puntuación.

```python
def recuperar(pregunta, k=3):
    sim = cosine_similarity(vectorizador.transform([pregunta]), matriz)[0]
    orden = np.argsort(sim)[::-1][:k]
    return [(float(sim[i]), fragmentos[i]) for i in orden]

for p, f in recuperar("¿Admiten perros?", 2):
    print(f"{p:.2f} | {f['seccion']} | {f['texto']}")
_r = recuperar("¿A qué hora es el check-in?", 3)
```

**Tiene que salir:**

```text
0.41 | 3. Mascotas | Se admiten perros y gatos de hasta 10 kg en los apartamentos, con un suplemento de 15 euros por estancia.
0.23 | 3. Mascotas | No se admiten mascotas en las suites.
```

### A7 · EJERCICIO 3 de 6 — Expandir la consulta con sinónimos

> Completa `expandir(pregunta)`: añade al final de la pregunta las palabras del diccionario `SINONIMOS` cuya clave aparezca en ella
> (sin tildes y en minúsculas). Después se guarda la nueva `recuperar_exp`, y se mide `h1_exp`.

```python
SINONIMOS = {"dejar la habitacion": "salida check-out", "bebes": "ninos cuna", "bebe": "ninos cuna", "equipaje": "consigna maleta"}

def expandir(pregunta):
    base = quitar_tildes(pregunta)
    extras = [v for k, v in SINONIMOS.items() if k in base]
    return pregunta + " " + " ".join(extras) if extras else pregunta

if "_recuperar_base" not in globals():     # se guarda solo la primera vez: así esta celda se puede volver a ejecutar sin problema
    _recuperar_base = recuperar
def recuperar_exp(pregunta, k=3):
    return _recuperar_base(expandir(pregunta), k)

recuperar = recuperar_exp          # a partir de aquí, todo el pipeline usa la consulta expandida
h1_exp, h3_exp, fallos_exp = evaluar_recuperacion()
print(f"Con expansión → 1.ª posición: {h1_exp:.0%} (antes {h1:.0%}) | entre los 3 primeros: {h3_exp:.0%}")
```

**Tiene que salir:**

```text
Con expansión → 1.ª posición: 95% (antes 84%) | entre los 3 primeros: 100%
```

### A12 · EJERCICIO 4 de 6 — El asistente completo con umbral

> Completa `responder(pregunta, umbral=0.15, k=3)`. Devuelve un diccionario con: `"respuesta"` (texto),
> `"fragmentos"` (lista de fragmentos usados) y `"puntuacion"` (la del mejor fragmento).
> Si `puntuacion < umbral`, la respuesta es `FRASE_NO_CONSTA` y no se llama a `generar`.

```python
def responder(pregunta, umbral=0.15, k=3):
    recuperados = recuperar(pregunta, k)
    mejor = recuperados[0][0]
    if mejor < umbral:
        return {"respuesta": FRASE_NO_CONSTA, "fragmentos": [], "puntuacion": mejor}
    respuesta = generar(construir_prompt(pregunta, recuperados))
    return {"respuesta": respuesta, "fragmentos": [f for _, f in recuperados], "puntuacion": mejor}

demo = responder("¿Se admiten mascotas en las suites?")
print(demo["respuesta"], "| puntuación:", round(demo["puntuacion"], 2))
```

**Tiene que salir:**

```text
No se admiten mascotas en las suites. [1] (Fuente: 3. Mascotas) | puntuación: 0.89
```

### A13 · EJERCICIO 5 de 6 — Detectar una alucinación

> Completa `es_alucinacion(respuesta, fragmentos, sin_respuesta)`. Pista para las cifras: `re.findall(r"\d+(?::\d+)?", texto)`.

```python
def es_alucinacion(respuesta, fragmentos, sin_respuesta):
    if FRASE_NO_CONSTA.lower() in respuesta.lower():
        return False
    if sin_respuesta:
        return True
    contexto = " ".join(f["texto"] for f in fragmentos)
    solo_texto = re.sub(r"\[\d+\]|\(Fuente:.*?\)", "", respuesta)      # las citas [1] y «(Fuente: 3. …)» no cuentan como cifras
    cifras_resp = set(re.findall(r"\d+(?::\d+)?", solo_texto))
    cifras_ctx = set(re.findall(r"\d+(?::\d+)?", contexto))
    return not cifras_resp <= cifras_ctx

_f = [{"seccion": "s", "texto": "La piscina abre de 9:00 a 20:00."}]

def evaluar(umbral=0.15, verboso=False):
    filas = []
    for (_, fila), clave in zip(preguntas.iterrows(), CLAVES):
        r = responder(fila["pregunta"], umbral)
        sin_resp = clave is None
        dice_no_consta = FRASE_NO_CONSTA.lower() in r["respuesta"].lower()
        acierto = dice_no_consta if sin_resp else (not dice_no_consta and contiene(clave, r["respuesta"]))
        sin_fuente = (not dice_no_consta) and ("[" not in r["respuesta"])
        alucina = es_alucinacion(r["respuesta"], r["fragmentos"], sin_resp)
        filas.append({"pregunta": fila["pregunta"], "acierto": acierto, "sin_fuente": sin_fuente, "alucinacion": alucina,
                      "respuesta": r["respuesta"]})
    df = pd.DataFrame(filas)
    if verboso:
        print(df[["pregunta", "acierto", "sin_fuente", "alucinacion"]].to_string())
    return df

res = evaluar(umbral=0.15)
print(f"Aciertos: {res['acierto'].sum()}/{len(res)} | sin fuente: {res['sin_fuente'].sum()} | alucinaciones: {res['alucinacion'].sum()}")
print("Fallos:", res.loc[~res["acierto"], "pregunta"].tolist())
```

**Tiene que salir:**

```text
Aciertos: 19/20 | sin fuente: 0 | alucinaciones: 0
Fallos: ['¿A qué hora es el desayuno?']
```

### A18 · EJERCICIO 6 de 6 — Un filtro de entradas sospechosas

> Completa `es_seguro(texto)`: devuelve `False` si el texto contiene señales típicas de inyección
> (por ejemplo «ignora las instrucciones», «olvida lo anterior», «system prompt», «eres ahora», «responde siempre que») y `True` en caso contrario.
> Usa `re.search` con `re.I` (mayúsculas/minúsculas) sobre `quitar_tildes(texto)`.

```python
PATRONES_SOSPECHOSOS = [r"ignora .{0,20}instrucciones", r"olvida .{0,20}(anterior|instrucciones)", r"system prompt", r"prompt del sistema",
                        r"eres ahora", r"responde siempre que"]

def es_seguro(texto):
    limpio = quitar_tildes(texto)
    return not any(re.search(p, limpio, re.I) for p in PATRONES_SOSPECHOSOS)

generador_simulado = generar_ingenuo
exitos_con_defensa = probar_ataques(generar_ingenuo, sanear_entrada=es_seguro)
generador_simulado = generar_simulado
print("Ataques que prosperan CON filtro:", sum(exitos_con_defensa), "de", len(exitos_con_defensa))
```

**Tiene que salir:**

```text
Ataques que prosperan CON filtro: 0 de 3
```

### A21 · MINI-RETO — ¿Qué umbral elegimos?

> El umbral es una decisión de negocio: **alto** = el asistente dice "no consta" más a menudo (seguro, pero menos útil);
> **bajo** = responde más (útil, pero arriesga alucinar). Evalúa los umbrales `[0.0, 0.1, 0.15, 0.3, 0.5]` y guarda en `tabla_umbral`
> un DataFrame con una fila por umbral y las columnas `umbral`, `aciertos`, `alucinaciones` (números enteros). Guarda en `umbral_elegido`
> el umbral que, entre los que dan **0 alucinaciones**, consigue más aciertos (si hay empate, el menor).

```python
filas = []
for u in [0.0, 0.1, 0.15, 0.3, 0.5]:
    r = evaluar(u)
    filas.append({"umbral": u, "aciertos": int(r["acierto"].sum()), "alucinaciones": int(r["alucinacion"].sum())})
tabla_umbral = pd.DataFrame(filas)
seguros = tabla_umbral[tabla_umbral["alucinaciones"] == 0]
umbral_elegido = float(seguros.sort_values(["aciertos", "umbral"], ascending=[False, True]).iloc[0]["umbral"])
print(tabla_umbral.to_string(index=False))
print("Umbral elegido:", umbral_elegido)
```

**Tiene que salir:**

```text
 umbral  aciertos  alucinaciones
   0.00        18              1
   0.10        19              0
   0.15        19              0
   0.30        18              0
   0.50        11              0
Umbral elegido: 0.1
```

---

## S12_07 · Autoencoders y modelos generativos (GAN y difusión)

### A3 · EJERCICIO 1 de 5 — Partir por orden temporal y escalar

> Reserva el **último 20 %** de las semanas para prueba (orden temporal, sin barajar) y **escala** con `MinMaxScaler`
> ajustado solo con las semanas de entrenamiento. Ya tienes `corte` (dónde acaba el entrenamiento). Guarda el escalador en `escalador` y las matrices ya escaladas (7 columnas) en `sem_ent` y `sem_test`.

```python
corte = int(0.8 * n_semanas)      # posición donde termina el entrenamiento y empieza la prueba
escalador = MinMaxScaler().fit(semanas[:corte])
sem_ent = escalador.transform(semanas[:corte])
sem_test = escalador.transform(semanas[corte:])
print("Entrenamiento:", sem_ent.shape, "| prueba:", sem_test.shape)
```

**Tiene que salir:**

```text
Entrenamiento: (124, 7) | prueba: (32, 7)
```

### A5 · EJERCICIO 2 de 5 — Entrenar el autoencoder

> Entrena `ae` con `sem_ent` como **entrada y objetivo** (¡el mismo array dos veces!), 150 épocas, `batch_size=16`, `verbose=0`,
> con el 15 % final como validación (`validation_split=0.15`). Guarda el historial en `historial`.

```python
historial = ae.fit(sem_ent, sem_ent, epochs=150, batch_size=16, validation_split=0.15, verbose=0)
print("Error final de entrenamiento:", round(historial.history["loss"][-1], 4), "| validación:", round(historial.history["val_loss"][-1], 4))

fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(historial.history["loss"], label="entrenamiento"); ax.plot(historial.history["val_loss"], label="validación")
ax.set_title("Error de reconstrucción durante el entrenamiento"); ax.set_xlabel("Época"); ax.set_ylabel("Error cuadrático medio"); ax.legend()
plt.show()
```

**Tiene que salir:**

```text
Error final de entrenamiento: 0.0076 | validación: 0.0095
```

Y además dibuja un gráfico.

### A8 · EJERCICIO 3 de 5 — Error de reconstrucción y umbral

> Completa `error_recons(modelo, X)`: devuelve un array con el error cuadrático medio de cada fila de `X`
> (media de `(X - modelo.predict(X))**2` por filas). Calcula `umbral` (percentil 95 de los errores de `sem_ent`, `np.percentile`).

```python
def error_recons(modelo, X):
    pred = modelo.predict(X, verbose=0)
    return np.mean((X - pred) ** 2, axis=1)

err_ent, err_test = error_recons(ae, sem_ent), error_recons(ae, sem_test)
umbral = float(np.percentile(err_ent, 95))
print(f"Umbral (percentil 95 en entrenamiento): {umbral:.4f}")
```

**Tiene que salir:**

```text
Umbral (percentil 95 en entrenamiento): 0.0154
```

### A10 · EJERCICIO 4 de 5 — Anomalías detectadas y semanas reales marcadas

> Calcula `n_detectadas` (cuántas de las 3 anomalías inyectadas superan el umbral) y `falsos_positivos`
> (cuántas semanas **reales de prueba**, `err_test`, superan el umbral).

```python
n_detectadas = int(np.sum(err_raras > umbral))
falsos_positivos = int(np.sum(err_test > umbral))
print(f"Anomalías detectadas: {n_detectadas}/3 | semanas reales marcadas: {falsos_positivos}/{len(err_test)}")

fig, ax = plt.subplots()
ax.plot(fechas_semana[corte:], err_test, "o-", ms=3, label="Semanas reales (prueba)")
ax.axhline(umbral, color="red", ls="--", label="Umbral (p95 entrenamiento)")
ax.set_title("Error de reconstrucción por semana (prueba)"); ax.set_ylabel("Error"); ax.set_xlabel("Fecha"); ax.legend()
plt.show()
```

**Tiene que salir:**

```text
Anomalías detectadas: 3/3 | semanas reales marcadas: 3/32
```

Y además dibuja un gráfico.

### A12 · MINI-RETO — ¿Qué semanas reales revisar?

> Construye `revisar`: un DataFrame con las semanas de **prueba** cuyo error supera el umbral, con columnas `inicio_semana` (fecha) y `error`,
> ordenado de mayor a menor error. Si no hay ninguna, queda vacío (es una buena noticia). Escribe en `interpretacion` (texto)
> una frase para el cliente: qué significa que una semana aparezca ahí y qué **no** significa (no es prueba de fallo, solo "merece mirarse").

```python
revisar = pd.DataFrame({"inicio_semana": fechas_semana[corte:], "error": err_test})
revisar = revisar[revisar["error"] > umbral].sort_values("error", ascending=False).reset_index(drop=True)
interpretacion = ("Estas semanas tienen un patrón de ocupación distinto al habitual; conviene revisar si hubo un evento, una promoción "
                  "o un fallo de datos, pero no prueba por sí sola que algo haya ido mal.")
print(revisar.head())
```

**Tiene que salir:**

```text
  inicio_semana     error
0    2025-07-13  0.028356
1    2025-10-19  0.016830
2    2025-08-31  0.015676
```

### A13 · EJERCICIO 5 de 5 — Emparejar situaciones con la técnica adecuada

> Asigna a `parejas` un diccionario que empareje cada situación con la técnica **más adecuada**
> (`"autoencoder"`, `"gan"` o `"difusion"`):
> - `"detectar semanas raras de ocupación"`
> - `"generar la foto de una terraza a partir de un texto"`
> - `"aprender a engañar a un discriminador con imágenes falsas"`

```python
parejas = {"detectar semanas raras de ocupación": "autoencoder",
           "generar la foto de una terraza a partir de un texto": "difusion",
           "aprender a engañar a un discriminador con imágenes falsas": "gan"}
```

