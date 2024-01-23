total_bill = 0
switch = True

def choosing_food_order():
    global total_bill
    bill = 0
    food_order = input('choose between {pizza, burger, salad}: ')
    food_order = food_order.lower()
    if food_order in {'pizza', 'burger', 'salad'}:
        if food_order == 'pizza':
            bill += 20
            print('you re choosing pizza')
            
            pizza_number = int(input('choose your number: '))
            def choose_pizza_size():
                nonlocal bill
                pizza_size_input = input('choose your pizza size {small, medium, large}: ')
                pizza_size_input = pizza_size_input.lower()
                if pizza_size_input == "small":
                    bill += 5
                elif pizza_size_input == "medium":
                    bill += 10
                elif pizza_size_input == "large":
                    bill += 15
                else:
                    print('invalid option')
                    choose_pizza_size()
            
            choose_pizza_size()
            bill *= pizza_number
            total_bill += bill
            
        elif food_order == 'burger':
            bill += 5
            print('you re choosing burger')
        
            burger_number = int(input('choose your number: '))
            def cheese_addition_option_choice():
                nonlocal bill    
                cheese_addition_option_input = input('want cheese or not {yes, no}: ')
                cheese_addition_option_input = cheese_addition_option_input.lower()
                if cheese_addition_option_input in {'yes', 'y'}:
                    bill += 2
                elif cheese_addition_option_input in {'no', 'n'}:
                    pass
            
            cheese_addition_option_choice()
            bill *= burger_number
            total_bill += bill

        elif food_order == 'salad':
            bill += 10
            print('you re choosing salad')
            salad_number = int(input('choose your number: '))
            def salad_type_of_dressing_choice():
                nonlocal bill
                pizza_size_input = input('choose your type of dressing {Italian, Rance, Ceasar}: ')
                pizza_size_input = pizza_size_input.lower()
                if pizza_size_input == "italian":
                    bill += 5
                elif pizza_size_input == "ranch":
                    bill += 10
                elif pizza_size_input == "ceasar":
                    bill += 15
            
            salad_type_of_dressing_choice()
            bill *= salad_number
            total_bill += bill
            
        print(f'your total payment: {total_bill}')
        
        def choice_function():
            global switch
            choice = input('would you like to continue to order {yes, no}: ')
            choice = choice.lower()
            if choice in {'yes', 'y'}:
                choosing_food_order()
            elif choice in {'no', 'n'}:
                exit()
            else:
                choice_function()
                
        choice_function()
        
    else:
        print('invalid order')
        choosing_food_order()

choosing_food_order()