import psycopg2 as db
from faker import Faker

fake = Faker()
db_str = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

conn = db.connect(db_str)
cur = conn.cursor()

data = []
i = 2

for x in range(1000):
    record = (i, fake.name(), fake.street_name(), fake.city(), fake.zipcode())
    data.append(record)
    i += 1

data_db = tuple(data)

query = "insert into users(id, name, street, city, zip) values(%s, %s, %s, %s, %s)"

cur.executemany(query, data)
conn.commit()
conn.close()
