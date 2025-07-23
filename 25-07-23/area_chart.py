import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'valori': [5, 15, 20, 10, 25]
})
st.area_chart(df)
