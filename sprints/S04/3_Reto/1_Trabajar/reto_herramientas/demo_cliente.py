"""MISIÓN 0 · La demostración del cliente.

TurisData nos ha enviado este programa de ejemplo: así quiere ver sus cifras. Funciona, pero solo con 8
reservas puestas a mano. Nuestro reto es construir la herramienta de verdad (leer un fichero, avisar de los
errores, guardar un JSON...). Antes de escribir nada, hay que ENTENDER esto.

Qué hacer (no hace falta cambiar nada todavía):
  1. Lee el programa de arriba abajo. No te preocupes si no entiendes todo: subraya lo que no entiendas.
  2. Antes de ejecutarlo, ANTICIPA qué cuatro cosas va a imprimir (mira las preguntas de la tarjeta de la misión 0).
  3. Ejecútalo:   python demo_cliente.py        y compara con lo que habías pensado.
"""
from reservas_demo import RESERVAS        # las 8 reservas de ejemplo (una lista de diccionarios)


def ingreso_de(reserva):
    """Dinero que deja una reserva: noches x precio de cada noche."""
    return reserva["noches"] * reserva["precio_noche"]


total = len(RESERVAS)
canceladas = 0
ingreso_total = 0.0
por_canal = {}

for reserva in RESERVAS:
    canal = reserva["canal"]
    por_canal[canal] = por_canal.get(canal, 0) + 1
    if reserva["cancelada"] == 1:
        canceladas += 1
    else:
        ingreso_total += ingreso_de(reserva)

confirmadas = total - canceladas
media = ingreso_total / confirmadas

print("=== Resumen semanal de reservas ===")
print(f"Reservas analizadas: {total}")
print(f"Canceladas: {canceladas} ({100 * canceladas / total:.1f} %)")
print(f"Ingreso medio por reserva confirmada: {media:.2f} €")
for canal, cantidad in por_canal.items():
    print(f"  - {canal}: {cantidad} reservas")
