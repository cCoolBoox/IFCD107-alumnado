# 🧩 Mini-reto · Tu IA de reglas contra el árbol

**Opcional · 40–45 min · en equipo (2–3 personas) · al cerrar S08 o para quien acabe antes.**

Creáis **una IA de verdad**, pero con reglas escritas por vosotros: decidís todo y lo entendéis todo. Después, la medís igual que se mide cualquier modelo y la enfrentáis al **árbol de decisión podado** del sprint.

> ¿Prefieres otros datos? Mira la [bolsa de miniretos](../../4_Referencia/miniretos/S08/README.md): spam, tumor, diabetes, precio de vivienda, números a mano y el zoo de fronteras.

## La pregunta del cliente
- **¿Cancelará esta reserva?** (sí o no), con los datos de `reservas_turisdata.csv` que ya conocéis.

## Reglas del juego
- **Máximo 3 reglas**, del tipo «si antelación > X y sin depósito → cancela».
- **Mirad solo el entrenamiento** (`train`) para decidir las reglas. Todas las veces que queráis.
- **El examen (`test`) se mira UNA sola vez, al final.** Si retocáis las reglas después de verlo, hacéis trampa (es la regla de oro del sprint).
- **Cada equipo usa al menos una variable distinta** de las del resto (`antelacion_dias`, `deposito`, `tarifa`, `canal`, `tipo_habitacion`, `noches`, `precio_noche`, `cliente_repetidor`…).

## Paso a paso

1. **Prepara los datos** (Colab, una celda):

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/reservas_turisdata.csv"
df = pd.read_csv(URL, parse_dates=["fecha_reserva", "fecha_llegada"])
df["temporada_alta"] = df["fecha_llegada"].dt.month.isin([1, 2, 3, 7, 8, 12]).astype(int)
train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df["cancelada"])
print(len(train), "reservas para mirar ·", len(test), "para el examen (NO mirar)")
```

2. **Explora el entrenamiento** (¿dónde se cancela más?):

```python
for col in ["deposito", "tarifa", "canal", "tipo_habitacion"]:
    print(train.groupby(col)["cancelada"].mean().round(2).to_dict())
print(train.groupby(pd.cut(train["antelacion_dias"], [0, 30, 60, 90, 120, 400]), observed=True)["cancelada"].mean().round(2))
```

3. **Escribe tu IA** (aquí solo hay una regla de ejemplo: cámbiala y añade las tuyas):

```python
def mi_ia(d):
    """Devuelve 1 (cancela) o 0 (se queda) para cada reserva de d."""
    regla1 = d["antelacion_dias"] > 100
    # regla2 = ...
    return regla1.astype(int)          # une las reglas con | (o) y & (y)
```

4. **Mídela con el entrenamiento** (repite hasta que os guste):

```python
def evaluar(d, nombre):
    y, p = d["cancelada"], mi_ia(d)
    vn, fp, fn, vp = confusion_matrix(y, p).ravel()
    print(f"{nombre}: acierta {(vn+vp)/len(d):.2f} · detecta {vp/(vp+fn):.2f} de las que cancelan · de sus avisos acierta {vp/(vp+fp):.2f}")
    print(f"   VN {vn} · FP {fp} · FN {fn} · VP {vp}")

evaluar(train, "entrenamiento")
```

5. **El examen: UNA vez.** Cuando el equipo esté de acuerdo, quitad el `#` y ejecutad:

```python
# evaluar(test, "EXAMEN")
```

6. **Dónde falla.** Con el examen ya hecho, mirad 3 reservas que vuestra IA no detectó (`FN`) o por las que avisó sin motivo (`FP`):

```python
p = mi_ia(test)
test[(p == 0) & (test["cancelada"] == 1)].head(3)      # cancelaciones que se escapan
```

## El duelo
Comparad vuestro examen con el del **árbol podado** (46 hojas, S08_01):

| | Acierta | Detecta (recall) | De sus avisos acierta (precisión) |
|---|---|---|---|
| **Árbol podado** | 0,65 | 0,60 | 0,63 |
| «Nunca avisar» (modelo tonto) | 0,54 | 0 | — |
| **Vuestra IA de reglas** | | | |

Premios (uno por categoría):
- 🎯 **Detecta más** cancelaciones (recall).
- ✅ **Acierta más** de sus avisos (precisión).
- ⚖️ **Mejor equilibrio** (la media de las dos).
- ✂️ **La más simple** que supere al modelo tonto.

## Tarjeta de cierre (3 líneas, en la hoja compartida)
- **Mi IA decide** si una reserva cancela a partir de ______ (variables).
- **Detecta** ___ de cada 10 cancelaciones y **de sus avisos acierta** ___ de cada 10.
- **Falla cuando** ______ y **no debe usarse para** ______.

## Para comentar al final
- ¿Vuestras reglas empatan con el árbol? ¿Cuál es la diferencia entre vuestras reglas y las del árbol? (**el árbol las aprende solo, pero son preguntas igual que las vuestras**).
- ¿Quién detecta más lo paga con más falsas alarmas? ¿Cuánto cuesta una llamada de más frente a una habitación vacía?
- ¿Qué haría falta para que una IA así se usara de verdad? (más datos, validar con otro año, vigilarla…).

*Ideas para vuestro proyecto final (S14–S17): apuntadlas en el muro de ideas de la clase, con una pregunta cerrada y los datos que tendríais.*
