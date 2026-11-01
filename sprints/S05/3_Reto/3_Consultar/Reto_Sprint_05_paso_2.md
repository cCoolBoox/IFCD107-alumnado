# Paso 2 · Mirar los datos (día 2, 10 minutos)

<!--nav-->
> Sprint 5 · Reto «¿La ocupación depende de esto?» · paso 2 de 6 · [Ficha del reto](Reto_Sprint_05.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_05_una_pagina.md) · [Paso 3 →](Reto_Sprint_05_paso_3.md)
<!--/nav-->

1. Describir la serie y calcular la media de ocupación por mes.
2. Hacer al menos dos gráficos: ocupación por mes y ocupación frente a temperatura.
3. Escribir 2–3 observaciones con vuestras palabras.

**En sencillo.** Antes de calcular nada hay que **mirar los datos**, igual que se mira un mapa antes de salir de viaje. Este paso no tiene una respuesta «correcta»: sirve para descubrir qué hay (¿cuánto se llena el alojamiento de media?, ¿hay meses más llenos que otros?, ¿se ve alguna relación con el calor?) y para tener algo que contar. Escribís pocas líneas, las ejecutáis y **describís con vuestras palabras lo que veis**.

**Palabras nuevas de este paso**

| Palabra | Qué significa, en sencillo |
|---|---|
| **Media** | La suma de todos los valores dividida entre cuántos son: el valor «típico». |
| **Dispersión** (`std`) | Cuánto se alejan los días de la media. Pequeña: los días se parecen; grande: hay días muy distintos. |
| **Mínimo y máximo** | El día de menor y el de mayor ocupación. |
| **`groupby`** | «Agrupar por»: reparte las filas en montones (uno por mes) y luego calcula algo de cada montón. |
| **Diagrama de caja** (*boxplot*) | Un dibujo por grupo. La caja contiene la mitad central de los días, la raya es la mediana (el valor del medio) y los palitos y puntos son los días más extremos. |
| **Gráfico de dispersión** (*scatter*) | Una nube de puntos: cada punto es un día, con la temperatura a lo ancho y la ocupación a lo alto. |

**Cómo se hace**

1. **Describir la ocupación.** En la celda del apartado «2 · Primer vistazo a los datos» (borrad los `...`) escribid:

    ```python
    print(diaria["ocupacion_pct"].describe())
    ```

    `diaria["ocupacion_pct"]` coge solo esa columna (entre corchetes y comillas, con el nombre exacto) y `.describe()` calcula de golpe la media, la dispersión, el mínimo y el máximo. **Los paréntesis son obligatorios**: sin ellos Python no calcula nada y escribe un texto raro que empieza por `<bound method`.

2. **Media por mes.** En la misma celda, debajo:

    ```python
    medias_mes = diaria.groupby("mes")["ocupacion_pct"].mean()
    print(medias_mes.round(1))
    ```

    Se lee de izquierda a derecha: «coge `diaria`, agrúpala por `mes`, quédate con la columna `ocupacion_pct` y calcula la media de cada grupo». `.round(1)` deja un decimal. Para ver de un vistazo los meses más y menos llenos, probad `print(medias_mes.sort_values())` (ordena de menor a mayor).

3. **Primer gráfico: la ocupación mes a mes.**

    ```python
    diaria.boxplot(column="ocupacion_pct", by="mes", figsize=(8, 4))
    plt.suptitle("")
    plt.title("Ocupación diaria según el mes")
    plt.xlabel("Mes (1 = enero, 12 = diciembre)")
    plt.ylabel("Ocupación (%)")
    plt.show()
    ```

    - `diaria.boxplot(…, by="mes")` dibuja una caja por cada mes; `figsize=(8, 4)` es el tamaño (ancho y alto).
    - `plt.suptitle("")` borra el título automático en inglés que pone la librería.
    - `plt.title(…)`, `plt.xlabel(…)` y `plt.ylabel(…)` ponen el título y los nombres de los ejes **en español y con unidades**. Es lo que pide el cuaderno.
    - `plt.show()` muestra el dibujo. Sin esta línea a veces solo sale un texto como `<Axes: …>`.

4. **Segundo gráfico: ocupación frente a temperatura.** En una celda nueva (botón **+ Código**):

    ```python
    plt.figure(figsize=(6, 4))
    plt.scatter(diaria["temperatura_c"], diaria["ocupacion_pct"], s=8, alpha=0.5)
    plt.title("A más temperatura, menos ocupación")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Ocupación (%)")
    plt.show()
    ```

    `plt.scatter(x, y)` dibuja un punto por día: primero lo que va a lo ancho (la temperatura) y después lo que va a lo alto (la ocupación). `s=8` hace los puntos pequeños y `alpha=0.5` los deja semitransparentes, para que se vea dónde se amontonan. Si dudáis del título, cambiadlo por lo que veáis vosotros.

5. **Escribir las observaciones.** Haced doble clic en la celda de texto «Mis observaciones» y sustituid los puntos por 2–3 frases con vuestras cifras. Pueden seguir estos moldes:

    - «En [meses] la ocupación media es [más alta / más baja]: alrededor del [cifra] %.»
    - «En el gráfico de puntos, a más temperatura [sube / baja] la ocupación.»
    - «Ojo: [el calor y ciertos meses van juntos], así que todavía no sabemos si el calor es la causa.»

    Es la base de vuestra respuesta al cliente, y no hace falta que sea técnica: escribid lo que le diríais a una persona que no ha visto los datos.

**Qué deberíais ver.**
- **El resumen** (`describe`): 1096 días, ocupación media ≈ 68,5 %, dispersión ≈ 9,6, mínimo 47,3 % y máximo 96,8 %.
- **Las medias por mes:** más altas en invierno (en torno al 78–79 % de media en enero, febrero y diciembre) y más bajas de mayo a octubre (en torno al 60–63 %).
- **El diagrama de caja:** cajas altas a los lados (invierno) y bajas en el centro (verano).
- **La nube de puntos:** **baja de izquierda a derecha**: a más temperatura, menos ocupación.

No hay `assert` en este paso: lo revisa el equipo.

**Hecho cuando:** hay dos gráficos con título y ejes en español y 2–3 observaciones escritas.

## Si algo falla

| Veis… | Qué significa | Qué hacer |
|---|---|---|
| `NameError: name 'diaria' is not defined` | La celda del apartado 1 no se ha ejecutado (o Colab se reinició). | Ejecutad desde la primera celda hacia abajo hasta la del apartado 1 y volved aquí. |
| `KeyError: 'ocupacion'` (con otro nombre) | El nombre de la columna no es exacto. | Escribid `diaria.columns` para ver los nombres: `fecha`, `ocupacion_pct`, `temperatura_c`, `festivo`, `precio_medio` y `mes`. |
| Sale `<bound method NDFrame.describe of …>` y muchas líneas | Falta el paréntesis: `describe` en vez de `describe()`. | Añadid `()` al final. |
| El gráfico sale con un título en inglés (*Boxplot grouped by mes*) | Falta `plt.suptitle("")`. | Añadid esa línea antes de `plt.title(…)`. |
| Sale un texto como `<Axes: …>` en vez del dibujo | Falta `plt.show()`. | Añadid `plt.show()` al final de la celda del gráfico. |
| Los dos gráficos salen uno encima del otro | Están en la misma celda sin `plt.figure(…)` entre ellos. | Poned cada gráfico en su celda, o empezad el segundo con `plt.figure(figsize=(6, 4))`. |

<!--nav-->
---

[← Paso 1](Reto_Sprint_05_paso_1.md) · [Ficha del reto](Reto_Sprint_05.md) · [Paso 3 →](Reto_Sprint_05_paso_3.md)
<!--/nav-->
