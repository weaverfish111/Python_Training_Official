### plotting graph - "f(x) = x(squared)"
### between x = 0 to x = 1.5 (steps of 0.01) use blue line
### plot the minimum of function with red dot

import numpy as np
import math
import matplotlib.pyplot as plt

list_x = []
list_y = []
list_xmin = []
my=0
mx=0

# Create x and y lists
for x in np.arange(0, 1.5, 0.01):
    list_x.append(x)
    y=x**x
    list_y.append(y)

# Create min points for x and y by working out min position in list_y
for i in range(len(list_y)):
    if list_y[i]<list_y[my]:
        my=i
ymin = round(list_y [my], 2)
xmin = list_x [my]
print(f"(xmin, ymin) = ({xmin}, {ymin})")

# Now create the graph
plt.plot(list_x, list_y, 'b-')
plt.plot(xmin, ymin, 'ro')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.text(0.2, 1.6, "(xmin, ymin) = (0.37, 0.69)", color = 'black', fontsize = 15)
plt.show()












# mx=0
# for i in range(len(list_x)):
#     if list_x[i]<list_x[mx]:
#         mx=i
# print(mx)
# xmin = list_x [mx]
# print(xmin)



# ymin_list = sorted(list_y, key=float)
# ymin = ymin_list[0]
# print(ymin)

# for x in list_y:
#     while x <= list_y:
#         xmin = x
#         print(xmin)



# for min in list_y:
#     if min < list_y:
#        minimum = number


# print(list_y)


# for y in np.arange(0.6, 2.0, 0.01):
#     list_y.append(y)

    # if y >=0:
    #     y_cubed = list_y ** 2
    #     list_ycubed.append(y_cubed)


# print(list_x)
# print(list_ycubed)


    # store the data in lists
    # list_x.append(x)
    # list_y.append(y)

