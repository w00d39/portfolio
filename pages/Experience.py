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
        st.subheader(exp["role"]) #role of the experience
        st.caption(f"{exp['company']} · {exp['start']} - {exp['end']}") #dates i was there

        for bullet in exp["bullets"]: #ye old bullet points
            st.write(f"• {bullet}")

        #skill badges :)
        badges = " ".join([ #joining the skill badges into a single string
            f'<span style="background-color:{s["color"]}; padding: 4px 10px; border-radius: 12px; color: white; margin: 2px">{s["name"]}</span>'
            for s in skills #for each skill it loops through and creates a badge
        ])
        st.markdown(badges, unsafe_allow_html=True)