n = int(input("Enter number of elements for the list: "))
my_list = []

for i in range(n):
    value = input(f"Enter element {i+1}: ")
    my_list.append(value)

print("Original list is:", my_list)

if 'b' in my_list:
    index = my_list.index('b')
    my_list[index:index+1] = [1, 2, 3]
    print("After replacing 'b' with [1,2,3], new list becomes:", my_list)
else:
    print("'b' is not present in the list.")