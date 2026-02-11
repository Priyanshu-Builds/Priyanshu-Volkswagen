num = [2, 3, 4, 5, 2, 6, 3, 2]
new_list = []

for i in num:
    if i not in new_list:
        new_list.append(i)

print("Result:", new_list, " => New list")