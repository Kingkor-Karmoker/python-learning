# code for problem 9.5:
# code from 9.3:
class User:
    def __init__(self, first_name, last_name, dob, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.profession = profession
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of birth: {self.dob}")
        print(f"Profession: {self.profession}")

    def greet_user(self):
        print(f"Hello! {self.first_name}")

user = User('Kingkor', 'Karmoker', '28-april-2020', 'Student')

user.describe_user()
user.greet_user()
print()

print(f"{user.first_name} has logged in for {user.login_attempts} time")
print()
user.increment_login_attempts()
print(f"{user.first_name} has logged in for {user.login_attempts} time")
user.increment_login_attempts()
user.increment_login_attempts()
print(f"{user.first_name} has logged in for {user.login_attempts} times")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"{user.first_name} has logged in for {user.login_attempts} times")
print()

user.reset_login_attempts()
print(f"{user.first_name} has logged in for {user.login_attempts} time")
