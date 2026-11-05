# Solucionario · cuadernos completos («para casa») del Sprint 5

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S05_01` a `S05_06`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).
- El cuaderno del reto (`S05_07`) no se incluye: su solución se contrasta con la rúbrica del reto.

---

## S05_01 · NumPy: arrays, vectorización y broadcasting

### Ejercicio 1 · Separar las columnas

> Guarda en cuatro variables las columnas de `tabla`: `ocupacion`, `temperatura`, `festivo` y `precio`.

```python
ocupacion = tabla[:, 0]
temperatura = tabla[:, 1]
festivo = tabla[:, 2]
precio = tabla[:, 3]
print("Correcto:", ocupacion.shape[0], "días")
```

**Tiene que salir:**

```text
Correcto: 1096 días
```

### Ejercicio 2 · Festivos frente a laborables

> Guarda en `media_festivos` la ocupación media de los días festivos y en `media_resto` la de los demás, ambas redondeadas a 2 decimales (`.round(2)`).

```python
media_festivos = ocupacion[festivo == 1].mean().round(2)
media_resto = ocupacion[festivo == 0].mean().round(2)
print(f"Festivos: {media_festivos} % · resto: {media_resto} % · diferencia: {media_festivos - media_resto:.2f} puntos")
```

**Tiene que salir:**

```text
Festivos: 83.88 % · resto: 67.58 % · diferencia: 16.30 puntos
```

### Ejercicio 3 · Ingreso diario y estandarización

> Suponiendo un alojamiento de **120 habitaciones**, el ingreso de cada día es `ocupacion / 100 * 120 * precio`. Guarda ese array en `ingreso_diario`. Después estandariza la ocupación (restar la media y dividir entre la desviación típica) en `ocupacion_z`.

```python
ingreso_diario = ocupacion / 100 * 120 * precio
ocupacion_z = (ocupacion - ocupacion.mean()) / ocupacion.std()
print(f"Correcto. Ingreso medio diario: {ingreso_diario.mean():,.0f} EUR")
```

**Tiene que salir:**

```text
Correcto. Ingreso medio diario: 7,237 EUR
```

### Ejercicio 4 · Estandarizar todas las columnas a la vez

> Guarda en `tabla_z` la tabla con **cada columna** estandarizada (media 0, desviación 1) usando broadcasting, sin bucles. Pista: `tabla.mean(axis=0)` y `tabla.std(axis=0)`.

```python
tabla_z = (tabla - tabla.mean(axis=0)) / tabla.std(axis=0)
print("Correcto")
```

**Tiene que salir:**

```text
Correcto
```

### Ejercicio 5 · Simulación reproducible

> Con un generador de semilla `SEMILLA`, genera `simulada` = 365 ocupaciones aleatorias con distribución normal de media 68,5 y desviación 9,6, y recórtalas al rango 0–100 con `np.clip`. Comprueba con un segundo generador igual que el resultado se repite.

```python
rng = np.random.default_rng(SEMILLA)
simulada = np.clip(rng.normal(68.5, 9.6, 365), 0, 100)
rng_b = np.random.default_rng(SEMILLA)
simulada_b = np.clip(rng_b.normal(68.5, 9.6, 365), 0, 100)
print("Correcto: media simulada", simulada.mean().round(2))
```

**Tiene que salir:**

```text
Correcto: media simulada 68.41
```

### 6 · Mini-reto integrador: media móvil de 7 días

> La ocupación diaria oscila mucho. Calcula `media_movil` con la **media de cada ventana de 7 días consecutivos** (una técnica que verás mucho en series temporales). Pista: `np.convolve(ocupacion, np.ones(7) / 7, mode="valid")`. Después se dibuja junto a la serie original.

```python
media_movil = np.convolve(ocupacion, np.ones(7) / 7, mode="valid")

plt.figure(figsize=(10, 3.5))
plt.plot(ocupacion, color="lightgray", label="Ocupación diaria")
plt.plot(np.arange(6, 1096), media_movil, color="tab:blue", label="Media móvil 7 días")
plt.xlabel("Día (desde 1/1/2023)")
plt.ylabel("Ocupación (%)")
plt.title("Ocupación diaria y su media móvil de 7 días")
plt.legend()
plt.tight_layout()
plt.show()
```

---

## S05_02 · Álgebra lineal con NumPy: vectores, matrices y sistemas de ecuaciones

### Ejercicio 1 · Producto escalar

> Un día se vendieron `noches_dia = [8, 6, 1]` noches de cada tipo, con los `precios` de arriba. Guarda en `ingreso_dia` el ingreso de ese día usando un producto escalar (sin bucles).

```python
noches_dia = np.array([8, 6, 1])
ingreso_dia = noches_dia @ precios
print("Correcto:", ingreso_dia)
```

**Tiene que salir:**

```text
Correcto: 1290.0
```

### Ejercicio 2 · Ingreso total con matrices

> Con `noches_semana` (4 días x 3 tipos) y un vector `tasa_por_noche = [1.5, 1.5, 3.0]` (tasa turística por noche y tipo), calcula: `ingresos_dia` (ingreso de alojamiento de cada día) y `tasas_dia` (tasas de cada día), y guarda en `total_semana` la suma de ambos para toda la semana (un número).

```python
tasa_por_noche = np.array([1.5, 1.5, 3.0])
ingresos_dia = noches_semana @ precios
tasas_dia = noches_semana @ tasa_por_noche
total_semana = (ingresos_dia + tasas_dia).sum()
print("Correcto:", total_semana)
```

**Tiene que salir:**

```text
Correcto: 6541.5
```

### Ejercicio 3 · Calcular precios desconocidos

> La contabilidad perdió los precios. Sabemos que, con `noches_ab` (filas = dos días; columnas = tipos A y B), se facturó `facturado` cada día. Guarda en `precios_ab` los precios de cada tipo.

```python
noches_ab = np.array([[12.0, 5.0],
                      [ 7.0, 9.0]])
facturado = np.array([1315.0, 1199.0])
precios_ab = np.linalg.solve(noches_ab, facturado)
print("Correcto:", precios_ab)
```

**Tiene que salir:**

```text
Correcto: [80. 71.]
```

### Ejercicio 4 · ¿Tiene solución?

> Dos filas iguales dan un sistema sin solución única. Guarda en `det_singular` el determinante de `M` (aproximado con `round(..., 6)`) y en `tiene_inversa` un booleano que diga si `M` se puede invertir.

```python
M = np.array([[2.0, 4.0],
              [1.0, 2.0]])
det_singular = round(np.linalg.det(M), 6)
tiene_inversa = det_singular != 0
print("Correcto: M no tiene inversa")
```

**Tiene que salir:**

```text
Correcto: M no tiene inversa
```

### Ejercicio 5 · Regresión por la ecuación normal

> Calcula `w` (vector de 2 coeficientes: término independiente y pendiente) con `np.linalg.solve` y la ecuación normal, usando `X` y `ocupacion`. Después, guarda en `prediccion_25` la ocupación predicha para un día de **25 °C**.

```python
w = np.linalg.solve(X.T @ X, X.T @ ocupacion)
prediccion_25 = np.array([1.0, 25.0]) @ w
print(f"Correcto: ocupación ≈ {w[0]:.2f} + ({w[1]:.2f}) x temperatura → a 25 °C: {prediccion_25:.1f} %")
```

**Tiene que salir:**

```text
Correcto: ocupación ≈ 107.73 + (-1.86) x temperatura → a 25 °C: 61.2 %
```

### 6 · Mini-reto integrador: varias variables a la vez

> Amplía el modelo: predice la ocupación con **temperatura, festivo y precio medio**. Construye `X3` con una columna de unos y esas tres variables (columnas 1, 2 y 3 de `tabla`), calcula `w3` con la ecuación normal y guarda en `efecto_festivo` el coeficiente del festivo (en puntos porcentuales).

```python
X3 = np.column_stack([np.ones(len(ocupacion)), tabla[:, 1:4]])
w3 = np.linalg.solve(X3.T @ X3, X3.T @ ocupacion)
efecto_festivo = w3[2]
print(f"Correcto: un festivo se asocia con {efecto_festivo:+.1f} puntos de ocupación, con temperatura y precio constantes")
```

**Tiene que salir:**

```text
Correcto: un festivo se asocia con +8.8 puntos de ocupación, con temperatura y precio constantes
```

---

## S05_03 · Descenso del gradiente y regresión lineal desde cero

### Ejercicio 1 · Derivada numérica

> Escribe la función `derivada_numerica(func, x, h=1e-6)` que devuelva la aproximación anterior para cualquier función.

```python
def derivada_numerica(func, x, h=1e-6):
    """Aproxima la derivada de func en x (diferencia centrada)."""
    return (func(x + h) - func(x - h)) / (2 * h)
print("Correcto")
```

**Tiene que salir:**

```text
Correcto
```

### Ejercicio 2 · MSE

> Escribe `mse(y_real, y_pred)`. Guarda en `mse_ingenuo` el MSE de un modelo "ingenuo" que predice **siempre la media** de la ocupación (será nuestra referencia a batir).

```python
def mse(y_real, y_pred):
    """Error cuadrático medio."""
    return np.mean((y_real - y_pred) ** 2)

mse_ingenuo = mse(ocupacion, ocupacion.mean())
print(f"Correcto. Referencia: MSE ingenuo = {mse_ingenuo:.2f} (error típico ≈ {np.sqrt(mse_ingenuo):.1f} puntos)")
```

**Tiene que salir:**

```text
Correcto. Referencia: MSE ingenuo = 92.36 (error típico ≈ 9.6 puntos)
```

### Ejercicio 3 · Tu propio descenso

> Usando `descender`, encuentra el mínimo de `g(x) = x² - 6x + 20` (mínimo en `x = 3`). Su derivada es `2x - 6`. Guarda en `x_minimo` el valor final tras **50 pasos** con tasa `0.1` partiendo de `x0 = 10`.

```python
camino_g = descender(lambda x: 2 * x - 6, 10.0, 0.1, 50)
x_minimo = camino_g[-1]
print(f"Correcto: x mínimo ≈ {x_minimo:.4f}")
```

**Tiene que salir:**

```text
Correcto: x mínimo ≈ 3.0001
```

### Ejercicio 4 · El gradiente

> Escribe `gradiente_mse(X, y, w)` que devuelva el vector gradiente `(2 / n) · Xᵀ (X w − y)`. El `assert` lo comparará con el gradiente calculado por derivadas numéricas.

```python
def gradiente_mse(X, y, w):
    """Gradiente del MSE de la regresión lineal y_pred = X @ w."""
    errores = X @ w - y
    return 2 / len(y) * X.T @ errores
w_prueba = np.array([50.0, 3.0])
numerico = np.array([
    derivada_numerica(lambda a: mse(y, X @ np.array([a, w_prueba[1]])), w_prueba[0]),
    derivada_numerica(lambda b: mse(y, X @ np.array([w_prueba[0], b])), w_prueba[1]),
])
print("Correcto: el gradiente analítico coincide con el numérico")
```

**Tiene que salir:**

```text
Correcto: el gradiente analítico coincide con el numérico
```

### Ejercicio 5 · Entrenar: el bucle del descenso del gradiente

> Escribe `entrenar(X, y, tasa=0.1, epocas=200)` que: 1. Empiece con `w = np.zeros(X.shape[1])`. 2. En cada época: calcule el gradiente y actualice `w = w - tasa * gradiente`. 3. Guarde el MSE de cada época en la lista `historial`. 4. Devuelva `(w, historial)`.

```python
def entrenar(X, y, tasa=0.1, epocas=200):
    """Descenso del gradiente para la regresión lineal. Devuelve (w, historial_de_mse)."""
    w = np.zeros(X.shape[1])
    historial = []
    for _ in range(epocas):
        w = w - tasa * gradiente_mse(X, y, w)
        historial.append(mse(y, X @ w))
    return w, historial
w_z, historial = entrenar(X, y)
w_exacto = np.linalg.solve(X.T @ X, X.T @ y)
print("Correcto:", w_z.round(3), "≈", w_exacto.round(3))
```

```python
# Curva de aprendizaje y recta ajustada
fig, ejes = plt.subplots(1, 2, figsize=(11, 3.8))
ejes[0].plot(historial)
ejes[0].set_xlabel("Época")
ejes[0].set_ylabel("MSE")
ejes[0].set_title("El error baja en cada paso")

ejes[1].scatter(temperatura, ocupacion, s=6, alpha=0.4, label="Días")
t_lin = np.linspace(temperatura.min(), temperatura.max(), 50)
ejes[1].plot(t_lin, w_z[0] + w_z[1] * (t_lin - media_t) / desv_t, color="crimson", label="Recta ajustada")
ejes[1].set_xlabel("Temperatura (°C)")
ejes[1].set_ylabel("Ocupación (%)")
ejes[1].set_title("Regresión desde cero: ocupación frente a temperatura")
ejes[1].legend()
plt.tight_layout()
plt.show()
```

**Tiene que salir:**

```text
Correcto: [68.488 -6.034] ≈ [68.488 -6.034]
```

### Ejercicio 6 · Diagnosticar la tasa

> Entrena con `tasa = 2.5` durante 30 épocas y guarda en `diverge` un booleano que indique si el MSE final es **mayor** que el MSE inicial (es decir, el entrenamiento se ha descontrolado).

```python
_, hist_grande = entrenar(X, y, tasa=2.5, epocas=30)
diverge = hist_grande[-1] > hist_grande[0]
print("Correcto: con una tasa demasiado grande el descenso se descontrola")
```

**Tiene que salir:**

```text
Correcto: con una tasa demasiado grande el descenso se descontrola
```

### Ejercicio 7 · Comprobar que coinciden

> Guarda en `coinciden` un booleano que indique si la pendiente y el intercepto "desde cero" coinciden con los de scikit-learn (tolerancia `1e-3`). Usa `np.isclose`.

```python
coinciden = bool(np.isclose(pendiente_scratch, modelo.coef_[0], atol=1e-3)
                 and np.isclose(intercepto_scratch, modelo.intercept_, atol=1e-3))
print("Correcto: ¡tu descenso del gradiente reproduce a scikit-learn!")
```

**Tiene que salir:**

```text
Correcto: ¡tu descenso del gradiente reproduce a scikit-learn!
```

### 7 · Mini-reto integrador: regresión múltiple desde cero

> Ahora con **tres variables**: temperatura, festivo y precio medio. La función `entrenar` ya sirve tal cual (el gradiente es el mismo para cualquier número de columnas). 1. Estandariza las tres variables (una a una o con broadcasting) y construye `X_multi` con la columna de unos. 2. Entrena con `entrenar(X_multi, y, tasa=0.1, epocas=500)`. 3. Guarda en `efecto_festivo` el efecto del festivo **en puntos de ocupación** (deshaz la estandarización:    coeficiente / desviación de la variable) y en `r2` el R² del modelo (`1 - MSE / varianza de y`).

```python
variables = np.column_stack([temperatura, festivo, precio])
medias, desvs = variables.mean(axis=0), variables.std(axis=0)
X_multi = np.column_stack([np.ones(len(y)), (variables - medias) / desvs])
w_multi, hist_multi = entrenar(X_multi, y, tasa=0.1, epocas=500)
efecto_festivo = w_multi[2] / desvs[1]
r2 = 1 - hist_multi[-1] / y.var()
modelo_multi = LinearRegression().fit(variables, y)
print(f"Correcto: efecto del festivo ≈ {efecto_festivo:+.2f} puntos · R² = {r2:.3f}")
```

**Tiene que salir:**

```text
Correcto: efecto del festivo ≈ +8.82 puntos · R² = 0.591
```

---

## S05_04 · Estadística con Python (1): descriptiva, distribuciones, Monte Carlo e intervalos de confianza

### Ejercicio 1 · Resumen de la ocupación

> Con la variable `serie` (ocupación diaria), guarda en `resumen` un diccionario con cuatro claves, todas redondeadas a 2 decimales: `"media"`, `"mediana"`, `"desviacion"` y `"iqr"` (rango intercuartílico: percentil 75 menos percentil 25 con `quantile`).

```python
serie = ocupacion_df["ocupacion_pct"]      # la serie de ocupación diaria
resumen = {
    "media": round(serie.mean(), 2),
    "mediana": round(serie.median(), 2),
    "desviacion": round(serie.std(), 2),
    "iqr": round(serie.quantile(0.75) - serie.quantile(0.25), 2),
}
print("Correcto:", resumen)
```

**Tiene que salir:**

```text
Correcto: {'media': np.float64(68.49), 'mediana': np.float64(67.7), 'desviacion': np.float64(9.61), 'iqr': np.float64(13.6)}
```

### Ejercicio 2 · Por meses

> Con `groupby("mes")`, calcula `media_por_mes` (media de ocupación de cada mes) y guarda en `mes_max` el mes de mayor ocupación media y en `mes_min` el de menor. Después se dibuja un diagrama de cajas por mes.

```python
media_por_mes = ocupacion_df.groupby("mes")["ocupacion_pct"].mean()
mes_max = int(media_por_mes.idxmax())
mes_min = int(media_por_mes.idxmin())

ocupacion_df.boxplot(column="ocupacion_pct", by="mes", figsize=(9, 3.8))
plt.suptitle("")
plt.title("Ocupación diaria por mes (2023-2025)")
plt.xlabel("Mes")
plt.ylabel("Ocupación (%)")
plt.tight_layout()
plt.show()
print(f"Correcto: mayor ocupación en el mes {mes_max} ({media_por_mes[mes_max]:.1f} %), menor en el mes {mes_min} ({media_por_mes[mes_min]:.1f} %)")
```

**Tiene que salir:**

```text
Correcto: mayor ocupación en el mes 1 (78.8 %), menor en el mes 9 (60.1 %)
```

### Ejercicio 3 · Probabilidad con la binomial

> Un día llegan 20 reservas y cada una se cancela con probabilidad `p_cancelacion = 0.459` (la tasa global de TurisData). Guarda en `p_10_o_mas` la probabilidad de que se cancelen **10 o más**. Pista: `stats.binom.sf(k, n, p)` da P(X > k), así que P(X ≥ 10) = `sf(9, ...)`.

```python
p_cancelacion = 0.459
p_10_o_mas = stats.binom.sf(9, 20, p_cancelacion)
print(f"Correcto: hay un {100 * p_10_o_mas:.1f} % de probabilidad de que se cancelen 10 o más de 20")
```

**Tiene que salir:**

```text
Correcto: hay un 44.1 % de probabilidad de que se cancelen 10 o más de 20
```

### Ejercicio 4 · Simular 10.000 días

> Repite la simulación **10.000 veces** (sin bucles: `rng.random((10000, 170)) < p_presentarse`) y guarda en `prob_reubicar` la proporción de simulaciones con **más de 100 presentados**. Compara con el valor exacto de la binomial (`stats.binom.sf(100, 170, p_presentarse)`).

```python
rng = np.random.default_rng(SEMILLA)
presentados = (rng.random((10000, 170)) < p_presentarse).sum(axis=1)
prob_reubicar = (presentados > 100).mean()
exacta = stats.binom.sf(100, 170, p_presentarse)
print(f"Correcto: Monte Carlo = {prob_reubicar:.3f} · exacto = {exacta:.3f}")
```

**Tiene que salir:**

```text
Correcto: Monte Carlo = 0.093 · exacto = 0.094
```

### Ejercicio 5 · IC de una proporción

> La **tasa de cancelación** de las 6.000 reservas es una proporción. Su IC aproximado del 95 % es `p ± 1.96 · √(p (1 − p) / n)`. Calcula `p_hat`, `n_res` y `ic_tasa` (tupla `(inferior, superior)`, redondeada a 4 decimales).

```python
p_hat = reservas["cancelada"].mean()
n_res = len(reservas)
margen = 1.96 * np.sqrt(p_hat * (1 - p_hat) / n_res)
ic_tasa = (round(p_hat - margen, 4), round(p_hat + margen, 4))
print(f"Correcto: tasa de cancelación {100 * p_hat:.1f} % (IC 95 %: {100 * ic_tasa[0]:.1f} % a {100 * ic_tasa[1]:.1f} %)")
```

**Tiene que salir:**

```text
Correcto: tasa de cancelación 45.9 % (IC 95 %: 44.6 % a 47.2 %)
```

### 5 · Mini-reto integrador: ¿enero y septiembre son realmente distintos?

> Calcula el IC del 95 % de la ocupación media de **enero** (`ic_ene`) y de **septiembre** (`ic_sep`) con `stats.t.interval` (cada uno con los datos de ese mes, tupla de 2 valores). Guarda en `se_solapan` un booleano: ¿se solapan los dos intervalos? Interpreta el resultado.

```python
def ic_mes(mes):
    x = ocupacion_df.loc[ocupacion_df["mes"] == mes, "ocupacion_pct"]
    return stats.t.interval(0.95, len(x) - 1, loc=x.mean(), scale=stats.sem(x))

ic_ene, ic_sep = ic_mes(1), ic_mes(9)
se_solapan = bool(ic_ene[0] <= ic_sep[1] and ic_sep[0] <= ic_ene[1])
print(f"Correcto. Enero: ({ic_ene[0]:.1f}, {ic_ene[1]:.1f}) · Septiembre: ({ic_sep[0]:.1f}, {ic_sep[1]:.1f}) → no se solapan: la diferencia no parece casualidad.")
```

**Tiene que salir:**

```text
Correcto. Enero: (77.5, 80.2) · Septiembre: (58.9, 61.3) → no se solapan: la diferencia no parece casualidad.
```

---

## S05_05 · Estadística con Python (2): contrastes de hipótesis, correlación y causalidad

### Ejercicio 1 · t de Student

> Con `stats.ttest_ind(a, b, equal_var=False)` guarda en `p_festivo` el p-valor de comparar festivos y normales, en `dif_medias` la diferencia de medias (festivos − normales, en puntos) y en `rechazar_h0` si se rechaza H0 con α = 0,05.

```python
resultado = stats.ttest_ind(festivos, normales, equal_var=False)
p_festivo = resultado.pvalue
dif_medias = festivos.mean() - normales.mean()
rechazar_h0 = bool(p_festivo < 0.05)
print(f"Correcto: diferencia = {dif_medias:.1f} puntos, p = {p_festivo:.2g} → rechazamos H0")
```

**Tiene que salir:**

```text
Correcto: diferencia = 16.3 puntos, p = 1.1e-30 → rechazamos H0
```

### Ejercicio 2 · Tamaño del efecto (d de Cohen)

> Un p-valor pequeño dice que la diferencia **no parece casualidad**, no que sea **grande**. El **d de Cohen** mide la diferencia en desviaciones típicas: `d = (media_a − media_b) / desviación_combinada`, con `desviación_combinada = √(((n_a−1)·var_a + (n_b−1)·var_b) / (n_a + n_b − 2))`. (Regla orientativa: 0,2 pequeño, 0,5 medio, 0,8 grande.) Guarda `d_cohen` (número).

```python
n_a, n_b = len(festivos), len(normales)
desv_comb = np.sqrt(((n_a - 1) * festivos.var() + (n_b - 1) * normales.var()) / (n_a + n_b - 2))
d_cohen = (festivos.mean() - normales.mean()) / desv_comb
print(f"Correcto: d = {d_cohen:.2f} → un festivo cambia la ocupación en casi 2 desviaciones típicas")
```

**Tiene que salir:**

```text
Correcto: d = 1.84 → un festivo cambia la ocupación en casi 2 desviaciones típicas
```

### Ejercicio 3 · Chi-cuadrado

> Guarda en `p_canal` el p-valor de `chi2_contingency(tabla_canal)` (es el segundo valor que devuelve) y en `canal_depende` si se rechaza la independencia con α = 0,05.

```python
chi2, p_canal, gl, esperados = stats.chi2_contingency(tabla_canal)
canal_depende = bool(p_canal < 0.05)
print(f"Correcto: chi² = {chi2:.1f}, gl = {gl}, p = {p_canal:.2g}")
```

**Tiene que salir:**

```text
Correcto: chi² = 203.2, gl = 3, p = 8.4e-44
```

### Ejercicio 4 · Matriz de correlaciones

> Calcula `matriz_corr`: la matriz de correlaciones (`DataFrame.corr()`) de las columnas `ocupacion_pct`, `temperatura_c`, `festivo` y `precio_medio`. Guarda en `r_temp` la correlación de la ocupación con la temperatura (redondeada a 2 decimales).

```python
matriz_corr = diaria[["ocupacion_pct", "temperatura_c", "festivo", "precio_medio"]].corr()
r_temp = round(matriz_corr.loc["ocupacion_pct", "temperatura_c"], 2)
print(matriz_corr.round(2))
```

**Tiene que salir:**

```text
               ocupacion_pct  temperatura_c  festivo  precio_medio
ocupacion_pct           1.00          -0.63     0.39          0.60
temperatura_c          -0.63           1.00    -0.22         -0.37
festivo                 0.39          -0.22     1.00          0.21
precio_medio            0.60          -0.37     0.21          1.00
```

### Ejercicio 5 · Controlar la confusión

> Ajusta `modelo_control` con la fórmula `"ocupacion_pct ~ temperatura_c + festivo + C(mes)"`. Guarda en `coef_temp_simple` el coeficiente de la temperatura del modelo simple, en `coef_temp_control` el del modelo con control y en `p_temp_control` su p-valor. Después mira qué ha pasado con el efecto de la temperatura.

```python
modelo_control = smf.ols("ocupacion_pct ~ temperatura_c + festivo + C(mes)", data=diaria).fit()
coef_temp_simple = modelo_simple.params["temperatura_c"]
coef_temp_control = modelo_control.params["temperatura_c"]
p_temp_control = modelo_control.pvalues["temperatura_c"]
print(f"Correcto: sin control, {coef_temp_simple:.2f} puntos por °C; controlando el mes, {coef_temp_control:.2f} (p = {p_temp_control:.2f}).")
print("El efecto del festivo se mantiene:", round(modelo_control.params["festivo"], 1), "puntos, p =", f"{modelo_control.pvalues['festivo']:.1g}")
```

**Tiene que salir:**

```text
Correcto: sin control, -1.86 puntos por °C; controlando el mes, -0.09 (p = 0.48).
El efecto del festivo se mantiene: 9.1 puntos, p = 3e-23
```

### Ejercicio 6 · ¿Qué probabilidad hay de que la web tenga más cancelaciones?

> Guarda en `prob_web_mayor` la proporción de muestras en las que `post_web` es **mayor** que `post_directo` (comparación elemento a elemento y `.mean()`).

```python
prob_web_mayor = (post_web > post_directo).mean()
print(f"Correcto: P(web cancela más que directo) ≈ {prob_web_mayor:.3f}")
```

**Tiene que salir:**

```text
Correcto: P(web cancela más que directo) ≈ 1.000
```

### 6 · Mini-reto integrador: ¿ocupación de invierno frente a verano?

> Compara la ocupación de **invierno** (meses 12, 1, 2) con la de **verano** (6, 7, 8): guarda en `dif_estaciones` la diferencia de medias (invierno − verano), en `ic_dif` el **intervalo de confianza del 95 %** de esa diferencia (`resultado.confidence_interval()` del t-test de Welch, tupla `(low, high)`) y en `pregunta_causal` una cadena con tu respuesta a: "¿podemos afirmar que el frío *provoca* más ocupación?" (`"si"` o `"no"`, y razona en una celda de texto).

```python
invierno = diaria.loc[diaria["mes"].isin([12, 1, 2]), "ocupacion_pct"]
verano = diaria.loc[diaria["mes"].isin([6, 7, 8]), "ocupacion_pct"]
res = stats.ttest_ind(invierno, verano, equal_var=False)
dif_estaciones = invierno.mean() - verano.mean()
ic_dif = (res.confidence_interval().low, res.confidence_interval().high)
pregunta_causal = "no"     # la estación es un paquete de factores (turismo europeo, festivos, precios...), no solo el frío
print(f"Correcto: invierno − verano = {dif_estaciones:.1f} puntos (IC 95 %: {ic_dif[0]:.1f} a {ic_dif[1]:.1f}).")
```

**Tiene que salir:**

```text
Correcto: invierno − verano = 16.4 puntos (IC 95 %: 15.3 a 17.5).
```

---

## S05_06 · CRUD desde Python: `sqlite3` y `pymongo` / `mongomock`

### Ejercicio 1 · Leer con pandas

> Guarda en `n_reservas` el número de reservas (con `fetchone()[0]`) y en `tasa_por_isla` un DataFrame con dos columnas, `isla` y `pct_cancelacion` (tasa de cancelación en % con 1 decimal), calculado con una consulta SQL con `JOIN` y `GROUP BY` (como en el Sprint 3) y `pd.read_sql_query`. Ordénalo por isla.

```python
n_reservas = con.execute("SELECT COUNT(*) FROM reservas").fetchone()[0]
tasa_por_isla = pd.read_sql_query("""
    SELECT a.isla AS isla, ROUND(100.0 * AVG(r.cancelada), 1) AS pct_cancelacion
    FROM reservas r JOIN alojamientos a ON a.id_alojamiento = r.id_alojamiento
    GROUP BY a.isla ORDER BY a.isla
""", con)
print("Correcto")
print(tasa_por_isla)
```

**Tiene que salir:**

```text
Correcto
            isla  pct_cancelacion
0  Fuerteventura             45.6
1   Gran Canaria             46.5
2      La Gomera             46.7
3       La Palma             46.0
4      Lanzarote             45.3
5       Tenerife             46.0
```

### Ejercicio 2 · Función de consulta parametrizada

> Escribe `reservas_de_cliente(con, id_cliente)` que devuelva la **lista de `id_reserva`** (enteros, ordenados) de ese cliente, usando un marcador `?`.

```python
def reservas_de_cliente(con, id_cliente):
    """Devuelve la lista ordenada de id_reserva del cliente."""
    filas = con.execute("SELECT id_reserva FROM reservas WHERE id_cliente = ? ORDER BY id_reserva", (id_cliente,)).fetchall()
    return [f[0] for f in filas]
print("Correcto")
```

**Tiene que salir:**

```text
Correcto
```

### Ejercicio 3 · Poblar la base con la serie diaria

> Lee `ocupacion_diaria.csv` con pandas (guárdalo en `diaria`; la fecha como texto) y **cárgalo en una tabla nueva `ocupacion_diaria`** de la base con `to_sql` (reemplazando si existe). Después guarda en `n_dias` el número de filas de esa tabla leído **desde la base**.

```python
diaria = pd.read_csv(dato("ocupacion_diaria.csv"))
diaria.to_sql("ocupacion_diaria", con, if_exists="replace", index=False)
con.commit()
n_dias = con.execute("SELECT COUNT(*) FROM ocupacion_diaria").fetchone()[0]
columnas = [c[1] for c in con.execute("PRAGMA table_info(ocupacion_diaria)").fetchall()]
print("Correcto: la base ya contiene la serie diaria")
```

**Tiene que salir:**

```text
Correcto: la base ya contiene la serie diaria
```

### Ejercicio 4 · Actualizar y probar un `rollback`

> 1. Marca como cancelada (`cancelada = 1`) la reserva `5046` con un `UPDATE` con parámetro y guarda en    `filas_actualizadas` el `rowcount`. Confirma con `commit`. 2. Borra **todas las reservas de 12 noches o más** *dentro de una transacción*, guarda en `borradas` cuántas has borrado y    luego **deshaz** con `rollback`. Guarda en `total_tras_rollback` el número de reservas que quedan (debe seguir siendo 6000).

```python
cur = con.execute("UPDATE reservas SET cancelada = 1 WHERE id_reserva = ?", (5046,))
filas_actualizadas = cur.rowcount
con.commit()

cur = con.execute("DELETE FROM reservas WHERE noches >= 12")
borradas = cur.rowcount
con.rollback()
total_tras_rollback = con.execute("SELECT COUNT(*) FROM reservas").fetchone()[0]
print(f"Correcto: se habrían borrado {borradas} reservas, pero el rollback las devolvió (quedan {total_tras_rollback})")
```

**Tiene que salir:**

```text
Correcto: se habrían borrado 45 reservas, pero el rollback las devolvió (quedan 6000)
```

### Ejercicio 5 · Ocupación media por mes desde la base

> Con una consulta sobre la tabla `ocupacion_diaria` (`SUBSTR(fecha, 6, 2)` da el mes, como texto `'01'`...`'12'`), crea `ocupacion_mes`: DataFrame con columnas `mes` y `media` (media redondeada a 2 decimales), ordenado por mes.

```python
ocupacion_mes = pd.read_sql_query("""
    SELECT SUBSTR(fecha, 6, 2) AS mes, ROUND(AVG(ocupacion_pct), 2) AS media
    FROM ocupacion_diaria GROUP BY mes ORDER BY mes
""", con)
print("Correcto")
print(ocupacion_mes.T)
```

**Tiene que salir:**

```text
Correcto
          0      1      2      3      4      5      6      7      8      9   \
mes       01     02     03     04     05     06     07     08     09     10   
media  78.83  77.58  74.52  70.08  62.65  60.78  62.96  62.13  60.06  63.31   

          10     11  
mes       11     12  
media  70.78  78.58
```

### Ejercicio 6 · CRUD en MongoDB

> Sobre `coleccion` (200 documentos): 1. **Crear:** inserta un documento `{"_id": 900001, "canal": "directo", "noches": 3, "precio_noche": 99.0, "cancelada": 0}`. 2. **Actualizar:** pon `precio_noche` en `105.0` a ese documento con `$set`. 3. **Leer:** guarda en `precio_leido` su precio leyéndolo de la colección. 4. **Borrar:** elimina todos los documentos con `cancelada` igual a 1 y guarda en `n_borrados` el número (`deleted_count`). 5. Guarda en `n_final` los documentos que quedan.

```python
coleccion.insert_one({"_id": 900001, "canal": "directo", "noches": 3, "precio_noche": 99.0, "cancelada": 0})
coleccion.update_one({"_id": 900001}, {"$set": {"precio_noche": 105.0}})
precio_leido = coleccion.find_one({"_id": 900001})["precio_noche"]
n_borrados = coleccion.delete_many({"cancelada": 1}).deleted_count
n_final = coleccion.count_documents({})
print(f"Correcto: {n_borrados} borrados, quedan {n_final}")
```

**Tiene que salir:**

```text
Correcto: 97 borrados, quedan 104
```

### 7 · Mini-reto integrador: «reservas por canal» desde SQL y desde MongoDB

> Escribe una función `contar_por_canal_sql(ruta_bd)` que devuelva un diccionario `{canal: nº de reservas}` **leyendo la base SQLite** (`sqlite3` + `GROUP BY`). Comprueba que coincide con el resultado de un `count_documents` por canal sobre una colección de MongoDB cargada con **todas** las reservas. Guarda ambos resultados en `por_canal_sql` y `por_canal_mongo`.

```python
def contar_por_canal_sql(ruta):
    """{canal: número de reservas} leído de SQLite."""
    with sqlite3.connect(ruta) as conexion:
        return dict(conexion.execute("SELECT canal, COUNT(*) FROM reservas GROUP BY canal").fetchall())

por_canal_sql = contar_por_canal_sql(ruta_bd)

conexion = sqlite3.connect(ruta_bd)
conexion.row_factory = sqlite3.Row
todas = [dict(f) for f in conexion.execute("SELECT id_reserva AS _id, canal FROM reservas")]
conexion.close()
todas_coleccion = mongomock.MongoClient()["turisdata"]["todas"]
todas_coleccion.insert_many(todas)
por_canal_mongo = {c: todas_coleccion.count_documents({"canal": c}) for c in por_canal_sql}
print("Correcto:", por_canal_sql)
```

**Tiene que salir:**

```text
Correcto: {'agencia': 1190, 'directo': 1462, 'empresa': 328, 'web_intermediaria': 3020}
```
