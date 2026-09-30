"""API local del modelo. Lanzar con:  uvicorn api:app --reload"""
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from logica import cargar_modelo, predecir_reserva

app = FastAPI(title="Riesgo de cancelación · TurisData", version="1.0")
modelo, meta = cargar_modelo()


class Reserva(BaseModel):
    antelacion_dias: int = Field(ge=0, le=1000)
    noches: int = Field(ge=1, le=30)
    adultos: int = Field(ge=1, le=6)
    ninos: int = Field(ge=0, le=6)
    precio_noche: float = Field(ge=20, le=600)
    cliente_repetidor: int = Field(ge=0, le=1)
    cancelaciones_previas: int = Field(ge=0, le=10)
    tipo_habitacion: str
    canal: str
    tarifa: Literal["flexible", "no_reembolsable"]
    deposito: Literal["sin_deposito", "parcial", "total"]


@app.get("/salud")
def salud():
    return {"estado": "ok", "modelo": meta["nombre"], "auc_test": meta["auc_test"]}


@app.post("/predecir")
def predecir(reserva: Reserva):
    resultado = predecir_reserva(reserva.model_dump(), modelo, meta)
    if resultado["errores"]:
        raise HTTPException(status_code=422, detail=resultado["errores"])
    return resultado
