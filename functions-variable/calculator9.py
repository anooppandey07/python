# Demonstrates rounding after the decimal point

x=float(input("Enter a number: "))
y=float(input("Enter another number: "))
z=x/y
print(f"{z:.2f}")  
print(round(z, 2))
