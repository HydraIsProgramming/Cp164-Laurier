"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 02
------------------------------------------------------------------------
Author:  Ranjot Sandhu
ID:      169020301
Email:   sand0301@mylaurier.ca
__updated__ = "2022-05-23"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, average_calories

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

avg = average_calories(foods)

print(f"Average Calories: {avg}")