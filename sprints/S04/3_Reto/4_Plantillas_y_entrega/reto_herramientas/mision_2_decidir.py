"""MISIÓN 2 · Decidir y repetir (if y for).

Aquí no copias funciones hechas: escribes TÚ los bucles que cuentan. Trabajas con las 8 reservas de ejemplo.
Completa cada TODO (sustituye el `None` por las líneas que faltan) y ejecuta:   python mision_2_decidir.py
"""
from reservas_demo import RESERVAS

# 2.1  Cuenta cuántas reservas están canceladas (cancelada == 1).
canceladas = 0
# TODO: recorre RESERVAS con un for y, con un if, suma 1 a `canceladas` cuando toque.

# 2.2  Suma las noches de las reservas NO canceladas.
noches_confirmadas = 0
# TODO: otro for con un if (cancelada == 0) que sume reserva["noches"].

# 2.3  Cuenta cuántas reservas hay en cada canal, con un diccionario:
#      {"directo": ..., "agencia": ..., "web_intermediaria": ...}
por_canal = {}
# TODO: for reserva in RESERVAS: ... usa  por_canal[canal] = por_canal.get(canal, 0) + 1

# 2.4  Haz una lista con el canal de las reservas CONFIRMADAS de 3 noches o más (en el orden en que aparecen).
largas = []
# TODO: for + if con dos condiciones unidas por `and`, y largas.append(...)

print("Canceladas:", canceladas)
print("Noches confirmadas:", noches_confirmadas)
print("Por canal:", por_canal)
print("Confirmadas de 3 noches o más:", largas)


# ───────────────────────── NO TOCAR: comprobación automática ─────────────────────────
def _comprobar():
    esperado = [
        (canceladas == 3, "2.1  `canceladas` debe valer 3"),
        (noches_confirmadas == 12, "2.2  `noches_confirmadas` debe valer 12"),
        (por_canal == {"directo": 3, "agencia": 2, "web_intermediaria": 3},
         "2.3  `por_canal` debe ser {'directo': 3, 'agencia': 2, 'web_intermediaria': 3}"),
        (largas == ["agencia", "directo"], "2.4  `largas` debe ser ['agencia', 'directo']"),
    ]
    fallos = [mensaje for ok, mensaje in esperado if not ok]
    print()
    if fallos:
        print(f"Misión 2: {len(esperado) - len(fallos)} de {len(esperado)} apartados bien. Te faltan:")
        for mensaje in fallos:
            print("   ✗", mensaje)
    else:
        print("✅ ¡Misión 2 superada! Ya sabes contar con if y for: es la base de los KPI.")


_comprobar()
