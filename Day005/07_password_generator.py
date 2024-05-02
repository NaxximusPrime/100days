import string
import random

letters = string.ascii_letters
numbers = string.digits
symbols = ["!", "?", "$", "#", "&"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many LETTERS would you like in your password? "))
nr_numbers = int(input("How many NUMBERS would you like in your password? "))
nr_symbols = int(input("How many SYMBOLS would you like in your password? "))

password_list = []

for l in range(nr_letters):
    password_list.append(random.choice(letters))

for n in range(nr_numbers):
    password_list.append(random.choice(numbers))

for s in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

pw_generated = "".join(password_list)

print(f"Your password is: {pw_generated}")
