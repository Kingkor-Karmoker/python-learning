# code for problem 10.12:
# code combined of 10.11:

from pathlib import Path
import json

path = Path('favourite_number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favourite number, it is: {number}")

else:
    number = int(input("What is your favourite number?\n:"))

    path = Path('favourite_number.json')
    contents = json.dumps(number)
    path.write_text(contents)

    print(f"We will remember your number: {number}")
