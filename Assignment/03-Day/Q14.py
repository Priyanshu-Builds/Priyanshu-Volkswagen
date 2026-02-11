def histogram(numbers):
    for num in numbers:
        print("*" * num)

n = int(input("How many numbers do you want to enter? =>"))
numbers = []

for i in range(n):
    numbers.append(int(input(f"Enter number {i+1}: ")))

print("Histogram looks like this:")
histogram(numbers)