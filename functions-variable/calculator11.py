# Demonstrates defining a function with a return value

def main():
    x=float(input("Enter a number: "))
    print(f"The square of {x} is {square(x)}")

def square(n):
    return n*n

main()