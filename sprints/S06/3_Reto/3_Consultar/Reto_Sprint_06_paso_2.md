# Paso 2 · Inventario de defectos (día 1, 30 minutos)

<!--nav-->
> Sprint 6 · Reto «Datos sucios, cliente impaciente» · paso 2 de 5 · [Ficha del reto](Reto_Sprint_06.md) · [Reto en una página](../1_Trabajar/Reto_Sprint_06_una_pagina.md) · [Paso 3 →](Reto_Sprint_06_paso_3.md)
<!--/nav-->

1. Abrir un cuaderno nuevo en Colab (`reto_S06`), cargar `reservas_sucio.csv` y pasar `resumen_calidad`.
2. Buscar defectos con tablas y gráficos, categoría por categoría.
3. Rellenar **una fila de la tabla del informe por cada defecto** (mínimo 6).
4. Apuntar las preguntas que haríais al cliente.

**Cómo se hace**
- **Cargar el CSV.** Copiad en la primera celda la función `dato(...)` de `S06_02` (descarga el fichero si no está) y usad `crudo = pd.read_csv(dato("reservas_sucio.csv"))`. Guardad siempre esa tabla original **sin tocarla**: se limpia una copia.
- **Mirar el estado de cada columna.** Copiad `resumen_calidad` de `S06_01` o `S06_02` (tipo, nulos, porcentaje de nulos y valores distintos por columna) y mirad también `crudo.shape` y `crudo.describe()`.
- **Buscar por categorías.** Estas son las ocho familias de defecto que debéis revisar (están también en la plantilla del informe):

| Categoría | Cómo se busca | Pista de pandas |
|---|---|---|
| Duplicados | Contar filas repetidas | `crudo.duplicated().sum()` |
| Tipos incorrectos | Ver si una columna numérica o de fecha aparece como texto | `crudo.info()` o la columna `tipo` de `resumen_calidad` |
| Formatos de fecha | Mirar cómo se escriben las columnas de fecha | Ver varias filas y probar `pd.to_datetime(..., format=..., errors="coerce")` |
| Categorías inconsistentes | Listar los valores distintos de las columnas de texto | `crudo[columna].value_counts()` |
| Valores imposibles | Mirar mínimos y máximos de las columnas numéricas | `crudo.describe()`, histogramas y diagramas de caja |
| *Outliers* | Distinguir un valor extremo pero posible de uno imposible | Diagrama de caja; ante la duda, es una pregunta para el cliente |
| Nulos | Ver dónde faltan datos y cuántos: **mirad todas las columnas**, también las de texto como `regimen` | `crudo.isna().sum()` |
| Incoherencias entre columnas | Cruzar columnas que deberían cuadrar | Recalcular una columna a partir de otras y comparar |

- **Rellenar la tabla.** Por cada defecto, una fila de [`informe_calidad_plantilla.md`](../1_Trabajar/plantillas/informe_calidad_plantilla.md). Un ejemplo (inventado) de cómo debe quedar:

| Campo | Ejemplo |
|---|---|
| **Qué** | Fechas de llegada en dos formatos (`2025-07-03` y `03/07/2025`) |
| **Dónde** | Columna `fecha_llegada` |
| **Filas** | 183 de 2.000 |
| **Causa probable** | Dos sistemas de origen exportan con formato distinto |
| **Tratamiento** | Convertir todas a formato ISO |
| **Por qué (y riesgo)** | No se pierde información; el riesgo es confundir día y mes |

- **Preguntas al cliente.** Lo que no podéis decidir solos se apunta como pregunta (por ejemplo: «¿un precio de 0 € es cortesía o un error?»), con lo que haréis mientras tanto. Pista de cuaderno: [`S06_01`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_01_pandas_eda.ipynb) y [`S06_02`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S06/2_Practica/S06_02_limpieza.ipynb).

**Qué deberíais ver.** Un fichero de **1545 filas y 18 columnas**, una tabla de `resumen_calidad` con nulos en **cuatro columnas** (`pais_origen`, `regimen`, `adultos` y `precio_noche`) y alguna columna con un tipo que no es el esperado, y en el informe una tabla con **al menos 6 filas**. La plantilla `informe_calidad_plantilla.md` da una columna para cada cosa: número, defecto, columna(s), filas afectadas, cómo lo detectasteis, causa probable, tratamiento aplicado y por qué (y riesgo). Marcad los tres defectos más graves.

**Hecho cuando:** la tabla tiene 6 o más defectos con sus datos completos y hay al menos una pregunta para el cliente. Si no encontráis más, mirad la «Ayuda 3».

<!--nav-->
---

[← Paso 1](Reto_Sprint_06_paso_1.md) · [Ficha del reto](Reto_Sprint_06.md) · [Paso 3 →](Reto_Sprint_06_paso_3.md)
<!--/nav-->
