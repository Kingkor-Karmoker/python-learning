# code for problem 10.11(part2):
from pathlib import Path
import json

path = Path('favourite_number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favourite number, it is: {number}")
