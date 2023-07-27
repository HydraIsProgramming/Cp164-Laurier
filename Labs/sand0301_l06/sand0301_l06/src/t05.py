"""
------------------------------------------------------------------------
CP164 Lab 06, Task 05
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

print(new_list.peek())

print()
print(new_list.remove(foods[5]))
