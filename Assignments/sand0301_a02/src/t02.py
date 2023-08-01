"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 02
------------------------------------------------------------------------
Author:  Name
ID:      ID
Email:   Email
__updated__ = "2022-05-23"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, average_calories

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

avg = average_calories(foods)

print(f"Average Calories: {avg}")
