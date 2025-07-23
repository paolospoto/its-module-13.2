import streamlit as st


def mostra_benvenuto(nome):
    st.write(f"Ciao {nome}, benvenuto!")


nome = st.text_input("Il tuo nome:")
mostra_benvenuto(nome)
