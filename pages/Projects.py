"""
This is the projects page for the portfolio and will cross reference the skills
"""
#streamlit was having trouble finding the database module so this fixes it hopefully?
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st
import database

#database connection
db = database.get_db()

st.title("Projects")
#pulling from the db into projects and firing off with .get()
projects = db.collection("projects").get()

#looping through the projects and displaying them
for project in projects:
    p = project.to_dict() 

    skills = [skill_ref.get().to_dict() for skill_ref in p["tech_stack"]]

    with st.container(border = True):
        st.subheader(p["title"])
        st.write(p["description"])

        #lil badges for skills
        cols = st.columns(len(skills)) #create columns for each skill need the len for num of them

        for col, skill in zip(cols, skills): #zips the len of cols with the skills so its accessing both but same loop
            with col: #accessing each column
                badge = f'<span style="background-color:{skill["color"]}; padding: 4px 10px; border-radius: 12px; color: white; margin: 2px">{skill["name"]}</span>'
                st.markdown(badge, unsafe_allow_html=True)

        st.markdown(f"[View Project]({p['link']})")