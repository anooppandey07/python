# Strips string before comparing

input=input("Do you agree? ").strip()
if input == "yes":
    print("You agreed.")
else:
    print("You disagreed.") 