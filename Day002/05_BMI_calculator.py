weight = input("What is your weight in kg? ")
height = input("What is your height in m? ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print("Your BMI is: " + str(bmi_as_int))
