# code for problem 10.11:
from pathlib import Path
import json

number = int(input("What is your favourite number?\n:"))

path = Path('favourite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print(f"We will remember your number: {number}")
