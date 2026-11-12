# 🚑 Miniapp 3 · ¿Gana la red neuronal al bosque?

⭐⭐ · 55 min · **red densa para datos de tabla** · practica S10 (red en Keras, curvas de aprendizaje, dropout, parada temprana) y S08 (bosque)

## Qué construyes
- Una **red neuronal** que decide si un paciente es urgente, y la enfrentas al **bosque** y a la **regresión logística**, con una pregunta honesta: **¿merece la pena la red?**
- Aprendes a leer **curvas de aprendizaje** y a ver que una red **no da siempre el mismo resultado**.

## Datos
- `triaje_urgencias.csv`: 4 000 pacientes **inventados**, 13 % urgentes. Columnas: edad, frecuencia cardiaca, tensión, saturación de oxígeno, temperatura, dolor (0–10), dolor de pecho, dificultad para respirar y si llega en ambulancia.
- Objetivo: `urgente`. Es un ejercicio de aprendizaje: **nada de esto decide quién se atiende primero.**

## Paso a paso

1. **Carga y separa en tres partes:** entrenar, validar (para elegir) y examen (una sola vez).

```python
import warnings, os; warnings.filterwarnings("ignore"); os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, confusion_matrix, precision_recall_curve

URL = "https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/triaje_urgencias.csv"
df = pd.read_csv(URL)
y = df["urgente"]; X = df.drop(columns="urgente")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
Xa, Xv, ya, yv = train_test_split(X_tr, y_tr, test_size=0.2, random_state=42, stratify=y_tr)
esc = StandardScaler().fit(Xa)                 # las redes necesitan los números escalados
Za, Zv, Zte = esc.transform(Xa), esc.transform(Xv), esc.transform(X_te)
print(len(ya), "para entrenar ·", len(yv), "para validar ·", len(y_te), "para el examen (NO mirar) · urgentes:", f"{y.mean():.1%}")
```

2. **Los modelos de referencia (S07 y S08).** El tonto, la logística y el bosque.

```python
def notas(proba):
    return {"AUC": roc_auc_score(yv, proba), "AP": average_precision_score(yv, proba)}

tabla = {}
tabla["Nadie es urgente (tonto)"] = notas(DummyClassifier(strategy="prior").fit(Za, ya).predict_proba(Zv)[:, 1])
tabla["Logística"] = notas(LogisticRegression(max_iter=1000).fit(Za, ya).predict_proba(Zv)[:, 1])
bosque = RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=42, n_jobs=2).fit(Xa, ya)
tabla["Bosque"] = notas(bosque.predict_proba(Xv)[:, 1])
pd.DataFrame(tabla).T.round(3)
```

3. **La red.** Dos capas ocultas, parada temprana y **3 semillas**. Se repite **con y sin dropout** y se dibujan las curvas de aprendizaje.

```python
def red(dropout, semilla):
    keras.utils.set_random_seed(semilla)
    m = keras.Sequential([keras.layers.Input((Xa.shape[1],)),
                          keras.layers.Dense(32, activation="relu"), keras.layers.Dropout(dropout),
                          keras.layers.Dense(16, activation="relu"), keras.layers.Dropout(dropout),
                          keras.layers.Dense(1, activation="sigmoid")])
    m.compile("adam", "binary_crossentropy")
    h = m.fit(Za, ya, validation_data=(Zv, yv), epochs=200, batch_size=64, verbose=0,
              callbacks=[keras.callbacks.EarlyStopping(patience=15, restore_best_weights=True)])
    return m, h

redes, ultimas = {}, {}
for dropout in (0.0, 0.3):
    auc, ap = [], []
    for semilla in range(3):
        m, h = red(dropout, semilla)
        p = m.predict(Zv, verbose=0).ravel()
        auc.append(roc_auc_score(yv, p)); ap.append(average_precision_score(yv, p))
        redes[(dropout, semilla)] = m
        ultimas[dropout] = h
    print(f"Red con dropout {dropout}: AUC {np.mean(auc):.3f} ± {np.std(auc):.3f} · AP {np.mean(ap):.3f} ± {np.std(ap):.3f} (3 semillas)")
    tabla[f"Red (dropout {dropout})"] = {"AUC": float(np.mean(auc)), "AP": float(np.mean(ap))}
for dropout, h in ultimas.items():
    plt.plot(h.history["loss"], label=f"entrenamiento · dropout {dropout}"); plt.plot(h.history["val_loss"], "--", label=f"validación · dropout {dropout}")
plt.xlabel("época"); plt.ylabel("error"); plt.legend(); plt.title("Curvas de aprendizaje de la red"); plt.show()
```

4. **La tabla y el campeón.**

```python
resumen = pd.DataFrame(tabla).T.sort_values("AP", ascending=False).round(3)
print(resumen)
print("Campeón por AP:", resumen.index[0])
```

5. **El examen, una vez, con el umbral de seguridad.** Pedimos detectar al **90 %** de los urgentes y miramos cuántas falsas alarmas cuesta. El umbral se busca con la validación, no con el examen.

```python
campeon = bosque if resumen.index[0] == "Bosque" else None
if campeon is not None:
    proba_v, proba_te = campeon.predict_proba(Xv)[:, 1], campeon.predict_proba(X_te)[:, 1]
else:
    m = redes[(0.3, 0)] if "0.3" in resumen.index[0] else redes[(0.0, 0)]
    proba_v, proba_te = m.predict(Zv, verbose=0).ravel(), m.predict(Zte, verbose=0).ravel()
precision, recall, umbrales = precision_recall_curve(yv, proba_v)
umbral = float(umbrales[np.where(recall[:-1] >= 0.90)[0][-1]])
aviso = proba_te >= umbral
vn, fp, fn, vp = confusion_matrix(y_te, aviso).ravel()
print(f"Umbral {umbral:.2f} · urgentes detectados {vp} de {vp + fn} · falsas alarmas {fp} de {vn + fp} no urgentes · AUC {roc_auc_score(y_te, proba_te):.3f}")
```

## Tu app
- Una función que valora **un paciente** con el campeón y dice si hay que dar prioridad.

```python
def paciente(edad, frecuencia_cardiaca, tension_sistolica, saturacion_o2, temperatura_c, dolor_0_10, dolor_pecho, dificultad_respirar, llega_en_ambulancia):
    fila = pd.DataFrame([dict(edad=edad, frecuencia_cardiaca=frecuencia_cardiaca, tension_sistolica=tension_sistolica, saturacion_o2=saturacion_o2,
                              temperatura_c=temperatura_c, dolor_0_10=dolor_0_10, dolor_pecho=dolor_pecho,
                              dificultad_respirar=dificultad_respirar, llega_en_ambulancia=llega_en_ambulancia)])[X.columns]
    if campeon is not None:
        p = campeon.predict_proba(fila)[0, 1]
    else:
        p = float(m.predict(esc.transform(fila), verbose=0)[0, 0])
    return f"probabilidad de urgencia {p:.0%} → {'🚨 prioridad' if p >= umbral else 'en cola'}"

print(paciente(70, 118, 95, 89, 38.5, 6, 1, 1, 1))
print(paciente(25, 78, 118, 99, 36.6, 2, 0, 0, 0))
print(paciente(52, 95, 130, 95, 37.0, 5, 0, 0, 0))
```

## Qué deberías ver
- Reparto: 2 400 para entrenar, 600 para validar y 1 000 para el examen; 13 % de urgentes (el tonto «nadie es urgente» acierta el 87 % y no sirve de nada: **AUC 0,50**).
- Validación (AUC / AP): **bosque 0,87 / 0,62**, red ≈ **0,82–0,83 / 0,56**, logística 0,81 / 0,47. **La red supera a la logística, pero no al bosque.** Es el resultado habitual en datos de tabla pequeños.
- Entre semillas la red varía poco (± 0,01), pero **no da dos veces el mismo número**. El dropout casi no cambia nada: con pocos datos y una red pequeña no hay mucho sobreajuste que frenar.
- Curvas: la de validación deja de mejorar pronto (unas pocas decenas de épocas) y la parada temprana corta ahí.
- Examen: con umbral ≈ 0,06 detectas **119 de 132 urgentes (90 %)** a cambio de ≈ 320 falsas alarmas de 868 no urgentes.
- App: el paciente de 70 años con saturación 89 sale **≈ 78 % → prioridad**; los otros dos, ≈ 1–2 % → en cola.
- Lección: **una red no siempre gana**; ahora sabes comprobarlo en lugar de suponerlo.

## Extra 🔴
- Cambia la red a **una sola capa de 8 neuronas** o a **tres capas**: ¿cambia algo?, ¿cuántos pesos tiene cada una?
- Pasa el **bosque** por las 3 semillas (`random_state`): ¿varía tanto como la red?
- Escribe en 3 líneas **cuándo usarías la red** en un problema de tabla y cuándo no.

## Cuidado
- Esto **no es una herramienta médica**: en urgencias, una persona decide siempre.
- La red **cambia un poco cada vez** que se entrena: da siempre la media de varias semillas, no un único número.
