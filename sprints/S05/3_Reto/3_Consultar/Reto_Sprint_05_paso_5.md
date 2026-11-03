# Paso 5 · Medir la seguridad del resultado (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 5 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 6 →](Reto_Sprint_05_paso_6.md)
<!--/nav-->

1. Obtener el p-valor, el intervalo de confianza y el R².
2. Calcular el tamaño del efecto.
3. Explicar cada cifra con palabras.

**En sencillo.** Ya tenéis números (una pendiente, un efecto del festivo…), pero el cliente querrá saber **cuánto se puede fiar de ellos**. Con solo tres años de datos, los resultados podrían ser casualidad. La estadística tiene herramientas para medir esa incertidumbre, y en este paso sacáis cuatro cifras del modelo de `statsmodels`: un **p-valor** (¿podría ser casualidad?), un **intervalo de confianza** (entre qué valores está el efecto) y el **R²** (cuánto explica el modelo). Después las **traducís a palabras**: es la parte que más cuenta, porque la respuesta al cliente se escribe con esas frases.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **p-valor** | «Si en realidad no hubiera ningún efecto, ¿qué probabilidad había de ver unos datos tan llamativos como estos?». Si es muy pequeño (menos de 0,05), sería raro que fuera casualidad. Si es grande, **los datos no bastan para afirmar un efecto** (no es lo mismo que «no hay efecto»). |
| **Intervalo de confianza del 95 %** | Un tramo de valores (de A a B) en el que, con bastante seguridad, está el efecto real. Cuanto más estrecho, más preciso. |
| **R²** | Cuánta de la variación de la ocupación explica el modelo: 0 es «nada» y 1 es «todo». |
| **Tamaño del efecto** | Cuánto cambia el resultado en las unidades de siempre (puntos de ocupación). Un p-valor pequeño dice que hay efecto, pero no si es grande o pequeño. |
| **t de Welch** | Una prueba que compara las medias de dos grupos (aquí, días festivos y no festivos) y devuelve un p-valor. |
| **`.loc[…]`** | Para elegir filas (y columnas) de una tabla por una condición o por su nombre. |
| **`1e-30`** | Notación científica: el 1 está en el lugar 30 después de la coma (0,000…001). Es un número minúsculo. |

**Cómo se hace**

1. **Separar los días festivos de los demás.** En la celda del apartado «5 · Responder con estadística» (borrad los `...`):

    ```python
    festivos = diaria.loc[diaria["festivo"] == 1, "ocupacion_pct"]
    no_festivos = diaria.loc[diaria["festivo"] == 0, "ocupacion_pct"]
    ```

    `diaria.loc[condición, "ocupacion_pct"]` se queda con la columna de ocupación **solo en las filas que cumplen la condición**. `==` significa «es igual a» (con un solo `=` se guardaría un valor, no se compararía).

2. **Sacar las cuatro cifras.**

    ```python
    p_temp_control = ols_control.pvalues["temperatura_c"]
    ic_festivo = tuple(ols_control.conf_int().loc["festivo"])
    p_festivo_ttest = stats.ttest_ind(festivos, no_festivos, equal_var=False).pvalue
    r2_control = ols_control.rsquared
    ```

    - `ols_control.pvalues["temperatura_c"]`: el p-valor de la temperatura **en el modelo con control** (el que ya tiene el mes).
    - `ols_control.conf_int().loc["festivo"]`: la fila del festivo de la tabla de intervalos de confianza (95 %); `tuple(…)` la guarda como pareja de dos números (A, B).
    - `stats.ttest_ind(…, equal_var=False).pvalue`: el t de Welch entre festivos y no festivos; `equal_var=False` es lo que lo convierte en la versión de Welch, y `.pvalue` se queda solo con el p-valor.
    - `ols_control.rsquared`: el R² del modelo con control.

3. **Mirar las cifras.** Para verlas, en una celda nueva:

    ```python
    print(round(p_temp_control, 3), tuple(round(x, 2) for x in ic_festivo), p_festivo_ttest, round(r2_control, 3))
    ```

4. **Calcular el tamaño del efecto.** No hay que calcular nada nuevo: ya lo tenéis en los coeficientes. Con un grado más, la ocupación cambia en `efecto_temp_control` puntos; un día festivo, en `efecto_festivo_control` puntos. Para ver el «antes y después de controlar», comparad las medias a pelo: `festivos.mean()` y `no_festivos.mean()`.
5. **Explicar cada cifra con palabras.** En una celda de texto, una frase por cifra, con estos moldes:

    - Festivo: *«Con un día festivo, la ocupación sube unos [X] puntos (con un 95 % de confianza, entre [A] y [B])».*
    - Temperatura: *«Una vez descontado el mes, la temperatura casi no cambia la ocupación: [X] puntos por grado, con un p-valor de [p]: con estos datos no podemos afirmar que influya».*
    - p-valor: *«Si no hubiera ningún efecto, sería muy raro (o no) ver unos datos así»*: usad «muy raro» si el p-valor es pequeño y «nada raro» si es grande.
    - R²: *«El modelo explica un [X] % de la variación de la ocupación; el resto depende de otras cosas».*

    Escribid las frases **con vuestras cifras**, porque son la base de la respuesta al cliente.

**Qué deberíais ver.** `Punto de control 4 superado` y, con el `print` de arriba, `0.481 (7.35, 10.87) 1.127026104033321e-30 0.579`:
- `p_temp_control` ≈ 0,48: la temperatura **no** es significativa una vez controlado el mes.
- `ic_festivo` ≈ (7,35 ; 10,87): un festivo suma entre 7 y 11 puntos.
- `p_festivo_ttest` minúsculo (del orden de `1e-30`): sin duda, los festivos se llenan más.
- `r2_control` ≈ 0,58: el modelo explica casi el 58 % de la variación.

Un detalle interesante: sin controlar nada, los días festivos tienen de media un 83,9 % de ocupación y los demás un 67,6 % (unos 16 puntos de diferencia); controlando el mes, el efecto del festivo baja a unos 9 puntos. Parte de la diferencia viene de que los festivos caen en meses de ocupación alta.

**Hecho cuando:** el punto de control 4 está superado y cada cifra tiene su frase explicada con palabras.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'ols_control' is not defined` | No se ha ejecutado el paso 4 (o Colab se reinició). | Ejecutad desde arriba, o al menos hasta el apartado 4. |
| `KeyError: 'festivo'` en `.loc[…]` | El nombre no coincide con una fila de la tabla. | Escribid `ols_control.conf_int()` para ver los nombres de las filas. |
| `AssertionError: Con control de mes, la temperatura no es significativa (p ≈ 0.48) y tienes p = …` | Habéis cogido el p-valor del modelo simple (`ols_simple`) en lugar del del modelo con control. | Usad `ols_control`. |
| `AssertionError: El IC del festivo debería ser ≈ (7.35, 10.87) y tienes …` | Habéis cogido otra fila o otro modelo. | Usad `ols_control.conf_int().loc["festivo"]`. |
| `AssertionError: El t-test de festivos debe dar un p-valor minúsculo` | Habéis comparado grupos mal formados (por ejemplo, con `=` en lugar de `==`). | Comprobad que `festivos.shape` es `(61,)` y `no_festivos.shape` es `(1035,)`. |
| El p-valor sale como `1.127026104033321e-30` y no entendéis qué es | Es notación científica: un número minúsculo. | Leedlo como «prácticamente cero»; en la explicación basta con decir «muy pequeño (menos de 0,001)». |

<!--nav-->
---

[← Paso 4](Reto_Sprint_05_paso_4.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 6 →](Reto_Sprint_05_paso_6.md)
<!--/nav-->
