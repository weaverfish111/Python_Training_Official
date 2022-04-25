# Richard Weaver
# Write a program that processes data from a car ride

# import the data needed
import matplotlib
import matplotlib.pyplot as plt
import statistics

data_list = []
## Create overall list variable for each Car_Data
# Person online says use 'with' statement to open and process file to iterate over data (more subjective) [https://peps.python.org/pep-0343/].
with open("CarRideData.csv") as car_data:
    data_list = car_data.read().splitlines()
data_list.pop(0)
print(data_list[0]) 

### 0=time, 1= timestamp, 3=latitude, 4=longitude, 6=speed
### ..... The rest I've honestly got no clue on... don't think u need them Rich


# make lists using .append and split data
kmphspeed_list = []
car_speed_list = []
time_list = []
longitudes_list = []
latitudes_list = []

## Split up each line
for line in data_list:
    data_value = line.split(',')

    # Add the 'Time' to a list and make it an int
    time = (data_value[0])
    time_list.append(time)

    # append the numbers using 'float'
    speed = float(data_value[6])
    car_speed_list.append((speed))

    # make a seperate one for kmh to input into graph later on!!
    kmphspeed = float(data_value[6])
    kmphspeed_list.append((kmphspeed)* 3.6)

    # Unpack Longitude and Latitude, and add them to lists!
    longitude = float(data_value[4])
    longitudes_list.append(longitude)
    latitude = float(data_value[3])
    latitudes_list.append(latitude)

# plot the details like steps, title and color of the line, situated below
plt.title("The Speed of the car")
plt.plot(time_list, car_speed_list, 'g-')

# add labels to the axes
plt.xlabel('Time in Seconds', fontsize = 16)
plt.ylabel('Speed In Kilometers Per Hour', fontsize = 16)
plt.show()

# make a list for the average speed and print distance travelled
mean_speed = statistics.mean(car_speed_list)
distance = (mean_speed * len(time_list))/1000
print(distance)

# make lists for function that will make the route in the graph
longitude_slow = []
latitude_slow = []
longitude_fast = []
latitude_fast = []

## Creating argument for red line (slower than 50) and green line (faster than 50)
for car in range(len(data_list)):
    if kmphspeed_list[car] < 50:
        longitude_slow.append(longitudes_list[car])
        latitude_slow.append(latitudes_list[car])
    else:
        longitude_fast.append(longitudes_list[car])
        latitude_fast.append(latitudes_list[car])

## plot details for red_or_green_line() like I did for steps in student!
plt.xlim([4.83, 4.97])
plt.ylim([52.32, 52.36])

# add labels to the axes
plt.xlabel('Longitude', fontsize = 13)
plt.ylabel('Latitude', fontsize = 13)

plt.plot(longitude_slow, latitude_slow,'ro', markersize=1.6)
plt.plot(longitude_fast, latitude_fast,'go', markersize=1.6)

# plot and print the graph
plt.show()


