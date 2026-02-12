def subtract(list1, list2):
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    return result

n1 = int(input("Enter number of elements for the first list: "))
list1 = []
for i in range(n1):
    list1.append(int(input(f"Enter element {i+1} for the first list: ")))

n2 = int(input("Enter number of elements for the second list: "))
list2 = []
for i in range(n2):
    list2.append(int(input(f"Enter element {i+1} for the second list: ")))

print("Elements present only in first list:", subtract(list1, list2))