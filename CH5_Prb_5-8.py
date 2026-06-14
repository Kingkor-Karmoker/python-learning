# code for problem 5.8:
usernames = ['Admin', 'Kingkor', 'admin', 'Wasik', 'Shaily', 'Shakib', 'Deep']

for username in usernames:
        if username.lower() == 'admin':
            print(f"Hello {username} would you like to see status report?")
        else:
            print(f"greetings {username} thank you for logging in again")
