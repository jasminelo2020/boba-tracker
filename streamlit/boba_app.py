import streamlit as st
import numpy as np
# import matplotlib.pyplot as plt

st.write("""
# Jasmine's Boba Tracker
2024 boba tracker
""")

# enter_boba = st.text_input(label='Enter drink name:', placeholder='format: base with topping 1 and topping 2 (drink name)')

with st.form('boba_tracker'):
    st.header('add a new drink!')

    month, date, location, drink = st.columns(4)

    with month:
        a = st.text_input(label='month:', placeholder='eg: january')
    with date:
        a = st.text_input(label='day of month:', placeholder='eg: 1')
    with location:
        a = st.text_input(label='location:', placeholder='eg: yun')
    with drink:
        enter_boba = st.text_input(label='drink (format: base with topping 1 and topping 2 (drink name)):', 
                                   placeholder='eg: jasmine milk tea with boba and pudding (snow jasmine)')

#     drink_rating, topping_rating = st.columns(2)
    
#     submit_button = st.form_submit_button('submit')
    
if st.form_submit_button:
    st.write('new boba recorded!')