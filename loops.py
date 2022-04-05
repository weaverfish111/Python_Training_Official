##for loop algorithm:

# total = 0
# maximum = 10
# for x in range(1, maximum):
#     print(f"x now has the value {x}")
#     total = total + x
#     print(f"The sum of all numbers from 1 to {x} = {total}")
# print(f"The sum of all numbers from 1 to {maximum} = {total}")

##while loops instead of for loop algorithm:

# total = 0
# maximum = 10
# x = 1
# while x < 10:
#     print(f"x now has the value {x}")
#     total = total + x 
#     print(f"The sum of all numbers from 1 to {x} = {total}")
#     x+=1
# print(f"The sum of all numbers from 1 to {maximum} = {total}")

## while loop algorithm for total rather than x:

# total = 0
# maximum = 10
# x = 1
# while total <= 20:
#     print(f"x now has the value {x}")
#     total = total + x
#     print(f"The sum of all numbers from 1 to {x} = {total}")
#     x += 1

# print(f"The sum of all numbers from 1 to {maximum} = {total}")

##for loop which counts divisibles of 3:

# x = 0
# for number in range(1, 20):
#     if number > 15:
#         print(f"This number is bigger than 15: {number}")
#     if number % 3 == 0:
#         x+=1
#         print(f"This number is exactly divisible by 3: {number}")
# print(f"From the numbers 1 to 20 there are {x} numbers that are exactly divisible by 3.")

##nested for loop printing value x at end of 1st loop:

for x in range(1, 6):
   for y in range(1, 4):
       print(f"x = {x}, y = {y}")
       if y >= 3:
        print(f"The value of x is now {x} and we have just finished the loop over y")

### THEIR SOLUTION:
# for x in range(1, 6):
#     for y in range(1, 4):
#         print(f"x = {x}, y = {y}")
#     print(f"The value of x is now {x} and we have just finished the loop over y")

## nested loop to have y variable run to x in for loop:
# for x in range(1, 6):
#    for y in range(1, x+1):
#        if y <= x:
#         print(f"x = {x}, y = {y}")
#    print(f"The value of x is now {x} and we have just finished the loop over y")
