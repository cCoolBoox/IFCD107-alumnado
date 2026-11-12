# 📧 Miniapp 2 · ¿Spam o correo de verdad?

⭐⭐ · 50 min · **clasificación** · practica S07 (logística, Naive Bayes) y S08 (árbol y bosque)

## Qué construyes
- Un **filtro de spam**: le pasas un correo y te dice «spam» o «correo normal», con su probabilidad.
- Lo haces de **dos formas** y las comparas: con pistas que calculáis vosotros (exclamaciones, enlaces…) y con las **palabras** del correo.

## Datos
- `correos.csv`: 1 500 correos en español **inventados** (asunto, texto y `es_spam`: 1 = spam, 0 = normal).
- Hay correos normales con «URGENTE» o «gratis» y spam muy educado: no es tan fácil como parece.

## Paso a paso

1. **Carga y lee unos cuantos.** ¿Qué os delata un spam?

```python
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/correos.csv"
df = pd.read_csv(URL)
df["completo"] = df["asunto"] + " " + df["texto"]
print("Spam:", round(df["es_spam"].mean(), 2), "· correos:", len(df))
df.sample(6, random_state=1)[["asunto", "es_spam"]]
```

2. **Inventa pistas (variables).** Cada columna nueva es una pregunta sobre el correo.

```python
t = df["completo"]
pistas = pd.DataFrame({
    "exclamaciones": t.str.count("!"),
    "pct_mayusculas": t.apply(lambda s: sum(c.isupper() for c in s) / len(s)),
    "enlaces": t.str.count("http"),
    "digitos": t.str.count(r"\d"),
    "palabras_gancho": t.str.lower().str.count("gratis|urgente|oferta|gana|premio|descuento"),
})
y = df["es_spam"]
print(pistas.groupby(y).mean().round(2))     # media de cada pista en normales (0) y spam (1)
```

3. **Separa.** El examen (`test`) no se mira hasta el final.

```python
P_train, P_test, T_train, T_test, y_train, y_test = train_test_split(
    pistas, t, y, test_size=0.2, random_state=42, stratify=y)
print(len(y_train), "para entrenar ·", len(y_test), "para el examen (NO mirar)")
```

4. **Duelo A: con vuestras pistas.** Acierto con validación cruzada (solo `train`).

```python
con_pistas = {
    "Nunca spam (tonto)": DummyClassifier(strategy="prior"),
    "Logística": make_pipeline(StandardScaler(), LogisticRegression()),
    "Árbol (profundidad 3)": DecisionTreeClassifier(max_depth=3, random_state=42),
    "Bosque": RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=2),
}
for n, m in con_pistas.items():
    print(f"{n:24s} {cross_val_score(m, P_train, y_train, cv=5).mean():.3f}")

arbol = con_pistas["Árbol (profundidad 3)"].fit(P_train, y_train)
print(export_text(arbol, feature_names=list(pistas.columns)))       # las reglas que ha aprendido
```

5. **Duelo B: con las palabras.** `CountVectorizer` cuenta cuántas veces sale cada palabra; con eso, Naive Bayes y la logística.

```python
con_palabras = {
    "Palabras + Naive Bayes": make_pipeline(CountVectorizer(), MultinomialNB()),
    "Palabras + Logística": make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000)),
}
for n, m in con_palabras.items():
    print(f"{n:24s} {cross_val_score(m, T_train, y_train, cv=5).mean():.3f}")

voc = con_palabras["Palabras + Logística"].fit(T_train, y_train)
palabras = np.array(voc[0].get_feature_names_out())
peso = voc[1].coef_[0]
orden = peso.argsort()
print("Delatan SPAM:", list(palabras[orden[-8:]][::-1]))
print("Delatan NORMAL:", list(palabras[orden[:8]]))
```

6. **El examen: UNA vez, con el campeón** (cambia `campeon` por el tuyo). Aquí un error no vale igual: un correo bueno en la carpeta de spam es peor que un spam que se cuela.

```python
campeon = voc                      # o con_pistas["Bosque"].fit(P_train, y_train), etc.
entrada = T_test                   # con el bosque o el árbol: P_test
pred = campeon.predict(entrada)
vn, fp, fn, vp = confusion_matrix(y_test, pred).ravel()
print(f"Acierta {(vn + vp) / len(y_test):.3f} · spam que se cuela (FN): {fn} · correos buenos a la basura (FP): {fp}")
ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=["normal", "spam"], cmap="Blues", colorbar=False)
plt.show()
```

## Tu app
- Una función que lee un correo y dice si es spam. Prueba **tus propios correos**: uno normal, uno de spam y uno «difícil» (un correo normal con «gratis» o «urgente»).

```python
def es_spam(texto, umbral=0.5):
    p = campeon.predict_proba([texto])[0, 1]        # solo con el modelo de palabras
    return f"{'SPAM' if p >= umbral else 'normal'} (probabilidad de spam: {p:.2f})"

print(es_spam("Hola Marta, mañana a las 10 reunión de equipo. Trae el informe."))
print(es_spam("¡¡GANA 5000 EUROS GRATIS!! Pulsa aquí YA http://premio.xyz"))
print(es_spam("URGENTE: hay un taller gratis para familias el jueves"))
```

## Qué deberías ver
- **42 % de spam** (0,42) y, en las pistas, el spam tiene más exclamaciones, enlaces y palabras gancho.
- Duelo A (acierto): tonto **0,58** · logística ≈ 0,85 · árbol ≈ 0,92 · bosque ≈ **0,99**.
- El árbol pregunta primero por los **enlaces**, luego por las **exclamaciones** y las **palabras gancho**.
- Duelo B (palabras): Naive Bayes ≈ **0,99** · logística ≈ **0,99**. Delatan spam `http`, `xyz`, `pastillas`, `euros`…; delatan normal `gracias`, `pedido`, `puedes`…
- Examen con la logística de palabras: acierta ≈ **0,98**; **4 spam se cuelan** y **1 correo bueno** va a la basura.
- La app: ≈ 0,10 (normal) · ≈ 0,93 (spam) · ≈ 0,18 (el «difícil» con «gratis»: lo deja pasar).
- Tus cifras pueden diferir en el último decimal.

## Extra 🔴
- Sube el `umbral` a 0,8: ¿cuántos correos buenos dejas de perder y cuántos spam se cuelan?
- Escribe **3 pistas nuevas** (por ejemplo, si el asunto lleva «¡¡» o si hay la palabra «euros») y mira si el árbol las usa.
- Mira los **errores del examen**: ¿qué tienen en común?

## Cuidado
- **No borrar correos solo por lo que diga el modelo**: mejor mandarlos a una carpeta de spam que se pueda revisar.
- Un modelo entrenado con estos correos no sabe nada de estafas nuevas: hay que **reentrenarlo** cuando cambian.
