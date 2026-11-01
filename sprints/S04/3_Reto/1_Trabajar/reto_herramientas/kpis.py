#!/usr/bin/env python3
"""Herramientas internas de TurisData: KPIs de reservas a partir de un CSV.   (PLANTILLA)

Uso cuando esté terminado:
    python kpis.py reservas_turisdata.csv salida.json --capacidad 40

El reto se hace en DOS FASES. Cada función tiene una marca que dice cuándo toca:

    FASE 1 · martes · misión 3   →  tasa_cancelacion_por_canal, ingreso_medio_por_reserva, ocupacion_proxy
                                    (trabajas con reservas ya en memoria, sin ficheros)
                                    Prueba:  python test_kpis.py 1
    FASE 2 · miércoles · misiones 4 y 5  →  _convertir_fila, leer_reservas, exportar_json, main
                                    (ficheros, errores y JSON)
                                    Prueba:  python test_kpis.py 2

Tu trabajo: sustituir cada `raise NotImplementedError` por código que haga lo que dice el docstring.
Los comentarios «Paso» te dicen en qué orden pensarlo; el código lo escribes tú.
Ve función a función y ejecuta las pruebas después de cada una: verás qué pruebas ya pasan.
Solo se permite la biblioteca estándar (csv, json, argparse, datetime...). La versión con pandas es opcional.
"""
import argparse
import csv
import json
import sys
from datetime import date

COLUMNAS_OBLIGATORIAS = ["fecha_llegada", "noches", "precio_noche", "canal", "cancelada"]


# ════════════════════════════════════════════════════════════════════════════════════════════════
#  FASE 1 · MARTES · MISIÓN 3 · Funciones que calculan   (las reservas ya están en memoria)
#  Una reserva es un diccionario: {"fecha_llegada": date, "noches": int, "precio_noche": float,
#                                   "canal": str, "cancelada": 0 o 1}.   Las reservas son una lista de ellos.
# ════════════════════════════════════════════════════════════════════════════════════════════════

def tasa_cancelacion_por_canal(reservas):
    """Devuelve {canal: porcentaje de reservas canceladas, con 1 decimal}. Sin reservas: {}.

    Ejemplo: 3 reservas del canal "web", 1 cancelada  ->  {"web": 33.3}
    """
    # Paso 1: crea dos diccionarios vacíos: total = {} (reservas por canal) y canceladas = {} (canceladas por canal).
    # Paso 2: recorre las reservas con un for; por cada una, suma 1 al total de su canal
    #         y, si cancelada vale 1, suma 1 a las canceladas de su canal.  (Pista: total.get(canal, 0) + 1)
    # Paso 3: construye y devuelve el diccionario con el porcentaje de cada canal: round(100 * ... / ..., 1)
    raise NotImplementedError("TODO (misión 3): tasa_cancelacion_por_canal")


def ingreso_medio_por_reserva(reservas):
    """Ingreso medio (noches x precio_noche) de las reservas NO canceladas, con 2 decimales.

    Si no hay ninguna reserva confirmada devuelve 0.0 (sin dividir entre cero).
    """
    # Paso 1: crea una lista vacía y añade noches * precio_noche de cada reserva que NO esté cancelada.
    # Paso 2: si la lista está vacía, devuelve 0.0.
    # Paso 3: si no, devuelve la media con 2 decimales:  round(sum(lista) / len(lista), 2)
    raise NotImplementedError("TODO (misión 3): ingreso_medio_por_reserva")


def ocupacion_proxy(reservas, capacidad_habitaciones):
    """Ocupación APROXIMADA en %, con 1 decimal:

        noches de reservas no canceladas / (días del periodo x capacidad_habitaciones) x 100

    - El periodo va de la primera a la última fecha_llegada, ambas incluidas.
    - Es un proxy: todas las noches se cuentan en el periodo aunque la estancia lo desborde.
    - Sin reservas devuelve 0.0. Si la capacidad es <= 0 lanza ValueError.
    """
    # (Esta función es de nivel estándar: el docente la hace contigo en el nivel mínimo.)
    # Paso 1: si la capacidad es <= 0, raise ValueError("La capacidad debe ser mayor que 0").
    # Paso 2: si no hay reservas, devuelve 0.0.
    # Paso 3: días del periodo = (última llegada - primera llegada).days + 1   (usa max() y min() sobre las fechas)
    # Paso 4: suma las noches de las reservas no canceladas.
    # Paso 5: aplica la fórmula y redondea a 1 decimal.
    raise NotImplementedError("TODO (misión 3): ocupacion_proxy")


def calcular_kpis(reservas, capacidad_habitaciones):
    """Reúne los KPIs en un diccionario con estas claves (ya montado para ti):"""
    return {
        "reservas_analizadas": len(reservas),
        "ocupacion_proxy_pct": ocupacion_proxy(reservas, capacidad_habitaciones),
        "ingreso_medio_por_reserva": ingreso_medio_por_reserva(reservas),
        "tasa_cancelacion_por_canal_pct": tasa_cancelacion_por_canal(reservas),
    }


# ════════════════════════════════════════════════════════════════════════════════════════════════
#  FASE 2 · MIÉRCOLES · MISIÓN 4 · Leer el CSV
# ════════════════════════════════════════════════════════════════════════════════════════════════

def _convertir_fila(fila):
    """Convierte una fila (diccionario de textos) a tipos Python y valida sus valores.

    Devuelve {"fecha_llegada": date, "noches": int, "precio_noche": float, "canal": str, "cancelada": int}.
    Lanza ValueError con el motivo si la fila no es válida: canal vacío, noches < 1, precio <= 0,
    cancelada distinto de 0/1, o números/fecha que no se pueden convertir.
    Pista: int(), float() y date.fromisoformat() ya lanzan ValueError si el texto no es válido.
    """
    # Paso 1: convierte cada campo:  noches = int(fila["noches"]),  precio = float(...),  fecha = date.fromisoformat(...)
    # Paso 2: valida que los valores tengan sentido; si no, raise ValueError("noches debe ser >= 1") (un mensaje claro por caso)
    # Paso 3: devuelve el diccionario con los tipos buenos.
    raise NotImplementedError("TODO (misión 4): _convertir_fila")


def leer_reservas(ruta):
    """Lee el CSV y devuelve (reservas, avisos).

    - reservas: lista de diccionarios ya convertidos (usa _convertir_fila).
    - avisos: un texto por fila descartada, con el formato "Fila 3 descartada: <motivo>".
      Numera las filas como en el fichero: la cabecera es la fila 1 y los datos empiezan en la 2.
    - Lanza FileNotFoundError (con la ruta en el mensaje) si el fichero no existe.
    - Lanza ValueError nombrando las columnas que falten de COLUMNAS_OBLIGATORIAS.
    Pista: csv.DictReader, enumerate(lector, start=2) y try/except dentro del bucle.
    """
    # Paso 1: abre el fichero (encoding="utf8", newline="") dentro de un try; si no existe, relanza FileNotFoundError con la ruta.
    # Paso 2: crea el csv.DictReader y comprueba la cabecera (lector.fieldnames): si faltan columnas, ValueError que las nombre.
    # Paso 3: recorre las filas con enumerate(lector, start=2); por cada una, intenta _convertir_fila dentro de un try:
    #         si va bien, la añades a las reservas; si lanza ValueError, añades el aviso "Fila N descartada: motivo" y sigues.
    # Paso 4: devuelve (reservas, avisos).
    raise NotImplementedError("TODO (misión 4): leer_reservas")


# ════════════════════════════════════════════════════════════════════════════════════════════════
#  FASE 2 · MIÉRCOLES · MISIÓN 5 · Guardar y entregar
# ════════════════════════════════════════════════════════════════════════════════════════════════

def exportar_json(datos, ruta):
    """Guarda `datos` en un JSON con UTF-8 (ensure_ascii=False) y sangría de 2 espacios."""
    # Paso 1: abre `ruta` para escribir ("w") con encoding="utf8".
    # Paso 2: json.dump(datos, f, ensure_ascii=False, indent=2)
    raise NotImplementedError("TODO (misión 5): exportar_json")


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
    # Paso 1: dentro de un try: reservas, avisos = leer_reservas(args.entrada)
    # Paso 2: kpis = calcular_kpis(reservas, args.capacidad)   (ya viene hecha)
    # Paso 3: kpis["calidad"] = {"filas_validas": ..., "filas_descartadas": ..., "avisos": ...}   (si hay muchos avisos, guarda 20)
    # Paso 4: exportar_json(kpis, args.salida), imprime un mensaje de éxito y devuelve 0.
    # Paso 5: except (FileNotFoundError, ValueError) as error: imprime "ERROR: ..." por sys.stderr y devuelve 1.
    raise NotImplementedError("TODO (misión 5): main")


if __name__ == "__main__":
    sys.exit(main())
