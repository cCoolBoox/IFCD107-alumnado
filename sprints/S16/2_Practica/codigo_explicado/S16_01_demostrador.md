# Código explicado · S16.01 · Plantilla de demostrador

> **Para qué sirve.** Es el cuaderno **explicado por escrito**: qué hace cada celda, qué significa cada palabra de código y qué hace cada línea. En clase solo se hace un **recorrido de 10 minutos** con el docente; el resto lo leéis vosotros, con calma, **mientras o después de ejecutar** cada celda. No hace falta saber programar.
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S16/2_Practica/S16_01_demostrador.ipynb) · [descargar](../S16_01_demostrador.ipynb) · ⏱ en clase: 45 min · 🏫 5 celdas de código en clase · 🏠 5 en casa
>
> **Cómo usarlo:** 1) ejecutad la celda; 2) buscad aquí el mismo número de celda; 3) leed qué hace cada línea; 4) cambiad una cosa y comprobad si pasa lo que esperabais (es la mejor manera de entender código).

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora y es para las personas.

## 1. Recorrido de 10 minutos (con el docente)

El docente ejecuta **estas celdas con todo el grupo** y las comenta en voz alta. Lo demás se lee aquí.

| Celda | Sección | Qué miramos |
|---|---|---|
| 1 |  | Practica `seed`, `join`. |
| 2 | 1. Guardar el modelo y sus metadatos | Practica `read_csv`, `train_test_split`, `ColumnTransformer`, `fit` y más (sección «1. Gu… |
| 3 | 1. Guardar el modelo y sus metadatos | Practica `round`, `join`, `open`, `listdir` y más (sección «1. Guardar el modelo y sus me… |
| 4 | 2. La lógica, separada de la interfaz | Practica `insert`, `open`, `write`, `join` (sección «2. La lógica, separada de la interfa… |

## 2. Qué guarda cada variable

| Variable | Se crea así | Celda |
|---|---|---|
| `SEMILLA` | `42` | 1 |
| `CARPETA` | `"demostrador"` | 1 |
| `reservas` | `pd.read_csv(dato("reservas_turisdata.csv"))` | 2 |
| `NUMERICAS` | `["antelacion_dias", "noches", "adultos", "ninos", "precio…` | 2 |
| `CATEGORICAS` | `["tipo_habitacion", "canal", "tarifa", "deposito"]` | 2 |
| `prep` | `ColumnTransformer([("num", StandardScaler(), NUMERICAS),…` | 2 |
| `modelo` | `Pipeline([("prep", prep), ("m", LogisticRegression(max_it…` | 2 |
| `auc_test` | `roc_auc_score(y_test, modelo.predict_proba(X_test)[:, 1])` | 2 |
| `meta` | `{ "nombre": "Riesgo de cancelación de reservas · TurisDat…` | 3 |
| `LOGICA` | `r'''"""Lógica del demostrador: cargar el modelo, validar…` | 4 |
| `reserva_ejemplo` | `{"antelacion_dias": 120, "noches": 5, "adultos": 2, "nino…` | 4 |
| `APP` | `r'''"""Demostrador Streamlit · TurisData. Lanzar con: str…` | 9 |
| `API` | `r'''"""API local del modelo. Lanzar con: uvicorn api:app…` | 11 |
| `paquetes` | `["numpy", "pandas", "scikit-learn", "joblib", "streamlit"…` | 13 |
| `lineas` | `[]` | 13 |

## 3. Palabras de código de este cuaderno

**Definidas en este cuaderno** (las crea el propio cuaderno; `def` define una función):

| Palabra | Qué hace |
|---|---|
| `validar_coherencia` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `mensaje_errores` | Función definida en el cuaderno. *(La escribís vosotros en un ejercicio.)* |
| `test_reserva_valida_devuelve_probabilidad` | Función definida en el cuaderno. |
| `test_entrada_invalida_no_rompe` | Función definida en el cuaderno. |
| `test_falta_un_campo` | Función definida en el cuaderno. |
| `test_sentido_comun` | Función definida en el cuaderno. |
| `al_pulsar` | Función definida en el cuaderno. |
| `cargar_modelo` | Devuelve (modelo, metadatos). Lanza FileNotFoundError con un mensaje claro si faltan los archivos. |
| `predecir_reserva` | Valida y predice. Devuelve un diccionario; si hay errores, solo {'errores': [...]}. |
| `validar_reserva` | Devuelve una lista de errores en español (lista vacía = entrada válida). |

**De Python y sus librerías:**

| Palabra | Qué hace | Celdas |
|---|---|---|
| `any` | Dice si ALGUNA condición es verdadera. | 8 |
| `append` | Añade un elemento al final de una lista. | 13 |
| `Button` | *(sin explicar todavía)* | 10 |
| `capitalize` | *(sin explicar todavía)* | 3 |
| `clear_output` | *(sin explicar todavía)* | 10 |
| `ColumnTransformer` | Aplica un preprocesado distinto a cada grupo de columnas. | 2 |
| `compile` | Prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas). | 9, 11 |
| `dato` | Devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga). | 2 |
| `display` | Muestra un objeto con el formato bonito del cuaderno. | 10 |
| `Dropdown` | *(sin explicar todavía)* | 10 |
| `dump` | *(sin explicar todavía)* | 3 |
| `fit` | Entrena el modelo con los datos (aquí es donde «aprende»). | 2 |
| `float` | Convierte un valor en número decimal. | 3, 10 |
| `FloatText` | *(sin explicar todavía)* | 10 |
| `get` | Lee un valor de un diccionario; si no existe, devuelve el valor por defecto en vez de fallar. | 12 |
| `insert` | Inserta elementos en una posición. | 4 |
| `int` | Convierte un valor en número entero. | 3, 10 |
| `isinstance` | Comprueba si un valor es de un tipo concreto. | 10 |
| `items` | Devuelve las parejas (clave, valor) de un diccionario. | 8, 10 |
| `join` | Une una lista de textos en uno solo con un separador. | 1, 3, 4, 9, 11, 13 |
| `json` | *(sin explicar todavía)* | 12 |
| `len` | Cuenta cuántos elementos tiene una lista, texto o tabla. | 3 |
| `list` | Crea una lista (o convierte algo en lista). | 10 |
| `listdir` | Lista el contenido de una carpeta. | 3 |
| `LogisticRegression` | Modelo de clasificación que da una probabilidad (aunque se llame «regresión»). | 2 |
| `makedirs` | Crea una carpeta (y las que falten). | 1 |
| `max` | Devuelve el valor más grande. | 3 |
| `mean` | Calcula la media. | 3 |
| `min` | Devuelve el valor más pequeño. | 3 |
| `on_click` | *(sin explicar todavía)* | 10 |
| `OneHotEncoder` | Convierte categorías en columnas de 0/1. | 2 |
| `open` | Abre un fichero para leerlo o escribirlo. | 3, 4, 9, 11, 13 |
| `Output` | *(sin explicar todavía)* | 10 |
| `Pipeline` | Encadena pasos (preprocesado + modelo) en un solo objeto. | 2 |
| `post` | *(sin explicar todavía)* | 12 |
| `predict_proba` | Pide la probabilidad de cada clase (no solo la clase). | 2 |
| `print` | Muestra un valor por pantalla. | 2, 3, 4, 8, 9, 10… |
| `prueba` | *(sin explicar todavía)* | 8 |
| `read_csv` | Lee un fichero CSV y lo convierte en una tabla. | 2 |
| `reload` | *(sin explicar todavía)* | 4, 12 |
| `replace` | Sustituye un trozo de texto (o valores de una tabla) por otro. | 3 |
| `roc_auc_score` | Calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar). | 2 |
| `round` | Redondea un número a los decimales indicados. | 3 |
| `seed` | Fija la semilla del azar para que salga siempre lo mismo. | 1 |
| `sorted` | Devuelve los elementos ordenados, sin cambiar el original. | 3 |
| `split` | Parte un texto en trozos por un separador. | 3 |
| `StandardScaler` | Escala los números para que tengan media 0 y desviación 1. | 2 |
| `str` | Da acceso a las operaciones de texto sobre una columna. | 3 |
| `TestClient` | *(sin explicar todavía)* | 12 |
| `today` | Fecha de hoy. | 3 |
| `tolist` | Convierte un array o una columna en una lista de Python. | 3 |
| `train_test_split` | Reparte los datos en entrenamiento y prueba. | 2 |
| `unique` | Devuelve los valores distintos. | 3 |
| `values` | Devuelve los valores de un diccionario o de una tabla. | 10 |
| `VBox` | *(sin explicar todavía)* | 10 |
| `version` | *(sin explicar todavía)* | 13 |
| `write` | Escribe en un fichero. | 4, 9, 11, 13 |

## 4. Celda a celda

🏫 = se hace en clase · 🏠 = para casa. Las celdas de **ejercicio** no llevan código aquí: son vuestras, y la solución de referencia está en el propio cuaderno.

### Celda 1 · 🏫

**Qué hace:** Practica `seed`, `join`.

```python
import os, sys, json, py_compile
from datetime import date
import numpy as np
import pandas as pd
import joblib
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

SEMILLA = 42
np.random.seed(SEMILLA)
CARPETA = "demostrador"                    # aquí se crean modelo/, logica.py, app.py y api.py
os.makedirs(os.path.join(CARPETA, "modelo"), exist_ok=True)
```

**Qué hace cada línea:**

- `import os, sys, json, py_compile` → Trae `os`, `sys`, `json`, `py_compile` para poder usarlo.
- `from datetime import date` → Trae `date` de `datetime` para poder usarlo.
- `import numpy as np` → Trae `numpy` (lo llamamos `np`) para poder usarlo.
- `import pandas as pd` → Trae `pandas` (lo llamamos `pd`) para poder usarlo.
- `import joblib` → Trae `joblib` para poder usarlo.
- `import sklearn` → Trae `sklearn` para poder usarlo.
- `from sklearn.model_selection import train_test_split` → Trae `train_test_split` de `sklearn.model_selection` para poder usarlo.
- `from sklearn.compose import ColumnTransformer` → Trae `ColumnTransformer` de `sklearn.compose` para poder usarlo.
- `from sklearn.pipeline import Pipeline` → Trae `Pipeline` de `sklearn.pipeline` para poder usarlo.
- … y 7 más con las mismas ideas.

### Celda 2 · 1. Guardar el modelo y sus metadatos · 🏫

**Qué hace:** Practica `read_csv`, `train_test_split`, `ColumnTransformer`, `fit` y más (sección «1. Guardar el modelo y sus metadatos»).

```python
reservas = pd.read_csv(dato("reservas_turisdata.csv"))
NUMERICAS = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche", "cliente_repetidor", "cancelaciones_previas"]
CATEGORICAS = ["tipo_habitacion", "canal", "tarifa", "deposito"]
X, y = reservas[NUMERICAS + CATEGORICAS], reservas["cancelada"]
X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEMILLA)

prep = ColumnTransformer([("num", StandardScaler(), NUMERICAS), ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAS)])
modelo = Pipeline([("prep", prep), ("m", LogisticRegression(max_iter=2000))]).fit(X_ent, y_ent)
auc_test = roc_auc_score(y_test, modelo.predict_proba(X_test)[:, 1])
print(f"AUC en test: {auc_test:.3f}")
```

**Qué hace cada línea:**

- `reservas = pd.read_csv(dato("reservas_turisdata.csv"))` → Guarda en `reservas` el resultado. `read_csv`: lee un fichero CSV y lo convierte en una tabla; `dato`: devuelve la ruta de un fichero de datos del curso (lo busca en las carpetas habituales y, si no está, lo descarga).
- `NUMERICAS = ["antelacion_dias", "noches", "adultos", "ninos", "precio_noche…` → Guarda el valor en `NUMERICAS`.
- `CATEGORICAS = ["tipo_habitacion", "canal", "tarifa", "deposito"]` → Guarda el valor en `CATEGORICAS`.
- `X, y = reservas[NUMERICAS + CATEGORICAS], reservas["cancelada"]` → Guarda el valor en `X, y`.
- `X_ent, X_test, y_ent, y_test = train_test_split(X, y, test_size=0.2, strati…` → Guarda en `X_ent, X_test, y_ent, y…` el resultado. `train_test_split`: reparte los datos en entrenamiento y prueba.
- `prep = ColumnTransformer([("num", StandardScaler(), NUMERICAS), ("cat", One…` → Guarda en `prep` el resultado. `ColumnTransformer`: aplica un preprocesado distinto a cada grupo de columnas; `StandardScaler`: escala los números para que tengan media 0 y desviación 1; `OneHotEncoder`: convierte categorías en columnas de 0/1.
- `modelo = Pipeline([("prep", prep), ("m", LogisticRegression(max_iter=2000))…` → Guarda en `modelo` el resultado. `fit`: entrena el modelo con los datos (aquí es donde «aprende»); `Pipeline`: encadena pasos (preprocesado + modelo) en un solo objeto; `LogisticRegression`: modelo de clasificación que da una probabilidad (aunque se llame «regresión»).
- `auc_test = roc_auc_score(y_test, modelo.predict_proba(X_test)[:, 1])` → Guarda en `auc_test` el resultado. `roc_auc_score`: calcula el AUC: la capacidad del modelo para ordenar bien los casos (1 = perfecto, 0,5 = azar); `predict_proba`: pide la probabilidad de cada clase (no solo la clase).
- `print(f"AUC en test: {auc_test:.3f}")` → `print`: muestra un valor por pantalla.

### Celda 3 · 1. Guardar el modelo y sus metadatos · 🏫

**Qué hace:** Practica `round`, `join`, `open`, `listdir` y más (sección «1. Guardar el modelo y sus metadatos»).

```python
meta = {
    "nombre": "Riesgo de cancelación de reservas · TurisData (datos sintéticos)",
    "campos": {
        "antelacion_dias": {"tipo": "entero", "min": int(X["antelacion_dias"].min()), "max": int(X["antelacion_dias"].max()), "etiqueta": "Antelación (días entre reserva y llegada)"},
        "noches": {"tipo": "entero", "min": 1, "max": 30, "etiqueta": "Noches"},
        "adultos": {"tipo": "entero", "min": 1, "max": 6, "etiqueta": "Adultos"},
        "ninos": {"tipo": "entero", "min": 0, "max": 6, "etiqueta": "Niños"},
        "precio_noche": {"tipo": "decimal", "min": 20.0, "max": 600.0, "etiqueta": "Precio por noche (€)"},
        "cliente_repetidor": {"tipo": "entero", "min": 0, "max": 1, "etiqueta": "Cliente repetidor (0 = no, 1 = sí)"},
        "cancelaciones_previas": {"tipo": "entero", "min": 0, "max": 10, "etiqueta": "Cancelaciones previas"},
        **{c: {"tipo": "categoria", "valores": sorted(X[c].unique().tolist()), "etiqueta": c.replace("_", " ").capitalize()} for c in CATEGORICAS},
    },
    "auc_test": round(float(auc_test), 3),
    "n_entrenamiento": int(len(X_ent)),
    "tasa_cancelacion_base": round(float(y.mean()), 3),
    "entrenado": str(date.today()),
    "semilla": SEMILLA,
    "versiones": {"python": sys.version.split()[0], "scikit-learn": sklearn.__version__, "pandas": pd.__version__, "numpy": np.__version__},
    "limitaciones": "Entrenado con datos sintéticos de un solo alojamiento ficticio. No usar para decidir sobre personas concretas: solo orienta la gestión de disponibilidad.",
}
joblib.dump(modelo, os.path.join(CARPETA, "modelo", "modelo_cancelaciones.joblib"))
with open(os.path.join(CARPETA, "modelo", "metadatos.json"), "w", encoding="utf8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)
print("Guardado:", os.listdir(os.path.join(CARPETA, "modelo")))
```

**Qué hace cada línea:**

- `meta = {` → Guarda en `meta` el resultado. `round`: redondea un número a los decimales indicados; `int`: convierte un valor en número entero; `str`: da acceso a las operaciones de texto sobre una columna.
- `joblib.dump(modelo, os.path.join(CARPETA, "modelo", "modelo_cancelaciones.j…` → `join`: une una lista de textos en uno solo con un separador.
- `with open(os.path.join(CARPETA, "modelo", "metadatos.json"), "w", encoding=…` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `dump`: escribe datos de Python en un fichero JSON.
- `print("Guardado:", os.listdir(os.path.join(CARPETA, "modelo")))` → `print`: muestra un valor por pantalla; `listdir`: lista el contenido de una carpeta; `join`: une una lista de textos en uno solo con un separador.

### Celda 4 · 2. La lógica, separada de la interfaz · 🏫

**Qué hace:** Practica `insert`, `open`, `write`, `join` (sección «2. La lógica, separada de la interfaz»).

```python
LOGICA = r'''"""Lógica del demostrador: cargar el modelo, validar la entrada y predecir. Sin interfaz."""
import json
import os

import joblib
import pandas as pd

CARPETA = os.path.dirname(os.path.abspath(__file__))


def cargar_modelo(carpeta=None):
    """Devuelve (modelo, metadatos). Lanza FileNotFoundError con un mensaje claro si faltan los archivos."""
    carpeta = carpeta or os.path.join(CARPETA, "modelo")
    ruta_modelo = os.path.join(carpeta, "modelo_cancelaciones.joblib")
    ruta_meta = os.path.join(carpeta, "metadatos.json")
    if not (os.path.exists(ruta_modelo) and os.path.exists(ruta_meta)):
        raise FileNotFoundError("Falta el modelo. Ejecuta primero el notebook S16_01 (o tu script de entrenamiento) para crear la carpeta 'modelo/'.")
    with open(ruta_meta, encoding="utf8") as f:
        return joblib.load(ruta_modelo), json.load(f)


def validar_reserva(reserva, meta):
    """Devuelve una lista de errores en español (lista vacía = entrada válida)."""
    errores = []
    for campo, regla in meta["campos"].items():
        if campo not in reserva or reserva[campo] in (None, ""):
            errores.append(f"Falta el campo '{campo}'.")
            continue
        valor = reserva[campo]
        if regla["tipo"] == "categoria":
            if valor not in regla["valores"]:
                errores.append(f"'{valor}' no es un valor válido para '{campo}'. Opciones: {', '.join(regla['valores'])}.")
        else:
            try:
                numero = float(valor)
            except (TypeError, ValueError):
                errores.append(f"'{campo}' debe ser un número (has escrito '{valor}').")
                continue
            if not regla["min"] <= numero <= regla["max"]:
                errores.append(f"'{campo}' debe estar entre {regla['min']} y {regla['max']} (has escrito {valor}).")
    return errores


def nivel_riesgo(probabilidad):
    """Traduce la probabilidad a una etiqueta que entiende quien no sabe de modelos."""
    if probabilidad < 0.30:
        return "bajo"
    if probabilidad < 0.50:
        return "medio"
    return "alto"


def predecir_reserva(reserva, modelo, meta):
    """Valida y predice. Devuelve un diccionario; si hay errores, solo {'errores': [...]}."""
    errores = validar_reserva(reserva, meta)
    if errores:
        return {"errores": errores}
    fila = pd.DataFrame([reserva])[list(meta["campos"])]
    probabilidad = float(modelo.predict_proba(fila)[0, 1])
    return {
        "errores": [],
        "probabilidad": round(probabilidad, 3),
        "nivel": nivel_riesgo(probabilidad),
        "tasa_base": meta["tasa_cancelacion_base"],
        "aviso": (f"Estimación orientativa. El modelo tiene un AUC de {meta['auc_test']} en datos de prueba: "
                  "se equivoca con frecuencia. "
                  + meta["limitaciones"]),
    }
'''
with open(os.path.join(CARPETA, "logica.py"), "w", encoding="utf8") as f:
    f.write(LOGICA)

sys.path.insert(0, CARPETA)
import importlib, logica
importlib.reload(logica)
modelo_cargado, meta_cargado = logica.cargar_modelo()

reserva_ejemplo = {"antelacion_dias": 120, "noches": 5, "adultos": 2, "ninos": 1, "precio_noche": 95.0, "cliente_repetidor": 0,
                   "cancelaciones_previas": 0, "tipo_habitacion": "estandar", "canal": "web_intermediaria", "tarifa": "flexible", "deposito": "sin_deposito"}
print(logica.predecir_reserva(reserva_ejemplo, modelo_cargado, meta_cargado))
print(logica.predecir_reserva({**reserva_ejemplo, "noches": -3, "canal": "telepatia"}, modelo_cargado, meta_cargado))
```

**Qué hace cada línea:**

- `LOGICA = r'''"""Lógica del demostrador: cargar el modelo, validar la entrad…` → Guarda el valor en `LOGICA`.
- `with open(os.path.join(CARPETA, "logica.py"), "w", encoding="utf8") as f:` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `write`: escribe en un fichero.
- `sys.path.insert(0, CARPETA)` → `insert`: inserta elementos en una posición.
- `import importlib, logica` → Trae `importlib`, `logica` para poder usarlo.
- `modelo_cargado, meta_cargado = logica.cargar_modelo()` → Guarda en `modelo_cargado, meta_ca…` el resultado. `cargar_modelo`: devuelve (modelo, metadatos). Lanza FileNotFoundError con un mensaje claro si faltan los archivos.
- `reserva_ejemplo = {"antelacion_dias": 120, "noches": 5, "adultos": 2, "nino…` → Guarda el valor en `reserva_ejemplo`.
- `print(logica.predecir_reserva(reserva_ejemplo, modelo_cargado, meta_cargado…` → `print`: muestra un valor por pantalla; `predecir_reserva`: valida y predice. Devuelve un diccionario; si hay errores, solo {'errores': [...]}.
- `print(logica.predecir_reserva({**reserva_ejemplo, "noches": -3, "canal": "t…` → `print`: muestra un valor por pantalla; `predecir_reserva`: valida y predice. Devuelve un diccionario; si hay errores, solo {'errores': [...]}.

### Celda 5 · 2. La lógica, separada de la interfaz · 🏠 · ejercicio 1

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 6 · 2. La lógica, separada de la interfaz · 🏠 · ejercicio 2

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 7 · 3. Pruebas de sentido común · 🏠 · ejercicio 3

Es un **ejercicio**: el enunciado y la pista están en el cuaderno, justo encima de la celda. Cuando funcione, la celda siguiente lo **comprueba sola** con un `assert`.

### Celda 8 · 3. Pruebas de sentido común · 🏠

**Qué hace:** Estas pruebas se guardarían tal cual en tests/test_logica.py (se ejecutan con: pytest -q).

```python
# Estas pruebas se guardarían tal cual en tests/test_logica.py (se ejecutan con:  pytest -q)
def test_reserva_valida_devuelve_probabilidad():
    r = logica.predecir_reserva(reserva_ejemplo, modelo_cargado, meta_cargado)
    assert 0 <= r["probabilidad"] <= 1 and r["nivel"] in ("bajo", "medio", "alto") and "aviso" in r

def test_entrada_invalida_no_rompe():
    r = logica.predecir_reserva({**reserva_ejemplo, "noches": -3}, modelo_cargado, meta_cargado)
    assert r["errores"] and "probabilidad" not in r

def test_falta_un_campo():
    incompleta = {k: v for k, v in reserva_ejemplo.items() if k != "canal"}
    assert any("canal" in e for e in logica.validar_reserva(incompleta, meta_cargado))

def test_sentido_comun():
    assert p_alto > p_bajo

for prueba in (test_reserva_valida_devuelve_probabilidad, test_entrada_invalida_no_rompe, test_falta_un_campo, test_sentido_comun):
    prueba()
    print("OK ", prueba.__name__)
```

**Qué hace cada línea:**

- `def test_reserva_valida_devuelve_probabilidad():` → Define la función `test_reserva_valida_devuelve_probabilidad`: Función definida en el cuaderno.
- `def test_entrada_invalida_no_rompe():` → Define la función `test_entrada_invalida_no_rompe`: Función definida en el cuaderno.
- `def test_falta_un_campo():` → Define la función `test_falta_un_campo`: Función definida en el cuaderno.
- `def test_sentido_comun():` → Define la función `test_sentido_comun`: Función definida en el cuaderno.
- `for prueba in (test_reserva_valida_devuelve_probabilidad, test_entrada_inva…` → Repite el bloque de debajo para cada valor de `prueba` en `(test_reserva_valida_devuelve_probabili…`.

### Celda 9 · 4. Opción A (recomendada): app de Streamlit · 🏫

**Qué hace:** Practica `compile`, `open`, `write`, `join` (sección «4. Opción A (recomendada): app de Strea…»).

```python
APP = r'''"""Demostrador Streamlit · TurisData. Lanzar con:  streamlit run app.py"""
import streamlit as st

from logica import cargar_modelo, predecir_reserva

st.set_page_config(page_title="Riesgo de cancelación · TurisData", layout="centered")


@st.cache_resource
def cargar():
    return cargar_modelo()


st.title("Riesgo de cancelación de una reserva")
st.caption("Demostrador del proyecto. Datos sintéticos de TurisData Canarias (empresa ficticia).")

try:
    modelo, meta = cargar()
except FileNotFoundError as error:
    st.error(str(error))
    st.stop()

with st.form("formulario"):
    reserva = {}
    columnas = st.columns(2)
    for i, (campo, regla) in enumerate(meta["campos"].items()):
        with columnas[i % 2]:
            if regla["tipo"] == "categoria":
                reserva[campo] = st.selectbox(regla["etiqueta"], regla["valores"])
            elif regla["tipo"] == "entero":
                reserva[campo] = st.number_input(regla["etiqueta"], value=int(max(regla["min"], min(regla["max"], 1))), step=1)
            else:
                reserva[campo] = st.number_input(regla["etiqueta"], value=float(regla["min"] + 75.0), step=5.0)
    enviado = st.form_submit_button("Calcular riesgo")

if enviado:
    resultado = predecir_reserva(reserva, modelo, meta)
    if resultado["errores"]:
        st.warning("No se puede calcular todavía:\n\n" + "\n".join(f"- {e}" for e in resultado["errores"]))
    else:
        c1, c2 = st.columns(2)
        c1.metric("Probabilidad de cancelación", f"{resultado['probabilidad']:.0%}", f"{resultado['probabilidad'] - resultado['tasa_base']:+.0%} frente a la media")
        c2.metric("Nivel de riesgo", resultado["nivel"].upper())
        st.progress(resultado["probabilidad"])
        st.info(resultado["aviso"])
'''
with open(os.path.join(CARPETA, "app.py"), "w", encoding="utf8") as f:
    f.write(APP)
py_compile.compile(os.path.join(CARPETA, "app.py"), doraise=True)      # comprueba que no tiene errores de sintaxis
print("app.py creado y sin errores de sintaxis. Para verlo: cd demostrador && streamlit run app.py")
```

**Qué hace cada línea:**

- `APP = r'''"""Demostrador Streamlit · TurisData. Lanzar con: streamlit run a…` → Guarda el valor en `APP`.
- `with open(os.path.join(CARPETA, "app.py"), "w", encoding="utf8") as f:` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `write`: escribe en un fichero.
- `py_compile.compile(os.path.join(CARPETA, "app.py"), doraise=True) # comprue…` → `compile`: prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas); `join`: une una lista de textos en uno solo con un separador.
- `print("app.py creado y sin errores de sintaxis. Para verlo: cd demostrador…` → `print`: muestra un valor por pantalla.

### Celda 10 · 5. Opción B: notebook con widgets (plan B sin i… · 🏠

**Qué hace:** Practica `items`, `display`, `list`, `isinstance` y más (sección «5. Opción B: notebook con widgets (plan…»).

```python
try:
    import ipywidgets as widgets
    from IPython.display import display, clear_output
    HAY_WIDGETS = True
except ImportError:
    HAY_WIDGETS = False
    print("ipywidgets no está instalado. En local: pip install ipywidgets (en Colab ya viene incluido).")

if HAY_WIDGETS:
    campos = {}
    for campo, regla in meta_cargado["campos"].items():
        if regla["tipo"] == "categoria":
            campos[campo] = widgets.Dropdown(options=regla["valores"], description=regla["etiqueta"][:22], style={"description_width": "170px"})
        else:
            campos[campo] = widgets.FloatText(value=float(reserva_ejemplo[campo]), description=regla["etiqueta"][:22], style={"description_width": "170px"})
    boton = widgets.Button(description="Calcular riesgo", button_style="primary")
    salida = widgets.Output()

    def al_pulsar(_):
        with salida:
            clear_output()
            reserva = {c: (w.value if isinstance(w, widgets.Dropdown) else (int(w.value) if meta_cargado["campos"][c]["tipo"] == "entero" else w.value))
                       for c, w in campos.items()}
            r = logica.predecir_reserva(reserva, modelo_cargado, meta_cargado)
            if r["errores"]:
                print(mensaje_errores(r["errores"]))
            else:
                print(f"Probabilidad de cancelación: {r['probabilidad']:.0%}  (riesgo {r['nivel']}; media histórica {r['tasa_base']:.0%})")
                print(r["aviso"])
    boton.on_click(al_pulsar)
    display(widgets.VBox(list(campos.values()) + [boton, salida]))
```

**Qué hace cada línea:**

- `try:` → Intenta el bloque; si ocurre un error, pasa al `except` en vez de romperse.
- `if HAY_WIDGETS:` → Decide: ejecuta el bloque solo si se cumple la condición (y `elif`/`else` si no). Dentro del bloque: `items`: devuelve las parejas (clave, valor) de un diccionario; `predecir_reserva`: valida y predice. Devuelve un diccionario; si hay errores, solo {'errores': [...]}; `isinstance`: comprueba si un valor es de un tipo concreto.

### Celda 11 · 6. Opción C (opcional): API con FastAPI · 🏠

**Qué hace:** Practica `compile`, `open`, `write`, `join` (sección «6. Opción C (opcional): API con FastAPI»).

```python
API = r'''"""API local del modelo. Lanzar con:  uvicorn api:app --reload"""
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from logica import cargar_modelo, predecir_reserva

app = FastAPI(title="Riesgo de cancelación · TurisData", version="1.0")
modelo, meta = cargar_modelo()


class Reserva(BaseModel):
    antelacion_dias: int = Field(ge=0, le=1000)
    noches: int = Field(ge=1, le=30)
    adultos: int = Field(ge=1, le=6)
    ninos: int = Field(ge=0, le=6)
    precio_noche: float = Field(ge=20, le=600)
    cliente_repetidor: int = Field(ge=0, le=1)
    cancelaciones_previas: int = Field(ge=0, le=10)
    tipo_habitacion: str
    canal: str
    tarifa: Literal["flexible", "no_reembolsable"]
    deposito: Literal["sin_deposito", "parcial", "total"]


@app.get("/salud")
def salud():
    return {"estado": "ok", "modelo": meta["nombre"], "auc_test": meta["auc_test"]}


@app.post("/predecir")
def predecir(reserva: Reserva):
    resultado = predecir_reserva(reserva.model_dump(), modelo, meta)
    if resultado["errores"]:
        raise HTTPException(status_code=422, detail=resultado["errores"])
    return resultado
'''
with open(os.path.join(CARPETA, "api.py"), "w", encoding="utf8") as f:
    f.write(API)
py_compile.compile(os.path.join(CARPETA, "api.py"), doraise=True)
print("api.py creado y sin errores de sintaxis.")
```

**Qué hace cada línea:**

- `API = r'''"""API local del modelo. Lanzar con: uvicorn api:app --reload"""` → Guarda el valor en `API`.
- `with open(os.path.join(CARPETA, "api.py"), "w", encoding="utf8") as f:` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `write`: escribe en un fichero.
- `py_compile.compile(os.path.join(CARPETA, "api.py"), doraise=True)` → `compile`: prepara el modelo para entrenar (en Keras: elige optimizador, pérdida y métricas); `join`: une una lista de textos en uno solo con un separador.
- `print("api.py creado y sin errores de sintaxis.")` → `print`: muestra un valor por pantalla.

### Celda 12 · 6. Opción C (opcional): API con FastAPI · 🏠

**Qué hace:** Comprobación OPCIONAL de la API (se salta si faltan fastapi o httpx).

```python
# Comprobación OPCIONAL de la API (se salta si faltan fastapi o httpx)
try:
    from fastapi.testclient import TestClient
    import api
    importlib.reload(api)
    cliente = TestClient(api.app)
    print("/salud →", cliente.get("/salud").json())
    ok = cliente.post("/predecir", json=reserva_ejemplo)
    print("/predecir (válida) →", ok.status_code, ok.json()["probabilidad"])
    mal = cliente.post("/predecir", json={**reserva_ejemplo, "noches": -3})
    print("/predecir (noches=-3) →", mal.status_code, "(la API rechaza la entrada errónea)")
    mal2 = cliente.post("/predecir", json={**reserva_ejemplo, "canal": "telepatia"})
    print("/predecir (canal inventado) →", mal2.status_code, mal2.json()["detail"][0][:60])
except ImportError as e:
    print("Comprobación de la API omitida (opcional):", e)
```

**Qué hace cada línea:**

- `try:` → Intenta el bloque; si ocurre un error, pasa al `except` en vez de romperse. Dentro del bloque: `get`: lee un valor de un diccionario; si no existe, devuelve el valor por defecto en vez de fallar.

### Celda 13 · 7. Lista de reproducibilidad del demostrador · 🏠

**Qué hace:** Generamos un requirements.txt con las versiones exactas de este entorno (revísalo y recórtalo a lo que uses).

```python
# Generamos un requirements.txt con las versiones exactas de este entorno (revísalo y recórtalo a lo que uses)
import importlib.metadata as md
paquetes = ["numpy", "pandas", "scikit-learn", "joblib", "streamlit", "ipywidgets", "fastapi", "uvicorn"]
lineas = []
for p in paquetes:
    try:
        lineas.append(f"{p}=={md.version(p)}")
    except md.PackageNotFoundError:
        lineas.append(f"# {p}  (no instalado aquí: fija la versión que uses)")
with open(os.path.join(CARPETA, "requirements.txt"), "w", encoding="utf8") as f:
    f.write("\n".join(lineas) + "\n")
print("\n".join(lineas))
```

**Qué hace cada línea:**

- `import importlib.metadata as md` → Trae `importlib.metadata` (lo llamamos `md`) para poder usarlo.
- `paquetes = ["numpy", "pandas", "scikit-learn", "joblib", "streamlit", "ipyw…` → Guarda el valor en `paquetes`.
- `lineas = []` → Guarda el valor en `lineas`.
- `for p in paquetes:` → Repite el bloque de debajo para cada valor de `p` en `paquetes`.
- `with open(os.path.join(CARPETA, "requirements.txt"), "w", encoding="utf8")…` → Abre un recurso (fichero, conexión…) y lo cierra solo al terminar el bloque. Dentro del bloque: `write`: escribe en un fichero; `join`: une una lista de textos en uno solo con un separador.
- `print("\n".join(lineas))` → `print`: muestra un valor por pantalla; `join`: une una lista de textos en uno solo con un separador.

---
*Generado a partir de `laboratorios/fuentes/S16_01_demostrador.py`. Si algo no os cuadra con lo que sale en vuestra pantalla, preguntad al docente.*
