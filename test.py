import psycopg2

conn = psycopg2.connect(
    host = "127.0.0.1",
    password = 'daysunmon',
    user = 'postgres',
    database = 'postgres')

cur = conn.cursor()
cur.execute("select * from test.location limit 10")
lis = cur.fetchall()
print(lis)

conn.close()