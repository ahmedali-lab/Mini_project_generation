#  CREATE products list
products_list = [] 
product_1 = 'coke'
product_2 = 'rubicon mango'
product_3 = 'vimto'
product_4 = 'diet coke'
product_5 = 'pepsi'

appending_product_list = products_list.append
appending_product_list(product_1)
appending_product_list(product_2)
appending_product_list(product_3)
appending_product_list(product_4)
appending_product_list(product_5) 

#  CREATE couriers list
couriers_list = []
couriers_1 = 'Phil'
couriers_2 = 'Gregg'
couriers_3 = 'James'
couriers_4 = 'Bob'
couriers_5 = 'Rumaanah'

appending_couriers = couriers_list.append
appending_couriers(couriers_1)
appending_couriers(couriers_2)
appending_couriers(couriers_3)
appending_couriers(couriers_4)
appending_couriers(couriers_5)
    

orders_in_progress = []

order_status = ['PREPARING', 'EN ROUTE', 'DELIVERED']

#### MAIN MENU FUNCTION ####

def main_menu():
#GET user input for main menu option
    main_menu_options = int(input('Please select 0 to exit app, 1 for product options, 2 for courier options or 3 to make an order: \n'))
    
    while main_menu_options < 0 or main_menu_options > 3:
        print('Invalid input')
        main_menu_options = int(input('Please select 0 to exit app, 1 for product options, 2 for courier options or 3 to make an order: \n'))
    
    if main_menu_options == 0:
#LOAD products list from products.txt
#LOAD couriers list from couriers.txt

        with open('products.txt') as f:
            for x in products_list:
                f.readlines()
        
        with open('couriers.txt') as f_2:
            for x in couriers_list:
                f_2.readlines()  
#LEAVE APP
        print('You have exited the app')
        
    elif main_menu_options == 1: 
#print products list and return products list menu
        print(f'Here is the current avaliable products: {products_list})')
        product_menu()
        
    elif main_menu_options == 2:
#print couriers list and return couriers list menu
        print(f'Here is the current avaliable couriers: {couriers_list})')
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
        
        print(f'{products_list} - Here is the current list of products. You will now return to main menu \n')
        main_menu()
        
    elif product_menu_option == 2:
        
        new_user_product = input('Please enter product you would like to add: \n')
        
        appending_product_list(new_user_product)
        
        with open('products.txt', 'w') as f:
            for x in products_list:
                f.write("%s\n" % x)
        
        print(f'{products_list} - Here is the current list of products. You will now return to main menu \n')
        main_menu()

    elif product_menu_option == 3:
        
        for index, value in enumerate(products_list):
            print(index, value)
        print(f'{products_list}')

        new_product_index_value = int(input('Please enter index value: \n'))

        new_user_product =  input('Please add new product: \n')
    
        products_list.insert(new_product_index_value, new_user_product)
        
        print(f'{products_list} - Here is the current list of products. You will now return to main menu \n')
        main_menu()

    elif product_menu_option == 4:
            
        print('\n Current product list looks like this:')
        for (i, item) in enumerate(products_list, start = 0):
            print(i, item)
            
        
        new_product_index_value = int(input('Please enter the num value you would like to delete: '))
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

        if orders_in_progress == []:
            print('there are currently no orders')
            
    elif order_menu_option == 2:
        
        customer_name = input('Please enter your name: ')
        # GET user input for customer phone number
        customer_address = input('Please enter your address: ')
        customer_number = int(input('Please enter your phone number: '))
        # PRINT couriers list with index value for each courier
        for index, value in enumerate(couriers_list):
            print(index, value)
        # GET user input for courier index to select courier
        courier_index_value = int(input(f'Please enter which courier you would like from 0 to {len(couriers_list)}: '))
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
        
        print(f'{orders_in_progress} - Here is your current order. You will now return to main menu' )
        main_menu()
    elif order_menu_option == 3:
        
        if orders_in_progress != []:
        # STRETCH - UPDATE existing order
        # PRINT orders list with its index values
            for index, value in enumerate(orders_in_progress):
                print(index, value)
        # GET user input for order index value
            desired_order = int(input(f'Please enter which from you would like to update from 0 to {len(orders_in_progress) }: '))
            order_to_update = orders_in_progress[desired_order]
#     FOR EACH key-value pair in selected order:
            new_order_status = input('what would you like your new order status to be?: \n')
            while new_order_status != '':
                order_to_update['Order status'] = new_order_status
                print(order_to_update)
                break
            else:
                print('Cannot be left blank')
#         GET user input for updated property

#         IF user input is blank:
        # while order_to_update == '':
        #     print('you cannot leave this blank')
        #     continue
        # else:
        
            

#             do not update this property
#         ELSE:
#             update the property value with user input
        else:
            print('there are currently no orders')
            
        order_menu_option == 4
        pass
        
main_menu()

