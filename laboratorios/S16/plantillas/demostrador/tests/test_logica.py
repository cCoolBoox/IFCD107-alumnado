"""Pruebas de sentido común del demostrador. Ejecutar desde la carpeta demostrador/ con:  pytest -q"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logica import cargar_modelo, nivel_riesgo, predecir_reserva, validar_reserva  # noqa: E402

RESERVA = {"antelacion_dias": 120, "noches": 5, "adultos": 2, "ninos": 1, "precio_noche": 95.0, "cliente_repetidor": 0,
           "cancelaciones_previas": 0, "tipo_habitacion": "estandar", "canal": "web_intermediaria",
           "tarifa": "flexible", "deposito": "sin_deposito"}   # >>> ADAPTA a los campos de TU proyecto


@pytest.fixture(scope="module")
def modelo_y_meta():
    try:
        return cargar_modelo()
    except FileNotFoundError:
        pytest.skip("Falta la carpeta modelo/: genera el modelo antes de probar")


def test_entrada_valida(modelo_y_meta):
    modelo, meta = modelo_y_meta
    r = predecir_reserva(RESERVA, modelo, meta)
    assert r["errores"] == [] and 0 <= r["probabilidad"] <= 1 and "aviso" in r


def test_entrada_fuera_de_rango(modelo_y_meta):
    _, meta = modelo_y_meta
    assert validar_reserva({**RESERVA, "noches": -3}, meta)


def test_falta_un_campo(modelo_y_meta):
    _, meta = modelo_y_meta
    incompleta = {k: v for k, v in RESERVA.items() if k != "canal"}
    assert any("canal" in e for e in validar_reserva(incompleta, meta))


def test_sentido_comun(modelo_y_meta):
    modelo, meta = modelo_y_meta
    alto = {**RESERVA, "antelacion_dias": 250, "deposito": "sin_deposito", "tarifa": "flexible", "canal": "web_intermediaria"}
    bajo = {**RESERVA, "antelacion_dias": 7, "deposito": "total", "tarifa": "no_reembolsable", "canal": "directo"}
    assert predecir_reserva(alto, modelo, meta)["probabilidad"] > predecir_reserva(bajo, modelo, meta)["probabilidad"]


def test_niveles():
    assert nivel_riesgo(0.1) == "bajo" and nivel_riesgo(0.4) == "medio" and nivel_riesgo(0.8) == "alto"
