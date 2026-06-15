# code for problem 5.10:
current_users = ['Kingkor', 'Wasik', 'Shaily', 'Deep', 'Shakib']
new_users = [ 'Mustafiz', 'Shakib', 'Dipto', 'Munim', 'Deep']
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user} name is already taken")
    else:
        print(f"great the name {new_user} is available ")
