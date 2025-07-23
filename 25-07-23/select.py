import streamlit as st

opzione = st.selectbox("Scegli un colore", ["Rosso", "Verde", "Blu"])
st.write("Hai scelto:", opzione)
