student_heights = input("Give me some heights in cm: ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
	total_height += height
print(f"The total height is: {total_height}")

number_of_students = 0
for number in student_heights:
	number_of_students += 1
print(f"The number of students is: {number_of_students}")

average_height = 0
for average in student_heights:
	average_height = total_height // number_of_students
print(f"The average height of the students is: {average_height}")
