import streamlit as st
import numpy as np
import pandas as pd
# from streamlit_gsheets import GSheetsConnection
import os
# import matplotlib.pyplot as plt

st.write("""
# Jasmine's Boba Tracker
2024 boba tracker
""")

# # Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)

# # df = conn.read()
# df = conn.read(
#     worksheet="boba",
#     ttl="10m",
#     usecols=[0, 1, 2, 3],
#     nrows=None,
# )

# # st.write(df)
# st.dataframe(df)

# enter_boba = st.text_input(label='Enter drink name:', placeholder='format: base with topping 1 and topping 2 (drink name)')

with st.form('boba_tracker', clear_on_submit=True):
    st.header('add a new drink!')

    month, date, location, drink = st.columns([0.2, 0.1, 0.2, 0.5])

    with month:
        a = st.text_input(label='month:', placeholder='eg: january')
    with date:
        a = st.text_input(label='date:', placeholder='eg: 1')
    with location:
        a = st.text_input(label='location:', placeholder='eg: yun')
    with drink:
        enter_boba = st.text_input(label='drink (format: base with topping 1 and topping 2 (drink name); omitting any that don\'t exist):', 
                                   placeholder='eg: jasmine milk tea with boba (snow jasmine)')

#     drink_rating, topping_rating = st.columns(2)
    
    submit_button = st.form_submit_button('submit')
    
    if submit_button:
        st.write('new boba recorded!')

        
st.write("""
## current 2024 boba consumption
""")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
csv_file_path = os.path.join(parent_dir, "data", "boba.csv")
df = pd.read_csv(csv_file_path)

st.write(df)