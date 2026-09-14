# code for problem 10.4:
from pathlib import Path

path = Path('guesst.txt')

promt = "Whats your name?: "
name = input(promt)

path.write_text(name)
