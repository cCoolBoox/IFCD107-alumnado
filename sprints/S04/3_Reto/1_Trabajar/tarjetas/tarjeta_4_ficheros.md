# Misión 4 · Leer el CSV
*Leer el fichero real sin que se rompa.*

| | |
|---|---|
| ⏱ **Cuándo** | Miércoles · 50 min + 50 min |
| 👥 **Cómo** | Todo el equipo; pilotos y copilotos rotan cada 15 minutos |
| 🧰 **Usáis** | 🌐 el navegador (curso y Taller) · 📄 `kpis.py` y el CSV `reservas_turisdata.csv` · 💻 la terminal |
| 🏁 **Al terminar** | `7 de 8 pruebas superadas` con `python test_kpis.py 2` |

**En esta tarjeta:** [Qué lograréis](#-qué-lograréis) · [La idea en un minuto](#-la-idea-en-un-minuto) · [Paso a paso](#-paso-a-paso) · [Misión terminada cuando](#-misión-terminada-cuando) · [Si os atascáis](#-si-os-atascáis) · [Siguiente](#-siguiente)

← [Volver al índice de misiones](../README.md)

## 🎯 Qué lograréis

`_convertir_fila` y `leer_reservas`: leer el fichero real `reservas_turisdata.csv` (6000 reservas), convertir los textos a números y fechas, **descartar y contar** las filas defectuosas y dar un **mensaje claro** si falta el fichero o una columna.

## 💡 La idea en un minuto

Tres ideas, de la más pequeña a la más importante:

1. **Un CSV es una tabla guardada como texto** (una fila por línea, valores separados por comas), así que **todo llega como texto.** `"2"` no es el número 2: se convierte con `int("2")`, `float("100.0")` o `date.fromisoformat("2025-01-01")`. Si el texto no sirve (`int("abc")`), Python lanza un `ValueError`.
2. **Un fichero real siempre trae filas mal, y el programa no se rompe:** prueba cada fila con `try` / `except` («intenta esto; si falla de esta manera, haz esto otro»), descarta la mala, guarda un aviso y sigue con la siguiente.
3. **`leer_reservas` devuelve dos cosas a la vez:** las reservas buenas y los avisos de las descartadas (`return reservas, avisos`; una *tupla*, dos valores juntos). Quien la llama las recoge así: `reservas, avisos = leer_reservas(ruta)`.

**Ejemplo.** La fila 3 del fichero tiene `noches = 0` → aviso `Fila 3 descartada: noches debe ser >= 1`, y esa fila no entra en la lista de reservas.

## 👣 Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| **Parte A** | | | | **50** | |
| 1 | 📚 Aprender | Excepciones (ejercicios 1 y 2) | Curso: [excepciones](https://www.curso.soultechlabs.io/basico/#pi-excepciones) | 15 | Los dos ejercicios en verde |
| 2 | 📚 Aprender | Ficheros de texto, CSV y JSON (ejercicios 2 y 3) | Curso: [ficheros](https://www.curso.soultechlabs.io/basico/#pi-ficheros) | 15 | Los dos ejercicios en verde |
| 3 | 📚 Aprender | «Leer un CSV sin que se rompa», «¿Qué error es cada uno?» y «Guardar los KPIs en JSON» | Taller: [bloque 3](https://www.curso.soultechlabs.io/taller/#t-leer) | 20 | Los tres puzles montados |
| **Parte B** | | | | **50** | |
| 4 | 🛠️ Construir | `_convertir_fila`: convertir los tipos y validar los valores (órdenes 1 y 2 de «Pasos 4 y 5», abajo) | [`kpis.py`](../reto_herramientas/kpis.py) | 15 | La función está escrita con sus «Paso» |
| 5 | 🛠️ Construir | `leer_reservas`: abrir el fichero, comprobar la cabecera, descartar y avisar, y devolver las dos cosas (órdenes 3 a 6 de «Pasos 4 y 5», abajo) | `kpis.py` | 25 | La función está escrita con sus «Paso» |
| 6 | ✅ Comprobar | Ejecutar las pruebas y verlas pasar de rojo a verde. Si una falla, leed qué esperaba y qué recibió | Terminal: `python test_kpis.py 2` | 10 | **`7 de 8 pruebas superadas`** |

En la parte B, pilotos y copilotos **rotan cada 15 minutos**.

### Pasos 4 y 5 · Qué hace cada función

**`_convertir_fila` recibe** una fila con todo en texto, `{"fecha_llegada": "2025-01-01", "noches": "2", "precio_noche": "100.0", "canal": "directo", "cancelada": "0"}`, y **la devuelve con los tipos buenos**: la fecha como `date`, `noches` como `int`, `precio_noche` como `float` y `cancelada` como `int`.

**Cómo pensarlo, en este orden.** Las pruebas llaman a `leer_reservas`, así que las órdenes 1 y 2 (que están dentro de `_convertir_fila`) no ponen nada en verde por sí solas: se ven al completar la función de lectura. A partir del orden 3 las pruebas se van poniendo en verde una a una:

| Orden | Qué hacéis | Pista de Python | Cuándo se ve en verde |
|---|---|---|---|
| 1 | Convertir los tipos en `_convertir_fila` | `int()`, `float()` y `date.fromisoformat()` ya lanzan `ValueError` si el texto no sirve | Todavía ninguna: se comprueba a través de `leer_reservas` |
| 2 | Validar los valores: además del tipo, el valor debe tener sentido (noches ≥ 1, precio > 0, `cancelada` 0 o 1, canal no vacío) | `raise ValueError("noches debe ser >= 1")` | Todavía ninguna: `test_valores_imposibles…` pasa con el orden 5 |
| 3 | Leer el fichero en `leer_reservas`; si no existe, lanzar un error que **incluya la ruta** | `open(ruta, newline="", encoding="utf8")`, `csv.DictReader` y `except FileNotFoundError` | `test_fichero_inexistente` |
| 4 | Comprobar la cabecera: si falta una columna, un error que **nombre las que faltan** | Comparar `lector.fieldnames` con `COLUMNAS_OBLIGATORIAS` | `test_faltan_columnas` |
| 5 | Descartar y avisar: probar cada fila, y si falla, guardar el aviso y seguir | `for n, fila in enumerate(lector, start=2)` (la fila 1 es la cabecera), `try`/`except ValueError` y `f"Fila {n} descartada: {error}"` | `test_filas_defectuosas…` y `test_valores_imposibles…` |
| 6 | Devolver **dos cosas a la vez**: las reservas buenas y los avisos | `return reservas, avisos` | `test_leer_reservas_convierte_tipos` (necesita los órdenes 1, 3, 5 y 6) |

**Pista de cuaderno:** [`S04_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_04_ficheros_excepciones.ipynb) (CSV, JSON y `try`/`except`).

## ✅ Misión terminada cuando

- [ ] `python test_kpis.py 2` da **`7 de 8 pruebas superadas`**: solo falla `test_exportar_json_y_main`, que es de la misión 5. (Si no habéis hecho el nivel extra de pandas, esa otra prueba opcional se omite y cuenta como superada.)
- [ ] Pasan las pruebas de lectura: `test_leer_reservas_convierte_tipos`, `test_fichero_inexistente`, `test_faltan_columnas`, `test_filas_defectuosas…` y `test_valores_imposibles…`; y también la de los datos reales.

## 🚑 Si os atascáis

> ⏰ **Señal de alarma a las 09:55.** Si a esa hora todavía no habéis empezado `leer_reservas`, **decídselo al docente**: la proyecta resuelta, **la copiáis y la explicáis con vuestras palabras** (línea a línea, en voz alta) y seguís con la misión 5. Es una ayuda legítima, y la declaráis en el README («Uso de IA y límites»).

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| Las pruebas de la fase 2 fallan **todas a la vez** | Dependen de `leer_reservas` | Empezar por esa función; la fase 1 (`python test_kpis.py 1`) no depende de ella |
| El programa se rompe con un fichero mal | No se controlan las excepciones | `try` / `except` con tipos concretos y mensajes claros |
| Las tildes salen rotas | Falta `encoding="utf8"` | Añadirlo al abrir y escribir ficheros |
| `leer_reservas` «devuelve una tupla» y falla al usarla | Se guarda en una sola variable | `reservas, avisos = leer_reservas(ruta)` |
| Todas las filas salen descartadas | La conversión falla siempre (clave mal escrita, fecha mal leída) | Imprimid el aviso de una fila y leed el error |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 4](../../3_Consultar/Solucionario_misiones.md) (se publica al acabar la clase el miércoles). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |

## 👉 Siguiente

[Misión 5 · Guardar y entregar](tarjeta_5_salida.md): guardáis el resultado en JSON, lo ponéis todo en marcha con un comando y entregáis.
