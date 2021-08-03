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

sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
val = [
    ('Cheese burger meal', 5.50),
    ('Chicken 1pc meal', 3.50),
    ('Lentil soup', 1.50),
    ('Rice and goat meat', 7.50),
    ('Water', 0.50),
    ('Can of soft drink', 0.80)
]

cursor.executemany(sql, val)
cursor.execute('SELECT product_name, product_price FROM products')

rows = cursor.fetchall()
for row in rows:
    print(row)
    print(f'product_name: {str(row[0])}, product_price: {row[1]},')


connection.commit()
cursor.close()
connection.close()