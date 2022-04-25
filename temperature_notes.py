# Richard Weaver
# KNMI temperature

# first import and open the right files
def read_file(File):
    open_file = open(File)
    data = open_file.read().splitlines()
    # open_file.close()
    without_spaces = []
    for line in data:
        without_spaces.append(line.replace(" ", ""))
    temperatures_list = get_temperatures(without_spaces)
    dates_list = get_dates(without_spaces)
    return dates_list, temperatures_list

# make two definitions for the temperatures and dates
def get_temperatures(i):
    temperatures_list = []
    for element in range(19, len(i)):
        splitted = i[element].split(",")
        temperatures_list.append(float(splitted[3]) / 10)
    return temperatures_list

# second function
def get_dates(n):
    dates_list = []
    for element in range(19,len(n)):
            splitted = n[element].split(",")
            dates_list.append(splitted[2])
    return dates_list

# get dates
def get_datetime(date):
    list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    year = date[:4]
    month = date[4:6]
    day = date[6:8]

    month_name = list_of_months[int(month) - 1]
    date_string = day + ' ' + month_name + ' ' + year
    return str(date_string)

# read files
max_dates, max_temperatures = read_file('DeBiltTempMaxOLD.txt')
min_dates, min_temperatures = read_file('DeBiltTempMinOLD.txt')

# set the highest and lowest temperature
def get_highest_temp(max_dates, max_temperatures):
    count = 0
    t_max = max_temperatures[0]
    while count < len(max_temperatures):
        if (max_temperatures[count]) > (t_max):

            # date is same as count
            t_max = (max_temperatures[count])
            date_count = count
        count += 1

    date_max = get_datetime(max_dates[date_count])
    return date_max, t_max

def get_lowest_temp(min_dates, min_temperatures):
    count = 0
    t_min = min_temperatures[0]
    while count < len(min_temperatures):
        if (min_temperatures[count]) < (t_min):
        # save lowest values
            t_min = (min_temperatures[count])
        # the count of the date is the same as the count of the place of min temperature
            min_date_count = count
        count += 1

    date_min = get_datetime(min_dates[min_date_count])
    return date_min, t_min


highest_temp_date, highest_temp = get_highest_temp(max_dates, max_temperatures)
lowest_temp_date, lowest_temp = get_lowest_temp(min_dates, min_temperatures)

print(f'The highest temperature was {highest_temp} degrees Celsius and was measured at {highest_temp_date}.')
print(f'The lowest temperature was {lowest_temp} degrees Celsius and was measured at {lowest_temp_date}.')

# freezing definition
def get_longest_freezing(filename) :
    streak_list = []
    index_list = []
    streak = 0
    i = 0

    for element in filename :
        if element < 0.0 :
            streak += 1
        else :
            streak_list.append(streak)
            streak = 0
            index_list.append(i)
        i += 1

    highest_streak = streak_list[0]
    i = 0
    index = 0
    for element in streak_list :
        if element > highest_streak :
            highest_streak = element
            index = i
        i += 1
    count = index_list[index]
    return highest_streak, max_dates[count-1]

longest_streak, last_streakday = get_longest_freezing(max_temperatures)
print(f'the longest streak of freezing temperatures was {longest_streak} days and the  last day of this streak was {get_datetime(last_streakday)}.')

# go on with making a function wich defines the sunny and tropical years
def sunny_tropical():

    # Open te right files, read data from line 19 for important information
    input_1 = open('DeBiltTempMaxOLD.txt')
    filename = input_1.readlines()[19:]

    # make lists for counts of summer, tropical, years, etc.
    summer_days = []
    tropical_days = []
    years_count = []
    amount_of_tropical_days = 0
    amount_of_summer_days = 0

    start_year = 1901

    # clean and split data
    for read_line in filename:

        seperate_data = read_line.split(',')

        max_temperature = float(seperate_data[3])

        date_of_max = seperate_data[2]
        year_summer_days = date_of_max[0:4]

        year_summer_days = float(year_summer_days)

        # only apply to certain temperatures, because +30 degrees is tropical summerday
        if 250 <= max_temperature <= 300:
            amount_of_summer_days += 1
        elif 300 <= max_temperature:
            amount_of_tropical_days += 1

        if year_summer_days > start_year:
            years_count.append(start_year)
            start_year = year_summer_days

            # append the days to the right list
            summer_days.append(amount_of_summer_days)
            tropical_days.append(amount_of_tropical_days)

            amount_of_summer_days = 0
            amount_of_tropical_days = 0

    return(summer_days, tropical_days, years_count)
    input_1.close()
# set equal to the function, because you need to "aanroepen, sorry weet engelse woord niet" the function
summer_days, tropical_days, years_count = sunny_tropical()

# import math statements for the bar statement
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.bar(years_count, summer_days)
plt.bar(years_count, tropical_days)

plt.xlim([1901, 2015])
plt.ylim([0, 50])

plt.xlabel('Years')
plt.ylabel('Amount of days')
plt.savefig("plot_temp_SDandTD.png")

def heat_wave_year():
    input_1 = open('DeBiltTempMaxOLD.txt')
    filename = input_1.readlines()[19:]

    # find variables counting the different days/year
    year_count = 0
    count_hot_days = 0
    extreme_count = 0
    first_year = []

    # split data again and float data needed
    for read_line in filename:
        seperate_data = read_line.split(',')
        max_temperature = float(int(seperate_data[3])/10)
        max_data = seperate_data[2]
        heat_wave_first_year = max_data[0:4]

        if 25 <= max_temperature:
            count_hot_days += 1
        if max_temperature >= 30:
            extreme_count += 1

        # set when the heat wave applies
        if count_hot_days == 5 and extreme_count == 3 and year_count == 0:
            # append the first found year of heatwave
            first_year.append(heat_wave_first_year)

            count_hot_days = 0
            extreme_count = 0
            year_count = 1

        if max_temperature < 25:

            count_hot_days = 0
            extreme_count = 0

    return first_year
    input_1.close()

# output, the function
print(f'The heatwave was first in {heat_wave_year()}')