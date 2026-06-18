"""
This is the experience page of the portfolio. Work experience to be specific
"""

#streamlit was having trouble finding the database module so this fixes it hopefully?
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st
import database

#database connection
db = database.get_db()

st.title("Experience")

experience = db.collection("experience").get() #grabbing and firing to the browser

for doc in experience: #looping through each experience and making a container for each
    exp = doc.to_dict()
    skills = [ref.get().to_dict() for ref in exp["skills_used"]] #getting the skill details for each skill used

    with st.container(border = True): #container for each experience
        col1, col2 = st.columns([3, 1]) #splits page into 1/3 and 2/3 layout
       
        with col1:
            st.markdown(f"""
             <p style="font-family: Space Mono, monospace; font-size: 9px; color: #C0392B; letter-spacing: 3px; margin: 0;">
                // {exp['company'].lower()}
            </p>
            <p style="font-family: DM Serif Display, serif; font-size: 22px; color: #0D0D0D; margin: 4px 0 2px;">
                {exp['role']}
            </p>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <p style="font-family: Space Mono, monospace; font-size: 9px; color: #888; text-align: right; margin-top: 8px;">
                {exp['start']} — {exp['end']}
            </p>
            """, unsafe_allow_html=True)

        for bullet in exp["bullets"]:
            st.markdown(f"""
            <p style="font-family: DM Serif Display, serif; font-size: 14px; color: #444; line-height: 1.8; margin: 4px 0;">
                — {bullet}
            </p>
            """, unsafe_allow_html=True)

        badges = " ".join([
            f'<span style="font-family: Space Mono, monospace; font-size: 9px; padding: 3px 10px; border: 0.5px solid #0D0D0D33; color: #0D0D0D; margin: 2px; display: inline-block; border-radius: 2px;">{s["name"]}</span>'
            for s in skills
        ])
        st.markdown(f'<div style="margin: 8px 0;">{badges}</div>', unsafe_allow_html=True)
