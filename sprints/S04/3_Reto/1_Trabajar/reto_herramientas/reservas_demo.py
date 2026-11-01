"""Datos de ejemplo para las misiones 0 a 3 del reto «Herramientas internas».

Son 8 reservas ya preparadas EN MEMORIA (sin fichero): una lista de diccionarios.
No hace falta cambiar nada aquí; se usa con:    from reservas_demo import RESERVAS
"""
from datetime import date

RESERVAS = [
    {"fecha_llegada": date(2025, 1, 1),  "noches": 2, "precio_noche": 100.0, "canal": "directo",           "cancelada": 0},
    {"fecha_llegada": date(2025, 1, 3),  "noches": 3, "precio_noche": 80.0,  "canal": "directo",           "cancelada": 1},
    {"fecha_llegada": date(2025, 1, 5),  "noches": 4, "precio_noche": 50.0,  "canal": "agencia",           "cancelada": 0},
    {"fecha_llegada": date(2025, 1, 10), "noches": 1, "precio_noche": 120.0, "canal": "agencia",           "cancelada": 0},
    {"fecha_llegada": date(2025, 1, 10), "noches": 5, "precio_noche": 60.0,  "canal": "web_intermediaria", "cancelada": 1},
    {"fecha_llegada": date(2025, 1, 12), "noches": 2, "precio_noche": 90.0,  "canal": "web_intermediaria", "cancelada": 0},
    {"fecha_llegada": date(2025, 1, 15), "noches": 3, "precio_noche": 70.0,  "canal": "directo",           "cancelada": 0},
    {"fecha_llegada": date(2025, 1, 20), "noches": 2, "precio_noche": 110.0, "canal": "web_intermediaria", "cancelada": 1},
]
