"""
This is the skills page for the portfolio and will display the skills and their associated colors.
"""
#streamlit was having trouble finding the database module so this fixes it hopefully?
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st
import database

#database connection
db = database.get_db()

st.title("Skills")
#pulling from the db into skills and firing off with .get()
skills = db.collection("skills").get()

categories = {} #empty dict for the cats
for doc in skills: #looping through each skill for the cat
    s = doc.to_dict() #converting into the readable for python
    categories.setdefault(s["category"], []).append(s) #appending the skill to its cat

for category, items in categories.items(): #looping through each cat and its items so it can display
    st.subheader(category)
    cols = st.columns(len(items))
    for col, skill in zip(cols, items): #loops through each column and skill and goes into each
        with col: 
            badge = f'<span style="background-color:{skill["color"]}; padding: 4px 10px; border-radius: 12px; color: white; margin: 2px">{skill["name"]}</span>'
            st.markdown(badge, unsafe_allow_html=True)
