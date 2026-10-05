"""Pruebas del reto «Herramientas internas».

Ejecuta:   python test_kpis.py        (no necesita pytest)
o bien:    python -m pytest -q        (si lo tienes instalado)

Cada función `test_...` comprueba una parte del script `kpis.py`.
"""
import json
import os
import tempfile
from datetime import date

import kpis

CSV_BUENO = """fecha_llegada,noches,precio_noche,canal,cancelada
2025-01-01,2,100.0,directo,0
2025-01-03,3,80.0,directo,1
2025-01-05,4,50.0,agencia,0
2025-01-10,1,120.0,agencia,0
2025-01-10,5,60.0,web_intermediaria,1
"""

CSV_CON_ERRORES = """fecha_llegada,noches,precio_noche,canal,cancelada
2025-01-01,2,100.0,directo,0
2025-01-02,tres,80.0,directo,1
2025-01-03,4,,agencia,0
no-es-fecha,1,120.0,agencia,0
2025-01-04,2,90.0,,0
2025-01-05,5,60.0,web_intermediaria,1
"""

CSV_SIN_COLUMNA = "fecha_llegada,noches,precio_noche,canal\n2025-01-01,2,100.0,directo\n"


def _escribir(texto):
    """Crea un CSV temporal con `texto` y devuelve su ruta."""
    carpeta = tempfile.mkdtemp()
    ruta = os.path.join(carpeta, "reservas.csv")
    with open(ruta, "w", encoding="utf8", newline="") as f:
        f.write(texto)
    return ruta


def test_leer_reservas_convierte_tipos():
    reservas, avisos = kpis.leer_reservas(_escribir(CSV_BUENO))
    assert len(reservas) == 5, "Debe leer las 5 filas válidas"
    assert avisos == [], "Un CSV correcto no debe generar avisos"
    primera = reservas[0]
    assert primera["noches"] == 2 and isinstance(primera["noches"], int), "noches debe ser int"
    assert primera["precio_noche"] == 100.0 and isinstance(primera["precio_noche"], float), "precio_noche debe ser float"
    assert primera["fecha_llegada"] == date(2025, 1, 1), "fecha_llegada debe ser un objeto date"
    assert primera["cancelada"] == 0 and primera["canal"] == "directo", "cancelada es int y canal es texto"


def test_fichero_inexistente():
    try:
        kpis.leer_reservas(os.path.join(tempfile.mkdtemp(), "no_existe.csv"))
    except FileNotFoundError as error:
        assert "no_existe.csv" in str(error), "El mensaje debe incluir el nombre del fichero"
    else:
        raise AssertionError("Debe lanzar FileNotFoundError si el fichero no existe")


def test_faltan_columnas():
    try:
        kpis.leer_reservas(_escribir(CSV_SIN_COLUMNA))
    except ValueError as error:
        assert "cancelada" in str(error), "El mensaje debe nombrar la columna que falta (cancelada)"
    else:
        raise AssertionError("Debe lanzar ValueError si falta una columna obligatoria")


def test_filas_defectuosas_se_descartan_y_se_avisan():
    reservas, avisos = kpis.leer_reservas(_escribir(CSV_CON_ERRORES))
    assert len(reservas) == 2, f"Solo 2 filas son válidas y has leído {len(reservas)}"
    assert len(avisos) == 4, f"Deben generarse 4 avisos y tienes {len(avisos)}"
    assert all(a.startswith("Fila ") and "descartada" in a for a in avisos), "Cada aviso debe empezar por 'Fila N descartada'"
    assert "Fila 3" in avisos[0], "La primera fila defectuosa es la 3 del fichero (la 1 es la cabecera)"


def test_tasa_cancelacion_por_canal():
    reservas, _ = kpis.leer_reservas(_escribir(CSV_BUENO))
    esperado = {"directo": 50.0, "agencia": 0.0, "web_intermediaria": 100.0}
    assert kpis.tasa_cancelacion_por_canal(reservas) == esperado, f"Debería ser {esperado}"
    assert kpis.tasa_cancelacion_por_canal([]) == {}, "Sin reservas, un diccionario vacío"


def test_ingreso_medio_por_reserva():
    reservas, _ = kpis.leer_reservas(_escribir(CSV_BUENO))
    # confirmadas: 2x100=200, 4x50=200, 1x120=120 -> media 173.33
    assert kpis.ingreso_medio_por_reserva(reservas) == 173.33, "Media de las confirmadas: (200+200+120)/3 = 173.33"
    assert kpis.ingreso_medio_por_reserva([]) == 0.0, "Sin reservas debe devolver 0.0, no error"


def test_ocupacion_proxy():
    reservas, _ = kpis.leer_reservas(_escribir(CSV_BUENO))
    # 7 noches confirmadas / (10 días x 5 habitaciones) = 14.0 %
    assert kpis.ocupacion_proxy(reservas, capacidad_habitaciones=5) == 14.0, "7 / (10 x 5) = 14.0 %"
    assert kpis.ocupacion_proxy([], capacidad_habitaciones=5) == 0.0, "Sin reservas, 0.0"
    try:
        kpis.ocupacion_proxy(reservas, capacidad_habitaciones=0)
    except ValueError:
        pass
    else:
        raise AssertionError("Una capacidad de 0 debe lanzar ValueError (no dividir entre cero)")


def test_exportar_json_y_main():
    entrada = _escribir(CSV_CON_ERRORES)
    salida = os.path.join(os.path.dirname(entrada), "kpis.json")
    assert kpis.main([entrada, salida, "--capacidad", "5"]) == 0, "main debe devolver 0 si todo va bien"
    with open(salida, encoding="utf8") as f:
        datos = json.load(f)
    assert datos["reservas_analizadas"] == 2, "El JSON debe recoger las 2 reservas válidas"
    assert datos["calidad"]["filas_descartadas"] == 4, "El JSON debe informar de las 4 filas descartadas"
    assert "tasa_cancelacion_por_canal_pct" in datos and "ocupacion_proxy_pct" in datos, "Faltan KPIs en el JSON"
    assert kpis.main([os.path.join(tempfile.mkdtemp(), "no_existe.csv"), salida]) == 1, "main debe devolver 1 si el fichero no existe"


def _ruta_datos_reales():
    for candidata in ("reservas_turisdata.csv", os.path.join("datos", "reservas_turisdata.csv"),
                      os.path.join("..", "..", "..", "datos", "reservas_turisdata.csv")):
        if os.path.exists(candidata):
            return candidata
    return None


def test_datos_reales_si_estan_disponibles():
    ruta = _ruta_datos_reales()
    if ruta is None:
        print("   (omitida: no se encuentra reservas_turisdata.csv junto al script)")
        return
    reservas, avisos = kpis.leer_reservas(ruta)
    assert len(reservas) == 6000 and avisos == [], "El CSV de TurisData tiene 6000 reservas válidas"
    tasas = kpis.tasa_cancelacion_por_canal(reservas)
    assert tasas == {"empresa": 43.3, "directo": 31.5, "web_intermediaria": 53.9, "agencia": 44.0}, f"Tasas inesperadas: {tasas}"
    assert kpis.ingreso_medio_por_reserva(reservas) == 576.04, "El ingreso medio de las confirmadas es 576.04"


def test_version_pandas_coincide_si_existe():
    """Opcional: solo se comprueba si has creado kpis_pandas.py."""
    try:
        import kpis_pandas
    except ImportError:
        print("   (omitida: no hay kpis_pandas.py)")
        return
    ruta = _escribir(CSV_BUENO)
    esperado = kpis.calcular_kpis(kpis.leer_reservas(ruta)[0], 5)
    obtenido = kpis_pandas.calcular_kpis_pandas(ruta, 5)
    for clave in ("reservas_analizadas", "ocupacion_proxy_pct", "ingreso_medio_por_reserva", "tasa_cancelacion_por_canal_pct"):
        assert obtenido[clave] == esperado[clave], f"La versión pandas no coincide en {clave}: {obtenido[clave]} frente a {esperado[clave]}"


if __name__ == "__main__":
    pruebas = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    fallos = 0
    for nombre, funcion in pruebas:
        try:
            funcion()
            print(f"[OK]    {nombre}")
        except AssertionError as error:
            fallos += 1
            print(f"[FALLO] {nombre}: {error}")
        except Exception as error:          # cualquier otro error también cuenta
            fallos += 1
            print(f"[ERROR] {nombre}: {type(error).__name__}: {error}")
    print(f"\n{len(pruebas) - fallos} de {len(pruebas)} pruebas superadas")
    raise SystemExit(1 if fallos else 0)
