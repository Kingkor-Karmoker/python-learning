#Chapter 3 problem 3.9:
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

#code for prb 3.9:
print(len(persons))
