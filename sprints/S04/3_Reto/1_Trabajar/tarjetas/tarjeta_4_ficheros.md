# Misión 4 · Leer el CSV sin que se rompa

> ⏱ **50 minutos + 50 minutos** · 🅱️ Fase 2 · miércoles · 👥 Todo el equipo, pilotos y copilotos rotando cada 15 minutos · [Volver al índice](../README.md)

## 🎯 Qué construís

`_convertir_fila` y `leer_reservas`: leer el fichero real `reservas_turisdata.csv` (6000 reservas), convertir los textos a números y fechas, **descartar y contar** las filas defectuosas y dar un **mensaje claro** si falta el fichero o una columna.

## 💡 La idea clave

Tres ideas, de la más pequeña a la más importante:

1. **En un CSV todo llega como texto.** `"2"` no es el número 2: hay que convertirlo (`int("2")`, `float("100.0")`, `date.fromisoformat("2025-01-01")`). Si el texto no sirve (`int("abc")`), Python lanza un `ValueError`.
2. **Un fichero real siempre trae filas mal.** El programa **no se rompe**: prueba cada fila, y si falla, la **descarta, guarda un aviso y sigue con la siguiente**. Esto se escribe con `try` / `except` («intenta esto; si falla de esta manera, haz esto otro»):

   ```python
   try:
       noches = int(texto)
   except ValueError:
       print("eso no es un número")
   ```

3. **`leer_reservas` devuelve dos cosas a la vez:** las reservas buenas y los avisos de las descartadas (`return reservas, avisos`; una *tupla*, dos valores juntos). Quien la llama las recoge así: `reservas, avisos = leer_reservas(ruta)`.

**Ejemplo.** La fila 3 del fichero tiene `noches = 0` → aviso `Fila 3 descartada: noches debe ser >= 1`, y esa fila no entra en la lista de reservas.

## 🧰 Antes de tocar el código *(50 min)*

1. **Curso «Python desde cero»** *(30 min)*: [excepciones](https://www.curso.soultechlabs.io/basico/#pi-excepciones) (ejercicios 1 y 2) y [ficheros de texto, CSV y JSON](https://www.curso.soultechlabs.io/basico/#pi-ficheros) (ejercicios 2 y 3).
2. **Taller de bloques** *(20 min)*: [bloque 3](https://www.curso.soultechlabs.io/taller/#t-leer), «Leer un CSV sin que se rompa», «¿Qué error es cada uno?» y «Guardar los KPIs en JSON».

## 🛠️ Paso a paso *(los otros 50 min)*

En [`kpis.py`](../reto_herramientas/kpis.py): **primero `_convertir_fila` y después `leer_reservas`**, con los comentarios «Paso» de cada docstring. Ejecutad `python test_kpis.py 2` después de cada paso y mirad cuáles pasan de rojo a verde.

**`_convertir_fila` recibe** una fila con todo en texto, `{"fecha_llegada": "2025-01-01", "noches": "2", "precio_noche": "100.0", "canal": "directo", "cancelada": "0"}`, y **la devuelve con los tipos buenos**: la fecha como `date`, `noches` como `int`, `precio_noche` como `float` y `cancelada` como `int`.

**Cómo pensarlo, en este orden** (así las pruebas se van poniendo en verde una a una):

| Orden | Qué hacéis | Pista de Python | Prueba que pasa a verde |
|---|---|---|---|
| 1 | Convertir los tipos en `_convertir_fila` | `int()`, `float()` y `date.fromisoformat()` ya lanzan `ValueError` si el texto no sirve | `test_leer_reservas_convierte_tipos` |
| 2 | Validar los valores: además del tipo, el valor debe tener sentido (noches ≥ 1, precio > 0, `cancelada` 0 o 1, canal no vacío) | `raise ValueError("noches debe ser >= 1")` | `test_valores_imposibles…` |
| 3 | Leer el fichero en `leer_reservas`; si no existe, lanzar un error que **incluya la ruta** | `open(ruta, newline="", encoding="utf8")`, `csv.DictReader` y `except FileNotFoundError` | `test_fichero_inexistente` |
| 4 | Comprobar la cabecera: si falta una columna, un error que **nombre las que faltan** | Comparar `lector.fieldnames` con `COLUMNAS_OBLIGATORIAS` | `test_faltan_columnas` |
| 5 | Descartar y avisar: probar cada fila, y si falla, guardar el aviso y seguir | `for n, fila in enumerate(lector, start=2)` (la fila 1 es la cabecera), `try`/`except ValueError` y `f"Fila {n} descartada: {error}"` | `test_filas_defectuosas…` |
| 6 | Devolver **dos cosas a la vez**: las reservas buenas y los avisos | `return reservas, avisos` | `test_leer_reservas_convierte_tipos` |

**Pista de cuaderno:** [`S04_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_04_ficheros_excepciones.ipynb) (CSV, JSON y `try`/`except`).

## 👀 Qué deberíais ver

`python test_kpis.py 2` da **`7 de 8 pruebas superadas`**: solo falla `test_exportar_json_y_main`, que es de la misión 5. (Si no habéis hecho el nivel extra de pandas, esa otra prueba opcional se omite y cuenta como superada.)

## ✅ Hecho cuando

Pasan las pruebas de lectura: `test_leer_reservas_convierte_tipos`, `test_fichero_inexistente`, `test_faltan_columnas`, `test_filas_defectuosas…` y `test_valores_imposibles…`; y también la de los datos reales.

## 🚑 Si os atascáis

> ⏰ **Señal de alarma a las 09:55.** Si a esa hora todavía no habéis empezado `leer_reservas`, **decídselo al docente**: la proyecta resuelta, **la copiáis y la explicáis con vuestras palabras** (línea a línea, en voz alta) y seguís con la misión 5. Es una ayuda legítima, y la declaráis en el README («Uso de IA y límites»).

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| Las pruebas de la fase 2 fallan **todas a la vez** | Dependen de `leer_reservas` | Empezar por esa función; la fase 1 (`python test_kpis.py 1`) no depende de ella |
| El programa se rompe con un fichero mal | No se controlan las excepciones | `try` / `except` con tipos concretos y mensajes claros |
| Las tildes salen rotas | Falta `encoding="utf8"` | Añadirlo al abrir y escribir ficheros |
| `leer_reservas` «devuelve una tupla» y falla al usarla | Se guarda en una sola variable | `reservas, avisos = leer_reservas(ruta)` |
| Todas las filas salen descartadas | La conversión falla siempre (clave mal escrita, fecha mal leída) | Imprimid el aviso de una fila y leed el error |

## ➡️ Siguiente

[Misión 5 · Guardar, poner en marcha y entregar](tarjeta_5_salida.md): guardáis el resultado en JSON, lo ponéis todo en marcha con un comando y entregáis.
