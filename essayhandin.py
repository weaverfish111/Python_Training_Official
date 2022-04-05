from wsgiref.validate import InputWrapper

# Code BY Richard Weaver
#07/02/2022

name = input("Please Enter Your Name Here -> ")
print("Hello", name)
seat_count = input("How many seats should be reserved? -> ")
seat_count = int(seat_count)
print(seat_count)