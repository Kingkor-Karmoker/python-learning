# code for problem 7.10:
dream_vacation ={}
messages = "Whats your name?: "
message2 = "If you could visit one place in the world, where would you go?: "

active = True
while active:
    name = input(messages)
    place = input(message2)

    dream_vacation[name] = place
    repeat = input("would you like to repeat the dream vacation? yes/no: ")
    if repeat.lower() == "no":
        active = False

print('\n')
print("Persons name and their favourite place:")
for key, values in dream_vacation.items():
    print(f"{key}: {values}")
