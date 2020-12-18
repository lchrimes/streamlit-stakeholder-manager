import streamlit as st
import pandas as pd
from utils.stakeholder_card import stakeholder_card
import datetime

def data_refresh():
    df = pd.read_csv("static/data/Stakeholder_rawData.csv")
    df.to_csv("static/data/Stakeholder_Data.csv")
    st.markdown("""<div class="alert alert-success" role="alert">
    Data Successfully Refreshed
    </div>""", unsafe_allow_html=True)

def load__stakeholder_data(filename):

    df = pd.read_csv(filename)

    # Generating a stakerholder lookup dict... Name : Index
    stakerholder_lookup = dict((v,k) for k,v in df[["Name"]].to_dict()['Name'].items())

    return df, stakerholder_lookup

def load__tags(filename):

    df = pd.read_csv(filename)

    return df

def stakeholder_searching(tags,df):
    names = []
    for stakeholder in df.iterrows():
            taged = stakeholder[1]['Tags']
            if type(taged) == str:
                list_tags = taged.split(',')
                for tag in list_tags:
                    if tag in tags:
                        names.append(stakeholder[1]['Name'])
    return st.selectbox("Search Results", list(set(names)))

def edit_last_contact(stakeholder, df, loc):
    df = df.drop(loc,axis=0)
    df = df.append(stakeholder, ignore_index=True)
    df.to_csv("static/data/Stakeholder_Data.csv", index=False)
    st.markdown("""<div class="alert alert-success" role="alert">
    Last Contacted Successfully Updated
    </div>""", unsafe_allow_html=True)

def display_card(name, df, lookup):

    stakeholder_df = df[df['Name'] == name]
    if not stakeholder_df.empty:
        loc = int(lookup[stakeholder_df['Name'].values[0]])
        stakeholder = df.iloc[loc].to_dict()
        st.markdown(stakeholder_card(stakeholder), unsafe_allow_html=True)

    update_last_contact = st.button("Contacted")
    if update_last_contact:
        stakeholder['Date Last Contacted'] = datetime.datetime.now().strftime('%Y-%m-%d')
        edit_last_contact(stakeholder, df, loc)


def search():

    st.write(
    """
    <div class="main">
    <b>Please be aware</b>
    This app is a demo intended to help you keep track of various contacts for use in projects, by tagging contacts by their expertise or how approachable they are. It includes an example set of data that can be edited and saved, and lets you easily track when each person was last contacted.
    As this is a public demo, the example data can be edited by anyone. It is highly recommended that the app is "reset" using the below button prior to using it, to remove other user's changes to the saved data.
    </div>
    """, unsafe_allow_html=True)
    
    refresh_app_data = st.button("Data Refresh")
    if refresh_app_data:
        data_refresh()

    st.title("Stakeholder Search")

    stakeholder_database, stakerholder_lookup = load__stakeholder_data("static/data/Stakeholder_Data.csv")
 
    tag_database = load__tags("static/data/Stakeholder_Tags.csv")

    tags = st.multiselect('Filter by Tag', options=list(tag_database['Tags'].values))
    selected_stakeholder = stakeholder_searching(tags,stakeholder_database)
    display_card(selected_stakeholder, stakeholder_database, stakerholder_lookup)

