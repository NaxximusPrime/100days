import random
print("Let's through a coin!")

coin = random.randint(0, 1)

if coin == 1:
	print("Heads")
else:
	print("Tails")