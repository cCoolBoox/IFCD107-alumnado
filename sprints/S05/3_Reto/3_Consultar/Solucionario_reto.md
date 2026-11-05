# Solucionario del reto · Sprint 5 · «¿La ocupación depende de esto?»

> **Para contrastar y para entender**, no solo para copiar. Cada paso tiene el **mismo número** que su [página del reto](Reto_Sprint_05_paso_1.md): buscad el vuestro, comparad y, si algo no sale, mirad «Fallos habituales». Volver a la [ficha del reto](Reto_Sprint_05.md).

## Índice

- [Cómo usarlo](#cómo-usarlo): primero intentarlo, después contrastar
- [Las cifras que tienen que salir](#las-cifras-que-tienen-que-salir): la tabla para comprobar todo de un vistazo
- [Paso 1 · Cargar los datos en una base de datos](#paso-1--cargar-los-datos-en-una-base-de-datos)
- [Paso 2 · Mirar los datos](#paso-2--mirar-los-datos)
- [Paso 3 · Regresión lineal desde cero](#paso-3--regresión-lineal-desde-cero)
- [Paso 4 · Comparar con una librería](#paso-4--comparar-con-una-librería)
- [Paso 5 · Medir la seguridad del resultado](#paso-5--medir-la-seguridad-del-resultado)
- [Paso 6 · Responder al cliente](#paso-6--responder-al-cliente): una respuesta de ejemplo de 150 palabras, explicada
- [Para la review: las cinco cosas que hay que saber explicar](#para-la-review-las-cinco-cosas-que-hay-que-saber-explicar)

## Cómo usarlo

**Primero intentadlo.** Cuando algo no sale, seguid siempre este orden:

| Escalón | Qué hacéis |
|---|---|
| 1 | Leed el mensaje del `assert`: dice **qué esperaba** y **qué ha recibido** |
| 2 | Mirad la página del paso (su «Si algo falla») y el cuaderno «en clase» que toque |
| 3 | Preguntad al equipo |
| 4 | Preguntad al docente |
| 5 | **Este solucionario**, para contrastar o desbloquearos |

**Después de mirarlo, cerradlo y volved a escribirlo sin mirar.**

- Copiar una línea no es saberla.
- La prueba de que la sabéis es **explicársela a vuestra pareja con vuestras palabras**.
- En la review, el docente puede preguntar por cualquier línea.

## Las cifras que tienen que salir

| Dónde | Cifra | Qué es |
|---|---|---|
| Paso 1 | `(1096, 6)` | 1096 días y 6 columnas (con `mes`) |
| Paso 2 | media `68.49` · mínimo `47.3` · máximo `96.8` | La ocupación de los tres años |
| Paso 2 | enero `78.8` · septiembre `60.1` | El mes más lleno y el más vacío |
| Paso 3 | `pendiente_simple` ≈ **−1.86** | Puntos de ocupación por cada °C, sin controlar nada |
| Paso 3 | `efecto_temp_control` ≈ **−0.09** | La temperatura, una vez descontado el mes |
| Paso 3 | `efecto_festivo_control` ≈ **+9.11** | Lo que suma un festivo, una vez descontado el mes |
| Paso 4 | las dos columnas de `comparacion` **iguales** | Vuestro descenso y `statsmodels` dan lo mismo |
| Paso 5 | `p_temp_control` ≈ **0.48** | La temperatura ya no es significativa con control |
| Paso 5 | `ic_festivo` ≈ **(7.35, 10.87)** | Un festivo suma entre 7 y 11 puntos |
| Paso 5 | `p_festivo_ttest` ≈ **1e-30** | Los festivos se llenan más, sin duda |
| Paso 5 | `r2_control` ≈ **0.58** | El modelo explica el 58 % de la variación |

## Paso 1 · Cargar los datos en una base de datos

**Qué tiene que salir:** `Punto de control 1 superado`, `diaria.shape` = `(1096, 6)` y el fichero `turisdata_reto.db` en el panel de archivos.

```python
datos = pd.read_csv(dato("ocupacion_diaria.csv"))
con = sqlite3.connect(RUTA_BD)
datos.to_sql("ocupacion_diaria", con, if_exists="replace", index=False)
con.execute("CREATE INDEX IF NOT EXISTS idx_ocupacion_fecha ON ocupacion_diaria(fecha)")
con.commit()
diaria = pd.read_sql_query(
    "SELECT *, CAST(SUBSTR(fecha, 6, 2) AS INTEGER) AS mes FROM ocupacion_diaria", con)
```

**Qué hace cada línea**

- `pd.read_csv(dato(...))`: lee el archivo de texto y lo guarda como tabla (`datos`).
- `sqlite3.connect(RUTA_BD)`: abre (o crea) la base. **La conexión se llama `con`**, porque el punto de control usa ese nombre.
- `datos.to_sql(...)`: copia la tabla dentro de la base. `if_exists="replace"` permite repetir la celda sin duplicar filas.
- `CREATE INDEX ...`: crea el índice. El nombre `idx_ocupacion_fecha` tiene que ser exactamente ese.
- `con.commit()`: guarda los cambios.
- `pd.read_sql_query(...)`: lee desde la base con SQL. `SUBSTR(fecha, 6, 2)` recorta el mes de `2023-07-14` (`07`) y `CAST(... AS INTEGER)` lo pasa a número (`7`).

**Fallos habituales**

- **`Falta la columna mes`:** falta `AS mes` o están mal el `6` y el `2` de `SUBSTR`.
- **`Falta el índice`:** el nombre es distinto o falta `con.commit()`.
- **`Cannot operate on a closed database`:** se ha ejecutado `con.close()` antes de tiempo; reiniciad y ejecutad de arriba abajo.

## Paso 2 · Mirar los datos

**Qué tiene que salir** (no hay `assert`: lo revisa el equipo):

- `describe()`: 1096 días, media `68.49`, desviación `9.61`, mínimo `47.3` y máximo `96.8`.
- Medias por mes: enero `78.8`, febrero `77.6` y diciembre `78.6` arriba; septiembre `60.1`, junio `60.8` y agosto `62.1` abajo.
- Un diagrama de cajas con cajas **altas a los lados** y **bajas en el centro**.
- Una nube de puntos que **baja de izquierda a derecha**.

```python
print(diaria["ocupacion_pct"].describe())

medias_mes = diaria.groupby("mes")["ocupacion_pct"].mean()
print(medias_mes.round(1))
print(medias_mes.sort_values().round(1))

diaria.boxplot(column="ocupacion_pct", by="mes", figsize=(8, 4))
plt.suptitle("")
plt.title("Ocupación diaria según el mes")
plt.xlabel("Mes (1 = enero, 12 = diciembre)")
plt.ylabel("Ocupación (%)")
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(diaria["temperatura_c"], diaria["ocupacion_pct"], s=8, alpha=0.5)
plt.title("A más temperatura, menos ocupación")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Ocupación (%)")
plt.show()
```

**Observaciones de ejemplo** (con vuestras palabras, vale algo más corto)

- «La ocupación media es del 68,5 %, y va del 47 % al 97 %.»
- «Los meses más llenos son diciembre, enero y febrero (en torno al 78 %); los más vacíos, de mayo a octubre (en torno al 60–63 %).»
- «En el gráfico de puntos, a más temperatura baja la ocupación. Ojo: el calor y ciertos meses van juntos, así que todavía no sabemos si el calor es la causa.»

**Fallos habituales**

- **Sale `<bound method ...>`:** falta el paréntesis de `describe()`.
- **El gráfico tiene un título en inglés:** falta `plt.suptitle("")`.
- **Sale `<Axes: ...>` y no el dibujo:** falta `plt.show()`.

## Paso 3 · Regresión lineal desde cero

**Qué tiene que salir**

- `pendiente_simple` ≈ **−1.86**.
- El mensaje `Punto de control 2 superado: simple -1.86 · con control: temp -0.09, festivo +9.11`.
- Una curva de aprendizaje que **cae en picado y se aplana enseguida**.

### 3.1 · Las dos funciones

```python
def gradiente_mse(X, y, w):
    return 2 / len(y) * X.T @ (X @ w - y)


def entrenar(X, y, tasa, epocas):
    w = np.zeros(X.shape[1])
    historial = []
    for _ in range(epocas):
        w = w - tasa * gradiente_mse(X, y, w)
        historial.append(np.mean((X @ w - y) ** 2))
    return w, historial
```

- `X @ w - y`: el **error de cada día** (lo que predice la recta menos lo que pasó de verdad).
- `2 / len(y) * X.T @ (...)`: resume esos errores en un número por peso. Es el **gradiente**: hacia dónde crece el error más deprisa.
- `w = np.zeros(...)`: se empieza con una recta plana (todos los pesos a 0).
- `w = w - tasa * gradiente`: un pasito **en sentido contrario** al gradiente, para que el error baje.
- `historial.append(...)`: se apunta el error de cada vuelta, para dibujar la curva.

### 3.2 · Modelo simple (solo temperatura)

```python
y = diaria["ocupacion_pct"].to_numpy()
t = diaria["temperatura_c"]
t_est = (t - t.mean()) / t.std()
X = np.column_stack([np.ones(len(diaria)), t_est.to_numpy()])
w, historial = entrenar(X, y, 0.1, 2000)
pendiente_simple = w[1] / t.std()
```

- **Estandarizar** (`t_est`) hace que la temperatura tenga una escala parecida a la de la columna de unos: así el descenso no se desboca con `tasa = 0.1`.
- **`w` sale** `[68.49, -6.04]`:
  - `68.49` es la ocupación media (la constante).
  - `-6.04` es la pendiente **por cada desviación de temperatura** (unos 3,2 °C).
- **Deshacer la estandarización:** `-6.04 / 3.245 = -1.86` puntos por °C. Es lo que entiende el cliente.

### 3.3 · Curva de aprendizaje

```python
plt.plot(historial)
plt.title("Curva de aprendizaje: el error baja y se estabiliza")
plt.xlabel("Época (vuelta del descenso)")
plt.ylabel("Error cuadrático medio (MSE)")
plt.show()
```

- El error arranca en unos **3081** y a la vuelta 50 ya está en ≈ **56**.
- Después casi no cambia: el modelo **ha convergido** (ya no mejora).
- Comentario de ejemplo: «Baja muy rápido al principio y se aplana: ha convergido.»

### 3.4 · Modelo con control (temperatura, festivo y mes)

```python
meses = pd.get_dummies(diaria["mes"], drop_first=True, dtype=float)
M = pd.concat([diaria[["temperatura_c", "festivo"]].astype(float), meses], axis=1)
medias, desv = M.mean(), M.std()
Xc = np.column_stack([np.ones(len(M)), ((M - medias) / desv).to_numpy()])
wc, historial_c = entrenar(Xc, y, 0.1, 2000)
efecto_temp_control = wc[1] / desv["temperatura_c"]
efecto_festivo_control = wc[2] / desv["festivo"]
```

- `get_dummies(..., drop_first=True)`: el mes pasa a **11 columnas de 0 y 1** (el mes que falta se deduce de los demás). Con 12 habría información repetida y el modelo se rompería.
- `M` tiene **13 columnas**: temperatura, festivo y los 11 meses.
- `wc[1]` es el peso de la temperatura y `wc[2]` el del festivo (el orden de las columnas: unos, temperatura, festivo, meses).
- Cada peso se divide entre **la desviación de su propia variable**: así vuelve a puntos por °C y a puntos por día festivo.
- **Resultado:** `efecto_temp_control` = **−0.09** y `efecto_festivo_control` = **+9.11**.

**Cómo se lee**

- Sin controlar, cada grado parece quitar **1.86 puntos**.
- Comparando días **del mismo mes**, cada grado quita **0.09**: casi nada.
- El calor no era la causa: **el mes** (la temporada) mueve a la vez la temperatura y la ocupación. Es una **variable de confusión**.
- El festivo sigue sumando **9 puntos**: ese efecto aguanta el control.

**Fallos habituales**

- **El error crece sin parar, sale `nan` o `inf`:** falta estandarizar o la tasa es demasiado grande. Probad con `0.05` o `0.01`.
- **`La pendiente simple debería ser ≈ -1.86 y tienes -6.037`:** falta dividir entre `t.std()`.
- **El efecto del festivo sale raro:** se ha dividido entre la desviación de la temperatura en vez de entre `desv["festivo"]`.
- **El efecto con control sale raro:** puede faltar algún mes (`M` construida sin `meses`) o haberse olvidado `drop_first=True`.

## Paso 4 · Comparar con una librería

**Qué tiene que salir:** `Punto de control 3 superado` y la tabla con **las dos columnas iguales**:

```text
                        desde_cero  statsmodels
pendiente_simple            -1.860       -1.860
efecto_temp_control         -0.089       -0.089
efecto_festivo_control       9.111        9.111
```

```python
ols_simple = smf.ols("ocupacion_pct ~ temperatura_c", data=diaria).fit()
ols_control = smf.ols("ocupacion_pct ~ temperatura_c + festivo + C(mes)", data=diaria).fit()

comparacion = pd.DataFrame(
    {"desde_cero": [pendiente_simple, efecto_temp_control, efecto_festivo_control],
     "statsmodels": [ols_simple.params["temperatura_c"],
                     ols_control.params["temperatura_c"],
                     ols_control.params["festivo"]]},
    index=["pendiente_simple", "efecto_temp_control", "efecto_festivo_control"])
```

**Qué hace cada parte**

- La fórmula `"ocupacion_pct ~ temperatura_c"` se lee: «la ocupación **depende de** la temperatura».
- `+ festivo + C(mes)` añade el festivo y el mes (`C(...)` lo trata como categoría: 12 meses distintos).
- `.fit()` ajusta el modelo. `.params["festivo"]` es el peso de esa variable.
- La tabla tiene **3 filas × 2 columnas**.

**Por qué coinciden**

- `statsmodels` resuelve lo mismo con otro método (la fórmula clásica de mínimos cuadrados).
- Si vuestro descenso del gradiente da lo mismo, **está bien escrito**. Esa es la comprobación.

**Fallos habituales**

- **`Tu implementación no coincide`:** mirad en qué fila. Si es la primera, el modelo simple (¿dividisteis entre `t.std()`?). Si son las otras dos, el modelo con control. Probad antes con más épocas (5000).
- **`La tabla debe tener 3 filas y 2 columnas`:** comprobad `comparacion.shape`, que debe ser `(3, 2)`.
- **`PatsyError`:** hay un nombre de columna mal escrito en la fórmula.

## Paso 5 · Medir la seguridad del resultado

**Qué tiene que salir:** `Punto de control 4 superado` y, con el `print`, `0.481 (7.35, 10.87) 1.127026104033321e-30 0.579`.

```python
festivos = diaria.loc[diaria["festivo"] == 1, "ocupacion_pct"]
no_festivos = diaria.loc[diaria["festivo"] == 0, "ocupacion_pct"]

p_temp_control = ols_control.pvalues["temperatura_c"]
ic_festivo = tuple(ols_control.conf_int().loc["festivo"])
p_festivo_ttest = stats.ttest_ind(festivos, no_festivos, equal_var=False).pvalue
r2_control = ols_control.rsquared

print(round(p_temp_control, 3), tuple(round(x, 2) for x in ic_festivo), p_festivo_ttest, round(r2_control, 3))
```

**Cómo se lee cada cifra** (una frase por cifra: son la base de la respuesta al cliente)

| Cifra | Valor | Frase |
|---|---|---|
| `p_temp_control` | 0.48 | «Una vez descontado el mes, la temperatura casi no cambia la ocupación (−0,09 puntos por grado, p = 0,48): con estos datos **no podemos afirmar** que influya.» |
| `ic_festivo` | (7.35, 10.87) | «Con un día festivo, la ocupación sube unos 9 puntos (con un 95 % de confianza, entre 7 y 11).» |
| `p_festivo_ttest` | 1e-30 | «Si no hubiera ningún efecto, sería **muy raro** ver unos datos así: los festivos se llenan más.» |
| `r2_control` | 0.58 | «El modelo explica un 58 % de la variación de la ocupación; el resto depende de otras cosas.» |

**Ideas que hay que tener claras**

- **p-valor grande (0.48)** no significa «no hay efecto»: significa que **los datos no bastan para afirmarlo**.
- **p-valor minúsculo (1e-30)** dice que el efecto existe, pero **no si es grande**. Para eso se mira el efecto: **9 puntos**.
- **El intervalo (7.35, 10.87)** es el rango razonable del efecto del festivo. Cuanto más estrecho, más preciso.
- **El tamaño del efecto** ya lo tenéis: `efecto_temp_control` (−0.09 puntos por grado) y `efecto_festivo_control` (+9.11 puntos por festivo).
- **Antes y después de controlar:** los festivos tienen de media `83.9 %` y los demás `67.6 %` (16,3 puntos de diferencia). Con control, la diferencia baja a **9 puntos**, porque parte venía de que los festivos caen en meses de temporada alta.

**Fallos habituales**

- **`KeyError: 'festivo'`:** el nombre está mal escrito dentro de `.loc[...]`.
- **`p_temp_control` sale 3e-121:** se ha cogido `ols_simple` en vez de `ols_control`.
- **`ic_festivo` no es una pareja:** falta `tuple(...)`.

## Paso 6 · Responder al cliente

**Qué tiene que salir:** una respuesta de **150 palabras o menos**, el cuaderno ejecutado de arriba abajo sin errores y las dos celdas finales rellenas.

### Respuesta de ejemplo (nivel alto)

> Los festivos suben la ocupación unos 9 puntos (entre 7 y 11, con un 95 % de confianza), incluso comparando días del mismo mes: es un efecto sólido. La temperatura, en cambio, solo *parece* bajarla (−1,9 puntos por grado) porque los meses más fríos son temporada alta; al comparar días del mismo mes el efecto desaparece (−0,1 puntos por grado, indistinguible de cero). Recomendamos reforzar el personal y ajustar los precios en festivos y por temporada, no según la temperatura de cada día. Límites: son datos sintéticos de un único alojamiento y solo observados, así que no prueban causalidad; el modelo explica un 58 % de la variación y el resto depende de otros factores. Cautela: no conviene fijar precios automáticamente con este modelo sin revisión humana.

**Por qué funciona**

- **Contesta primero** a las dos preguntas del cliente (festivos y temperatura) con **cifras e incertidumbre**.
- **Explica el espejismo** del calor con palabras sencillas: «los meses más fríos son temporada alta».
- **Recomienda algo que se puede hacer:** personal y precios, por festivo y por temporada.
- **Dice lo que no se puede afirmar:** causalidad, un solo alojamiento, datos sintéticos, el 58 %.
- **Termina con una frase de IA responsable:** nada de precios automáticos sin revisión humana.
- **Todas las cifras salen del cuaderno** (−1.86, −0.09, 9.11, 7.35, 10.87, 0.58).
- **Sin jerga:** no aparece «p-valor», «OLS» ni «gradiente».

**Qué la empeoraría**

- Decir que **el calor baja la ocupación** (confundir correlación con causalidad).
- Dar cifras sin intervalo («9 puntos» a secas).
- Pasarse de 150 palabras o dejar el `...` de la plantilla.
- Una recomendación vaga («hay que tener cuidado con los precios»).

### Las dos celdas finales (ejemplos)

**«Uso de IA»**

> Le pedí que me explicara el descenso del gradiente con una analogía y revisara la redacción de la respuesta. Comprobé que las cifras eran las de mi cuaderno y no cambié ninguna. Cambié dos frases que sonaban demasiado técnicas.

**«Revisión con la rúbrica»**

```text
## Revisión con la rúbrica
**Revisado por:** Ana · **Fecha:** 05/11/2026

| Criterio | Nivel (1-4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 4 | La tabla `comparacion` tiene las dos columnas iguales |
| Reproducibilidad | 4 | He reiniciado y ejecutado todo: sin errores y con la base creada |
| Análisis y comunicación al cliente | 3 | La respuesta cabe en 150 palabras y trae intervalos; falta una recomendación más concreta |
| IA responsable | 3 | Dice que no hay que fijar precios sin revisión humana |

**Lo primero que mejoraríamos:** concretar cuánto personal reforzar en festivos.
```

## Para la review: las cinco cosas que hay que saber explicar

Cada persona del equipo tiene que poder contestar, **sin mirar**:

1. **¿Qué es el descenso del gradiente?** Empezar con una recta plana y, vuelta a vuelta, dar un pasito en el sentido en que el error baja, hasta que se estabiliza.
2. **¿Por qué se estandariza y luego se «deshace»?** Para que el descenso no se desboque; y para dar el resultado en puntos por °C, que es lo que entiende el cliente.
3. **¿Por qué coincide con `statsmodels`?** Resuelven el mismo problema con otro método: si dan lo mismo, nuestro código está bien.
4. **¿Por qué la temperatura pasa de −1,86 a −0,09?** Porque el mes mueve a la vez la temperatura y la ocupación (variable de confusión). Comparando días del mismo mes, el calor casi no importa.
5. **¿Qué no podemos afirmar?** Que el festivo o el calor **causen** nada: los datos son observados, sintéticos y de un solo alojamiento.
