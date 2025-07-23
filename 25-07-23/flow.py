import streamlit as st

op = st.selectbox(
    "Operazione", ["Somma", "Sottrazione", "Moltiplica", "Divisione"])
x = st.number_input("x")
y = st.number_input("y")

if st.button("Calcola"):
    if op == "Somma":
        st.write(str(x + y))
    elif op == "Sottrazione":
        st.write(str(x - y))
    elif op == "Divisione":
        st.write(str(x / y))
    else:
        st.write(str(x * y))
