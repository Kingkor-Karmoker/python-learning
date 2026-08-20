# code for problem 9.15:
import random
tup = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')
my_ticket = [2, 9, 'd', 7]
loop = 0

flag = True
while flag:
    winning_ticket = random.sample(tup,4)
    loop += 1

    if set(winning_ticket) == set(my_ticket):
        flag = False

print(f"It took {loop} attempts to win this tickets{my_ticket}")
