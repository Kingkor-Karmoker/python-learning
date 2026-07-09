# code for problem 8.3:
def make_shirt(size, text):
    print(f"Shirt size: {size}")
    print(f'The message "{text}" will be printed on the shirt. \n')

# calling the function using positional arguments:
make_shirt(32, 'King')

# calling the function using keyword arguments:
make_shirt(size= 38, text='Happy')
