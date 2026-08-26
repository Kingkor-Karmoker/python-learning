# code for problem 10.2:
from pathlib import Path
path = Path('Learning_python.txt')
contents = path.read_text()
print(contents)
messages = contents.splitlines()

for message in messages:
    message = message.replace('Python', 'Java')
    print(message)
