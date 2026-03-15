import psycopg2 as db

conn_str = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"

conn = db.connect(conn_str)

cur = conn.cursor()

data = (1, "Umesh", "MG Road", "Pune", "412210")
query = "insert into users(id, name, street, city, zip) values(%s, %s, %s, %s, %s)"

cur.execute(query, data)
conn.commit()


