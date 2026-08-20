# code for problem 9.14:
import random
from random import randint

tup = (1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e')

choice = random.sample(tup,4)

print("any ticket number bellow are the winners")
for c in choice:
    print(c)
