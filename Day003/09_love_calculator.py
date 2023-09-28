print("Welcome to the love calculator!")
print("You need to fill in the full name to see if it is true love.")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

true = name1.count("t") + name2.count("t")
true = name1.count("r") + name2.count("r")
true = name1.count("u") + name2.count("u")
true = name1.count("e") + name2.count("e")

love = name1.count("l") + name2.count("l")
love = name1.count("o") + name2.count("o")
love = name1.count("v") + name2.count("v")
love = name1.count("e") + name2.count("e")

print(f"Your lovescore is: {true}{love}%")