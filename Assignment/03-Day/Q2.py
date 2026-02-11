n = int(input("How many items do you want to add in the list? => "))
my_list = []

for i in range(n):
    value = input(f"Enter item {i+1}: ")
    my_list.append(value)

print("The list you entered is:", my_list)
print("Alternate elements from the list are:", my_list[::2])