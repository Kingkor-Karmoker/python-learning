# code for problem 9.3:
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

user1 = User('Kingkor', 'Karmoker', '28-april-2003', 'Student')
user2 = User('Shaily', 'Saha', '12-december-2003', 'Student')
user3 = User('Wasik', 'Billah', '12-february-2003', 'Student')

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
print()
user3.describe_user()
user3.greet_user()
