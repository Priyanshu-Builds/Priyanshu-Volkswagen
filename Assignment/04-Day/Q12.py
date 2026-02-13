n = int(input("How many numbers do you want to enter? => "))
numbers = []

for i in range(n):
    numbers.append(int(input(f"Enter number {i+1}: ")))

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency of numbers is:", freq)