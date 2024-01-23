total_bill = 0
def choosing_your_order():
    global total_bill
    bill = 0
    order = input('choose between {pizza, burger, salad}: ')
    order = order.lower()
    if order in {'pizza', 'burger', 'salad'}:
        if order == 'pizza':
            bill += 20
            def choosing_pizza_quantity():
                number = input('choosing your pizza quantity: ')
                def if_integer(number):
                    try:
                        int(number)
                        return True
                    except ValueError:
                        return False
                if not if_integer(number):
                    print('invalid number, pls try again, press any key')
                    return choosing_pizza_quantity()
                
                return int(number)
            pizza_number = choosing_pizza_quantity()
            
            def choosing_pizza_size():
                nonlocal bill
                size = input('choose between {small, medium, large}: ')
                size = size.lower()
                if size == 'small':
                    bill += 5
                elif size == 'medium':
                    bill += 10
                elif size == 'large':
                    bill += 15
                    
                else:
                    print('invalid size, pls try again, press any key')
                    return choosing_pizza_size()
            choosing_pizza_size()
            bill *= pizza_number
            total_bill  += bill
            
        elif order == 'burger':
            bill += 4
            def choosing_burger_quantity():
                number = input('choosing your burger quantity: ')
                def if_integer(number):
                    try:
                        int(number)
                        return True
                    except ValueError:
                        return False
                if not if_integer(number):
                    print('invalid number, pls try again, press any key')
                    return choosing_burger_quantity
                
                return int(number)
            choosing_burger_quantity()
            burger_number = choosing_burger_quantity()
            
            def choosing_burger_type():
                nonlocal bill
                type = input('choose between {vegan, default, special}: ')
                type = type.lower()
                if type == 'vegan':
                    bill += 0
                elif type == 'default':
                    bill += 2
                elif type == 'special':
                    bill += 6
                    
                else:
                    print('invalid type, pls try again, press any key')
                    return choosing_burger_type()
            choosing_burger_type()
            bill *= burger_number
            total_bill += bill
                
        elif order == 'salad':
            bill += 3
            def choosing_salad_quantity():
                number = input('choosing your salad quantity: ')
                def if_integer(number):
                    try:
                        int(number)
                        return True
                    except ValueError:
                        return False
                if not if_integer(number):
                    print('invalid number, pls try again, press any key')
                    return choosing_salad_quantity()
                
                return int(number)
            choosing_salad_quantity()
            salad_number = choosing_salad_quantity()
            
            def choosing_salad_type():
                nonlocal bill
                type = input('choose between {french, italy}: ')
                type = type.lower()
                if type == 'french':
                    bill += 7
                elif type == 'italy':
                    bill += 2
                else:
                    print('invalid type, pls try again, press any key')
                    return choosing_salad_type()
            choosing_salad_type()
            bill *= salad_number
            total_bill += bill
            
    else:
        print('invalid input, pls try again, press any key')
        choosing_your_order()
        
    def order_repeat():
        print(f'your total payment is {total_bill}')
        order_continue = input('would you like to order more {yes, no}: ')
        if order_continue in {'y', 'yes'}:
            choosing_your_order()
            order_repeat()
            
        elif order_continue in ('n', 'no'):
            exit()
            
        else:
            print('invalid key, pls try again, press any key')
            order_repeat()
    order_repeat()



from run_time_algorithm import run_time_algorithm
if __name__ == '__main__':
    run_time_algorithm('choosing_your_order')