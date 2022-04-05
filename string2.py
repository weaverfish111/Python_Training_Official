# fruit = 'banana'
# backwards = 0
# last = len(fruit)
# index = 0

# for index in fruit:
#     backwards += 1
#     print(fruit[-backwards])

# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in "O,Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
