# code for problem 7.2:
message = "How many people are in your dinner group?"
people = int(input(f"{message}\n: "))

if people > 8:
    print("You'll have to wait for a table to be free")
else:
    print("Your table is ready")
