import csv

with open("data/data.csv") as f:
    reader = csv.DictReader(f)
    header = next(reader)

    for row in reader:
        print(row['name'])
