import streamlit as st
import Main as ma

st.set_page_config(
    page_title="Hello",
    page_icon="🏏",
)
st.write(f'Welcome *{st.session_state["name"]}*')
st.write("# Welcome to IPL Winner Predictor! 🏏")

if st.button("Registered User"):
    st.dataframe(ma.get_registered_user())
# authenticator.logout('Logout', 'main')