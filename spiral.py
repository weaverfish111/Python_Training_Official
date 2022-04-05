## spiral.py
## Richard Weaver
## 15/03/2022


import math
import numpy as np
import matplotlib.pyplot as plt

Radius = 10
x_coordinates = []
y_coordinates = []
for angle in np.arange(0, 20, 0.1):
    Radius -= 0.05
    x = math.cos(angle) * Radius
    y = math.sin(angle) * Radius
   
    
    # x = angle * np.cos(angle)
    # y = angle * np.sin(angle)
    
    # Radius_x = math.cos(angle)
    # Radius_y = math.sin(angle)

    # Radius = math.sin(angle) * math.cos(angle) [WRONG]

## But I need to calculate the angle... using sin and cos...?
## question: is it angle from the centre or angle from the previous point??
## The angle is increasing, The Radius is getting smaller!
# ## Does Pi have to be used because it's a circlar shape?

    # plotting graph
    plt.title('Spiral')
    plt.plot(x, y, 'bo', markersize = 10)  # blue point
    plt.plot
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # update graph
    plt.draw()
    plt.pause(0.001)

    # clear graph
plt.clf()







# import numpy as np 
# import matplotlib.pyplot as plt 
# import matplotlib.cm as cm 

# n = 256
# angle = np.linspace(0,12*2*np.pi, n)
# radius = np.linspace(.5,1.,n)

# x = radius * np.cos(angle)
# y = radius * np.sin(angle)

# plt.scatter(x,y,c = angle, cmap = cm.hsv)
# plt.show()

