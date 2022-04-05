
##museum
user_input = input('What is your age? ')
student_discount = input('Are you a student (y/[n])? -> ')
age = int(user_input)

if age < 12:
    print("Free entrance!")
elif age < 18 or age >= 65 or student_discount == "y" or student_discount == "yes":
    print("You receive a discount at the museum.")

else:
    print("No discount.")

