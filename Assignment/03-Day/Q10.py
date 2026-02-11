my_tuple = (1, 2, 3, 4, 2, 5, 3, 6)

value = int(input("Enter the number you want to check in the tuple: "))

count = my_tuple.count(value)

if count > 1:
    print("The number is repeated", count, "times in the tuple.")
elif count == 1:
    print("The number appears only once in the tuple.")
else:
    print("The number is not present in the tuple.")