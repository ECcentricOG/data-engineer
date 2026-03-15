import psycopg2 as db

file = open("data/data_db.csv", mode="w")

db_str = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

conn = db.connect(db_str)
cur = conn.cursor()

cur.copy_to(file, "users", sep=",")

with open("data/data_db.csv") as f:
    print(f.read())
