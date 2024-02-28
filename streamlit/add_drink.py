import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def add_new_drink():
    # Use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    json_path = 'credentials.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
    client = gspread.authorize(creds)

    # Open the spreadsheet
    sheet = client.open("boba tracker").sheet1

    # Streamlit form to input data
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
            enter_boba = st.text_input(label='drink (format: base with topping 1 and topping 2 (drink name); omitting anything that doesn\'t exist):', 
                                       placeholder='eg: jasmine milk tea with boba (snow jasmine)')

    #     drink_rating, topping_rating = st.columns(2)

        submitted = st.form_submit_button('submit')

        if submitted:
            # Insert data into the sheet
            sheet.append_row([name, score])
            st.success('new boba recorded!')