# Demonstrates defining a function with a parameter with a default value

def hello(name="World"):
    print(f"Hello, {name}!")

hello()
name=input("Enter your name (or press Enter for default): ")
hello(name)