def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

n1 = int(input("Enter number of elements for first list: "))
list1 = []
for i in range(n1):
    list1.append(input(f"Enter element {i+1} for first list: "))

n2 = int(input("Enter number of elements for second list: "))
list2 = []
for i in range(n2):
    list2.append(input(f"Enter element {i+1} for second list: "))

print("First list:", list1)
print("Second list:", list2)

if overlapping(list1, list2):
    print("Both lists have at least one common element.")
else:
    print("No common elements found in the lists.")