# 💬 Miniapp 4 · ¿De qué trata este mensaje?

⭐⭐ · 55 min · **clasificar texto** · practica S12 (texto → números con TF-IDF, Naive Bayes, logística, n-gramas, LSA)

## Qué construyes
- Un clasificador que lee un mensaje de un cliente y lo manda a su **departamento**: factura, avería, contratar o baja.
- Comparas **bolsa de palabras**, **pares de palabras** y **LSA** (S12), y miras **qué palabras pesan** en cada decisión.

## Datos
- `mensajes_soporte.csv`: 2 600 mensajes **inventados** de clientes de una compañía ficticia, con faltas, mensajes mezclados (dos temas a la vez) y algo de ruido a propósito. Columnas: `texto`, `categoria`.
- Es difícil de forma honesta: **no esperes 100 %**.

## Paso a paso

1. **Carga y separa.** Entrenar, validar y examen (una vez).

```python
import warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/mensajes_soporte.csv"
df = pd.read_csv(URL)
print(df["categoria"].value_counts().to_string())
X_tr, X_te, y_tr, y_te = train_test_split(df["texto"], df["categoria"], test_size=0.2, random_state=42, stratify=df["categoria"])
Xa, Xv, ya, yv = train_test_split(X_tr, y_tr, test_size=0.25, random_state=42, stratify=y_tr)
print(len(Xa), "para entrenar ·", len(Xv), "para validar ·", len(X_te), "para el examen (NO mirar)")
for t, c in df.sample(3, random_state=1).itertuples(index=False): print(f"[{c}] {t}")
```

2. **Compara varias formas de convertir texto en números** (el tonto, Naive Bayes, logística, con pares de palabras y con LSA).

```python
def tfidf(**kw): return TfidfVectorizer(lowercase=True, strip_accents="unicode", **kw)

modelos = {
    "Siempre la más común (tonto)": make_pipeline(tfidf(), DummyClassifier(strategy="most_frequent")),
    "Palabras + Naive Bayes": make_pipeline(tfidf(), MultinomialNB()),
    "Palabras + logística": make_pipeline(tfidf(), LogisticRegression(max_iter=1000)),
    "Palabras y pares + logística": make_pipeline(tfidf(ngram_range=(1, 2), min_df=2), LogisticRegression(max_iter=1000)),
    "LSA (50 temas) + logística": make_pipeline(tfidf(), TruncatedSVD(50, random_state=0), LogisticRegression(max_iter=1000)),
}
notas = {}
for nombre, m in modelos.items():
    m.fit(Xa, ya)
    notas[nombre] = accuracy_score(yv, m.predict(Xv))
tabla = pd.Series(notas).sort_values(ascending=False).round(3)
print(tabla.to_string())
campeon_nombre = tabla.index[0]
print("Campeón:", campeon_nombre)
```

3. **Qué palabras pesan** en cada departamento (con la logística de palabras): así sabes **por qué** decide lo que decide.

```python
m = modelos["Palabras + logística"]
palabras = np.array(m[0].get_feature_names_out())
for i, clase in enumerate(m[1].classes_):
    top = palabras[np.argsort(m[1].coef_[i])[-8:][::-1]]
    print(f"{clase:10s} → {', '.join(top)}")
```

4. **Dónde se confunde.** Matriz de confusión del campeón sobre la validación.

```python
campeon = modelos[campeon_nombre]
ConfusionMatrixDisplay.from_predictions(yv, campeon.predict(Xv), cmap="Blues", xticks_rotation=30)
plt.title("Validación: qué manda a dónde"); plt.show()
errores = pd.DataFrame({"texto": Xv.values, "real": yv.values, "predicho": campeon.predict(Xv)})
errores = errores[errores["real"] != errores["predicho"]]
print(len(errores), "errores de", len(yv))
for t, r, p in errores.head(4).itertuples(index=False): print(f"  real={r} · dijo={p} · {t}")
```

5. **Examen, una vez.**

```python
print(f"Acierto en el examen con '{campeon_nombre}': {accuracy_score(y_te, campeon.predict(X_te)):.3f}")
```

## Tu app
- Una función que recibe un mensaje y dice a qué departamento va y **con cuánta seguridad**. Si no está seguro, que lo diga.

```python
def clasifica(mensaje, minimo=0.5):
    p = campeon.predict_proba([mensaje])[0]
    orden = np.argsort(p)[::-1]
    mejor, segundo = campeon.classes_[orden[0]], campeon.classes_[orden[1]]
    if p[orden[0]] < minimo:
        return f"🤔 No lo tengo claro: ¿{mejor} ({p[orden[0]]:.0%}) o {segundo} ({p[orden[1]]:.0%})? Que lo mire una persona."
    return f"→ {mejor} ({p[orden[0]]:.0%})"

for frase in ["No me llega internet desde ayer y el router parpadea en rojo",
              "Quiero dar de baja la línea de mi madre",
              "Me habéis cobrado dos veces este mes",
              "Hola, ¿tenéis fibra en mi calle? Me gustaría contratarla",
              "Quiero darme de baja porque la factura es muy cara"]:
    print(frase, "\n   ", clasifica(frase))
```

## Qué deberías ver
- Cuatro departamentos casi repartidos a partes iguales (≈ 620–680 mensajes cada uno). El tonto acierta **26 %**.
- Validación: **palabras + pares + logística ≈ 0,86** (campeón), LSA ≈ 0,84, palabras + logística ≈ 0,84, Naive Bayes ≈ 0,84. **Las diferencias entre los cuatro son pequeñas**: no hace falta lo más sofisticado.
- Palabras que pesan: `baja` → *servicio, baja, cancelar, portabilidad*; `contratar` → *contratar, piso, nuevo, instalar*; `factura` → *factura, duplicado, recibo, cobrado*; `averia` → *internet, ayer, llevo, no*. Salen también palabras vacías (*se, no, en, un*): **buena pista para mejorar**.
- Errores (≈ 74 de 520): casi todos son **mensajes con dos temas mezclados** («quiero cancelar… y me cobrasteis de más»).
- Examen: **≈ 0,88**. No es 100 % y no debe serlo: el ruido está puesto a propósito.
- App: la avería sale `averia` (≈ 68 %), la baja de la línea de la madre `baja` (≈ 93 %), el doble cobro `factura` (≈ 82 %) y **«¿tenéis fibra? quiero contratarla» queda en duda** (≈ 45 % contratar) → «que lo mire una persona».

## Extra 🔴
- Prueba `ngram_range=(1, 3)` o `min_df=5`: ¿mejora o solo se complica?
- Cambia `minimo` en `clasifica` (0,4 / 0,6 / 0,8): ¿cuántos mensajes quedan para una persona? **Más seguridad = más trabajo humano.**
- Escribe 5 mensajes tuyos que **tú crees** que lo van a engañar. ¿Lo consigues?

## Cuidado
- Los mensajes son **inventados**: con mensajes reales habría que revisar privacidad y datos personales.
- Si un mensaje habla de dos cosas a la vez, **la red no es tonta, el problema es ambiguo**. Prueba la frase de «baja + factura»: elige una con un 72 %, pero **la otra mitad del mensaje también era cierta**.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

#### Extra 1 · `ngram_range=(1, 3)` o `min_df=5`
- **Qué hacer:**
  1. Cambia `ngram_range` y `min_df` en `tfidf(...)` y entrena otra logística.
  2. Mira el acierto **y el tamaño del vocabulario**: ¿compensa complicarlo?
```python
for nombre, kw in (("pares, min_df=2", dict(ngram_range=(1, 2), min_df=2)),
                     ("hasta tríos", dict(ngram_range=(1, 3), min_df=2)),
                     ("pares, min_df=5", dict(ngram_range=(1, 2), min_df=5))):
    m = make_pipeline(tfidf(**kw), LogisticRegression(max_iter=1000)).fit(Xa, ya)
    print(f"{nombre:18s} acierto {accuracy_score(yv, m.predict(Xv)):.3f} · vocabulario {len(m[0].vocabulary_)}")
```
- **Qué sale y por qué:**
  - Pares (campeón): **0,858** con vocabulario de 1 564.
  - Hasta **tríos**: **0,877** pero vocabulario de **3 685** (más del doble).
  - `min_df=5`: **0,854** y vocabulario de **971**.
  - Con 520 mensajes de validación, la diferencia entre 0,858 y 0,877 son **unos 10 mensajes**: no es suficiente para decir que mejora. **Se complica más de lo que gana.**

#### Extra 2 · `minimo` en `clasifica` (validación de 520 mensajes)
- **Qué hacer:**
  1. Calcula la seguridad de cada mensaje de validación (`predict_proba(...).max`).
  2. Para cada `minimo`, cuenta cuántos pasan a una persona y el acierto del resto.
```python
proba_v = campeon.predict_proba(Xv)
seguridad = proba_v.max(axis=1)
predicho = campeon.classes_[proba_v.argmax(axis=1)]
for minimo in (0.4, 0.6, 0.8):
    seguro = seguridad >= minimo
    print(f"minimo {minimo}: a una persona {int((~seguro).sum())} de {len(Xv)} · acierto del resto {accuracy_score(yv[seguro], predicho[seguro]):.3f}")
```
- **Qué sale y por qué:**
  - **0,4:** **0** mensajes para una persona; acierto del resto 0,858.
  - **0,6:** **117 (22 %)** a persona; acierto del resto **0,963**.
  - **0,8:** **245 (47 %)** a persona; acierto del resto **0,985**.
  - **Más seguridad = más trabajo humano.** Se decide el punto según **lo que cuesta una persona** frente a **lo que cuesta un error**.

#### Extra 3 · Frases que engañan (probadas)
- **Qué hacer:**
  1. Escribe 5 mensajes que creas que van a engañar (dos temas, palabras de otro tema, sin contenido) y pásalos por `clasifica`.
```python
for frase in ["Quiero cancelar la línea y además me habéis cobrado de más",
              "No tengo internet y quiero un duplicado de la factura",
              "Buenas tardes",
              "Mi vecino tiene fibra y yo no sé qué hacer"]:
    print(frase, "\n   ", clasifica(frase))
```
- **Qué sale y por qué:**
  - «Quiero cancelar la línea y además me habéis cobrado de más» → **baja 54 %** (la otra mitad también era cierta).
  - «Mi vecino tiene fibra y yo no sé qué hacer» → **avería 63 %** (no tiene nada de avería).
  - «Buenas tardes» → **duda** (avería 35 %, contratar 29 %): bien, avisa a una persona.
  - Lo que engaña: **mensajes con dos temas**, **palabras de otro tema** y **mensajes sin contenido**.

#### Para cerrar
- **Para comentar:** las diferencias entre los cuatro modelos son **pequeñas**: **no hace falta lo más sofisticado**. Los errores son **ambigüedad del problema**, no «torpeza».
- **Tarjeta de ejemplo:**
  - Mi IA decide **a qué departamento va un mensaje** a partir de **sus palabras y pares de palabras (TF-IDF)**.
  - Se equivoca **≈ 12 de cada 100 mensajes** (acierto 0,88), frente al **74 %** de error del modelo tonto (acierta 0,26).
  - Falla cuando **el mensaje mezcla dos temas** (baja + factura).
  - No debe usarse para **cerrar una consulta sin que lo mire una persona** cuando la seguridad es baja.
