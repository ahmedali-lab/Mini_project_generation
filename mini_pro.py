
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
couriers_5 = 'Herman'

appending_couriers = couriers_list.append
appending_couriers(couriers_1)
appending_couriers(couriers_2)
appending_couriers(couriers_3)
appending_couriers(couriers_4)
appending_couriers(couriers_5)

# with open('products.txt', 'r') as f:
#     f.readline()

#### MAIN MENU FUNCTION ####

def main_menu():
    main_menu_options = int(input('Please select 0 to exit app, 1 for product options or 2 for courier options: '))
#  GET user input for main menu option
#  IF user input is 0:
#  EXIT app
    if main_menu_options == 0:
        #leave app
        print('You have exited the app')
    elif main_menu_options == 1: 
        #print products list and return products list menu
        print(products_list)
        product_menu()
    else:
        main_menu_options == 2
        print(couriers_list)
        courier_menu()
        
#### PRODUCT MENU FUNCTION ####

def product_menu():
# PRINT product menu options 
# GET user input for product menu option
    product_menu_option = int(input(
'''
Please select: 
0 to return to the main menu, 
1 to view product list, 
2 to add your new product and view courier menu, 
3 to add product at specific position or 
4 to delete specific product: 

'''))
    
    if  product_menu_option == 0:
# IF user input is 0: RETURN to main menu
        main_menu()
    elif product_menu_option== 1:
# IF user input is 1: Print product list
        print(products_list)
    elif product_menu_option == 2:
        new_user_product = input('Please add new product: ')
        appending_product_list(new_user_product)
        print(products_list)
# GET user input for courier menu option
    elif product_menu_option == 3:
# STRETCH GOAL - UPDATE existing product
#  PRINT product names with its index value
        for index, value in enumerate(products_list):
            print(index, value)
        print(products_list)
#  GET user input for product index value
        new_product_index_value = int(input('Please enter index value: '))
#  GET user input for new product name
        new_user_product =  input('Please add new product: ')
#  UPDATE product name at index in products list
        products_list.insert(new_product_index_value, new_user_product)
        print(products_list)
    elif product_menu_option == 4:
# STRETCH GOAL - DELETE product
#  PRINT products list
        print(products_list)
#  GET user input for product index value
        new_product_index_value = int(input('Please enter index value: '))
#  DELETE product at index in products list
        del products_list[new_product_index_value]
        print(products_list)

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
    if couriers_menu_option == 0:
        main_menu()
    elif couriers_menu_option == 1:
        print(couriers_list)
    elif couriers_menu_option == 2:
        new_user_courier = input('Please add new courier: ')
        couriers_list.append(new_user_courier)
        print(couriers_list)
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

main_menu()

