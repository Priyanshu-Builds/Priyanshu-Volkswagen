def union(list1, list2):
    result = list1.copy()
    for item in list2:
        if item not in result:
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

print("Union of both lists is:", union(list1, list2))