import csv
import pymysql
import os
from dotenv import load_dotenv
import csv

def read_csv_file(file_path, csv_to_read):
    with open (file_path, 'r') as csv_file:
        read_csv = csv.DictReader(csv_file)
        csv_list = []
        for row in read_csv:
            csv_list.append(row) 
        return csv_list
    
def write_csv_file(file_path, csv_to_write):
    with open(file_path, "w", newline='') as file:
        if csv_to_write:
            writer = csv.DictWriter(file, fieldnames=csv_to_write[0].keys())
            writer.writeheader()
            writer.writerows(csv_to_write)
            
def append_dict(file_path, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_path, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = csv.DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)
        
def update_items(chosen_item):
    for key, value in chosen_item.items():
        chosen_value = input(
            f'\n{key} Has the value of {value}. Enter new value for {key}: ')
        if chosen_value == '':
            chosen_item[key] = value
            print('\nNothing has been changed')
        else:
            chosen_item[key] = chosen_value

def write_into_courier_db(Courier_name, Phone_number):
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
    sql = 'INSERT INTO courier (Courier_name, Phone_number) VALUES (%s, %s)'
    val = [(Courier_name, Phone_number)]
    cursor.executemany(sql, val)
    connection.commit()
    cursor.close()
    connection.close()
    
def read_courier_from_db():
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
    cursor.execute(
        'SELECT Courier_id, Courier_name, Phone_number FROM courier')
    rows = cursor.fetchall()
    for row in rows:
        print(
            f"\n Courier_id: {int(row[0])}, Courier_name: {str(row[1])}, Phone_number: {row[2]}")
    cursor.close()
    connection.close()

def read_product_from_db():
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
    cursor.execute(
        'SELECT product_id, product_name, product_price FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(
            f"\n product id: {int(row[0])}, product name: {str(row[1])}, product price: {float(row[2])}")
    cursor.close()
    connection.close()

def write_into_product_db(product_name, product_price):
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
    sql = 'INSERT INTO products (product_name, product_price) VALUES (%s, %s)'
    val = [(product_name, product_price)]
    cursor.executemany(sql, val)
    connection.commit()
    cursor.close()
    connection.close()