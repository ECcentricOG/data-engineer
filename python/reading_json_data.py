import json

with open("data/data.json") as f:
    data = json.load(f)

    print(data['records'][0])
