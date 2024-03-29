import streamlit as st
import Main as ma
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def log_out():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    # st.write(config)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    authenticator.logout('Logout', 'sidebar')
    # authenticator._implement_logout()


# if 'username' not in st.session_state or st.session_state["username"] == "":
if not st.session_state["authentication_status"] or st.session_state['authentication_status'] is None:
    # st.divider()
    # st.write("Inside if")
    # st.write(st.session_state)
    # st.write(st.session_state["name"])
    # st.divider()
    st.switch_page("login.py")
else:
    st.set_page_config(
        page_title="Hello",
        page_icon="🏏",
    )
    # st.divider()
    # st.write("Inside else")
    # st.write(st.session_state)
    # st.write(st.session_state["name"])
    # st.divider()
    # if st.button("Logout"):
    log_out()
    # with open('config.yaml') as file:
    #     config = yaml.load(file, Loader=SafeLoader)
    # # st.write(config)
    #
    # authenticator = stauth.Authenticate(
    #     config['credentials'],
    #     config['cookie']['name'],
    #     config['cookie']['key'],
    #     config['cookie']['expiry_days'],
    #     config['preauthorized']
    # )
    # authenticator.logout('Logout', 'main')

    st.write(f'Welcome *{st.session_state["name"]}*')
    st.write("# Welcome to IPL Winner Predictor! 🏏")


    # if st.button("Registered User"):
    st.dataframe(ma.get_registered_user())
# authenticator.logout('Logout', 'main')
