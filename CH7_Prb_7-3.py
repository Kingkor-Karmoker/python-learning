# code for problem 7.3:
message = "Enter a number : "
number = int(input(message))

if number % 10 == 0:
    print(f"Your number is {number} and its multiple of 10.")
else:
    print(f"Your number {number} is not multiple of 10")
