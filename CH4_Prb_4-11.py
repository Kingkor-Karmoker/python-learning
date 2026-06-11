#code from chapter 4 problem 11:
#Code copied from problem 4.1:
favourite_Pizzas = ['Margherita', 'Pepperoni', 'Meat Lover', 'BBQ Chicken']

for pizza in favourite_Pizzas:
    print(pizza)
#modifying for loop:

for pizza in favourite_Pizzas:
    print(f"I love eating {pizza} pizza so much")
print("I really love to eat pizza's")

#code starts from here:
friends_favourite = favourite_Pizzas[:]

favourite_Pizzas.append('Vegies')
friends_favourite.append('Chocolate')

print("My favourite pizzas are:")
for my in favourite_Pizzas:
    print(my)
print('\n')

print("My friends favorite pizzas are:")
for friends in friends_favourite:
    print(friends)
