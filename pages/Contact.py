
import sys
import os
import datetime
import html 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import streamlit as st
import database



db = database.get_db()

if "last_submission" not in st.session_state:
    st.session_state.last_submission = None



st.title("Contact")

name = html.escape(st.text_input("Name"))
email = html.escape(st.text_input("Email"))
message = html.escape(st.text_area("Message"))

if len(message) > 1000:
    st.error("Message must be less than 1000 characters.")

honeypot = st.text_input("Leave this blank", label_visibility = "hidden")

if st.button("Send"):
    if honeypot:
        st.stop() 

    now = datetime.datetime.now()
    if st.session_state.last_submission and (now - st.session_state.last_submission).total_seconds() < 60:
        st.error("Please wait at least 60 seconds before submitting another message.")

    elif name and database.valid_email(email) and message:
        db.collection("contact").add({
            "name": name,
            "email": email,
            "message": message,
            "timestamp":datetime.datetime.now()
        })
        st.success("Message sent successfully!")

    else:
        st.error("Please fill in all fields with valid information.")