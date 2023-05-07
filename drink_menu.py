from collections import defaultdict

import streamlit as st
import pandas as pd
import numpy as np
# from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
# from streamlit_star_rating import st_star_rating

import io

st.title('Drink Menu')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv('drinks.csv', nrows=nrows)
    data = data[30:46]
    return data


rating_dict = defaultdict(list)



def write_drink_buttons(df):
    for _, drink in df.iterrows():
        if st.button(drink['name']):
            # Open a new page to display the filtered DataFrame
            st.write('## ' + ':green[' + drink['name'] + ']')
            # Display ingredients of this drink
            ingredient_columns = ['Ingredient 1', "Ingredient 2",
                                  'Ingredient 3', "Ingredient 4",
                                  'Ingredient 5']
            for ingredient in ingredient_columns:
                if not pd.isna(drink[ingredient]):
                    st.markdown(':green[' + drink[ingredient] + ']')
            # stars = st_star_rating('Rate This Drink', 5, 0, 20, key='rating')
            # st.write(stars)
            # rating = st.session_state['rating']
            # rating_dict['name'].append(rating)
    # st.write(rating_dict)


data = load_data(46)


text_search = st.text_input("Search All Drinks", value="", key="text")

# Filter the dataframe using masks
m1 = data["name"].str.lower().str.contains(text_search.lower())
m2 = data["Base Alc"].str.lower().str.contains(text_search.lower())
m3 = data["Ingredient 1"].str.lower().str.contains(text_search.lower())
m4 = data["Ingredient 2"].str.lower().str.contains(text_search.lower())
m5 = data["Ingredient 3"].str.lower().str.contains(text_search.lower())
m6 = data["Ingredient 4"].str.lower().str.contains(text_search.lower())
m7 = data["Ingredient 5"].str.lower().str.contains(text_search.lower())
df_search = data[m1 | m2 | m3 | m4 | m5 | m6 | m7]


def clear_text():
    st.session_state["text"] = ""


st.button(':green[Clear Search]', on_click=clear_text)

if text_search:
    write_drink_buttons(df_search)
else:
    write_drink_buttons(data)

# with st.sidebar:
#     vibe_choice = option_menu("Vibe", ["All", "Fruity", "Creamy", "Boozy", "Light", "Bubbly",
#                                        "Floral", "Herbal", "Shot", "Smokey", "Warm", "Extras",
#                                        "Sharing"],
#                               default_index=0,
#                               styles={
#                                   "container": {"padding": "5!important", "background-color": "#023020"},
#                                   "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
#                                                "--hover-color": "#000000"},
#                                   "nav-link-selected": {"background-color": "#02ab21"},
#                               }
#                               )
# with st.sidebar:
#     alc_choice = option_menu("Base Alcohol", ["All", "Vodka", "Gin", "Rum", "Whiskey", "Bourbon", "Aperitif",
#                                               "Liqueur", "Mezcal", "Wine", "Cognac", "Beer"],
#                              default_index=0,
#                              styles={
#                                  "container": {"padding": "5!important", "background-color": "#023020"},
#                                  "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
#                                               "--hover-color": "#000000"},
#                                  "nav-link-selected": {"background-color": "#02ab21"},
#                              }
#                              )
#
# filtered_for_choices = data[data[vibe_choice] == True]
# filtered_copy = pd.DataFrame.copy(filtered_for_choices)
# if alc_choice != 'All':
#     filtered_for_secondary_choice = filtered_copy[filtered_copy['Base Alc'] == alc_choice.lower()]
# else:
#     filtered_for_secondary_choice = pd.DataFrame.copy(filtered_copy)
#
# if not text_search:
#     write_drink_buttons(filtered_for_secondary_choice)
