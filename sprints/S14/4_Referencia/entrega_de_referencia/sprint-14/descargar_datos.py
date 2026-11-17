#!/usr/bin/env python3
"""Descarga el conjunto «Bike Sharing» de la UCI (fichero hour.csv) y lo guarda como data/bicis_horas.csv.

Fuente: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset · Licencia: CC BY 4.0 (citar a Fanaee-T y Gama, 2013).
Uso:  python sprint-14/descargar_datos.py     (desde la raíz del repositorio; tarda unos segundos)
"""
import hashlib
import io
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"
FILAS = 17379                                        # filas de datos del original
HUELLA = "b03a2d02e8c10f435c43c7f0b358b7e34a003afea53dbc37f0183f2763295133"    # sha256 del CSV con saltos de línea \n
DESTINO = Path(__file__).resolve().parent.parent / "data" / "bicis_horas.csv"


def main():
    print("Descargando", URL)
    with urllib.request.urlopen(URL, timeout=60) as r:
        zip_bytes = r.read()
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
        contenido = z.read("hour.csv").replace(b"\r\n", b"\n")      # mismo contenido, saltos de línea de Linux
    filas = contenido.count(b"\n") - 1
    huella = hashlib.sha256(contenido).hexdigest()
    if filas != FILAS or huella != HUELLA:
        raise SystemExit(f"Los datos no coinciden con los esperados (filas {filas}, huella {huella[:12]}…). No se guardan.")
    DESTINO.parent.mkdir(exist_ok=True)
    DESTINO.write_bytes(contenido)
    print(f"Guardado {DESTINO} ({filas} filas, huella {huella[:12]}…)")


if __name__ == "__main__":
    main()
