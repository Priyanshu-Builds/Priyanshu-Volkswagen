import mod1

start = int(input("Enter 1st Number: "))
end = int(input("Enter Last Number: "))

while True:
    print("\n1 : ODD Numbers")
    print("\n2 : EVEN Numbers")
    print("\n3 : ALL Numbers")
    print("\n4 : Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        mod1.odd_numbers(start, end)

    elif choice == 2:
        mod1.even_numbers(start, end)

    elif choice == 3:
        mod1.all_numbers(start, end)

    elif choice == 4:
        print("!! EXIT !!")
        break

    else:
        print("Select Correct Choice")