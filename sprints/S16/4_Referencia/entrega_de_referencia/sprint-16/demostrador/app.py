"""Demostrador Streamlit · BiciPrevisión. Lanzar desde la raíz del repositorio con:  streamlit run sprint-16/demostrador/app.py"""
from datetime import date

import pandas as pd
import streamlit as st

from logica import TIEMPOS, cargar_modelo, predecir_dia

st.set_page_config(page_title="BiciPrevisión · bicis por hora", layout="centered")


@st.cache_resource
def cargar():
    return cargar_modelo()


st.title("BiciPrevisión: bicis alquiladas hora a hora")
st.caption("Demostrador del proyecto final. Datos reales del sistema de bicis compartidas de Washington D. C. (UCI, CC BY 4.0). "
           "Es una estimación orientativa: la decisión de recolocar bicis la toma una persona.")

try:
    modelo, meta, historico = cargar()
except FileNotFoundError as error:
    st.error(str(error))
    st.stop()

ini, fin = (pd.Timestamp(v).date() for v in meta["rango_fechas"])
with st.form("formulario"):
    c1, c2 = st.columns(2)
    fecha = c1.date_input("Día que quieres prever", value=date(2012, 11, 14), min_value=ini, max_value=fin)
    opciones = ["Usar el clima real de ese día"] + [f"{k} · {v}" for k, v in TIEMPOS.items()]
    eleccion = c2.selectbox("Previsión del tiempo", opciones)
    ajuste = st.slider("Ajuste de la temperatura prevista (°C)", -10.0, 10.0, 0.0, 0.5)
    enviado = st.form_submit_button("Prever el día")

if enviado:
    tiempo = None if eleccion == opciones[0] else int(eleccion[0])
    r = predecir_dia(str(fecha), modelo, meta, historico, tiempo=tiempo, ajuste_temp=ajuste)
    if r["errores"]:
        st.warning("No se puede prever todavía:\n\n" + "\n".join(f"- {e}" for e in r["errores"]))
    else:
        a, b = st.columns(2)
        a.metric("Bicis previstas en el día", f"{r['total_previsto']:,}".replace(",", "."))
        b.metric("Hora de más demanda", f"{r['hora_pico']}:00", f"≈ {r['pico']:.0f} bicis")
        tabla = pd.DataFrame({"Previsión": r["prevision"], "Mínimo probable": r["minimo"], "Máximo probable": r["maximo"]}, index=r["horas"])
        if r["real"] is not None:
            tabla["Real (solo en la demo)"] = r["real"]
        tabla.index.name = "hora"
        st.line_chart(tabla)
        for texto in r["advertencias"]:
            st.warning(texto)
        st.info(r["aviso"])
