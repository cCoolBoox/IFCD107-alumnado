# Misión 5 · Guardar y entregar
*Guardar el JSON, ponerlo en marcha con un comando y entregar.*

| | |
|---|---|
| ⏱ **Cuándo** | Miércoles · 25 min + 25 min de entrega |
| 👥 **Cómo** | Piloto y copiloto; en la parte B, repartíos el trabajo |
| 🧰 **Usáis** | 🌐 el navegador (Taller y GitHub) · 📄 `kpis.py` y un `README.md` nuevo · 💻 la terminal |
| 🏁 **Al terminar** | `12 de 12 pruebas superadas`, `salida.json` y la entrega subida |

**En esta tarjeta:** [Qué lograréis](#-qué-lograréis) · [La idea en un minuto](#-la-idea-en-un-minuto) · [Paso a paso](#-paso-a-paso) · [Misión terminada cuando](#-misión-terminada-cuando) · [Si os atascáis](#-si-os-atascáis) · [Kata 2](#-kata-2--leer-un-csv-sin-que-se-rompa) · [Siguiente](#-siguiente)

← [Volver al índice de misiones](../README.md)

## 🎯 Qué lograréis

`exportar_json` y `main`: **la herramienta de verdad**, que se ejecuta con un solo comando, lee el CSV, calcula los tres KPI, avisa si algo está mal y guarda un **JSON** (los mismos datos como diccionarios y listas, escritos en un fichero de texto) que otros sistemas puedan leer. Y después, **la entrega**.

## 💡 La idea en un minuto

**`main` es la receta que encadena todo lo que ya habéis hecho**: leer → calcular → guardar. Las piezas ya existen (`leer_reservas`, `calcular_kpis`, `exportar_json`); `main` solo las pone en orden y decide qué hacer si algo falla:

```
leer_reservas  →  calcular_kpis  →  exportar_json  →  mensaje de éxito  (devuelve 0)
      ↓ si falla el fichero o una columna
      mensaje de error claro por sys.stderr  (devuelve 1)
```

El **código de salida** (0 = bien, 1 = mal) es la forma en que un programa le dice al sistema si ha ido bien. Los errores se escriben por `sys.stderr`, la salida de errores de la terminal. Y un error **no es un `Traceback`** (esas líneas rojas que salen cuando Python se rompe): es un mensaje que entiende cualquiera.

## 👣 Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| **Parte A** | | | | **25** | |
| 1 | 📚 Aprender | «Encadena las funciones» y «Escribe la función principal». Es exactamente vuestro `main` | Taller: [bloque 4](https://www.curso.soultechlabs.io/taller/#t-tuberia) | 8 | Los dos puzles montados |
| 2 | 🛠️ Construir | `exportar_json(datos, ruta)` (ver «Pasos 2 y 3», abajo) | [`kpis.py`](../reto_herramientas/kpis.py) | 4 | La función está escrita |
| 3 | 🛠️ Construir | `main(argumentos=None)` (ver «Pasos 2 y 3», abajo) | `kpis.py` | 8 | La función está escrita |
| 4 | ✅ Comprobar | Ejecutar el programa entero con el CSV real, abrir `salida.json` y pasar todas las pruebas | Terminal: `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` y `python test_kpis.py` | 5 | `salida.json` como en «Misión terminada cuando» y **`12 de 12 pruebas superadas`** |
| **Parte B** | | *(repartíos el trabajo: los pasos 5 y 6 se hacen a la vez)* | | **25** | |
| 5 | ✅ Comprobar | Provocar **a propósito** los tres errores, siempre sobre **copias** del CSV (ver «Paso 5», abajo) | Terminal | 10 | Los tres casos dan lo que dice la tabla |
| 6 | 🛠️ Construir | Copiar `README_PLANTILLA.md` como `README.md` y rellenarlo (apartado 4 de [Entrega y rúbrica](../../2_Entregar/entrega_y_rubrica.md)) | `README.md` | 10 | Otra persona podría ejecutar el proyecto siguiendo solo el README |
| 7 | ✅ Comprobar | Revisión con la rúbrica: **alguien que no escribió esa parte** la revisa y anota el resultado en el README (apartado 3 de Entrega y rúbrica) | `README.md`, sección «Revisión con la rúbrica» | 5 | La sección está rellena |
| 8 | 📤 Entregar | Subir los ficheros del equipo a `sprint-04/` en **tres o más subidas, hechas por personas distintas**; **cada persona** sube su hoja con la autoevaluación (apartado 5 de Entrega y rúbrica); la coevaluación se añade el jueves, tras la review, y se vuelve a subir la hoja | GitHub, carpeta `sprint-04/` | 10 | Están los cuatro ficheros del equipo y una hoja por persona (**4 + N**), con tres *commits* (versiones guardadas) o más |
| 9 | 📤 Entregar | **Jueves** (review de los Sprints 4 y 5, tras la entrega del 5): enseñar el script con el CSV real, el JSON, un error provocado con su mensaje y las pruebas en verde. Explicar **una decisión de diseño** (por ejemplo, cómo definisteis la ocupación) | A la clase | jueves · 3–5 por equipo | Lo habéis enseñado |

Si sobran minutos, empezad el extra (pruebas propias o `extra/plantilla_kpis_pandas.py`).

### Pasos 2 y 3 · `exportar_json` y `main`

1. **`exportar_json(datos, ruta)`**: abrid `ruta` para escribir con `encoding="utf8"` y guardad con `json.dump(datos, f, ensure_ascii=False, indent=2)`. Sin `ensure_ascii=False`, las tildes saldrían como secuencias del estilo `\u00f3` (así se escribe la «ó»). Pista: [`S04_04`](https://colab.research.google.com/github/cCoolBoox/IFCD107-alumnado/blob/main/sprints/S04/2_Practica/S04_04_ficheros_excepciones.ipynb).
2. **`main(argumentos=None)`**: la plantilla ya lee los argumentos (`args.entrada`, `args.salida` y `args.capacidad`). Vosotros, **dentro de un `try`**:
   1. `leer_reservas(args.entrada)`;
   2. `calcular_kpis(reservas, args.capacidad)`, que ya viene hecha;
   3. añadir al resultado la clave `"calidad"` con `filas_validas`, `filas_descartadas` y `avisos` (si hay muchos avisos, guardad solo los 20 primeros);
   4. `exportar_json`;
   5. imprimir un mensaje de éxito y **devolver 0**.

   En el `except (FileNotFoundError, ValueError)`: imprimir `ERROR: …` **por `sys.stderr`** y **devolver 1**.

### Paso 5 · Los tres errores a propósito

| Caso | Cómo se provoca | Qué deberíais ver | Código de salida |
|---|---|---|---|
| 1. Fichero que no existe | `python kpis.py no_existe.csv salida.json` | `ERROR: No se encuentra el fichero: no_existe.csv` | 1 |
| 2. Falta una columna | Copiad el CSV como `sin_col.csv` y, con el editor, cambiad en la primera línea `precio_noche` por `precio`. Ejecutad con `sin_col.csv` | `ERROR: Faltan columnas obligatorias: ['precio_noche']` | 1 |
| 3. Dato incorrecto | Copiad el CSV como `con_error.csv` y, con el editor, escribid `abc` como precio de la fila 5 y `0` como noches de la fila 10. Ejecutad con `con_error.csv` | El programa **no se rompe**: `OK: 5998 reservas analizadas, 2 descartadas -> …` y en `calidad.avisos` aparecen `Fila 5 descartada: …` y `Fila 10 descartada: noches debe ser >= 1` | 0 |

El código de salida se mira justo después de ejecutar: en Linux o Mac, `echo $?`; en Windows (cmd), `echo %errorlevel%`; en PowerShell, `echo $LASTEXITCODE`. **Al terminar, borrad las copias de prueba** (`sin_col.csv`, `con_error.csv` y el JSON de prueba): no se suben. Ese será vuestro «provocar un error» en la review.

## ✅ Misión terminada cuando

- [ ] `python kpis.py reservas_turisdata.csv salida.json --capacidad 40` escribe `OK: 6000 reservas analizadas, 0 descartadas -> salida.json` y deja un `salida.json` con las cifras de abajo.
- [ ] `python test_kpis.py` da **`12 de 12 pruebas superadas`** (con `kpis_pandas.py` ausente, la prueba opcional se omite y cuenta como superada).
- [ ] Los tres errores provocados (paso 5) dan su mensaje.
- [ ] En `sprint-04/` están el README, la revisión con la rúbrica, los cuatro ficheros del equipo y una hoja de autoevaluación por persona (**4 + N**); y en el historial (el icono del reloj), al menos tres *commits* con nombres distintos.
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

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| La ocupación no sale `42.0` | Falta el `+ 1` en los días, se cuentan canceladas o la capacidad no es 40 | Releer la fórmula y ejecutar con `--capacidad 40` |
| Las tildes de `salida.json` salen como `\u00f3` y similares | Falta `ensure_ascii=False` | Añadirlo en `json.dump` |
| Sale un `Traceback` rojo en vez de `ERROR: …` | El `except` no recoge ese tipo de error | `except (FileNotFoundError, ValueError)` |
| `test_exportar_json_y_main` falla | `main` no devuelve 0, o no escribe el fichero | Revisad el `return 0` y la ruta de `args.salida` |
| Un solo *commit* gigante | «Lo subo al final» | Commits pequeños mientras avanzáis; la entrega pide tres o más |
| Cambiar las pruebas para que pasen | Prisa | No se tocan las pruebas dadas; las propias van aparte |
| Queréis usar un asistente de IA | Es una ayuda legítima, con reglas | Seguid las reglas de la [ficha del reto](../../3_Consultar/Reto_Sprint_04.md) y declarad el uso en el README |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 5](../../3_Consultar/Solucionario_misiones.md) (se publica al acabar la clase el miércoles). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |

## 🥋 Kata 2 · Leer un CSV sin que se rompa

⏱ 10 min · 👤 **Individual** · fin del miércoles · [Abrir la kata 2](https://www.curso.soultechlabs.io/taller/#kata-2)

**Cada persona sola**, sin mirar esta tarjeta ni preguntar al equipo: escribid `media_precio(ruta)`, que lee un CSV, ignora las filas defectuosas y devuelve `None` si el fichero no existe. Apuntad **cuántas pistas** habéis usado. Sirve para comprobar que **cada persona** lo ha aprendido, no solo el equipo.

## 👉 Siguiente

¡Reto terminado! 🎉 Continuamos con el [Sprint 5](../../../../S05/README.md).
