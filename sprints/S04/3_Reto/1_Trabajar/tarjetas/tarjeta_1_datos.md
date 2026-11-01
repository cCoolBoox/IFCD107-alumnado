# Misión 1 · Datos en memoria
*Leer y modificar una lista de reservas.*

| | |
|---|---|
| ⏱ **Cuándo** | Martes · 50 min |
| 👥 **Cómo** | Piloto y copiloto (cambiad de papel respecto a la misión 0) |
| 🧰 **Usáis** | 🌐 el navegador (curso y Taller) · 📄 `mision_1_datos.py` · 💻 la terminal |
| 🏁 **Al terminar** | «✅ ¡Misión 1 superada!» en la terminal |

**En esta tarjeta:** [Qué lograréis](#-qué-lograréis) · [La idea en un minuto](#-la-idea-en-un-minuto) · [Paso a paso](#-paso-a-paso) · [Misión terminada cuando](#-misión-terminada-cuando) · [Si os atascáis](#-si-os-atascáis) · [Siguiente](#-siguiente)

← [Volver al índice de misiones](../README.md)

## 🎯 Qué lograréis

**Leer y modificar** una lista de reservas: saber cuántas hay, mirar un dato de una reserva concreta, cambiarlo y añadir una nueva. Es el «abecé» de todo lo que viene después: los KPI no son más que cálculos sobre esta lista.

## 💡 La idea en un minuto

**Una reserva es una ficha con etiquetas** (un *diccionario*) y **muchas reservas son una caja de fichas** (una *lista*).

```python
reserva = {"canal": "directo", "noches": 2}   # una ficha con etiquetas
reservas = [reserva, otra_reserva]            # la caja de fichas
len(reservas)             # cuántas fichas hay
reservas[0]["canal"]      # de la PRIMERA (se cuenta desde 0), la etiqueta canal
reservas[-1]              # la ÚLTIMA
reserva["noches"] = 3     # cambia lo que pone en esa etiqueta
reservas.append({...})    # mete una ficha nueva al final de la caja
```

`reservas[0]["canal"]` se lee de izquierda a derecha: «de la primera reserva, el canal».

## 👣 Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| 1 | 📚 Aprender | Listas (ejercicios 1 y 2) | Curso: [listas](https://www.curso.soultechlabs.io/basico/#list) | 15 | Los dos ejercicios en verde |
| 2 | 📚 Aprender | Diccionarios (los 3 ejercicios) | Curso: [diccionarios](https://www.curso.soultechlabs.io/basico/#dict) | 10 | Los tres ejercicios en verde |
| 3 | 🛠️ Construir | Sustituir cada `TODO` del archivo (un aviso de «aquí falta algo»): cambiad el `None`, que significa «vacío», o escribid las líneas que faltan. Los seis apartados, en «Paso 3» (abajo) | [`mision_1_datos.py`](../reto_herramientas/mision_1_datos.py) | 13 | Ya no queda ningún `TODO` |
| 4 | ✅ Comprobar | Ejecutarlo **después de cada apartado**, no al final | Terminal: `python mision_1_datos.py` | 2 | «✅ ¡Misión 1 superada!» |
| 5 | 📚 Aprender | «El total de una reserva» y «Un mensaje con f-string»: lo mismo, montado con piezas | Taller: [bloque 1](https://www.curso.soultechlabs.io/taller/#t-total) | 10 | Los dos puzles montados |

### Paso 3 · Los seis apartados de `mision_1_datos.py`

| Apartado | Qué pide | En qué os fijáis |
|---|---|---|
| 1.1 | Guardar **cuántas reservas** hay | `len(...)` |
| 1.2 | El canal de la **primera** reserva | Posición `0` y etiqueta `"canal"` |
| 1.3 | El precio por noche de la **última** | El índice `-1` |
| 1.4 | **Cambiar** a 1 la cancelación de la primera | Una asignación con `=` |
| 1.5 | **Añadir** una reserva nueva al final | `append` con un diccionario completo |
| 1.6 | Un **mensaje** con datos de la segunda reserva | Un `f-string` (el de la misión 0) |

## ✅ Misión terminada cuando

- [ ] `python mision_1_datos.py` termina con **«✅ ¡Misión 1 superada!»**.

Por el camino: al empezar sale `Misión 1: 0 de 6 apartados bien`, con la lista de lo que falta. **Es lo normal.** Cada apartado que arregláis desaparece de la lista.

## 🚑 Si os atascáis

| Qué sale | Por qué | Qué hacer |
|---|---|---|
| `KeyError: 'canl'` | La etiqueta está mal escrita o no existe | Copiad la etiqueta tal cual de la reserva de ejemplo |
| `IndexError: list index out of range` | Esa posición no existe en la lista | Recordad: la primera es `0` y la última `-1` |
| `TypeError` o el apartado sigue en la lista | Dejasteis el `None` o falta una coma o una llave | Releed la línea en voz alta, símbolo a símbolo |
| `ModuleNotFoundError` | La terminal no está en la carpeta del reto | Abridla **dentro** de la carpeta descomprimida |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 1](../../3_Consultar/Solucionario_misiones.md) (se publica al acabar la clase el martes). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |

## 👉 Siguiente

[Misión 2 · Decidir y repetir](tarjeta_2_decidir.md): con los mismos datos, recorreréis la lista y contaréis.
