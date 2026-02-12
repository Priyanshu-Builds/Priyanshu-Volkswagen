import random
import string

print("!!----------------------------------------- Secure Password Generator -----------------------------------------!!")

length = int(input("Enter password length you want (minimum 8 recommended): "))

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*"

password = [
    random.choice(upper),
    random.choice(lower),
    random.choice(digits),
    random.choice(special)
]

all_chars = upper + lower + digits + special
for i in range(length - 4):
    password.append(random.choice(all_chars))

random.shuffle(password)

final_password = "".join(password)

print("\nYour secure password has been generated!")
print("Generated Password:", final_password)


print("\n!!----------------------------------------- CAPTCHA Verification -----------------------------------------!!")

captcha = "".join(random.choices(string.ascii_letters + string.digits, k=6))

print("CAPTCHA:", captcha)

user_input = input("Please type the CAPTCHA exactly as shown above: ")

if user_input == captcha:
    print("Verification successful! Access granted.")
else:
    print("Incorrect CAPTCHA! Please run the program again and try again!.")