from typing import Dict
from funcs import read_csv_file, write_csv_file, append_dict
import csv

    
products_list = [] 

read_products_csv = read_csv_file('products.csv', products_list)


couriers_list = []

read_couriers_csv = read_csv_file('couriers.csv',couriers_list)


orders_in_progress = []

order_csv = read_csv_file('orders.csv',couriers_list)

order_status = ['PREPARING', 'EN ROUTE', 'DELIVERED']

#### MAIN MENU FUNCTION ####

def main_menu():
#GET user input for main menu option
    main_menu_options = int(input('Please select 0 to exit app, 1 for product options, 2 for courier options or 3 to for order options: \n'))
    
    while main_menu_options < 0 or main_menu_options > 3:
        print('Invalid input')
        main_menu_options = int(input('Please select 0 to exit app, 1 for product options, 2 for courier options or 3 for order options: \n'))
    
    if main_menu_options == 0:
#LOAD products list from products.txt
#LOAD couriers list from couriers.txt
        
        # with open('products.txt') as f:
        #     for x in products_list:
        #         f.readlines()
        
        # with open('couriers.txt') as f_2:
        #     for x in couriers_list:
        #         f_2.readlines()  
#LEAVE APP
        print('You have exited the app')
        
    elif main_menu_options == 1: 
#print products list and return products list menu

        for i in read_products_csv:
            print(i)
            
        print('\n Here are the current avaliable products. You will now enter the product menu.\n')
        
        product_menu()
        
    elif main_menu_options == 2:
#print couriers list and return couriers list menu DONT WORRY ABOUT THIS YET
        for key, value in enumerate(read_couriers_csv):
            print(key, value)
        print('\n Here are the current avaliable couriers. You will now enter the courier menu.\n')
        courier_menu()
    else:
        main_menu_options == 3
        order_menu()
        
#### PRODUCT MENU FUNCTION ####

def product_menu():

    product_menu_option = int(input(
'''
Please select: 
0 to return to the main menu, 
1 to view product list, 
2 to add a new product, 
3 to add product at a specific position or 
4 to delete specific product: \n
'''))
    
    while product_menu_option < 0 or product_menu_option > 4:
        print('Invalid input')
        product_menu_option = int(input(
'''
Please select: 
0 to return to the main menu, 
1 to view product list, 
2 to add a new product, 
3 to add product at a specific position or 
4 to delete specific product: \n
'''))
        
    if  product_menu_option == 0:
        
        main_menu()
        
    elif product_menu_option== 1:
        
        for i in read_products_csv:
            print(i)
            
        print('\n Here are the current avaliable products. You will now return to the main menu.\n')
        
        main_menu()
        
    elif product_menu_option == 2:
        
        new_product = input('Please enter product you would like to add: \n')
        new_product_price = float(input('Please enter new product price: \n'))
        
        
        emp_dict = {}
        emp_dict['product_name'] = new_product
        emp_dict['product_price'] = new_product_price
        headers = ['product_name', 'product_price']
        
        append_dict('products.csv', emp_dict, headers)
        
        print(f'{emp_dict} - Here is your new product and price \n' )
        
        main_menu()

    elif product_menu_option == 3:
        
        for index, value in enumerate(read_products_csv):
            print(index, value)
            
        # print(f'{products_list}')

        # new_product_index_value = int(input('Please enter index value: \n'))

        # new_user_product =  input('Please add new product: \n')
    
        # products_list.insert(new_product_index_value, new_user_product)
        
        # print(f'{products_list} - Here is the current list of products. You will now return to main menu \n')
        # main_menu()

    elif product_menu_option == 4:
            
        print('\n Current product list looks like this:')
        for (i, item) in enumerate(products_list, start = 0):
            print(i, item)
            
        
        new_product_index_value = int(input('Please enter the number value you would like to delete: '))
        # FIX THIS BEFORE MOVING ON!!!!
        # while new_product_index_value > len(products_list) or new_product_index_value < len(products_list):
        #     print('Invalid input')
        #     new_product_index_value = int(input('Please enter the num value you would like to delete: '))

        del products_list[new_product_index_value]
        print(f'''{products_list} \n  You have successfully deleted the product Here is the current list of products. 
                                            You will now return to main menu \n''')
        main_menu()

#### COURIER FUNCTION ####

def courier_menu():
    couriers_menu_option = int(input(
'''
Please select: 
0 to return to the main menu, 
1 to view couriers_ list, 
2 to add new courier, 
3 to add courier at specific position or 
4 to delete specific courier: 

'''))
    while couriers_menu_option < 0 or couriers_menu_option > 4:
        print('Invalid input')
        couriers_menu_option = int(input(
'''
Please select: 
0 to return to the main menu, 
1 to view couriers_ list, 
2 to add new courier, 
3 to add courier at specific position or 
4 to delete specific courier: \n 
'''))
    
    if couriers_menu_option == 0:
        main_menu()
        
    elif couriers_menu_option == 1:
        print(couriers_list)
        
    elif couriers_menu_option == 2:
        
        new_user_courier = input('Please add new courier: ')
        
        couriers_list.append(new_user_courier)
        
        print(couriers_list)
        
        with open('couriers.txt', 'w') as f_2:
            for x in couriers_list:
                f_2.write("%s\n" % x)
                
    elif couriers_menu_option == 3:
        
        for index, value in enumerate(couriers_list):
            print(index, value)
            
        print(couriers_list)
        
        new_courier_index_value = int(input('Please enter index value: '))
        
#  GET user input for new courier name

        new_user_courier =  input('Please add new courier name: ')
        
#  UPDATE courier name at index in couriers list

        couriers_list.insert(new_courier_index_value, new_user_courier)
        
        print(couriers_list)
        
    elif couriers_menu_option == 4:
# STRETCH GOAL - DELETE courier
#  PRINT products list

        print(couriers_list)
        
#  GET user input for courier index value

        new_courier_index_value = int(input('Please enter index value: '))
#  DELETE product at index in products list

        del couriers_list[new_courier_index_value]
        
        print(couriers_list)
        
def order_menu():
    order_menu_option = int(input(
'''
Please select: 
0 to return to the main menu, 
1 to view orders status, 
2 to make an order, 
3 update existing order status  
4 to update an existing order or
5 to delete a courier 

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
        # GET user input for customer phone number
        customer_address = input('Please enter your address: \n')
        customer_number = int(input('Please enter your phone number: \n'))
        # PRINT couriers list with index value for each courier
        for index, value in enumerate(couriers_list):
            print(index, value)
        # GET user input for courier index to select courier
        courier_index_value = int(input(f'Please enter which courier you would like from 0 to {len(couriers_list) - 1}: '))
        # SET order status to be 'PREPARING'
        # APPEND order to orders list
        order_dict = {
            'Customer name': customer_name,
            'Customer address': customer_address,
            'Customer number': customer_number,
            'Courier': couriers_list[courier_index_value],
            'Order status': order_status[0]
        }
        orders_in_progress.append(order_dict)
        
        print(f'{orders_in_progress} - Here is your current order. You will now return to main menu /n' )
        main_menu()
        
    elif order_menu_option == 3:
        
        if orders_in_progress != []:
            
            for index, value in enumerate(orders_in_progress):
                print(index, value)
                
            desired_order = int(input(f'Please enter which from you would like to update from 0 to {len(orders_in_progress) - 1 }: '))
            
            order_to_update = orders_in_progress[desired_order]

            new_order_status = input('what would you like your new order status to be?: \n')
            while new_order_status == '':
                print('Cannot be left blank')
                new_order_status = input('what would you like your new order status to be?: \n')
            
            order_to_update['Order status'] = new_order_status
            print(f'{order_to_update} - Here is your order with your updated order status. You will now return to main menu \n')
            main_menu()
            
        else:
            print('there are currently no orders - You will now return to order menu')
            order_menu()
            
    elif order_menu_option == 4:
        
        for key, value in enumerate(orders_in_progress):
            print(key, value)
        
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
            
        print(f'{orders_in_progress} - Here is a list of current orders. You wll now return to main menu')
        main_menu()
        
    else:
        order_menu_option == 5
        
        for key, value in enumerate(orders_in_progress):
                print(key, value)
        
        which_order_input_2 = int(input(f'Please select which order you would like to update from 0 to {len(orders_in_progress) - 1 }: \n'))
        
        del orders_in_progress[which_order_input_2]
        
        print(orders_in_progress)
        main_menu()
        
main_menu()

