"""Versión OPCIONAL con pandas.  Cópiala como kpis_pandas.py cuando termines la versión estándar.

Objetivo: obtener exactamente los mismos KPIs que kpis.calcular_kpis, con menos código.
La prueba `test_version_pandas_coincide_si_existe` de test_kpis.py lo comprobará.
"""
import pandas as pd


def calcular_kpis_pandas(ruta, capacidad_habitaciones):
    """Devuelve un diccionario con las mismas claves y valores que kpis.calcular_kpis.

    Pistas: pd.read_csv(ruta, parse_dates=["fecha_llegada"]); filtra las confirmadas (cancelada == 0);
    df.groupby("canal")["cancelada"].mean() da la tasa por canal; .round(1) y .to_dict() para el resultado.
    Cuidado: convierte a float/int de Python (float(x), int(x)) para que el JSON se pueda escribir.
    """
    # TODO
    raise NotImplementedError("TODO: calcular_kpis_pandas")
