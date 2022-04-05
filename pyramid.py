# Mario Pyramid - Richard Weaver 
# (11/02/22)

height=0
row=0
block = "# "
spaces = "  "

# User input for height value
height = int(input("What height should the pyramid be? -> "))
while height < 1 or height > 23:
    # print("Invalid Height: Please provide a new height")
    height = int(input("What height should the pyramid be? -> "))

# Creating Pyramid with nested for loops
for row in range (height):
    height-=1
    row+=1
    print(spaces * (height), end=block * (row))
    for row in range (height):
        row+=1
        print(block*row)
        break
print("#")





















# height=0
# row=0
# block = "# "
# spaces = "  "

# height = int(input("What height should the pyramid be? -> "))
# while height < 1 or height > 23:
#     print("Invalid Height: Please provide a new height")
#     height = int(input("What height should the pyramid be? -> "))
#     # height -=1
#     # row +=1

# for i in range (1, row):
#     num = 1
#     for j in range (1,-1):
#         print(spaces)
#         height -=1
#         if height == row:
#             print(end=block)
#         # elif height


    # row+=1
    # print(spaces * (height), end=block * (row+1))
    # print("")
    # for row in range (height:
    #     print(spaces)
    #     row+=1
    
    
#     for row in range (height):
#         row+=1
#         print(block*row)
#         break
# print("#")

    # , end=block)
    # for row in range (height):
    #     height-=1
# print(end=block)

    #     print(block*height)
    # print(row)
    # print(spaces * (height-1))
    # print(block*row)
    # for height in range (height):
    #     height -=1
    #     row +=1
    #     print(end = block)



    # for row in range (height):

   
    # print(end = block)
    # for row in range (height):
    #     row+=1
    #     print(end= (block))
    
    # for row in range (row):
    #     print(block)


    # print(end=block)
    # for height in range(height): 
    #     print(end = block)
    
    
    # row+=1
    # print(block * row)
    # for height in range(0, height):
    #     print(end= spaces * height)















# print(row)
# print(height)
##space characters before block = (height) - (row)!!!
# for height in range(1,height):
    # row+=1
    
    
    # print(spaces)
    # for row in range (height):
    #     print(block)
    # print(spaces, end="")
    # print(block)
    


    # print(space * 8, end="")
    # print(block * 2)
    # print(space * height, end=" ")
    # print(block)
    # for row in range (height+1):
    #     print(block)
    # print(block)

##spaces = (height*2) - (row*2) 



###This seems to be a solution for it...:
# for width in range(height):
#     space = " " * (height - width)
#     block = (width + 1) * "#"
#     print(space+block)



    # print(" " * (height - 1)), # Print spaces precluding hashes
    # print(" #" * (height + 2)) # Two hashes for start of pyramid    
    # height -= 1 # Subtracts one space for every iteration


    # print(" " * (height+1)
        
    #     block*height)
    # for width in range (0,height+1):
    #     print(f" {block}")
   
    
    # for height in range (0,height):
    #     print(space * height)
    # for width in range (0,height):
    #     height +=1





    # for height in range(0,height+1):
    #     print(" ")
    # for width in range(0,height+1):
    #     print("done")


    # for width in range(1,24):
    #     print(space)
    # if height > width:
    #     break
    # for width in range (1, height):
    #     print("done")
    # for width in range(1, height):
    #     print(block * width)
#         print(width * block)
    # for width in range (1,24)
    #     height += 1
    #     width += 1
    #     print(block * block)
    
      

    # for height in range (1,24):
    #     print(block * width)


    # pyramid += 1
    # for width in range (1,height):
    #     print(block * width)

# if height < max_blocks and height >= 0:
#     pyramid = block * height
# print(pyramid)







    # print(height)
    # if height > max_blocks:
    #     print("Invalid Height: Please provide a new height")
    # else:
    #     print(block)
    #     break


# height = int(input("What height should the pyramid be? -> "))
# if height > max_blocks or height <= min_blocks:
#     print("Invalid Height: Please provide a new height")
#     height = int(input("What height should the pyramid be? -> "))
#     break
# else:
#     print(height)


# # while blocks  0:
# #     print(blocks)

# # if blocks > max_blocks or blocks < min_blocks:
# #     print("no")







# blocks = "# "
# 

# if 0 < x < 23:
#     print(x)
# x = input("What height should the pyramid be? -> ")

# if input > 23:
#     print("invalid height")
#     print(height_input)
# while height_input in range (0, 23):
#     blocks += 1
#     print(blocks * height_input)