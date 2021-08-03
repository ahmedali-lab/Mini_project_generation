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

sql = "INSERT INTO orders_in_progress (customer_name,customer_address,customer_number,product_choice,courier_choice,order_status) VALUES (%s, %s,%s,%s,%s,%s)"
val = [
    ('Ahmed', '52 Beaudesert Road, Birmingham, B20 3LX', 75473638, 2, 2, 'PREPARING'),
    ('Ahmed', '227 Mary Street, Birmingham, B12 9RW', 75433532, 2, 2, 'DELIVERED')
]

cursor.executemany(sql, val)
cursor.execute('SELECT customer_name,customer_address,customer_number,product_choice,courier_choice,order_status FROM orders_in_progress')

rows = cursor.fetchall()
for row in rows:
    print(row)
    print(f'customer_name: {str(row[0])}, customer_address: {str(row[1])}, customer_number: {row[2]},product_choice: {row[3]},courier_choice: {row[4]}, order_status: {str(row[5])},')


connection.commit()
cursor.close()
connection.close()