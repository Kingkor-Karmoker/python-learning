# code for problem 10.2:
#from file_reader.py(book page 187):
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
print('')

path2 = Path('pi_million_digits.txt')
contents2 = path2.read_text()

pi_string = ''
for line in contents2.splitlines():
    pi_string += line.strip()

print(f'pi_string: {pi_string[:50]}')
print(len(pi_string))
