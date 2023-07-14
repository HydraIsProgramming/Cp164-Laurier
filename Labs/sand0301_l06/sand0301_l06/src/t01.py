"""
------------------------------------------------------------------------
CP164 Lab 06, Task 01
------------------------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2023-06-20"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List

file_variable = open("food.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

new_list.append(foods[2])

new_list.prepend(foods[0])

new_list.insert(1, foods[1])

for value in new_list:
    print(value)
    print()