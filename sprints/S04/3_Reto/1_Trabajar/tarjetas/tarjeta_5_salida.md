# Misión 5 · Guardar y entregar

<h2 align="center">Guardar el JSON, ponerlo en marcha con un comando y entregar</h2>

| | |
|---|---|
| ⏱ **Cuándo** | Miércoles · 25 min + 25 min de entrega |
| 👥 **Cómo** | Piloto y copiloto; en la parte B, repartíos el trabajo |
| 🧰 **Usáis** | 🌐 el navegador (Taller y GitHub) · 📄 `kpis.py` y un `README.md` nuevo · 💻 la terminal (dentro de la carpeta del reto) |
| 🏁 **Al terminar** | `12 de 12 pruebas superadas`, `salida.json` y la entrega subida |

**Esta tarjeta tiene dos partes:**

- [1 · Guía paso a paso](#1--guía-paso-a-paso): solo lo que hay que hacer.
- [2 · Explicaciones](#2--explicaciones): el porqué de cada cosa, para cuando lo necesitéis.
- Si queréis, seguid solo la parte 1.

← [Volver al índice de misiones](../README.md)

---

# 1 · Guía paso a paso

**Qué vais a hacer**

- `exportar_json`: **guarda** los resultados en un fichero.
- `main`: **encadena todo**: lee el CSV, calcula, guarda y avisa si algo falla.
- La entrega.

**Cómo se sigue**

- De arriba abajo, **un número cada vez**.
- Cada paso termina en ✅: lo que tiene que salir.
- Si no sale, no sigáis: mirad la parte 2.

**Tres reglas que evitan perderse** (las mismas de la misión 4)

1. **Los espacios del principio (la sangría)**
   - Un **nivel** son 4 espacios, o una pulsación de **Tab**.
   - Una línea que acaba en `:` abre un nivel nuevo: la siguiente va **un nivel más a la derecha**.
   - Si una línea queda de más a la derecha: **Shift+Tab**. De menos: **Tab**.
2. **Guardar antes de probar**
   - Pulsad **Ctrl+S**.
   - Mirad que la pestaña de `kpis.py` **no tenga un punto ●** junto al nombre.
   - Python lee el fichero **guardado**, no el que veis en pantalla.
3. **No pulséis el botón ▶ (Run) de VS Code**
   - Ejecuta `kpis.py` sin datos y da error.
   - Probad **solo** con las líneas de la terminal.

## Parte A · Construir (25 min)

### Paso 1 · Aprender (8 min)

- Taller, [bloque 4](https://www.curso.soultechlabs.io/taller/#t-tuberia): «Encadena las funciones» y «Escribe la función principal».
- Es exactamente vuestro `main`.
- ✅ Los dos puzles montados.

### Paso 2 · `exportar_json` (4 min)

| # | Qué hacéis |
|---|---|
| **2.1** | En [`kpis.py`](../reto_herramientas/kpis.py), buscad `def exportar_json`. |
| **2.2** | Borrad **solo** la línea `raise NotImplementedError(...)`. |
| **2.3** | Escribid, **un nivel** (4 espacios) a la derecha de `def`: `with open(ruta, "w", encoding="utf8") as f:` |
| **2.4** | En la línea de debajo, **un nivel más a la derecha** (8 espacios): `json.dump(datos, f, ensure_ascii=False, indent=2)` |
| **2.5** | Guardad con **Ctrl+S**. |

**Probadla.** En la terminal, dentro de la carpeta del reto, copiad **entera** esta línea y pulsad Intro:

```
python -c "from kpis import exportar_json; exportar_json({'canal': 'ocupación'}, 'prueba.json')"
```

Después, abrid `prueba.json` (aparece en el Explorador de VS Code). ✅ Tiene que poner:

```
{
  "canal": "ocupación"
}
```

- La «ó» tiene que salir **con su tilde**.
- Si pone `ocupaci\u00f3n`, falta `ensure_ascii=False`.
- Borrad `prueba.json` al terminar.

### Paso 3 · `main` (8 min)

| # | Qué hacéis |
|---|---|
| **3.1** | En `kpis.py`, buscad `def main`. Veréis ya escritas las líneas del `parser` y `args`: **no las toquéis**. Tampoco las dos **últimas líneas del fichero**, `if __name__ == "__main__":` y `sys.exit(main())`: son las que ponen en marcha `main` cuando escribís `python kpis.py …`. |
| **3.2** | Haced **triple clic** sobre la línea `raise NotImplementedError(...)`: se selecciona **entera**, con sus espacios. Pegad encima el esqueleto de abajo (copiadlo antes con Ctrl+C). |
| **3.3** | Comprobad la sangría: `try:`, `except …` y el último comentario, **un nivel** a la derecha de `def`; los huecos de dentro, **dos niveles**. Arreglad con Tab / Shift+Tab. |

```python
    try:
        # (3.4) leer el fichero
        # (3.5) calcular los KPI
        # (3.6) añadir la calidad
        # (3.7) guardar el JSON
    except (FileNotFoundError, ValueError) as error:
        # (3.8) mostrar el error y devolver 1
    # (3.9) mostrar el mensaje de éxito y devolver 0
```

**Cada hueco se rellena con lo que dice su paso.** Se borra el comentario `# (3.x)` y se escribe en su lugar, **alineado con él**.

| # | Qué hacéis |
|---|---|
| **3.4** | Guardad en `reservas, avisos` lo que devuelve `leer_reservas(args.entrada)`. |
| **3.5** | Guardad en `kpis` lo que devuelve `calcular_kpis(reservas, args.capacidad)`. (Esa función ya viene hecha.) |
| **3.6** | Añadid a `kpis` la clave `"calidad"` con un diccionario de 3 cosas: `"filas_validas"` (cuántas reservas, `len(reservas)`), `"filas_descartadas"` (cuántos avisos, `len(avisos)`) y `"avisos"` (los 20 primeros: `avisos[:20]`). |
| **3.7** | Llamad a `exportar_json(kpis, args.salida)`. |
| **3.8** | Imprimid `f"ERROR: {error}"` con `file=sys.stderr` y, debajo, `return 1`. |
| **3.9** | Imprimid `f"OK: {len(reservas)} reservas analizadas, {len(avisos)} descartadas -> {args.salida}"` y, debajo, `return 0`. |
| **3.10** | Guardad con **Ctrl+S**. |

**Así tiene que quedar la forma** (rellenad los `...`):

```
    try:
        reservas, avisos = ...                                ← 3.4
        kpis = ...                                            ← 3.5
        kpis["calidad"] = {...}                               ← 3.6
        ...(kpis, args.salida)                                ← 3.7
    except (FileNotFoundError, ValueError) as error:
        print(..., file=sys.stderr)                           ← 3.8
        return 1
    print(...)                                                ← 3.9
    return 0
```

### Paso 4 · Probar el programa entero (5 min)

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **4.1** | En la terminal: `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` | `OK: 6000 reservas analizadas, 0 descartadas -> salida.json` |
| **4.2** | Abrid `salida.json` (en el Explorador) | Las cifras de «Misión terminada cuando», abajo |
| **4.3** | En la terminal: `python test_kpis.py` | **`12 de 12 pruebas superadas`** |

## Parte B · Errores y entrega (25 min)

*Repartíos el trabajo: los pasos 5 y 6 se hacen a la vez.*

### Paso 5 · Los tres errores a propósito (10 min)

Siempre sobre **copias** del CSV, nunca sobre el original.

**Fichero que no existe**

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **5.1** | **Fichero que no existe.** En la terminal: `python kpis.py no_existe.csv salida.json` | `ERROR: No se encuentra el fichero: no_existe.csv` |
| **5.2** | Mirad el código de salida: `echo $LASTEXITCODE` (PowerShell) | `1` |

**Falta una columna**

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **5.3** | Copiad el CSV: `copy reservas_turisdata.csv sin_col.csv` | Aparece `sin_col.csv` en el Explorador |
| **5.4** | Abrid `sin_col.csv` y, en la **primera línea**, cambiad `precio_noche` por `precio` | — |
| **5.5** | Guardad con **Ctrl+S** y comprobad el cambio: `python -c "print('precio_noche' in open('sin_col.csv', encoding='utf8').readline())"` | `False` |
| **5.6** | Ejecutad: `python kpis.py sin_col.csv salida_prueba.json` | `ERROR: Faltan columnas obligatorias: ['precio_noche']` (código `1`) |

**Dato incorrecto**

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **5.7** | Copiad el CSV: `copy reservas_turisdata.csv con_error.csv` | Aparece `con_error.csv` en el Explorador |
| **5.8** | Abrid `con_error.csv`. En la **línea 5**, cambiad `,total,133.22,` por `,total,abc,`. En la **línea 10**, cambiad `,114,6,2,1,` por `,114,0,2,1,` | — |
| **5.9** | Guardad con **Ctrl+S** y comprobad los cambios: `python -c "l = open('con_error.csv', encoding='utf8').read().split('\n'); print(',total,abc,' in l[4], ',114,0,2,1,' in l[9])"` | `True True` |
| **5.10** | Ejecutad: `python kpis.py con_error.csv salida_prueba.json` | El programa **no se rompe**: `OK: 5998 reservas analizadas, 2 descartadas -> salida_prueba.json` (código `0`) |
| **5.11** | Abrid `salida_prueba.json` y buscad `"avisos"` | `Fila 5 descartada: …` y `Fila 10 descartada: noches debe ser >= 1` |

**Al terminar**

| # | Qué hacéis | ✅ Tiene que salir |
|---|---|---|
| **5.12** | **Borrad las copias**: `del sin_col.csv, con_error.csv, salida_prueba.json` (no se suben) | Desaparecen del Explorador. Ese será vuestro «provocar un error» en la review |

### Paso 6 · README (10 min)

| # | Qué hacéis |
|---|---|
| **6.1** | Copiad `README_PLANTILLA.md` como **`README.md`** (o `README_PLANTILLA_corta.md`, si el docente os la ha dado). |
| **6.2** | Rellenadlo (apartado 4 de [Entrega y rúbrica](../../2_Entregar/entrega_y_rubrica.md)). |

✅ Terminado cuando otra persona podría ejecutar el proyecto siguiendo **solo** el README.

### Paso 7 · Revisión con la rúbrica (5 min)

- **Alguien que no escribió esa parte** la revisa con la rúbrica.
- Anota el resultado en el README, en la sección «Revisión con la rúbrica» (apartado 3 de Entrega y rúbrica).
- ✅ La sección está rellena.

### Paso 8 · Subir la entrega (10 min)

| # | Qué hacéis |
|---|---|
| **8.1** | Subid los ficheros del equipo a la carpeta `sprint-04/` de GitHub, en **tres o más subidas, hechas por personas distintas**. |
| **8.2** | **Cada persona** sube su hoja con la autoevaluación (apartado 5 de Entrega y rúbrica). |
| **8.3** | La coevaluación se añade el **jueves**, tras la review, y se vuelve a subir la hoja. |

✅ Están los cuatro ficheros del equipo y una hoja por persona (**4 + N**), con tres *commits* o más.

### Paso 9 · Jueves: la review (3–5 min por equipo)

Enseñad al grupo:

- El script con el CSV real.
- El JSON.
- **Un error provocado**, con su mensaje.
- Las pruebas en verde.
- **Una decisión de diseño** explicada (por ejemplo, cómo definisteis la ocupación).

✅ Lo habéis enseñado.

*Si sobran minutos, empezad el extra: pruebas propias o `extra/plantilla_kpis_pandas.py`.*

## ✅ Misión terminada cuando

- [ ] `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` escribe `OK: 6000 reservas analizadas, 0 descartadas -> salida.json`.
- [ ] `python test_kpis.py` da **`12 de 12 pruebas superadas`** (con `kpis_pandas.py` ausente, la prueba opcional se omite y cuenta como superada).
- [ ] Los tres errores provocados (paso 5) dan su mensaje.
- [ ] En `sprint-04/` están el README, la revisión con la rúbrica, los cuatro ficheros del equipo y una hoja de autoevaluación por persona (**4 + N**), con al menos tres *commits* con nombres distintos.
- [ ] **Prueba final:** otra persona podría ejecutar el proyecto siguiendo solo el README.

**Lo que tiene que salir** en `salida.json`:

```json
{
  "reservas_analizadas": 6000,
  "ocupacion_proxy_pct": 42.0,
  "ingreso_medio_por_reserva": 576.04,
  "tasa_cancelacion_por_canal_pct": {"empresa": 43.3, "directo": 31.5, "web_intermediaria": 53.9, "agencia": 44.0},
  "calidad": {"filas_validas": 6000, "filas_descartadas": 0, "avisos": []}
}
```

## 🥋 Kata 2 · Leer un CSV sin que se rompa

⏱ 10 min · 👤 **Individual** · fin del miércoles · [Abrir la kata 2](https://www.curso.soultechlabs.io/taller/#kata-2)

- **Cada persona sola**, sin mirar esta tarjeta ni preguntar al equipo.
- Escribid `media_precio(ruta)`: lee un CSV, ignora las filas defectuosas y devuelve `None` si el fichero no existe.
- Apuntad **cuántas pistas** habéis usado.

## 👉 Siguiente

¡Reto terminado! 🎉 Continuamos con el [Sprint 5](../../../../S05/README.md).

---

# 2 · Explicaciones

*Para cuando una cosa no sale o queréis entender por qué se hace así. No hace falta leerlo para resolver la misión.*

## Las palabras de la misión

| Palabra | Qué significa |
|---|---|
| **JSON** | Los mismos datos (diccionarios y listas) escritos en un fichero de texto, que otros programas pueden leer |
| `json.dump(datos, f, ...)` | Escribe `datos` en el fichero `f` como JSON |
| `ensure_ascii=False` | «Deja las tildes como son». Sin esto, la «ó» sale escrita como `\u00f3` |
| `indent=2` | Sangra el JSON con 2 espacios, para que se lea bien |
| **`main`** | La función principal: la receta que pone en orden las demás |
| `if __name__ == "__main__":` y `sys.exit(main())` | Las dos últimas líneas del fichero. Dicen: «si ejecutan este fichero con `python kpis.py`, arranca `main` y usa lo que devuelva como código de salida». **No se tocan** |
| **argumentos** (`args.entrada`, `args.salida`, `args.capacidad`) | Lo que se escribe **después de `python kpis.py`** en la terminal: el CSV de entrada, el JSON de salida y la capacidad |
| **`sys.stderr`** | La salida de **errores** de la terminal, separada de la salida normal |
| **código de salida** | Un número con el que un programa dice si ha ido bien (**0**) o mal (**1**) |
| **`Traceback`** | Las líneas rojas que salen cuando Python se rompe. Un error bien hecho **no** es un `Traceback`: es un mensaje que entiende cualquiera |

## La receta de `main`

```
leer_reservas  →  calcular_kpis  →  exportar_json  →  mensaje de éxito  (devuelve 0)
      ↓ si falla el fichero o una columna
      mensaje de error claro por sys.stderr  (devuelve 1)
```

- Las piezas ya existen: `leer_reservas`, `calcular_kpis` y `exportar_json`.
- `main` solo las pone en orden.
- Y decide qué hacer si algo falla.

## Por qué se hace así

- **`try` / `except (FileNotFoundError, ValueError)`** (3.8): son los dos errores que `leer_reservas` lanza **a propósito** cuando falta el fichero o una columna. Se recogen aquí y se convierten en un mensaje, en lugar de dejar que salga un `Traceback`.
- **Una fila mala no es un error de `main`** (5.4): `leer_reservas` ya la descarta y la apunta en `avisos`. Por eso el programa termina con `OK` y código 0, y los avisos aparecen en `calidad`.
- **`avisos[:20]`** (3.6): si un fichero tuviera miles de filas malas, el JSON sería enorme. Se guardan solo los 20 primeros.
- **`return 0` / `return 1`** (3.8 y 3.9): la plantilla termina con `sys.exit(main())`, así que **lo que devuelve `main` es el código de salida**. Otros sistemas (un programador de tareas, otra herramienta) miran ese número para saber si ha ido bien.
- **Los errores van por `sys.stderr`**, no por `print` normal: así se pueden separar de la salida buena.
- **`argumentos=None`:** cuando se ejecuta desde la terminal, `main` lee lo que se escribe allí. Las pruebas le pasan una lista de argumentos directamente (`main([entrada, salida, "--capacidad", "5"])`) y así pueden probarlo sin abrir ninguna terminal.

## Ver el código de salida

Se mira **justo después** de ejecutar el programa:

| Dónde | Escribid |
|---|---|
| PowerShell (la terminal de VS Code en Windows) | `echo $LASTEXITCODE` |
| cmd de Windows | `echo %errorlevel%` |
| Linux o Mac | `echo $?` |

## Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| `kpis.py: error: the following arguments are required: entrada, salida` | Habéis pulsado el botón ▶ (Run) de VS Code, o habéis escrito `python kpis.py` sin los ficheros | No uséis ese botón. Escribid los dos nombres: `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` |
| `NotImplementedError` aunque ya lo habéis escrito | El fichero **no está guardado** (punto ● en la pestaña) | Ctrl+S y repetid |
| `IndentationError` | Una línea tiene más o menos espacios que sus vecinas | Mirad el dibujo de «Así tiene que quedar la forma»; arreglad con Tab / Shift+Tab |
| La ocupación no sale `42.0` | Falta el `+ 1` en los días, se cuentan canceladas o la capacidad no es 40 | Revisad `ocupacion_proxy` y ejecutad con `--capacidad 40` |
| Las tildes de `salida.json` salen como `\u00f3` | Falta `ensure_ascii=False` | Añadirlo en `json.dump` (2.4) |
| Sale un `Traceback` rojo en vez de `ERROR: …` | El `except` no recoge ese tipo de error | `except (FileNotFoundError, ValueError)` (3.8) |
| `ERROR: …` pero el código de salida es 0 | Falta el `return 1` | Debajo del `print` de error (3.8) |
| `test_exportar_json_y_main` falla | `main` no devuelve 0, o no escribe el fichero | Revisad el `return 0` (3.9) y que usáis `args.salida` (3.7) |
| En el paso 5, `sin_col.csv` o `con_error.csv` no dan el resultado esperado | El CSV **editado no está guardado**, o el cambio no está donde toca | Ctrl+S y repetid la comprobación 5.5 o 5.9: tiene que salir `False` o `True True` |
| Un solo *commit* gigante | «Lo subo al final» | Commits pequeños mientras avanzáis; la entrega pide tres o más |
| Queréis cambiar las pruebas para que pasen | Prisa | No se tocan las pruebas dadas; las propias van aparte |
| Queréis usar un asistente de IA | Es una ayuda legítima, con reglas | Seguid las reglas de la [ficha del reto](../../3_Consultar/Reto_Sprint_04.md) y declarad el uso en el README |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 5](../../3_Consultar/Solucionario_misiones.md), que tiene **los mismos pasos**. Lo que copiéis, tenéis que saber explicarlo |
