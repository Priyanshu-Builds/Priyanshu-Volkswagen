print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Select choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter Celsius temperature: "))
    fahrenheit = (celsius * 1.8) + 32
    print("Fahrenheit Temperature =", fahrenheit,"F")

elif choice == 2:
    fahrenheit = float(input("Enter Fahrenheit temperature: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Celsius Temperature =", celsius,"C")

else:
    print("!! Choose the correct choice !!")