import csv
import pymysql
import os
from dotenv import load_dotenv


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

def read_courier_from_database():
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

def write_into_courier_database(Courier_name, Phone_number):
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
    
    
def read_product_from_database():
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

def write_into_product_database(product_name, product_price):
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
    
def delete_products_from_database(del_product_id):
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
    sql = 'DELETE FROM products WHERE product_id = %s'
    val = [(del_product_id)]
    
    cursor.execute(sql,val)
    
    connection.commit()
    cursor.close()
    connection.close()

def delete_courier_from_database(del_courier_id):
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
    sql = 'DELETE FROM courier WHERE courier_id = %s'
    val = [(del_courier_id)]
    
    cursor.execute(sql,val)
    
    connection.commit()
    cursor.close()
    connection.close()


def change_product_value_in_db(new_product_input, new_price_input, product_id):
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
    if new_product_input or new_price_input:
        sql = 'UPDATE products SET'
        if new_product_input and new_price_input:
            sql += ' product_name = %s, product_price = %s WHERE product_id = %s'
            val = (new_product_input, new_price_input, product_id)
            
        elif new_product_input:
            sql += ' product_name = %s WHERE product_id = %s'
            val = (new_product_input, product_id)
            print(f'{Print_colours.green}\nProduct price will remain the same{Print_colours.reset}')
            
        elif new_price_input:
            sql += ' product_price = %s WHERE product_id = %s'
            val = (new_price_input, product_id)
            print(f'{Print_colours.green}\nProduct name will remain the same{Print_colours.reset}')
            
        cursor.execute(sql, val)
        connection.commit()
    else:
        print(f"\n{Print_colours.green}Nothing has been updated. Entry will stay the same{Print_colours.reset}")
    cursor.close()
    connection.close()
    
    
def change_courier_value_in_db(new_courier_input, new_courier_num_input, courier_id):
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
    if new_courier_input or new_courier_num_input:
        
        sql = 'UPDATE courier SET'
        if new_courier_input and new_courier_num_input:
            sql += ' courier_name = %s, Phone_number = %s WHERE Courier_id = %s'
            val = (new_courier_input, new_courier_num_input, courier_id)
            
        elif new_courier_input:
            sql += ' courier_name = %s WHERE Courier_id = %s'
            val = (new_courier_input, courier_id)
            print(f'{Print_colours.green}\ncourier number has not been changed{Print_colours.reset}')
            
        elif new_courier_num_input:
            sql += ' Phone_number = %s WHERE Courier_id = %s'
            val = (new_courier_num_input, courier_id)
            print(f'{Print_colours.green}\ncourier name has not been changed{Print_colours.reset}')
        cursor.execute(sql, val)
        connection.commit()
    else:
        print(f"{Print_colours.green}\nNothing has been updated. Entry will stay the same{Print_colours.reset}")
    cursor.close()
    connection.close()
    
    
def read_orders_from_database():
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
        'SELECT order_id,customer_name,customer_address,customer_number,product_choice,courier_choice,order_status FROM orders_in_progress')
    rows = cursor.fetchall()
    for row in rows:
        print(f'''\norder_id: {row[0]},customer_name: {str(row[1])}, customer_address: {str(row[2])}, 
            customer_number: {row[3]},product_choice: {row[4]},courier_choice: {row[5]}, order_status: {str(row[6])}''')
        
    cursor.close()
    connection.close()

def write_into_order_database(customer_name, customer_address, customer_number,customer_product_choice,customer_courier_choice,new_order_status):
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
    sql = 'INSERT INTO orders_in_progress (customer_name,customer_address,customer_number,product_choice,courier_choice,order_status) VALUES (%s, %s,%s,%s,%s,%s)'
    val = [(customer_name, customer_address, customer_number,customer_product_choice,customer_courier_choice, new_order_status)]
    cursor.executemany(sql, val)
    connection.commit()
    cursor.close()
    connection.close()
    
def delete_order_from_database(del_order_id):
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
    sql = 'DELETE FROM orders_in_progress WHERE order_id = %s'
    val = [(del_order_id)]
    
    cursor.execute(sql,val)
    
    connection.commit()
    cursor.close()
    connection.close()

class Print_colours:
    green = '\033[92m' #GREEN
    yellow = '\033[93m' #YELLOW
    red = '\033[91m' #RED
    reset = '\033[0m' #RESET COLOR
    

def re_main_menu():
    print(f'{Print_colours.green}\nYou will now return to main menu{Print_colours.reset}')

def invalid_input():
    print(f'{Print_colours.red} Invalid input {Print_colours.reset}')

def success():
    print(f'\n{Print_colours.green}Success!{Print_colours.reset}')
    
