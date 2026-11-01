"""MISIÓN 1 · Datos en memoria.

Una reserva es un DICCIONARIO (clave: valor). Muchas reservas son una LISTA de diccionarios.
Completa cada TODO (sustituye el `None` o escribe las líneas que faltan) y ejecuta:   python mision_1_datos.py
Abajo, la comprobación automática te dirá qué has conseguido.
"""
reservas = [
    {"canal": "directo", "noches": 2, "precio_noche": 100.0, "cancelada": 0},
    {"canal": "agencia", "noches": 4, "precio_noche": 50.0, "cancelada": 0},
    {"canal": "web_intermediaria", "noches": 5, "precio_noche": 60.0, "cancelada": 1},
]

# 1.1  Guarda en `cantidad` cuántas reservas hay ahora mismo.      (pista: len(...))
cantidad = None                                                     # TODO

# 1.2  Guarda en `canal_primera` el canal de la PRIMERA reserva.   (pista: reservas[0]["canal"])
canal_primera = None                                                # TODO

# 1.3  Guarda en `precio_ultima` el precio por noche de la ÚLTIMA reserva.   (pista: el índice -1)
precio_ultima = None                                                # TODO

# 1.4  Cambia a 1 la clave "cancelada" de la primera reserva (el cliente la ha cancelado).
#      (pista: reservas[0]["cancelada"] = ...)
# TODO

# 1.5  Añade UNA reserva nueva al final de la lista: canal "directo", 3 noches, 80.0 € la noche, no cancelada.
#      (pista: reservas.append({...}))
# TODO

# 1.6  Guarda en `texto` este mensaje, construido con un f-string a partir de la SEGUNDA reserva (reservas[1]):
#      "La reserva 2 es del canal agencia: 4 noches a 50.0 euros"
texto = None                                                        # TODO

print("Cantidad al empezar:", cantidad)
print("Canal de la primera:", canal_primera)
print("Precio de la última:", precio_ultima)
print("Ahora hay", len(reservas), "reservas")
print(texto)


# ───────────────────────── NO TOCAR: comprobación automática ─────────────────────────
def _comprobar():
    esperado = [
        (cantidad == 3, "1.1  `cantidad` debe valer 3 (cuéntala ANTES de añadir la reserva nueva)"),
        (canal_primera == "directo", "1.2  `canal_primera` debe valer 'directo'"),
        (precio_ultima == 60.0, "1.3  `precio_ultima` debe valer 60.0 (la última de las tres iniciales)"),
        (reservas[0]["cancelada"] == 1, "1.4  la primera reserva debe tener cancelada = 1"),
        (len(reservas) == 4 and reservas[-1] == {"canal": "directo", "noches": 3, "precio_noche": 80.0, "cancelada": 0},
         "1.5  debe haber 4 reservas y la última: canal 'directo', 3 noches, 80.0, cancelada 0"),
        (texto == "La reserva 2 es del canal agencia: 4 noches a 50.0 euros",
         "1.6  `texto` debe ser exactamente: La reserva 2 es del canal agencia: 4 noches a 50.0 euros"),
    ]
    fallos = [mensaje for ok, mensaje in esperado if not ok]
    print()
    if fallos:
        print(f"Misión 1: {len(esperado) - len(fallos)} de {len(esperado)} apartados bien. Te faltan:")
        for mensaje in fallos:
            print("   ✗", mensaje)
    else:
        print("✅ ¡Misión 1 superada! Ya sabes leer y modificar los datos del reto.")


_comprobar()
