import pandas.io.json as pd

file = open("data/data.json")
df = pd.read_json(file)

print(df.head(3).to_json(orient="records")) # Orient make sure it gets each record
