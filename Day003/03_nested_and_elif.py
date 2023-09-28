print("Welcome to the ticket shop!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Fine, that's enough to ride.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket costs $5.")
    elif age <= 18:
        print("Your ticket costs $7.")
    else:
        print("Your ticket costs $12.")
else:
    print("You are too small, you can't ride")