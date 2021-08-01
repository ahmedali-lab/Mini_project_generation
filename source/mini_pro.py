from typing import Dict
from funcs import read_csv_file, write_csv_file, append_dict, update_items, write_into_courier_database, read_courier_from_database, read_product_from_database, write_into_product_database, delete_products_from_database, delete_courier_from_database
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

def main_menu():

    main_menu_options = int(input('''\nPlease select 0 to exit app and save data, 1 for product options, 2 for courier options or 3 to for order options: '''))
    
    while main_menu_options < 0 or main_menu_options > 3:
        print('Invalid input')
        main_menu_options = int(input('Please select 0 to exit app, 1 for product options, 2 for courier options or 3 for order options: \n'))
    
    if main_menu_options == 0:
        
        write_csv_file('products.csv', products_list)
        write_csv_file('couriers.csv', couriers_list)
        write_csv_file('orders.csv', orders_in_progress)

        print('You have successfully saved your changes and will now exit app')
        
    elif main_menu_options == 1: 

        for i in products_list:
            print(i)
        print('\n Here are the current avaliable products. You will now enter the product menu.\n')
        
        product_menu()
        
    elif main_menu_options == 2:

        for i in couriers_list:
            print(i)
        print('\n Here are the current avaliable couriers. You will now enter the courier menu.\n')
        courier_menu()
        
    else:
        main_menu_options == 3
        order_menu()
        
#### PRODUCT MENU FUNCTION ####

def product_menu():

    product_menu_option = int(input(
'''
\nPlease select: 
0 to return to the main menu, 
1 to view product list, 
2 to add a new product, 
3 to update an existing product or 
4 to delete a product: \n
'''))
    
    while product_menu_option < 0 or product_menu_option > 4:
        print('Invalid input')
        product_menu_option = int(input(
'''
\nPlease select: 
0 to return to the main menu, 
1 to view product list, 
2 to add a new product, 
3 to update an existing product or 
4 to delete a product: 
'''))
        
    if  product_menu_option == 0:
        
        main_menu()
        
    elif product_menu_option== 1:
        
        # for i in products_list:
        #     print(i)
        read_product_from_database()
        print('\n Here are the current avaliable products. You will now return to the main menu.\n')
        main_menu()
        
    elif product_menu_option == 2:
        
        print('\nproduct list: ')
        read_product_from_database()
        new_product = input('\nPlease enter product you would like to add: ')
        new_product_price = float(input(('\nPlease enter new product price: ')))
        write_into_product_database(new_product, new_product_price)
        
        
        print('new list: ')
        read_product_from_database()
        
        
        # emp_dict = {}
        # emp_dict['product_name'] = new_product
        # emp_dict['product_price'] = new_product_price
        # products_list.append(emp_dict)
        # headers = ['product_name', 'product_price']
        
        # append_dict('products.csv', emp_dict, headers)
        
        # print(f'\n{emp_dict} - Here is your new product and price. You will now return to main menu. ' )
        
        main_menu()

    elif product_menu_option == 3:
        
        for index, value in enumerate(products_list):
            print(index, value)
        
        user_index_value = int(input('please enter your desired product index number to update'))
        new_var = products_list[user_index_value]
        update_items(new_var)
        
        print(f'{new_var} - Here is your updated product item \n')
        
        main_menu()
        
    elif product_menu_option == 4:
        
        print('\nCurrent product list: ')
        read_product_from_database()
        
        product_to_delete = int(input('\nPlease select which product you would like to delete via ID'))
        delete_products_from_database(product_to_delete)
        
        print('\nNew product list: ' )
        read_product_from_database()
        print('\nYou will now return to main menu')
        main_menu()
        
        # print('Current product list looks like this: \n')
        # for (key, value) in enumerate(products_list):
        #     print(key, value)
            
        
        # new_product_index_value = int(input('\nPlease enter the product number value you would like to delete: '))

        # del products_list[new_product_index_value]
        
        # print(f'''\nYou have successfully deleted the product Here is the current list of products: ''')
        
        # for (key, value) in enumerate(products_list):
        #     print(key, value)

        # print('\n You will now return to main menu.')
        

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
        print('Invalid input')
        couriers_menu_option = int(input(
'''
\nPlease select: 
0 to return to the main menu, 
1 to view couriers_ list, 
2 to add new courier, 
3 to update  an existing courier or 
4 to delete a courier:   
'''))
    
    if couriers_menu_option == 0:
        main_menu()
        
    elif couriers_menu_option == 1:
        
        # for i in couriers_list:
        #     print(i)
            
        
        print('\nHere are the current avaliable couriers. You will now return to the main menu. ')
        
        read_courier_from_database()
        
        main_menu()
        
    elif couriers_menu_option == 2:
        
        print('\nCurrent couriers list: ')
        read_courier_from_database()
        new_courier = input('\nPlease enter new courier name: ')
        new_courier_phone_number = input('\nPlease enter new courier phone number: ')
        write_into_courier_database(new_courier, new_courier_phone_number)
        
        # emp_dict2 = {}
        # emp_dict2['courier_name'] = new_courier 
        # emp_dict2['courier_number'] = new_courier_phone_number
        # couriers_list.append(emp_dict2)
        # headers2 = ['courier_name', 'courier_number']
        
        #append_dict('couriers.csv', emp_dict2, headers2)
        
        #print(f'\n{emp_dict2} - Here is your new courier name and number. You will now return to main menu. ' )
        
        print('\n New courier list: ')
        read_courier_from_database()
        
        main_menu()
        
    elif couriers_menu_option == 3:
        
        for index, value in enumerate(couriers_list):
            print(index, value)
        
        user_index_value2 = int(input('\nplease enter your desired courier index number to update '))
        new_var2 = couriers_list[user_index_value2]
        update_items(new_var2)
        
        print(f'\n{new_var2} - Here is your updated courier information')
        
        main_menu()
        
    elif couriers_menu_option == 4:
        
        print('\nCurrent courier list: ')
        read_courier_from_database()
        
        courier_to_delete = int(input('\nPlease select which courier you would like to delete via ID: '))
        delete_courier_from_database(courier_to_delete)
        
        print('\nNew product list: ' )
        read_courier_from_database()
        print('\nYou will now return to main menu')
        main_menu()
        # for index, value in enumerate(couriers_list):
        #         print(index, value)
        
        # new_courier_index_value = int(input('\nPlease the number index value of courier info you would like to delete: '))

        # del couriers_list[new_courier_index_value] 
        
        # for index, value in enumerate(couriers_list):
        #         print(index, value)
        #         print('\nHere is your new list of couriers')

def order_menu():
    order_menu_option = int(input(
'''
\n Please select: 
0 to return to the main menu, 
1 to view orders status, 
2 to make an order, 
3 update existing order status  
4 to update an existing order or
0 to delete an order 

'''))
    if order_menu_option == 0:
            main_menu()
        
    elif order_menu_option == 1:
        if orders_in_progress != []:
            print(orders_in_progress)
        else:
            print('there are currently no orders')
        
        main_menu()
            
    elif order_menu_option == 2:
        
        customer_name = input('Please enter your name: \n')
        customer_address = input('Please enter your address: \n')
        customer_number = int(input('Please enter your phone number: \n'))
        
        for key, value in enumerate(products_list):
            print(key, value)
        customer_product_choice = input('Please select your product')
        
        for key, value in enumerate(couriers_list):
            print(key, value)
        customer_courier_choice = int(input(f'Please enter which courier you would like from 0 to {len(couriers_list) - 1}: '))
        
        new_order = {}
        new_order['customer_name'] = customer_name 
        new_order ['customer_address'] = customer_address
        new_order ['customer_number'] = customer_number
        new_order['products'] = customer_product_choice
        new_order ['courier'] = customer_courier_choice
        new_order['status'] = order_status[0]
        
        order_headers = ['customer_name', "customer_address", 'customer_number','products', 'courier', 'status']
        
        append_dict('orders.csv', new_order, order_headers)
        
        print('Here is your new order', new_order)
        
        main_menu()
        
    elif order_menu_option == 3:
        
        if orders_in_progress != []:
            for key, value in enumerate(orders_in_progress):
                print(key, value)
                
            desired_order = int(input(f'\nPlease enter which from you would like to update from 0 to {len(orders_in_progress) - 1 }: '))
            
            for key, value in enumerate(order_status):
                print(key, value)
                
            new_order_status = int(input('\nwhat would you like your new order status to be?: '))
            
            order_to_update = orders_in_progress[desired_order]
            order_to_update['order_status'] = order_status[new_order_status]
            
            print(f'\n{orders_in_progress[desired_order]} - Here is your order with the updated order status. You will now return to main menu ')
            main_menu()
        else:
            print('there are currently no orders - You will now return to order menu')
            order_menu()
            
    elif order_menu_option == 4:
        
        for key, value in enumerate(orders_in_progress):
            print(key, value)
        
        which_order_input = int(input(f'Please select which order you would like to update from 0 to {len(orders_in_progress) - 1 }: \n'))
        
        while which_order_input < 0  or  which_order_input > len(orders_in_progress) - 1:
            print('Invalid input. Please try again')
            which_order_input = int(input(f'Please select which order you would like to update from 0 to {len(orders_in_progress) - 1 }: \n'))
            
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
        
        for key, value in enumerate(orders_in_progress):
                print(key, value)
        
        which_order_input_2 = int(input(f'Please select which order you would like to update from 0 to {len(orders_in_progress) - 1 }: \n'))
        
        del orders_in_progress[which_order_input_2]
        
        print(f'\nYou have successfully deleted your order. Here is a list of current orders in progress: {orders_in_progress}. You will now return to main menu.')
        main_menu()
        
main_menu()

