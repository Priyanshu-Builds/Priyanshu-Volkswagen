import random

print("!! Welcome to the Number Guessing Game!!")

secret_number = random.randint(1, 100)
attempts = 8

for i in range(attempts):
    guess = int(input(f"Attempt {i+1} - Enter your guess (1 to 100): "))
    
    if guess > secret_number:
        print("Too high! Try a smaller number.")
    
    elif guess < secret_number:
        print("Too low! Try a larger number.")
    
    else:
        print("Congratulations! You guessed the correct number.")
        break

else:
    print("You used all attempts. The correct number was:", secret_number)