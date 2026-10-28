"""
Generador de reservas del cliente ancla TurisData Canarias (datos SINTÉTICOS).

Uso:
    python generar_reservas_turisdata.py            # crea reservas_turisdata.csv (6000 filas)
    python generar_reservas_turisdata.py 20000 7    # 20000 filas, semilla 7

Columnas (objetivo: cancelada, 1 = la reserva se canceló):
    id_reserva, fecha_reserva, fecha_llegada, antelacion_dias, noches, adultos, ninos,
    tipo_habitacion, regimen, canal, pais_origen, tarifa, deposito, precio_noche,
    peticiones_especiales, cliente_repetidor, cancelaciones_previas, cancelada

No incluye ninguna columna posterior al desenlace (sin fuga de datos).
Las relaciones están inventadas para que el modelo tenga algo que aprender:
NO son estadísticas reales del turismo en Canarias.
"""
import sys

import numpy as np
import pandas as pd


def generar(n: int = 6000, semilla: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(semilla)

    # Fechas: las reservas se hacen a lo largo de dos años
    fecha_reserva = pd.Timestamp("2024-01-01") + pd.to_timedelta(
        rng.integers(0, 730, n), unit="D"
    )
    antelacion = np.clip(rng.gamma(shape=2.0, scale=45.0, size=n).round(), 0, 400).astype(int)
    fecha_llegada = fecha_reserva + pd.to_timedelta(antelacion, unit="D")
    noches = np.clip(rng.poisson(4.5, n) + 1, 1, 21)
    adultos = rng.choice([1, 2, 3, 4], n, p=[0.15, 0.6, 0.15, 0.10])
    ninos = rng.choice([0, 1, 2, 3], n, p=[0.7, 0.15, 0.12, 0.03])

    tipo_habitacion = rng.choice(
        ["estandar", "superior", "suite", "familiar"], n, p=[0.5, 0.25, 0.1, 0.15]
    )
    regimen = rng.choice(
        ["solo_alojamiento", "desayuno", "media_pension", "todo_incluido"],
        n, p=[0.15, 0.4, 0.2, 0.25],
    )
    canal = rng.choice(["directo", "web_intermediaria", "agencia", "empresa"], n,
                       p=[0.25, 0.5, 0.2, 0.05])
    pais_origen = rng.choice(
        ["ES", "UK", "DE", "NL", "IT", "FR", "Nordicos", "otros"], n,
        p=[0.28, 0.25, 0.14, 0.06, 0.05, 0.04, 0.08, 0.10],
    )
    tarifa = rng.choice(["flexible", "no_reembolsable"], n, p=[0.6, 0.4])
    deposito = rng.choice(["sin_deposito", "parcial", "total"], n, p=[0.55, 0.3, 0.15])

    base = {"estandar": 70, "superior": 95, "suite": 160, "familiar": 110}
    temporada_alta = pd.Series(fecha_llegada.month).isin([7, 8, 12, 1, 2, 3]).to_numpy()
    precio = (
        np.array([base[t] for t in tipo_habitacion])
        * np.where(temporada_alta, 1.25, 1.0)
        * rng.normal(1.0, 0.08, n)
    ).round(2)

    peticiones = rng.poisson(0.6, n)
    repetidor = rng.choice([0, 1], n, p=[0.85, 0.15])
    canc_previas = np.where(repetidor == 1, rng.poisson(0.4, n), 0)

    # Probabilidad de cancelación (relaciones inventadas)
    z = (
        -1.6
        + 0.012 * antelacion
        + 0.9 * (tarifa == "flexible")
        - 1.4 * (deposito == "total")
        - 0.7 * (deposito == "parcial")
        + 0.5 * (canal == "web_intermediaria")
        - 0.6 * (canal == "directo")
        + 0.25 * (noches > 7)
        + 0.6 * canc_previas
        - 0.35 * repetidor
        - 0.25 * peticiones
        + 0.3 * temporada_alta
        + 0.2 * (pais_origen == "UK")
        - 0.006 * (precio - 100)
    )
    p = 1.0 / (1.0 + np.exp(-z))
    cancelada = (rng.random(n) < p).astype(int)

    df = pd.DataFrame({
        "id_reserva": np.arange(1, n + 1),
        "fecha_reserva": fecha_reserva.date if hasattr(fecha_reserva, "date") else fecha_reserva,
        "fecha_llegada": fecha_llegada.date if hasattr(fecha_llegada, "date") else fecha_llegada,
        "antelacion_dias": antelacion,
        "noches": noches,
        "adultos": adultos,
        "ninos": ninos,
        "tipo_habitacion": tipo_habitacion,
        "regimen": regimen,
        "canal": canal,
        "pais_origen": pais_origen,
        "tarifa": tarifa,
        "deposito": deposito,
        "precio_noche": precio,
        "peticiones_especiales": peticiones,
        "cliente_repetidor": repetidor,
        "cancelaciones_previas": canc_previas,
        "cancelada": cancelada,
    })

    # Un poco de suciedad realista: valores nulos en el país de origen
    nulos = rng.random(n) < 0.02
    df.loc[nulos, "pais_origen"] = np.nan

    return df.sort_values("fecha_reserva").reset_index(drop=True)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    datos = generar(n, semilla)
    datos.to_csv("reservas_turisdata.csv", index=False)
    print(f"Creado reservas_turisdata.csv: {len(datos)} filas, "
          f"{datos['cancelada'].mean():.1%} canceladas")
