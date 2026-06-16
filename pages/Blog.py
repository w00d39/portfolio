"""
This is the blog page where i can yap, may work better for me than linkedin
"""

#streamlit was having trouble finding the database module so this fixes it hopefully?
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st
import database

#database connection
db = database.get_db()

st.title("Blog")

posts = db.collection("blog").get() #grabbing and firing to browser

for doc in posts: #looping through each post and making a container for each
    post = doc.to_dict()

    with st.container(border = True): #container for each post
        st.subheader(post["title"]) #title of the post
        st.caption(post["date"]) #date of the post
        st.write(post["body"]) #my yapping

    tags = " ".join([f" `{tag}`" for tag in post["tags"]]) #join the tags with backticks so they look like code
    st.markdown(tags, unsafe_allow_html=True)