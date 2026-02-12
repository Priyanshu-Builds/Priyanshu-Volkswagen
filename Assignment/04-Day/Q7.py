start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("FizzBuzz output using FOR loop: ")

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    
    elif num % 3 == 0:
        print("Fizz")
    
    elif num % 5 == 0:
        print("Buzz")
    
    else:
        print(num)