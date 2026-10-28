"""
API local del modelo de cancelaciones (equivale al endpoint de SageMaker).

Ejecución:
    pip install fastapi uvicorn
    uvicorn api_cancelaciones:app --reload
    Abre http://127.0.0.1:8000/docs para probar POST /predecir

Requiere la carpeta modelo_cancelaciones/ creada por el laboratorio S3.5.
"""
import os

import pandas as pd
from autogluon.tabular import TabularPredictor
from fastapi import FastAPI
from pydantic import BaseModel, Field

CARPETA_MODELO = os.environ.get("MODELO", "modelo_cancelaciones")
predictor = TabularPredictor.load(CARPETA_MODELO)
UMBRAL = float(os.environ.get("UMBRAL", "0.5"))

app = FastAPI(title="TurisData · Predicción de cancelaciones", version="1.0")


class Reserva(BaseModel):
    fecha_reserva: str = Field(..., examples=["2025-11-03"])
    fecha_llegada: str = Field(..., examples=["2026-01-15"])
    antelacion_dias: int = Field(..., ge=0)
    noches: int = Field(..., ge=1)
    adultos: int = Field(..., ge=1)
    ninos: int = Field(0, ge=0)
    tipo_habitacion: str
    regimen: str
    canal: str
    pais_origen: str | None = None
    tarifa: str
    deposito: str
    precio_noche: float = Field(..., gt=0)
    peticiones_especiales: int = Field(0, ge=0)
    cliente_repetidor: int = Field(0, ge=0, le=1)
    cancelaciones_previas: int = Field(0, ge=0)


@app.get("/salud")
def salud():
    return {"estado": "ok", "modelo": CARPETA_MODELO}


@app.post("/predecir")
def predecir(reserva: Reserva):
    fila = pd.DataFrame([reserva.model_dump()])
    fila["fecha_reserva"] = pd.to_datetime(fila["fecha_reserva"])
    fila["fecha_llegada"] = pd.to_datetime(fila["fecha_llegada"])
    probabilidad = float(predictor.predict_proba(fila)[1].iloc[0])
    return {
        "probabilidad_cancelacion": round(probabilidad, 4),
        "alerta": probabilidad >= UMBRAL,
        "umbral": UMBRAL,
    }
