print("Factorial values from 0 to 10 are:\n")

for num in range(0, 11):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "comes out to be", fact)