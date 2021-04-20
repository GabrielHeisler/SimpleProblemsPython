
#03 - Modify the previous program such that only the users Alice and Bob are greeted with their names.

print("Please, insert your name:")
name = input()
if name.lower() == "alice" or name.lower() == "bob":
    print("Welcome,", name)
