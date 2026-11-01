# Misión 2 · Decidir y repetir

> ⏱ **50 minutos** · 🅰️ Fase 1 · martes · 👥 Piloto y copiloto (cambiad de papel) · [Volver al índice](../README.md)
>
> **En esta misión usáis:** 🌐 el navegador (el curso) · 📄 un archivo: `mision_2_decidir.py` · 💻 la terminal

## 🎯 Qué construís

Los **contadores** que hay detrás de todos los KPI: contar las reservas canceladas, sumar noches y contar reservas por canal. Es **la base de todo el reto**: lo que viene después es meter esto dentro de funciones.

## 💡 La idea clave

**Contar es siempre lo mismo: una variable que empieza en `0`, un `for` que recorre y un `if` que suma `1` cuando toca.** Imaginad que contáis a mano las reservas de una sola noche: empezáis con el marcador a cero, cogéis las fichas una a una y, cada vez que veis una de una noche, sumáis uno.

```python
de_una_noche = 0                       # 1. el marcador empieza en cero
for reserva in RESERVAS:               # 2. coge las fichas una a una
    if reserva["noches"] == 1:         # 3. ¿es de una noche?
        de_una_noche = de_una_noche + 1    # 4. solo entonces, suma uno
```

Para **sumar** en vez de contar, en lugar de `+ 1` se suma el dato: `total = total + reserva["noches"]`.

**Contar por grupos** (por canal) necesita un diccionario que va creciendo: una etiqueta por canal y, como valor, cuántas reservas lleva.

```python
por_canal[canal] = por_canal.get(canal, 0) + 1
```

Se lee así: «`por_canal.get(canal, 0)` es lo que llevo de ese canal, o `0` si todavía no lo he visto; le sumo 1 y lo guardo». La primera vez que aparece `directo` empieza en 1; la segunda, pasa a 2. (Mirad cómo lo hace [`demo_cliente.py`](../reto_herramientas/demo_cliente.py).)

## 🛠️ Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| 1 | 📚 Aprender | `if / elif / else` (ejercicios 1 y 2) | Curso: [`elif`](https://www.curso.soultechlabs.io/basico/#elif) | 10 | Los dos ejercicios en verde |
| 2 | 📚 Aprender | `for` (los 3 ejercicios) | Curso: [`for`](https://www.curso.soultechlabs.io/basico/#for) | 15 | Los tres ejercicios en verde |
| 3 | 🛠️ Construir | Completar los cuatro apartados con los contadores (detalle abajo). Usa las 8 reservas de ejemplo | [`mision_2_decidir.py`](../reto_herramientas/mision_2_decidir.py) (datos: [`reservas_demo.py`](../reto_herramientas/reservas_demo.py)) | 20 | Ya no queda ningún `TODO` |
| 4 | ✅ Comprobar | Ejecutarlo **después de cada apartado**. Si falla uno, el mensaje dice qué esperaba y qué obtuvo | Terminal: `python mision_2_decidir.py` | 5 | «✅ ¡Misión 2 superada!» |

### Detalle del paso 3: los cuatro apartados de `mision_2_decidir.py`

| Apartado | Qué pide | Cómo pensarlo |
|---|---|---|
| 2.1 | Contar las reservas **canceladas** | El patrón de arriba, con `cancelada == 1` |
| 2.2 | Sumar las **noches** de las **no** canceladas | Un `for` con `if cancelada == 0` que suma `reserva["noches"]` |
| 2.3 | Contar las reservas **por canal** | El diccionario con `.get(canal, 0) + 1` |
| 2.4 | Hacer una **lista** con el canal de las confirmadas de **3 noches o más** | Un `if` con dos condiciones unidas por `and` y `largas.append(...)` |

## 👀 Qué deberíais ver

Al empezar, `Misión 2: N de 4 apartados bien` y los que faltan. Cuando están bien, los resultados son: **3 canceladas**, **12 noches** confirmadas, `{'directo': 3, 'agencia': 2, 'web_intermediaria': 3}` y `['agencia', 'directo']`.

## ✅ Hecho cuando

`python mision_2_decidir.py` termina con **«✅ ¡Misión 2 superada!»**.

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| `NameError: name 'canceladas' is not defined` | Falta crear el contador **antes** del `for` | Escribid `canceladas = 0` encima del bucle |
| `IndentationError` | Lo que va dentro del `for` o del `if` debe estar **más a la derecha** | Cuatro espacios por nivel; mirad cómo está en `demo_cliente.py` |
| El contador sale siempre 0 (o siempre 8) | El `+ 1` está fuera del `if`, o usáis `=` donde va `==` | Comparar es `==`; asignar es `=` |
| Cuenta de más al sumar noches | Se incluyen las canceladas | Solo `cancelada == 0` |

## ➡️ Siguiente

[Misión 3 · Funciones que calculan](tarjeta_3_funciones.md): meteréis estos contadores dentro de funciones y las pruebas os dirán si están bien.
