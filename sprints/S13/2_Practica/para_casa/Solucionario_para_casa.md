# Solucionario · cuadernos completos («para casa») del Sprint 13

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S13_01`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).
- Los **mini-retos abiertos** (sin una única respuesta correcta) no llevan solución aquí: se contrastan con el razonamiento y con las cifras del propio cuaderno.
- El cuaderno del reto (`S13_02`) no se incluye(n): su solución se contrasta con la rúbrica del reto.

---

## S13_01 · Contar lo que hace el modelo: visualización de resultados

### A3 · EJERCICIO 1 de 5 — Matriz de confusión normalizada y recall

> Calcula `cm` con `confusion_matrix(y_test, pred_lr, normalize="true")`, siendo `pred_lr` la predicción de
> la logística con umbral 0,5 (`prob_lr >= 0.5`). Guarda en `recall_cancelaciones` la proporción de
> cancelaciones reales que el modelo detecta (fila de las cancelaciones, columna "cancela").

```python
pred_lr = (prob_lr >= 0.5).astype(int)
cm = confusion_matrix(y_test, pred_lr, normalize="true")
recall_cancelaciones = cm[1, 1]

print(f"Ejercicio 1 correcto ✔ — el modelo detecta el {recall_cancelaciones:.0%} de las cancelaciones")

fig, ax = plt.subplots(figsize=(4.5, 4))
ConfusionMatrixDisplay(cm, display_labels=["No cancela", "Cancela"]).plot(ax=ax, cmap="Blues", values_format=".0%", colorbar=False)
ax.set_title("Matriz de confusión (% de cada clase real)")
ax.set_xlabel("Lo que dijo el modelo"); ax.set_ylabel("Lo que ocurrió")
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Ejercicio 1 correcto ✔ — el modelo detecta el 62% de las cancelaciones
```

Y además dibuja un gráfico.

### A5 · EJERCICIO 2 de 5 — AUC y precisión media de los dos modelos

> Calcula `auc_lr` y `auc_rf` (`roc_auc_score`) y `ap_lr` y `ap_rf` (`average_precision_score`, el área
> de la curva PR) para ambos modelos con las probabilidades `prob_lr` y `prob_rf`. Guarda en
> `mejor_modelo` el texto `"Regresión logística"` o `"Bosque aleatorio"` según cuál tenga mayor AUC.

```python
auc_lr, auc_rf = roc_auc_score(y_test, prob_lr), roc_auc_score(y_test, prob_rf)
ap_lr, ap_rf = average_precision_score(y_test, prob_lr), average_precision_score(y_test, prob_rf)
mejor_modelo = "Regresión logística" if auc_lr >= auc_rf else "Bosque aleatorio"

print(f"Ejercicio 2 correcto ✔ — AUC logística {auc_lr:.3f} · bosque {auc_rf:.3f} → {mejor_modelo}")

fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
for nombre, prob, color in (("Regresión logística", prob_lr, "tab:blue"), ("Bosque aleatorio", prob_rf, "tab:orange")):
    fpr, tpr, _ = roc_curve(y_test, prob)
    ax[0].plot(fpr, tpr, color=color, label=f"{nombre} (AUC = {roc_auc_score(y_test, prob):.2f})")
    prec, rec, _ = precision_recall_curve(y_test, prob)
    ax[1].plot(rec, prec, color=color, label=f"{nombre} (AP = {average_precision_score(y_test, prob):.2f})")
ax[0].plot([0, 1], [0, 1], "--", color="gray", label="Azar")
ax[0].set_xlabel("Falsas alarmas (% de no cancelaciones avisadas)"); ax[0].set_ylabel("Cancelaciones detectadas")
ax[0].set_title("Curva ROC"); ax[0].legend(loc="lower right")
ax[1].axhline(y_test.mean(), linestyle="--", color="gray", label="Azar (tasa de cancelación)")
ax[1].set_xlabel("Exhaustividad (cancelaciones detectadas)"); ax[1].set_ylabel("Precisión (avisos que eran ciertos)")
ax[1].set_title("Curva precisión-exhaustividad"); ax[1].legend(loc="upper right"); ax[1].set_ylim(0, 1)
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Ejercicio 2 correcto ✔ — AUC logística 0.744 · bosque 0.733 → Regresión logística
```

Y además dibuja un gráfico.

### A7 · EJERCICIO 3 de 5 — Importancia por permutación

> Calcula la importancia por permutación de `modelo_lr` sobre `X_test`/`y_test` con
> `permutation_importance(..., scoring="roc_auc", n_repeats=5, random_state=SEMILLA)`.
> Guarda en la `Series` `importancias` la media (`importances_mean`) con el nombre de cada variable como
> índice, ordenada de mayor a menor, y en `top3` la lista de las 3 primeras variables.

```python
res = permutation_importance(modelo_lr, X_test, y_test, scoring="roc_auc", n_repeats=5, random_state=SEMILLA)
importancias = pd.Series(res.importances_mean, index=X_test.columns).sort_values(ascending=False)
top3 = importancias.index[:3].tolist()

print("Ejercicio 3 correcto ✔ — las 3 más importantes:", top3)

fig, ax = plt.subplots(figsize=(7, 4))
importancias.head(8)[::-1].plot.barh(ax=ax, color="tab:blue")
ax.set_xlabel("Caída del AUC al desordenar la variable")
ax.set_title(f"Lo que más pesa en una cancelación: {top3[0]}")
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Ejercicio 3 correcto ✔ — las 3 más importantes: ['antelacion_dias', 'deposito', 'canal']
```

Y además dibuja un gráfico.

### A9 · EJERCICIO 4 de 5 — El umbral que minimiza el coste

> Para cada umbral de `umbrales` (de 0,05 a 0,95), calcula el coste total con las probabilidades
> `prob_lr`: `50 × falsos negativos + 30 × falsos positivos`. Guarda los costes en la lista `costes`, el
> mejor umbral en `umbral_optimo` y su coste en `coste_minimo`. Guarda también `coste_05`, el coste del
> umbral 0,5.

```python
umbrales = np.round(np.arange(0.05, 0.96, 0.01), 2)

def coste_total(prob, umbral, c_fn=50, c_fp=30):
    pred = (prob >= umbral).astype(int)
    fn = int(((pred == 0) & (y_test == 1)).sum())
    fp = int(((pred == 1) & (y_test == 0)).sum())
    return c_fn * fn + c_fp * fp

costes = [coste_total(prob_lr, u) for u in umbrales]
umbral_optimo = umbrales[int(np.argmin(costes))]
coste_minimo = min(costes)
coste_05 = coste_total(prob_lr, 0.5)

print(f"Ejercicio 4 correcto ✔ — umbral óptimo {umbral_optimo:.2f}: ahorra {euros(coste_05 - coste_minimo)} frente al umbral 0,5 en esta muestra")

fig, ax = plt.subplots(figsize=(7, 3.8))
ax.plot(umbrales, costes, color="tab:blue")
ax.plot(umbral_optimo, coste_minimo, "o", color="tab:red")
ax.annotate(f"Umbral óptimo {umbral_optimo:.2f}\n{euros(coste_minimo)}", (umbral_optimo, coste_minimo),
            xytext=(umbral_optimo + 0.12, coste_minimo + 0.08 * (max(costes) - min(costes))),
            arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("Umbral (avisamos si la probabilidad supera este valor)"); ax.set_ylabel("Coste total en la muestra de prueba (€)")
ax.set_title(f"Coste total según el umbral: mínimo en {umbral_optimo:.2f}")
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Ejercicio 4 correcto ✔ — umbral óptimo 0.35: ahorra 1.900 € frente al umbral 0,5 en esta muestra
```

Y además dibuja un gráfico.

### A12 · EJERCICIO 5 de 5 — Gráfico para dirección: cancelación por depósito

> Crea para dirección un gráfico de barras de la **tasa de cancelación (%) por tipo de `deposito`**
> (`sin_deposito`, `parcial`, `total`). Cumple las reglas: figura `fig_dir` con un solo eje, barras desde 0,
> eje Y con nombre, valores etiquetados y un **título que sea una conclusión** (más de 25 caracteres).
> Usa la variable `tasa_deposito` (ya calculada) para las alturas.

```python
tasa_deposito = reservas.groupby("deposito")["cancelada"].mean().mul(100).reindex(["sin_deposito", "parcial", "total"])
fig_dir, ax = plt.subplots(figsize=(6, 3.8))
barras = ax.bar(["Sin depósito", "Depósito parcial", "Depósito total"], tasa_deposito.values, color=["tab:red", "lightgray", "lightgray"])
ax.bar_label(barras, fmt="%.0f %%", padding=3)
ax.set_ylim(0, 65)
ax.set_ylabel("Reservas canceladas (%)")
ax.set_title("Pedir depósito total reduce las cancelaciones a la mitad")
sns.despine()

ejes = fig_dir.axes
plt.tight_layout(); plt.show()
print("Ejercicio 5 correcto ✔")
```

**Tiene que salir:**

```text
Ejercicio 5 correcto ✔
```

Y además dibuja un gráfico.

