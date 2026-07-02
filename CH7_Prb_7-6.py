# code for problem 7.6:
# code from problem 7.4:
message = "Enter a pizza topping (type 'quit' to finish) \n:"
toppings = ''

# exit using flag:
active = True
while active:
    toppings = input(message)

    if toppings == 'quit':
        active = False
    else:
        print(f"I will add {toppings} to your pizza")

# exit using condition:
message = "Whats your age? \n{type '0' if you dont want to buy ticket now} \n:"

age = (input(message))
age = int(age)
while age != 0:
    if age < 3:
        print("Tickets are free for under 3 years of age")
    elif 2 < age < 13:
        print(f"You have to pay $10 as your age is {age}")
    elif age > 12:
        print(f"you have to pay $15 as your age is {age}")
    age = int(input("What's your age? (0 to quit): "))

# exit using quit value:
message = "Whats your age? \n{type 'quit' if you dont want to buy ticket now} \n:"

while True:
    age = (input(message))
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Tickets are free for under 3 years of age")
    elif 2 < age < 13:
        print(f"You have to pay $10 as your age is {age}")
    else:
        print(f"you have to pay $15 as your age is {age}")
