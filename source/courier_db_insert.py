import pymysql
import os
from dotenv import load_dotenv
import csv
load_dotenv()

host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
    host,
    user,
    password,
    database
)
cursor = connection.cursor()

sql = "INSERT INTO courier (Courier_name, Phone_number) VALUES (%s, %s)"
val = [
    ('Ahmed', 75936647),
    ('Rumaanah', 70000002),
    ('Oussama',700000003),
    ('Idris',70000004),
]

cursor.executemany(sql, val)
cursor.execute('SELECT Courier_name,  Phone_number FROM courier')

rows = cursor.fetchall()
for row in rows:
    print(row)
    print(f'Courier_name: {str(row[0])}, Phone_number: {row[1]},')


connection.commit()
cursor.close()
connection.close()