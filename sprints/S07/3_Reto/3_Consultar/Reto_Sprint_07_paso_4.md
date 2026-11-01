# Paso 4 · Análisis de sensibilidad (día 2, 5 minutos)

<!--nav-->
> Sprint 7 · Reto «Precio y cancelación» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_07.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_07_una_pagina.md) · [Paso 5 →](Reto_Sprint_07_paso_5.md)
<!--/nav-->

1. Cambiar los costes: ¿y si una noche vacía costara el doble? ¿y si la compensación costara la mitad?
2. Calcular el umbral óptimo y el coste total de cada combinación.
3. Resumir en una tabla y una frase.

**En sencillo.** Los costes del paso 1 son **hipótesis**: nadie en el hotel os ha dado la cifra exacta. Antes de recomendar un umbral, conviene preguntarse: «¿y si me equivoco con el coste?». El análisis de sensibilidad es eso: repetir la búsqueda del umbral con otros costes y ver **cuánto se mueve la decisión**. Si el umbral casi no cambia, la recomendación es sólida; si cambia mucho, hay que decirlo. Es como probar una receta con más o menos sal antes de dársela a los invitados. No hay código nuevo difícil: reutilizáis la función `buscar_umbral` del paso 3 dentro de un bucle.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Análisis de sensibilidad** | Repetir un cálculo cambiando una cifra de partida para ver cuánto cambia el resultado. |
| **Bucle (`for`)** | Repetir un bloque de código una vez por cada elemento de una lista. |
| **Lista de parejas** | Una lista donde cada elemento agrupa varios valores: aquí, el nombre de la hipótesis y sus dos costes. |
| **Umbral óptimo** | El umbral de menor coste para unos costes dados. |
| **`sin_modelo`** | Lo que costaría no hacer nada: todas las cancelaciones reales de *train* multiplicadas por el coste de un FN. |

**Cómo se hace**

1. **Probar varias hipótesis de coste.** Celda nueva. Usa `buscar_umbral`, `COSTE_FN`, `COSTE_FP` y `y_train` del paso 3. Las cuatro combinaciones salen de multiplicar por 2 o por 0,5 una de las dos cifras; podéis añadir las vuestras.

    ```python
    hipotesis = [("la nuestra", COSTE_FN, COSTE_FP),
                 ("FN el doble", COSTE_FN * 2, COSTE_FP),
                 ("FP la mitad", COSTE_FN, COSTE_FP / 2),
                 ("FP el doble", COSTE_FN, COSTE_FP * 2)]
    filas = []
    for nombre, coste_fn, coste_fp in hipotesis:
        umbral, costes = buscar_umbral(coste_fn, coste_fp)
        filas.append({"hipótesis": nombre, "COSTE_FN": coste_fn, "COSTE_FP": coste_fp,
                      "umbral_optimo": umbral, "coste_total": round(min(costes)),
                      "sin_modelo": round(y_train.sum() * coste_fn)})
    sensibilidad = pd.DataFrame(filas)
    print(sensibilidad)
    ```

    Qué hace cada línea:

    - `hipotesis = […]`: una lista de cuatro parejas «nombre, coste de FN, coste de FP». Los dos primeros costes de cada fila son los que se prueban.
    - `for nombre, coste_fn, coste_fp in hipotesis:`: repite lo que hay debajo (con 4 espacios) una vez por hipótesis. **Las líneas de dentro llevan sangría.**
    - `buscar_umbral(coste_fn, coste_fp)`: la función del paso 3. Devuelve el mejor umbral y la lista de costes de cada umbral.
    - `filas.append({…})`: añade una fila (un diccionario) a la lista `filas`. `min(costes)` es el coste del mejor umbral; `round(…)` lo redondea a euros.
    - `y_train.sum() * coste_fn`: el coste de no hacer nada con esa hipótesis.
    - `pd.DataFrame(filas)`: convierte la lista de filas en una tabla.

2. **Dibujar el umbral óptimo (opcional).** Un gráfico también vale. Celda nueva:

    ```python
    sensibilidad.plot.bar(x="hipótesis", y="umbral_optimo", legend=False, rot=0)
    plt.ylabel("Umbral óptimo")
    plt.title("Cómo se mueve el umbral si cambian los costes")
    plt.show()
    ```

    - `sensibilidad.plot.bar(x=…, y=…)`: barras con una por hipótesis; `rot=0` deja los nombres rectos.
    - `plt.ylabel(…)`, `plt.title(…)`: nombre del eje y título. `plt.show()` dibuja.

3. **Escribir la conclusión.** Una frase con este molde y **vuestras cifras**: «Con estos costes recomendamos un umbral de X; si el coste de una falsa alarma sube al doble, el umbral sube a Y». Apuntad también en qué hipótesis cambia más la decisión.

    Una advertencia: `coste_total` de esta tabla es el de las 4800 reservas de *train*, calculado con validación cruzada. **No es comparable** con el coste en test del paso 3 (1200 reservas). Sirve para comparar hipótesis entre sí, no para dar el ahorro.

**Qué deberíais ver.** Una tabla de al menos tres filas (aquí cuatro) y cómo se mueve el umbral óptimo. Con los costes de ejemplo, aproximadamente:

```text
     hipótesis  COSTE_FN  COSTE_FP  umbral_optimo  coste_total  sin_modelo
0   la nuestra       284     103.0           0.25       223121      625652
1  FN el doble       568     103.0           0.15       249011     1251304
2  FP la mitad       284      51.5           0.15       124506      625652
3  FP el doble       284     206.0           0.40       354720      625652
```

- Si FN se encarece, el umbral **baja** (0,25 → 0,15): se avisa más.
- Si FP se abarata, también baja (0,25 → 0,15); si se encarece, **sube** (0,25 → 0,40): se avisa menos.

**Hecho cuando:** la tabla (o el gráfico) está en el cuaderno y tenéis la frase de conclusión escrita.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'buscar_umbral' is not defined` | La celda del umbral del paso 3 no se ha ejecutado. | Ejecutadla antes (de arriba abajo). |
| `NameError: name 'COSTE_FN' is not defined` | La celda del paso 1 no se ha ejecutado. | Ejecutad desde arriba. |
| `IndentationError: expected an indented block after 'for' statement on line 5` (el número de línea puede ser otro) | Las líneas de dentro del `for` no tienen sangría. | Dejad 4 espacios al principio de cada línea del bucle. |
| `TypeError: buscar_umbral() missing 1 required positional argument: 'coste_fp'` | Se llamó a la función con un solo coste. | Pasad los dos: `buscar_umbral(coste_fn, coste_fp)`. |
| Todas las filas dan el mismo umbral | Se usó siempre `COSTE_FN` y `COSTE_FP` en vez de `coste_fn` y `coste_fp` del bucle. | Dentro del bucle, usad los nombres en minúscula. |
| La columna `coste_total` no se parece al coste en test del paso 3 | Son otros datos: aquí, las 4800 reservas de *train* con validación cruzada. | No es un error; usad la tabla para comparar hipótesis, no para dar el ahorro. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_07_paso_3.md) · [Ficha del reto](Reto_Sprint_07.md) · [Paso 5 →](Reto_Sprint_07_paso_5.md)
<!--/nav-->
