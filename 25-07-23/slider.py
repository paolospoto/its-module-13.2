import streamlit as st

numero = st.slider("Scegli un numero", 0, 100)
st.write("Hai scelto:", str(numero))
