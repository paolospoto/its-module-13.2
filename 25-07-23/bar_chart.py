import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'valori': [1, 3, 2, 4]
})
st.bar_chart(df)
