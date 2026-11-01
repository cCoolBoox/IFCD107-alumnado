# Paso 5 · Go / no-go, EDA, calidad del dato y baseline (día 2, 200 minutos)

<!--nav-->
> Sprint 14 · Reto «Proyecto final: definir, tener datos y un punto de partida» · paso 5 de 7 · [Ficha del reto](Reto_Sprint_14.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_14_una_pagina.md) · [Paso 6 →](Reto_Sprint_14_paso_6.md)
<!--/nav-->

1. Leer el *go / no-go* del docente y corregir la ficha si hace falta.
2. Hacer el EDA y el informe de calidad del dato en `01_eda.ipynb`.
3. Fijar la partición de los datos y la métrica técnica **antes** de mirar resultados.
4. Construir el baseline en `02_baseline.ipynb` y calcular su métrica.

**Cómo se hace.** Reparto sugerido de los 200 minutos:

| Bloque | Qué hacéis | Minutos |
|---|---|---|
| 5.1 | Leer el *go / no-go* y corregir la ficha | 20 |
| 5.2 | EDA e informe de calidad | 90 |
| 5.3 | Partición y métrica | 20 |
| 5.4 | Baseline y subida de los cuadernos | 70 |

## 5.1 · El go / no-go (20 minutos)

Hay tres respuestas posibles: **GO** (adelante), **GO con cambios** o **NO-GO** (hay que cambiar el enfoque). Un *no-go* o un cambio es **normal**: corregid la ficha ese mismo día, subid la versión 2 a `sprint-14/` con otro mensaje de *commit* y seguid. Si el docente cambia el alcance, apuntadlo en la ficha.

## 5.2 · EDA e informe de calidad (90 minutos)

En Colab, abrid un cuaderno nuevo y guardadlo como `01_eda.ipynb`. La primera celda carga los datos con el enlace o el script del plan de datos. Después, un EDA con estas preguntas:

| Orden | Qué miráis | Qué escribís |
|---|---|---|
| 1 | Qué trae el conjunto: filas, columnas, periodo y tipos | Una tabla o un resumen de tres líneas |
| 2 | **Nulos** y **duplicados** | Cuántos hay y qué hacéis con ellos |
| 3 | **Valores raros** (imposibles o muy extremos) | Qué son y si los quitáis o los dejáis, y por qué |
| 4 | **Sesgo de muestreo**: ¿quién o qué falta en los datos? | Una frase, por ejemplo «solo hay hoteles grandes» |
| 5 | Tres gráficos o tablas que respondan a **vuestra pregunta** | Un título y una frase de conclusión por gráfico |
| 6 | **Fugas posibles**: variables que no se conocen en el momento de decidir | Cuáles hay y si se descartan |

En el brief 2 mirad cuántas imágenes hay por clase; en el brief 3, cuántos documentos hay y cómo de largos son. Terminad con el **informe de calidad del dato**: rellenad el apartado 3 de `plan_datos_licencias.md` (hallazgo y acción tomada, uno por fila) y el apartado 4 (**linaje**: de dónde viene el dato y qué le habéis hecho). Elegid **un hallazgo que cambie el enfoque** para contarlo en la review.

## 5.3 · Partición y métrica (20 minutos)

Antes de ejecutar ningún modelo, escribid en el apartado 5 de `plan_datos_licencias.md` y en el apartado 5 de la ficha:
- **Cómo partís los datos:** si hay series de tiempo, **por fechas** (entrenar con el pasado y evaluar con el futuro); si no, aleatoria y estratificada. Y por qué así se evitan las fugas.
- **Qué tamaño tiene cada parte:** entrenamiento, validación y test. **El test no se toca hasta el final del proyecto.**
- **La métrica técnica** (por ejemplo MAE, MAPE, F1 o aciertos sobre 40 preguntas) y el umbral de éxito.

## 5.4 · Baseline (70 minutos)

Abrid `02_baseline.ipynb`. Construid el **modelo más simple posible**: «predecir lo mismo que ayer o que el año anterior», la media, la clase más frecuente o una búsqueda por palabras clave. Calculad su métrica sobre la **validación** y dejad escrita una frase: «Nuestro baseline tiene [métrica] de [valor]». Es el **suelo** que intentaréis superar en los sprints siguientes; no lo compliquéis. Después, en cada cuaderno, *Entorno de ejecución → Reiniciar y ejecutar todo*, *Archivo → Descargar → Descargar .ipynb* y subid el fichero a `sprint-14/` (cada cuaderno, una persona distinta).

**Qué deberíais ver.** La ficha con el *go* (o corregida), un `01_eda.ipynb` que termina con la tabla de calidad, la partición y la métrica escritas, y un `02_baseline.ipynb` que acaba con un número.

**Hecho cuando:** los dos cuadernos se ejecutan de arriba abajo sin errores, la métrica y la partición están escritas antes del baseline y los cuadernos están en `sprint-14/`.

<!--nav-->
---

[← Paso 4](Reto_Sprint_14_paso_4.md) · [Ficha del reto](Reto_Sprint_14.md) · [Paso 6 →](Reto_Sprint_14_paso_6.md)
<!--/nav-->
