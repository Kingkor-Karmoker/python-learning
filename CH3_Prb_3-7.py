#code from prb 3.4:
persons = ['Jasmine', 'Sazid', 'Cintiya']
for person in persons:
    print(f"{person},You are invited to Kingkor's dinner party")

#prb 3.6 starts here:
    print(f"{person}, Found a new bigger table for every one,kindly join there")

persons.insert(2, 'Mustafiz')
persons.insert(0,'Riddy')
persons.append('Raian')

print(f"\t new persons list: {persons}")

for per in persons:
    print(f"{per},you are invited to join the new table, thank you")

#Code 3.7 starts from here:
print ("sorry guys Only two person can be invited. See you next time")
p1 = persons.pop(0)
print(f"sorry you are not invited: {p1}")
p2 = persons.pop(2)
print(f"sorry you are not invited: {p2}")
p3 = persons.pop(-1)
print(f"sorry you are not invited: {p3}")
p4 = persons.pop(1)
print(f"sorry you are not invited: {p4}")

for pr in persons:
    print(f"{pr}, you are still invited to dinner")

del persons[0]
del persons[0]

print(f"{persons} empty persons list")