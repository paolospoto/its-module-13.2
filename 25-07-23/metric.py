import streamlit as st

bpm_ieri = st.number_input("Inserire frequenza media di ieri")
bpm_oggi = st.number_input("Inserire frequenza media di oggi")

st.metric(label="Frequenza Cardiaca", value=bpm_oggi,
          delta=(bpm_oggi - bpm_ieri))
