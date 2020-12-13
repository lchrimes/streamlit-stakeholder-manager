import streamlit as st
import pandas as pd
from utils.base64_handler import file_to_base64
from pages.stakeholder_search import search
from pages.stakeholder_editor import database_admin

# Changing title page and the favicon - set page call only be called once per app and only at the start
st.set_page_config(page_title='Stakeholder Management')

# Adding sytle sheet
def remote_css(url):
  st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def execute_markdown(markdown):
  st.markdown(markdown, unsafe_allow_html=True)

# font-awsome addition for icons
remote_css("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

# Add some bootstrap css
execute_markdown('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')

# hiding the streamlit menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Databound Logo - Top of Page
st.image("static/images/app_logo.png", use_column_width=True)

#Pages
PAGES = {
  "Stakeholder Search" : search,
  'Stakeholders Database Management' : database_admin,
}

# Slide bar
st.sidebar.title("Navigation")
# Add a selectbox to the sidebar:
page = st.sidebar.selectbox(
    'Page',
    ('Stakeholder Search', 'Stakeholders Database Management')
)

with st.spinner(f"Loading {page} ..."):
  current_page = PAGES[page]
  current_page()


