# code for problem 6.7:
# code below copied from problem 6.1:
person = {
    'First_name': 'Tahsin',
    'Last_name': 'Deep',
    'Age': 24,
    'City': 'Dhaka'
}

# from here new code starts for problem 6.7:
person_1 = {
    'First_name': 'wasik',
    'Last_name': 'billah',
    'Age': 25,
    'City': 'Bogra'
}

person_2 ={
    'First_name': 'Shaily',
    'Last_name': 'saha',
    'Age': 23,
    'City': 'Narsingdi'
}

people = []
people.append(person)
people.append(person_1)
people.append(person_2)

for details in people:
    print("details are")
    for n, d in details.items():
        print(f"{n}: {d}")
    print('\n')