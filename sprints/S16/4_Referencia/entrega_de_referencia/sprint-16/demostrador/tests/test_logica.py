"""Pruebas de sentido común del demostrador. Ejecutar desde la carpeta demostrador/ con:  pytest -q"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logica import cargar_modelo, cerca_de_festivo, predecir_dia, validar_entrada  # noqa: E402

LABORABLE = "2012-11-14"      # miércoles normal
SABADO = "2012-12-08"
VISPERA = "2012-12-24"        # víspera de Navidad


@pytest.fixture(scope="module")
def datos():
    try:
        return cargar_modelo()
    except FileNotFoundError:
        pytest.skip("Falta la carpeta modelo/: ejecuta antes notebooks/04_evaluacion.ipynb")


@pytest.mark.parametrize("fecha", [LABORABLE, SABADO, VISPERA])
def test_tres_entradas_normales(datos, fecha):
    modelo, meta, historico = datos
    r = predecir_dia(fecha, modelo, meta, historico)
    assert r["errores"] == [] and len(r["prevision"]) == 24 and "aviso" in r
    assert all(v >= 0 for v in r["prevision"])
    assert all(lo <= p <= hi for lo, p, hi in zip(r["minimo"], r["prevision"], r["maximo"]))


def test_entrada_imposible(datos):
    _, meta, _ = datos
    assert any("entre" in e for e in validar_entrada("2020-01-01", None, 0, meta))
    assert validar_entrada(LABORABLE, 9, 0, meta)
    assert validar_entrada(LABORABLE, None, 50, meta)


def test_entrada_vacia_o_rara(datos):
    modelo, meta, historico = datos
    assert predecir_dia(None, modelo, meta, historico)["errores"] == ["Falta la fecha del día que quieres prever."]
    assert any("No entiendo" in e for e in predecir_dia("mañana", modelo, meta, historico)["errores"])


def test_el_aviso_viaja_con_cada_respuesta(datos):
    modelo, meta, historico = datos
    r = predecir_dia(LABORABLE, modelo, meta, historico)
    assert "orientativa" in r["aviso"] and "persona" in r["aviso"]


def test_sentido_comun_la_madrugada_pide_menos_que_la_hora_punta(datos):
    modelo, meta, historico = datos
    r = predecir_dia(LABORABLE, modelo, meta, historico)
    assert r["prevision"][3] < r["prevision"][8] and r["prevision"][3] < r["prevision"][17]


def test_sentido_comun_la_lluvia_recorta_la_demanda(datos):
    modelo, meta, historico = datos
    seco = predecir_dia(LABORABLE, modelo, meta, historico, tiempo=1)
    lluvia = predecir_dia(LABORABLE, modelo, meta, historico, tiempo=3)
    assert lluvia["total_previsto"] < seco["total_previsto"]
    assert any("Lluvia" in a for a in lluvia["advertencias"])


def test_avisa_cerca_de_festivo_y_no_en_un_dia_normal(datos):
    modelo, meta, historico = datos
    assert cerca_de_festivo(VISPERA) and not cerca_de_festivo(LABORABLE)
    assert predecir_dia(VISPERA, modelo, meta, historico)["advertencias"]
    assert predecir_dia(LABORABLE, modelo, meta, historico)["advertencias"] == []


def test_coincide_con_la_prevision_del_cuaderno(datos):
    modelo, meta, historico = datos
    ej = meta["ejemplo"]
    r = predecir_dia(ej["fecha"], modelo, meta, historico)
    assert r["prevision"] == pytest.approx(ej["prevision"], abs=0.1)
