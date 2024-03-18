import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="🏏",
)
st.write(f'Welcome *{st.session_state["name"]}*')
st.write("# Welcome to IPL Winner Predictor! 🏏")
authenticator.logout('Logout', 'main')