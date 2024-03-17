# import csv
# with open('Config/Registeration.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#     for lines in csvFile:
# 		    print(lines)

import pandas as pd
df = pd.read_csv('Config/Registeration.csv')



print(df)

df.set_index("UserId", drop=True, inplace=True)
dictionary = df.to_dict(orient="index")

print(dictionary)

print(dictionary['Dunggeon'])


