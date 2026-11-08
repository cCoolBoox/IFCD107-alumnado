# Solucionario · cuadernos «en clase» del Sprint 12

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S12_01`, `S12_02`, `S12_03`, `S12_05`, `S12_06`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S12_01 · Series temporales: baseline, descomposición y ARIMA/SARIMAX

### A4 · EJERCICIO 1 de 3 — Día de más ocupación y mes de menos

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

### A7 · EJERCICIO 2 de 3 — Baseline: media de las últimas 4 semanas

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

### A11 · EJERCICIO 3 de 3 — SARIMAX sin exógenas

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

---

## S12_03 · NLP clásico: sentimiento y temas en las reseñas de TurisData

### A4 · EJERCICIO 1 de 4 — Limpiar un texto

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

### A6 · EJERCICIO 2 de 4 — Las 5 palabras más frecuentes

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

### A9 · EJERCICIO 3 de 4 — Regresión logística frente a Naive Bayes

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

### A13 · EJERCICIO 4 de 4 — ¿Falla con las negaciones?

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

---

## S12_05 · Transformers y LLM: tokenización y atención paso a paso

### A6 · EJERCICIO 1 de 3 — Escribir softmax por filas

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

### A8 · EJERCICIO 2 de 3 — La función de atención completa

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

### A10 · EJERCICIO 3 de 3 — Atención con máscara causal

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

---

## S12_06 · Mini RAG: un asistente que responde con la política del alojamiento

### A3 · EJERCICIO 1 de 3 — Trocear la política en frases

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

### A5 · EJERCICIO 2 de 3 — Recuperar los fragmentos más parecidos

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

### A11 · EJERCICIO 3 de 3 — El asistente completo con umbral

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

