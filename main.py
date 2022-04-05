##Lucas solution to pyramid

row = 0
height = int(input("What height should the pyramid be? -> "))
while height < 1 or height > 23:
    print("Invalid Height: Please provide a new height")
    height = int(input("What height should the pyramid be? -> "))

for i in range(1, height+1):
    num = 1
    for j in range(height, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print("# ", end="")
            num += 1
    print('#')


# rows = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, rows+1):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print("_", end="_")
#         else:
#             print("# ", end="")
#             num += 1
#     print('')