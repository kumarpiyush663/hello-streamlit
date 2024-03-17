# import csv
# with open('Config/Registeration.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#     for lines in csvFile:
# 		    print(lines)

import pandas as pd
import streamlit as st
#df = pd.read_csv('/Users/piyushkumar/PycharmProjects/hello-streamlit/winner-predictor/Config/Registeration.csv')

df = pd.read_csv('winner-predictor/Config/Registeration.csv')


st.dataframe(df)

df.set_index("UserId", drop=True, inplace=True)
dictionary = df.to_dict(orient="index")

# print(dictionary)



