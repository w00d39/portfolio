
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

st.markdown("""
<p style="font-family: Space Mono, monospace; font-size: 10px; color: #888; letter-spacing: 2px;">
    // drop me a line
</p>
<p style="font-family: DM Serif Display, serif; font-size: 18px; color: #444; line-height: 1.8; max-width: 540px;">
    I'm currently looking for opportunities in machine learning and data engineering. 
    Whether you have a role, a project, or just want to talk tech — I'd love to hear from you.
</p>
""", unsafe_allow_html=True)

st.divider()

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