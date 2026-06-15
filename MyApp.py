"""
This is the landing page / about for the portfolio shebang 
"""
import streamlit as st
#custom module to get the db connection
import database

#setting up the page configuration
st.set_page_config(page_title = "Portfolio", layout = "wide")
st.title("Portfolio")

try:
    db = database.get_db() #firestore connection from database module
    #st.success("Connected to Firestore")
    #database.seed_data(db)
    #about calls the about collection document("main") is pointing to the main in about
    #.get fires the request and to dict makes the collection into a plain ol dict
    about = db.collection("about").document("main").get().to_dict()


    #Lay of the land
    col1, col2 = st.columns([1, 2]) #splits page into 1/3 and 2/3 layout

    #with col1:
        #st.image(about["photo_url"], width = 250)

    with col2:
        st.title(about["name"])
        st.subheader(about["title"])
        st.write(about["bio"])
        st.markdown(f" {about['email']}")
        st.markdown(f"[LinkedIn]({about['linkedin']}) · [GitHub]({about['github']})")
except Exception as e:
    st.error(f"Error connecting to Firestore: {e}")

