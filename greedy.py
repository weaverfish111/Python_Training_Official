# Greedy Algorithm
# Richard Weaver
# 15/02/2022

coin = 0
deno_list = [25, 10, 5, 1]
coin_count = 0
coin_returned = 0


num = float(input("How much change is owed? -> "))
while num < 0:
    num = float(input("How much change is owed? -> "))
int_num = num * 100

twofive = 0
ten = 0
five = 0 
one = 0
all = 0
while int_num > 0:
    for coin in deno_list:
        coin_count = int_num // coin #finding how many demonination go into input
        remainder = int_num % coin #finding remainder after highest denomination has been subtracted
        int_num = remainder #change num for next iteration in loop
        if coin == 25:
            # print(f"The current 0.25 is {twofive + coin_count}")
            all = twofive + coin_count
        if coin == 10:
            # print(f"The current 0.10 is {ten + coin_count}")
            all += ten + coin_count
        if coin == 5:
            # print(f"The current 0.05 is {five + coin_count}")
            all += five + coin_count
        if coin == 1:
            # print(f"The current 0.01 is {one + coin_count}")
            all += one + coin_count
        if coin == 0:
            int_num = 0

print (int(all))
        ## testing the variables for each iteration ## 
        # print(f"The current denomination is {coin}")
        # print(f"The number of times denomination goes into num is {coin_count}")
        # print(f"The remaining amount left over is {remainder}")
