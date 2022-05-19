## dict_complexity.py

from time import time
from random import randint

# create a list or dictionary containing n items
list = []
dict = {}

# test speed
iterations = 100000
start = time()
# for _ in range(iterations):
for n in range(iterations):
    entry = randint(0,1000)
    list.append(entry)
    dict[n] = entry
    # print(dict)
	# TODO: enter code to test

end = time()
print(f'The time elapsed: {end-start:.2f} seconds (with {iterations} iterations)')