# Solucionario · cuadernos «en clase» del Sprint 15

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S15_01`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S15_01 · Seguimiento de experimentos y reproducibilidad

### Ejercicio 1 · Reproducibilidad: semillas y versiones

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

### Ejercicio 2 · El registro de experimentos: una fila por prueba

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

### Ejercicio 3 · Experimentos: baseline y modelos con validación cruzada

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

