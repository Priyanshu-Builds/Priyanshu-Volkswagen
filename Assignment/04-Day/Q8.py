start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("FizzBuzz output using WHILE loop:")

num = start

while num <= end:
    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    
    elif num % 3 == 0:
        print("Fizz")
    
    elif num % 5 == 0:
        print("Buzz")
    
    else:
        print(num)
    
    num += 1