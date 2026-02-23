# Demonstrates defining a main function

def main():
    input_value = input("Enter your name: ")
    hello(input_value)

def hello(name):
    print(f"Hello, {name}!")

main()