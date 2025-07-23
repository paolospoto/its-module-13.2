# Ask the user to enter their name
# Display "Hello, [name]!" under the input
import streamlit as st

nome = st.text_input("Inserisci il nome")
st.write("Ciao, ", nome)
