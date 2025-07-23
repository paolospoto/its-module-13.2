import streamlit as st

op = st.selectbox("Operazione", ["Somma", "Moltiplica"])
x = st.slider("x", 0, 10)
y = st.slider("y", 0, 10)

if op == "Somma":
    st.write(x + y)
else:
    st.write(x * y)
