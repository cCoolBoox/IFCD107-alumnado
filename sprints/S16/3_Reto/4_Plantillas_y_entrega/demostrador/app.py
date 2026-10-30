"""Demostrador Streamlit · TurisData. Lanzar con:  streamlit run app.py"""
import streamlit as st

from logica import cargar_modelo, predecir_reserva

st.set_page_config(page_title="Riesgo de cancelación · TurisData", layout="centered")


@st.cache_resource
def cargar():
    return cargar_modelo()


st.title("Riesgo de cancelación de una reserva")
st.caption("Demostrador del proyecto. Datos sintéticos de TurisData Canarias (empresa ficticia).")

try:
    modelo, meta = cargar()
except FileNotFoundError as error:
    st.error(str(error))
    st.stop()

with st.form("formulario"):
    reserva = {}
    columnas = st.columns(2)
    for i, (campo, regla) in enumerate(meta["campos"].items()):
        with columnas[i % 2]:
            if regla["tipo"] == "categoria":
                reserva[campo] = st.selectbox(regla["etiqueta"], regla["valores"])
            elif regla["tipo"] == "entero":
                reserva[campo] = st.number_input(regla["etiqueta"], value=int(max(regla["min"], min(regla["max"], 1))), step=1)
            else:
                reserva[campo] = st.number_input(regla["etiqueta"], value=float(regla["min"] + 75.0), step=5.0)
    enviado = st.form_submit_button("Calcular riesgo")

if enviado:
    resultado = predecir_reserva(reserva, modelo, meta)
    if resultado["errores"]:
        st.warning("No se puede calcular todavía:\n\n" + "\n".join(f"- {e}" for e in resultado["errores"]))
    else:
        c1, c2 = st.columns(2)
        c1.metric("Probabilidad de cancelación", f"{resultado['probabilidad']:.0%}", f"{resultado['probabilidad'] - resultado['tasa_base']:+.0%} frente a la media")
        c2.metric("Nivel de riesgo", resultado["nivel"].upper())
        st.progress(resultado["probabilidad"])
        st.info(resultado["aviso"])
