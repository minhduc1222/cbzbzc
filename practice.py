total_bill = 0
def choosing_your_order():
    global total_bill # declare the outmost variable inside a function (make the function able to modify it in global scale)
    bill = 0 # payment for each order( which will finally be add to the total_bill till the code ends)
    
    order = input('choose between {pizza, burger, salad}: ')
    order = order.lower()
    if order in {'pizza', 'burger', 'salad'}:
        if order == 'pizza':
            bill += 20 # pizza = 20$ (initial value)
            def choosing_pizza_quantity():
                number = input('choosing your pizza quantity: ')
                
                def if_integer(number): # to validate the input( only accept the int value)
                    try:
                        int(number)
                        return True
                    except ValueError:
                        return False
                    
                if not if_integer(number): # to validate the input( only accept the int value)
                    print('invalid number, pls try again, press any key')
                    return choosing_pizza_quantity() # in case the first input invalid, then only right through many input, the first invalid one can return something
                
                return int(number)
            pizza_number = choosing_pizza_quantity() # also a way to call a function
            
            def choosing_pizza_size():
                nonlocal bill # declare a variable which originally locates outside of the being considered function, make the function impacts on the variable outside of its scale
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
            
            bill *= pizza_number # add to the current order payment
            total_bill  += bill # add to the final payment( combined of many orders)
            
        elif order == 'burger':
            bill += 4 # burger = 4$ (initial value)
            def choosing_burger_quantity():
                number = input('choosing your burger quantity: ') # to validate the input( only accept the int value)
                
                def if_integer(number):
                    try:
                        int(number)
                        return True
                    except ValueError:
                        return False
                    
                if not if_integer(number): # to validate the input( only accept the int value)
                    print('invalid number, pls try again, press any key') 
                    return choosing_burger_quantity
                
                return int(number)
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
            choosing_your_order() # repeat the order calculating process like above and this repeat function
            order_repeat()
            
        elif order_continue in ('n', 'no'):
            exit() # end the code if no
            
        else:
            print('invalid key, pls try again, press any key')
            order_repeat() # repeat this repeat function if the option is invalid
    order_repeat()

choosing_your_order()

from run_time_algorithm import run_time_algorithm
if __name__ == '__main__':
    run_time_algorithm('choosing_your_order')