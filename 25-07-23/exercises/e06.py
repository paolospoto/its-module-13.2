# Ask for a name and score
# Show the updated table after pressing "Add"
import streamlit as st

st.session_state.setdefault("dati", [])

name = st.text_input("Inserire nome")
punteggio = st.number_input("Inserire punteggio")

if st.button("Aggiungi"):
    st.session_state.dati.append({
        "nome": name,
        "score": punteggio
    })

for dato in st.session_state.dati:
    st.write("Nome: ", dato["nome"], "Punteggio: ", dato["score"])
