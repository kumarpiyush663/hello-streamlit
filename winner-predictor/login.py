# import stauth
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
#st.write(config)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('main')

# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{name}*')
#     st.title('Some content')
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    if st.button("Registered User"):
        st.switch_page('pages/test.py')
    # authenticator.logout('Logout', 'main')
    # st.switch_page('pages/3_DataFrame_Demo.py')
    # authenticator.logout('Logout', 'main')
    # st.write(f'Welcome *{st.session_state["name"]}*')
    # st.title('Some content')
    # st.switch_page("winner-predictor/Main.py")
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

    # Saving config file
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

if st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)