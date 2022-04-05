## Random Walk
## Richard Weaver
## 15/03/2022

import math
import numpy as np
import matplotlib.pyplot as plt
import random

# Setting Variables
x1_coordinates = []
x2_coordinates = []
y1_coordinates = []
y2_coordinates = []
steps = 200
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# For Loops for 200 steps:
for steps in range(0, 200, 1):
    Radius = 1
    angle1 = random.randint(0, 360)
    angle2 = random.randint(0, 360)
    
    # Calculating coordinates (trig)
    x1 = x1 + math.cos(angle1) * Radius
    y1 = y1 + math.sin(angle1) * Radius
    x1_coordinates.append(x1)
    y1_coordinates.append(y1)
    x2 = x2 + math.cos(angle2) * Radius
    y2 = y2 + math.sin(angle2) * Radius
    x2_coordinates.append(x2)
    y2_coordinates.append(y2)

    # Creating variable for each person tracking
    person1 = x1, x2
    person2 = y1, y2

    # print(f"person 1 coord = {person1}")
    # print(f"person 2 coord = {person2}")
    
    ## Plotting Graph
    plt.plot(x1, y1, 'bo', markersize = 10)  # blue point
    plt.plot(x2, y2, 'go', markersize = 10)  # green point
    plt.plot(x1_coordinates, y1_coordinates, 'b-') #blue line
    plt.plot(x2_coordinates, y2_coordinates, 'g-') #green line
    plt.plot(person1, person2, 'r-')
    
    plt.plot
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)

    # plt.text
    plt.title('Two Drunk Students')
    plt.text(-18,-18, f"steps = {steps}/200")

    # update graph
    plt.draw()
    plt.pause(0.001)

    # clear graph
    plt.clf()


#### THE VARIOUS NOTES AND SCRAPS I DONE MADE:
  # person_1 = x1_coordinates, y1_coordinates
    # person_2 = x2_coordinates, y2_coordinates

    # connectpoints(x1_coordinates,y1_coordinates,0,1)
    # connectpoints(x2_coordinates,y2_coordinates,2,3)    

# for steps in range(0, 200, 1):
#     Radius = 1
#     angle = random.randint(0, 360)

    

    # print(x1, y1)


## Thinks to ask Iris: When each step is taken, the point traves in a random 360 degree direction, 1 radius (1 Integer).
## Am I right in creating a for loop around the angle? Or should I be creating a for loop which cycles through steps (0, 200, 1)?
## Have I created the random angle in the correct way? (# angle = random.randint(0, 360))
## The radius has to be an integer, but does the angle have to be?

## Things I know: I have to log the position after each step, this coordinate is then used in the process of creating a new coordinate.
## So I'll have to use both the angle and radius in the process of creating a new coordinate.
## x and y will have to be be worked out seperately

### WAIT! imagine a circle around the coordinate point with a radius of 1 in all directions. The next coordinate has to on the circumstrance.
### Does that mean I need Pi? Nah, I don't think so, because I've already got the radius.





