import streamlit as st
from utils.stakeholder_card import stakeholder_card
import pandas as pd
import datetime
import numpy as np
import math

#TO-DO : extract repeated code into seperate functions

def load_test_data():
    # Just loading the data

    main_data_df = pd.read_csv("static/data/Stakeholder_Data.csv")
    tags_df = pd.read_csv("static/data/Stakeholder_Tags.csv")
    return main_data_df, tags_df

def edit_row(stakeholder, df, loc):
    df = df.drop(loc,axis=0)
    df = df.append(stakeholder, ignore_index=True)
    df.to_csv("static/data/Stakeholder_Data.csv", index=False)
    
def add(main_data_df, tags, stakerholder_lookup):
    """
    Adding a new stakeholder to the database
    """

    st.title("Add Stakeholder")
    
    # Creating two columns for user inputs
    c1, c2 = st.beta_columns((3,3))

    with c1:
        
        avatar = st.selectbox("Avatar", ["avatar"+str(av) for av in range(1,7)], index=0)
        name = st.text_input("Name", value="Frodeo Baggends")
        company = st.text_input("Company", value="Mordeor")
        job_title = st.text_input("Job Title", value="The Shire")
        address = st.text_input("address", value="17, The Shire Road")
        post_code = st.text_input("Post Code", value="SH17 1MOR")
        last_date_contacted  = st.date_input("Last Date Contacted")

    with c2:
        
        email = st.text_input("Email", value="hobbit@shire.com")
        phone_num = st.text_input("Phone Number", value="+44 123456789")
        current_employment_length = st.number_input("Employment Length", value=5)
        employment_start_date = st.date_input("Employment Start Date")
        URLs = st.text_input("Comma Separated Weblinks", value="bagends_primary.com")
        tags = st.multiselect("Comma Separated Tags", options=tags, default=None)


    # New Stakeholder Data    
    stakeholder = {
        "Avatar Number" : avatar,
        "Name" : name,
        "Email" : email,
        "Company" : company,
        "Job Title" : job_title,
        "Address" : address,
        "Post Code" : post_code,
        "Phone Number" : phone_num,
        "Current Employment Length" : current_employment_length,
        "Employment Start Date" : employment_start_date,
        "Date Last Contacted" : last_date_contacted,
        "URLs" : URLs,
        "Tags" : ",".join(tags)
    }
    
    add_stakerholder_button = st.button("Add Stakeholder Record")

    if add_stakerholder_button:
        # Check if Name Exists
        if (main_data_df['Name'] == name).any():
            st.markdown("""<div class="alert alert-warning" role="alert">
            Stakeholder Already Exists Please Edit Instead
            </div>""", unsafe_allow_html=True)
        # Adding to database
        else:
            main_data_df = main_data_df.append(stakeholder, ignore_index=True)
            main_data_df.to_csv("static/data/Stakeholder_Data.csv", index=False)
            # Save successful statement
            st.markdown("""<div class="alert alert-success" role="alert">
                Stakeholder Added
                </div>""", unsafe_allow_html=True)

    # Display stakeholder card
    st.markdown(stakeholder_card(stakeholder), unsafe_allow_html=True)

def edit(main_data_df, tags, stakerholder_lookup):
    """
    Editing a current stakeholder
    """

    st.title("Edit Stakeholder")

    # Stakeholder selection and data extraction
    edit_stakeholder = st.selectbox("Stakeholder", main_data_df['Name'].values, index=5)
    loc = int(stakerholder_lookup[edit_stakeholder])
    stakeholder = main_data_df.iloc[loc].to_dict()

    # Displays a stakeholder
    st.markdown(stakeholder_card(stakeholder), unsafe_allow_html=True)
    
    st.title("Editor")

    # Creating two columns for user inputs
    c1, c2 = st.beta_columns((3,3))

    with c1:
        
        avatar = st.selectbox("Avatar", ["avatar"+str(av) for av in range(1,7)], index=int(stakeholder['Avatar Number'][-1])-1)
        name = st.text_input("Name", value=stakeholder['Name'])
        company = st.text_input("Company", value=stakeholder['Company'])
        job_title = st.text_input("Job Title", value=stakeholder['Job Title'])
        address = st.text_input("address", value=stakeholder['Address'])
        post_code = st.text_input("Post Code", value=stakeholder["Post Code"])
        stakehodler_last_date = datetime.datetime.strptime(stakeholder['Date Last Contacted'], '%Y-%m-%d')
        last_date_contacted  = st.date_input("Last Date Contacted", value=stakehodler_last_date)

    with c2:
        
        email = st.text_input("Email", value=stakeholder['Email'])
        phone_num = st.text_input("Phone Number", value=stakeholder['Phone Number'])
        current_employment_length = st.number_input("Employment Length", value=int(stakeholder['Current Employment Length']))
        #Generating Datatime object
        stakehodler_start_date = datetime.datetime.strptime(stakeholder['Employment Start Date'], '%Y-%m-%d')
        employment_start_date = st.date_input("Employment Start Date", stakehodler_start_date)

        URLs = st.text_input("Comma Separated Weblinks", value=stakeholder['URLs'])
        if type(stakeholder['Tags']) !=  str:
            default_tags = None
        else:
            default_tags = list(stakeholder['Tags'].split(","))
        tags = st.multiselect("Comma Separated Tags", options=list(tags), default=default_tags)

    stakeholder = {
        "Name" : name,
        "Email" : email,
        "Company" : company,
        "Job Title" : job_title,
        "Phone Number" : phone_num,
        "Address" : address,
        "Post Code" : post_code,
        "Employment Start Date" : employment_start_date,
        "Current Employment Length" : current_employment_length,
        "Avatar Number" : avatar,
        "Date Last Contacted" : last_date_contacted,
        "URLs" : URLs,
        "Tags" : ",".join(tags)
        }

    update_button = st.button("Update Stakeholder")

    if update_button:
        
        edit_row(stakeholder, main_data_df, loc)

        # Save successful statement
        st.markdown("""<div class="alert alert-success" role="alert">
            Stakeholder Updated
            </div>""", unsafe_allow_html=True)



def edit_tags(main_data_df, tags, stakerholder_lookup):
    """
    Managing the current tags
    """

    st.title("Tag Management")

    # Generating a list of tags, required for the multi-select function
    list_tags = list(tags)

    new_tag = st.text_input("Please Enter New Tag e.g. WearableInjectables or SpaceStation")

    update_tag_button = st.button("Add Tag")

    if update_tag_button:
        # Checking if the tags is already present
        if new_tag not in list_tags:
            tags_df = pd.DataFrame({"Tags" : list_tags + [new_tag]})
            tags_df.to_csv("static/data/Stakeholder_Tags.csv", index=False)
            st.markdown("""<div class="alert alert-success" role="alert">
                Tag Successfully Added
                </div>""", unsafe_allow_html=True)
    
        else:
            st.markdown("""<div class="alert alert-success" role="alert">
                Tag already exists, not added to database
                </div>""", unsafe_allow_html=True)

    # removing tags
    remove_tags = st.multiselect("Tags to Remove", options=list_tags)

    remove_tags_button = st.button("Remove Tag(s)")

    if remove_tags_button:
        for tag in remove_tags:
            list_tags.remove(tag)
        # Checking if the tags is already present
        tags_df = pd.DataFrame({"Tags" : list_tags})
        tags_df.to_csv("static/data/Stakeholder_Tags.csv", index=False)
        st.markdown("""<div class="alert alert-success" role="alert">
            Tag(s) Successfully Removed
            </div>""", unsafe_allow_html=True)

def database_admin():
    """
    Main function for the database maintance page
    """

    # Loading the data
    main_data_df , tags_df = load_test_data()
    tags = tags_df['Tags'].values

    # Generating a stakerholder lookup dict... Name : Index
    stakerholder_lookup = dict((v,k) for k,v in main_data_df[["Name"]].to_dict()['Name'].items())

    # Available pages in Stakeholders Database Management mode
    PAGES = {
        "Add Stakeholder" : add,
        "Edit Stakeholder" : edit,
        "Tag Management" : edit_tags
    }

    # Update sidebar for the database maintance page
    page_selection = st.sidebar.radio(
        "Edit Mode", 
        [
            "Add Stakeholder",
            "Edit Stakeholder",
            "Tag Management"
        ]
        )
    

    # Load the page based on the selected option
    page = PAGES[page_selection]
    page(main_data_df, tags, stakerholder_lookup)
    
