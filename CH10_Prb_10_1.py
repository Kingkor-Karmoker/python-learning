# code for problem 10.1:
from pathlib import Path
path = Path('Learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
