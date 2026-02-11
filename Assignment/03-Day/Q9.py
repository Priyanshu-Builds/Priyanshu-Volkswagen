list1 = ["Hello ", "Hai "]
list2 = ["Bye", "Byeeeeeeeee"]

result = [i + j for i in list1 for j in list2]

print("After combining both lists, we get:")
print(result)