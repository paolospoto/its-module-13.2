# Ask for weight (kg) and height (m)
# Display the Body Mass Index (weight / height * height)
import streamlit as st

weight = st.number_input("Inserire peso")
height = st.number_input("Inserire altezza")

bmi = weight / (height * height)

st.write(bmi)
