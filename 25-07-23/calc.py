import streamlit as st

a = st.number_input("Numero A")
b = st.number_input("Numero B")
if st.button("Somma"):
    st.write("Risultato:", a + b)
