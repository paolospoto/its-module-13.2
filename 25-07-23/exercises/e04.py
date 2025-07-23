# Use a selectbox to choose from a list of animals
# Display a message about the chosen animal
import streamlit as st

animal = st.selectbox("Scegli animali:", ["Cane", "Gatto", "Coccodrillo"])

match animal:
    case "Cane":
        st.write("Bau")
    case "Gatto":
        st.write("Miao")
    case _:
        st.write("Boh..")
