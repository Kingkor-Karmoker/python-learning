# code for problem 10.7:
# modifying code of 10.5:
from pathlib import Path

path = Path('number_book.txt')

prompt = "What is your number? (To exit type exit): "

num = []
while True:
    numb = input(prompt)
    if numb == 'exit':
        break

    try:
       numb = int(numb)
    except ValueError:
        pass

    else:
        num.append(numb)
        print(f"{numb}, we are adding your number to our list.")
        print("Thank you for your time!")

number_book = ''
for n in num:
    number_book += f'{n}\n'

path.write_text(number_book)

contents = path.read_text()
print(contents)
