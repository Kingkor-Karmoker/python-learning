# code for problem 10.5:
from pathlib import Path
path = Path('guest_book.txt')

promt = "What is your name? (To exit type exit): "

names = []
flag = True
while flag:
    name = input(promt)
    if name == 'exit':
        flag = False
    else:
        names.append(name)
        print(f"{name}, we are adding your name to our list.")
        print("Thank you for your time!")

guesst_book = ''
for n in names:
    guesst_book += f'{n}\n'

path.write_text(guesst_book)
