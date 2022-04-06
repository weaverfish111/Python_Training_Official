## Monopoly.py
## Richard Weaver
## 18/03/2022


import random
import matplotlib.pyplot as plt	

from turtle import position

def throw_two_dice():
    double = 0
    min_val = 1
    max_val = 6
    dice_1 = random.randint(min_val, max_val)
    dice_2 = random.randint(min_val, max_val)
    roll = dice_1 + dice_2
    # print(f"throw = {roll}")
    # print(f"The Total Value of the Dice Roll Was {roll}")
    if dice_1 == dice_2:
        # print("A Double Has Been Thrown!")
        double = 1
    return(roll)

def simulate_monopoly(starting_money_p1, starting_money_p2):
    throw = 0
    position_p1 = 0
    position_p2 = 0
    positions = [0, 0]
    # starting_money_1 = 1500
    # starting_money_2 = 1500
    properties_left = 28

    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]
    possessions_p1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    possessions_p2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

    # completed_list = list(range(40))    

    ## While looped actioning simulation
    while properties_left != 0: 
        throw += 1
        
        position_p1 += throw_two_dice()
        position_p2 += throw_two_dice()
        positions[0] = position_p1
        positions[1] = position_p2
        print(positions)
        # print(position_p2)
        ## If function for going past 'GO' (if over 40 minus 40)
        if position_p1 >= 40:
            starting_money_p1 += 200
            position_p1 = position_p1 - 40

        if position_p2 >= 40:
            starting_money_p2 += 200
            position_p2 = position_p2 - 40
        
        ## If function for landing on position (buy or carry on)
        if board_values[position_p1] > 0 and possessions_p1[position_p1] == 0 and starting_money_p1 > board_values[position_p1] and possessions not in :
            possessions_p1[position_p1] = board_values[position_p1]
            starting_money_p1 -= board_values[position_p1]
            # print("Property Bought!")
            properties_left -= 1

        if board_values[position_p2] > 0 and possessions_p2[position_p2] == 0 and starting_money_p2 > board_values[position_p2]:
            possessions_p2[position_p2] = board_values[position_p2]
            starting_money_p2 -= board_values[position_p2]
            # print("Property Bought!")
            properties_left -= 1


            print(starting_money_p1)
            print(starting_money_p2)
            print(possessions_p1)
            print(possessions_p2)


            # print(f"Number of properties left = {properties_left}")

        # if possessions == board_values:
            # print("done")
        
        # print(f"On Throw {throw} the Position is {position} (Value = {position_value})")
        # print(len(position_list))
        # print(position_list)
        # print(completed_list)
        
        # delta = possession_count_p1 - possession_count_p2      ## Delta is the advantage of P1 vs P2
    return()

def simulate_monopoly_games(total_games, starting_money):
    number_of_throws_for_completion = []
    total_throws = 0
    for game in range(0, total_games):
        number_of_throws = simulate_monopoly(starting_money)
        number_of_throws_for_completion.append(number_of_throws)
        number_of_throws_for_completion.sort()
        total_throws += number_of_throws 
    average_throws = total_throws / total_games

## Histogram Graph showing Number of Turns
    # plt.hist(number_of_throws_for_completion)
    # plt.title(f'Histogram showing Number of Turns taken in {total_games} Games of Monopoly')
    # plt.xlabel('Number Of Turns Taken')
    # plt.ylabel('Number of Games')
    # plt.text(average_throws, max,max)
    # plt.show()
    return(average_throws)


def finding_average_throws():
    average_num_throws_list = []
    starting_money_list = []
    starting_money = 3000
    for starting_money in range (0, 3001, 500):
        average_throws = simulate_monopoly_games(2500, starting_money)
        average_num_throws_list.append(average_throws)
        starting_money_list.append(starting_money)
        print(f"Monopoly simulator: 1 player, {starting_money} euros starting money, 2500 games It took an average of {average_throws} throws for the player to collect all streets")

    x = starting_money_list
    y = average_num_throws_list
    plt.plot(x, y, 'r-')
    plt.title(f'Histogram showing Average Number of Turns taken in Games of Monopoly')
    plt.xlabel('Starting Money')
    plt.ylabel('Average Number of Throws')
    # plt.text(average_throws, max,max)
    plt.show()
    return()



### DRIVER CODE

# print(simulate_monopoly_games(1, 3000))
# number_of_throws = simulate_monopoly(4000)
# print(finding_average_throws())
print(simulate_monopoly(1500, 1500))