import pymysql
import os
from dotenv import load_dotenv
import pandas as pd
import csv
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)
# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

data = csv.reader(open('couriers.csv'))
sql = """INSERT INTO courier (Courier_name, Phone_number) VALUES (%s, %s)"""
next(data)
for line in data:
    line=[None if cell == '' else cell for cell in line]
    cursor.execute(sql, line)

# data = pd.read_csv (r'couriers.csv')   
# df = pd.DataFrame(data, columns= ['courier_name','courier_number'])

# cursor.execute('CREATE TABLE Couriers (Courier_name varchar(50), Phone_number int)')

# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO Couriers (Couriers_name, Phone_number)
#                 VALUES (%,%)
#                 ''',
#                 row.Couriers_name, 
#                 row.Phone_number,
#                 )
    
# sql = "INSERT INTO courier (Courier_name, Phone_number) VALUES (%s, %s)"
# val = ("Ahmed", 7593969647)
# cursor.execute(sql, val)
# sql = "INSERT INTO courier (Courier_name, Phone_number) VALUES (%s, %s)"
# val = [
#     ('Ahmed', 75936647),
#     ('Rumaanah', 70000002),
#     ('Oussama',700000003),
#     ('Idris',70000004),
# ]

# cursor.executemany(sql, val)
# cursor.execute('SELECT Courier_name,  Phone_number FROM courier')
# Gets all rows from the result
#rows = cursor.fetchall()
# for row in rows:
#     print(row)
#     print(f'Courier_name: {str(row[0])}, Phone_number: {row[1]},')
# # Add code here to insert a new record

connection.commit()
cursor.close()
connection.close()
print ("Imported")