# code for problem 9.12(module2):
from CH9_Prb_9_12_module1 import *
class Privilege:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        for privilege in  self.privileges:
            print(privilege)
            print()

class Admin(User):
    def __init__(self,first_name,last_name,dob,profession):
        super().__init__(first_name,last_name,dob,profession)
        self.privileges = Privilege()
