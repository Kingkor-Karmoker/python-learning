# code for problem 7.9:
# from problem 7.8:
sandwich_orders = ['veggies sandwich', 'pastrami', 'Chicken sandwich', 'pastrami', 'sub sandwich', 'egg sandwich', 'pastrami']
finished_sandwiches = []

print("deli has run out of pastrami \n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    ordered = sandwich_orders.pop(0)

    finished_sandwiches.append(ordered)
    print(f"I made your {ordered}")

print('\n')
for sandwich in finished_sandwiches:
    print(f"your {sandwich} is ready to eat")
