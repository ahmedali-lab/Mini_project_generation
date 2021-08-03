
from funcs import read_csv_file, write_csv_file, append_dict, update_items, write_into_courier_database, read_courier_from_database
from funcs import read_product_from_database, write_into_product_database, delete_products_from_database 
from funcs import delete_courier_from_database, change_product_value_in_db,change_courier_value_in_db,read_orders_from_database
from funcs import write_into_order_database,delete_order_from_database,Print_colours,invalid_input,success,re_main_menu  
import csv
import pymysql
import os
from dotenv import load_dotenv


products_list = [] 

products_list = read_csv_file('products.csv', products_list)

couriers_list = []

couriers_list = read_csv_file('couriers.csv',couriers_list)

orders_in_progress = []

orders_in_progress = read_csv_file('orders.csv',orders_in_progress)

order_status = ['PREPARING', 'EN ROUTE', 'DELIVERED']

#### MAIN MENU FUNCTION ####
print(f'\n\t---------------------------{Print_colours.yellow}WELCOME{Print_colours.reset} {Print_colours.green}TO{Print_colours.reset} {Print_colours.red}CHILLY\'S{Print_colours.reset}---------------------------------')

def main_menu():

    main_menu_options = int(input(f'''\n\bPlease select 0 to exit app and save data, 1 for product options, 2 for courier options or 3 for order options: '''))
    
    while main_menu_options < 0 or main_menu_options > 3:
        invalid_input()
        main_menu_options = int(input(f'''\nPlease select 0 to exit app, 1 for product options, 2 for courier options or 3 for order options: '''))
    
    if main_menu_options == 0:
        
        write_csv_file('products.csv', products_list)
        write_csv_file('couriers.csv', couriers_list)
        write_csv_file('orders.csv', orders_in_progress)

        print(f'{Print_colours.green} \nYou have successfully saved your changes and will now exit app {Print_colours.reset}')
        print('\n')
    elif main_menu_options == 1: 

        read_product_from_database()
        print(f'{Print_colours.green}\nHere are the current avaliable products. You are now entering the product menu.{Print_colours.reset}')
        product_menu()
        
    elif main_menu_options == 2:

        read_courier_from_database()
        print(f'{Print_colours.green}\n Here are the current avaliable couriers. You are now entering the courier menu.{Print_colours.reset}')
        courier_menu()
        
    else:
        main_menu_options == 3
        read_orders_from_database()
        print(f'{Print_colours.green}\nHere are the current orders. You are now entering the order menu.{Print_colours.reset}')
        order_menu()
        
#### PRODUCT MENU FUNCTION ####

def product_menu():

    product_menu_option = int(input(f'''\nPlease select: 0 to return to the main menu, 1 to view product list, 
2 to add a new product, 
3 to update an existing product or 
4 to delete a product: 
'''))
    
    while product_menu_option < 0 or product_menu_option > 4:
        print('\n')
        invalid_input()
        product_menu_option = int(input(f'''\nPlease select: 0 to return to the main menu, 1 to view product list, 
2 to add a new product, 
3 to update an existing product or 
4 to delete a product: 
'''))
        
    if  product_menu_option == 0:
        
        main_menu()
        
    elif product_menu_option== 1:
        
        read_product_from_database()
        print(f'\n{Print_colours.green}Here are the current avaliable products. You will now return to the main menu.\n{Print_colours.reset}')
        main_menu()
        
    elif product_menu_option == 2:
        
        print(f'{Print_colours.yellow}\nCurrent product list: {Print_colours.reset}')
        read_product_from_database()
        new_product = input('\nPlease enter product name you would like to add: ')
        while new_product == '':
            invalid_input()
            new_product = input('\nPlease enter product name you would like to add: ')

        new_product_price = float(input(('\nPlease enter new product price: ')))

        write_into_product_database(new_product, new_product_price)
        
        print(f'{Print_colours.yellow}\nnew list: {Print_colours.reset}')
        read_product_from_database()
        
        re_main_menu()
        
        main_menu()

    elif product_menu_option == 3:
        
        read_product_from_database()
        
        product_id = input('\nPlease choose which product you would like to update via ID: ')

        product_name = input('\nPlease choose a new product name: ')
            
        product_price = input('\nPlease choose a new product price value: ')

        change_product_value_in_db(product_name, product_price, product_id)
        
        print(f'\n{Print_colours.yellow}Updated products:{Print_colours.reset} ')
        read_product_from_database()
        
        re_main_menu()
        main_menu()
        
    elif product_menu_option == 4:
        
        print('\nCurrent product list: ')
        read_product_from_database()
        

        product_to_delete = input('\nPlease select which product you would like to delete via ID: ')

        delete_products_from_database(product_to_delete)
            
        print(f'{Print_colours.yellow}\nNew product list: {Print_colours.reset}' )
        read_product_from_database()
        re_main_menu()
        main_menu()

#### COURIER FUNCTION ####

def courier_menu():
    couriers_menu_option = int(input(
'''
\nPlease select: 
0 to return to the main menu, 
1 to view couriers_ list, 
2 to add new courier, 
3 to update  an existing courier or 
4 to delete a courier: 

'''))
    while couriers_menu_option < 0 or couriers_menu_option > 4:
        invalid_input()
        couriers_menu_option = int(input(
'''
\nPlease select: 
0 to return to the main menu, 
1 to view couriers_ list, 
2 to add new courier, 
3 to update an existing courier or 
4 to delete a courier:   
'''))
    
    if couriers_menu_option == 0:
        main_menu()
        
    elif couriers_menu_option == 1:
        
        print(f'\n{Print_colours.green}Here are the current avaliable couriers. You will now return to the main menu. {Print_colours.reset}')
        read_courier_from_database()
        main_menu()
        
    elif couriers_menu_option == 2:
        
        print(f'{Print_colours.yellow}\nCurrent couriers list: {Print_colours.reset}')
        read_courier_from_database()
        
        new_courier = input('\nPlease enter new courier name: ')
        while new_courier == '':
            invalid_input()
            new_courier = input('\nPlease enter new courier name: ')
            
        new_courier_phone_number = int(input('\nPlease enter new courier phone number: '))
            
        write_into_courier_database(new_courier, new_courier_phone_number)
        
        print(f'\n{Print_colours.yellow}\nnew list: {Print_colours.reset}')
        read_courier_from_database()
        
        re_main_menu()
        
        main_menu()
        
    elif couriers_menu_option == 3:
        
        
        read_courier_from_database()
        
        courier_id = input('\nPlease choose which courier you would like to update via ID: ')
        new_courier_input = input('\nPlease choose a new courier name: ')
        new_courier_num_input = input('\nPlease choose a new courier number value: ')
        
        
        change_courier_value_in_db(new_courier_input, new_courier_num_input, courier_id)
        
        print(f'\n{Print_colours.yellow}Updated couriers: {Print_colours.reset}')
        read_courier_from_database()
        re_main_menu()
        
        main_menu()
                
    elif couriers_menu_option == 4:
        
        print('\nCurrent courier list: ')
        read_courier_from_database()
        
        courier_to_delete = input('\nPlease select which courier you would like to delete via ID: ')
        delete_courier_from_database(courier_to_delete)
        print(f'{Print_colours.yellow}\nNew courier list: ' )
        read_courier_from_database()
        
        re_main_menu()
        
        main_menu()

def order_menu():
    order_menu_option = int(input(
'''
\n Please select: 
0 to return to the main menu, 
1 to view orders status, 
2 to make an order, 
3 update existing order status  
4 to update an existing order or
5 to delete an order: 

'''))
    while order_menu_option  < 0 or order_menu_option  > 5:
        invalid_input()
        order_menu_option = int(input(
'''
\n Please select: 
0 to return to the main menu, 
1 to view orders status, 
2 to make an order, 
3 update existing order status  
4 to update an existing order or
5 to delete an order:   
'''))
        
    if order_menu_option == 0:
            re_main_menu()
            main_menu()
        
    elif order_menu_option == 1:
        
        print(f'{Print_colours.yellow}\nCurrent orders in progress: {Print_colours.reset}')
        read_orders_from_database()
        
        print('\nReturning to main menu: ')
        main_menu()
            
    elif order_menu_option == 2:
        
        customer_name = input('\nPlease enter your name: ')
        while customer_name == '':
            invalid_input()
            customer_name = input('\nPlease enter your name: ')
            
        customer_address = input('\nPlease enter your address: ')
        while customer_address == '':
            invalid_input()
            customer_address = input('\nPlease enter your address: ')
        
        customer_number = int(input('\nPlease enter your phone number: '))
        
        read_product_from_database()
        customer_product_choice = input('\nPlease select your product via the ID: ')
        
        read_courier_from_database()
        customer_courier_choice = int(input(f'\nPlease enter which courier you would like: '))
        
        new_order_status = order_status[1]
        
        write_into_order_database(customer_name, customer_address, customer_number,customer_product_choice,customer_courier_choice,new_order_status)
        
        print(f'{Print_colours.yellow}\nUpdated orders in progress: {Print_colours.reset}')
        read_orders_from_database()
        re_main_menu()
        
        main_menu()
    elif order_menu_option == 3:
        
        for key, value in enumerate(orders_in_progress):
            print(key, value)
                
            desired_order = int(input(f'\nPlease enter which order from you would like to update from 0 to {len(orders_in_progress) }: '))
            
            for key, value in enumerate(order_status):
                print(key, value)
                
            new_order_status = int(input('\nwhat would you like your new order status to be?: '))
            
            order_to_update = orders_in_progress[desired_order]
            order_to_update['order_status'] = order_status[new_order_status]
            
            print(f'\n{orders_in_progress[desired_order]} - Here is your order with the updated order status. You will now return to main menu ')
            main_menu()
            
    elif order_menu_option == 4:
        
        for key, value in enumerate(orders_in_progress):
            print(key, value)
        
        which_order_input = int(input(f'\nPlease select which order you would like to update from 0 to {len(orders_in_progress) - 1 }: '))
        
        while which_order_input < 0  or  which_order_input > len(orders_in_progress) - 1:
            print('Invalid input. Please try again')
            which_order_input = int(input(f'\nPlease select which order you would like to update from 0 to {len(orders_in_progress) - 1 }: '))
            
        order_to_update = orders_in_progress[which_order_input]
        
        for key,value in order_to_update.items():
            user_input_value = input(
            f'\n{key} Has value of {value}. Enter new value for {key}: ')

            if user_input_value == '':
                order_to_update[key] = value
                print('\nValue has not been changed.')
            else:
                order_to_update[key] = user_input_value
            
        print(f'\nYou have successfully updated your order. You wll now return to main menu')
        main_menu()
        
    else:
        order_menu_option == 5

        read_orders_from_database()
        
        which_order_input_2 = int(input(f'\nPlease select which order you would like to delete via ID: '))
        
        delete_order_from_database(which_order_input_2)
        
        read_orders_from_database()
        
        re_main_menu()
        
        main_menu()
main_menu()

