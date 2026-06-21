# code for problem 6.8:
pet = {
    'kind': 'dog',
    'pet name': 'kiku',
    'owner': 'wasik'
}

pet1 = {
    'kind': 'cat',
    'pet name': 'lalu',
    'owner': 'deep'
}

pet2 = {
    'kind': 'Bird',
    'pet name': 'Moina',
    'owner': 'Shaily'
}

pet3 = {
    'kind': 'cat',
    'pet name': 'tota',
    'owner': 'Kingkor'
}

pets = []
pets.append(pet)
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)
# I could directly store the dictionaries in list

for p in pets:
    print("About pets:")
    for k, v in p.items():
        print(f"{k.title()}: {v.title()}")
    print('\n')
