# code for problem 10.8:
from pathlib import Path

files = ['cats.txt', 'dogs.txt']

for file in files:
    path = Path(file)

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'{file} not found')

    else:
        print(contents)
