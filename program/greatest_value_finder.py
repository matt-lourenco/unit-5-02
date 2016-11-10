# Created on 9 Nov 2016
# Created by: Matthew Lourenco
# This is a program that finds the largest value in an array.

from copy import deepcopy
from numpy import random

def find_greatest(array):
    greatest_value = float(0)
    for index in array:
        if greatest_value < index:
            greatest_value = index
    return greatest_value

my_array = []
for random_generation in range(0, random.randint(1, 11)):
    my_array.append(random.randint(1, 26))
print(my_array)
print(find_greatest(my_array))
