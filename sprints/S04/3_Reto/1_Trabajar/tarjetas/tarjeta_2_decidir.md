# Misión 2 · Decidir y repetir
*Contar con `if` y `for`.*

| | |
|---|---|
| ⏱ **Cuándo** | Martes · 50 min |
| 👥 **Cómo** | Piloto y copiloto (cambiad de papel) |
| 🧰 **Usáis** | 🌐 el navegador (el curso) · 📄 `mision_2_decidir.py` · 💻 la terminal |
| 🏁 **Al terminar** | «✅ ¡Misión 2 superada!» en la terminal |

**En esta tarjeta:** [Qué lograréis](#-qué-lograréis) · [La idea en un minuto](#-la-idea-en-un-minuto) · [Paso a paso](#-paso-a-paso) · [Misión terminada cuando](#-misión-terminada-cuando) · [Si os atascáis](#-si-os-atascáis) · [Siguiente](#-siguiente)

← [Volver al índice de misiones](../README.md)

## 🎯 Qué lograréis

Los **contadores** que hay detrás de todos los KPI: contar las reservas canceladas, sumar noches y contar reservas por canal. Es **la base de todo el reto**: lo que viene después es meter esto dentro de funciones.

## 💡 La idea en un minuto

**Contar es siempre lo mismo: una variable que empieza en `0`, un `for` que recorre y un `if` que suma `1` cuando toca.** Como contar a mano las reservas de una noche: marcador a cero, fichas una a una y, cada vez que veis una de una noche, sumáis uno.

```python
de_una_noche = 0                       # 1. el marcador empieza en cero
for reserva in RESERVAS:               # 2. coge las fichas una a una
    if reserva["noches"] == 1:         # 3. ¿es de una noche?
        de_una_noche = de_una_noche + 1    # 4. solo entonces, suma uno
```

- **Sumar** en vez de contar: en lugar de `+ 1`, se suma el dato (`total = total + reserva["noches"]`).
- **Contar por grupos** (por canal): `por_canal[canal] = por_canal.get(canal, 0) + 1` se lee «lo que llevo de ese canal, o `0` si todavía no lo he visto; le sumo 1 y lo guardo». Mirad cómo lo hace [`demo_cliente.py`](../reto_herramientas/demo_cliente.py).

## 👣 Paso a paso

| # | Tipo | Qué hacéis | Dónde | Min | Está terminado cuando |
|---|---|---|---|---|---|
| 1 | 📚 Aprender | `if / elif / else` (ejercicios 1 y 2) | Curso: [`elif`](https://www.curso.soultechlabs.io/basico/#elif) | 10 | Los dos ejercicios en verde |
| 2 | 📚 Aprender | `for` (los 3 ejercicios) | Curso: [`for`](https://www.curso.soultechlabs.io/basico/#for) | 15 | Los tres ejercicios en verde |
| 3 | 🛠️ Construir | Completar los cuatro apartados con los contadores (ver «Paso 3», abajo). Usa las 8 reservas de ejemplo | [`mision_2_decidir.py`](../reto_herramientas/mision_2_decidir.py) (datos: [`reservas_demo.py`](../reto_herramientas/reservas_demo.py)) | 20 | Ya no queda ningún `TODO` |
| 4 | ✅ Comprobar | Ejecutarlo **después de cada apartado**. Si falla uno, el mensaje dice qué esperaba y qué obtuvo | Terminal: `python mision_2_decidir.py` | 5 | «✅ ¡Misión 2 superada!» |

### Paso 3 · Los cuatro apartados de `mision_2_decidir.py`

| Apartado | Qué pide | Cómo pensarlo |
|---|---|---|
| 2.1 | Contar las reservas **canceladas** | El patrón de arriba, con `cancelada == 1` |
| 2.2 | Sumar las **noches** de las **no** canceladas | Un `for` con `if cancelada == 0` que suma `reserva["noches"]` |
| 2.3 | Contar las reservas **por canal** | El diccionario con `.get(canal, 0) + 1` |
| 2.4 | Hacer una **lista** con el canal de las confirmadas de **3 noches o más** | Un `if` con dos condiciones unidas por `and` y `largas.append(...)` |

## ✅ Misión terminada cuando

- [ ] `python mision_2_decidir.py` termina con **«✅ ¡Misión 2 superada!»**.

Por el camino: al empezar sale `Misión 2: N de 4 apartados bien` y los que faltan. Cuando están bien, los resultados son: **3 canceladas**, **12 noches** confirmadas, `{'directo': 3, 'agencia': 2, 'web_intermediaria': 3}` y `['agencia', 'directo']`.

## 🚑 Si os atascáis

| Qué pasa | Por qué | Qué hacer |
|---|---|---|
| `NameError: name 'canceladas' is not defined` | Falta crear el contador **antes** del `for` | Escribid `canceladas = 0` encima del bucle |
| `IndentationError` | Lo que va dentro del `for` o del `if` debe estar **más a la derecha** | Cuatro espacios por nivel; mirad cómo está en `demo_cliente.py` |
| El contador sale siempre 0 (o siempre 8) | El `+ 1` está fuera del `if`, o usáis `=` donde va `==` | Comparar es `==`; asignar es `=` |
| Cuenta de más al sumar noches | Se incluyen las canceladas | Solo `cancelada == 0` |
| Seguís sin verlo | A veces pasa | 1) Preguntad al equipo; 2) después, al docente; 3) **cuando hayáis terminado o agotado las pistas**, contrastad con el [solucionario de la misión 2](../../3_Consultar/Solucionario_misiones.md) (se publica al acabar la clase el martes). Primero intentadlo: lo que copiéis, tenéis que saber explicarlo |

## 👉 Siguiente

[Misión 3 · Funciones que calculan](tarjeta_3_funciones.md): meteréis estos contadores dentro de funciones y las pruebas os dirán si están bien.
