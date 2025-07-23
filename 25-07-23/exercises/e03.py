# Add a button to increment a counter
# Show the current counter value
import streamlit as st

st.session_state.setdefault("counter", 0)

if st.button("Incrementa"):
    st.session_state.counter += 1

st.write(str(st.session_state.counter))
