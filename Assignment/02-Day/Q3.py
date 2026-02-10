number = int(input("Enter 4 digit number: "))

if number < 1000 or number > 9999:
    print("!! Enter a valid 4 digit number !!")
else:
    n1 = number // 1000
    n2 = (number // 100) % 10
    n3 = (number // 10) % 10
    n4 = number % 10

    print("\nFace Value:")
    print(n1, n2, n3, n4)

    print("\nPlace Value:")
    print(f"{number} = {n1}000 + {n2}00 + {n3}0 + {n4}")

    reverse = n4*1000 + n3*100 + n2*10 + n1
    print("\nReverse numberber:", reverse)