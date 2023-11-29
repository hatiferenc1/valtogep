import streamlit as st


level = st.slider(".slider: Select the level", 1, 5)

st.text('Selected: {}'.format(level))
