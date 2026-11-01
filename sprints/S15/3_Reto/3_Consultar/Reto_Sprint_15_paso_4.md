# Paso 4 · Elegir el candidato sin tocar el test (día 3, 70 minutos)

<!--nav-->
> Sprint 15 · Reto «El mejor modelo, demostrado» · paso 4 de 5 · [Ficha del reto](Reto_Sprint_15.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_15_una_pagina.md) · [Paso 5 →](Reto_Sprint_15_paso_5.md)
<!--/nav-->

1. Calcular media ± desviación de cada modelo.
2. Comparar teniendo en cuenta la incertidumbre y añadir coste y complejidad.
3. Elegir el candidato y escribir la justificación de una página.

**En sencillo.** Ya tenéis un montón de pruebas apuntadas; hoy toca **elegir cuál os lleváis**, sin mirar el test. No gana siempre el que tiene el número más alto: si dos modelos van casi igual, la diferencia puede ser **ruido** (casualidad del reparto), y entonces conviene el más simple, el más rápido o el más fácil de explicar. Es como elegir coche: dos modelos con casi el mismo consumo, pero uno es mucho más barato de mantener. El código es corto: ordenar la tabla del registro y comparar. Lo difícil y valioso es **escribir por qué**.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Media ± desviación** | Resultado medio de las 5 pruebas de la validación cruzada y cuánto se separan entre sí. `0,755 ± 0,012` significa «0,755, con un margen de ≈ 0,012». |
| **Solapar / ruido** | Dos modelos se solapan si la diferencia entre sus medias es **menor que su desviación**: no se puede afirmar que uno sea mejor. |
| **Candidato** | El modelo que elegís para evaluar en el test y llevar al demostrador. |
| **Explicabilidad** | Lo fácil que es contar por qué el modelo decide lo que decide. |
| **Coste y complejidad** | Tiempo de entrenamiento y lo difícil que es mantenerlo o explicarlo. |
| **Justificación** | Una página que cuenta qué modelo elegís y por qué, para que lo entienda quien no programa. |

**Cómo se hace**

1. **La tabla ordenada (15 minutos, con los puntos 2 y 3).** En `03_modelos.ipynb`, una celda nueva, tras *Reiniciar y ejecutar todo* para tener el registro completo. Quitad las pruebas con fuga:

    ```python
    tabla = pd.read_csv(RUTA_REGISTRO)
    legitimos = tabla[~tabla["modelo"].str.contains("Fuga")]
    ordenada = legitimos.sort_values("valor_cv", ascending=False)[["id", "responsable", "modelo", "valor_cv", "desv_cv", "tiempo_s"]]
    print(ordenada.to_string(index=False))
    ```

    - `legitimos` conserva las filas cuyo nombre **no** contiene «Fuga» (la `~` significa «no»).
    - `sort_values("valor_cv", ascending=False)` ordena de mayor a menor. **Si vuestra métrica es un error (MAE), el mejor es el menor: usad `ascending=True`.**
    - Muestra una fila por prueba con quién la hizo, el modelo, la media, la desviación y el tiempo.

2. **Ver si la diferencia es ruido.** Esta función aplica la regla del solape, y el bucle compara cada modelo con el mejor:

    ```python
    def parecen_iguales(a, b):
        return abs(a["valor_cv"] - b["valor_cv"]) < max(a["desv_cv"], b["desv_cv"])

    mejor = legitimos.loc[legitimos["valor_cv"].idxmax()]
    for _, fila in legitimos.iterrows():
        if fila["modelo"] != mejor["modelo"]:
            print(fila["modelo"], "→ ¿diferencia dentro del ruido?", parecen_iguales(mejor, fila))
    ```

    - `parecen_iguales` devuelve `True` si la diferencia de medias es menor que la mayor de las dos desviaciones.
    - `idxmax()` da la fila con la mayor media (con MAE, usad `idxmin()`). Cada línea impresa dice si ese modelo está dentro del ruido del mejor. **Es una regla práctica, no una prueba estadística.**

    Con las pruebas de ejemplo (datos de práctica) el mejor es la regresión logística (0,755 ± 0,012): el *baseline*, el bosque sin ajustar, el boosting y el bosque de profundidad 3 salen `False` (hay diferencia clara) y el bosque de profundidad 6 y 10 y la red neuronal salen `True` (**solapan**: la diferencia puede ser ruido).

3. **(Opcional) Un gráfico de la comparación.** Con barras de error de un vistazo:

    ```python
    import matplotlib.pyplot as plt

    t = legitimos.sort_values("valor_cv")
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.barh(t["modelo"], t["valor_cv"], xerr=t["desv_cv"], color="tab:blue", capsize=4)
    ax.axvline(0.5, color="gray", linestyle="--", label="Azar (AUC 0,5)")
    ax.set_xlim(0.4, 0.85)
    ax.set_xlabel("AUC medio en validación cruzada (± desviación)")
    ax.set_title("Comparativa de modelos (validación cruzada, sin usar el test)")
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.show()
    ```

    Sale una barra horizontal por modelo con un «bigote» que marca su desviación y una línea discontinua en 0,5 (el azar). Si los bigotes de dos barras se solapan, esos modelos son indistinguibles. Con un MAE, quitad la línea del azar y el `set_xlim`.

4. **Coste y complejidad (15 minutos).** Añadid a la comparación: el **tiempo de entrenamiento** (`tiempo_s`), lo difícil que es **mantener** el modelo y lo fácil que es **explicar** su decisión (por ejemplo, la regresión logística tiene un peso por variable que se puede leer; una red neuronal es más difícil de explicar). Escribidlo en una tabla de cuatro columnas en la justificación (el punto 6).

5. **Elegir (15 minutos).** Reglas: se elige con la **validación**, **no se mira el test**; si dos modelos van casi igual, **elegid el más simple y explicadlo**. Una frase del tipo: «Elegimos la regresión logística (0,755 ± 0,012) frente al bosque de profundidad 6 (0,745 ± 0,013): la diferencia puede ser ruido y la logística es mucho más rápida y fácil de explicar» (es el ejemplo con datos de práctica).

6. **Escribir `justificacion_candidato.md` (25 minutos).** En `sprint-15` de GitHub: *Add file → Create new file*, nombre `justificacion_candidato.md`. Una página con esta tabla, rellenada con **vuestras cifras**, y unas líneas debajo que digan por qué gana:

    | Modelo | Métrica (media ± desv.) | Tiempo | Explicabilidad | Comentario |
    |---|---|---|---|---|
    | Baseline | 0,500 ± 0,000 | ≈ 0,1 s | — | Azar: no mira las pistas |
    | Regresión logística | 0,755 ± 0,012 | ≈ 0,1 s | Alta: cada variable tiene un peso | **Candidata** |
    | Bosque (profundidad 6) | 0,745 ± 0,013 | ≈ 2 s | Media | Solapa con la logística: puede ser ruido |
    | Red neuronal (MLP) | 0,738 ± 0,019 | ≈ 1 s | Baja | Solapa con la logística; más difícil de explicar |

    Debajo, 3–5 líneas con: qué modelo elegís, **si la diferencia con el siguiente puede ser ruido**, el coste y el beneficio, y qué no sabéis. Dejad ya un hueco para el resultado en test y para la «Revisión con la rúbrica» del paso 5. Si vais a por el nivel extra, añadid una **hipótesis de por qué gana**: por ejemplo, «los datos tienen relaciones no lineales entre antelación y canal que un árbol captura mejor que una regresión» (ejemplo de redacción; la vuestra se contrasta con la explicación del paso 5).

**Qué deberíais ver.** Una tabla ordenada con una fila por prueba legítima, un candidato elegido y una frase del tipo «Elegimos X (0,71 ± 0,02) frente a Y (0,72 ± 0,04): la diferencia puede ser ruido y X es mucho más rápido» (cifras de ejemplo). Y `justificacion_candidato.md` en `sprint-15`.

**Hecho cuando:** `justificacion_candidato.md` tiene la tabla comparativa y el candidato razonado, y nadie ha mirado el test.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'RUTA_REGISTRO' is not defined` | Colab se reinició y las celdas comunes no se ejecutaron. | *Reiniciar y ejecutar todo*; así se rehace el registro. |
| `KeyError: 'valor_cv'` | El nombre de la columna está mal escrito, o la tabla no es el registro. | Escribid `tabla.columns` y comprobad que salen las doce columnas. |
| La fila `LogisticaConFuga` sale la primera | Falta el filtro `legitimos` o se ha usado `tabla` en vez de `legitimos`. | Usad `legitimos` en todas las líneas siguientes. |
| El «mejor» tiene la métrica más baja | Con un error (MAE) el mejor es el menor. | Cambiad `ascending=True` y `idxmin()`. |
| Dos modelos empatan | Es normal cuando solapan. | Elegid el más simple, rápido o fácil de explicar, y escribidlo. |
| Alguien ha mirado el test para decidir | El test deja de ser una prueba limpia. | Decidid solo con validación, anotadlo en la justificación y no volváis a elegir con él. |

<!--nav-->
---

[← Paso 3](Reto_Sprint_15_paso_3.md) · [Ficha del reto](Reto_Sprint_15.md) · [Paso 5 →](Reto_Sprint_15_paso_5.md)
<!--/nav-->
