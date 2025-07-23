import streamlit as st
import pandas as pd

file = st.file_uploader("Carica un file CSV")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.line_chart(df["Età"])
