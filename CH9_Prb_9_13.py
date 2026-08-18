# code for problem 9.13:
from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

roll = Die()
roll1 = Die(10)
roll2 = Die(20)

roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
print()

for rl in range(10):
    roll1.roll_die()

print()

for rl in range(10):
    roll2.roll_die()
