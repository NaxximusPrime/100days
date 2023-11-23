import random

game = ["Rock", "Paper", "Scissors"]
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

print("Welcome to Rock, Paper, Scissors!")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 0:
	print("You chose Rock")
	print("Computer chose Rock")
	print("It's a draw")
elif player_choice == 0 and computer_choice == 1:
	print("You chose Rock")
	print("Computer chose Paper")
	print("You loose")
elif player_choice == 0 and computer_choice == 2:
	print("You chose Rock")
	print("Computer chose Scissors")
	print("You win")
elif player_choice == 1 and computer_choice == 0:
	print("You chose Paper")
	print("Computer chose Rock")
	print("You win")
elif player_choice == 1 and computer_choice == 1:
	print("You chose Paper")
	print("Computer chose Paper")
	print("It's a draw")
elif player_choice == 1 and computer_choice == 2:
	print("You chose Paper")
	print("Computer chose Scissors")
	print("You loose")
elif player_choice == 2 and computer_choice == 0:
	print("You chose Scissors")
	print("Computer chose Rock")
	print("You loose")
elif player_choice == 2 and computer_choice == 1:
	print("You chose Scissors")
	print("Computer chose Paper")
	print("You win")
elif player_choice == 2 and computer_choice == 2:
	print("You chose Scissors")
	print("Computer chose Scissors")
	print("It's a draw")
else:
	print("You typed an invalid number and loose.")
