import streamlit as st
import pandas as pd
import numpy as np

st.title('Drink Menu')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv('drinks.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")
st.write(data)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)





