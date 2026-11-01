# Misión 1 · Los datos en memoria

> ⏱ **50 minutos** · 🅰️ Fase 1 · martes · 👥 Piloto y copiloto (cambiad de papel respecto a la misión 0) · [Volver al índice](../README.md)

## 🎯 Qué construís

Aprendéis a **leer y modificar** una lista de reservas: saber cuántas hay, mirar un dato de una reserva concreta, cambiarlo y añadir una nueva. Es el «abecé» de todo lo que viene después: los KPI no son más que cálculos sobre esta lista.

## 💡 La idea clave

**Una reserva es una ficha con etiquetas** (un *diccionario*) y **muchas reservas son una caja de fichas** (una *lista*).

```python
reserva = {"canal": "directo", "noches": 2, "precio_noche": 100.0, "cancelada": 0}

reserva["noches"]         # 2  → «dame lo que pone en la etiqueta noches»
reserva["noches"] = 3     # cambia lo que pone en esa etiqueta

reservas = [reserva, otra_reserva]   # la caja de fichas

len(reservas)             # cuántas fichas hay
reservas[0]               # la PRIMERA (se empieza a contar en 0, no en 1)
reservas[-1]              # la ÚLTIMA
reservas[0]["canal"]      # de la primera ficha, la etiqueta canal
reservas.append({...})    # mete una ficha nueva al final de la caja
```

Si lo pensáis así, `reservas[0]["canal"]` se lee de izquierda a derecha: «de la primera reserva, el canal».

## 🧰 Antes de tocar el código

**Curso «Python desde cero»** *(25 min)*: [listas](https://www.curso.soultechlabs.io/basico/#list) (ejercicios 1 y 2) y [diccionarios](https://www.curso.soultechlabs.io/basico/#dict) (los 3 ejercicios).

## 🛠️ Paso a paso

1. **Abrid [`mision_1_datos.py`](../reto_herramientas/mision_1_datos.py)** *(15 min)*. Tiene seis apartados con un `TODO` cada uno. El de arriba ya trae la lista de reservas de ejemplo.

   | Apartado | Qué pide | En qué os fijáis |
   |---|---|---|
   | 1.1 | Guardar **cuántas reservas** hay | `len(...)` |
   | 1.2 | El canal de la **primera** reserva | Posición `0` y etiqueta `"canal"` |
   | 1.3 | El precio por noche de la **última** | El índice `-1` |
   | 1.4 | **Cambiar** a 1 la cancelación de la primera | Una asignación con `=` |
   | 1.5 | **Añadir** una reserva nueva al final | `append` con un diccionario completo |
   | 1.6 | Un **mensaje** con datos de la segunda reserva | Un `f-string` (el de la misión 0) |

2. **Sustituid cada `TODO`** (cambiad el `None` o escribid las líneas que faltan) y ejecutad `python mision_1_datos.py` **después de cada apartado**. No esperéis a terminar los seis.
3. **Taller de bloques** *(10 min)*: [bloque 1](https://www.curso.soultechlabs.io/taller/#t-total), «El total de una reserva» y «Un mensaje con f-string». Es lo mismo que acabáis de hacer, pero montado con piezas.

## 👀 Qué deberíais ver

Al empezar: `Misión 1: 0 de 6 apartados bien`, con la lista de lo que falta. **Es lo normal.** Cada apartado que arregláis desaparece de la lista.

## ✅ Hecho cuando

`python mision_1_datos.py` termina con **«✅ ¡Misión 1 superada!»**.

## 🚑 Si os atascáis

| Qué sale | Por qué | Qué hacer |
|---|---|---|
| `KeyError: 'canl'` | La etiqueta está mal escrita o no existe | Copiad la etiqueta tal cual de la reserva de ejemplo |
| `IndexError: list index out of range` | Esa posición no existe en la lista | Recordad: la primera es `0` y la última `-1` |
| `TypeError` o el apartado sigue en la lista | Dejasteis el `None` o falta una coma o una llave | Releed la línea en voz alta, símbolo a símbolo |
| `ModuleNotFoundError` | La terminal no está en la carpeta del reto | Abridla **dentro** de la carpeta descomprimida |

## ➡️ Siguiente

[Misión 2 · Decidir y repetir](tarjeta_2_decidir.md): con los mismos datos, recorreréis la lista y contaréis.
