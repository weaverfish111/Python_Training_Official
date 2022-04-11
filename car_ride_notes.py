# Richard Weaver
# Write a program that processes data from a car ride

# import the data needed
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import statistics

data_list = []
with open("CarRideData.csv", encoding="utf8") as car_data:
     data_list = car_data.read().splitlines()
data_list.pop(0)

# make lists using append and split data
kmhspeed_list = []
speed_list = []
time_list = []
longitude_list = []
latitude_list = []

for line in data_list:
    split_data = line.split(',')

    # append time using int, making it a number instead of a string
    time = (split_data[0])
    time_list.append(time)

    # append the numbers using 'float', which appends including the comma
    speed = float(split_data[6])
    speed_list.append((speed))

    # make a seperate one for kmh, for the red or green line later on
    kmhspeed = float(split_data[6])
    kmhspeed_list.append((kmhspeed)* 3.6)

    # append the right splitted data from data in longitude and latitude lists
    longitude = float(split_data[4])
    longitude_list.append(longitude)
    latitude = float(split_data[3])
    latitude_list.append(latitude)

# plot the details like steps, title and color of the line, situated below
plt.xticks([0,180,360,540,720,900])
plt.title("Speed of the car")
plt.plot(time_list, speed_list, 'b-')

# add labels to the axes
plt.xlabel('Time (s)', fontsize = 13)
plt.ylabel('Speed (km/h)', fontsize = 13)
plt.savefig('plot_speedandtime.png')
plt.clf()

# make a list
mean_speed = statistics.mean(speed_list)
distance = (mean_speed * len(time_list))/1000
print(distance)

# make lists for function that will make the route in the graph
longitude_red = []
latitude_red = []
longitude_green = []
latitude_green = []

# define a red line for speeds lower than 50 kmh and green for speeds higher than 50 kmh
for count in range(len(data_list)):
    if kmhspeed_list[count] < 50:
        longitude_red.append(longitude_list[count])
        latitude_red.append(latitude_list[count])


    else:
        longitude_green.append(longitude_list[count])
        latitude_green.append(latitude_list[count])

# plot details for red_or_green_line() like steps
plt.xlim([4.83, 4.97])
plt.ylim([52.32, 52.36])

# add labels to the axes
plt.xlabel('Longitude', fontsize = 13)
plt.ylabel('Latitude', fontsize = 13)

plt.plot(longitude_red, latitude_red,'ro', markersize=1.6)
plt.plot(longitude_green, latitude_green,'go', markersize=1.6)

# plot out and save the function
plt.savefig("plot_route.png")
