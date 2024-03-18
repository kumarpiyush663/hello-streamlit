import streamlit as st
import Main as ma

if 'username' not in st.session_state or st.session_state["username"] == "":
    st.divider()
    st.write(st.session_state)
    st.write(st.session_state["name"])
    st.divider()
    st.switch_page("pages/login.py")
else :
    st.set_page_config(
        page_title="Hello",
        page_icon="🏏",
    )
    # st.divider()
    # st.write(st.session_state)
    # st.write(st.session_state["name"])
    # st.divider()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.write("# Welcome to IPL Winner Predictor! 🏏")

    if st.button("Registered User"):
        st.dataframe(ma.get_registered_user())
# authenticator.logout('Logout', 'main')