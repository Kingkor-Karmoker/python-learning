# code for problem 7.8:
sandwich_orders = ['veggies sandwich', 'Chicken sandwich', 'sub sandwich', 'egg sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich}")

    finished_sandwiches.append(sandwich)

print('\n')
for san in finished_sandwiches:
    print(f"{san} was made")
