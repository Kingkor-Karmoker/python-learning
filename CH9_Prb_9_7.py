# code for problem 9.7:
# code from 9.3:
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

class Admin(User):
    def __init__(self,first_name,last_name,dob,profession):
        super().__init__(first_name,last_name,dob,profession)
        self.privileges = []

    def show_privileges(self):
        for privilege in  self.privileges:
            print(privilege)
            print()

adm = Admin('John','Doe', '28 jun 2004', 'Businessman' )
adm.privileges = ["can add post", "can delete post", "can ban user"]
adm.show_privileges()
