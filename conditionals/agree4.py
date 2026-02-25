# Compares multiple strings

input=input("Do you agree? ").strip().lower()
if input.startswith("y"):
    print("You agreed.")
else:
    print("You disagreed.")