# def half(val):
#     z = val/2
#     return(z)
    
# x = 4
# y = 3
# a = half(x)
# b = half(y)

# print(a, b)

# def mean(a, b):
#     c = (a + b) / 2
#     return(c)

# x = mean(4, 6)
# print(x)


## working out max of two (and 3) variables!!!
# def max(a, b):
#     if a < b:
#         return b
#     else:
#         return a

# def maxx(a, b, c):
#     if c < max(a, b):
#         return(max(a, b))
#     else:
#         return c

# x = 4
# y = 18
# z = 16
# z1 = max(x, y)
# z2 = max(y, x)
# z3 = maxx(x, y, z)

# print(z3)


# Sum of list
def my_sum(lst):
    e = sum(lst)
    return(e)

my_list = [1,2,3,5]
s = my_sum(my_list)
print(s)


## Their solution:
# def my_sum(lst):
#     acc = 0
#     for number in lst:
#         acc += number
#     return acc

# my_list = [1,2,3,4]
# s = my_sum(my_list)
# print(s)

