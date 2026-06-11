# code for chapter 4 problem 13:
buffet_food = ('Fish curry', 'Chicken curry', 'Lentils soup', 'Vegetables', 'Smashed potato')

for offers in buffet_food:
    print(f"Resturant offers: {offers}")

# trying to see if python rejects mutilation of tuple:
# (remve # to check the error) buffet_food[0] = 'Salad'

# But tuple can be rewritten:
buffet_food = ('Fish curry', 'Chicken curry', 'Lentils soup', 'Vegetables', 'Salad')

for new in buffet_food:
    print(new)
print(f"5th Item was smashed potato and now its changed with {buffet_food[-1]}")
