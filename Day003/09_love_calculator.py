print("Welcome to the love calculator!")
print("You need to fill in the full name to see if it is true love.")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combined_names = name1 + name2


t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or(score > 90):
    print(f"fYour score is {score}%, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}%, you are alright together.")
else:
    print(f"Your score is {score}%.")
