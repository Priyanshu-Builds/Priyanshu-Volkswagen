n = int(input("How many numbers do you want to enter? => "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The biggest number from the list is:", largest)