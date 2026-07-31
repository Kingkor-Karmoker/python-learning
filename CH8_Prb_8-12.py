# code for problem 8.12:
def sandwich(*items):
    print('Creating sandwich with items:')
    for item in items:
        print(f'- {item}')
    print('')

sandwich('Turkey')
sandwich('Ham', 'Cheese')
sandwich('Lettuce', 'Tomato', 'Mayonnaise')
