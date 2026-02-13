lst = [1, 2, 3, 4]
tup = (5, 6, 7, 8)

result = list(map(str, lst + list(tup)))

print("Converted list of strings:", result)