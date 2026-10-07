import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
In_letters = int(input("How many letters would you like in your password?\n"))
In_symbols = int(input(f"How many symbols would you like in your password?\n"))
In_numbers = int(input(f"How many numbers would you like in your password?\n"))

# Easy password generation
final = ""
for i in range(0, In_letters ):
    final+=random.choice(letters)
for j in range(0, In_symbols):
     final+=random.choice(symbols)
for k in range(0, In_numbers):
     final +=random.choice(numbers)
print("Your generated password is :-> "+final)

# Tough password generation
password = []
for i in range(0, In_letters ):
    password+=random.choice(letters)
for j in range(0, In_symbols):
    password+=random.choice(symbols)
for k in range(0, In_numbers):
    password +=random.choice(numbers)

random.shuffle(password)
final_password = ""

for last in password:
 final_password+=last
print("Your generated secure password is :-> " + final_password)
