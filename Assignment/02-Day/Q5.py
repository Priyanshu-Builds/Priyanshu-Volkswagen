def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

n1 = float(input("Enter First Number: "))
n2 = float(input("Enter Second Number: "))
n3 = float(input("Enter Third Number: "))

result = find_maximum(n1, n2, n3)
print("Maximum Among The Numbers =>", result)