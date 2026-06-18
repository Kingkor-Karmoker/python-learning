# code for problem 6.5:
major_rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'Mississippi': 'United states'
}

for r, c in major_rivers.items():
    print(f"The {r} runs through {c}")

print("\nThe names of each rivers are:")
for r in major_rivers.keys():
    print('\t'+r)

print("\nThe names of each countries are:")
for c in major_rivers.values():
    print(f'\t{c}')
