# Solucionario del reto · Sprint 6 · «Datos sucios, cliente impaciente»

> **Para contrastar y para entender**, no solo para copiar. El **código** de cada paso ya está en su [página del reto](../Reto_Sprint_06_paso_2.md) (con «Qué hace cada línea»). Aquí está lo que **no** está allí: las cifras para comprobar y las respuestas de ejemplo de las partes que se escriben con palabras propias. Volver a la [ficha del reto](../Reto_Sprint_06.md).

## Índice

- [Cómo usarlo](#cómo-usarlo)
- [Las cifras que tienen que salir](#las-cifras-que-tienen-que-salir)
- [Paso 1 · Planning y roles](#paso-1--planning-y-roles)
- [Paso 2 · Inventario de defectos: la tabla completa](#paso-2--inventario-de-defectos-la-tabla-completa)
- [Paso 3 · Función de limpieza y partición](#paso-3--función-de-limpieza-y-partición)
- [Paso 4 · Pipeline y baseline](#paso-4--pipeline-y-baseline)
- [Paso 5 · Informe: respuestas de ejemplo](#paso-5--informe-respuestas-de-ejemplo)
- [Entrega de referencia: los tres ficheros resueltos](#entrega-de-referencia-los-tres-ficheros-resueltos)

## Cómo usarlo

- **Primero intentadlo.** Si algo falla: leed el error → «Si algo falla» de la página del paso → equipo → docente → **este solucionario**.
- **Después de mirarlo, cerradlo y volved a escribirlo con vuestras palabras.** La prueba de que lo sabéis es explicárselo a otra persona del equipo.
- En la review, el docente puede preguntar por cualquier línea o cualquier fila de la tabla.

## Las cifras que tienen que salir

| Dónde | Cifra | Qué es |
|---|---|---|
| Paso 2 | `(1545, 18)` · `id_reserva` con 1500 valores distintos | 1545 filas, de las que 45 son repetidas |
| Paso 2 | duplicados `45` · precios con coma `153` | Defectos de formato y repetición |
| Paso 2 | fechas ISO `1391` · dd/mm/aaaa `154` · sin leer `0` | Dos sistemas de origen |
| Paso 2 | `canal` 9 valores · `pais_origen` 12 valores | Mismo dato escrito de varias formas |
| Paso 2 | precios ≤ 0: `4` · > 1000: `4` · noches ≤ 0: `6` · antelaciones negativas: `5` | Valores imposibles |
| Paso 3 | `filas_antes 1545` · `duplicados_quitados 45` · `imposibles_a_nulo 14` · `antelaciones_recalculadas 5` · `filas_despues 1500` | El `resumen` de `limpiar_reservas` |
| Paso 3 | `(1200, 15)` y `(300, 15)` · `0.471` y `0.47` | *Train* y *test*, con la misma proporción de canceladas |
| Paso 4 | `(1200, 15) → (1200, 34)` | Columnas antes y después del preprocesado |
| Paso 4 | modelo tonto AUC `0.500 ± 0.000` · logística `0.758 ± 0.025` | Validación cruzada de 5 particiones |

## Paso 1 · Planning y roles

- No hay código ni respuesta única. Un reparto de ejemplo está en la [página del paso](../Reto_Sprint_06_paso_1.md).
- Lo que se revisa: que los roles no repiten respecto al sprint anterior, que hay **una persona responsable por tarjeta** y que el nivel está anotado.

## Paso 2 · Inventario de defectos: la tabla completa

Se piden **6 o más**. Estos son los **12** que tiene el fichero (el mínimo es elegir 6; los extra son nivel extra).

| Nº | Defecto | Columna(s) | Filas | Cómo se detecta | Causa probable | Tratamiento y riesgo |
|---|---|---|---|---|---|---|
| 1 | Filas duplicadas exactas | todas | 45 | `crudo.duplicated().sum()` | Exportación repetida o doble envío | `drop_duplicates()`. Riesgo bajo: son idénticas en todo |
| 2 | Fechas en dos formatos | `fecha_reserva` | 154 | `.str.contains("/").sum()` | Dos sistemas de origen | Leer cada formato por separado y unir. Riesgo: confundir día y mes (se comprueba con el rango de fechas) |
| 3 | Precio con coma decimal | `precio_noche` | 153 | `.astype(str).str.contains(",").sum()` | Exportación de Excel con configuración española | Cambiar la coma por punto y pasar a número |
| 4 | Precio imposible (≤ 0 o 9999) | `precio_noche` | 8 | `describe()` y filtros `≤ 0` / `> 1000` | Valores centinela o errores de carga | A nulo (no se borra la fila). Riesgo: un 9999 podría ser un precio real raro → pregunta al cliente |
| 5 | Noches imposibles (≤ 0) | `noches` | 6 | `(crudo["noches"] <= 0).sum()` | Error de carga | A nulo; lo imputa el *pipeline* |
| 6 | Antelación negativa (−3) | `antelacion_dias` | 5 | `(crudo["antelacion_dias"] < 0).sum()` y comparar con las fechas | Incoherente con las fechas | Recalcular desde `fecha_llegada − fecha_reserva` |
| 7 | Variantes de canal | `canal` | 135 | `value_counts()`: 9 valores donde debería haber 4 | Texto libre (mayúsculas, espacios) | `strip().lower()` y espacio → `_` |
| 8 | Variantes de país | `pais_origen` | 94 | `value_counts()`: 12 valores donde debería haber 8 | Texto libre (`es`, `España`, `Reino Unido`…) | Diccionario de equivalencias. Riesgo: un país no previsto pasa a nulo |
| 9 | Nulos en `pais_origen` | `pais_origen` | 115 | `isna().sum()` | Campo opcional | No se rellena en la limpieza; lo hace el *pipeline* (más frecuente) |
| 10 | Nulos en `regimen` | `regimen` | 61 | `isna().sum()` | Campo no obligatorio | *Pipeline* (más frecuente) |
| 11 | Nulos en `adultos` | `adultos` | 46 | `isna().sum()` | Falta el dato; explica el tipo `float` | *Pipeline* (mediana) |
| 12 | Nulos en `precio_noche` | `precio_noche` | 84 | `isna().sum()` | Falta el dato | *Pipeline* (mediana) |

- **Antes de tratar nada**, una celda de `describe()` ya enseña el 4 (mínimo `−50.0`, máximo `9999.0`) y el 5.
- **Error frecuente:** tratar un precio alto como imposible sin más. Un valor extremo pero posible es un *outlier*: se pregunta, no se borra.

## Paso 3 · Función de limpieza y partición

- El código completo es el de la [página del paso](../Reto_Sprint_06_paso_3.md). Lo que se comprueba:
  - `crudo.shape` sigue en `(1545, 18)` después de limpiar: la función **no toca** el original.
  - `limpia.shape` es `(1500, 19)`: 45 filas menos y una columna más (`mes_llegada`).
  - Antes y después: duplicados `45 → 0`, valores de `canal` `9 → 4`, de país `12 → 8`.
  - Fechas de reserva entre `2024-01-01` y `2025-12-30`: otro rango sería señal de día y mes cambiados.
- **Por qué `train` y `test` se separan ya:** lo que se aprende de los datos (medianas, escalas) debe calcularse **solo con *train***. La limpieza usa reglas fijas (precio entre 20 y 1000, noches entre 1 y 60) que no dependen de los datos, y por eso puede ir antes.

## Paso 4 · Pipeline y baseline

| Qué | Dónde va | Por qué |
|---|---|---|
| Quitar duplicados, normalizar texto, pasar imposibles a nulo | **Antes** (`limpiar_reservas`) | Reglas fijas: no aprenden nada de los datos |
| Imputar (mediana en números, más frecuente en texto) | **Dentro** del *pipeline* | La mediana se calcula solo con *train* |
| Escalar los números | **Dentro** | Media y desviación solo de *train* |
| Codificar las categorías (one-hot) | **Dentro** | Evita errores con categorías nuevas |

- Frase de ejemplo para el informe: «El modelo de regresión logística obtiene un AUC de 0,758 ± 0,025 en validación cruzada frente a 0,500 del modelo tonto: aprende algo real, pero no es un modelo para decidir solo.»
- Si vuestro modelo no supera a 0,500, mirad la «Ayuda 2» de la ficha del reto.

## Paso 5 · Informe: respuestas de ejemplo

**1. Resumen para el gerente (5 líneas)**

- «El fichero tiene 1545 filas, de las que 45 están repetidas: quedan **1500 reservas distintas**.»
- «Lo más grave: 154 fechas en otro formato y 153 precios con coma, que habrían dado errores o cifras falsas.»
- «Hay 14 valores imposibles (precios y noches) que se han pasado a nulo, y 5 antelaciones que no cuadraban con las fechas.»
- «Tras la limpieza se puede construir un primer modelo (AUC 0,76), mejor que el azar.»
- «Necesitamos que nos confirméis tres cosas (ver preguntas).»

**5. Preguntas al cliente (3 o más)**

- ¿Por qué hay precios con coma? ¿Los exporta un sistema con configuración española?
- El precio `9999` y el precio negativo: ¿son «sin dato» o un error de carga?
- ¿Qué pasa con el país cuando reserva una agencia? ¿Es el del cliente o el de la agencia?
- ¿Una reserva duplicada es un doble envío o dos reservas distintas del mismo cliente?

**6. IA responsable (ejemplo)**

- **Riesgo específico:** el país de origen entra en el modelo. En el fichero, por ejemplo, IT cancela un 60 % (77 reservas), NL un 37 % (75) y ES un 45 % (388): son pocas reservas por país y el modelo podría tratar peor a un grupo.
- **Medidas:** no usar el modelo para denegar reservas ni para cobrar más por país; revisar la tasa de aviso por país; imputar el país ausente con la categoría más frecuente **solo con *train***.
- **Qué se pidió a la IA y qué se revisó:** decirlo en una frase concreta (por ejemplo: «pedimos el diccionario de países; comprobamos con `value_counts()` que no dejaba valores nulos nuevos y añadimos `Reino Unido`»).

## Entrega de referencia: los tres ficheros resueltos

Son los tres ficheros que se suben a `sprint-06/`, ya hechos, con el nivel extra completo. Úsalos **después** de intentarlo, para contrastar, no para copiar.

| Fichero | Qué es |
|---|---|
| [`informe_calidad.md`](informe_calidad.md) | Informe con los 7 apartados, 10 defectos, preguntas al cliente, IA responsable, extras y la revisión con la rúbrica |
| [`reto_S06.ipynb`](reto_S06.ipynb) | Cuaderno completo: inventario, `limpiar_reservas`, partición, *pipeline*, *baseline*, IA responsable y extras. Se abre en Colab con *Archivo → Subir cuaderno* |
| [`README.md`](README.md) | Cómo ejecutarlo, versiones, quién hizo qué y uso de la IA |

- Las partes de «versiones», «quién hizo qué» y «uso de la IA» son **de ejemplo**: cada equipo cuenta lo que hizo de verdad.
- Las cifras de control son las de la tabla de arriba: 1545 → 1500 filas y AUC 0,758 ± 0,025 frente a 0,500 del modelo tonto.
