# Paso 3 · Función de limpieza y partición train/test (día 2, 15 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 3 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md) · [Paso 4 →](Reto_Sprint_06_paso_4.md)
<!--/nav-->

1. Escribir `limpiar_reservas(df)`: una función con docstring que aplica **todos** vuestros tratamientos.
2. Comprobar el antes y el después.
3. Separar *train* y *test*.

**Cómo se hace**
- **La función.** Recibe la tabla sucia y devuelve **dos cosas**: la tabla limpia y un resumen de lo que ha cambiado (por ejemplo, un diccionario con filas antes y después, duplicados quitados y nulos nuevos). Empezad por la función del mini-reto de `S06_02` y adaptadla a los defectos de vuestra tabla. Trabaja sobre una **copia** (`crudo.copy()`): el original no se modifica.
- **Reglas fijas, no estadísticas.** La función solo aplica reglas que no dependen de los datos (convertir tipos, unificar categorías, marcar como nulo lo imposible). **No calcula medias, medianas ni categorías frecuentes**: eso se aprende en el *pipeline* del paso 4, solo con *train*.
- **Ninguna fila se pierde sin avisar.** Cada fila que eliminéis (por ejemplo, un duplicado) se cuenta y se justifica en el informe. Un valor imposible se convierte en nulo en lugar de borrar la fila entera.
- **Antes y después.** Haced una tabla pequeña con filas, duplicados, nulos por columna y valores distintos de las categorías antes y después. Si una corrección no se nota, no sirve. Es el apartado 3 del informe.
- **Partición.** Con la tabla limpia, `train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)`, donde `y` es la columna `cancelada`. Decidid qué columnas entran en `X`: pregunta para cada una, «¿se conoce **al reservar**?». Un identificador como `id_reserva` no sirve para predecir. Pista de cuaderno: [`S06_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_02_limpieza.ipynb) (mini-reto) y [`S06_03`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_03_preprocesado_pipeline.ipynb) (partición).

**Qué deberíais ver.** La tabla limpia sin duplicados exactos (con el CSV del curso, **1545 filas antes y 1500 después**), con las fechas como fechas, los valores de `canal` y `pais_origen` unificados y los valores imposibles convertidos en nulos; el resumen de cambios; y dos tablas, *train* y *test*, con la misma proporción de reservas canceladas.

**Hecho cuando:** `limpiar_reservas(crudo)` devuelve la tabla limpia y el resumen sin cambiar `crudo`, y *train* y *test* están separados antes de calcular nada que se aprenda de los datos.

<!--nav-->
---

[← Paso 2](Reto_Sprint_06_paso_2.md) · [Ficha del reto](Reto_Sprint_06.md) · [Paso 4 →](Reto_Sprint_06_paso_4.md)
<!--/nav-->
