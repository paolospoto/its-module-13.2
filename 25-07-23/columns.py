import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.write("Colonna 1")

with col2:
    st.write("Colonna 2")
