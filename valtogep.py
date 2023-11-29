import streamlit as st

level = st.slider(".slider: Select the level", 1, 16)
st.text(format(2**level))

