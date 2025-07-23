import streamlit as st

nome = st.text_input("Come ti chiami?")
if st.toggle("Conferma"):
    st.write("Ciao", nome)
