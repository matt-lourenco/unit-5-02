# Created on 9 Nov 2016
# Created by: Matthew Lourenco
# This is a program that finds the largest value in an array.

from copy import deepcopy

def find_greatest(array):
    greatest_value = float(0)
    for index in array:
        if greatest_value < index:
            greatest_value = index
    return greatest_value

my_array = [13, 17, 5, 23, 9]
print(find_greatest(my_array))
