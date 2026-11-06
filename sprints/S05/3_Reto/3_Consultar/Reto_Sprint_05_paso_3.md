# Paso 3 · Regresión lineal desde cero (día 2, 35 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 3 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 4 →](Reto_Sprint_05_paso_4.md)
<!--/nav-->

1. Escribir `gradiente_mse` y `entrenar` (el descenso del gradiente).
2. Ajustar el modelo simple (solo temperatura) y dibujar la curva de aprendizaje.
3. Ajustar el modelo con control (temperatura, festivo y mes).

**En sencillo.** El cliente quiere saber **cuánto cambia la ocupación por cada grado más de temperatura**. Si miráis la nube de puntos del paso anterior, entre ellos cabe una «mejor recta», y su **pendiente** responde justo a eso: cuántos puntos de ocupación sube o baja por cada °C. En vez de pedirle esa recta a una librería, la vais a encontrar vosotros con el **descenso del gradiente**. Es como bajar una montaña con niebla: no veis el valle, pero notáis hacia dónde baja el suelo bajo los pies, dais un pasito en esa dirección y repetís. Aquí la «montaña» es el **error** de la recta (cuánto se equivoca) y cada paso la corrige un poquito. Después repetís con más información (festivos y mes) para ver si el resultado cambia. Es el paso más largo y el más «de código», pero casi todo lo que tenéis que escribir está debajo, línea a línea.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Función** (`def`) | Una receta con nombre: la escribís una vez y la usáis las veces que haga falta. `def entrenar(…):` define la receta `entrenar`. |
| **Bucle** (`for`) | Repetir las mismas líneas varias veces. |
| **Lista** | Una colección ordenada de valores. Con `.append(x)` se añade uno al final. |
| **NumPy** (`np`) | La librería de cálculo con números y tablas de números (*arrays*). |
| **`@`** | El producto de matrices (el «multiplicar» de las tablas de números). `X.T` es la tabla de `X` girada (la traspuesta). |
| **Error cuadrático medio** (MSE) | La media de los errores al cuadrado: cuánto se aleja la recta de los puntos. Cuanto más pequeño, mejor. |
| **Gradiente** | La indicación de hacia dónde hay que mover la recta para que el error crezca más deprisa. Se va en sentido contrario. |
| **Tasa de aprendizaje** (`tasa`) | El tamaño del pasito. Muy pequeño: tarda mucho. Muy grande: se pasa de largo y el error se dispara. |
| **Época** | Una vuelta completa del bucle (calcular el gradiente y dar un paso). |
| **Estandarizar** | Restar la media y dividir entre la desviación, para que las variables tengan una escala parecida y el descenso no se desboque. |
| **Pesos** (`w`) | Los números que definen la recta: la constante y la pendiente. |
| **Variable indicadora** | Una columna de 0 y 1 (por ejemplo, «¿es julio?: sí o no»). Así se meten los meses en la cuenta. |

**Cómo se hace**

1. **Saber qué llega a las funciones.** `y` es lo que queremos predecir (la ocupación). `X` es una tabla de números con una **columna de unos** (para la constante de la recta) y las variables explicativas. `w` son los pesos: uno por columna de `X`. Con `X @ w` se calcula la predicción de todos los días de una vez.
2. **Escribir las dos funciones.** En la celda del apartado «3 · Regresión lineal desde cero» (borrad los `...`). **Importante:** los `assert` y el `print` del final de la celda se quedan **al final**; todo el código de este paso (funciones, modelo simple y modelo con control) va **entre la línea `# TODO` y los `assert`**, nunca debajo de ellos, porque los `assert` comprueban lo que se ha calculado antes:

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

    Qué hace cada parte:

    - `gradiente_mse(X, y, w)` calcula el gradiente: `X @ w - y` es el error de cada día, y `2 / len(y) * X.T @ (…)` los resume en un número por peso. Basta con teclearla bien; la idea es la del cuaderno [`S05_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/en_clase/S05_03_gradiente_regresion_en_clase.ipynb).
    - `w = np.zeros(X.shape[1])`: empieza con todos los pesos a cero (una recta plana). `X.shape[1]` es el número de columnas de `X`.
    - `historial = []`: una lista vacía donde se apuntará el error de cada vuelta.
    - `for _ in range(epocas):`: repite lo de debajo `epocas` veces. Lo que está **hacia dentro** (con sangría) es lo que se repite.
    - `w = w - tasa * gradiente_mse(X, y, w)`: el pasito: se mueven los pesos en sentido contrario al gradiente, en la medida que marca `tasa`.
    - `historial.append(np.mean((X @ w - y) ** 2))`: calcula el error (MSE) actual y lo apunta en la lista.
    - `return w, historial`: devuelve los pesos finales y la lista de errores. **Sin `scikit-learn`**: el reto pide hacerlo a mano.

3. **Modelo simple (solo temperatura).** En la misma celda, debajo de las funciones y **encima de los `assert`**:

    ```python
    y = diaria["ocupacion_pct"].to_numpy()
    t = diaria["temperatura_c"]
    t_est = (t - t.mean()) / t.std()
    X = np.column_stack([np.ones(len(diaria)), t_est.to_numpy()])
    w, historial = entrenar(X, y, 0.1, 2000)
    pendiente_simple = w[1] / t.std()
    ```

    - `y = …to_numpy()`: la ocupación como tabla de números de NumPy.
    - `t_est = (t - t.mean()) / t.std()`: la temperatura **estandarizada** (restada la media y dividida entre la desviación).
    - `np.column_stack([…])`: pega columnas en una tabla; la primera es una columna de unos (`np.ones`), la segunda, la temperatura estandarizada.
    - `entrenar(X, y, 0.1, 2000)`: hace 2000 vueltas con pasitos de tamaño 0,1.
    - `w[1] / t.std()`: `w[1]` es la pendiente **en «desviaciones de temperatura»**; al dividir entre `t.std()` (unos 3,2 °C) se **deshace la estandarización** y queda en **puntos de ocupación por cada °C**, que es lo que entiende el cliente. Esa es `pendiente_simple`.

4. **Curva de aprendizaje.** En la celda siguiente del cuaderno (la del `plt.plot`):

    ```python
    plt.plot(historial)
    plt.title("Curva de aprendizaje: el error baja y se estabiliza")
    plt.xlabel("Época (vuelta del descenso)")
    plt.ylabel("Error cuadrático medio (MSE)")
    plt.show()
    ```

    Debajo, una línea de texto: ¿baja y se aplana? (entonces el modelo ha **convergido**: ya no mejora). Para ver mejor la bajada del principio, probad `plt.plot(historial[:100])`.

5. **Modelo con control: temperatura, festivo y mes.** «Controlar» significa meter también el festivo y el mes, para ver qué pasa con la temperatura cuando ya se tiene en cuenta la época del año. En la misma celda del apartado 3, debajo de lo anterior y **todavía encima de los `assert`**:

    ```python
    meses = pd.get_dummies(diaria["mes"], drop_first=True, dtype=float)
    M = pd.concat([diaria[["temperatura_c", "festivo"]].astype(float), meses], axis=1)
    medias, desv = M.mean(), M.std()
    Xc = np.column_stack([np.ones(len(M)), ((M - medias) / desv).to_numpy()])
    wc, historial_c = entrenar(Xc, y, 0.1, 2000)
    efecto_temp_control = wc[1] / desv["temperatura_c"]
    efecto_festivo_control = wc[2] / desv["festivo"]
    ```

    - `pd.get_dummies(diaria["mes"], drop_first=True, …)`: convierte el mes en **11 columnas** de 0 y 1 (una por mes menos uno: el mes que falta se deduce de los demás, y así no se repite información).
    - `pd.concat([…], axis=1)`: pega a la derecha la temperatura, el festivo y las 11 columnas de meses en una sola tabla `M` (13 columnas).
    - `medias, desv = M.mean(), M.std()`: la media y la desviación de **cada** columna. Se guardan porque hace falta `desv` al final.
    - `Xc = …((M - medias) / desv)…`: estandariza todas las columnas y les pega delante la columna de unos.
    - `wc[1]` es el peso de la temperatura y `wc[2]`, el del festivo (el orden de las columnas: unos, temperatura, festivo, meses). Cada uno se divide entre **la desviación de su propia variable** para volver a las unidades originales: puntos por °C para la temperatura y puntos por día festivo (la desviación del festivo es la suya, no la de la temperatura).

6. **Ejecutar y comprobar.** Pulsad ▶. Los `assert` de debajo comparan vuestros tres números con los esperados.

**Qué deberíais ver.**
- **El error (MSE)** arranca en unos 3081 y baja a ≈ 56 en menos de 50 vueltas; el resto de las 2000 vueltas casi no cambia nada. Por eso la curva cae en picado y **se aplana enseguida**.
- **`pendiente_simple` ≈ −1,86**: por cada grado más, la ocupación baja unos 1,86 puntos.
- El mensaje `Punto de control 2 superado: simple -1.86 · con control: temp -0.09, festivo +9.11`.
- Fijaos en que **la temperatura casi deja de importar** (−0,09) cuando se controla el mes, y que el festivo suma unos 9 puntos.

En el nivel mínimo, el punto de control dará error en las líneas del modelo con control hasta que lo hagáis.

**Hecho cuando:** `pendiente_simple` sale ≈ −1,86, la curva de aprendizaje está dibujada y comentada y (en el estándar) el punto de control 2 está superado.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'np' is not defined` (o `'diaria'`) | No se han ejecutado la celda de importaciones o la del apartado 1. | Ejecutad desde la primera celda hacia abajo. |
| El error crece sin parar, sale `nan` o `inf`, o números enormes | La tasa es demasiado grande (o no habéis estandarizado). Con la temperatura sin estandarizar y tasa 0,1 el error llega a cifras de más de 100 cifras. | Estandarizad la temperatura y usad tasa 0,1; si aun así se dispara, bajadla (0,05 o 0,01). |
| `AssertionError: La pendiente simple debería ser ≈ -1.86 puntos/°C y tienes -6.037` | Habéis dejado la pendiente «en desviaciones»: falta deshacer la estandarización. | Dividid `w[1]` entre `t.std()`: `pendiente_simple = w[1] / t.std()`. |
| `AssertionError` en el efecto con control (temperatura cerca de −1,86 o festivo raro) | Falta algún mes en el modelo, o se ha dividido entre la desviación equivocada. | Comprobad que `M` tiene 13 columnas (`M.shape`) y que cada coeficiente se divide entre **su** desviación. |
| `NameError: name 'pendiente_simple' is not defined` (o `efecto_temp_control`, `efecto_festivo_control`) | Ese código está **debajo** de los `assert` (se ejecuta después de comprobarlo), falta en la celda, o el nombre no coincide con el del cuaderno. | Poned todo el código **encima** de los `assert` y usad exactamente esos tres nombres. |
| `ValueError` que habla de `shapes` o `matmul` | Los tamaños no cuadran: `X` y `w` deben tener tantas columnas como pesos. | Mirad `X.shape` y `w.shape`: el segundo número de `X` debe ser el tamaño de `w`. |
| La curva es una raya casi vertical y plana | Es normal: el error baja casi todo en las primeras vueltas. | Dibujad solo el principio: `plt.plot(historial[:100])`. |

<!--nav-->
---

[← Paso 2](Reto_Sprint_05_paso_2.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 4 →](Reto_Sprint_05_paso_4.md)
<!--/nav-->
