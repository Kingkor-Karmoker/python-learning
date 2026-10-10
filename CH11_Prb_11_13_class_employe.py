# code for problem 11.3:
class Employee:
    def __init__(self, name, last_name, salary):
        self.name = name
        self.salary = salary
        self.last_name = last_name

    def giveRaise(self, amount=5000):
        self.salary += amount
