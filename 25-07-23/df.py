import pandas as pd
import streamlit as st

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [1, 2, 3]})
st.write("Ecco un DataFrame:")
st.dataframe(df)
