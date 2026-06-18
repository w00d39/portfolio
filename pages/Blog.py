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

st.markdown("""
<p style="font-family: Space Mono, monospace; font-size: 10px; color: #888; letter-spacing: 2px;">
    // thoughts on AI, data, and building things
</p>
""", unsafe_allow_html=True)

posts = db.collection("blog").order_by("date", direction="DESCENDING").get() #grabbing and firing to browser

if not posts:
    st.markdown("""
    <div style="margin-top: 3rem; text-align: center;">
        <p style="font-family: DM Serif Display, serif; font-size: 22px; color: #0D0D0D;">
            Posts coming soon.
        </p>
        <p style="font-family: Space Mono, monospace; font-size: 10px; color: #888; letter-spacing: 2px;">
            // check back later
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    for doc in posts:
        p = doc.to_dict()

        with st.container(border=True):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"""
                <p style="font-family: DM Serif Display, serif; font-size: 22px; color: #0D0D0D; margin: 0;">
                    {p['title']}
                </p>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <p style="font-family: Space Mono, monospace; font-size: 9px; color: #888; text-align: right; margin-top: 8px;">
                    {p['date']}
                </p>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <p style="font-family: DM Serif Display, serif; font-size: 15px; color: #444; line-height: 1.8;">
                {p['body']}
            </p>
            """, unsafe_allow_html=True)

            tags = " ".join([
                f'<span style="font-family: Space Mono, monospace; font-size: 9px; padding: 3px 10px; border: 0.5px solid #C0392B44; color: #C0392B; margin: 2px; display: inline-block; border-radius: 2px;">{tag}</span>'
                for tag in p.get("tags", [])
            ])
            st.markdown(f'<div style="margin: 8px 0;">{tags}</div>', unsafe_allow_html=True)