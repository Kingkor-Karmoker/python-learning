# code for problem 10.6:
prompt = "Enter 2 numbers\n"
prompt += "(If you want to quit enter q): \n"

while True:
    num1 = input(prompt)
    num2 = input(prompt)

    if num1 == 'q' or num2 == 'q':
        break

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Please enter numbers only")

    else:
        result = num1 + num2
        print(result)
