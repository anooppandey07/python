# Lowercases string before comparing

input=input("Do you agree? ").strip().lower()
if input == "yes":
    print("You agreed.")
else:
    print("You disagreed.")
    