import psycopg2 as db
import pandas as pd

db_str = "dbname='dataengineering' host='localhost' user='postgres' password='postgrea'"

conn = db.connect(db_str)

df = pd.read_sql("select * from users", conn)

print(df)
