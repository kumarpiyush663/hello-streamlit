# import pandas as pd
# import streamlit as st
#
# def initialise():
#     st.set_page_config(
#         page_title="Hello",
#         page_icon="🏏",
#     )
#     st.write("# Welcome to IPL Winner Predictor! 🏏")
#
#
# def get_registered_user():
#     df = pd.read_csv('winner-predictor/Config/Registeration.csv')
#     # st.dataframe(df)
#     return df
#
#
# def get_normalized_registered_user(df):
#     df["UserIdExt"] = df["UserId"]
#     df.set_index("UserIdExt", drop=True, inplace=True)
#     dictionary = df.to_dict(orient="index")
#     return dictionary
#
#
# def update_registered_user(registereduserdf, userId):
#     registeredUser = get_normalized_registered_user(registereduserdf)
#     st.write(registeredUser)
#     st.divider()
#     User = registeredUser[userId]
#     User.update({"Email Id": "noemail@notavailable.com"})
#     registeredUser[userId] = User
#     st.write(registeredUser)
#     columns = registereduserdf.columns.values.tolist()
#     st.write(columns)
#
#
# def generate_secret_key():
#     registereduserdf = get_registered_user()
#     registereduser = get_normalized_registered_user(registereduserdf)
#     secret_key = {}
#     for key in registereduser:
#         x = registereduser[key]["UserId"][0] + registereduser[key]["UserId"][-1]
#         y = registereduser[key]["First Name"][0] + registereduser[key]["First Name"][-1]
#         z = registereduser[key]["Last Name"][0] + registereduser[key]["Last Name"][-1]
#         sk = z + x + y
#         secret_key[key] = sk.lower()
#
#     # st.write(secret_key)
#     return secret_key
#
#
# def run():
#     registereduserdf = get_registered_user()
#     st.dataframe(registereduserdf)
#     registereduser = get_normalized_registered_user(registereduserdf)
#     update_registered_user(registereduserdf, "Dunggeon")
#     generate_secret_key()
#
#
# if __name__ == "__main__":
#     initialise()
#     run()
