print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $ "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

final_bill = bill / people * tip_percent / 100 + (bill / people)

final_bill_str = round(final_bill, 2)
print(f"Each person should pay: ${final_bill_str}")
