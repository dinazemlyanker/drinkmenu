import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image

import io

st.title('Drink Menu')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv('drinks.csv', nrows=nrows)
    return data


data = load_data(46)
with st.sidebar:
    vibe_choice = option_menu("Vibe", ["All", "Fruity", "Creamy", "Boozy", "Light", "Bubbly",
                                       "Floral", "Herbal", "Shot", "Smokey", "Warm", "Extras"],
                              menu_icon="app-indicator", default_index=0,
                              styles={
                                  "container": {"padding": "5!important", "background-color": "#023020"},
                                  "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                               "--hover-color": "#000000"},
                                  "nav-link-selected": {"background-color": "#02ab21"},
                              }
                              )
with st.sidebar:
    alc_choice = option_menu("Base Alcohol", ["All", "Vodka", "Gin", "Rum", "Whiskey", "Bourbon", "Aperitif",
                                              "Liqueur", "Mezcal", "Wine", "Cognac", "Beer"],
                             menu_icon="app-indicator", default_index=0,
                             styles={
                                 "container": {"padding": "5!important", "background-color": "#023020"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                              "--hover-color": "#000000"},
                                 "nav-link-selected": {"background-color": "#02ab21"},
                             }
                             )
if vibe_choice != 'All':
    filtered_for_choices = data[data[vibe_choice] == True]
else:
    filtered_for_choices = pd.DataFrame.copy(data)
filtered_copy = pd.DataFrame.copy(filtered_for_choices)
if alc_choice != 'All':
    filtered_for_secondary_choice = filtered_copy[filtered_copy['Base Alc'] == alc_choice.lower()]
else:
    filtered_for_secondary_choice = pd.DataFrame.copy(filtered_copy)

for _, drink in filtered_for_secondary_choice.iterrows():
    if st.button(drink['name']):
        # Open a new page to display the filtered DataFrame
        st.write('## ' + drink['name'])
        # Display ingredients of this drink
        st.write(drink['Ingredient 1'])
        st.write(drink['Ingredient 2'])
        st.write(drink['Ingredient 3'])

