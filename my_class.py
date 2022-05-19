## my_class.py
students = ["Michele", "Diana", "Maria", "Ralph", "Jacobus"]
grades = {"Ralph": 4,"Diana": 8, "Jordi": 7, "Michele": 5}

## Exercise 2:
# grades["Gretel"] = 9

## Exercise 3:
# student_search = str(input("Please enter a student name -> "))
# for name in grades:
#     if student_search in grades:
#         print(f"{student_search} is a student in this class, and has the grade: {grades[student_search]}.")
#     else:
#         print(f"{student_search} is not a student in this class.")
#     break

"""Exercise 4 - Write a loop that looks up each student from the lists in my_class and prints “[name]: [grade]” on a new line for each student.
 If the student doesn’t exist in my_class it should print the text “n/a” for the grade. Epected Output:
 Michele: 5
Diana: 8
Maria: n/a
Ralph: 4
Jacobus: n/a"""

## Exercise 4 with "if" statement:
# for name in students:
#     if name in grades:
#         print(f"{name} : {grades[name]}")
#     elif name not in grades:
#         print(f"{name} : n/a")

## Exercise 4 with ".get" statement:
for name in students:
    grading = grades.get(name, "n/a")
    print(f"{name} : {grading}")
