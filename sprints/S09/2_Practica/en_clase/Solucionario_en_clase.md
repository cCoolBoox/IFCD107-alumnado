# Solucionario · cuadernos «en clase» del Sprint 9

- Las soluciones de los ejercicios de los cuadernos «en clase» (`S09_01`, `S09_02`, `S09_03`, `S09_04`), con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Son las mismas soluciones que llevan los cuadernos completos en «🆘 Solución de referencia».
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos completos («para casa») están en [`../para_casa/Solucionario_para_casa.md`](../para_casa/Solucionario_para_casa.md).

---

## S09_01 · Segmentar huéspedes con clustering

### Ejercicio 1 · Escalar: que todas las variables "pesen" lo mismo

> Crea la matriz `X` con **todas las variables menos `id_huesped`**, estandarizadas con
> `StandardScaler` (usa `fit_transform`). `X` debe ser una matriz de 1200 filas y 7 columnas.
> Guarda también los nombres de las variables en la lista `variables`. Ojo: más abajo (apartado 3) se añade a la tabla la
> columna `grupo`; si repites esta celda después, **no la incluyas** en `variables` (o reinicia el cuaderno).

```python
variables = [c for c in huespedes.columns if c not in ("id_huesped", "grupo")]   # "grupo" aparece más abajo; así puedes repetir esta celda
X = StandardScaler().fit_transform(huespedes[variables])

print("Ejercicio 1 correcto ✔")
```

**Tiene que salir:**

```text
Ejercicio 1 correcto ✔
```

### Ejercicio 2 · k-means: agrupar alrededor de centros

> Calcula en el diccionario `siluetas` la silueta media (`silhouette_score(X, etiquetas)`)
> de k-means para cada `k` de 2 a 8 (clave = `k`, valor = silueta). Después guarda en
> `k_mejor` el `k` con silueta más alta. Usa `n_init=10` y `random_state=SEMILLA`.

```python
siluetas = {}
for k in range(2, 9):
    etiquetas = KMeans(n_clusters=k, n_init=10, random_state=SEMILLA).fit_predict(X)
    siluetas[k] = silhouette_score(X, etiquetas)
k_mejor = max(siluetas, key=siluetas.get)

print("k con mejor silueta:", k_mejor)

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(list(siluetas), list(siluetas.values()), marker="o")
ax.axvline(k_mejor, color="tab:red", linestyle="--", label=f"mejor k = {k_mejor}")
ax.set_xlabel("Número de grupos (k)")
ax.set_ylabel("Silueta media")
ax.set_title("¿Cuántos segmentos de huéspedes hay?")
ax.legend()
plt.show()
```

**Tiene que salir:**

```text
k con mejor silueta: 4
```

Y además dibuja un gráfico.

---

## S09_02 · Reducir dimensiones con PCA

### Ejercicio 1 · La idea de PCA

> Calcula en `varianza_acum` la varianza explicada **acumulada** (usa `np.cumsum` sobre `varianza`)
> y en `n_comp_90` el **número mínimo de componentes** que explican al menos el 90 % de la varianza.

```python
varianza_acum = np.cumsum(varianza)
n_comp_90 = int(np.argmax(varianza_acum >= 0.90)) + 1

print("Ejercicio 1 correcto ✔ — con", n_comp_90, "componentes conservamos el 90 % de la información")

fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))
ax[0].bar(range(1, 8), varianza)
ax[0].set_title("Varianza explicada por componente")
ax[0].set_xlabel("Componente"); ax[0].set_ylabel("Proporción")
ax[1].plot(range(1, 8), varianza_acum, marker="o")
ax[1].axhline(0.9, color="tab:red", linestyle="--", label="90 %")
ax[1].set_title("Varianza explicada acumulada")
ax[1].set_xlabel("Número de componentes"); ax[1].legend()
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Ejercicio 1 correcto ✔ — con 5 componentes conservamos el 90 % de la información
```

Y además dibuja un gráfico.

### Ejercicio 2 · Ver a los huéspedes en 2D

> Dibuja un diagrama de dispersión de `Z2` (columna 0 en el eje X, columna 1 en el eje Y) coloreando
> cada punto según la variable `grupo` (el segmento de k-means). Guarda la figura en `fig2d`.
> Pon título y nombres de ejes con el porcentaje de varianza de cada componente.

```python
fig2d, ax = plt.subplots(figsize=(7, 5))
sc = ax.scatter(Z2[:, 0], Z2[:, 1], c=grupo, cmap="tab10", s=12, alpha=0.7)
ax.set_xlabel(f"Componente 1 ({pca2.explained_variance_ratio_[0]:.0%})")
ax.set_ylabel(f"Componente 2 ({pca2.explained_variance_ratio_[1]:.0%})")
ax.set_title("Mapa de huéspedes (PCA) coloreado por segmento")
ax.legend(*sc.legend_elements(), title="Segmento")

plt.show()
```

**Tiene que salir:** un gráfico.

---

## S09_03 · Recomendar experiencias a los huéspedes

### Ejercicio 1 · Recomendador por popularidad

> Calcula en `media_item` la nota media de cada experiencia **solo con la matriz de entrenamiento `R`**
> (una `Series` de 25 valores). Después crea `P_pop`, una matriz de 300 × 25 en la que **todas las filas**
> son `media_item` (`np.tile`), y guarda su error en `rmse_pop` con `evaluar_rmse`.

```python
media_item = R.mean()
P_pop = np.tile(media_item.values, (300, 1))
rmse_pop = evaluar_rmse(P_pop)

print(f"Ejercicio 1 correcto ✔ — RMSE popularidad = {rmse_pop:.3f}")

top = media_item.sort_values(ascending=False).head(5)
print(experiencias.set_index("id_experiencia").loc[top.index, "nombre"].to_frame().assign(nota=top.round(2)))
```

**Tiene que salir:**

```text
Ejercicio 1 correcto ✔ — RMSE popularidad = 1.029
                                 nombre  nota
id_experiencia
11                     Parque Timanfaya  4.43
22                   Visita a Garachico  4.21
2               Observación de cetáceos  3.93
24                            Parapente  3.82
13               Astronomía en el Roque  3.77
```

### Ejercicio 2 · Métrica de ranking: precision@k

> Completa la función `precision_k(P, k=3)`. Para cada usuario de `relevantes`: (1) toma su fila de `P`,
> (2) pon `-inf` en las experiencias que ya valoró en entrenamiento (fila de `M`), (3) quédate con las
> `k` de mayor puntuación (`np.argsort`; suma 1 para pasar de posición a `id_experiencia`) y (4) calcula
> qué fracción de esas `k` están en sus experiencias relevantes. Devuelve la media de todos los usuarios.

```python
relevantes = prueba[prueba["valoracion"] >= 4]      # lo que "le gusta" a cada usuario
print("Usuarios evaluables:", relevantes["id_usuario"].nunique())

def precision_k(P, k=3):
    aciertos = []
    for u, g in relevantes.groupby("id_usuario"):
        puntuacion = P[u - 1].astype(float).copy()
        puntuacion[M[u - 1]] = -np.inf
        recomendadas = np.argsort(-puntuacion)[:k] + 1
        aciertos.append(len(set(recomendadas) & set(g["id_experiencia"])) / k)
    return float(np.mean(aciertos))

p_pop = precision_k(P_pop)
azar = precision_k(np.random.default_rng(SEMILLA).random((300, 25)))
print(f"Ejercicio 2 correcto ✔ — precision@3 popularidad = {p_pop:.3f} · azar = {azar:.3f}")
```

**Tiene que salir:**

```text
Usuarios evaluables: 115
Ejercicio 2 correcto ✔ — precision@3 popularidad = 0.125 · azar = 0.081
```

### Ejercicio 3 · Recomendador basado en contenido

> Calcula `perfil_usuario` (300 × 7): para cada usuario y categoría, la **suma de sus residuos en esa
> categoría dividida entre (número de valoraciones en esa categoría + 3)**. El "+3" es prudencia: con pocas
> valoraciones no nos fiamos. Pista: `C @ F` suma residuos por categoría y `M @ F` cuenta valoraciones
> (convierte `M` a `float`).

```python
perfil_usuario = (C @ F) / (M.astype(float) @ F + 3)

print("Ejercicio 3 correcto ✔")

# Predicción por contenido: nota media de la experiencia + afinidad del usuario con su categoría
P_cont = media_item_v[None, :] + perfil_usuario @ F.T
print("RMSE contenido:", round(evaluar_rmse(P_cont), 3), "· precision@3:", round(precision_k(P_cont), 3))
```

**Tiene que salir:**

```text
Ejercicio 3 correcto ✔
RMSE contenido: 1.066 · precision@3: 0.13
```

---

## S09_04 · Aprendizaje por refuerzo: Q-learning en el hotel

### Ejercicio 1 · La tabla Q y su regla de actualización

> Escribe `actualizar_q(Q, s, a, r, s2, alpha, gamma)` que aplique la regla **modificando `Q` en su sitio**
> (no hace falta devolver nada).

```python
def actualizar_q(Q, s, a, r, s2, alpha, gamma):
    objetivo = r + gamma * Q[s2].max()
    Q[s, a] += alpha * (objetivo - Q[s, a])

Qprueba = np.zeros((20, 4))
Qprueba[5, 3] = 4.0
actualizar_q(Qprueba, s=0, a=3, r=-1.0, s2=5, alpha=0.5, gamma=0.9)
print("Ejercicio 1 correcto ✔")
```

**Tiene que salir:**

```text
Ejercicio 1 correcto ✔
```

