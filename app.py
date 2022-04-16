# Reference: https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030


import streamlit as st
from multipage import MultiPage
from pages import home, data_upload

# Create an instance of the app
app = MultiPage()

# -- Title of the main page, Icon, Website Layout ---
st.set_page_config(page_title="My Website", page_icon=":wave:", layout="wide")

# Add all your applications page here
app.add_page("Home", home.app)
app.add_page("Upload Data", data_upload.app)

# The main app
app.run()