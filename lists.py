#lists

# list = ["banana", 10.9, 2, "fruit", 42]
# print(list[0])
# print(list[4])
# list [2] = "Hello"
# print(list[2])

# list = ["1kg apples", "100g sugar", "1 tsp cinnamon", "1 lemon", "300g flour", "1 tsp baking powder"]
# for list in list:
#     print(list)

# num_list = [0]
# for list in range(1,31):
#     num_list.append(list)
#     print(list)
#     print(num_list)

# list = [9, 10, 11, 12]
# sum = 0

# for list in list:
#     sum += list
# print(sum)


# numbers = [8, 2, 3, 15, 7, 19]
# count = 0
# numbers2 = []
# for number in numbers:
#     if number > 5 and number < 16:
#         numbers2.append(number)
#         count = len(numbers2)

# print(numbers2)
# print(count)

list_div3 = []

n = 123
for list in range(0, n):
    if list % 3 ==0:
        list_div3.append(list)
print(list_div3)
