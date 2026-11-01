# Misión 5 · Guardar el resultado, ponerlo en marcha y entregar

> ⏱ **25 minutos + 25 minutos de entrega** · 🅱️ Fase 2 · miércoles · 👥 Piloto y copiloto; en la parte B, repartíos el trabajo · [Volver al índice](../README.md)
>
> **En esta misión usáis:** 🌐 el navegador (Taller y GitHub) · 📄 `kpis.py` y un `README.md` nuevo · 💻 la terminal

## 🎯 Qué construís

`exportar_json` y `main`: **la herramienta de verdad**, que se ejecuta con un solo comando, lee el CSV, calcula los tres KPI, avisa si algo está mal y guarda un JSON que otros sistemas puedan leer. Y después, **la entrega**.

## 💡 La idea clave

**`main` es la receta que encadena todo lo que ya habéis hecho**: leer → calcular → guardar. Las piezas ya existen (`leer_reservas`, `calcular_kpis`, `exportar_json`); `main` solo las pone en orden y decide qué hacer si algo falla:

```
leer_reservas  →  calcular_kpis  →  exportar_json  →  mensaje de éxito  (devuelve 0)
      ↓ si falla el fichero o una columna
      mensaje de error claro por sys.stderr  (devuelve 1)
```

El **código de salida** (0 = bien, 1 = mal) es la forma en que un programa le dice al sistema si ha ido bien. Y un error **no es un `Traceback` rojo**: es un mensaje que entiende cualquiera.

## 🛠️ Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| **Parte A** | | | | **25** | |
| 1 | 📚 Aprender | «Encadena las funciones» y «Escribe la función principal». Es exactamente vuestro `main` | Taller: [bloque 4](https://www.curso.soultechlabs.io/taller/#t-tuberia) | 8 | Los dos puzles montados |
| 2 | 🛠️ Construir | `exportar_json(datos, ruta)` (detalle abajo) | [`kpis.py`](../reto_herramientas/kpis.py) | 4 | La función está escrita |
| 3 | 🛠️ Construir | `main(argumentos=None)` (detalle abajo) | `kpis.py` | 8 | La función está escrita |
| 4 | ✅ Comprobar | Ejecutar el programa entero con el CSV real, abrir `salida.json` y pasar todas las pruebas | Terminal: `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` y `python test_kpis.py` | 5 | `salida.json` como en «Qué deberíais ver» y **`12 de 12 pruebas superadas`** |
| **Parte B** | | *(repartíos el trabajo: los pasos 5 y 6 se hacen a la vez)* | | **25** | |
| 5 | ✅ Comprobar | Provocar **a propósito** los tres errores, siempre sobre **copias** del CSV (detalle abajo) | Terminal | 10 | Los tres casos dan lo que dice la tabla |
| 6 | 🛠️ Construir | Copiar `README_PLANTILLA.md` como `README.md` y rellenarlo (apartado 4 de [Entrega y rúbrica](../../2_Entregar/entrega_y_rubrica.md)) | `README.md` | 10 | Otra persona podría ejecutar el proyecto siguiendo solo el README |
| 7 | ✅ Comprobar | Revisión con la rúbrica: **alguien que no escribió esa parte** la revisa y anota el resultado en el README (apartado 3 de Entrega y rúbrica) | `README.md`, sección «Revisión con la rúbrica» | 5 | La sección está rellena |
| 8 | 📤 Entregar | Subir los ficheros del equipo a `sprint-04/` en **tres o más subidas, hechas por personas distintas**; **cada persona** sube su autoevaluación y coevaluación (apartado 5 de Entrega y rúbrica) | GitHub, carpeta `sprint-04/` | 10 | Están los cuatro ficheros del equipo y una hoja por persona (**4 + N**), con tres *commits* o más |
| 9 | 📤 Entregar | La review: enseñar el script con el CSV real, el JSON, un error provocado con su mensaje y las pruebas en verde. Explicar **una decisión de diseño** (por ejemplo, cómo definisteis la ocupación) | A la clase | 3–5 | Lo habéis enseñado |

Si sobran minutos, empezad el extra (pruebas propias o `extra/plantilla_kpis_pandas.py`).

### Detalle de los pasos 2 y 3: `exportar_json` y `main`

**`main` es la receta que encadena todo lo que ya habéis hecho:** `leer_reservas` → `calcular_kpis` → `exportar_json` → mensaje de éxito.

1. **`exportar_json(datos, ruta)`**: abrid `ruta` para escribir con `encoding="utf8"` y guardad con `json.dump(datos, f, ensure_ascii=False, indent=2)`. Sin `ensure_ascii=False`, las tildes saldrían como `\u00f3`. Pista: [`S04_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_04_ficheros_excepciones.ipynb).
2. **`main(argumentos=None)`**: la plantilla ya lee los argumentos (`args.entrada`, `args.salida` y `args.capacidad`). Vosotros, **dentro de un `try`**:
   1. `leer_reservas(args.entrada)`;
   2. `calcular_kpis(reservas, args.capacidad)`, que ya viene hecha;
   3. añadir al resultado la clave `"calidad"` con `filas_validas`, `filas_descartadas` y `avisos` (si hay muchos avisos, guardad solo los 20 primeros);
   4. `exportar_json`;
   5. imprimir un mensaje de éxito y **devolver 0**.

   En el `except (FileNotFoundError, ValueError)`: imprimir `ERROR: …` **por `sys.stderr`** y **devolver 1**.

### Detalle del paso 5: los tres errores a propósito

| Caso | Cómo se provoca | Qué deberíais ver | Código de salida |
|---|---|---|---|
| 1. Fichero que no existe | `python kpis.py no_existe.csv salida.json` | `ERROR: No se encuentra el fichero: no_existe.csv` | 1 |
| 2. Falta una columna | Copiad el CSV como `sin_col.csv` y, con el editor, cambiad en la primera línea `precio_noche` por `precio`. Ejecutad con `sin_col.csv` | `ERROR: Faltan columnas obligatorias: ['precio_noche']` | 1 |
| 3. Dato incorrecto | Copiad el CSV como `con_error.csv` y, con el editor, escribid `abc` como precio de la fila 5 y `0` como noches de la fila 10. Ejecutad con `con_error.csv` | El programa **no se rompe**: `OK: 5998 reservas analizadas, 2 descartadas -> …` y en `calidad.avisos` aparecen `Fila 5 descartada: …` y `Fila 10 descartada: noches debe ser >= 1` | 0 |

El código de salida se mira justo después de ejecutar: en Linux o Mac, `echo $?`; en Windows (cmd), `echo %errorlevel%`; en PowerShell, `echo $LASTEXITCODE`. **Al terminar, borrad las copias de prueba** (`sin_col.csv`, `con_error.csv` y el JSON de prueba): no se suben. Ese será vuestro «provocar un error» en la review.

## 👀 Qué deberíais ver

Por pantalla, un mensaje como `OK: 6000 reservas analizadas, 0 descartadas -> salida.json` y, en la carpeta, un fichero `salida.json` con este contenido:

```
{
  "reservas_analizadas": 6000,
  "ocupacion_proxy_pct": 42.0,
  "ingreso_medio_por_reserva": 576.04,
  "tasa_cancelacion_por_canal_pct": {"empresa": 43.3, "directo": 31.5, "web_intermediaria": 53.9, "agencia": 44.0},
  "calidad": {"filas_validas": 6000, "filas_descartadas": 0, "avisos": []}
}
```

Y `python test_kpis.py` da **`12 de 12 pruebas superadas`** (con `kpis_pandas.py` ausente, la prueba opcional se omite y cuenta como superada). En `sprint-04/`: los cuatro ficheros del equipo y una hoja de autoevaluación por persona (**4 + N**); y en el historial (el icono del reloj), al menos tres *commits* con nombres distintos.

## ✅ Hecho cuando

Existe `salida.json` con esas cifras, las 12 pruebas pasan, los tres errores provocados dan su mensaje, y el README, la revisión con la rúbrica y los *commits* están subidos. Prueba final: **otra persona podría ejecutar el proyecto siguiendo solo el README**.

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| La ocupación no sale `42.0` | Falta el `+ 1` en los días, se cuentan canceladas o la capacidad no es 40 | Releer la fórmula y ejecutar con `--capacidad 40` |
| Las tildes de `salida.json` salen como `ó` | Falta `ensure_ascii=False` | Añadirlo en `json.dump` |
| Sale un `Traceback` rojo en vez de `ERROR: …` | El `except` no recoge ese tipo de error | `except (FileNotFoundError, ValueError)` |
| `test_exportar_json_y_main` falla | `main` no devuelve 0, o no escribe el fichero | Revisad el `return 0` y la ruta de `args.salida` |
| Un solo *commit* gigante | «Lo subo al final» | Commits pequeños mientras avanzáis; la entrega pide tres o más |
| Cambiar las pruebas para que pasen | Prisa | No se tocan las pruebas dadas; las propias van aparte |

Si usáis un asistente de IA, seguid las reglas de la «Ayuda 1» de la [ficha completa](../../3_Consultar/Reto_Sprint_04.md) y declarad el uso en el README.

## 🥋 Kata 2 · Leer un CSV sin que se rompa — 10 min, **individual**, fin del miércoles

[Abrir la kata 2](https://www.curso.soultechlabs.io/taller/#kata-2). **Cada persona sola**: escribid `media_precio(ruta)`, que lee un CSV, ignora las filas defectuosas y devuelve `None` si el fichero no existe. Apuntad cuántas pistas habéis usado.

## ➡️ Siguiente

¡Reto terminado! 🎉 Continuamos con el [Sprint 5](../../../../S05/README.md).
