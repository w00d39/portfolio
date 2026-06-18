"""
This is the landing page / about for the portfolio shebang 
"""
import streamlit as st
#custom module to get the db connection
import database

#setting up the page configuration
st.set_page_config(page_title = "Sarah Wood", page_icon="▶", layout = "wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=DM+Serif+Display:ital@0;1&display=swap');

    /* Base */
    .stApp { background-color: #F5F0E8; }
    * { font-family: 'Space Mono', monospace; }
    p, .stMarkdown p { font-family: 'DM Serif Display', serif; font-size: 16px; line-height: 1.8; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0D0D0D !important;
        border-right: 1px solid #C0392B;
    }
    [data-testid="stSidebar"] * { color: #F5F0E8 !important; font-family: 'Space Mono', monospace !important; font-size: 11px; letter-spacing: 2px; }
    [data-testid="stSidebarNav"] a:hover { color: #C0392B !important; }

    /* Headings */
    h1 { font-family: 'DM Serif Display', serif !important; font-size: 48px !important; font-weight: 400 !important; color: #0D0D0D; }
    h1 em { color: #C0392B; font-style: italic; }
    h2, h3 { font-family: 'Space Mono', monospace !important; font-size: 11px !important; letter-spacing: 3px; color: #C0392B; text-transform: none; }
    h2::before, h3::before { content: '// '; }

    /* Containers */
    [data-testid="stContainer"] {
        background: #0D0D0D !important;
        border-radius: 4px !important;
        padding: 1rem 1.2rem !important;
        border: none !important;
    }
    [data-testid="stContainer"] * { color: #F5F0E8 !important; }

    /* Buttons */
    .stButton > button {
        background: #C0392B !important;
        color: #fff !important;
        border: none !important;
        border-radius: 2px !important;
        font-family: 'Space Mono', monospace !important;
        letter-spacing: 2px;
        font-size: 10px !important;
        padding: 10px 24px !important;
    }
    .stButton > button:hover { background: #0D0D0D !important; }

    /* Inputs */
    .stTextInput input, .stTextArea textarea {
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid #0D0D0D !important;
        border-radius: 0 !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 12px !important;
        color: #0D0D0D !important;
    }

    /* Divider */
    hr { border-color: #C0392B44 !important; }
</style>
""", unsafe_allow_html=True)

st.title("Home")

try:
    db = database.get_db() #firestore connection from database module
   
   
    #about calls the about collection document("main") is pointing to the main in about
    #.get fires the request and to dict makes the collection into a plain ol dict
    about = db.collection("about").document("main").get().to_dict()


    #Lay of the land
    col1, col2 = st.columns([2, 1]) #splits page into 1/3 and 2/3 layout

    with col1:
        #st.image(about["photo_url"], width = 250)
        st.markdown("// data engineer · ml · ai", unsafe_allow_html=False)
        st.title("Sarah *Wood*")
        st.markdown("""
        <p style="font-family: 'DM Serif Display', serif; font-size: 22px; color: #0D0D0D; line-height: 1.6;">
        I build AI that makes sense to humans.<br>The hard problems are the most exciting ones.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="margin-top: 1.5rem; display: flex; gap: 16px;">
            <a href="{about['linkedin']}" target="_blank" style="font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 2px; color: #C0392B; text-decoration: none;">// LinkedIn</a>
            <a href="{about['github']}" target="_blank" style="font-family: 'Space Mono', monospace; font-size: 11px; letter-spacing: 2px; color: #C0392B; text-decoration: none;">// GitHub</a>
        </div>
        """, unsafe_allow_html=True)


    with col2:
        st.image(about["photo_url"], width=280)


    st.divider()

        # Ticker
    st.markdown("""
    <div style="font-family: 'Space Mono', monospace; font-size: 10px; color: #C0392B; letter-spacing: 3px; display: flex; gap: 24px; flex-wrap: wrap;">
        <span>▶ PYTHON</span><span>▶ MACHINE LEARNING</span><span>▶ HUMAN-IN-THE-LOOP</span><span>▶ EXPLAINABILITY</span><span>▶ STREAMLIT</span><span>▶ FIRESTORE</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Bio
    st.header("about")
    st.markdown(f"""
    <p style="font-family: 'DM Serif Display', serif; font-size: 18px; line-height: 1.9; max-width: 680px;">
    {about['bio']}
    </p>
    """, unsafe_allow_html=True)


except Exception as e:
    st.error(f"Error connecting to Firestore: {e}")

