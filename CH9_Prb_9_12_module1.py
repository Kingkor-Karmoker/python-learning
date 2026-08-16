# code for problem 9.12(module1):
class User:
    def __init__(self,first_name,last_name,dob,profession):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.profession = profession

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of birth: {self.dob}")
        print(f"Profession: {self.profession}")

    def greet_user(self):
        print(f"Hello! {self.first_name}")
