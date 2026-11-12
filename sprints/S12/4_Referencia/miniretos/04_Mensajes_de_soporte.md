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
