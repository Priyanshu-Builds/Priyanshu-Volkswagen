import math

def circle(r):
    print("Area:", math.pi * r * r)
    print("Perimeter:", 2 * math.pi * r)

def square(a):
    print("Area:", a * a)
    print("Perimeter:", 4 * a)

def rectangle(l, b):
    print("Area:", l * b)
    print("Perimeter:", 2 * (l + b))

print("1. Circle\n2. Square\n3. Rectangle")
choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    circle(r)

elif choice == 2:
    a = float(input("Enter side: "))
    square(a)

elif choice == 3:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    rectangle(l, b)