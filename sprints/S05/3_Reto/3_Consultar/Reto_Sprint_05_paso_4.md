# Paso 4 · Comparar con una librería (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 4 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 5 →](Reto_Sprint_05_paso_5.md)
<!--/nav-->

1. Ajustar los mismos dos modelos con `statsmodels`.
2. Reunir los tres coeficientes en la tabla `comparacion`.
3. Comprobar que coinciden con los vuestros.

**En sencillo.** ¿Cómo sabéis que vuestro descenso del gradiente funciona? Comparándolo con una **librería profesional** que resuelve el mismo problema. `statsmodels` ajusta la recta con otro método (la fórmula clásica, mínimos cuadrados ordinarios) y, además, trae de serie las cifras estadísticas que necesitaréis en el paso siguiente. Si vuestro código y la librería dan **los mismos números**, vuestro código está bien; si no, hay algo que revisar. Es, además, el momento de ver qué se gana usando una librería: dos líneas hacen lo que vosotros habéis programado a mano.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **`statsmodels`** (`smf`) | Librería de estadística. `smf` es el apodo que le pone el cuaderno al módulo de modelos con fórmulas. |
| **OLS** (mínimos cuadrados) | El método clásico para ajustar una recta: busca los pesos que dejan el error cuadrático lo más pequeño posible (lo mismo que persigue vuestro descenso). |
| **Fórmula** (`"y ~ x1 + x2"`) | Una frase que describe el modelo: la `~` se lee «se explica por». `ocupacion_pct ~ temperatura_c` es «la ocupación se explica por la temperatura». |
| **`C(mes)`** | «Trata `mes` como categorías, no como un número». La librería crea sola las 11 columnas de 0 y 1 que vosotros hicisteis con `get_dummies`. |
| **`.fit()`** | «Ajusta»: calcula los pesos. Devuelve un objeto con todos los resultados. |
| **`.params`** | Los pesos (coeficientes) del modelo ajustado, con su nombre. |

**Cómo se hace**

1. **Ajustar los dos modelos.** En la celda del apartado «4 · Contraste con una librería» (borrad los `...`):

    ```python
    ols_simple = smf.ols("ocupacion_pct ~ temperatura_c", data=diaria).fit()
    ols_control = smf.ols("ocupacion_pct ~ temperatura_c + festivo + C(mes)", data=diaria).fit()
    ```

    - `smf.ols("…", data=diaria)` prepara el modelo: la fórmula dice qué se explica y con qué, y `data=diaria` indica de qué tabla salen las columnas.
    - `.fit()` lo ajusta. Guardad el resultado en `ols_simple` y `ols_control` (con esos nombres: se usan en el paso 5).

2. **Montar la tabla `comparacion`.** Debajo:

    ```python
    comparacion = pd.DataFrame(
        {"desde_cero": [pendiente_simple, efecto_temp_control, efecto_festivo_control],
         "statsmodels": [ols_simple.params["temperatura_c"],
                         ols_control.params["temperatura_c"],
                         ols_control.params["festivo"]]},
        index=["pendiente_simple", "efecto_temp_control", "efecto_festivo_control"])
    ```

    La tabla tiene **dos columnas** (`desde_cero`: vuestros números; `statsmodels`: los de la librería) y **tres filas** (las que dice `index=`). `ols_control.params["festivo"]` es el peso de la columna `festivo`, y así con los demás.

3. **Ejecutar.** Pulsad ▶: el cuaderno comprueba que la tabla es de 3 × 2 y que las dos columnas coinciden (se admite una diferencia de 0,02), y luego imprime la tabla.

**Qué deberíais ver.** `Punto de control 3 superado` y la tabla con dos columnas casi idénticas:

```
                        desde_cero  statsmodels
pendiente_simple            -1.860       -1.860
efecto_temp_control         -0.089       -0.089
efecto_festivo_control       9.111        9.111
```

Para curiosear, `print(ols_control.summary())` muestra el informe completo de la librería: lo usaréis en el paso 5.

**Hecho cuando:** `comparacion` tiene 3 × 2 valores que coinciden y el punto de control 3 está superado.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `AssertionError: Tu implementación no coincide con statsmodels:` y la tabla | Vuestros números y los de la librería se separan más de 0,02. | Mirad en qué fila: si es la primera, repasad el modelo simple (¿dividisteis entre `t.std()`?); si son las otras dos, el modelo con control. Antes de buscar un fallo, probad con más épocas (por ejemplo, 5000). |
| `AssertionError: La tabla debe tener 3 filas y 2 columnas` | Falta una fila o una columna, o hay alguna de más. | Comprobad `comparacion.shape`: debe ser `(3, 2)`. |
| `NameError: name 'pendiente_simple' is not defined` (o `efecto_…`) | No se ejecutó la celda del apartado 3 (o Colab se reinició). | Ejecutad de nuevo desde arriba, o al menos hasta el apartado 3. |
| `KeyError: 'temperatura_c'` en `.params[…]` | Nombre mal escrito dentro de los corchetes. | Mirad los nombres con `ols_control.params.index` (verás `Intercept`, los meses `C(mes)[T.2]`, …, `temperatura_c` y `festivo`). |
| `PatsyError: Error evaluating factor: NameError: name '…' is not defined` | La fórmula tiene un nombre de columna que no existe o un error de escritura. | Revisad la fórmula: `ocupacion_pct`, `temperatura_c`, `festivo` y `C(mes)` tal cual. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_05_paso_3.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 5 →](Reto_Sprint_05_paso_5.md)
<!--/nav-->
