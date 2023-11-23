import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
		   "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
		   "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "?", "$", "#", "&"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many LETTERS would you like in your password? "))
nr_numbers = int(input("How many NUMBERS would you like in your password? "))
nr_symbols = int(input("How many SYMBOLS would you like in your password? "))


for l in range(nr_letters):
	print(random.choice(letters))
for n in range(nr_numbers):
	print(random.choice(numbers))
for s in range(nr_symbols):
	print(random.choice(symbols))

# shuffle the generated l n s
pw_generated =
