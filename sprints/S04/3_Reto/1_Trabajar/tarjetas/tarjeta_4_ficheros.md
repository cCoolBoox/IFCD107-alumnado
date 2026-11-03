# Misión 4 · Leer el CSV

<h2 align="center">Leer el fichero real sin que se rompa</h2>

| | |
|---|---|
| ⏱ **Cuándo** | Miércoles · 50 min + 50 min |
| 👥 **Cómo** | Todo el equipo; pilotos y copilotos rotan cada 15 minutos |
| 🧰 **Usáis** | 🌐 el navegador (curso y Taller) · 📄 `kpis.py` · 💻 la terminal (dentro de la carpeta del reto) |
| 🏁 **Al terminar** | `7 de 8 pruebas superadas` con `python test_kpis.py 2` |

**Esta tarjeta tiene dos partes:**

- [1 · Guía paso a paso](#1--guía-paso-a-paso): solo lo que hay que hacer.
- [2 · Explicaciones](#2--explicaciones): el porqué de cada cosa, para cuando lo necesitéis.
- Si queréis, seguid solo la parte 1.

← [Volver al índice de misiones](../README.md)

---

# 1 · Guía paso a paso

**Qué vais a hacer**

- `_convertir_fila`: convierte **una fila** del CSV.
- `leer_reservas`: lee **todo el fichero**, usando la anterior.

**Cómo se sigue**

- De arriba abajo, **un número cada vez**.
- Cada paso termina en ✅: lo que tiene que salir.
- Si no sale, no sigáis: mirad la parte 2.

## Parte A · Aprender (50 min)

| Paso | Qué hacéis | Min | ✅ Terminado cuando |
|---|---|---|---|
| **1** | Curso: [excepciones](https://www.curso.soultechlabs.io/basico/#pi-excepciones), ejercicios 1 y 2 | 15 | Los dos en verde |
| **2** | Curso: [ficheros](https://www.curso.soultechlabs.io/basico/#pi-ficheros), ejercicios 2 y 3 | 15 | Los dos en verde |
| **3** | Taller, [bloque 3](https://www.curso.soultechlabs.io/taller/#t-leer): «Leer un CSV sin que se rompa», «¿Qué error es cada uno?» y «Guardar los KPIs en JSON» | 20 | Los tres puzles montados |

## Parte B · Construir (50 min)

Pilotos y copilotos **rotan cada 15 minutos**. Se trabaja en [`kpis.py`](../reto_herramientas/kpis.py).

**Tres reglas que evitan perderse**

1. **Los espacios del principio (la sangría)**
   - Un **nivel** son 4 espacios, o una pulsación de **Tab**.
   - Una línea que acaba en `:` abre un nivel nuevo: la siguiente va **un nivel más a la derecha**.
   - Si una línea queda de más a la derecha: **Shift+Tab**. De menos: **Tab**.
   - Una línea nueva se escribe **alineada con la línea de arriba** que os digamos.
2. **Guardar antes de probar**
   - Pulsad **Ctrl+S**.
   - Mirad que la pestaña de `kpis.py` **no tenga un punto ●** junto al nombre.
   - Python lee el fichero **guardado**, no el que veis en pantalla.
3. **No pulséis el botón ▶ (Run) de VS Code**
   - Ejecuta `kpis.py` sin datos y da siempre `error: the following arguments are required: entrada, salida`.
   - No es un fallo vuestro: probad **solo** con las líneas `python -c "..."` de la terminal.

### Paso 4 · `_convertir_fila` (15 min)

| # | Qué hacéis |
|---|---|
| **4.1** | Abrid `kpis.py` y buscad `def _convertir_fila`. |
| **4.2** | Borrad **solo** la línea `raise NotImplementedError(...)` de esa función. |
| **4.3** | Escribid, **un nivel** (4 espacios) a la derecha de `def`: `noches = int(fila["noches"])`. |
| **4.4** | Haced lo mismo con las otras tres: `precio` con `float(...)` y la clave `"precio_noche"`; `cancelada` con `int(...)`; `fecha` con `date.fromisoformat(...)` y la clave `"fecha_llegada"`. |
| **4.5** | Escribid: `canal = fila["canal"].strip()`. |
| **4.6** | Escribid las **4 comprobaciones**. Cada una son dos líneas: el `if` (al nivel de `noches = …`) y debajo el `raise ValueError("...")`, **un nivel más a la derecha**. Mirad la tabla de abajo. |
| **4.7** | Escribid el final: `return {"fecha_llegada": fecha, "noches": noches, "precio_noche": precio, "canal": canal, "cancelada": cancelada}` |
| **4.8** | Guardad con **Ctrl+S**. |

**Las 4 comprobaciones del paso 4.6:**

| Si… | Escribid el `if` | Mensaje del `raise ValueError(...)` |
|---|---|---|
| el canal está vacío | `if canal == "":` | `"canal vacío"` |
| hay menos de 1 noche | `if noches < 1:` | `"noches debe ser >= 1"` |
| el precio es 0 o menos | `if precio <= 0:` | `"precio_noche debe ser > 0"` |
| `cancelada` no es 0 ni 1 | `if cancelada not in (0, 1):` | `"cancelada debe ser 0 o 1"` |

**Probadla.** En la terminal, dentro de la carpeta del reto, copiad **entera** esta línea y pulsad Intro:

```
python -c "from kpis import _convertir_fila; print(_convertir_fila({'fecha_llegada': '2025-01-01', 'noches': '2', 'precio_noche': '100.0', 'canal': 'directo', 'cancelada': '0'}))"
```

✅ Sale: `{'fecha_llegada': datetime.date(2025, 1, 1), 'noches': 2, 'precio_noche': 100.0, 'canal': 'directo', 'cancelada': 0}`

**Probad también el error**

- Repetid la línea cambiando `'noches': '2'` por `'noches': '0'`.
- ✅ Sale: `ValueError: noches debe ser >= 1`.

### Paso 5 · `leer_reservas` (25 min)

| # | Qué hacéis |
|---|---|
| **5.1** | En `kpis.py`, buscad `def leer_reservas`. |
| **5.2** | Haced **triple clic** sobre la línea `raise NotImplementedError(...)`: se selecciona **entera**, con sus espacios. Pegad encima el esqueleto de abajo (copiadlo antes con Ctrl+C). |
| **5.3** | Comprobad la sangría del esqueleto: `try:` y `except` **un nivel** a la derecha de `def`; `with` y `raise` (del `except`) **dos niveles**; `lector = …` y los huecos `# (5.x)` **tres niveles**. Si no, arreglad con Tab / Shift+Tab. Los `(5.x)` son los huecos que vais a rellenar. |

```python
    try:
        with open(ruta, newline="", encoding="utf8") as f:
            lector = csv.DictReader(f)
            # (5.4) comprobar la cabecera
            # (5.5) preparar las dos listas
            # (5.6) recorrer las filas
            # (5.7) devolver las dos listas
    except FileNotFoundError:
        # (5.8) error claro si no existe el fichero
```

**Cómo se rellenan los huecos**

- Cada hueco se rellena con lo que dice su paso.
- En los dibujos, cada `...` es lo que tenéis que escribir vosotros. **La sangría del dibujo es la buena.**
- Se borra el comentario `# (5.x)` y se escribe en su lugar, **alineado con `lector = …`** (3 niveles), salvo el 5.8.

| # | Qué hacéis |
|---|---|
| **5.4** | Cabecera. Una lista `faltan` y un `for` por las `COLUMNAS_OBLIGATORIAS` que mira si cada columna **no está** en `lector.fieldnames` (`not in`) y, si no está, la añade a `faltan` (`.append`). Después, si `faltan` no está vacía, `raise ValueError(f"Faltan columnas obligatorias: {faltan}")`. |
| **5.5** | Dos listas vacías: `reservas` y `avisos`. |
| **5.6** | Un `for n, fila in enumerate(lector, start=2):`. Dentro, un `try:` que añade a `reservas` el resultado de `_convertir_fila(fila)`; y un `except ValueError as error:` que añade a `avisos` el texto `f"Fila {n} descartada: {error}"`. |
| **5.7** | `return reservas, avisos`. |
| **5.8** | En el `except FileNotFoundError:`: `raise FileNotFoundError(f"No se encuentra el fichero: {ruta}")`. |
| **5.9** | Guardad con **Ctrl+S** y **mirad la pestaña de `kpis.py`: si tiene un punto ● al lado del nombre, todavía no está guardado.** Probar sin guardar es el error más común: Python lee el fichero **guardado** y sale `NotImplementedError` aunque en pantalla ya esté bien. |
| **5.10** | Probadla con el **fichero real** (línea de abajo). |
| **5.11** | Crear el fichero de ejemplo `mini.csv` (explicado abajo). |
| **5.12** | Probadla con **`mini.csv`** (línea de abajo). |

**5.10 · Probadla con el fichero real** (una línea, entera, en la terminal):

```
python -c "from kpis import leer_reservas; reservas, avisos = leer_reservas('reservas_turisdata.csv'); print(len(reservas), len(avisos))"
```

✅ Sale: `6000 0` (6000 reservas y ningún aviso).

**5.11 · Crear `mini.csv`**

- En VS Code, en la barra lateral izquierda (el **Explorador**), pulsad el icono de **«Nuevo archivo»** (una hoja con un +).
- Escribid `mini.csv` y pulsad Intro: se abre un fichero vacío en la carpeta del reto.
- Pegad estas 4 líneas y guardad con **Ctrl+S**.
- Si usáis el menú *Archivo → Nuevo archivo…*, elegid **Archivo de texto** (no «Archivo Python» ni «Jupyter Notebook») y guardadlo como `mini.csv` en la carpeta del reto.


```
fecha_llegada,noches,precio_noche,canal,cancelada
2025-01-01,2,100.0,directo,0
2025-01-03,3,,agencia,0
2025-01-05,0,50.0,web_intermediaria,1
```

**5.12 · Probadla con `mini.csv`** (una línea, entera):

```
python -c "from kpis import leer_reservas; reservas, avisos = leer_reservas('mini.csv'); print(len(reservas), avisos)"
```

✅ Sale: **1** reserva y **2** avisos, uno para la «Fila 3» y otro para la «Fila 4»:

```
1 ["Fila 3 descartada: could not convert string to float: ''", 'Fila 4 descartada: noches debe ser >= 1']
```

### Paso 6 · Pruebas (10 min)

| # | Qué hacéis |
|---|---|
| **6.1** | En la terminal: `python test_kpis.py 2` |
| **6.2** | Si una prueba sale en rojo, leed qué **debería salir**, comparadlo con lo que sale en la vuestra y corregid. |

- ✅ Terminado cuando sale **`7 de 8 pruebas superadas`**.
- La que falla, `test_exportar_json_y_main`, es de la misión 5.

> ⏰ **Señal de alarma a las 09:55**
>
> - Si a esa hora todavía no habéis empezado `leer_reservas`, **decídselo al docente**.
> - El docente la proyecta resuelta; **la copiáis y la explicáis con vuestras palabras** (línea a línea, en voz alta).
> - Seguís con la misión 5.
> - Es una ayuda legítima: la declaráis en el README («Uso de IA y límites»).

## ✅ Misión terminada cuando

- [ ] `_convertir_fila` da el diccionario con `'noches': 2` (sin comillas) y `ValueError: noches debe ser >= 1` con 0 noches.
- [ ] `leer_reservas` con el fichero real da `6000 0`, y con `mini.csv`, 1 reserva y 2 avisos.
- [ ] `python test_kpis.py 2` da **`7 de 8 pruebas superadas`**.

[Misión 5 · Guardar y entregar](tarjeta_5_salida.md) →

---

# 2 · Explicaciones

*Para cuando una cosa no sale o queréis entender por qué se hace así. No hace falta leerlo para resolver la misión.*

## Las palabras de la misión

| Palabra | Qué significa |
|---|---|
| **CSV** | Una tabla escrita como texto: una fila por línea, valores separados por comas. Python lo lee **todo como texto**: `"2"` no es el número 2 |
| `int("2")` | Convierte el texto `"2"` en el número 2 |
| `float("100.0")` | Convierte el texto `"100.0"` en el número 100.0 |
| `date.fromisoformat("2025-01-01")` | Convierte el texto en una fecha |
| **`ValueError`** | El error que da Python cuando un texto no se puede convertir: `int("tres")` |
| **`raise ValueError("...")`** | «Para: esto está mal», con un mensaje |
| **`try` / `except`** | «Intenta esto; si da este error, haz esto otro **y sigue**» |
| **`return a, b`** | Devuelve **dos cosas a la vez**. Se recogen con `x, y = funcion()` |

## El ejemplo de `mini.csv`

La fila 1 es la cabecera; los datos empiezan en la fila 2.

| Fila | Contenido | Qué pasa |
|---|---|---|
| 2 | `2025-01-01,2,100.0,directo,0` | Todo se convierte y tiene sentido → **entra en `reservas`** |
| 3 | `2025-01-03,3,,agencia,0` | El precio está vacío: `float("")` falla → **aviso** y se sigue |
| 4 | `2025-01-05,0,50.0,web_intermediaria,1` | `int("0")` funciona, pero **0 noches no tiene sentido** → `ValueError` nuestro → **aviso** |

## Por qué se hace así

- **Convertir y comprobar son dos cosas distintas** (paso 4). `int("0")` funciona y da 0, pero 0 noches no tiene sentido: por eso, además de convertir, hay 4 `if` que comprueban el **valor**.
- **Una fila mala no para el programa** (paso 5.6). El `try` / `except` dentro del `for` dice «si esta fila falla, apunta un aviso y pasa a la siguiente». Con 6000 filas, parar en la primera mala sería inútil; descartarla **sin decir nada** sería peor, porque nadie sabría que faltan datos.
- **Los avisos empiezan en la fila 2** (`start=2`): la cabecera es la fila 1 del fichero, y quien lea el aviso busca esa fila en el fichero.
- **El fichero que no existe o la columna que falta sí paran el programa** (5.4 y 5.8): sin fichero o sin esa columna no hay nada que calcular, y un mensaje claro ahorra tiempo.
- **`with open(...) as f:`** abre el fichero y **lo cierra solo** al terminar. `encoding="utf8"` hace que las tildes salgan bien.
- **`leer_reservas` devuelve dos listas** (`return reservas, avisos`): las buenas y los avisos de las malas.
- **Por qué los espacios importan.** En Python, lo que va **más a la derecha** está «dentro de» lo de arriba: el `if` está dentro del `for`, y el `for` dentro del `with`, y el `with` dentro del `try`. Por eso el esqueleto del paso 5.3 marca el nivel de cada cosa.

## Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| `IndentationError` | Una línea tiene más o menos espacios que sus vecinas, o el fichero **no está guardado** | Contad los espacios de la línea que dice el error; guardad con Ctrl+S |
| `kpis.py: error: the following arguments are required: entrada, salida` | Habéis pulsado el botón ▶ (Run) de VS Code: ejecuta `kpis.py` sin datos | No es un fallo: no uséis ese botón; probad con las líneas `python -c "..."` de la terminal |
| `ParserError` o `>>>` en la terminal | Habéis pegado líneas que empiezan por `>>>` | Usad la línea `python -c "..."` de la tarjeta, **entera** |
| `NotImplementedError` | O queda la línea `raise NotImplementedError(...)`, o **el fichero no está guardado** (mirad el punto ● de la pestaña) | Guardad con Ctrl+S. Si sigue, buscad esa línea: tiene que quedar solo vuestro código |
| `'noches': '2'` con comillas | Falta el `int(...)`: devuelve el texto | Convertid cada campo |
| `KeyError: 'noches'` | Clave mal escrita | Tiene que ser exactamente `"noches"` |
| Avisos de «Fila 2» y «Fila 3» | Contáis desde 1 | `enumerate(lector, start=2)` |
| 2 reservas válidas (entra la de 0 noches) | Falta comprobar el valor | `if noches < 1:` con su `raise` |
| 1 reserva y `avisos` vacío | La fila mala se descarta **en silencio** | Falta `avisos.append(...)` en el `except` |
| El programa se rompe en la fila 3 con `ValueError` | Falta el `try` / `except` dentro del `for` | Paso 5.6 |
| `TypeError: list indices must be integers…` | `leer_reservas` devuelve dos cosas y se guardan en una variable | `reservas, avisos = leer_reservas(...)` |
| Las tildes salen rotas | Falta `encoding="utf8"` al abrir | Paso 5.3 |
| Todas las pruebas de la fase 2 fallan a la vez | Dependen de `leer_reservas` | Empezad por esa función |
| `test_datos_reales…` falla | Falta la misión 3 (`tasa_cancelacion_por_canal`) | Hacedla; sin ella salen `6 de 8` |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 4](../../3_Consultar/Solucionario_misiones.md), que tiene **los mismos pasos**. Lo que copiéis, tenéis que saber explicarlo |
