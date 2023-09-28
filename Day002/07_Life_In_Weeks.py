current_age = input("What is your age? ")
current_age_int = int(current_age)

years_left = 90 - current_age_int
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365


print(f"Your have only {months_left} month, {weeks_left} weeks and {days_left} days left.")