print("Welcome to the ticket shop!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Fine, that's enough to ride.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket costs $5.")
    elif age <= 18:
        bill = 7
        print("Teen ticket costs $7.")
    else:
        bill = 12
        print("Adult ticket costs $12.")
    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is: {bill}")

else:
    print("You are too small, you can't ride")