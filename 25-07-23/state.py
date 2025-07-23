import streamlit as st

st.session_state.setdefault("contatore", 0)

if st.button("Incrementa"):
    st.session_state.contatore += 1

st.write("Valore:", st.session_state.contatore)
