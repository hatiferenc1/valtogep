import streamlit as st
import pandas as pd 
import numpy as np

level = st.slider("válassz egy számot", 1, 16)
st.text(format(2**level))


 hatvany = {
   'x' : [i**2 for i in range(hatvanykitevo)]}

dataframe = pd.DataFrame(data)
st.write('This is a line_chart.')
st.line_chart(dataframe)







