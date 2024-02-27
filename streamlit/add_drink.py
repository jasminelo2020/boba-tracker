import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
json_path = 'client_secret_29793288865-kjg9u0r7m42ntk6g2nh5l4615ak9o3h5.apps.googleusercontent.com.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
client = gspread.authorize(creds)

# Open the spreadsheet
sheet = client.open("boba tracker").sheet1

# Streamlit form to input data
with st.form("my_form"):
    st.write("Enter details:")
    # Assuming you want to input a name and a score
    name = st.text_input("Name")
    score = st.text_input("Score")
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Insert data into the sheet
        sheet.append_row([name, score])
        st.success("Data submitted!")

if __name__ == "__main__":
    st.run()