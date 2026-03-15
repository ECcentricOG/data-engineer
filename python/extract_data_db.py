import psycopg2 as db

db_str = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

conn = db.connect(db_str)

cur = conn.cursor()

cur.execute("select * from users")

#data = cur.fetchall()
#data = cur.fetchone()
data = cur.fetchmany(10)
print(data)

print(cur.rowcount)
