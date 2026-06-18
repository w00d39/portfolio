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
for doc in projects:
    p = doc.to_dict()
    skills = [ref.get().to_dict() for ref in p.get("tech_stack", [])] #get the skill details for each tech stack item

    with st.container(border=True): #create a container for each project
        col1, col2 = st.columns([3, 1]) #split the container into 3/1 ratio
        
        with col1: #display the project details
            st.markdown(f"""
            <p style="font-family: Space Mono, monospace; font-size: 9px; color: #C0392B; letter-spacing: 3px; margin: 0;">
                // {p.get('role', '').lower()}
            </p>
            <p style="font-family: DM Serif Display, serif; font-size: 22px; color: #0D0D0D; margin: 4px 0 2px;">
                {p['title']}
            </p>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <p style="font-family: Space Mono, monospace; font-size: 9px; color: #888; text-align: right; margin-top: 8px;">
                {p.get('date', '')}
            </p>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <p style="font-family: DM Serif Display, serif; font-size: 15px; color: #444; line-height: 1.8;">
            {p['description']}
        </p>
        """, unsafe_allow_html=True)

        #badges :) for each skill
        badges = " ".join([
            f'<span style="font-family: Space Mono, monospace; font-size: 9px; padding: 3px 10px; border: 0.5px solid #0D0D0D33; color: #0D0D0D; margin: 2px; display: inline-block; border-radius: 2px;">{s["name"]}</span>'
            for s in skills
        ])
        st.markdown(f'<div style="margin: 8px 0;">{badges}</div>', unsafe_allow_html=True)

        #links if applicable
        if p.get("link"):
            st.markdown(f"""
            <a href="{p['link']}" target="_blank" style="font-family: Space Mono, monospace; font-size: 10px; color: #C0392B; text-decoration: none; letter-spacing: 2px;">
                // view on github ↗
            </a>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <span style="font-family: Space Mono, monospace; font-size: 10px; color: #888; letter-spacing: 2px;">
                // private repository
            </span>
            """, unsafe_allow_html=True)