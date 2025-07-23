import streamlit as st


if st.button("Cliccami!", disabled=not st.button("Sblocca secondo bottone")):
    st.write("Hai cliccato il bottone")
