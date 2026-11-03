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

Dos funciones de `kpis.py` que leen el fichero real `reservas_turisdata.csv` (6000 reservas):

- `_convertir_fila`: coge **una fila** (todo texto) y la convierte a números y fechas, comprobando que tenga sentido.
- `leer_reservas`: abre el fichero, recorre las filas, **guarda las buenas y apunta un aviso por cada mala**. Si falta el fichero o una columna, da un mensaje claro.

## 💡 La idea en un minuto

**Un CSV es una tabla escrita como texto:** una fila por línea y los valores separados por comas. Python lo lee **todo como texto**: `"2"` no es el número 2.

| Palabra | Qué significa |
|---|---|
| `int("2")` | Convierte el texto `"2"` en el número 2 |
| `float("100.0")` | Convierte el texto `"100.0"` en el número 100.0 |
| `date.fromisoformat("2025-01-01")` | Convierte el texto en una fecha |
| **`ValueError`** | El error que da Python cuando un texto no se puede convertir: `int("tres")` |
| **`raise ValueError("...")`** | «Para: esto está mal», con un mensaje |
| **`try` / `except`** | «Intenta esto; si da este error, haz esto otro **y sigue**» |
| **`return a, b`** | Devuelve **dos cosas a la vez**. Se recogen con `x, y = funcion()` |

**El ejemplo que seguiremos** en toda la tarjeta, con 3 reservas (la fila 1 es la cabecera):

```
fecha_llegada,noches,precio_noche,canal,cancelada
2025-01-01,2,100.0,directo,0               ← fila 2: buena
2025-01-03,3,,agencia,0                    ← fila 3: mala (falta el precio)
2025-01-05,0,50.0,web_intermediaria,1      ← fila 4: mala (0 noches)
```

## 👣 Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| **Parte A** | | | | **50** | |
| 1 | 📚 Aprender | Excepciones (ejercicios 1 y 2) | Curso: [excepciones](https://www.curso.soultechlabs.io/basico/#pi-excepciones) | 15 | Los dos ejercicios en verde |
| 2 | 📚 Aprender | Ficheros de texto, CSV y JSON (ejercicios 2 y 3) | Curso: [ficheros](https://www.curso.soultechlabs.io/basico/#pi-ficheros) | 15 | Los dos ejercicios en verde |
| 3 | 📚 Aprender | «Leer un CSV sin que se rompa», «¿Qué error es cada uno?» y «Guardar los KPIs en JSON» | Taller: [bloque 3](https://www.curso.soultechlabs.io/taller/#t-leer) | 20 | Los tres puzles montados |
| **Parte B** | | | | **50** | |
| 4 | 🛠️ Construir | `_convertir_fila`: convertir una fila a los tipos buenos y comprobar que tiene sentido (ver «Paso 4», abajo) | [`kpis.py`](../reto_herramientas/kpis.py) | 15 | La probáis a mano y sale lo esperado |
| 5 | 🛠️ Construir | `leer_reservas`: abrir el fichero, recorrer las filas y avisar de las malas (ver «Paso 5», abajo) | `kpis.py` | 25 | La probáis a mano con `mini.csv` y sale lo esperado |
| 6 | ✅ Comprobar | Ejecutar las pruebas de la fase 2 | Terminal: `python test_kpis.py 2` | 10 | **`7 de 8 pruebas superadas`** |

En la parte B, pilotos y copilotos **rotan cada 15 minutos**. En el [solucionario](../../3_Consultar/Solucionario_misiones.md) cada paso tiene su apartado con **el mismo número**.

### Paso 4 · `_convertir_fila`

**Qué hace.** Recibe **una fila** con todo en texto y la devuelve con los **tipos buenos**. Si algo no tiene sentido, **para** con un `ValueError` y un mensaje.

**A mano, con la fila 2 del ejemplo** (`2025-01-01,2,100.0,directo,0`):

| Campo | Llega como texto | Sale como | Se hace con |
|---|---|---|---|
| `fecha_llegada` | `"2025-01-01"` | una fecha | `date.fromisoformat(...)` |
| `noches` | `"2"` | el número 2 | `int(...)` |
| `precio_noche` | `"100.0"` | el número 100.0 | `float(...)` |
| `cancelada` | `"0"` | el número 0 | `int(...)` |
| `canal` | `"directo"` | `"directo"` | se queda igual |

Y las filas malas:

- **Fila 3** (precio vacío): `float("")` falla **solo** con un `ValueError`.
- **Fila 4** (0 noches): `int("0")` funciona, pero **0 noches no tiene sentido**. Hay que pararlo nosotros: `ValueError: noches debe ser >= 1`.

**Qué tocáis en [`kpis.py`](../reto_herramientas/kpis.py).** Dejad el `def` y el texto entre comillas triples. Borrad **solo** la línea `raise NotImplementedError(...)` y escribid con 4 espacios delante. Los pasos de la tabla son **los mismos `# Paso 1, 2, 3`** que están como comentario dentro de la función (no los confundáis con los pasos 1 a 6 de la tarjeta).

| Paso de `kpis.py` | Lo que hacíais a mano | Pista |
|---|---|---|
| 1 | Convertir cada campo | `noches = int(fila["noches"])`, `float(...)`, `date.fromisoformat(...)` |
| 2 | Comprobar que tiene sentido. Son **4 comprobaciones**: canal no vacío, noches ≥ 1, precio > 0, `cancelada` 0 o 1 | `if noches < 1:` y `raise ValueError("noches debe ser >= 1")` |
| 3 | Devolver los valores ya convertidos, en un diccionario | `return {"fecha_llegada": fecha, ...}` |

**Probadla a mano.** En la terminal, dentro de la carpeta del reto, copiad **entera** esta línea y pulsad Intro:

```
python -c "from kpis import _convertir_fila; print(_convertir_fila({'fecha_llegada': '2025-01-01', 'noches': '2', 'precio_noche': '100.0', 'canal': 'directo', 'cancelada': '0'}))"
```

Tiene que salir `{'fecha_llegada': datetime.date(2025, 1, 1), 'noches': 2, 'precio_noche': 100.0, 'canal': 'directo', 'cancelada': 0}`. Fijaos: `'noches': 2` **sin comillas**, es un número. Si cambiáis `'noches': '2'` por `'noches': '0'`, tiene que salir `ValueError: noches debe ser >= 1`.

### Paso 5 · `leer_reservas`

**Qué hace.** Abre el CSV, recorre las filas y devuelve **dos cosas**: las reservas buenas y los avisos de las malas.

**A mano, con las 3 filas del ejemplo:**

1. **Fila 2**: se convierte bien → entra en `reservas`.
2. **Fila 3**: da `ValueError` → **no se para**: se apunta el aviso `Fila 3 descartada: ...` y se sigue.
3. **Fila 4**: da `ValueError` → se apunta `Fila 4 descartada: noches debe ser >= 1` y se sigue.

Resultado: **1 reserva y 2 avisos**. Los números de fila son los del fichero: la cabecera es la fila 1, por eso se cuenta desde 2.

Y dos casos en los que **sí** se para, con un mensaje claro: si el fichero **no existe** (el mensaje incluye su nombre) y si **falta una columna** (el mensaje dice cuál).

| Paso de `kpis.py` | Lo que hacíais a mano | Pista |
|---|---|---|
| 1 | Abrir el fichero; si no existe, error con la ruta | `with open(ruta, newline="", encoding="utf8") as f:` dentro de un `try`, y `except FileNotFoundError:` |
| 2 | Mirar la cabecera: si falta una columna, error que diga cuál | `csv.DictReader(f)`, `lector.fieldnames` y `COLUMNAS_OBLIGATORIAS` |
| 3 | Recorrer las filas; si una falla, apuntar el aviso y seguir | `for n, fila in enumerate(lector, start=2):`, `try` / `except ValueError as error` y `f"Fila {n} descartada: {error}"` |
| 4 | Devolver las dos listas | `return reservas, avisos` |

Pista de cuaderno: [`S04_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_04_ficheros_excepciones.ipynb) (CSV, JSON y `try`/`except`).

**Probadla a mano.** Primero, el fichero pequeño. En VS Code: *Archivo → Nuevo archivo*, pegad estas 4 líneas y guardadlo como **`mini.csv`** en la carpeta del reto:

```
fecha_llegada,noches,precio_noche,canal,cancelada
2025-01-01,2,100.0,directo,0
2025-01-03,3,,agencia,0
2025-01-05,0,50.0,web_intermediaria,1
```

Después, en la terminal (una línea, entera):

```
python -c "from kpis import leer_reservas; reservas, avisos = leer_reservas('mini.csv'); print(len(reservas), avisos)"
```

Tiene que salir **1 reserva y 2 avisos**:

```
1 ["Fila 3 descartada: could not convert string to float: ''", 'Fila 4 descartada: noches debe ser >= 1']
```

(El texto del primer aviso lo pone Python y puede variar; lo que importa es el **número de fila** y que haya **un aviso por cada fila mala**.) Con el fichero real tiene que salir `6000 0`:

```
python -c "from kpis import leer_reservas; reservas, avisos = leer_reservas('reservas_turisdata.csv'); print(len(reservas), len(avisos))"
```

### Paso 6 · Pruebas

Antes de escribir nada, `python test_kpis.py 2` dice **`1 de 8`**: todo en rojo, menos una prueba opcional que se omite. Es lo normal. Cuando `leer_reservas` esté hecha, las pruebas se ponen en verde:

| Prueba | Qué comprueba |
|---|---|
| `test_leer_reservas_convierte_tipos` | Los tipos buenos (`int`, `float`, fecha) |
| `test_fichero_inexistente` | Error claro si falta el fichero |
| `test_faltan_columnas` | Error que nombra la columna que falta |
| `test_filas_defectuosas_se_descartan_y_se_avisan` | Las filas mal se descartan y se avisa |
| `test_valores_imposibles_se_descartan` | 0 noches, precio 0, `cancelada` 2… no valen |
| `test_datos_reales_si_estan_disponibles` | Los 6000 datos reales (necesita también la misión 3) |

La que queda en rojo, `test_exportar_json_y_main`, es de la misión 5. Terminad con **`7 de 8 pruebas superadas`**. Si una falla, leed qué **debería salir** y comparadlo con lo que sale en la vuestra.

## ✅ Misión terminada cuando

- [ ] `python test_kpis.py 2` da **`7 de 8 pruebas superadas`**: solo falla `test_exportar_json_y_main`, que es de la misión 5. (Si no habéis hecho el nivel extra de pandas, esa otra prueba opcional se omite y cuenta como superada.)
- [ ] Pasan las pruebas de lectura: `test_leer_reservas_convierte_tipos`, `test_fichero_inexistente`, `test_faltan_columnas`, `test_filas_defectuosas…` y `test_valores_imposibles…`; y también la de los datos reales.

## 🚑 Si os atascáis

> ⏰ **Señal de alarma a las 09:55.** Si a esa hora todavía no habéis empezado `leer_reservas`, **decídselo al docente**: la proyecta resuelta, **la copiáis y la explicáis con vuestras palabras** (línea a línea, en voz alta) y seguís con la misión 5. Es una ayuda legítima, y la declaráis en el README («Uso de IA y límites»).

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| Las pruebas de la fase 2 fallan **todas a la vez** | Dependen de `leer_reservas` | Empezar por esa función; la fase 1 (`python test_kpis.py 1`) no depende de ella |
| El programa se rompe con un fichero mal | No se controlan las excepciones | `try` / `except` con tipos concretos y mensajes claros |
| `IndentationError` | Líneas mal sangradas, o fichero sin guardar | Dentro de la función, 4 espacios; dentro de un `for`, 8. Si pegáis la solución, pegad la **función entera** (de `def` a `raise`) y guardad con Ctrl+S |
| `ParserError` o `>>>` en la terminal | Habéis pegado líneas que empiezan por `>>>` | Usad la línea `python -c "..."` de la tarjeta, que se pega **entera** |
| Las tildes salen rotas | Falta `encoding="utf8"` | Añadirlo al abrir y escribir ficheros |
| `leer_reservas` «devuelve una tupla» y falla al usarla | Se guarda en una sola variable | `reservas, avisos = leer_reservas(ruta)` |
| Todas las filas salen descartadas | La conversión falla siempre (clave mal escrita, fecha mal leída) | Imprimid el aviso de una fila y leed el error |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 4](../../3_Consultar/Solucionario_misiones.md) (tiene **los mismos pasos que esta tarjeta**). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |

## 👉 Siguiente

[Misión 5 · Guardar y entregar](tarjeta_5_salida.md): guardáis el resultado en JSON, lo ponéis todo en marcha con un comando y entregáis.
