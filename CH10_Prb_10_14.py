# code for problem 10.14:
from pathlib import Path
import json
# from book:
def get_stored_username(path):
    if path.exists():
        content = path.read_text()
        username = json.loads(content)
        return username
    else:
        return None

def get_new_username(path):
    username = input("Please enter your username: ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Is this correct?{username} (y/n): ")
        if correct.lower() == "y":
            print(f"Greetings, you are now logged in!{username}")
        else:
            username = get_new_username(path)
            print(f"We will remember you, {username}")
    else:
        username = get_new_username(path)
        print(f"We will remember you, {username}")

greet_user()
