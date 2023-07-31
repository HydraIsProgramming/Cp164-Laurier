"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 05
------------------------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2022-05-23"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, food_table, food_search

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

result = food_search(foods, 11, 0, False)

food_table(result)