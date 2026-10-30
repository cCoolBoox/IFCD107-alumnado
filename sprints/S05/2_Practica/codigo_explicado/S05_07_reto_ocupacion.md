# Código explicado · S05.07 · Reto «¿La ocupación depende de esto?» (plantilla del cuaderno entregable)
<!--manual-->

> **Para qué sirve.** Este cuaderno es la **plantilla del reto**: no trae el código hecho, trae **huecos** (`...` y `# TODO`) que rellenáis vosotros. Por eso esta página no explica código ya escrito: os dice, **hueco por hueco**, qué hay que construir, con qué herramienta y qué error es el más habitual. Las palabras de código nuevas se explican en los cuadernos `S05_03` (descenso del gradiente), `S05_05` (contrastes) y `S05_06` (bases de datos).
>
> **Cuaderno:** [abrir en Colab](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S05/2_Practica/S05_07_reto_ocupacion.ipynb) · [descargar](../S05_07_reto_ocupacion.ipynb)
>
> **Cómo usarlo:** 1) leed el apartado del cuaderno; 2) buscad aquí el mismo número; 3) escribid vuestro código en el hueco; 4) ejecutad la celda: los `assert` (puntos de control) os avisan si algo no cuadra.

**Cómo se lee una línea de código.** Casi todo sigue la forma `resultado = objeto.acción(opciones)`: se lee **de derecha a izquierda**, «coge este objeto, hazle esta acción con estas opciones y guarda lo que salga en `resultado`». Lo que va tras `#` es un comentario: Python lo ignora.

## Celdas de preparación (no se tocan)

Las dos primeras celdas de código ya están hechas: descargan los datos del curso y cargan las librerías (`sqlite3` para la base de datos, `pandas` para las tablas, `matplotlib` para los gráficos, `statsmodels` y `scipy.stats` para la estadística). También fijan `SEMILLA = 42` (para que el azar salga igual en todos los ordenadores) y `RUTA_BD = "turisdata_reto.db"` (el nombre del archivo de la base).

## 1 · Base de datos: cargar y consultar

| Qué hay que hacer | Con qué | Ojo con… |
|---|---|---|
| Crear la tabla `ocupacion_diaria` desde el CSV | `datos.to_sql("ocupacion_diaria", con, if_exists="replace", index=False)` | `replace` borra y vuelve a crear la tabla: así podéis ejecutar la celda varias veces sin duplicar filas. |
| Crear un índice sobre `fecha` | `con.execute("CREATE INDEX IF NOT EXISTS ... ON ocupacion_diaria(fecha)")` | Un índice es como el índice de un libro: acelera las búsquedas por esa columna. |
| Leer los datos **con SQL** | `pd.read_sql("SELECT ..., CAST(SUBSTR(fecha, 6, 2) AS INTEGER) AS mes FROM ocupacion_diaria", con)` | `SUBSTR(fecha, 6, 2)` recorta los caracteres 6 y 7 de `2025-07-14` (el mes, `07`); `CAST(... AS INTEGER)` lo convierte en el número 7. |

Resultado: un DataFrame `diaria` con una columna `mes` de 1 a 12.

## 2 · Primer vistazo a los datos

- `diaria["ocupacion_pct"].describe()` da media, dispersión y extremos de golpe.
- `diaria.groupby("mes")["ocupacion_pct"].mean()` calcula **una media por mes**; ordenadla para ver los meses de mayor y menor ocupación.
- Dos gráficos como mínimo: un **diagrama de caja** por mes (`sns.boxplot` o `plt.boxplot`) y una **dispersión** temperatura-ocupación (`plt.scatter`). Poned título y ejes **en español**.
- Debajo, en la celda de texto, 2–3 observaciones en vuestras palabras («en agosto la ocupación…»).

## 3 · Regresión lineal desde cero

Es el mismo método del cuaderno `S05_03`, con datos nuevos.

1. **Estandarizar** una variable es restarle su media y dividir entre su desviación (`(x - x.mean()) / x.std()`). Así todas las variables tienen una escala parecida y el descenso del gradiente converge.
2. **`gradiente_mse(X, y, w)`** devuelve `(2 / n) * X.T @ (X @ w - y)`: cuánto cambia el error al mover cada peso. `@` es el producto de matrices; `X.T` es la matriz traspuesta.
3. **`entrenar(X, y, tasa, epocas)`** repite `w = w - tasa * gradiente` durante las épocas indicadas y guarda el error en cada vuelta (`historial`). Para el modelo con control: unas 2.000 épocas con tasa 0,1.
4. **Modelo con control:** añadid `festivo` y los indicadores de mes con `pd.get_dummies(diaria["mes"], drop_first=True)` (11 columnas; se quita una para no repetir información).
5. **Deshacer la estandarización:** cada coeficiente se divide entre la desviación de **su** variable. Así `pendiente_simple` queda en *puntos de ocupación por °C* y no en «desviaciones».

Error típico: olvidar la columna de unos (el término independiente) o dividir entre la desviación equivocada.

La **curva de aprendizaje** es `plt.plot(historial)`: el error tiene que bajar y aplanarse. Si sube o da saltos, la tasa es demasiado grande.

## 4 · Contraste con una librería

`smf.ols("ocupacion_pct ~ temperatura_c", data=diaria).fit()` ajusta el mismo modelo con `statsmodels`. La fórmula del modelo con control es `"ocupacion_pct ~ temperatura_c + festivo + C(mes)"` (`C(mes)` trata el mes como categoría). Los coeficientes están en `.params["temperatura_c"]`. La tabla `comparacion` (3 filas × 2 columnas) debe mostrar que **vuestro código y la librería coinciden** casi al decimal.

## 5 · Responder con estadística

| Variable que se guarda | De dónde sale |
|---|---|
| `p_temp_control` | `ols_control.pvalues["temperatura_c"]` |
| `ic_festivo` | `tuple(ols_control.conf_int().loc["festivo"])` (intervalo de confianza del 95 %) |
| `p_festivo_ttest` | `stats.ttest_ind(festivos, no_festivos, equal_var=False).pvalue` (t de Welch) |
| `r2_control` | `ols_control.rsquared` |

Recordad lo que enseña `S05_05`: un p-valor alto (> 0,05) **no demuestra** que no haya efecto, solo que estos datos no bastan para afirmarlo.

## 6 · Respuesta al cliente

No hay código: son 150 palabras como máximo para una persona que no programa. Usad el orden del cuaderno: respuesta directa con cifras e incertidumbre → recomendación accionable → límites (correlación no es causalidad, el mes confunde, datos sintéticos de un solo alojamiento) → una frase de IA responsable.

## 7 · Antes de entregar

La última celda (`con.close()`) cierra la conexión con la base. Antes de subir el cuaderno: **Entorno de ejecución → Reiniciar y ejecutar todo** y comprobad que no hay errores. Las versiones de las librerías se anotan en el **README de vuestro repositorio** (o con una celda `!pip freeze`).
