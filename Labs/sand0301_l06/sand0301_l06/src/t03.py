"""
------------------------------------------------------------------------
CP164 Lab 06, Task 04
------------------------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2023-06-20"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List


file_variable = open("food.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

for value in foods:
    new_list.append(value)

print(new_list.find(foods[1]))

print(new_list.index(foods[1]))

print(foods[1] in new_list)
