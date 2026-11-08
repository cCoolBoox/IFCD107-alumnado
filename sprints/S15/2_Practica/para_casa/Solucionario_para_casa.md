# Solucionario · cuadernos completos («para casa») del Sprint 15

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S15_01`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).
- Los **mini-retos abiertos** (sin una única respuesta correcta) no llevan solución aquí: se contrastan con el razonamiento y con las cifras del propio cuaderno.

---

## S15_01 · Seguimiento de experimentos y reproducibilidad

### A2 · EJERCICIO 1 de 5 — Fijar las semillas

> Escribe `fijar_semillas(semilla)` que fije la semilla de `random` y de `numpy` (`np.random.seed`),
> guarde `PYTHONHASHSEED` en `os.environ` (como texto) y **devuelva** un generador
> `np.random.default_rng(semilla)`. (Con TensorFlow añadirías `tf.random.set_seed(semilla)`.)

```python
def fijar_semillas(semilla):
    random.seed(semilla)
    np.random.seed(semilla)
    os.environ["PYTHONHASHSEED"] = str(semilla)
    return np.random.default_rng(semilla)

SEMILLA = 42
rng = fijar_semillas(SEMILLA)
a = (random.random(), np.random.rand(), rng.random())
rng = fijar_semillas(SEMILLA)
b = (random.random(), np.random.rand(), rng.random())
print("Ejercicio 1 correcto ✔")

# Ficha del entorno: cópiala en la memoria técnica y en el README del equipo
ENTORNO = {"python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__, "scikit-learn": sklearn.__version__}
print(json.dumps(ENTORNO, indent=2))
```

**Tiene que salir:**

```text
Ejercicio 1 correcto ✔
{
  "python": "3.13.18",
  "numpy": "2.5.3",
  "pandas": "2.3.3",
  "scikit-learn": "1.9.1"
}
```

### A4 · EJERCICIO 2 de 5 — Escribir una fila en el registro

> Completa `registrar(...)`, que añade **una fila** al CSV `RUTA_REGISTRO`: si el archivo no existe, lo crea
> con la cabecera; si existe, añade la fila sin repetir la cabecera. El `id` es el número de filas ya
> existentes + 1. Devuelve el `id` asignado.

```python
RUTA_REGISTRO = "experimentos/registro.csv"
COLUMNAS = ["id", "fecha", "responsable", "modelo", "hiperparametros", "datos_hash", "semilla",
            "metrica", "valor_cv", "desv_cv", "tiempo_s", "notas"]
os.makedirs("experimentos", exist_ok=True)
if os.path.exists(RUTA_REGISTRO):
    os.remove(RUTA_REGISTRO)          # empezamos el laboratorio con el registro vacío

def registrar(responsable, modelo, hiperparametros, datos_hash, semilla, metrica, valor_cv, desv_cv, tiempo_s, notas=""):
    existe = os.path.exists(RUTA_REGISTRO)
    n = len(pd.read_csv(RUTA_REGISTRO)) if existe else 0
    fila = pd.DataFrame([{
        "id": n + 1, "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"), "responsable": responsable, "modelo": modelo,
        "hiperparametros": json.dumps(hiperparametros, sort_keys=True), "datos_hash": datos_hash, "semilla": semilla,
        "metrica": metrica, "valor_cv": round(float(valor_cv), 4), "desv_cv": round(float(desv_cv), 4),
        "tiempo_s": round(float(tiempo_s), 2), "notas": notas}], columns=COLUMNAS)
    fila.to_csv(RUTA_REGISTRO, mode="a", header=not existe, index=False)
    return n + 1

id1 = registrar("prueba", "ModeloDePrueba", {"a": 1}, "abc123", 42, "AUC", 0.5, 0.01, 0.1, "fila de prueba")
id2 = registrar("prueba", "ModeloDePrueba", {"a": 2}, "abc123", 42, "AUC", 0.6, 0.01, 0.1)
tabla_prueba = pd.read_csv(RUTA_REGISTRO)
os.remove(RUTA_REGISTRO)              # borramos las filas de prueba
print("Ejercicio 2 correcto ✔")
```

**Tiene que salir:**

```text
Ejercicio 2 correcto ✔
```

### A6 · EJERCICIO 3 de 5 — Registrar bosque y gradient boosting y elegir candidato

> Registra dos experimentos más con la función `experimento(nombre, estimador, hiperparametros)`:
> un **bosque aleatorio** `RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2)`
> con nombre `"RandomForest"` y un **gradient boosting** `HistGradientBoostingClassifier(random_state=SEMILLA)` con
> nombre `"HistGradientBoosting"` (hiperparámetros: los que uses, en un diccionario). Después lee el registro
> en `tabla` (`pd.read_csv(RUTA_REGISTRO)`) y guarda en `candidato` el **nombre del modelo con mayor `valor_cv`**.

```python
experimento("RandomForest", RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=SEMILLA, n_jobs=2),
            {"n_estimators": 200, "min_samples_leaf": 5})
experimento("HistGradientBoosting", HistGradientBoostingClassifier(random_state=SEMILLA), {"defecto": True})
tabla = pd.read_csv(RUTA_REGISTRO)
candidato = tabla.loc[tabla["valor_cv"].idxmax(), "modelo"]

print("Ejercicio 3 correcto ✔ — candidato provisional:", candidato)
tabla[["id", "modelo", "hiperparametros", "valor_cv", "desv_cv", "tiempo_s"]]

fig, ax = plt.subplots(figsize=(7, 3.5))
t = tabla.sort_values("valor_cv")
ax.barh(t["modelo"], t["valor_cv"], xerr=t["desv_cv"], color="tab:blue", capsize=4)
ax.axvline(0.5, color="gray", linestyle="--", label="Azar (AUC 0,5)")
ax.set_xlim(0.4, 0.85); ax.set_xlabel("AUC medio en validación cruzada (± desviación)")
ax.set_title("Comparativa de modelos (validación cruzada, sin usar el test)"); ax.legend(loc="lower right")
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Ejercicio 3 correcto ✔ — candidato provisional: RegresionLogistica
```

Y además dibuja un gráfico.

### A8 · EJERCICIO 4 de 5 — Probar tres profundidades del bosque

> Prueba un bosque aleatorio con `max_depth` = 3, 6 y 10 (resto de parámetros como antes), **registrando cada
> prueba** con `experimento` y el nombre `f"RandomForest_prof{d}"`. Guarda en `resultados_prof` un diccionario
> `{profundidad: AUC medio}` y en `mejor_prof` la profundidad con mejor AUC.

```python
resultados_prof = {}
for d in (3, 6, 10):
    media, desv = experimento(f"RandomForest_prof{d}",
                              RandomForestClassifier(n_estimators=200, min_samples_leaf=5, max_depth=d, random_state=SEMILLA, n_jobs=2),
                              {"n_estimators": 200, "min_samples_leaf": 5, "max_depth": d}, notas="ajuste de profundidad")
    resultados_prof[d] = media
mejor_prof = max(resultados_prof, key=resultados_prof.get)

print("Ejercicio 4 correcto ✔ — mejor profundidad:", mejor_prof, {k: round(v, 3) for k, v in resultados_prof.items()})
```

**Tiene que salir:**

```text
Ejercicio 4 correcto ✔ — mejor profundidad: 6 {3: np.float64(0.742), 6: np.float64(0.745), 10: np.float64(0.742)}
```

### A10 · EJERCICIO 5 de 5 — Evaluar el candidato en el test una sola vez

> Elige el candidato de la tabla (**solo con criterios de validación cruzada, sin fuga**): el
> `RandomForest_prof{mejor_prof}` o el ganador del ejercicio 3, el que tenga mayor `valor_cv` entre las filas
> **sin** la palabra "Fuga" en el nombre. Reentrénalo con todo `X_ent` y calcula el AUC en `X_test`
> (`auc_test`). Guarda en `auc_cv_candidato` su AUC de validación cruzada para compararlos.
> *(Pista: si el test sale muy por debajo de la validación cruzada, hay sobreajuste o fuga.)*

```python
tabla = pd.read_csv(RUTA_REGISTRO)
legitimos = tabla[~tabla["modelo"].str.contains("Fuga")]
fila = legitimos.loc[legitimos["valor_cv"].idxmax()]
hp = json.loads(fila["hiperparametros"])
if fila["modelo"] == "RegresionLogistica":
    estimador = LogisticRegression(max_iter=2000)
elif fila["modelo"] == "HistGradientBoosting":
    estimador = HistGradientBoostingClassifier(random_state=SEMILLA)
else:
    estimador = RandomForestClassifier(random_state=SEMILLA, n_jobs=2, **{k: v for k, v in hp.items()})
final = crear_pipeline(estimador, X_ent.columns).fit(X_ent, y_ent)
auc_test = roc_auc_score(y_test, final.predict_proba(X_test)[:, 1])
auc_cv_candidato = fila["valor_cv"]

print(f"Ejercicio 5 correcto ✔ — candidato: {fila['modelo']} · AUC validación {auc_cv_candidato:.3f} · AUC test {auc_test:.3f}")
```

**Tiene que salir:**

```text
Ejercicio 5 correcto ✔ — candidato: RegresionLogistica · AUC validación 0.755 · AUC test 0.745
```

