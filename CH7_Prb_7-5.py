# code for problem 7.5:
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
