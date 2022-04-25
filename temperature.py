## Richard Weaver
## Temperature Assignment
## 07/04/2022

## Import Libraries Section
import matplotlib
import matplotlib.pyplot as plt

## Function for reading and unpacking raw data from files
def read_data(filename):
    data_without_spaces = []
    with open(filename) as opened_file:
        data = opened_file.read().splitlines()  
        # For Loop removing spaces in between lines
    for line in data:
        data_without_spaces.append(line.replace(" ", ""))
    # print(data_without_spaces[19])

    # Creating seperate lists for data to be added into:
    temperature_list = get_temperatures(data_without_spaces)
    date_list = get_dates(data_without_spaces)
    return(date_list, temperature_list)

## Function for getting temperature data from big data file
def get_temperatures(i):
    # Tempreture is 3rd value in each line [3]
    temperature_list = []
    # Weather Data starts from line 19
    for value in range(19, len(i)):
        splitted = i[value].split(",")
        # Convert temperatire into correct form
        temp_in_celcius = float(splitted[3]) / 10
        temperature_list.append(temp_in_celcius)
    return(temperature_list)

## Function for getting date data from big data file
def get_dates(n):
    # Date is 2nd value in each line [2]
    date_list = []
    # Weather Data starts from line 19
    for value in range(19,len(n)):
        splitted = n[value].split(",")
        date_list.append(splitted[2])
    return(date_list)

# FUnction returning Dates in correct format
def correct_date(date):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Slice up the list items to return: year, month, day 
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    # Minus 1 because list starts at 0 not 1!!!
    month_name = month_list[int(month) - 1]
    date_string = day + ' ' + month_name + ' ' + year
    return str(date_string)

## READ THE TWO FILES (there's two files so you have to read seperately u plonker -.-):
max_dates, max_temperatures = read_data('DeBiltTempMaxOLD.txt')
min_dates, min_temperatures = read_data('DeBiltTempMinOLD.txt')


## Function returning highest temperature
def get_highest_temp(max_dates, max_temperatures):
    count = 0
    t_max = max_temperatures[0]
    while count < len(max_temperatures):
        if (max_temperatures[count]) > (t_max):

            # date is same as count
            t_max = (max_temperatures[count])
            date_count = count
        count += 1

    date_max = correct_date(max_dates[date_count])
    return(date_max, t_max)

## FUnction returning lowest temperature
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

    date_min = correct_date(min_dates[min_date_count])
    return(date_min, t_min)

## Call the functions to return highest temps and date when they were highest
highest_temp_date, highest_temp = get_highest_temp(max_dates, max_temperatures)
lowest_temp_date, lowest_temp = get_lowest_temp(min_dates, min_temperatures)

## Print the final results:
print(f'The highest temperature was {highest_temp} degrees Celsius and was measured at {highest_temp_date}.')
print(f'The lowest temperature was {lowest_temp} degrees Celsius and was measured at {lowest_temp_date}.')


## Function to find longest cold streak:
def get_longest_freezing(filename) :
    cold_streak_list = []
    index_list = []
    streak = 0
    i = 0
## For loop filtering through file to find streaks of < 0 Celcius:
    for value in filename :
        if value < 0 :
            streak += 1
        else :
            cold_streak_list.append(streak)
            streak = 0
            index_list.append(i)
        i += 1       ### You can use an index list to track the place of cold streak in file!!!
 
## Now set the highest streak by filtering through the cold_streak_list (for loop)!!
### You can't sort list because it messes up the index order for max_dates variable
    highest_cold_streak = cold_streak_list[0]  
    i = 0
    index = 0
    for value in cold_streak_list:
        if value > highest_cold_streak:
            highest_cold_streak = value
            index = i
        i += 1
    date_count = index_list[index]
    return(highest_cold_streak, max_dates[date_count-1])

# print(get_longest_freezing(max_temperatures))
longest_cold_streak, last_day_of_streak = get_longest_freezing(max_temperatures)
print(f'the longest streak of freezing temperatures was {longest_cold_streak} days and the final day when this streak ended was {correct_date(last_day_of_streak)}.')


###Now we start with Tropical!
def tropical_and_sunny():

    # Open the file and start reading data from line 19 onwards:
    tropical_sunny_raw_data = open('DeBiltTempMaxOLD.txt')
    tropical_sunny_data = tropical_sunny_raw_data.readlines()[19:]

    # make lists for counts of summer, tropical, years, etc.
    summer_days = []
    tropical_days = []
    years_list = []
    number_of_tropical_days = 0
    number_of_summer_days = 0
    start_year = 1901

## Use For Loop to split up and clean data:
    for read_line in tropical_sunny_data:
        hot_data = read_line.split(',')
        max_temperatures = float(hot_data[3])   # Needs to be float!
        date_of_max_temp = hot_data[2]
        year_summer_days = date_of_max_temp[0:4]
        year_summer_days = float(year_summer_days)

    ## Only temperatures over 30 degrees Celcius are classed as "Tropical"
        if 250 <= max_temperatures <= 300:
            number_of_summer_days += 1
        elif 300 <= max_temperatures:
            number_of_tropical_days += 1
        
    ## Create new lists for tropical and sunny days
        if year_summer_days > start_year:
            years_list.append(start_year)
            start_year = year_summer_days
            
            summer_days.append(number_of_summer_days)
            tropical_days.append(number_of_tropical_days)
            
            # U need to reset the tracked variables to make sure the bar chart replots
            number_of_summer_days = 0
            number_of_tropical_days = 0
    return(summer_days, tropical_days, years_list)

## call the function to assign the variables for the bar chart! 
#(stop making variables and not using them afterwards u fool)
summer_days, tropical_days, years_list = tropical_and_sunny()

## Now plot a Barchart using these variables to show number of summer and tropical days:
plt.bar(years_list, summer_days)
plt.bar(years_list, tropical_days)
plt.xlabel('Year')
plt.ylabel('Quantity of Days')
plt.xlim([1901, 2015])
plt.ylim([0, 50])
plt.legend("ts")
plt.show()

### Final function - Heatwave

def heat_wave_year():
    heatwave_raw_data = open('DeBiltTempMaxOLD.txt')
    heatwave_data = heatwave_raw_data.readlines()[19:]

    # set variables counting the different days/year of weather data
    year_count = 0
    summer_days = 0
    tropical_days = 0
    heatwave_year = []
    for read_line in heatwave_data:
        seperated_data = read_line.split(',')
        max_temperature = float(int(seperated_data[3])/10)   #Remember to divide by 10 because of Celcius
        max_data = seperated_data[2]
        heat_wave_first_year = max_data[0:4]
        if max_temperature >= 25:
            summer_days += 1
        if max_temperature >= 30:
            tropical_days += 1
        
        # set when the heatwave applies (5 Summer Days + 3 Tropical Days!!)
        if summer_days == 5 and tropical_days == 3 and year_count == 0:
            # create new list for year when first heatwave was recorded
            heatwave_year.append(heat_wave_first_year)
            # reset variables (because it didn't like it last time)
            summer_days = 0
            tropical_days = 0
            year_count = 1
        if max_temperature < 25:
            summer_days = 0
            tropical_days = 0

## Converting the returned heatwave year into a string so it doesn't look as ugly as a print statement
    heatwave_string = ' '.join([str(item) for item in heatwave_year])
    return(heatwave_string)
print(f'The first Dutch heatwave was in {(heat_wave_year())}')




## Omg this one took me ages, I'm glad I don't have to look at weather data anymore...
## sweet release
## now time to enjoy the sunshine!
