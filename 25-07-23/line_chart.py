import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'valori': [10, 20, 15, 30, 25]
})
st.line_chart(df)
