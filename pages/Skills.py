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
#it looked quite chaotic earlier so this will make it look more professional and not like a child went to town on their labrador with those dot markers
category_order = [
    "AI & Machine Learning",
    "Languages",
    "Data & Big Data",
    "Geospatial",
    "Backend & APIs",
    "Databases",
    "Frontend & Visualization",
    "Infrastructure & Tools",
    "AI Tools",
    "Soft Skills"
]

for category in category_order: #looping through each category in the order
    if category not in categories:
        continue
    
    items = categories[category] #getting the skills for the category
    
    st.markdown(f"""
    <div style="margin: 2rem 0 0.5rem;">
        <span style="font-family: 'Space Mono', monospace; font-size: 10px; letter-spacing: 3px; color: #C0392B;">// {category.lower()}</span>
    </div>
    """, unsafe_allow_html=True)
    
    #renders the skills as badges 
    badges = " ".join([
        f'<span style="font-family: Space Mono, monospace; font-size: 10px; padding: 4px 12px; border: 0.5px solid #0D0D0D33; color: #0D0D0D; margin: 3px; display: inline-block; border-radius: 2px;">{s["name"]}</span>'
        for s in items
    ])
    st.markdown(f'<div style="line-height: 2.4;">{badges}</div>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-color: #0D0D0D11; margin: 0.5rem 0;">', unsafe_allow_html=True)
