# code for problem 7.4:
message = "Enter a pizza topping (type 'quit' to finish) \n:"
toppings = ''

active = True
while active:
    toppings = input(message)

    if toppings == 'quit':
        active = False
    else:
        print(f"I will add {toppings} to your pizza")
