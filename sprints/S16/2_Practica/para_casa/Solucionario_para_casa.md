# Solucionario · cuadernos completos («para casa») del Sprint 16

- Las soluciones de **todos los ejercicios** de los cuadernos completos `S16_01`, con lo que tiene que salir.
- Úsalo **después de intentarlo**: copiar sin entender no sirve para aprender.
- Si el ejercicio usa azar, entrena un modelo o mide tiempos, **tus cifras pueden diferir un poco** de las del texto; lo que importa es que el cuaderno dé la comprobación por buena.
- Los **mini-retos abiertos** (sin una única respuesta correcta) no llevan solución aquí: se contrastan con el razonamiento y con las cifras del propio cuaderno.

---

## S16_01 · Plantilla de demostrador

### Ejercicio 1 · La lógica, separada de la interfaz

> Las validaciones por campo no detectan **incoherencias entre campos**. Escribe `validar_coherencia(reserva)`
> que devuelva una lista de errores (vacía si todo va bien) con estas dos reglas:
> 1. Si hay niños (`ninos > 0`) tiene que haber al menos un adulto (`adultos >= 1`):
>    error `"Los menores deben viajar con al menos un adulto."`
> 2. Si el importe total (`noches * precio_noche`) supera 5000 €: error que empiece por
>    `"El importe total supera los 5000 €"`.
> *Nota: en el demostrador el campo `adultos` ya exige un mínimo de 1, así que con la interfaz la regla 1 casi nunca salta; aquí la practicas con una reserva de 0 adultos porque esta función es la red de seguridad entre campos.*

```python
def validar_coherencia(reserva):
    errores = []
    if reserva["ninos"] > 0 and reserva["adultos"] < 1:
        errores.append("Los menores deben viajar con al menos un adulto.")
    if reserva["noches"] * reserva["precio_noche"] > 5000:
        errores.append("El importe total supera los 5000 €: revisa las noches y el precio.")
    return errores

err = validar_coherencia({**reserva_ejemplo, "noches": 20, "precio_noche": 400.0})
print("Ejercicio 1 correcto ✔")
```

**Tiene que salir:**

```text
Ejercicio 1 correcto ✔
```

### Ejercicio 2 · La lógica, separada de la interfaz

> Escribe `mensaje_errores(errores)`: recibe una lista de errores y devuelve **un único texto** para mostrar
> al usuario. Debe empezar por `"No se puede calcular todavía:"` y listar cada error en una línea que empiece
> por `"- "`. Si la lista está vacía, devuelve una cadena vacía `""`.

```python
def mensaje_errores(errores):
    if not errores:
        return ""
    return "No se puede calcular todavía:\n" + "\n".join(f"- {e}" for e in errores)

m = mensaje_errores(["A", "B"])
print("Ejercicio 2 correcto ✔")
print(mensaje_errores(logica.validar_reserva({**reserva_ejemplo, "noches": -3, "canal": "telepatia"}, meta_cargado)))
```

**Tiene que salir:**

```text
Ejercicio 2 correcto ✔
No se puede calcular todavía:
- 'noches' debe estar entre 1 y 30 (has escrito -3).
- 'telepatia' no es un valor válido para 'canal'. Opciones: agencia, directo, empresa, web_intermediaria.
```

### Ejercicio 3 · Pruebas de sentido común

> Define dos reservas completas (diccionarios con los 11 campos, como `reserva_ejemplo`):
> `reserva_riesgo_alto` (mucha antelación, sin depósito, tarifa flexible, canal `web_intermediaria`) y
> `reserva_riesgo_bajo` (poca antelación, depósito total, tarifa no reembolsable, canal `directo`).
> Calcula sus probabilidades en `p_alto` y `p_bajo` con `logica.predecir_reserva`.

```python
reserva_riesgo_alto = {**reserva_ejemplo, "antelacion_dias": 250, "deposito": "sin_deposito", "tarifa": "flexible", "canal": "web_intermediaria"}
reserva_riesgo_bajo = {**reserva_ejemplo, "antelacion_dias": 7, "deposito": "total", "tarifa": "no_reembolsable", "canal": "directo"}
p_alto = logica.predecir_reserva(reserva_riesgo_alto, modelo_cargado, meta_cargado)["probabilidad"]
p_bajo = logica.predecir_reserva(reserva_riesgo_bajo, modelo_cargado, meta_cargado)["probabilidad"]

print(f"Ejercicio 3 correcto ✔ — riesgo alto {p_alto:.0%} · riesgo bajo {p_bajo:.0%}")

# Estas pruebas se guardarían tal cual en tests/test_logica.py (se ejecutan con:  pytest -q)
def test_reserva_valida_devuelve_probabilidad():
    r = logica.predecir_reserva(reserva_ejemplo, modelo_cargado, meta_cargado)
    assert 0 <= r["probabilidad"] <= 1 and r["nivel"] in ("bajo", "medio", "alto") and "aviso" in r

def test_entrada_invalida_no_rompe():
    r = logica.predecir_reserva({**reserva_ejemplo, "noches": -3}, modelo_cargado, meta_cargado)
    assert r["errores"] and "probabilidad" not in r

def test_falta_un_campo():
    incompleta = {k: v for k, v in reserva_ejemplo.items() if k != "canal"}
    assert any("canal" in e for e in logica.validar_reserva(incompleta, meta_cargado))

def test_sentido_comun():
    assert p_alto > p_bajo

for prueba in (test_reserva_valida_devuelve_probabilidad, test_entrada_invalida_no_rompe, test_falta_un_campo, test_sentido_comun):
    prueba()
    print("OK ", prueba.__name__)
```

**Tiene que salir:**

```text
Ejercicio 3 correcto ✔ — riesgo alto 95% · riesgo bajo 4%
OK  test_reserva_valida_devuelve_probabilidad
OK  test_entrada_invalida_no_rompe
OK  test_falta_un_campo
OK  test_sentido_comun
```

