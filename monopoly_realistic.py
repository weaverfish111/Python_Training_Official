## Monopoly.py
## Richard Weaver
## 18/03/2022


import random
import matplotlib.pyplot as plt	
import numpy as np

## Function simulating the rolling of two dice 
def throw_two_dice():
    double = 0
    min_val = 1
    max_val = 6
    dice_1 = random.randint(min_val, max_val)
    dice_2 = random.randint(min_val, max_val)
    roll = dice_1 + dice_2
    if dice_1 == dice_2:
        # print("A Double Has Been Thrown!")
        double = 1
    return(roll)

## Function simulating a single game of Monopoly
def simulate_monopoly(starting_money_p1, starting_money_p2):
    ## Setting Variables
    throw = 0
    position_p1 = 0
    position_p2 = 0
    positions = [0, 0]
    possession_count_p1 = 0
    possession_count_p2 = 0
    properties_left = 28
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]
    possessions_p1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    possessions_p2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

    ## While Loop actioning the Simulation
    while properties_left != 0: 
        ## Throwing dice and recording postions of two players
        throw += 1
        position_p1 += throw_two_dice()
        position_p2 += throw_two_dice()
        positions[0] = position_p1
        positions[1] = position_p2
        
        ## If function for players going past 'GO' (if over 40 minus 40)
        # Player 1
        if position_p1 >= 40:
            starting_money_p1 += 200
            position_p1 = position_p1 - 40
        
        # Player 2
        if position_p2 >= 40:
            starting_money_p2 += 200
            position_p2 = position_p2 - 40

        ## If function for players landing on position (purchase or continue), counting possessions for each player
        # Player 1
        if board_values[position_p1] > 0 and possessions_p1[position_p1] == 0 and starting_money_p1 > board_values[position_p1] and possessions_p2[position_p1] == 0:
            possessions_p1[position_p1] = board_values[position_p1]
            starting_money_p1 -= board_values[position_p1]
            possession_count_p1 += 1
            properties_left -= 1

        # Player 2
        if board_values[position_p2] > 0 and possessions_p2[position_p2] == 0 and starting_money_p2 > board_values[position_p2] and possessions_p1[position_p2] == 0: 
            possessions_p2[position_p2] = board_values[position_p2]
            starting_money_p2 -= board_values[position_p2]
            possession_count_p2 += 1
            properties_left -= 1

    ## Delta is the advantage of P1 vs P2
    delta = possession_count_p1 - possession_count_p2     
    # print(f"After this game player 1 had {delta} more streets than player 2.")
    return(delta)

## Function simulating numerous games of monopoly to return average delta value for total games
def simulate_monopoly_games(total_games, starting_money_p1, starting_money_p2):
    # number_of_throws_for_completion = []
    # starting_money_p1 = starting_money
    # starting_money_p2 = starting_money
    # total_throws = 0
    total_delta = 0
    for game in range(0, total_games):
        total_delta  += simulate_monopoly(starting_money_p1, starting_money_p2)
    average_delta = total_delta / total_games
    
## Code working out how many Turns it takes to complete the Game of Monopoly!
    #     number_of_throws = simulate_monopoly(starting_money_p1, starting_money_p2)
    #     number_of_throws_for_completion.append(number_of_throws)
    #     number_of_throws_for_completion.sort()
    #     total_throws += number_of_throws 
    # average_throws = total_throws / total_games
    # print(f"Monopoly simulator: two players, {starting_money_p1} euro starting money, {total_games} games On average player 1 has {average_delta} more streets in their possession when all streets have been bought")

## Histogram Graph showing Number of Turns needed to complete Game of Monopoly
    # plt.hist(number_of_throws_for_completion)
    # plt.title(f'Histogram showing Number of Turns taken in {total_games} Games of Monopoly')
    # plt.xlabel('Number Of Turns Taken')
    # plt.ylabel('Number of Games')
    # plt.text(average_throws, max,max)
    # plt.show()
    return(average_delta)

## Function calculating average number of throws to complete monopoly games
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
    plt.show()
    return()

## Function calculating how to resolve disadvantage of P2 being second dice roller to P1
def equilibrium():
    total_games = 10000
    starting_money_p1 = 1500
    starting_money_p2 = 1500
    extra_monies = range(1500,1701, 50)
    delta_list = []
    extra_money_list = []
    ## For Loop varying starting money of P2
    for starting_money_p2 in extra_monies:
        starting_money = [starting_money_p1, starting_money_p2]
        delta_difference = simulate_monopoly_games(total_games, starting_money_p1, starting_money_p2)
        extra_money_count = starting_money_p2 - starting_money_p1
        delta_list.append(delta_difference)
        extra_money_list.append(extra_money_count)
        print(f"Starting money {starting_money}: player 1 on average {delta_difference} more streets (player 2 - {extra_money_count} euros extra)")

## Graph Plotting Delta Difference between two players
    x = extra_money_list
    y = delta_list
    plt.plot(x, y, 'r-')
    plt.axhline(0)
    plt.title(f'Graph Plotting Varying Disadvantage of Player 2 in Games of Monopoly')
    plt.xlabel('Amount of Extra Money for P2')
    plt.ylabel('Delta Difference between P1 and P2')
    plt.show()
    return()

### DRIVER CODE:
print(equilibrium())
# print(simulate_monopoly_games(10000, 1500, 1600))   ### Total Games, Starting Money
# number_of_throws = simulate_monopoly(4000)    
# print(finding_average_throws())
# print(simulate_monopoly(1500, 1500))   ### Starting Money P1, Starting Money P2