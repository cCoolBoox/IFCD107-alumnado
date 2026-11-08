# Solucionario · cuadernos completos («para casa») del Sprint 9

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S09_01` a `S09_04`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Las soluciones de los cuadernos «en clase» están en [`../en_clase/Solucionario_en_clase.md`](../en_clase/Solucionario_en_clase.md).
- Los **mini-retos abiertos** (sin una única respuesta correcta) no llevan solución aquí: se contrastan con el razonamiento y con las cifras del propio cuaderno.

---

## S09_01 · Segmentar huéspedes con clustering

### A5 · EJERCICIO 1 de 5 — La matriz X estandarizada

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

### A7 · EJERCICIO 2 de 5 — ¿Cuántos grupos? La silueta de cada k

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

### A11 · EJERCICIO 3 de 5 — Familias y aventureros

> Guarda en `grupo_familias` el número del grupo con **mayor proporción de huéspedes que
> viajan con niños** (media de `viaja_con_ninos` por grupo) y en `grupo_aventura` el
> número del grupo con **mayor `pct_gasto_actividades`** medio.

```python
grupo_familias = huespedes.groupby("grupo")["viaja_con_ninos"].mean().idxmax()
grupo_aventura = huespedes.groupby("grupo")["pct_gasto_actividades"].mean().idxmax()

print("Ejercicio 3 correcto ✔")
```

**Tiene que salir:**

```text
Ejercicio 3 correcto ✔
```

### A13 · EJERCICIO 4 de 5 — Clustering jerárquico con 4 grupos

> Aplica `AgglomerativeClustering` con `n_clusters=4` y `linkage="ward"` sobre **todos** los
> huéspedes (`X`). Guarda las etiquetas en `etiquetas_jer` y su silueta en `silueta_jer`.

```python
etiquetas_jer = AgglomerativeClustering(n_clusters=4, linkage="ward").fit_predict(X)
silueta_jer = silhouette_score(X, etiquetas_jer)

print(f"Silueta jerárquico = {silueta_jer:.3f} · k-means con k={k_mejor}: {siluetas[k_mejor]:.3f}")
```

**Tiene que salir:**

```text
Silueta jerárquico = 0.424 · k-means con k=4: 0.431
```

### A15 · EJERCICIO 5 de 5 — DBSCAN con eps = 1,0

> Entrena DBSCAN con `eps=1.0` y `min_samples=10`. Guarda las etiquetas en `etiquetas_db`,
> el número de grupos encontrados (sin contar el ruido) en `n_grupos_db` y cuántos huéspedes
> quedan como ruido en `n_ruido`.

```python
etiquetas_db = DBSCAN(eps=1.0, min_samples=10).fit_predict(X)
n_grupos_db = len(set(etiquetas_db)) - (1 if -1 in etiquetas_db else 0)
n_ruido = int((etiquetas_db == -1).sum())

print(f"DBSCAN: {n_grupos_db} grupos y {n_ruido} huéspedes atípicos")
```

**Tiene que salir:**

```text
DBSCAN: 5 grupos y 149 huéspedes atípicos
```

### A16 · MINI-RETO — Ponle nombre a tus segmentos

> 1. Elige el método que te parezca mejor (k-means, jerárquico o DBSCAN) y justifícalo en una frase.
> 2. Para cada grupo, escribe **un nombre**, **una descripción de una línea** y **una acción comercial**.
> 3. Guarda los nombres en el diccionario `nombres_segmentos` (clave = número de grupo de k-means).
> *Ejemplo:* `{0: "Familias de verano"}`. Este trabajo alimenta el reto "Conocer al huésped".

```python
nombres_segmentos = {}   # rellena: {0: "...", 1: "...", ...}
nombres_segmentos = {}
for g in range(k_mejor):
    fila = perfil_z.iloc[g]
    if fila["viaja_con_ninos"] > 0.8:
        nombres_segmentos[g] = "Familias"
    elif fila["pct_gasto_actividades"] > 0.8:
        nombres_segmentos[g] = "Aventureros"
    elif fila["edad"] > 0.5:
        nombres_segmentos[g] = "Descanso premium"
    else:
        nombres_segmentos[g] = "Escapadas cortas"

print(nombres_segmentos)
```

**Tiene que salir:**

```text
{0: 'Escapadas cortas', 1: 'Familias', 2: 'Descanso premium', 3: 'Aventureros'}
```

---

## S09_02 · Reducir dimensiones con PCA

### A3 · EJERCICIO 1 de 4 — La varianza acumulada y el 90 %

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

### A6 · EJERCICIO 2 de 4 — El mapa de huéspedes en 2D

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

### A9 · EJERCICIO 3 de 4 — Las variables opuestas a la edad

> Guarda en `opuestas_a_edad` la lista de variables cuya carga en `PC1` tiene **signo contrario** a la
> de `edad` (es decir, cuando la edad sube en el componente 1, ellas bajan). Usa el DataFrame `cargas`.

```python
signo_edad = np.sign(cargas.loc["edad", "PC1"])
opuestas_a_edad = [v for v in cargas.index if np.sign(cargas.loc[v, "PC1"]) != signo_edad]

print("Ejercicio 3 correcto ✔ — el componente 1 opone «mayor, planificador, estancias largas» a «activo y viajero frecuente»")
```

**Tiene que salir:**

```text
Ejercicio 3 correcto ✔ — el componente 1 opone «mayor, planificador, estancias largas» a «activo y viajero frecuente»
```

### A11 · EJERCICIO 4 de 4 — Agrupar con el 90 % de la varianza

> Entrena `PCA(n_components=n_comp_90)` sobre `X`, guarda el resultado en `Z90` y agrupa `Z90` con
> k-means (`k=4`, `n_init=10`, `random_state=SEMILLA`). Guarda las etiquetas en `grupo_pca90` y
> calcula en `ari_pca90` su coincidencia (ARI) con `grupo`.

```python
Z90 = PCA(n_components=n_comp_90, random_state=SEMILLA).fit_transform(X)
grupo_pca90 = KMeans(n_clusters=4, n_init=10, random_state=SEMILLA).fit_predict(Z90)
ari_pca90 = adjusted_rand_score(grupo, grupo_pca90)

print(f"Ejercicio 4 correcto ✔ — ARI = {ari_pca90:.2f}")
```

**Tiene que salir:**

```text
Ejercicio 4 correcto ✔ — ARI = 1.00
```

---

## S09_03 · Recomendar experiencias a los huéspedes

### A5 · EJERCICIO 1 de 5 — Popularidad: la media de cada experiencia

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

### A7 · EJERCICIO 2 de 5 — La función precision@k

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

### A9 · EJERCICIO 3 de 5 — El perfil de gustos de cada usuario

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

### A11 · EJERCICIO 4 de 5 — Experiencias parecidas al Teide

> Calcula `S`, la matriz 25 × 25 de similitud coseno entre experiencias a partir de las **columnas de `C`**
> (`cosine_similarity(C.T)` ya está importado). Pon la diagonal a 0 (una experiencia no se ayuda a sí misma)
> con `np.fill_diagonal`. Después guarda en `similares_teide` los **nombres** de las 3 experiencias más
> parecidas al *Ascenso al Teide* (id 1, columna 0).

```python
S = cosine_similarity(C.T)
np.fill_diagonal(S, 0)
ids_similares = np.argsort(-S[0])[:3] + 1
similares_teide = experiencias.set_index("id_experiencia").loc[ids_similares, "nombre"].tolist()

print("Ejercicio 4 correcto ✔ — parecidas al Teide:", similares_teide)

# Predicción item-item: nota media + media ponderada de los residuos del usuario en experiencias parecidas
P_item = media_item_v[None, :] + (C @ S.T) / (M.astype(float) @ np.abs(S).T + 1e-9)

# Predicción user-user: lo mismo mirando usuarios parecidos
Su = cosine_similarity(C)
np.fill_diagonal(Su, 0)
P_user = media_item_v[None, :] + (Su @ C) / (np.abs(Su) @ M.astype(float) + 1e-9)

for nombre, P in (("item-item", P_item), ("user-user", P_user)):
    print(f"{nombre}: RMSE = {evaluar_rmse(P):.3f} · precision@3 = {precision_k(P):.3f}")
```

**Tiene que salir:**

```text
Ejercicio 4 correcto ✔ — parecidas al Teide: ['Paseo a caballo', 'Spa y termas', 'Parque acuático']
item-item: RMSE = 0.895 · precision@3 = 0.171
user-user: RMSE = 0.865 · precision@3 = 0.148
```

### A14 · EJERCICIO 5 de 5 — La factorización y la tabla comparativa

> Guarda en `P_mf` la matriz de `factorizar(R, k=3)` y calcula `rmse_mf` y `p_mf` (precision@3).
> Después, en `mejor_rmse`, el nombre del método con menor RMSE de entre los que hay en el diccionario
> `metodos` (que ya está preparado).

```python
P_mf = factorizar(R, k=3)
rmse_mf = evaluar_rmse(P_mf)
p_mf = precision_k(P_mf)

metodos = {"Popularidad": P_pop, "Contenido": P_cont, "Item-item": P_item, "User-user": P_user, "Factorización": P_mf}
tabla = pd.DataFrame({
    "RMSE": {n: evaluar_rmse(P) for n, P in metodos.items()},
    "precision@3": {n: precision_k(P) for n, P in metodos.items()},
}).round(3)
mejor_rmse = tabla["RMSE"].idxmin()
print("Ejercicio 5 correcto ✔")
tabla

fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))
tabla["RMSE"].plot.barh(ax=ax[0], color="tab:blue"); ax[0].set_title("Error de la nota (RMSE) — menos es mejor"); ax[0].set_xlabel("estrellas")
tabla["precision@3"].plot.barh(ax=ax[1], color="tab:green"); ax[1].set_title("precision@3 — más es mejor"); ax[1].set_xlabel("proporción de aciertos")
plt.tight_layout(); plt.show()
```

**Tiene que salir:**

```text
Ejercicio 5 correcto ✔
```

Y además dibuja un gráfico.

### A16 · MINI-RETO — La función recomendar

> Escribe `recomendar(id_usuario, n=3, P=P_mf)` que devuelva un `DataFrame` con las `n` experiencias
> **que el usuario aún no ha valorado** con mayor puntuación prevista, con las columnas `nombre`,
> `categoria`, `isla` y `nota_prevista`. Prueba con los usuarios 1 y 2 y comprueba que las
> recomendaciones son distintas. Los `id_usuario` van de 1 al número de usuarios (`len(M)`): ante cualquier otro
> valor (por ejemplo 0, que en Python apuntaría al último usuario) la función debe lanzar un `ValueError`.
> **Para el reto del sprint:** el segundo método que se compara con la popularidad es **item-item**, así que allí
> llamad a `recomendar(..., P=P_item)` (el valor por defecto `P_mf` es solo el de este cuaderno).

```python
def recomendar(id_usuario, n=3, P=P_mf):
    if not 1 <= id_usuario <= len(M):
        raise ValueError(f"id_usuario debe estar entre 1 y {len(M)}")
    puntuacion = P[id_usuario - 1].astype(float).copy()
    puntuacion[M[id_usuario - 1]] = -np.inf
    ids = np.argsort(-puntuacion)[:n] + 1
    res = experiencias.set_index("id_experiencia").loc[ids, ["nombre", "categoria", "isla"]].copy()
    res["nota_prevista"] = np.clip(P[id_usuario - 1][ids - 1], 1, 5).round(2)
    return res

r1, r2 = recomendar(1), recomendar(2)
vistas_1 = set(np.where(M[0])[0] + 1)
try:
    recomendar(0)
    raise AssertionError("recomendar(0) debería lanzar ValueError: los usuarios empiezan en 1")
except ValueError:
    pass
print("Usuario 1:"); display(r1)
print("Usuario 2:"); display(r2)
```

**Tiene que salir:**

```text
Usuario 1:
Usuario 2:
```

---

## S09_04 · Aprendizaje por refuerzo: Q-learning en el hotel

### A3 · EJERCICIO 1 de 4 — La regla de actualización de Q

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

### A4 · EJERCICIO 2 de 4 — La función epsilon-greedy

> Escribe `elegir_accion(Q, s, epsilon, rng)`: con probabilidad `epsilon` devuelve una acción aleatoria
> (`rng.integers(4)`), y si no, la de mayor valor en `Q[s]` (`np.argmax`). Usa `rng.random()` para decidir.

```python
def elegir_accion(Q, s, epsilon, rng):
    if rng.random() < epsilon:
        return int(rng.integers(Q.shape[1]))
    return int(np.argmax(Q[s]))

rng_t = np.random.default_rng(0)
Qt = np.zeros((20, 4)); Qt[7] = [0, 0, 5, 0]
distintas = {elegir_accion(Qt, 7, 1.0, rng_t) for _ in range(200)}
print("Ejercicio 2 correcto ✔")
```

**Tiene que salir:**

```text
Ejercicio 2 correcto ✔
```

### A7 · EJERCICIO 3 de 4 — La política y el camino aprendido

> Guarda en `politica` un vector de 20 acciones (la mejor en cada estado). Después escribe el `camino`
> que sigue el agente **sin explorar** desde recepción: lista de estados visitados, empezando en 0, hasta
> llegar a la meta (estado 19) o hasta un máximo de 30 pasos. Usa `EntornoHotel` y `politica`.

```python
politica = np.argmax(Q, axis=1)
entorno = EntornoHotel()
s = entorno.reset()
camino = [s]
for _ in range(30):
    s, _, fin = entorno.step(politica[s])
    camino.append(s)
    if fin:
        break

print(f"Ejercicio 3 correcto ✔ — camino de {len(camino) - 1} pasos:", camino)

# Dibujo de la política: flechas sobre la cuadrícula
flechas = {0: "↑", 1: "↓", 2: "←", 3: "→"}
mapa = np.full((4, 5), "", dtype=object)
fig, ax = plt.subplots(figsize=(6, 4.5))
valores = Q.max(axis=1).reshape(4, 5)
sns.heatmap(valores, annot=False, cmap="YlGn", cbar_kws={"label": "valor del estado (max Q)"}, ax=ax, linewidths=1, linecolor="white")
for f in range(4):
    for c in range(5):
        if (f, c) in EntornoHotel.PAREDES:
            texto = "PARED"
        elif (f, c) == EntornoHotel.META:
            texto = "META"
        else:
            texto = flechas[politica[f * 5 + c]] + ("\nOBRAS" if (f, c) == EntornoHotel.OBRAS else "")
        ax.text(c + 0.5, f + 0.5, texto, ha="center", va="center", fontsize=13)
ax.set_title("Política aprendida y valor de cada casilla"); ax.set_xticks([]); ax.set_yticks([])
plt.show()
```

**Tiene que salir:**

```text
Ejercicio 3 correcto ✔ — camino de 7 pasos: [0, 1, 2, 3, 8, 13, 14, 19]
```

Y además dibuja un gráfico.

### A9 · EJERCICIO 4 de 4 — Con pasos gratis, ¿ayuda explorar?

> Entrena dos agentes con `entrenar(..., coste_paso=0.0)`: uno con `epsilon=0.0` (nunca explora) y otro con
> `epsilon=0.3`. Guarda sus recompensas por episodio en `rec_eps0` y `rec_eps03`. Calcula `media_final_eps0`
> y `media_final_eps03` como la media de sus **últimos 100 episodios** y guarda en `explorar_ayuda`
> (`True`/`False`) si el agente que explora consigue mayor recompensa media final que el que no.

```python
_, rec_eps0 = entrenar(epsilon=0.0, coste_paso=0.0)
_, rec_eps03 = entrenar(epsilon=0.3, coste_paso=0.0)
media_final_eps0 = rec_eps0[-100:].mean()
media_final_eps03 = rec_eps03[-100:].mean()
explorar_ayuda = bool(media_final_eps03 > media_final_eps0)

print(f"Sin explorar: {media_final_eps0:.1f} · Explorando (0,3): {media_final_eps03:.1f}")
_, rec_gamma0 = entrenar(gamma=0.0)
print("Con gamma=0 (sin mirar al futuro), recompensa final:", rec_gamma0[-100:].mean().round(1), "(compárala con el +3 óptimo)")
```

**Tiene que salir:**

```text
Sin explorar: 0.0 · Explorando (0,3): 9.1
Con gamma=0 (sin mirar al futuro), recompensa final: -49.5 (compárala con el +3 óptimo)
```

