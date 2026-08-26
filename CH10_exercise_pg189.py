# code for exercise practice on page 189:
from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday =input("Enter your birthday in this format(ddmmyy): ")
if birthday in pi_string:
    print("Yes your birthday num exist in pi numbers")
else:
    print("No, your birthday num does not exist in pi numbers")
