#!/usr/bin/env python3
"""Herramientas internas de TurisData: KPIs de reservas a partir de un CSV.   (PLANTILLA)

Uso cuando esté terminado:
    python kpis.py reservas_turisdata.csv salida.json --capacidad 40

Tu trabajo: sustituir cada `raise NotImplementedError` por código que haga lo que dice el docstring.
Ve función a función y ejecuta `python test_kpis.py` después de cada una: verás qué pruebas ya pasan.
Solo se permite la biblioteca estándar (csv, json, argparse, datetime...). La versión con pandas es opcional.
"""
import argparse
import csv
import json
import sys
from datetime import date

COLUMNAS_OBLIGATORIAS = ["fecha_llegada", "noches", "precio_noche", "canal", "cancelada"]


def _convertir_fila(fila):
    """Convierte una fila (diccionario de textos) a tipos Python y valida sus valores.

    Devuelve {"fecha_llegada": date, "noches": int, "precio_noche": float, "canal": str, "cancelada": int}.
    Lanza ValueError con el motivo si la fila no es válida: canal vacío, noches < 1, precio <= 0,
    cancelada distinto de 0/1, o números/fecha que no se pueden convertir.
    Pista: int(), float() y date.fromisoformat() ya lanzan ValueError si el texto no es válido.
    """
    # TODO: implementa la conversión y las validaciones
    raise NotImplementedError("TODO: _convertir_fila")


def leer_reservas(ruta):
    """Lee el CSV y devuelve (reservas, avisos).

    - reservas: lista de diccionarios ya convertidos (usa _convertir_fila).
    - avisos: un texto por fila descartada, con el formato "Fila 3 descartada: <motivo>".
      Numera las filas como en el fichero: la cabecera es la fila 1 y los datos empiezan en la 2.
    - Lanza FileNotFoundError (con la ruta en el mensaje) si el fichero no existe.
    - Lanza ValueError nombrando las columnas que falten de COLUMNAS_OBLIGATORIAS.
    Pista: csv.DictReader, enumerate(lector, start=2) y try/except dentro del bucle.
    """
    # TODO: abre el fichero (encoding="utf8", newline=""), valida la cabecera y recorre las filas
    raise NotImplementedError("TODO: leer_reservas")


def tasa_cancelacion_por_canal(reservas):
    """Devuelve {canal: porcentaje de reservas canceladas, con 1 decimal}. Sin reservas: {}."""
    # TODO: dos diccionarios contadores (total y canceladas) y un cociente por canal
    raise NotImplementedError("TODO: tasa_cancelacion_por_canal")


def ingreso_medio_por_reserva(reservas):
    """Ingreso medio (noches x precio_noche) de las reservas NO canceladas, con 2 decimales.

    Si no hay ninguna reserva confirmada devuelve 0.0 (sin dividir entre cero).
    """
    # TODO
    raise NotImplementedError("TODO: ingreso_medio_por_reserva")


def ocupacion_proxy(reservas, capacidad_habitaciones):
    """Ocupación APROXIMADA en %, con 1 decimal:

        noches de reservas no canceladas / (días del periodo x capacidad_habitaciones) x 100

    - El periodo va de la primera a la última fecha_llegada, ambas incluidas.
    - Es un proxy: todas las noches se cuentan en el periodo aunque la estancia lo desborde.
    - Sin reservas devuelve 0.0. Si la capacidad es <= 0 lanza ValueError.
    """
    # TODO
    raise NotImplementedError("TODO: ocupacion_proxy")


def calcular_kpis(reservas, capacidad_habitaciones):
    """Reúne los KPIs en un diccionario con estas claves (ya montado para ti):"""
    return {
        "reservas_analizadas": len(reservas),
        "ocupacion_proxy_pct": ocupacion_proxy(reservas, capacidad_habitaciones),
        "ingreso_medio_por_reserva": ingreso_medio_por_reserva(reservas),
        "tasa_cancelacion_por_canal_pct": tasa_cancelacion_por_canal(reservas),
    }


def exportar_json(datos, ruta):
    """Guarda `datos` en un JSON con UTF-8 (ensure_ascii=False) y sangría de 2 espacios."""
    # TODO
    raise NotImplementedError("TODO: exportar_json")


def main(argumentos=None):
    """Punto de entrada: devuelve 0 si todo va bien y 1 si hay un error (mensaje claro por stderr).

    Pasos: leer -> calcular KPIs -> añadir al resultado la clave "calidad" con
    {"filas_validas", "filas_descartadas", "avisos"} -> exportar. Captura FileNotFoundError y ValueError.
    """
    parser = argparse.ArgumentParser(description="KPIs de reservas de TurisData")
    parser.add_argument("entrada", help="CSV de reservas")
    parser.add_argument("salida", help="JSON de salida")
    parser.add_argument("--capacidad", type=int, default=40, help="habitaciones disponibles (proxy de ocupación)")
    args = parser.parse_args(argumentos)
    # TODO: usa args.entrada, args.salida y args.capacidad
    raise NotImplementedError("TODO: main")


if __name__ == "__main__":
    sys.exit(main())
