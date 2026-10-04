# code for problem 10.13:
from pathlib import Path
import json
def greet_user():
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)

        print(f"Hello, welcome back: {username['username']}")
        print(f"Your dob: {username['dob']}")
        print(f"Your age: {username['age']}")

    else:
        username = input("What is your name? ")
        dob = input("What is your date of birth? ")
        age = input("What is your age? ")
        user_info = {
            "username": username,
            "dob": dob,
            "age": age
        }
        contents = json.dumps(user_info)
        path.write_text(contents)
        print(f"We will remember you: {username}")

greet_user()
