"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 03
------------------------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2022-05-23"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, calories_by_origin

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

avg = calories_by_origin(foods, 2)

print(f"Average Calories: {avg}")