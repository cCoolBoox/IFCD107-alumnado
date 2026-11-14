# 📚 Miniapp 5 · Un asistente que consulta el reglamento (y sabe decir «no sé»)

⭐⭐⭐ · 55 min · **buscar en documentos (mini-RAG)** · practica S12 (TF-IDF, similitud del coseno, LSA, recuperar antes de responder)

## Qué construyes
- Un asistente que, ante una pregunta, **busca en el reglamento** de una biblioteca el fragmento que mejor la contesta y **te lo enseña con su apartado**.
- No es una IA que genera texto: **solo recupera** frases que ya existen. Por eso **no se inventa nada**, y por eso puede decir «no lo sé».
- Mides lo bien que busca con **preguntas de examen** y eliges un umbral de «no sé».

## Datos
- `normas_biblioteca.md`: reglamento **ficticio** de una biblioteca municipal (12 apartados).
- `preguntas_biblioteca.csv`: 28 preguntas con la respuesta esperada. **20 sí están en el reglamento y 8 no** (aparcamiento, piscina, la capital de Francia…). Columnas: `pregunta`, `respuesta_esperada`, `en_el_reglamento`.

## Paso a paso

1. **Carga el reglamento y trocéalo.** Cada línea es un fragmento; guardamos el apartado al que pertenece.

```python
import warnings, re, unicodedata; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from urllib.request import urlopen
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

BASE = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/"
texto = urlopen(BASE + "normas_biblioteca.md").read().decode("utf-8") if BASE.startswith("http") else open(BASE + "normas_biblioteca.md", encoding="utf-8").read()
preguntas = pd.read_csv(BASE + "preguntas_biblioteca.csv")

def trocear(texto):
    trozos, apartado = [], ""
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea.startswith("## "): apartado = linea[3:]
        elif linea and not linea.startswith("#"): trozos.append((apartado, linea))
    return pd.DataFrame(trozos, columns=["apartado", "fragmento"])

trozos = trocear(texto)
print(len(trozos), "fragmentos en", trozos["apartado"].nunique(), "apartados")
print(trozos.head(3).to_string())
```

2. **Cuatro buscadores.** Cada uno convierte fragmentos y preguntas en números y busca **el más parecido** (coseno). Los dos últimos **quitan las palabras vacías** («cómo», «cuánto», «hay»…), que no dicen nada del tema.

```python
VACIAS = set("a al algo ante aqui como con cual cuales cuando cuanto cuantos cuanta cuantas cuesta de del desde donde el ella en es esta estan hay la las le lo los me mi mis no o para pero por que se si sin sobre son su sus te tiene tienen un una uno unos y yo puedo puede pueden hacer quien dan hasta ser".split())

def limpia(t):
    t = unicodedata.normalize("NFD", t.lower())
    return re.sub(r"[^a-z0-9 ]", " ", "".join(c for c in t if unicodedata.category(c) != "Mn"))

def raiz(t):                                   # recorte tosco: 5 primeras letras de cada palabra
    return " ".join(w[:5] for w in limpia(t).split())

def raiz_sin_vacias(t):
    return " ".join(w[:5] for w in limpia(t).split() if w not in VACIAS)

class Buscador:
    def __init__(self, prepara, temas=None):
        self.tfidf = TfidfVectorizer(preprocessor=prepara, sublinear_tf=True)
        M = self.tfidf.fit_transform(trozos["fragmento"])
        self.svd = TruncatedSVD(temas, random_state=0).fit(M) if temas else None
        self.M = self.svd.transform(M) if temas else M
    def puntuar(self, pregunta):
        q = self.tfidf.transform([pregunta])
        q = self.svd.transform(q) if self.svd else q
        return cosine_similarity(q, self.M)[0]

buscadores = {"Palabras exactas": Buscador(limpia),
              "Raíces": Buscador(raiz),
              "Raíces sin palabras vacías": Buscador(raiz_sin_vacias),
              "LSA (30 temas) sin vacías": Buscador(raiz_sin_vacias, temas=30)}
```

3. **Mide cada buscador con las preguntas que sí están en el reglamento.** Acierto = el fragmento devuelto **contiene la respuesta esperada**. `@1` mira el primero; `@3`, los tres primeros. Además medimos si **distingue** las preguntas que sí están de las que no (`separa`: 1 = perfecto, 0,5 = al azar), mirando la mejor similitud de cada pregunta.

```python
from sklearn.metrics import roc_auc_score
dentro = preguntas[preguntas["en_el_reglamento"] == "si"]

def contiene(fragmento, esperada): return limpia(esperada) in limpia(fragmento)

def acierto(buscador, k):
    n = 0
    for pregunta, esperada in zip(dentro["pregunta"], dentro["respuesta_esperada"]):
        top = np.argsort(buscador.puntuar(pregunta))[::-1][:k]
        n += any(contiene(trozos["fragmento"][i], esperada) for i in top)
    return n / len(dentro)

def separa(buscador):
    mejor_parecido = [buscador.puntuar(q).max() for q in preguntas["pregunta"]]
    return roc_auc_score(preguntas["en_el_reglamento"] == "si", mejor_parecido)

tabla = pd.DataFrame({nombre: {"acierto@1": acierto(b, 1), "acierto@3": acierto(b, 3), "separa": separa(b)}
                      for nombre, b in buscadores.items()}).T.round(2)
print(tabla)
campeon_nombre = tabla.sort_values(["acierto@1", "separa"], ascending=False).index[0]
print("Campeón:", campeon_nombre)
```

4. **Aprende a decir «no sé».** Si la mejor similitud es baja, el asistente no responde. El umbral se elige **con la mitad de las preguntas (desarrollo)** y se evalúa **con la otra mitad (examen)**, mezclando preguntas que sí y que no están.

```python
b = buscadores[campeon_nombre]
dev, test = train_test_split(preguntas, test_size=0.5, random_state=0, stratify=preguntas["en_el_reglamento"])

def resultado(fila, umbral):
    p = b.puntuar(fila["pregunta"]); mejor = int(np.argmax(p))
    if p[mejor] < umbral:
        return "no sé", fila["en_el_reglamento"] == "no"            # callar es correcto si no estaba
    if fila["en_el_reglamento"] == "no":
        return "respondió", False                                  # inventó una respuesta
    return "respondió", contiene(trozos["fragmento"][mejor], fila["respuesta_esperada"])

def puntuacion(datos, umbral):
    return np.mean([resultado(f, umbral)[1] for _, f in datos.iterrows()])

umbrales = np.round(np.arange(0.0, 0.8, 0.05), 2)
curva = pd.Series({u: puntuacion(dev, u) for u in umbrales})
mejor_umbral = float(np.median(curva[curva == curva.max()].index))   # el centro de la zona buena
print(curva.round(2).to_string())
print("Umbral elegido con el desarrollo:", mejor_umbral)
print(f"Examen (otra mitad): {puntuacion(test, mejor_umbral):.2f} · si siempre respondiera: {puntuacion(test, 0.0):.2f}")
```

## Tu app
- El asistente: pregunta → fragmento + apartado, o «no lo sé».

```python
def pregunta_al_reglamento(pregunta):
    p = b.puntuar(pregunta); mejor = int(np.argmax(p))
    if p[mejor] < mejor_umbral:
        return f"🤷 No lo sé: no encuentro nada parecido en el reglamento. (parecido {p[mejor]:.2f})"
    t = trozos.iloc[mejor]
    return f"📖 {t['fragmento']}\n   — Apartado: {t['apartado']} (parecido {p[mejor]:.2f})"

for q in ["¿Cuántos libros puedo sacar?", "¿Puedo entrar con mi perro?", "¿Cuándo cierra en agosto?",
          "¿Tienen impresora en color?", "¿Cuánto cuesta el parking?", "¿Qué tiempo hará mañana?"]:
    print(q, "\n  ", pregunta_al_reglamento(q), "\n")
```

## Qué deberías ver
- 33 fragmentos en 12 apartados.
- Tabla de buscadores: **palabras exactas** acierta el primero en el 70 % (`@1`), **raíces** en el 80 %; con tres intentos (`@3`) llega al 95–100 %. Lo que más cambia es `separa`: **sin palabras vacías sube de ≈ 0,78 a ≈ 0,98**, es decir, distingue mucho mejor «esto está en el reglamento» de «esto no».
- Campeón: **LSA (30 temas) sin vacías** (acierto@1 ≈ 0,80, separa ≈ 0,99). Quitar las palabras vacías ayuda más que usar LSA.
- «No sé»: sin umbral el asistente acierta ≈ **0,64** del examen (responde siempre, también lo que no sabe); con el umbral (≈ 0,4) sube a ≈ **0,86**. Ojo: con solo 14 preguntas de desarrollo la curva es **una meseta**, no un pico claro.
- App: perro → *mascotas* (0,99) ✅; agosto → *horario de julio y agosto* ✅; impresora en color → *0,30 euros* ✅; parking → «no lo sé» ✅.
- **Dónde falla (y está bien verlo):** «¿Cuántos libros puedo sacar?» devuelve la norma de los **retrasos** («sin poder *sacar* nada»), y «¿Qué tiempo hará mañana?» devuelve las **donaciones** porque ambas dicen *mañana* (`por la mañana`), con un parecido de 0,94. **Buscar palabras parecidas no es entender.**

## Extra 🔴
- Cambia el troceado: en vez de líneas, **frases** o **apartados enteros**. ¿Qué pasa con el acierto@1?
- Añade a `normas_biblioteca.md` una norma nueva (por ejemplo, «préstamo de juegos de mesa») y comprueba que el asistente **la encuentra sin reentrenar nada**.
- Pregunta con sinónimos («¿puedo sacar cine?»): ¿qué buscador aguanta mejor?

## Cuidado
- Este asistente **no entiende** el reglamento: busca palabras parecidas. Puede devolver un fragmento que **suena igual pero contesta otra cosa**.
- Un asistente que **siempre responde** es peor que uno que a veces calla. En un reglamento, una respuesta inventada puede causar un problema real.
- Con 28 preguntas el resultado es **orientativo**: añade más preguntas antes de fiarte de un número.

## 🔑 Solucionario (Extra)
> Míralo **después** de intentarlo. Las cifras salen de ejecutar la ficha tal cual y pueden variar un poco (librerías, semilla): lo que cuenta es la **conclusión**.

- **Extra 1 · Cambiar el troceado (acierto@1, buscador campeón):**
  - **Líneas** (la ficha, 33 fragmentos): **0,80**.
  - **Frases** (33, ya coincide casi con las líneas): **0,80** (@3: 0,90).
  - **Apartados enteros** (12): **0,85** (@3: 1,00).
  - Parece que «mejora» con trozos grandes, pero es **trampa de medida**: el trozo grande **contiene** la respuesta más fácil (la métrica comprueba que la respuesta esté dentro), pero devuelve un **párrafo largo** donde hay que buscar. **El acierto sube y la utilidad baja.**
- **Extra 2 · Añadir una norma nueva:** añadiendo «Préstamo de juegos de mesa… 3 días…» a `normas_biblioteca.md`, la pregunta «¿Cuántos días puedo llevarme un juego de mesa?» **la encuentra a la primera** (parecido **0,53**), **sin reentrenar nada**. Es la gran ventaja de buscar en un texto en vez de **hacer entrenar** un modelo: **actualizas el documento y ya**.
- **Extra 3 · Sinónimos:**
  - «¿Puedo sacar **cine**?» → **falla en los cuatro buscadores** (el reglamento dice «películas», no «cine»). Peor: el LSA da **0,73 de parecido** pero a la norma de **los retrasos** (por «sacar»): se equivoca con seguridad.
  - «¿Puedo llevarme una **película** a casa?» → palabras exactas **falla** (el texto tiene «películas»); **raíces, raíces sin vacías y LSA aciertan** (0,48 · 0,62 · 0,96).
  - «¿Puedo coger una película prestada?» → raíces **0,28**, sin vacías **0,38**, LSA **0,64** pero a «Estos préstamos no se renuevan» (equivocado).
  - Conclusión: **ningún buscador entiende sinónimos de verdad**; las raíces y el LSA **ayudan con variantes de la misma palabra**, no con palabras distintas.
- **Para comentar:** «**Buscar palabras parecidas no es entender**» (el ejemplo de «sacar» y «mañana»). Y un asistente que **siempre responde** es peor que uno que a veces calla: sin umbral 0,64; con umbral ≈ 0,4, **0,86**.
- **Tarjeta de ejemplo:**
  - Mi IA decide **qué norma contesta a la pregunta** (o «no lo sé») a partir de **el parecido de palabras con 33 fragmentos**.
  - Se equivoca **en el 14 % de las preguntas del examen** (acierta 0,86 con umbral), frente al **36 %** si siempre respondiera (acierta 0,64).
  - Falla cuando **la pregunta usa un sinónimo o una palabra que sale en otra norma** («sacar», «mañana»).
  - No debe usarse para **dar respuestas oficiales sin citar el apartado**.
