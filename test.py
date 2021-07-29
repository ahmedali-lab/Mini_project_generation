orders_in_progress = [{'c': 'a', 'b': 'c'}]

# for key, value in enumerate(orders_in_progress):
#     print(orders_in_progress[0]) 
desired_order = orders_in_progress[0]




for key, value in enumerate(order_list):
            print(key, value)
order_index = int(input('''
        \033[33m\n\tSelect and order to update:    \033[0m'''))
        
chosen_order = order_list[order_index]

        for key, value in chosen_order.items():

            chosen_value = input(
                f'\n{key} Has value of {value}. Enter new value for {key}: ')

            if chosen_value == '':
                chosen_order[key] = value
                print('\nNothing has been changed')
            else:
            chosen_order[key] = chosen_value

        print('Your order has been updated:', chosen_order)


with open('Product_list.csv', 'w', newline='') as file:
            fieldnames = ['Name', 'Price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products_list)





