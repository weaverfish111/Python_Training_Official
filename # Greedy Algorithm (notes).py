# Greedy Algorithm
# Richard Weaver
# 15/02/2022

coin = 0
deno_list = [25, 10, 5, 1]
coin_count = 0
coin_returned = 0
total_coin = 0


num = float(input("How much change is owed? -> "))
int_num = num * 100
# while num < 0
# Greedy Algorithm

twofive = 0
ten = 0
five = 0 
one = 0
all = 0
while int_num >= 0:
    for coin in deno_list:
        coin_count = int(int_num // coin) #finding how many demonination go into input
        remainder = int_num % coin #finding remainder after highest denomination has been subtracted
        int_num = remainder #change num for next iteration in loop
        total_coin = int(sum(coin_count))

        # += wont work because the total number of coins is accumulating over each iteration,
        # not each denomination (replaces each time iterated)

        # if num >= coin:
        #     coin_returned = round(num // coin, 2) #counting number of loops... but needs to be number of times into!
        #     total_coin = coin_returned + coin_returned
        
        print(f"The current denomination is {coin}")
        print(f"The number of times denomination goes into num is {coin_count}")
        print(f"The remaining amount left over is {remainder}")
    break
print (total_coin)