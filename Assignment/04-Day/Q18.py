text = input("Enter a string: ")

print("A. Characters from even position")
print("B. Characters from odd position")
print("C. Length of string")
print("D. Add 'a' at end of string length times")

choice = input("Enter your choice: ")
choice = choice.upper()

if choice == 'A':
    print("Characters from even positions are:")
    print(text[1::2])

elif choice == 'B':
    print("Characters from odd positions are:")
    print(text[0::2])

elif choice == 'C':
    print("Length of the string is:", len(text))

elif choice == 'D':
    print("Updated string is:")
    print(text + "a" * len(text))

else:
    print("Invalid choice entered.")