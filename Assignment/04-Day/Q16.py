n = int(input("How many numbers you want to enter? => "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter number {i+1}: ")))

result = list(map(lambda x: x * 2, nums))

print("Numbers after doubling:", result)