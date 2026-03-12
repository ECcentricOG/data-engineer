import pandas as pd

data = {'name': ['Umesh', 'Leo', 'Cris', 'Ney'], 'age': [1,2,3,4]}

df = pd.DataFrame(data)

print(df)

df.to_csv("data/df.csv", index=False) #row number 0 that contains headers are also added in csv file
