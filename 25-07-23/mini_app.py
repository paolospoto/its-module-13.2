import streamlit as st
import pandas as pd

st.session_state.setdefault("nome", "")
st.session_state.setdefault("età", 0)
st.session_state.setdefault("genere", "Maschio")

nome = st.text_input("Nome", value=st.session_state.nome)
età = st.number_input("Età", min_value=0, value=st.session_state.età)
genere = st.selectbox("Genere", ["Maschio", "Femmina"], index=0)

st.session_state.nome = nome
st.session_state.età = età
st.session_state.genere = genere

st.divider()

st.session_state.setdefault("pressione", 120)
st.session_state.setdefault("glicemia", 90)

pressione = st.slider("Pressione sistolica (mmHg)", 80,
                      200, value=st.session_state.pressione)
glicemia = st.slider("Glicemia a digiuno (mg/dL)", 70,
                     200, value=st.session_state.glicemia)

st.session_state.pressione = pressione
st.session_state.glicemia = glicemia

st.divider()


def calcola_rischio(pressione, glicemia):
    if pressione > 140 or glicemia > 126:
        return "Alto"
    else:
        return "Normale"


rischio = calcola_rischio(pressione, glicemia)


st.session_state.setdefault("dati", [])

if st.button("Salva valutazione"):
    st.session_state.dati.append({
        "nome": nome,
        "età": età,
        "genere": genere,
        "pressione": pressione,
        "glicemia": glicemia,
        "rischio": rischio
    })

st.divider()


if st.session_state.dati:
    df = pd.DataFrame(st.session_state.dati)
    st.dataframe(df)

if st.button("Reset"):
    st.session_state.dati = []
    st.rerun()
