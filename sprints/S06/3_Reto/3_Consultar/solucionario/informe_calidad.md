# Informe de calidad del dato · reservas_sucio.csv

**Equipo:** referencia del docente · **Fecha:** 10/11/2026 · **Versión de los datos:** reservas_sucio.csv (nº de filas: 1545, columnas: 18)

## 1. Resumen para el gerente (máx. 5 líneas)
- El fichero **no se puede usar tal cual**: 1 de cada 3 filas (506 de 1545) tiene algún error de formato o de valor, y 1 de cada 5 tiene huecos en datos importantes.
- Lo más grave: **precios imposibles** (0, −50 y 9999 €), **fechas escritas de dos formas** y **45 reservas repetidas**.
- Todo se corrige con una función que se ejecuta siempre igual y no toca el fichero original: quedan 1500 reservas.
- Con los datos limpios, un primer modelo acierta bastante más que adivinar (AUC 0,76 frente a 0,50), así que merece la pena seguir.

## 2. Tabla de defectos

Los tres más graves van en **negrita**.

| Nº | Defecto | Columna(s) | Filas afectadas | Cómo lo detectamos | Causa probable | Tratamiento aplicado | Por qué (y riesgo) |
|---|---|---|---|---|---|---|---|
| 1 | **Precios imposibles** (0, −50 y 9999) | `precio_noche` | 8 | `describe()` (mínimo −50, máximo 9999) y filtros `≤ 0` / `> 1000` | Valores centinela o errores de carga | Pasar a nulo (no se borra la fila); lo imputa el *pipeline* con la mediana | Un solo 9999 distorsiona medias y escalado. Riesgo: un precio muy alto podría ser real, hay que preguntarlo |
| 2 | **Fechas en dos formatos** (`2025-11-09` y `19/11/2024`) | `fecha_reserva` | 154 | `.str.contains("/").sum()` y lectura por formato (0 sin leer) | Dos sistemas de origen | Leer cada formato por separado y unir | Si se mezclan, la antelación sale mal sin avisar. Riesgo: confundir día y mes (se comprueba con el rango 2024-01-01 a 2025-12-30) |
| 3 | **Filas duplicadas exactas** | todas | 45 | `crudo.duplicated().sum()` | Exportación repetida o doble envío | `drop_duplicates()` | Una reserva repetida podría caer en *train* y en *test* a la vez. Riesgo bajo: son idénticas en todo |
| 4 | Precio con coma decimal (`93,5`) | `precio_noche` | 153 | `.astype(str).str.contains(",").sum()` | Excel con configuración regional española | Cambiar la coma por punto y pasar a número | Sin esto la columna entera es texto. Riesgo: ninguno si se hace antes de filtrar |
| 5 | Noches imposibles (0 y −2) | `noches` | 6 | `(crudo["noches"] <= 0).sum()` | Error de carga | Pasar a nulo; lo imputa el *pipeline* | No se inventa un valor en la limpieza |
| 6 | Antelación negativa (−3) | `antelacion_dias` | 5 | `(crudo["antelacion_dias"] < 0).sum()` y comparar con las fechas | Incoherente con las fechas | Recalcular como `fecha_llegada − fecha_reserva` | Las 5 se corrigen con un dato fiable |
| 7 | Variantes de canal (`WEB_INTERMEDIARIA`, `Web Intermediaria`, `directo`…) | `canal` | 135 | `value_counts()`: 9 valores donde debería haber 4 | Texto libre | Minúsculas, quitar espacios y `_` | Sin esto el modelo ve 9 canales en vez de 4 |
| 8 | Variantes de país (`es`, `España`, `uk`, `Reino Unido`) | `pais_origen` | 94 | `value_counts()`: 12 valores donde debería haber 8 | Texto libre | Diccionario de equivalencias | Riesgo: un país no previsto pasaría a nulo (comprobado: no ocurre) |
| 9 | Nulos en país, régimen y adultos | `pais_origen`, `regimen`, `adultos` | 115 · 61 · 46 | `isna().sum()` | Campos opcionales; explica que `adultos` sea decimal | No se rellenan en la limpieza: el *pipeline* usa la más frecuente (texto) o la mediana (número) | Imputar antes de partir sería fuga de datos |
| 10 | Nulos en precio | `precio_noche` | 84 | `isna().sum()` | Falta el dato | *Pipeline* con la mediana | Tras la limpieza suben a 87 por los precios imposibles pasados a nulo |

Total de filas con algún defecto de formato o de valor (sin contar los nulos): **506 de 1545 (32,8 %)**; con los nulos: 705 (45,6 %).

## 3. Antes y después

| | Antes | Después |
|---|---|---|
| Filas | 1545 | 1500 |
| Duplicados | 45 | 0 |
| Valores distintos de `canal` | 9 | 4 |
| Valores distintos de `pais_origen` | 12 | 8 |
| Nulos en `noches` | 0 | 6 |
| Nulos en `precio_noche` | 84 | 87 |
| Nulos en `regimen` | 61 | 59 |
| Nulos en `pais_origen` | 115 | 112 |
| Nulos en `adultos` | 46 | 46 |

- **Resumen de `limpiar_reservas`:** 45 duplicados quitados, 14 valores imposibles pasados a nulo, 5 antelaciones recalculadas, 1545 → 1500 filas.
- Los nulos cambian porque los duplicados que se quitan tenían huecos y porque los valores imposibles pasan a nulo. La única fila que desaparece es una repetida, y todas están contadas.

## 4. Pipeline y modelo de referencia
- **Columnas numéricas (9):** `antelacion_dias`, `noches`, `adultos`, `ninos`, `precio_noche`, `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`, `mes_llegada`. **De texto (6):** `tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito`. Fuera: `id_reserva` (es un identificador) y las fechas.
- **Antes (reglas fijas, en `limpiar_reservas`):** duplicados, formatos, categorías, valores imposibles a nulo y antelación recalculada. No calcula nada a partir de los datos.
- **Dentro del *pipeline* (solo con *train*):** mediana y escalado en los números; categoría más frecuente y *one-hot* en el texto. De 15 a 34 columnas.
- **Partición:** 1200 filas de *train* y 300 de *test*, con la misma proporción de canceladas (0,47).
- **Resultado (validación cruzada de 5 particiones, métrica AUC):** regresión logística **0,758 ± 0,025** frente a **0,500 ± 0,000** del modelo tonto. Eso significa que el modelo ordena las reservas por riesgo de cancelación mucho mejor que el azar. En *test*, mirado una sola vez: 0,752.

## 5. Preguntas para el cliente
1. ¿Un precio de **0 €** significa «gratis» (cortesía) o «sin dato»? Mientras no respondan, lo tratamos como dato que falta.
2. ¿Qué es el **9999**? ¿Un código de «sin precio» o una tarifa real? Lo tratamos como error.
3. ¿Por qué hay precios con coma y fechas de dos formas? ¿Cuántos sistemas exportan y se puede unificar el formato en origen?
4. ¿El país vacío es «no se sabe» o «no aplica» (reserva de empresa o agencia)? Mientras tanto, no usamos el país en el modelo.

## 6. IA responsable
- **Si el país se imputa mal.** Faltan 112 países (7,5 %). El imputador pondría `ES`, el más frecuente, y mezclaría reservas de otros países con las de España.
- **¿Podría el modelo discriminar por nacionalidad?** Sí: Italia cancela 0,60 (77 reservas) y Países Bajos 0,37 (75), y un modelo con el país podría tratar peor o mejor a quien reserva desde un lugar concreto sin una razón válida.
- **Medida aplicada y evaluada:** el mismo modelo **sin `pais_origen`** obtiene AUC 0,759 ± 0,026, igual que con él (0,758 ± 0,025). No aporta nada, así que **recomendamos no usarlo**.
- **Columnas que no deberían usarse:** `id_reserva` (no significa nada), `pais_origen` (riesgo de sesgo sin aportar) y, si el cliente confirma que el valor se conoce tarde, `cancelaciones_previas`.
- Los datos son sintéticos y no hay datos personales. Uso de la IA y qué se revisó: ver el README.

## 7. Cómo reproducirlo
- Python 3.13, pandas 2.3.3, scikit-learn 1.9.1 (en Colab saldrán otras versiones; las cifras pueden variar en el último decimal).
- Abrir `reto_S06.ipynb` en Colab y ejecutar de arriba abajo (*Reiniciar y ejecutar todo*). La primera celda descarga `reservas_sucio.csv` si no está.
- Semilla fija: 42. Ficheros: `reto_S06.ipynb`, `reservas_sucio.csv`.

## Extras (nivel 🔴)
- **Partición temporal:** entrenando con el 80 % más antiguo y evaluando con el 20 % más reciente, el AUC es 0,737, algo menor que con la aleatoria (0,758). Es la estimación más honesta si el modelo se va a usar con reservas futuras.
- **Fuga de datos:** ajustar el escalado con todos los datos cambia la media del precio que «ve» el modelo (102,68 con solo *train*; 102,73 con todos). La diferencia es pequeña, pero el *test* ya no sería independiente.
- **Recomendación para el cliente:** seguir adelante con un modelo sencillo, sin usar el país, y pedir que el sistema exporte un solo formato de fecha y precio. Límite: AUC 0,76 es útil para ordenar reservas por riesgo, no para decidir una a una.

## Revisión con la rúbrica
**Revisado por:** persona C (ejemplo de referencia) · **Fecha:** 10/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
|---|---|---|
| Corrección técnica | 4 | El cuaderno corre entero, `limpiar_reservas` es una sola función con docstring que devuelve tabla y resumen, el `fit` solo usa *train* y están la partición temporal y la prueba de la fuga |
| Reproducibilidad | 3 | Las mismas cifras siguiendo solo el README, con versiones y semilla; falta probarlo en un cuaderno nuevo de Colab para llegar al 4 |
| Análisis y comunicación al cliente | 4 | 10 defectos con causa, tratamiento y riesgo, resumen sin jerga, 4 preguntas y una recomendación con límites |
| IA responsable | 3 | Responde con ejemplos del dataset, mide el modelo sin país y dice qué se pidió y qué se revisó; para el 4 faltaría contar un fallo real de la IA, que solo puede contar el equipo |

**Lo primero que mejoraríamos:** probar el cuaderno en un Colab nuevo y anotar las versiones que salgan allí.
