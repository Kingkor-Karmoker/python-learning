# code for problem 6.10:
# code from problem 6.2 (modified for 6.10):
numbers = {
    'Kingkor': [99, 45, 7],
    'Deep': [69, 17, 33],
    'Wasik': [62, 69],
    'Shaily': [9],
    'Shakib': [19, 49, 11, 66]
}

for n, f in numbers.items():
    print(f"Persons name is: {n}")
    print(f"{n}'s favourite numbers are:")
    for ns in f:
        print(f"\t{ns}")
    print('\n')