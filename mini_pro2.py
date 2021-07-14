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

couriers_list = []
couriers_1 = 'Phill'
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

print(couriers_list)
# LOAD products list from products.txt
# LOAD couriers list from couriers.txt

# PRINT main menu options
# GET user input for main menu option
# IF user input is 0:    

#     SAVE products list to products.txt    
#     SAVE couriers list to couriers.txt    
#     EXIT app

# products menu
# ELSE IF user input is 1:    
# PRINT product menu options    
# GET user input for product menu option

# IF user inputs 0:        
#     RETURN to main menu    

# ELSE IF user input is 1:        
#     PRINT products list    

# ELSE IF user input is 2:        
#     # CREATE new product        
#     # GET user input for product name        
#     # APPEND product name to products list    
#     # 
# ELSE IF user input is 3:         
# # STRETCH GOAL - UPDATE existing product
# PRINT product names with its index value      
# GET user input for product index value    
# GET user input for new product name       
# UPDATE product name at index in products list

# ELSE IF user input is 4:        
#     # STRETCH GOAL - DELETE product        
#     # PRINT products list        
#     # GET user input for product index value        
#     # DELETE product at index in products list
    
# # couriers menu
# # ELSE IF user input is 2:    
# # PRINT courier menu options    
# # GET user input for courier menu option    

# # IF user inputs 0:        
# # RETURN to main menu    
# # ELIF user inputs 1:        
# # PRINT couriers list   
# # ELSE IF user input is 2:        
# # # CREATE new courier        
# # GET user input for courier name        
# # APPEND courier name to couriers list    
# # ELSE IF user input is 3:         
# # # STRETCH GOAL - UPDATE existing courier        
# # PRINT courier names with its index value        
# # GET user input for courier index value        
# # GET user input for new courier name        
# # UPDATE courier name at index in couriers list    
# # ELSE IF user input is 4:        
# # # STRETCH GOAL - DELETE courier        
# # PRINT courier list
# GET user input for courier index value        
# DELETE courier at index in courier list
#         product_menu_option = int(input(
# '''
# Please select: 
# 0 to exit app, 
# 1 to view product list, 
# 2 to add your new product, 
# 3 to add product at specific position or 
# 4 to delete specific product: 
# '''))
#         return product_menu_option
    
#     f  == 0:
#         main_menu()
#     elif == 1:
#         print(products_list)
#     elif () == 2:
#         new_user_product = input('Please add new product: ')
#         appending_product_list(new_user_product)
#         print(products_list)
#     elif () == 3:
# # STRETCH GOAL - UPDATE existing product
# #  PRINT product names with its index value
#         for index, value in enumerate(products_list):
#             print(index, value)
#         print(products_list)
# #  GET user input for product index value
#         new_product_index_value = int(input('Please enter index value: '))
# #  GET user input for new product name
#         new_user_product =  input('Please add new product: ')
# #  UPDATE product name at index in products list
#         products_list.insert(new_product_index_value, new_user_product)
#         print(products_list)
#     elif m() == 4:
# # STRETCH GOAL - DELETE product
# #  PRINT products list
#         print(products_list)
# #  GET user input for product index value
#         new_product_index_value = int(input('Please enter index value: '))
# #  DELETE product at index in products list
#         del products_list[new_product_index_value]
#         print(products_list)

# product_menu()