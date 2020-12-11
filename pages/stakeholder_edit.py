import streamlit as st
from utils.stakeholder_card import stakeholder_card
import pandas as pd

avatars ={
    "avatar1" : "https://www.w3schools.com/w3css/img_avatar.png",
    "avatar2" : "https://www.w3schools.com/w3css/img_avatar2.png",
    "avatar3" : "https://www.w3schools.com/w3css/img_avatar3.png",
    "avatar4" : "https://www.w3schools.com/w3css/img_avatar4.png",
    "avatar5" : "https://www.w3schools.com/w3css/img_avatar5.png",
    "avatar6" : "https://www.w3schools.com/w3css/img_avatar6.png"
}

@st.cache
def load_test_data():
    main_data_df = pd.read_excel("static/data/Stakeholder_Dummy_Data.xlsx", sheet_name="Stakeholder Data", engine='openpyxl', index_col="Name")
    tags_df = pd.read_excel("static/data/Stakeholder_Dummy_Data.xlsx", sheet_name="All Available Tags",engine='openpyxl')
    return main_data_df, tags_df

def add():

    st.title("Add Stakeholder")
    
    c1, c2 = st.beta_columns((3,3))
    main_data_df , tags_df = load_test_data()
    tags = tags_df['Tags'].values

    with c1:
        
        avatar = st.selectbox("Avatar", list(avatars.keys()), index=0)
        name = st.text_input("Name", value="Mr Sam JP Blogs")
        company = st.text_input("Company", value="Fake Company")
        job_title = st.text_input("Job Title", value="Best Employee")
        street_name = st.text_input("Address", value="Street Name")
        post_code = st.text_input("Address", value="Post Code")
        last_date_contacted  = st.date_input("Last Date Contacted")

    with c2:
        
        email = st.text_input("Email", value="Email.com")
        phone_num = st.text_input("Phone Number", value="+44 123456789")
        current_employment_length = st.number_input("Employment Length", value=5)
        employment_start_date = st.date_input("Employment Start Date")
        URLs = st.text_input("Comma Separated Weblinks", value="blogs_web_profile.com")
        tags = st.multiselect("Comma Separated Tags", options=tags, default=None)


    # New Stakeholder Data    
    stakeholder = {
        "Avatar Number" : avatars[avatar],
        "Name" : name,
        "Email" : email,
        "Company" : company,
        "Job Title" : job_title,
        "Street Name" : street_name,
        "Post Code" : post_code,
        "Phone Number" : phone_num,
        "Current Employment Length" : current_employment_length,
        "Employment Start Date" : employment_start_date,
        "Date Last Contacted" : last_date_contacted,
        "URLs" : URLs,
        "Tags" : tags
    }
    
    add_stakerholder = st.button("Add Stakeholder Record")

    st.markdown(stakeholder_card(stakeholder), unsafe_allow_html=True)

    print(main_data_df)
    if add_stakerholder:
        if not main_data_df.append(stakeholder, ignore_index=True):
            st.write("Unable to Submit New Record")
        else:
            st.write("Record Saved")

def edit():
    st.title("Edit Stakeholder")
    pass

def add_tag():
    st.title("Tag Management")
    pass

def database_main():

    PAGES = {
        "Add Stakeholder" : add,
        "Edit Stakeholder" : edit,
        "Tag Management" : add_tag
    }

    page_selection = st.sidebar.radio(
        "Edit Mode", 
        [
            "Add Stakeholder",
            "Edit Stakeholder",
            "Tag Management"
        ]
        )
    
    page = PAGES[page_selection]
    page()
    
